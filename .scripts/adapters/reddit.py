"""Reddit-Public-JSON-Adapter (kein OAuth, aber custom User-Agent benoetigt)."""

from __future__ import annotations

import os
import time
from typing import Any

import requests

USER_AGENT = os.environ.get("REDDIT_USER_AGENT", "zentria-intel/0.1 (by /u/zentria-bot)")


def fetch(source: dict[str, Any], since_iso: str | None = None) -> list[dict[str, Any]]:
    """source: {"id": str, "subreddit": str, "fetch_top_n": int, "trust": int}"""
    sub = source.get("subreddit")
    if not sub:
        return []
    url = source.get("url") or f"https://www.reddit.com/r/{sub}/new.json"
    n = source.get("fetch_top_n", 25)
    try:
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            params={"limit": n},
            timeout=15,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[reddit] WARN: fetch failed for r/{sub}: {e}")
        return []
    data = resp.json().get("data", {})
    posts = data.get("children", [])
    items: list[dict[str, Any]] = []
    for post in posts:
        d = post.get("data", {})
        if d.get("stickied"):
            continue
        created_utc = d.get("created_utc")
        published_iso = ""
        if created_utc:
            from datetime import datetime, timezone
            published_iso = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()
        if since_iso and published_iso and published_iso <= since_iso:
            continue
        items.append({
            "source_id": source.get("id"),
            "source_trust": source.get("trust", 5),
            "title": d.get("title", "")[:300],
            "url": f"https://reddit.com{d.get('permalink', '')}",
            "summary": d.get("selftext", "")[:1000],
            "body": None,
            "published_at": published_iso,
            "score": d.get("score", 0),
            "num_comments": d.get("num_comments", 0),
        })
    # Politeness: 60 req/min Limit. 1s sleep zwischen subreddits.
    time.sleep(1.1)
    return items
