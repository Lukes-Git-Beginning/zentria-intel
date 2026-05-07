"""Lade settings.yaml und alle sources/*.yaml in eine kombinierte Konfiguration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_settings() -> dict[str, Any]:
    with (REPO_ROOT / "settings.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_all_sources() -> dict[str, dict[str, Any]]:
    """Returns dict[modul_name -> source_config]."""
    out: dict[str, dict[str, Any]] = {}
    for path in (REPO_ROOT / "sources").glob("*.yaml"):
        with path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
        out[path.stem] = data
    return out


def flatten_feed_sources(sources_by_modul: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Flatten alle Modul-/Themen-/Quellen-YAMLs zu einer flachen Liste von Feed-Konfigurationen.

    Returns Liste mit Items wie:
        {"id": "zendesk-blog-helpdesk", "url": "...", "type": "rss", "trust": 8, "modules": ["helpdesk"]}
    """
    out: list[dict[str, Any]] = []

    for modul_key, data in sources_by_modul.items():
        # Modul-YAMLs (haben "competitors")
        if "competitors" in data:
            modul = data.get("module", modul_key)
            for comp in data.get("competitors", []):
                comp_name = comp.get("name", "unknown")
                for feed in comp.get("feeds", []) or []:
                    out.append({
                        "id": f"{comp_name.lower().replace(' ', '-')}-{feed.get('type', 'rss')}-{modul}",
                        "url": feed.get("url"),
                        "type": feed.get("type", "rss"),
                        "trust": feed.get("trust", 6),
                        "modules": [modul],
                        "competitor_name": comp_name,
                    })

        # Themen-YAMLs (haben "themes")
        if "themes" in data:
            for theme in data.get("themes", []):
                theme_id = theme.get("id")
                for feed in theme.get("feeds", []) or []:
                    out.append({
                        "id": f"theme-{theme_id}-{feed.get('type', 'rss')}",
                        "url": feed.get("url"),
                        "type": feed.get("type", "rss"),
                        "trust": feed.get("trust", 6),
                        "modules": theme.get("cosmi_modules") or ["cross"],
                        "themes": [theme_id],
                    })

        # Regulation-YAMLs (haben "regulation")
        if "regulation" in data:
            for reg in data.get("regulation", []):
                reg_id = reg.get("id")
                for feed in reg.get("feeds", []) or []:
                    out.append({
                        "id": f"reg-{reg_id}",
                        "url": feed.get("url"),
                        "type": feed.get("type", "rss"),
                        "trust": feed.get("trust", 9),
                        "modules": ["regulation"],
                        "regulation_id": reg_id,
                    })

        # Tech-Trends / Magazines (haben "sources")
        if "sources" in data:
            for src in data.get("sources", []):
                modules_for_src = src.get("modules") or [modul_key]
                out.append({
                    "id": src.get("id"),
                    "url": src.get("url"),
                    "type": src.get("type", "rss"),
                    "trust": src.get("trust", 6),
                    "modules": modules_for_src,
                    "subreddit": src.get("subreddit"),
                    "fetch_top_n": src.get("fetch_top_n"),
                    "keywords_must_match_any": src.get("keywords_must_match_any"),
                })

    return [s for s in out if s.get("url") or s.get("subreddit")]


if __name__ == "__main__":
    # CLI-Test: liste alle Quellen
    sources = flatten_feed_sources(load_all_sources())
    print(f"Total feed sources: {len(sources)}")
    by_type: dict[str, int] = {}
    for s in sources:
        t = s.get("type", "unknown")
        by_type[t] = by_type.get(t, 0) + 1
    print(f"By type: {by_type}")
