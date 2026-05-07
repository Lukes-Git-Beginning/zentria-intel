"""Trigger-Watch Poll-Loop + Slash-Command /trigger."""
from __future__ import annotations

import asyncio
import json
import logging
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import discord
import yaml

log = logging.getLogger("intel-bot.trigger")
STATE_DIR = Path("/app/.state")
FOLLOWUPS_DIR = Path("/app/followups")
POLL_INTERVAL = 30

PRIORITY_COLORS = {"high": 0xFF0000, "medium": 0xFFA500, "low": 0xFFFF00}
EVENT_COLORS = {
    "acquisition": 0xFF0000,
    "funding": 0xFF6600,
    "layoff": 0xFF9900,
    "pricing-change": 0xFFCC00,
    "product-launch": 0x00AAFF,
}


async def poll_loop(client: discord.Client) -> None:
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            await _check_and_post(client)
        except Exception:
            log.exception("trigger_watch poll error")
        await asyncio.sleep(POLL_INTERVAL)


async def _check_and_post(client: discord.Client) -> None:
    pending_file = STATE_DIR / "trigger_pending.json"
    if not pending_file.exists():
        return
    try:
        triggers: list[dict] = json.loads(
            pending_file.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError:
        log.warning("trigger_pending.json corrupt — verschoben nach .invalid")
        pending_file.rename(pending_file.with_suffix(".json.invalid"))
        return
    if not triggers:
        # leere Liste -> aufraeumen
        pending_file.rename(pending_file.with_suffix(".json.processed"))
        return
    channel = _get_channel(client, "triggers")
    if not channel:
        log.error("Channel #triggers nicht gefunden")
        return
    user_id = _get_luke_user_id()
    remaining: list[dict] = []
    for trigger in triggers:
        try:
            await _post_trigger(channel, trigger, user_id)
            await asyncio.sleep(0.5)  # rate limit
        except Exception:
            log.exception("Fehler beim Post von Trigger %s", trigger.get("slug"))
            remaining.append(trigger)
    if remaining:
        pending_file.write_text(
            json.dumps(remaining, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    else:
        pending_file.rename(pending_file.with_suffix(".json.processed"))


async def _post_trigger(
    channel: discord.TextChannel, trigger: dict, user_id: str | None
) -> None:
    priority = trigger.get("priority", "medium")
    color = EVENT_COLORS.get(
        trigger.get("event_type", ""),
        PRIORITY_COLORS.get(priority, 0xFFAA00),
    )
    embed = discord.Embed(
        title=f"Trigger: {trigger.get('competitor', '?')} — {trigger.get('event_type', '?')}",
        color=color,
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(
        name="Was ist passiert",
        value=trigger.get("description", "_keine Beschreibung_")[:1024],
        inline=False,
    )
    embed.add_field(
        name="Beruehrt Module",
        value=", ".join(trigger.get("modules", [])) or "—",
        inline=True,
    )
    embed.add_field(
        name="Kurzfristige Aktionen",
        value=trigger.get("actions", "_pruefen_")[:512],
        inline=False,
    )
    slug = trigger.get(
        "slug",
        trigger.get("competitor", "unknown").lower().replace(" ", "-"),
    )
    view = _build_trigger_view(slug)
    content = f"<@{user_id}>" if priority == "high" and user_id else ""
    await channel.send(content=content, embed=embed, view=view)


def _build_trigger_view(slug: str) -> discord.ui.View:
    view = discord.ui.View(timeout=None)
    buttons = [
        ("🚨 Tiefenrecherche", "deep", discord.ButtonStyle.danger),
        ("📌 Auf Friday-Watch", "friday", discord.ButtonStyle.primary),
        ("🟡 Followup 14d", "followup14d", discord.ButtonStyle.secondary),
    ]
    for label, action, style in buttons:
        view.add_item(
            discord.ui.Button(
                label=label,
                style=style,
                custom_id=f"trigger_{action}_{slug}",
            )
        )
    return view


# --- Button-Handler ---


async def handle_trigger_button(
    interaction: discord.Interaction, action: str, slug: str
) -> None:
    """Verarbeitet Button-Clicks aus Trigger-Embeds."""
    await interaction.response.defer(ephemeral=True)
    if action == "deep":
        await _trigger_deep_research(interaction, slug)
    elif action == "friday":
        await _add_to_friday_watch(interaction, slug)
    elif action == "followup14d":
        await _create_trigger_followup(interaction, slug)
    else:
        await interaction.followup.send("Unbekannte Aktion.", ephemeral=True)


# --- Slash-Command ---


async def handle_trigger_slash(
    interaction: discord.Interaction,
    competitor: str,
    event_type: str,
) -> None:
    """Verarbeitet /trigger Slash-Command — schreibt neuen Pending-Entry."""
    slug = competitor.lower().replace(" ", "-")
    entry = {
        "competitor": competitor,
        "event_type": event_type,
        "priority": "high",
        "slug": slug,
        "description": f"Manueller Trigger via Discord: {competitor} / {event_type}",
        "modules": [],
        "actions": "Recherche starten.",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _append_pending(entry)
    await interaction.response.send_message(
        f"Trigger fuer `{competitor}` ({event_type}) in Queue.",
        ephemeral=True,
    )


# --- Helpers ---


async def _trigger_deep_research(
    interaction: discord.Interaction, slug: str
) -> None:
    entry = {
        "competitor": slug,
        "event_type": "deep",
        "priority": "high",
        "slug": slug,
        "description": "Deep-Research-Request via Discord-Button",
        "modules": [],
        "actions": "intel-deep-Routine beim naechsten Trigger ausfuehren.",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _append_pending(entry)
    await interaction.followup.send(
        f"Tiefenrecherche fuer `{slug}` geplant.", ephemeral=True
    )


async def _add_to_friday_watch(
    interaction: discord.Interaction, slug: str
) -> None:
    watch_file = STATE_DIR / "friday_watch.json"
    slugs: list[str] = []
    if watch_file.exists():
        try:
            slugs = json.loads(watch_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            slugs = []
    if slug not in slugs:
        slugs.append(slug)
        watch_file.write_text(
            json.dumps(slugs, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    await interaction.followup.send(
        f"`{slug}` auf Friday-Watch gesetzt.", ephemeral=True
    )


async def _create_trigger_followup(
    interaction: discord.Interaction, slug: str
) -> None:
    due = (datetime.now(timezone.utc) + timedelta(days=14)).strftime("%Y-%m-%d")
    FOLLOWUPS_DIR.mkdir(exist_ok=True)
    filepath = FOLLOWUPS_DIR / f"trigger-{slug}-followup.md"
    fm = {
        "id": f"trigger-{slug}",
        "slug": f"trigger-{slug}-followup",
        "created": date.today().isoformat(),
        "decision": "followup",
        "followup_due": due,
        "modules": [],
        "source": "trigger-watch",
    }
    content = (
        f"---\n{yaml.dump(fm, allow_unicode=True, sort_keys=False)}---\n\n"
        f"Followup aus Trigger-Watch: `{slug}`\n"
    )
    filepath.write_text(content, encoding="utf-8")
    bot = interaction.client  # type: ignore
    await bot._batcher_queue.put(
        (
            str(filepath),
            "followup",
            f"feat(intel): trigger followup {slug}",
        )
    )
    await interaction.followup.send(
        f"Followup +14d fuer `{slug}` erstellt.", ephemeral=True
    )


def _append_pending(entry: dict) -> None:
    pending_file = STATE_DIR / "trigger_pending.json"
    existing: list = []
    if pending_file.exists():
        try:
            existing = json.loads(pending_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = []
    existing.append(entry)
    pending_file.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def _get_channel(
    client: discord.Client, name: str
) -> discord.TextChannel | None:
    return getattr(client, "_channel_cache", {}).get(name)


def _get_luke_user_id() -> str | None:
    return os.environ.get("DISCORD_USER_ID_LUKE")
