"""Pick-Handler: Buttons + Slash + Modals + Promotion-Check."""
from __future__ import annotations

import asyncio
import logging
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import discord
import yaml

log = logging.getLogger("intel-bot.pick")
REPO_ROOT = Path("/app")
STATE_DIR = REPO_ROOT / ".state"
WEEKLY_DIR = REPO_ROOT / "weekly"
_INDEX_LOCK = asyncio.Lock()


# --- Public Entry Points ---


async def handle_pick_button(
    interaction: discord.Interaction, stable_id: str, action: str
) -> None:
    """Verarbeitet Button-Klick aus friday_post-Embed."""
    if action == "note":
        await _show_note_modal(interaction, stable_id)
        return
    insight = find_insight_by_id(stable_id)
    if not insight:
        await interaction.response.send_message(
            f"Insight `{stable_id}` nicht gefunden.", ephemeral=True
        )
        return
    if action == "followup":
        await _show_followup_modal(interaction, stable_id, insight)
        return
    await interaction.response.defer(ephemeral=True)
    await _execute_pick(interaction, stable_id, action, insight, note="")
    await _update_embed_buttons(interaction, stable_id, action)


async def handle_pick_slash(
    interaction: discord.Interaction,
    id: str,
    action: str,
    tags: str = "",
    note: str = "",
) -> None:
    """Verarbeitet /intel-pick Slash-Command."""
    insight = find_insight_by_id(id)
    if not insight:
        await interaction.response.send_message(
            f"Insight `{id}` nicht gefunden.", ephemeral=True
        )
        return
    if tags:
        insight.setdefault("tags", []).extend(t.strip() for t in tags.split(","))
    if action == "followup":
        await _show_followup_modal(interaction, id, insight)
        return
    await interaction.response.defer(ephemeral=True)
    await _execute_pick(interaction, id, action, insight, note=note)


async def handle_modal_submit(interaction: discord.Interaction) -> None:
    """Verarbeitet Modal-Submission (Followup-Datum oder Notiz)."""
    cid: str = (interaction.data or {}).get("custom_id", "")
    if cid.startswith("modal_note_"):
        stable_id = cid[len("modal_note_") :]
        note_value = _extract_modal_value(interaction, "note_text")
        await _append_note_to_insight(interaction, stable_id, note_value)
    elif cid.startswith("modal_followup_"):
        stable_id = cid[len("modal_followup_") :]
        custom_date = _extract_modal_value(interaction, "custom_date")
        quick_pick = _extract_modal_value(interaction, "quick_pick")
        due_value = custom_date or quick_pick
        insight = find_insight_by_id(stable_id)
        if not insight:
            await interaction.response.send_message(
                f"Insight `{stable_id}` nicht mehr gefunden.", ephemeral=True
            )
            return
        insight["followup_due"] = _resolve_due_date(due_value)
        await interaction.response.defer(ephemeral=True)
        await _execute_pick(interaction, stable_id, "followup", insight, note="")
        await _update_embed_buttons(interaction, stable_id, "followup")


# --- Core Pick Workflow ---


async def _execute_pick(
    interaction: discord.Interaction,
    stable_id: str,
    action: str,
    insight: dict,
    note: str,
) -> None:
    """Gemeinsamer Core: schreibt File, queued git-batch, updated Index."""
    bot = interaction.client  # type: ignore
    if action == "dismiss":
        try:
            import state  # /app/.scripts/state.py

            state.append_dismissed(stable_id, "discord")
        except Exception:
            log.exception("append_dismissed fehlgeschlagen")
        await interaction.followup.send(
            f"Dismissed `{stable_id}`.", ephemeral=True
        )
        return

    target_dir, index_file = _action_target(action)
    module = (insight.get("modules") or ["cross"])[0]
    week_prefix = (
        stable_id[: stable_id.index("-")] if "-" in stable_id else stable_id[:3]
    )
    slug = slugify(insight.get("title", stable_id), module, week_prefix)
    frontmatter = _build_frontmatter(stable_id, action, insight, note, slug)
    filepath = REPO_ROOT / target_dir / f"{slug}.md"
    filepath.parent.mkdir(exist_ok=True)
    content = (
        f"---\n{yaml.dump(frontmatter, allow_unicode=True, sort_keys=False)}---\n\n"
        f"{insight.get('body', '')}\n"
    )
    filepath.write_text(content, encoding="utf-8")

    commit_msg = f"feat(intel): pick {action} {stable_id} ({slug})"
    await bot._batcher_queue.put((str(filepath), action, commit_msg))

    async with _INDEX_LOCK:
        update_index_file(
            REPO_ROOT / index_file,
            module,
            slug,
            insight.get("title", ""),
            frontmatter,
        )
        await bot._batcher_queue.put(
            (
                str(REPO_ROOT / index_file),
                "index",
                f"chore(intel): index {action} {stable_id}",
            )
        )

    if action == "keep":
        await _check_promotion(interaction, insight)

    await interaction.followup.send(
        f"Picked as **{action}**: `{slug}.md`", ephemeral=True
    )


