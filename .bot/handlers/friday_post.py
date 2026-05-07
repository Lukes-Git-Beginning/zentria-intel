"""Friday-Report Poll-Loop: liest discord_push_pending.json -> postet Embeds."""
from __future__ import annotations

import asyncio
import json
import logging
import re
from datetime import datetime
from pathlib import Path

import discord
import yaml

log = logging.getLogger("intel-bot.friday")
STATE_DIR = Path("/app/.state")
WEEKLY_DIR = Path("/app/weekly")
POLL_INTERVAL = 30
RATE_LIMIT_BUFFER = 0.5


async def poll_loop(client: discord.Client) -> None:
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            await _check_and_post(client)
        except Exception:
            log.exception("friday_post poll error")
        await asyncio.sleep(POLL_INTERVAL)


async def _check_and_post(client: discord.Client) -> None:
    pending = STATE_DIR / "discord_push_pending.json"
    if not pending.exists():
        return
    # Atomic claim — sofort umbenennen, damit zweite Instanz nicht doppelt postet
    claimed = pending.with_suffix(".json.processing")
    pending.rename(claimed)
    try:
        data = json.loads(claimed.read_text(encoding="utf-8"))
        filename = data.get("filename")
        if not filename:
            log.warning("pending.json ohne 'filename' — verworfen")
            claimed.rename(claimed.with_suffix(".invalid"))
            return
        report_path = WEEKLY_DIR / filename
        if not report_path.exists():
            log.warning("Weekly file not found: %s — restoring pending", report_path)
            claimed.rename(pending)
            return
        insights = parse_weekly_report(report_path)
        channel = _get_channel(client, "friday-report")
        if not channel:
            log.error("Channel #friday-report nicht gefunden")
            claimed.rename(pending)
            return

        from bot import _save_msg_id_map  # type: ignore

        for insight in insights[:5]:
            embed, view = _build_embed_and_view(insight)
            msg = await channel.send(embed=embed, view=view)
            client._msg_id_map[insight["stable_id"]] = msg.id  # type: ignore
            _save_msg_id_map(client)  # sofort persistieren
            await asyncio.sleep(RATE_LIMIT_BUFFER)

        claimed.rename(claimed.with_suffix(".processed"))
        log.info("Posted %d insights from %s", len(insights[:5]), filename)
    except Exception:
        log.exception("Friday-Post error — restoring pending")
        if claimed.exists():
            claimed.rename(pending)


def _get_channel(
    client: discord.Client, name: str
) -> discord.TextChannel | None:
    cache = getattr(client, "_channel_cache", {})
    return cache.get(name)


def _build_embed_and_view(insight: dict) -> tuple[discord.Embed, discord.ui.View]:
    embed = discord.Embed(
        title=f"`{insight['stable_id']}` {insight['title'][:200]}",
        description=insight["body"][:2000],
        color=_trend_color(insight.get("trend_score", 5)),
    )
    embed.add_field(
        name="Module",
        value=", ".join(insight.get("modules", [])) or "—",
        inline=True,
    )
    embed.add_field(
        name="Quellen", value=str(insight.get("n_sources", "?")), inline=True
    )
    embed.add_field(
        name="Trend", value=str(insight.get("trend_score", "?")), inline=True
    )
    embed.set_footer(
        text=f"{insight['stable_id'][:3]} · {datetime.now().strftime('%Y-%m-%d')}"
    )
    view = _build_pick_view(insight["stable_id"])
    return embed, view


def _build_pick_view(stable_id: str) -> discord.ui.View:
    view = discord.ui.View(timeout=None)
    buttons = [
        ("🟢 Keep", "keep", discord.ButtonStyle.success),
        ("🟡 Followup", "followup", discord.ButtonStyle.primary),
        ("🔵 Inspire", "inspire", discord.ButtonStyle.secondary),
        ("🔴 Dismiss", "dismiss", discord.ButtonStyle.danger),
        ("📝 Notiz", "note", discord.ButtonStyle.secondary),
    ]
    for label, action, style in buttons:
        view.add_item(
            discord.ui.Button(
                label=label,
                style=style,
                custom_id=f"pick_{stable_id}_{action}",
            )
        )
    return view


def _trend_color(score: float) -> int:
    if score >= 8:
        return 0xFF4444
    if score >= 6:
        return 0xFFAA00
    return 0x4488FF


def parse_weekly_report(path: Path) -> list[dict]:
    """Parst weekly/*.md, extrahiert Insights mit Stable-ID-Headern (W..-T..-i..)."""
    text = path.read_text(encoding="utf-8")
    _, content = _split_frontmatter(text)
    HEADER_RE = re.compile(
        r"^#{1,3}\s+(W\d+-T\d+-i\d+)[:\s]+(.+?)$", re.MULTILINE
    )
    matches = list(HEADER_RE.finditer(content))
    insights: list[dict] = []
    for i, m in enumerate(matches):
        stable_id, title = m.group(1), m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()
        meta = _extract_inline_meta(body)
        insights.append(
            {
                "stable_id": stable_id,
                "title": title,
                "body": body,
                "modules": meta.get("modules", []),
                "n_sources": meta.get("n_sources", 0),
                "trend_score": meta.get("trend_score", 5),
            }
        )
    return insights


def _split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    return (yaml.safe_load(parts[1]) or {}), parts[2]


def _extract_inline_meta(body: str) -> dict:
    meta: dict = {}
    if m := re.search(r"modules?:\s*\[([^\]]+)\]", body, re.IGNORECASE):
        meta["modules"] = [s.strip() for s in m.group(1).split(",")]
    if m := re.search(r"n_sources?:\s*(\d+)", body, re.IGNORECASE):
        meta["n_sources"] = int(m.group(1))
    if m := re.search(r"trend_score?:\s*([\d.]+)", body, re.IGNORECASE):
        meta["trend_score"] = float(m.group(1))
    return meta
