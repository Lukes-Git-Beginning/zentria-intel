"""Reddit-Adapter.

Default: OAuth Application-Only (Client-Credentials Flow) ueber `oauth.reddit.com`
— braucht REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET aus einer reddit.com/prefs/apps
"script"-App. Rate-Limit: 600 req / 600s.

Fallback: Public-JSON ueber `www.reddit.com/r/.../new.json` (kein Auth) — wird
seit 2023 zunehmend mit 403 geblockt, deshalb nur als Notfall.
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone
from typing import Any

import requests

USER_AGENT = os.environ.get(
    "REDDIT_USER_AGENT",
    "zentria-intel/0.1 (by /u/zentria-bot)",
)
CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID", "").strip()
CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET", "").strip()

_token: str | None = None
_token_expires_at: float = 0.0


def _get_oauth_token() -> str | None:
    """Returns a cached app-only access token, or None if creds missing/fetch fails."""
    global _token, _token_expires_at
    if not (CLIENT_ID and CLIENT_SECRET):
        return None
    if _token and time.time() < _token_expires_at - 60:
        return _token
    try:
        resp = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=(CLIENT_ID, CLIENT_SECRET),
            data={"grant_type": "client_credentials"},
            headers={"User-Agent": USER_AGENT},
            timeout=15,
        )
        resp.raise_for_status()
        body = resp.json()
        _token = body["access_token"]
        _token_expires_at = time.time() + int(body.get("expires_in", 3600))
        return _token
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"[reddit] WARN: OAuth token fetch failed: {e}")
        _token = None
        _token_expires_at = 0.0
        return None


def fetch(source: dict[str, Any], since_iso: str | None = None) -> list[dict[str, Any]]:
    """source: {"id": str, "subreddit": str, "fetch_top_n": int, "trust": int}"""
    sub = source.get("subreddit")
    if not sub:
        return []
    n = source.get("fetch_top_n", 25)

    token = _get_oauth_token()
    if token:
        url = f"https://oauth.reddit.com/r/{sub}/new"
        headers = {
            "User-Agent": USER_AGENT,
            "Authorization": f"Bearer {token}",
        }
    else:
        url = source.get("url") or f"https://www.reddit.com/r/{sub}/new.json"
        headers = {"User-Agent": USER_AGENT}

    try:
        resp = requests.get(
            url,
            headers=headers,
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
    # OAuth: 10 req/s allowed. Public: ~1 req/s. 1s sleep is safe for both.
    time.sleep(1.1)
    return items
