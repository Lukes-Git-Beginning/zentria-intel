"""HackerNews-Adapter via Firebase-API (kein Rate-Limit, aber sequenziell pro Item)."""

from __future__ import annotations

from typing import Any

import requests

API_BASE = "https://hacker-news.firebaseio.com/v0"


def fetch(source: dict[str, Any], since_iso: str | None = None) -> list[dict[str, Any]]:
    """Holt Top-N Stories von HN-Frontpage. Filtert auf must-match-keywords falls definiert."""
    n = source.get("fetch_top_n", 30)
    keywords = source.get("keywords_must_match_any", [])

    try:
        resp = requests.get(f"{API_BASE}/topstories.json", timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[hackernews] WARN: topstories failed: {e}")
        return []

    ids = resp.json()[:n]
    items: list[dict[str, Any]] = []

    for hn_id in ids:
        try:
            r = requests.get(f"{API_BASE}/item/{hn_id}.json", timeout=5)
            r.raise_for_status()
            item = r.json()
        except requests.RequestException:
            continue
        if not item or item.get("type") != "story":
            continue
        title = item.get("title", "")

        if keywords and not any(kw.lower() in title.lower() for kw in keywords):
            continue

        ts = item.get("time")
        published_iso = ""
        if ts:
            from datetime import datetime, timezone
            published_iso = datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
        if since_iso and published_iso and published_iso <= since_iso:
            continue

        items.append({
            "source_id": source.get("id"),
            "source_trust": source.get("trust", 6),
            "title": title[:300],
            "url": item.get("url", f"https://news.ycombinator.com/item?id={hn_id}"),
            "summary": item.get("text", "")[:1000] if item.get("text") else "",
            "body": None,
            "published_at": published_iso,
            "score": item.get("score", 0),
            "descendants": item.get("descendants", 0),
            "hn_id": hn_id,
        })

    return items
