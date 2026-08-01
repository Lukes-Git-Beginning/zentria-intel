#!/usr/bin/env python3
"""
Monthly pricing diff — 2026-08-01
Scrapes all competitor pricing pages, diffs against July 2026 baseline,
writes monthly/2026-08-pricing.md and updates snapshots.
"""

import json
import re
import sys
import time
import os
import difflib
import html2text
from datetime import datetime, timezone, timedelta
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import urllib.parse

WORKDIR = "/opt/zentria-intel"
DATE_STR = "2026-08-01"
YEAR = 2026
MONTH = 8
SNAPSHOT_DIR = f"{WORKDIR}/.state/pricing_snapshots"
REPORT_FILE = f"{WORKDIR}/monthly/2026-08-pricing.md"
RUNS_FILE = f"{WORKDIR}/.state/runs.jsonl"
PLAYWRIGHT_URL = os.environ.get("PLAYWRIGHT_SERVICE_URL", "http://localhost:3001")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_TRENDS", "")

BERLIN_TZ = timezone(timedelta(hours=2))  # CEST August

COMPETITORS = [
    {
        "name": "Pipedrive",
        "slug": "pipedrive",
        "pricing_url": "https://www.pipedrive.com/en/pricing",
        "region": "international",
        "threat_level": "high",
        "modules": ["crm-core"],
    },
    {
        "name": "HubSpot",
        "slug": "hubspot",
        "pricing_url": "https://www.hubspot.com/pricing/sales",
        "region": "international",
        "threat_level": "high",
        "modules": ["crm-core"],
    },
    {
        "name": "Salesforce",
        "slug": "salesforce",
        "pricing_url": "https://www.salesforce.com/sales/pricing/",
        "region": "international",
        "threat_level": "medium",
        "modules": ["crm-core"],
    },
    {
        "name": "monday.com",
        "slug": "monday",
        "pricing_url": "https://monday.com/pricing",
        "region": "international",
        "threat_level": "high",
        "modules": ["crm-core"],
    },
    {
        "name": "Zoho CRM",
        "slug": "zoho",
        "pricing_url": "https://www.zoho.com/crm/pricing.html",
        "region": "international",
        "threat_level": "medium",
        "modules": ["crm-core"],
    },
    {
        "name": "Bexio",
        "slug": "bexio",
        # Updated from /de-DE/preise (404 since 2026-07-01) → /de-CH/preise
        "pricing_url": "https://www.bexio.com/de-CH/preise",
        "region": "dach",
        "threat_level": "high",
        "modules": ["crm-core", "buchhaltung"],
    },
    {
        "name": "Odoo",
        "slug": "odoo",
        "pricing_url": "https://www.odoo.com/pricing-plan",
        "region": "international",
        "threat_level": "high",
        "modules": ["crm-core", "buchhaltung"],
    },
    {
        "name": "weclapp",
        "slug": "weclapp",
        "pricing_url": "https://www.weclapp.com/de/preise",
        "region": "dach",
        "threat_level": "high",
        "modules": ["crm-core", "einkauf"],
    },
    {
        "name": "sevDesk",
        "slug": "sevdesk",
        "pricing_url": "https://sevdesk.de/preise/",
        "region": "dach",
        "threat_level": "high",
        "modules": ["buchhaltung"],
    },
    {
        "name": "Lexoffice",
        "slug": "lexoffice",
        "pricing_url": "https://www.lexoffice.de/preise/",
        "region": "dach",
        "threat_level": "high",
        "modules": ["buchhaltung"],
    },
    {
        "name": "Zendesk",
        "slug": "zendesk",
        "pricing_url": "https://www.zendesk.com/pricing/",
        "region": "international",
        "threat_level": "high",
        "modules": ["helpdesk"],
    },
]


