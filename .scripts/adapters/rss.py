"""RSS/Atom-Adapter via feedparser."""

from __future__ import annotations

from typing import Any

import feedparser


def fetch(source: dict[str, Any], since_iso: str | None = None) -> list[dict[str, Any]]:
    """Fetch RSS/Atom-Feed.

    source: {"id": str, "url": str, "trust": int, "type": "rss" | "atom"}
    """
    url = source.get("url") or source.get("feeds", [{}])[0].get("url")
    if not url:
        return []
    try:
        feed = feedparser.parse(url, request_headers={"User-Agent": "zentria-intel/0.1"})
    except Exception as e:
        print(f"[rss] WARN: fetch failed for {url}: {e}")
        return []
    items: list[dict[str, Any]] = []
    for entry in feed.entries[:50]:
        published = entry.get("published") or entry.get("updated") or ""
        # ISO-normalisierung wenn moeglich
        try:
            from dateutil import parser as dt_parser
            published_iso = dt_parser.parse(published).isoformat() if published else ""
        except (ValueError, TypeError, ImportError):
            published_iso = published
        if since_iso and published_iso and published_iso <= since_iso:
            continue
        items.append({
            "source_id": source.get("id"),
            "source_trust": source.get("trust", 5),
            "title": entry.get("title", "")[:300],
            "url": entry.get("link", ""),
            "summary": entry.get("summary", "")[:1000],
            "body": None,
            "published_at": published_iso,
        })
    return items