# --- Helpers ---


def find_insight_by_id(stable_id: str) -> dict | None:
    """Sucht Insight in weekly/*.md, neueste zuerst."""
    from handlers.friday_post import parse_weekly_report

    for md_file in sorted(WEEKLY_DIR.glob("*.md"), reverse=True):
        for ins in parse_weekly_report(md_file):
            if ins["stable_id"] == stable_id:
                return ins
    return None


def slugify(title: str, module: str, week: str) -> str:
    """Erzeugt kebab-case Slug: title-module-week."""
    clean = re.sub(r"[^\w\s-]", "", title.lower())
    clean = re.sub(r"[\s_]+", "-", clean).strip("-")[:50]
    return f"{clean}-{module}-{week}".lower()


def update_index_file(
    index_path: Path,
    module: str,
    slug: str,
    title: str,
    frontmatter: dict,
) -> None:
    """Appended Eintrag unter Modul-Header in KEEPERS.md/FOLLOWUPS.md."""
    text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    target_dir = _action_target_from_index(index_path)
    entry = (
        f"- [{title}]({target_dir}/{slug}.md) — modul:{module} · "
        f"created:{frontmatter.get('created', '')} · "
        f"n_sources:{frontmatter.get('n_sources', '?')}\n"
    )
    header = f"## {module}"
    if header in text:
        pos = text.index(header) + len(header)
        next_section = text.find("\n## ", pos)
        insert_at = next_section if next_section != -1 else len(text)
        text = text[:insert_at] + "\n" + entry + text[insert_at:]
    else:
        text = (text or "") + f"\n{header}\n\n{entry}"
    index_path.write_text(text, encoding="utf-8")


def _build_frontmatter(
    stable_id: str, action: str, insight: dict, note: str, slug: str
) -> dict:
    now = datetime.now(timezone.utc)
    fm: dict[str, Any] = {
        "id": stable_id,
        "slug": slug,
        "created": now.date().isoformat(),
        "weekday": now.strftime("%A").lower(),
        "modules": insight.get("modules", ["cross"]),
        "themes": insight.get("themes", []),
        "n_sources": insight.get("n_sources", 0),
        "trend_score": insight.get("trend_score", 5),
        "decision": action,
    }
    if note:
        fm["note"] = note
    if action == "followup" and insight.get("followup_due"):
        fm["followup_due"] = insight["followup_due"]
    return fm


def _action_target(action: str) -> tuple[str, str]:
    return {
        "keep": ("keepers", "KEEPERS.md"),
        "followup": ("followups", "FOLLOWUPS.md"),
        "inspire": ("inspiration", "INSPIRATION.md"),
    }.get(action, ("keepers", "KEEPERS.md"))


def _action_target_from_index(index_path: Path) -> str:
    return {
        "KEEPERS.md": "keepers",
        "FOLLOWUPS.md": "followups",
        "INSPIRATION.md": "inspiration",
    }.get(index_path.name, "keepers")


async def _update_embed_buttons(
    interaction: discord.Interaction, stable_id: str, picked_action: str
) -> None:
    """Markiert gepickten Button gruen, deaktiviert alle Buttons."""
    if not interaction.message:
        return
    try:
        new_view = discord.ui.View(timeout=None)
        for row in interaction.message.components:
            for comp in getattr(row, "children", []):
                cid = getattr(comp, "custom_id", "") or ""
                action = cid.rsplit("_", 1)[-1] if cid else ""
                btn = discord.ui.Button(
                    label=getattr(comp, "label", action),
                    style=(
                        discord.ButtonStyle.success
                        if action == picked_action
                        else discord.ButtonStyle.secondary
                    ),
                    custom_id=cid,
                    disabled=True,
                )
                new_view.add_item(btn)
        await interaction.message.edit(view=new_view)
    except Exception:
        log.exception("Embed-Edit fehlgeschlagen fuer %s", stable_id)


async def _show_followup_modal(
    interaction: discord.Interaction, stable_id: str, insight: dict
) -> None:
    now = datetime.now(timezone.utc)
    modal = discord.ui.Modal(
        title="Followup-Datum",
        custom_id=f"modal_followup_{stable_id}",
    )
    modal.add_item(
        discord.ui.TextInput(
            label="Schnellwahl: +7d / +14d / +30d",
            custom_id="quick_pick",
            default="+14d",
            required=False,
            placeholder="+7d  |  +14d  |  +30d",
        )
    )
    modal.add_item(
        discord.ui.TextInput(
            label="Custom-Datum (YYYY-MM-DD, optional)",
            custom_id="custom_date",
            required=False,
            placeholder=(now + timedelta(days=14)).strftime("%Y-%m-%d"),
        )
    )
    await interaction.response.send_modal(modal)


