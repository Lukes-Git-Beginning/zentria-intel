"""zentria-intel Discord Bot — Entrypoint."""
from __future__ import annotations

import asyncio
import json
import logging
import os
import signal
import sys
import time
from pathlib import Path

import discord
from discord import app_commands
from dotenv import load_dotenv

# .scripts ist ein Punkt-Prefix-Verzeichnis und kann nicht als normales Package
# importiert werden. sys.path-Insert macht state.py / load_settings.py
# direkt als Top-Level-Modul verfuegbar.
sys.path.insert(0, "/app/.scripts")
sys.path.insert(0, "/app/.bot")
from load_settings import load_settings  # noqa: E402

load_dotenv("/app/.env")

REPO_ROOT = Path("/app")
STATE_DIR = REPO_ROOT / ".state"
STATE_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("intel-bot")

settings = load_settings()
BOT_CFG = settings.get("bot", {}) if settings else {}
POLL_INTERVAL = BOT_CFG.get("poll_interval_seconds", 30)
BATCH_WINDOW = BOT_CFG.get("push_batch_window_seconds", 60)
HEARTBEAT_S = BOT_CFG.get("health_heartbeat_seconds", 300)

GUILD_ID = int(os.environ["DISCORD_GUILD_ID"])


class IntelBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.guilds = True
        intents.message_content = False
        super().__init__(
            intents=intents,
            application_id=int(os.environ["DISCORD_APPLICATION_ID"]),
        )
        self.tree = app_commands.CommandTree(self)
        self._channel_cache: dict[str, discord.TextChannel] = {}
        self._msg_id_map: dict[str, int] = {}
        self._batcher_queue: asyncio.Queue = asyncio.Queue()
        self._tasks: list[asyncio.Task] = []

    async def setup_hook(self) -> None:
        _register_slash_commands(self.tree)
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        from handlers import friday_post, trigger_watch, git_batcher

        self._tasks = [
            asyncio.create_task(friday_post.poll_loop(self), name="friday-poll"),
            asyncio.create_task(trigger_watch.poll_loop(self), name="trigger-poll"),
            asyncio.create_task(
                git_batcher.flush_loop(self._batcher_queue, BATCH_WINDOW),
                name="git-batch",
            ),
            asyncio.create_task(_heartbeat_loop(HEARTBEAT_S), name="heartbeat"),
        ]

    async def on_ready(self) -> None:
        guild = self.get_guild(GUILD_ID)
        if guild:
            self._channel_cache = {ch.name: ch for ch in guild.text_channels}
        _load_msg_id_map(self)
        log.info(
            "Bot ready. Guild=%s channels=%d",
            guild and guild.name,
            len(self._channel_cache),
        )

    async def on_interaction(self, interaction: discord.Interaction) -> None:
        # Slash-Commands werden vom CommandTree intern dispatcht — hier NICHT
        # abfangen, sonst werden Slash-Calls doppelt verarbeitet.
        if interaction.type == discord.InteractionType.application_command:
            return
        await _dispatch_component(interaction)

    async def on_error(self, event: str, *args, **kwargs) -> None:
        import traceback

        with (STATE_DIR / "bot_errors.log").open("a", encoding="utf-8") as f:
            f.write(f"\n--- {event} ---\n")
            traceback.print_exc(file=f)
        log.error("Error in %s (logged)", event)


