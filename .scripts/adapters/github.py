"""GitHub-Releases via Atom-Feed. Kein PAT noetig fuer Public-Repos.

Wenn PAT gesetzt: nutze Search-API fuer Trending.
"""

from __future__ import annotations

from typing import Any

from . import rss


def fetch_releases(source: dict[str, Any], since_iso: str | None = None) -> list[dict[str, Any]]:
    """source: {"id": str, "github_org": str, "github_repo": str, "trust": int}

    Nutzt den Atom-Feed `https://github.com/<org>/<repo>/releases.atom`.
    """
    org = source.get("github_org")
    repo = source.get("github_repo") or org
    if not org:
        return []
    feed_source = {
        "id": source.get("id"),
        "url": f"https://github.com/{org}/{repo}/releases.atom",
        "trust": source.get("trust", 7),
    }
    items = rss.fetch(feed_source, since_iso)
    for item in items:
        item["github_org"] = org
        item["github_repo"] = repo
    return items