async def _show_note_modal(
    interaction: discord.Interaction, stable_id: str
) -> None:
    modal = discord.ui.Modal(
        title="Notiz", custom_id=f"modal_note_{stable_id}"
    )
    modal.add_item(
        discord.ui.TextInput(
            label="Notiz",
            custom_id="note_text",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500,
        )
    )
    await interaction.response.send_modal(modal)


async def _append_note_to_insight(
    interaction: discord.Interaction, stable_id: str, note: str
) -> None:
    """Findet bestehendes File mit der ID und ergaenzt note: in Frontmatter."""
    bot = interaction.client  # type: ignore
    for target in ("keepers", "followups", "inspiration"):
        for md in (REPO_ROOT / target).glob("*.md"):
            content = md.read_text(encoding="utf-8")
            if f"id: {stable_id}" not in content:
                continue
            updated = re.sub(
                r"^---\n(.*?)\n---\n",
                lambda m: f"---\n{m.group(1)}\nnote: \"{note}\"\n---\n",
                content,
                count=1,
                flags=re.DOTALL,
            )
            md.write_text(updated, encoding="utf-8")
            await bot._batcher_queue.put(
                (str(md), "note", f"feat(intel): note {stable_id}")
            )
            await interaction.response.send_message(
                "Notiz gespeichert.", ephemeral=True
            )
            return
    await interaction.response.send_message(
        f"Kein File mit ID `{stable_id}` gefunden.", ephemeral=True
    )


def _resolve_due_date(value: str) -> str:
    now = datetime.now(timezone.utc)
    delta_map = {"+7d": 7, "+14d": 14, "+30d": 30}
    if value in delta_map:
        return (now + timedelta(days=delta_map[value])).strftime("%Y-%m-%d")
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except (ValueError, TypeError):
        return (now + timedelta(days=14)).strftime("%Y-%m-%d")


def _extract_modal_value(
    interaction: discord.Interaction, custom_id: str
) -> str:
    for row in (interaction.data or {}).get("components", []):
        for sub in row.get("components", []):
            if sub.get("custom_id") == custom_id:
                return (sub.get("value") or "").strip()
    return ""


async def _check_promotion(
    interaction: discord.Interaction, insight: dict
) -> None:
    """Prueft ob ein Modul >= 5 Keepers ueber >= 3 Wochen hat -> Promotion-Suggestion."""
    modules = insight.get("modules", [])
    if not modules:
        return
    module = modules[0]
    keepers: list[dict] = []
    keepers_dir = REPO_ROOT / "keepers"
    if not keepers_dir.exists():
        return
    for md in keepers_dir.glob("*.md"):
        fm = _parse_fm_quick(md.read_text(encoding="utf-8"))
        if module in (fm.get("modules") or []):
            keepers.append(fm)
    if len(keepers) < 5:
        return
    weeks: list[int] = []
    for fm in keepers:
        if m := re.match(r"W(\d+)", str(fm.get("id", ""))):
            weeks.append(int(m.group(1)))
    if not weeks or (max(weeks) - min(weeks)) < 3:
        return

    promo_path = (
        REPO_ROOT
        / "promotions"
        / f"{module}-suggestion-{date.today().isoformat()}.md"
    )
    promo_path.parent.mkdir(exist_ok=True)
    if promo_path.exists():
        return
    lines = [
        f"# Promotion-Suggestion: {module}\n\n",
        f"{len(keepers)} Keepers ueber W{min(weeks)}-W{max(weeks)}.\n\n",
        "## Keeper-Files\n\n",
    ]
    for fm in keepers:
        lines.append(f"- {fm.get('slug', fm.get('id', '?'))}\n")
    promo_path.write_text("".join(lines), encoding="utf-8")
    bot = interaction.client  # type: ignore
    await bot._batcher_queue.put(
        (
            str(promo_path),
            "promotion",
            f"chore(intel): promotion-suggestion {module}",
        )
    )
    channel = bot._channel_cache.get("bot-commands")
    if channel:
        embed = discord.Embed(
            title=f"📦 Promotion bereit: {module}",
            description=f"{len(keepers)} Keepers, W{min(weeks)}-W{max(weeks)}",
            color=0x9B59B6,
        )
        embed.add_field(
            name="Naechster Schritt",
            value=f"In KMU-Hub: `/intel-promote {module}`",
            inline=False,
        )
        await channel.send(embed=embed)


def _parse_fm_quick(content: str) -> dict:
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 2:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}