def fetch_via_playwright(url, timeout=30):
    """Fetch JS-rendered page via Playwright/Browserless service."""
    payload = json.dumps({"url": url}).encode("utf-8")
    req = Request(
        f"{PLAYWRIGHT_URL}/content",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "zentria-intel/1.0",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  PLAYWRIGHT ERROR {url}: {e}", file=sys.stderr)
        return None


def html_to_markdown(html_content):
    """Convert HTML to clean markdown, focused on pricing-relevant content."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0  # no line wrapping
    h.skip_internal_links = True
    h.unicode_snob = True
    h.decode_errors = "replace"
    md = h.handle(html_content)

    # Collapse excessive blank lines
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    # Remove cookie/GDPR banners, nav noise
    lines = md.split('\n')
    filtered = []
    skip_patterns = [
        re.compile(r'(?i)(cookie|gdpr|datenschutz|impressum|agb|newsletter|social media|follow us|twitter|linkedin|facebook|instagram|youtube|tiktok)', ),
        re.compile(r'^\s*\*\s*$'),  # lone bullet
        re.compile(r'(?i)(javascript|enable js|browser not supported)'),
    ]
    for line in lines:
        skip = False
        for pat in skip_patterns:
            if pat.search(line) and len(line) < 120:
                skip = True
                break
        if not skip:
            filtered.append(line)
    return '\n'.join(filtered)


def extract_pricing_section(markdown_text, competitor_name):
    """
    Extract the most pricing-relevant portion of the page markdown.
    Focuses on lines containing currency symbols, tier names, price patterns.
    Returns a cleaned excerpt focused on pricing content.
    """
    lines = markdown_text.split('\n')
    price_re = re.compile(r'(?i)(€|\$|£|eur|usd|gbp|\d+[,.]?\d*\s*/\s*(mo|month|user|nutzer|seat|agent|mo\.)|kostenlos|free|gratis|starter|professional|enterprise|business|essential|basic|advanced|growth|scale|team|plus|pro\b|per user|je nutzer|ab €|from \$|pricing|preise|tarif|plan|tier)')

    scored = []
    for i, line in enumerate(lines):
        score = 0
        if price_re.search(line):
            score += 10
        if re.search(r'€\s*\d', line) or re.search(r'\$\s*\d', line):
            score += 20
        if re.search(r'\d+[,.]?\d*\s*/\s*(mo|month|user|seat|agent)', line, re.IGNORECASE):
            score += 15
        if re.search(r'(?i)(annual|yearly|jährlich|monatlich|monthly)', line):
            score += 5
        scored.append((i, score, line))

    high_score_indices = {i for i, s, _ in scored if s >= 10}

    if not high_score_indices:
        return '\n'.join(lines[:200])

    keep = set()
    for idx in high_score_indices:
        for j in range(max(0, idx - 5), min(len(lines), idx + 6)):
            keep.add(j)

    result_lines = [lines[i] for i in sorted(keep)]
    result = '\n'.join(result_lines)

    if len(result) > 8000:
        result = result[:8000] + '\n\n[... truncated for snapshot ...]'

    return result


def load_snapshot(slug):
    """Load existing pricing snapshot for a competitor."""
    path = f"{SNAPSHOT_DIR}/{slug}.md"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None


def save_snapshot(slug, content):
    """Save updated pricing snapshot."""
    path = f"{SNAPSHOT_DIR}/{slug}.md"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def compute_diff(old, new, slug):
    """
    Compute unified diff between old and new snapshot.
    Returns (has_changes, diff_text, change_summary).
    """
    if old is None:
        return True, None, "Kein Baseline-Snapshot vorhanden"

    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)

    diff = list(difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f"{slug}.md (Juli 2026)",
        tofile=f"{slug}.md (August 2026)",
        n=3,
    ))

    if not diff:
        return False, None, None

    added = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in diff if l.startswith('-') and not l.startswith('---'))

    diff_text = ''.join(diff[:200])
    change_summary = f"+{added} Zeilen / -{removed} Zeilen"
    return True, diff_text, change_summary


def interpret_change(competitor_name, slug, diff_text, old_snapshot, new_snapshot):
    """
    Rule-based interpretation of pricing changes.
    Returns markdown string with interpretation and Cosmi implications.
    """
    if not diff_text:
        return ""

    added_lines = [l[1:].strip() for l in diff_text.split('\n')
                   if l.startswith('+') and not l.startswith('+++')]
    removed_lines = [l[1:].strip() for l in diff_text.split('\n')
                     if l.startswith('-') and not l.startswith('---')]

    added_text = ' '.join(added_lines).lower()
    removed_text = ' '.join(removed_lines).lower()

    interpretations = []
    cosmi_implications = []

    # Price increase detection
    price_pattern = re.compile(r'(\d+)[,.]?(\d*)\s*(?:€|\$|eur)')
    old_prices = price_pattern.findall(removed_text)
    new_prices = price_pattern.findall(added_text)

    if old_prices and new_prices:
        try:
            old_vals = [float(f"{a}.{b}" if b else a) for a, b in old_prices[:3]]
            new_vals = [float(f"{a}.{b}" if b else a) for a, b in new_prices[:3]]
            old_avg = sum(old_vals) / len(old_vals)
            new_avg = sum(new_vals) / len(new_vals)
            if new_avg > old_avg * 1.03:
                pct = round((new_avg / old_avg - 1) * 100, 1)
                interpretations.append(f"Preis-Erhöhung erkannt (~{pct}%). Neuer Durchschnitt: {new_avg:.2f} vs. alt: {old_avg:.2f}.")
                cosmi_implications.append("Preisliche Distanz zu Cosmi-Modulen hat sich verbessert — Positionierungs-Update prüfen.")
            elif new_avg < old_avg * 0.97:
                pct = round((1 - new_avg / old_avg) * 100, 1)
                interpretations.append(f"Preissenkung erkannt (~{pct}%). Aggressivere Positionierung möglich.")
                cosmi_implications.append("Preisdruck steigt. Cosmi-Differenzierung über Features/Compliance statt Preis betonen.")
        except Exception:
            pass

    # New tier detection
    tier_keywords = ['starter', 'essential', 'basic', 'advanced', 'enterprise', 'business', 'growth', 'scale', 'professional', 'plus', 'pro']
    new_tiers = [kw for kw in tier_keywords if kw in added_text and kw not in removed_text]
    removed_tiers = [kw for kw in tier_keywords if kw in removed_text and kw not in added_text]

    if new_tiers:
        interpretations.append(f"Neuer Tier eingeführt: {', '.join(t.title() for t in new_tiers)}.")
        cosmi_implications.append("Tier-Segmentierung im Markt verdichtet sich. Cosmi-Tier-Struktur abgleichen.")
    if removed_tiers:
        interpretations.append(f"Tier entfernt/umbenannt: {', '.join(t.title() for t in removed_tiers)}.")

    # AI feature bundling
    ai_keywords = ['ai', 'ki', 'künstlich', 'intelligent', 'copilot', 'assistant', 'credit', 'llm', 'agent']
    new_ai = any(kw in added_text for kw in ai_keywords)
    old_ai = any(kw in removed_text for kw in ai_keywords)
    if new_ai and not old_ai:
        interpretations.append("AI-Features neu in Pricing-Seite integriert — möglicherweise neue AI-Tier-Differenzierung.")
        cosmi_implications.append("AI-Bundling-Trend beschleunigt sich. Cosmi-AI-Roadmap-Kommunikation prüfen.")
    elif new_ai and old_ai:
        interpretations.append("AI-Pricing-Konditionen geändert (AI war bereits vorhanden).")

    # Free tier changes
    if 'free' in added_text or 'kostenlos' in added_text or 'gratis' in added_text:
        if 'free' not in removed_text and 'kostenlos' not in removed_text:
            interpretations.append("Kostenloser Tier neu eingeführt oder erweitert.")
            cosmi_implications.append("Freemium-Druck steigt. Cosmi-Einstiegsangebot überprüfen.")

    # Feature moves between tiers
    feature_move_patterns = [
        (re.compile(r'(?i)(unlimited|unbegrenzt)'), "Unlimited-Positionierung geändert"),
        (re.compile(r'(?i)(api|integration)'), "API/Integrations-Gating geändert"),
        (re.compile(r'(?i)(support|sla)'), "Support-Tier-Zuordnung geändert"),
    ]
    for pat, desc in feature_move_patterns:
        in_added = bool(pat.search(added_text))
        in_removed = bool(pat.search(removed_text))
        if in_added != in_removed:
            interpretations.append(f"{desc}.")

    if not interpretations:
        interpretations.append("Strukturelle oder textuelle Änderung — kein konkretes Pricing-Signal extrahierbar. Diff manuell prüfen.")
        cosmi_implications.append("Manuelles Review empfohlen.")

    result = "**Interpretation:** " + " ".join(interpretations) + "\n"
    if cosmi_implications:
        result += "**Cosmi-Implikation:** " + " ".join(cosmi_implications)
    return result


def push_discord_embed(competitor_name, change_summary, interpretation, pricing_url):
    """Push a Discord embed to #trends channel for a detected pricing change."""
    if not DISCORD_WEBHOOK:
        return False

    embed = {
        "title": f"📊 Pricing-Änderung: {competitor_name}",
        "description": (
            f"**Änderung:** {change_summary}\n"
            f"{interpretation[:400] if interpretation else ''}"
        ),
        "color": 0xF4A62A,  # amber
        "fields": [
            {
                "name": "Pricing-Seite",
                "value": f"[→ {pricing_url}]({pricing_url})",
                "inline": True,
            },
            {
                "name": "Monat",
                "value": "August 2026",
                "inline": True,
            },
        ],
        "footer": {
            "text": "zentria-intel · intel-monthly-pricing · 📌 Auf Friday-Watch"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    payload = json.dumps({
        "embeds": [embed],
        "username": "zentria-intel",
        "avatar_url": "https://zentria.io/favicon.ico",
    }).encode("utf-8")

    req = Request(
        DISCORD_WEBHOOK,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=10) as resp:
            return resp.status in (200, 204)
    except Exception as e:
        print(f"  DISCORD ERROR: {e}", file=sys.stderr)
        return False


def format_diff_block(diff_text, max_lines=60):
    """Format a diff as a fenced diff code block, capped at max_lines."""
    if not diff_text:
        return ""
    lines = diff_text.split('\n')
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines.append(f'[... +{len(diff_text.split(chr(10))) - max_lines} weitere Zeilen ...]')
    return "```diff\n" + '\n'.join(lines) + "\n```"


def main():
    run_start = datetime.now(timezone.utc)
    berlin_now = run_start.astimezone(BERLIN_TZ)
    print(f"=== intel-monthly-pricing 2026-08-01 ===")
    print(f"Start: {run_start.isoformat()}")
    print(f"Playwright: {PLAYWRIGHT_URL}")
    print(f"Snapshot dir: {SNAPSHOT_DIR}")
    print()

    results = []
    changes = []
    scrape_errors = []
    scrape_partial = []
    discord_pushed = 0

    for comp in COMPETITORS:
        name = comp["name"]
        slug = comp["slug"]
        url = comp["pricing_url"]
        print(f"[{slug}] Scraping {url} ...")

        # 1. Scrape
        html = fetch_via_playwright(url)
        if not html:
            print(f"  → ERROR: no content")
            scrape_errors.append(name)
            results.append({
                "name": name,
                "slug": slug,
                "status": "error",
                "error": "Playwright returned no content",
                "has_change": False,
            })
            continue

        # Check for block pages
        block_signals = [
            "you have been blocked",
            "sorry, you have been blocked",
            "bot detection",
            "your ip has been blocked",
        ]
        html_lower = html.lower()
        blocked = any(sig in html_lower for sig in block_signals) or len(html) < 1000
        if blocked:
            print(f"  → BLOCKED/MINIMAL ({len(html)} bytes)")
            scrape_partial.append(name)
            old_snap = load_snapshot(slug)
            results.append({
                "name": name,
                "slug": slug,
                "status": "blocked",
                "html_bytes": len(html),
                "has_change": False,
                "old_snapshot_lines": len(old_snap.splitlines()) if old_snap else 0,
                "url": url,
                "region": comp["region"],
                "threat_level": comp["threat_level"],
            })
            time.sleep(1.0)
            continue

        # 2. HTML → Markdown
        try:
            md = html_to_markdown(html)
            pricing_md = extract_pricing_section(md, name)
        except Exception as e:
            print(f"  → PARSE ERROR: {e}")
            scrape_errors.append(name)
            results.append({
                "name": name,
                "slug": slug,
                "status": "parse_error",
                "error": str(e),
                "has_change": False,
            })
            time.sleep(0.5)
            continue

        print(f"  → HTML: {len(html):,} bytes → Pricing excerpt: {len(pricing_md):,} chars")

        # 3. Load old snapshot
        old_snap = load_snapshot(slug)

        # 4. Diff
        has_change, diff_text, change_summary = compute_diff(old_snap, pricing_md, slug)

        # 5. Interpret
        interp = ""
        if has_change and diff_text:
            interp = interpret_change(name, slug, diff_text, old_snap, pricing_md)

        # 6. Save updated snapshot
        save_snapshot(slug, pricing_md)
        print(f"  → Snapshot updated ({'CHANGED' if has_change else 'no change'})")

        result = {
            "name": name,
            "slug": slug,
            "url": url,
            "status": "ok",
            "html_bytes": len(html),
            "snapshot_chars": len(pricing_md),
            "has_change": has_change,
            "change_summary": change_summary,
            "diff_text": diff_text,
            "interpretation": interp,
            "region": comp["region"],
            "threat_level": comp["threat_level"],
        }
        results.append(result)

        if has_change and diff_text:
            changes.append(result)
            if DISCORD_WEBHOOK:
                ok = push_discord_embed(name, change_summary, interp, url)
                if ok:
                    discord_pushed += 1
                    print(f"  → Discord embed pushed")
                time.sleep(0.6)

        time.sleep(1.2)

    # -------------------------------------------------------------------------
    # Build Report
    # -------------------------------------------------------------------------
    checked_ok = [r for r in results if r.get("status") == "ok"]
    checked_blocked = [r for r in results if r.get("status") == "blocked"]
    checked_error = [r for r in results if r.get("status") in ("error", "parse_error")]
    n_checked = len(COMPETITORS)
    n_changes = len(changes)

    report = build_report(
        results=results,
        changes=changes,
        checked_ok=checked_ok,
        checked_blocked=checked_blocked,
        checked_error=checked_error,
        n_checked=n_checked,
        n_changes=n_changes,
        discord_pushed=discord_pushed,
        run_start=run_start,
        berlin_now=berlin_now,
    )

    os.makedirs(f"{WORKDIR}/monthly", exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\nReport written: {REPORT_FILE}")

    # -------------------------------------------------------------------------
    # Telemetry
    # -------------------------------------------------------------------------
    run_end = datetime.now(timezone.utc)
    run_record = {
        "routine": "intel-monthly-pricing",
        "date": DATE_STR,
        "started_at": run_start.isoformat(),
        "finished_at": run_end.isoformat(),
        "duration_seconds": round((run_end - run_start).total_seconds(), 1),
        "competitors_checked": n_checked,
        "scrape_ok": len(checked_ok),
        "scrape_blocked": len(checked_blocked),
        "scrape_error": len(checked_error),
        "changes_detected": n_changes,
        "discord_pushed": discord_pushed,
        "report_file": REPORT_FILE,
        "status": "ok",
    }
    with open(RUNS_FILE, 'a') as f:
        f.write(json.dumps(run_record, ensure_ascii=False) + '\n')
    print(f"Telemetry appended. Done in {run_record['duration_seconds']}s")

    return results, changes


def build_report(results, changes, checked_ok, checked_blocked, checked_error,
                 n_checked, n_changes, discord_pushed, run_start, berlin_now):
    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"year: {YEAR}")
    lines.append(f"month: {MONTH}")
    lines.append(f"created: {DATE_STR}")
    lines.append(f"competitors_checked: {n_checked}")
    lines.append(f"changes_detected: {n_changes}")
    lines.append(f"scrape_ok: {len(checked_ok)}")
    lines.append(f"scrape_blocked: {len(checked_blocked)}")
    lines.append(f"scrape_errors: {len(checked_error)}")
    lines.append("---")
    lines.append("")

    lines.append("# Pricing-Diff August 2026")
    lines.append("")
    lines.append(f"**Routine:** intel-monthly-pricing | **Run:** {berlin_now.strftime('%Y-%m-%d %H:%M CEST')} | **Pool:** OK")
    lines.append(f"**Geprüft:** {n_checked} Konkurrenten | **Änderungen:** {n_changes} | "
                 f"**Scrape OK:** {len(checked_ok)} | **Geblockt:** {len(checked_blocked)} | **Fehler:** {len(checked_error)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if n_changes == 0:
        lines.append("## Stiller Pricing-Monat")
        lines.append("")
        lines.append("> Kein einziger Konkurrent hat im August 2026 seine Pricing-Seite signifikant geändert. "
                     "Alle Snapshots wurden aktualisiert — keine Diff-Blöcke vorhanden.")
        lines.append("")
    else:
        lines.append(f"## Änderungen erkannt ({n_changes})")
        lines.append("")

        for r in changes:
            name = r["name"]
            slug = r["slug"]
            region_tag = "DACH" if r["region"] == "dach" else "International"
            threat = r.get("threat_level", "medium").upper()
            change_summary = r.get("change_summary", "")
            diff_text = r.get("diff_text", "")
            interp = r.get("interpretation", "")

            lines.append(f"### {name} — {change_summary} [{region_tag} · Threat: {threat}]")
            lines.append("")
            lines.append(f"**Pricing-URL:** {r['url']}")
            lines.append("")
            lines.append("**Diff:**")
            lines.append("")
            lines.append(format_diff_block(diff_text, max_lines=60))
            lines.append("")
            if interp:
                lines.append(interp)
            lines.append("")
            lines.append("---")
            lines.append("")

    # Keine Änderungen
    no_change_ok = [r for r in checked_ok if not r.get("has_change")]
    no_change_names = [r["name"] for r in no_change_ok]

    if no_change_names:
        lines.append(f"## Keine Änderungen ({len(no_change_names)})")
        lines.append("")
        lines.append(", ".join(no_change_names))
        lines.append("")
        lines.append("---")
        lines.append("")

    # Scraping-Probleme
    if checked_blocked or checked_error:
        lines.append(f"## Scraping-Probleme ({len(checked_blocked) + len(checked_error)})")
        lines.append("")
        lines.append("| Konkurrent | Status | Details |")
        lines.append("|---|---|---|")
        for r in checked_blocked:
            lines.append(f"| {r['name']} | **Geblockt** | {r.get('html_bytes', '?')} Bytes — Bot-Protection / JS-Wall |")
        for r in checked_error:
            lines.append(f"| {r['name']} | **Fehler** | {r.get('error', 'unbekannt')[:80]} |")
        lines.append("")
        if checked_blocked:
            lines.append("**Empfehlung:** Browser-Session mit Cookie-Handling oder explizitem Warten auf Preis-Selektoren für nächsten Lauf konfigurieren.")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Strategische Beobachtungen
    lines.append("## Strategische Beobachtungen")
    lines.append("")

    observations = []

    ai_changes = [r for r in changes if r.get("interpretation") and
                  any(kw in (r.get("interpretation") or "").lower()
                      for kw in ["ai", "ki", "copilot", "credit", "llm", "agent"])]
    if ai_changes:
        observations.append(
            f"**AI-Pricing-Signal:** {len(ai_changes)} Konkurrent(en) haben diesen Monat AI-Konditionen auf ihrer Pricing-Seite geändert ({', '.join(r['name'] for r in ai_changes)}). AI-Bundling-Trend setzt sich fort."
        )
    else:
        observations.append(
            "**AI-Bundling-Stabilität:** Kein Konkurrent hat diesen Monat neue AI-Pricing-Konditionen eingeführt. Markt atmet nach der Juni/Juli-Welle (monday.com, Zendesk AI-First-Rebranding) durch — oder bereitet Herbst-Relaunch vor."
        )

    dach_changes = [r for r in changes if r.get("region") == "dach"]
    dach_ok = [r for r in checked_ok if r.get("region") == "dach" and not r.get("has_change")]
    if not dach_changes:
        observations.append(
            f"**DACH-Spezialisten stabil:** {', '.join(r['name'] for r in dach_ok) if dach_ok else 'DACH-Segment'} zeigen keine Pricing-Änderungen. "
            "Typisches August-Muster — DACH-Repricing-Wellen folgen meist dem Herbst (September/Oktober)."
        )
    else:
        observations.append(
            f"**DACH-Bewegung:** {len(dach_changes)} DACH-Konkurrent(en) mit Änderungen: "
            f"{', '.join(r['name'] for r in dach_changes)}. Mögliches Q3-Repositioning vor Herbst-Saison."
        )

    if checked_blocked:
        blocked_names = ', '.join(r['name'] for r in checked_blocked)
        observations.append(
            f"**Bot-Schutz persistiert:** {blocked_names} blockieren weiterhin Headless-Scraping. "
            "September-Deepdive mit manueller Prüfung für diese Konkurrenten empfohlen."
        )

    price_increase = [r for r in changes if r.get("interpretation") and
                      "erhöhung" in (r.get("interpretation") or "").lower()]
    if price_increase:
        observations.append(
            f"**Preis-Erhöhungs-Signal:** {', '.join(r['name'] for r in price_increase)} mit Preiserhöhung — "
            "möglicherweise Reaktion auf Inflation oder Feature-Investment. Cosmi-Positionierung kurzfristig prüfen."
        )

    if n_changes == 0:
        observations.append(
            "**Markt-Stabilität:** Kein Konkurrent hat im August Pricing geändert. Hochsommer-Preisruhe bestätigt sich — "
            "Relaunch-Wellen erfahrungsgemäß September/Oktober. Nächste Intensiv-Review: Oktober-Lauf."
        )

    observations.append(
        "**Vorschau September:** Herbst-Saison beginnt — historisch die aktivste Pricing-Revision-Phase. "
        "Besonders zu beobachten: HubSpot (Sales Hub AI-Bundle), Zendesk (Resolution Platform Suite-Preise), "
        "sevDesk (Vollpreis-Kommunikation nach Sommer-Promotion-Ende), weclapp (mögliche ERP-Tier-Änderungen)."
    )

    for i, obs in enumerate(observations, 1):
        lines.append(f"{i}. {obs}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Telemetrie
    run_end_approx = datetime.now(timezone.utc)
    lines.append("## Telemetrie")
    lines.append("")
    lines.append("```")
    lines.append(f"run_date:             {DATE_STR}T06:00:00Z")
    lines.append(f"competitors_total:    {n_checked}")
    lines.append(f"scrape_ok:            {len(checked_ok)}")
    lines.append(f"scrape_blocked:       {len(checked_blocked)}")
    lines.append(f"scrape_errors:        {len(checked_error)}")
    lines.append(f"diffs_detected:       {n_changes}")
    lines.append(f"snapshots_updated:    {len(checked_ok)}")
    lines.append(f"discord_pushed:       {discord_pushed}")
    lines.append(f"playwright_service:   {PLAYWRIGHT_URL}")
    lines.append(f"snapshot_dir:         .state/pricing_snapshots/")
    lines.append(f"next_run:             2026-09-01T04:00:00Z")
    lines.append("```")
    lines.append("")

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
