"""State-Management: Watermarks, Run-Telemetry, Hot-Items.

Alle State-Files leben unter ~/Documents/zentria-intel/.state/.
Watermarks sind per-Quelle published_at-Cursor.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / ".state"
STATE_DIR.mkdir(exist_ok=True)

WATERMARKS_FILE = STATE_DIR / "watermarks.json"
RUNS_LOG = STATE_DIR / "runs.jsonl"
DISMISSED_LOG = STATE_DIR / "dismissed.jsonl"


def load_watermarks() -> dict[str, str]:
    if not WATERMARKS_FILE.exists():
        return {}
    with WATERMARKS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def update_watermark(source_id: str, latest_iso: str) -> None:
    wm = load_watermarks()
    current = wm.get(source_id, "")
    if latest_iso > current:
        wm[source_id] = latest_iso
        with WATERMARKS_FILE.open("w", encoding="utf-8") as f:
            json.dump(wm, f, indent=2, sort_keys=True)


def get_watermark(source_id: str) -> str | None:
    return load_watermarks().get(source_id)


def append_run_telemetry(run: dict[str, Any]) -> None:
    """Append eine Zeile JSON nach .state/runs.jsonl."""
    run.setdefault("recorded_at", datetime.now(timezone.utc).isoformat())
    with RUNS_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(run, ensure_ascii=False) + "\n")


def append_dismissed(item_id: str, reason: str = "user-dismiss") -> None:
    entry = {
        "item_id": item_id,
        "reason": reason,
        "at": datetime.now(timezone.utc).isoformat(),
    }
    with DISMISSED_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def write_hot_items(date_str: str, items: list[dict[str, Any]]) -> Path:
    """Schreibt Top-N Hot-Items aus intel-morning fuer intel-deep am Abend."""
    path = STATE_DIR / f"hot_items_{date_str}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return path


def read_hot_items(date_str: str) -> list[dict[str, Any]]:
    path = STATE_DIR / f"hot_items_{date_str}.json"
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return json.load(f)
