"""HTTP-Client fuer self-hosted Playwright-Container auf Hetzner.

Container-Endpoint setzt JS-rendered HTML als JSON zurueck.
Container-Code separat in .bot/ oder docker-compose mit `browserless/chrome`-Image.
"""

from __future__ import annotations

import os
from typing import Any

import requests

ENDPOINT = os.environ.get("PLAYWRIGHT_SERVICE_URL", "http://localhost:3001")


def scrape(url: str, wait_for_selector: str | None = None, timeout: int = 30) -> dict[str, Any]:
    """Returns {"html": str, "markdown": str | None, "status": int}.

    Bei Outage: returns {"html": "", "markdown": None, "status": 0, "error": str}.
    """
    payload: dict[str, Any] = {"url": url, "timeout": timeout * 1000}
    if wait_for_selector:
        payload["waitForSelector"] = wait_for_selector

    try:
        resp = requests.post(f"{ENDPOINT}/content", json=payload, timeout=timeout + 5)
        resp.raise_for_status()
        data = resp.json()
        html = data.get("data") or data.get("html") or ""
    except requests.RequestException as e:
        print(f"[playwright] WARN: scrape failed for {url}: {e}")
        return {"html": "", "markdown": None, "status": 0, "error": str(e)}

    md: str | None = None
    if html:
        try:
            import trafilatura
            md = trafilatura.extract(html, output_format="markdown") or ""
        except (ImportError, Exception):
            try:
                from markdownify import markdownify
                md = markdownify(html)
            except (ImportError, Exception):
                md = None

    return {"html": html, "markdown": md, "status": 200}


def diff_pricing_page(url: str, last_snapshot: str | None) -> dict[str, Any]:
    """Vergleicht aktuelle Pricing-Page mit letzter Snapshot.

    Returns {"changed": bool, "diff": str | None, "current_snapshot": str}
    """
    import difflib

    current = scrape(url)
    current_md = current.get("markdown") or ""
    if not current_md:
        return {"changed": False, "diff": None, "current_snapshot": "", "error": "scrape_failed"}

    if last_snapshot is None:
        return {"changed": True, "diff": "(initial snapshot)", "current_snapshot": current_md}

    if current_md.strip() == last_snapshot.strip():
        return {"changed": False, "diff": None, "current_snapshot": current_md}

    diff_text = "".join(
        difflib.unified_diff(
            last_snapshot.splitlines(keepends=True),
            current_md.splitlines(keepends=True),
            fromfile="prev",
            tofile="curr",
            n=3,
        )
    )
    return {"changed": True, "diff": diff_text, "current_snapshot": current_md}
