"""End-to-End-Pipeline: Lade alle Quellen, polle, dedup, filter, score.

CLI-Wrapper fuer Routinen. Routinen rufen das via Subprocess oder direkt via Python-Import.

Usage:
    python .scripts/fetch_all.py --tier=tier1 --output=daily/2026-05-06-morning-raw.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# .scripts ist ein Punkt-Prefix-Verzeichnis und kann nicht als Package
# importiert werden. sys.path-Insert macht alle .scripts-Module direkt
# als Top-Level verfuegbar.
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

# pylint: disable=wrong-import-position
import dedup  # noqa: E402
import prefilter  # noqa: E402
import state  # noqa: E402
from adapters import github, hackernews, reddit, rss  # noqa: E402
from load_settings import (  # noqa: E402
    flatten_feed_sources,
    load_all_sources,
    load_settings,
)


ADAPTERS = {
    "rss": rss.fetch,
    "atom": rss.fetch,
    "reddit-public-json": reddit.fetch,
    "json": hackernews.fetch,    # HN
    "github-trending": rss.fetch,    # einfach behandeln
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", choices=["tier1", "tier2", "all"], default="tier1")
    parser.add_argument("--output", required=True)
    parser.add_argument("--target-modules", default="")
    args = parser.parse_args()

    settings = load_settings()
    sources_by_modul = load_all_sources()
    feed_sources = flatten_feed_sources(sources_by_modul)
    muted = set(settings.get("muted_sources", []) or [])

    # Tier-Filter — Tier-Info steht im Modul-YAML, hier vereinfacht
    if args.tier == "tier1":
        feed_sources = [
            s for s in feed_sources
            if (sources_by_modul.get(s.get("modules", ["unknown"])[0], {}).get("priority") == "tier1")
            or s.get("type") in ("reddit-public-json", "json")
        ]

    print(f"[fetch_all] Polling {len(feed_sources)} feed sources (tier={args.tier})")

    all_items: list[dict] = []
    failures: list[tuple[str, str]] = []

    for src in feed_sources:
        if src.get("id") in muted:
            continue
        watermark = state.get_watermark(src.get("id", ""))
        adapter_fn = ADAPTERS.get(src.get("type", "rss"))
        if not adapter_fn:
            print(f"[fetch_all] WARN: no adapter for type={src.get('type')}, source={src.get('id')}")
            continue
        try:
            if src.get("github_org"):
                items = github.fetch_releases(src, since_iso=watermark)
            else:
                items = adapter_fn(src, since_iso=watermark)
            all_items.extend(items)
            # Watermark update
            if items:
                latest = max((i.get("published_at", "") for i in items), default="")
                if latest:
                    state.update_watermark(src.get("id", ""), latest)
        except Exception as e:    # noqa: BLE001
            failures.append((src.get("id", "?"), str(e)))

    print(f"[fetch_all] Raw items: {len(all_items)}, failures: {len(failures)}")

    # Pre-Filter
    filtered, prefilter_stats = prefilter.filter_items(all_items, muted)
    print(f"[fetch_all] After prefilter: {len(filtered)} (stats: {prefilter_stats})")

    # Dedup
    deduped = dedup.dedup(filtered, threshold=settings.get("optimization", {}).get("simhash_threshold", 3))
    print(f"[fetch_all] After dedup: {len(deduped)}")

    # Pre-Score
    target_modules = [m.strip() for m in args.target_modules.split(",") if m.strip()] or None
    for item in deduped:
        item["pre_score"] = prefilter.pre_score(item, target_modules)
    deduped.sort(key=lambda x: x.get("pre_score", 0), reverse=True)

    # Output
    output_path = REPO_ROOT / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump({
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "tier": args.tier,
            "raw_count": len(all_items),
            "after_prefilter": len(filtered),
            "after_dedup": len(deduped),
            "prefilter_stats": prefilter_stats,
            "failures": failures,
            "items": deduped,
        }, f, ensure_ascii=False, indent=2)
    print(f"[fetch_all] Wrote {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