def _register_slash_commands(tree: app_commands.CommandTree) -> None:
    @tree.command(
        name="intel-pick",
        description="Insight picken/followupen/dismissen",
    )
    @app_commands.describe(
        id="Stable-ID z.B. W20-T03-i02",
        action="Aktion",
        tags="Tags komma-separiert (optional)",
        note="Notiz (optional)",
    )
    @app_commands.choices(
        action=[
            app_commands.Choice(name="keep", value="keep"),
            app_commands.Choice(name="followup", value="followup"),
            app_commands.Choice(name="inspire", value="inspire"),
            app_commands.Choice(name="dismiss", value="dismiss"),
        ]
    )
    async def intel_pick(
        interaction: discord.Interaction,
        id: str,
        action: str,
        tags: str = "",
        note: str = "",
    ) -> None:
        from handlers.pick_handler import handle_pick_slash

        await handle_pick_slash(interaction, id, action, tags, note)

    @tree.command(name="trigger", description="Manuellen Competitor-Trigger pushen")
    @app_commands.describe(
        competitor="Competitor-Name",
        event_type="Event-Typ",
    )
    @app_commands.choices(
        event_type=[
            app_commands.Choice(name="funding", value="funding"),
            app_commands.Choice(name="acquisition", value="acquisition"),
            app_commands.Choice(name="layoff", value="layoff"),
            app_commands.Choice(name="pricing-change", value="pricing-change"),
            app_commands.Choice(name="product-launch", value="product-launch"),
        ]
    )
    async def trigger_cmd(
        interaction: discord.Interaction,
        competitor: str,
        event_type: str,
    ) -> None:
        from handlers.trigger_watch import handle_trigger_slash

        await handle_trigger_slash(interaction, competitor, event_type)

    @tree.command(name="intel-status", description="Bot-Status anzeigen")
    async def intel_status(interaction: discord.Interaction) -> None:
        await _handle_status(interaction)


async def _dispatch_component(interaction: discord.Interaction) -> None:
    cid = (interaction.data or {}).get("custom_id", "")
    if cid.startswith("pick_"):
        parts = cid.split("_", 2)
        if len(parts) < 3:
            return
        stable_id, action = parts[1], parts[2]
        from handlers.pick_handler import handle_pick_button

        await handle_pick_button(interaction, stable_id, action)
    elif cid.startswith("trigger_"):
        parts = cid.split("_", 2)
        if len(parts) < 3:
            return
        action, slug = parts[1], parts[2]
        from handlers.trigger_watch import handle_trigger_button

        await handle_trigger_button(interaction, action, slug)
    elif cid.startswith("modal_"):
        from handlers.pick_handler import handle_modal_submit

        await handle_modal_submit(interaction)


async def _handle_status(interaction: discord.Interaction) -> None:
    pending_friday = (STATE_DIR / "discord_push_pending.json").exists()
    pending_triggers: list = []
    t_file = STATE_DIR / "trigger_pending.json"
    if t_file.exists():
        try:
            pending_triggers = json.loads(t_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pending_triggers = []
    bot: IntelBot = interaction.client  # type: ignore
    embed = discord.Embed(title="Intel-Bot Status", color=0x00FF88)
    embed.add_field(name="Friday-Push pending", value=str(pending_friday))
    embed.add_field(name="Trigger-Queue", value=str(len(pending_triggers)))
    embed.add_field(name="Git-Batch-Queue", value=str(bot._batcher_queue.qsize()))
    embed.add_field(name="Channels gecacht", value=str(len(bot._channel_cache)))
    await interaction.response.send_message(embed=embed, ephemeral=True)


async def _heartbeat_loop(interval: int) -> None:
    while True:
        await asyncio.sleep(interval)
        (STATE_DIR / "bot_heartbeat.txt").write_text(
            str(time.time()), encoding="utf-8"
        )
        log.info("Heartbeat OK")


def _load_msg_id_map(bot: IntelBot) -> None:
    p = STATE_DIR / "discord_messages.json"
    if not p.exists():
        return
    try:
        bot._msg_id_map = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        log.warning("discord_messages.json corrupt — startet leer")
        bot._msg_id_map = {}


def _save_msg_id_map(bot: IntelBot) -> None:
    p = STATE_DIR / "discord_messages.json"
    p.write_text(json.dumps(bot._msg_id_map, indent=2), encoding="utf-8")


async def _shutdown(bot: IntelBot) -> None:
    log.info("Shutdown — flushing git batch queue...")
    from handlers.git_batcher import flush_all

    await flush_all(bot._batcher_queue)
    for t in bot._tasks:
        t.cancel()
    await bot.close()


def main() -> None:
    bot = IntelBot()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(
                sig,
                lambda: asyncio.ensure_future(_shutdown(bot), loop=loop),
            )
        except NotImplementedError:
            # Windows-Dev: add_signal_handler nicht verfuegbar
            pass
    loop.run_until_complete(bot.start(os.environ["DISCORD_BOT_TOKEN"]))


if __name__ == "__main__":
    main()
