#!/usr/bin/env python3
"""
Regulation-Sweep fetch pipeline — 2026-06-13 (Saturday KW24)
Polls sources/_regulation.yaml sources, filters by watermarks and Cosmi-relevance,
writes .state/regulation_raw_2026-06-13.json for LLM analysis.
"""

import json
import re
import hashlib
import time
import sys
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

WORKDIR = "/opt/zentria-intel"
DATE_STR = "2026-06-13"
KW = 24
WATERMARKS_FILE = f"{WORKDIR}/.state/watermarks.json"
RAW_FILE = f"{WORKDIR}/.state/regulation_raw_2026-06-13.json"
RUNS_FILE = f"{WORKDIR}/.state/runs.jsonl"
BERLIN_TZ = timezone(timedelta(hours=2))  # CEST in June

# Sources from _regulation.yaml (hardcoded — no PyYAML dependency)
REGULATION_SOURCES = [
    {
        "id": "eur-lex",
        "label": "EUR-Lex EU-Recht-Datenbank",
        "url": "https://eur-lex.europa.eu/EN/display-feeds.do?type=COM&category=N&numTermDocs=10",
        "trust": 10,
        "keywords": ["data protection", "ai act", "nis2", "e-invoice", "vat"],
    },
    {
        "id": "edpb-newsroom",
        "label": "European Data Protection Board (EDPB)",
        "url": "https://www.edpb.europa.eu/news/news_en?sort_by=created&sort_order=DESC&format=feed",
        "trust": 10,
        "keywords": None,
    },
    {
        "id": "bfdi-pressemitteilungen",
        "label": "Bundesbeauftragter fuer den Datenschutz (BfDI)",
        "url": "https://www.bfdi.bund.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed/RSSNewsfeed_Pressemitteilungen.xml",
        "trust": 10,
        "keywords": None,
    },
    {
        "id": "bsi-warnungen",
        "label": "Bundesamt fuer Sicherheit in der Informationstechnik (BSI)",
        "url": "https://wid.cert-bund.de/content/public/securityAdvisory/rss",
        "trust": 10,
        "keywords": ["crm", "saas", "cloud", "postgres", "postgresql", "nginx", "docker", "linux", "kubernetes"],
    },
    {
        "id": "bsi-pressemitteilungen",
        "label": "BSI Pressemitteilungen",
        "url": "https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed/RSSNewsfeed_Presse.xml",
        "trust": 10,
        "keywords": None,
    },
    {
        "id": "oedp-eaid",
        "label": "Europaeischer Datenschutzbeauftragter (EDPS)",
        "url": "https://www.edps.europa.eu/press-publications/press-news/news_en?format=feed",
        "trust": 9,
        "keywords": None,
    },
    {
        "id": "e-rechnung-bmwk",
        "label": "BMWi/BMWK — XRechnung, e-Rechnung, GoBD",
        "url": "https://www.e-rechnung-bund.de/rss-feed/",
        "trust": 10,
        "keywords": ["xrechnung", "zugferd", "e-rechnung", "gobd"],
    },
    {
        "id": "eaid-arbeitsrecht",
        "label": "Bundesarbeitsministerium (BMAS) — ArbZG, Arbeitsrecht",
        "url": "https://www.bmas.de/SiteGlobals/Functions/RSSFeed/DE/RSS/Pressemitteilungen.xml",
        "trust": 9,
        "keywords": ["arbzg", "schichtarbeit", "ruhezeit", "mindestlohn"],
    },
    {
        "id": "cybernews-eu",
        "label": "EU-CyberSec, ENISA, NIS2",
        "url": "https://www.enisa.europa.eu/news/RSS",
        "trust": 9,
        "keywords": None,
    },
    {
        "id": "noyb",
        "label": "noyb.eu — Schrems-Aktivismus, GDPR-Klagen",
        "url": "https://noyb.eu/en/feed",
        "trust": 8,
        "keywords": None,
    },
]

# Cosmi regulation relevance keywords (topic → keywords)
COSMI_RELEVANCE = {
    "dsgvo": ["dsgvo", "datenschutz", "gdpr", "data protection", "einwilligung", "consent",
              "betroffenenrechte", "data subject", "art. 6", "art. 7", "art. 12", "art. 13",
              "art. 14", "art. 15", "verarbeitung", "processing", "bußgeld", "fine",
              "enforcement", "noyb", "bfdi", "edpb", "edps", "schrems", "pay or okay",
              "datenschutzbehörde", "supervisory authority"],
    "aiact": ["ai act", "ai-act", "ki-verordnung", "artificial intelligence act", "hochrisiko",
              "high-risk", "anhang iii", "annex iii", "gpts", "general purpose", "gpai",
              "prohibited ai", "ai omnibus", "omnibus", "prohibited practice"],
    "nis2": ["nis2", "nis-2", "netzwerk- und informationssicherheit", "network information security",
             "cybersicherheit", "cybersecurity", "bsi", "kritische infrastruktur", "critical infrastructure",
             "registrierung", "meldepflicht", "incident reporting"],
    "xrechnung": ["xrechnung", "x-rechnung", "zugferd", "e-rechnung", "e-invoice", "gobd",
                  "en 16931", "elektronische rechnung", "electronic invoice", "peppol"],
    "arbzg": ["arbzg", "arbeitszeit", "arbeitszeitgesetz", "schichtarbeit", "ruhezeit",
              "mindestlohn", "minimum wage", "arbeitsrecht", "bmas", "tarifvertrag",
              "urlaubsgesetz", "mutterschutz"],
    "eidas": ["eidas", "eudi", "eudi wallet", "electronic identity", "elektronische identität",
              "vertrauensdienst", "trust service", "esignatur", "e-signatur", "qualified signature",
              "wallet", "digital identity"],
    "bsi_cve": ["postgresql", "postgres", "nginx", "docker", "kubernetes", "linux kernel",
                "crm", "saas", "cloud", "cve", "advisory", "schwachstelle", "vulnerability",
                "patch", "critical", "high", "kritisch"],
}

SPAM_PATTERNS = [
    re.compile(r"(?i)(webinar zur|anmeldung jetzt|whitepaper download)"),
    re.compile(r"(?i)(black friday|cyber monday|sale)"),
    re.compile(r"(?i)^(get started|try free|sign up)"),
    re.compile(r"(?i)(newsletter subscription|subscribe now)"),
]

SIMHASH_THRESHOLD = 3


def load_watermarks():
    try:
        with open(WATERMARKS_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_watermarks(wm):
    with open(WATERMARKS_FILE, "w") as f:
        json.dump(wm, f, indent=2)


def parse_date(s):
    if not s:
        return None
    for fmt in [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%a, %d %b %Y %H:%M:%S +0000",
    ]:
        try:
            dt = datetime.strptime(s.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            pass
    try:
        s2 = re.sub(r'\.\d+', '', s.strip())
        s2 = re.sub(r'Z$', '+00:00', s2)
        dt = datetime.fromisoformat(s2)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        pass
    return None


def fetch_url(url, timeout=12):
    h = {
        "User-Agent": "zentria-intel/1.0 (+https://zentria.io/intel-bot)",
        "Accept": "application/rss+xml, application/atom+xml, application/json, text/xml, */*",
    }
    req = Request(url, headers=h)
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.read(), resp.getcode()
    except HTTPError as e:
        return None, e.code
    except Exception as e:
        print(f"  FETCH ERROR {url}: {e}", file=sys.stderr)
        return None, None


def simhash(text):
    words = re.findall(r'\w+', text.lower())
    v = [0] * 64
    for word in words:
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        for i in range(64):
            if h & (1 << i):
                v[i] += 1
            else:
                v[i] -= 1
    fingerprint = 0
    for i in range(64):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint


def hamming_distance(a, b):
    return bin(a ^ b).count('1')


def is_spam(title):
    if not title or len(title) < 10:
        return True
    for pat in SPAM_PATTERNS:
        if pat.search(title):
            return True
    return False


def parse_rss_atom(data):
    items = []
    if not data:
        return items
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        print(f"  XML parse error: {e}", file=sys.stderr)
        return items

    def strip_ns(tag):
        return re.sub(r'\{[^}]+\}', '', tag)

    def find_text(elem, *tags):
        for tag in tags:
            child = elem.find(tag)
            if child is not None and child.text:
                return child.text.strip()
        return None

    root_tag = strip_ns(root.tag)

    if root_tag == 'rss':
        for channel in root.findall('.//channel'):
            for item in channel.findall('item'):
                title = find_text(item, 'title') or ''
                link = find_text(item, 'link') or ''
                if not link:
                    guid = item.find('guid')
                    if guid is not None and guid.text and guid.text.startswith('http'):
                        link = guid.text
                pub = find_text(item, 'pubDate', 'published', 'updated')
                summary = find_text(item, 'description', 'summary', 'content') or ''
                summary = re.sub(r'<[^>]+>', ' ', summary)[:400]
                items.append({'title': title.strip(), 'url': link.strip(),
                              'published': pub, 'summary': summary.strip()})

    elif root_tag == 'feed':
        for entry in root.findall('.//{http://www.w3.org/2005/Atom}entry'):
            title_el = entry.find('{http://www.w3.org/2005/Atom}title')
            title = title_el.text.strip() if title_el is not None and title_el.text else ''

            link_el = entry.find('{http://www.w3.org/2005/Atom}link[@rel="alternate"]')
            if link_el is None:
                link_el = entry.find('{http://www.w3.org/2005/Atom}link')
            link = link_el.get('href', '') if link_el is not None else ''

            pub_el = entry.find('{http://www.w3.org/2005/Atom}published')
            if pub_el is None:
                pub_el = entry.find('{http://www.w3.org/2005/Atom}updated')
            pub = pub_el.text.strip() if pub_el is not None and pub_el.text else None

            summary_el = entry.find('{http://www.w3.org/2005/Atom}summary')
            if summary_el is None:
                summary_el = entry.find('{http://www.w3.org/2005/Atom}content')
            summary = summary_el.text or '' if summary_el is not None else ''
            summary = re.sub(r'<[^>]+>', ' ', summary)[:400].strip()

            items.append({'title': title, 'url': link, 'published': pub, 'summary': summary})
    else:
        for entry_tag in ['item', 'entry']:
            for entry in root.iter(entry_tag):
                title = ''
                link = ''
                pub = None
                summary = ''
                for child in entry:
                    ct = strip_ns(child.tag).lower()
                    if ct == 'title' and child.text:
                        title = child.text.strip()
                    elif ct == 'link' and child.text:
                        link = child.text.strip()
                    elif ct == 'link' and child.get('href'):
                        link = child.get('href')
                    elif ct in ('published', 'updated', 'pubdate') and child.text:
                        pub = child.text.strip()
                    elif ct in ('description', 'summary') and child.text:
                        summary = re.sub(r'<[^>]+>', ' ', child.text)[:400].strip()
                if title:
                    items.append({'title': title, 'url': link, 'published': pub, 'summary': summary})

    return items


def classify_topics(title, summary):
    """Return list of matching Cosmi regulation topics."""
    text = (title + ' ' + summary).lower()
    matched = []
    for topic, kws in COSMI_RELEVANCE.items():
        if any(kw in text for kw in kws):
            matched.append(topic)
    return matched


def fetch_source(source, watermarks):
    src_id = source["id"]
    label = source["label"]
    url = source["url"]
    trust = source["trust"]
    keywords = source.get("keywords")

    wm_str = watermarks.get(src_id)
    wm_dt = parse_date(wm_str) if wm_str else None

    print(f"  [{src_id}] Fetching {label[:50]}...")
    data, status_code = fetch_url(url)

    if data is None:
        print(f"    → FAILED (HTTP {status_code})")
        return [], "failed", status_code

    items_raw = parse_rss_atom(data)
    items = []
    newest_dt = None

    for raw in items_raw[:50]:
        title = raw.get('title', '')
        link = raw.get('url', '')
        pub_str = raw.get('published')
        summary = raw.get('summary', '')

        if not title or not link:
            continue
        if is_spam(title):
            continue

        pub_dt = parse_date(pub_str) if pub_str else None

        # Watermark filter
        if wm_dt and pub_dt and pub_dt <= wm_dt:
            continue

        # Track newest seen
        if pub_dt and (newest_dt is None or pub_dt > newest_dt):
            newest_dt = pub_dt

        # Source-level keyword filter (if source has specific keywords)
        if keywords:
            text_lower = (title + ' ' + summary).lower()
            if not any(kw.lower() in text_lower for kw in keywords):
                continue

        # Cosmi relevance check
        topics = classify_topics(title, summary)

        items.append({
            'id': f"{src_id}-{hashlib.md5(link.encode()).hexdigest()[:8]}",
            'title': title,
            'url': link,
            'published': pub_dt.isoformat() if pub_dt else pub_str,
            'published_dt': pub_dt,
            'summary': summary[:350],
            'source_id': src_id,
            'source_label': label,
            'trust': trust,
            'topics': topics,
        })

    print(f"    → {len(items)} new relevant items (of {len(items_raw)} fetched)")
    return items, "ok", status_code, newest_dt


def deduplicate(items):
    hashes = []
    unique = []
    for item in items:
        h = simhash(item.get('title', '') + ' ' + (item.get('summary', '') or ''))
        is_dup = any(hamming_distance(h, eh) <= SIMHASH_THRESHOLD for eh in hashes)
        if not is_dup:
            hashes.append(h)
            unique.append(item)
    return unique


def main():
    run_start = datetime.now(timezone.utc)
    print(f"=== Regulation-Sweep 2026-06-13 (KW{KW}) ===")
    print(f"Start: {run_start.isoformat()}")

    watermarks = load_watermarks()
    all_items = []
    sources_ok = []
    sources_failed = []
    sources_404 = []
    watermark_updates = {}

    for source in REGULATION_SOURCES:
        result = fetch_source(source, watermarks)
        if len(result) == 3:
            items, status, code = result
            newest_dt = None
        else:
            items, status, code, newest_dt = result

        if status == "failed":
            sources_failed.append(source["id"])
            if code in (404, 403):
                sources_404.append(source["id"])
        else:
            sources_ok.append(source["id"])
            if newest_dt:
                watermark_updates[source["id"]] = newest_dt

        all_items.extend(items)
        time.sleep(0.4)

    print(f"\nRaw items collected: {len(all_items)}")
    print(f"Sources OK: {sources_ok}")
    print(f"Sources 404/failed: {sources_failed}")

    # Dedup
    all_items = deduplicate(all_items)
    print(f"After dedup: {len(all_items)} items")

    # Update watermarks for successful sources
    for src_id, newest_dt in watermark_updates.items():
        existing_str = watermarks.get(src_id)
        existing_dt = parse_date(existing_str) if existing_str else None
        if existing_dt is None or newest_dt > existing_dt:
            watermarks[src_id] = newest_dt.isoformat()

    save_watermarks(watermarks)
    print(f"Watermarks updated.")

    # Clean for JSON (remove datetime objects)
    items_clean = []
    for item in all_items:
        clean = {k: v for k, v in item.items() if k != 'published_dt'}
        items_clean.append(clean)

    # Write raw output
    raw_output = {
        "date": DATE_STR,
        "kw": KW,
        "run_start": run_start.isoformat(),
        "sources_ok": sources_ok,
        "sources_failed": sources_failed,
        "sources_404": sources_404,
        "items_scanned": sum(1 for _ in REGULATION_SOURCES),
        "items_after_filter": len(items_clean),
        "items": items_clean,
    }

    with open(RAW_FILE, 'w') as f:
        json.dump(raw_output, f, indent=2, ensure_ascii=False)
    print(f"Raw data written: {RAW_FILE}")

    run_end = datetime.now(timezone.utc)
    duration = round((run_end - run_start).total_seconds(), 1)
    print(f"\nFetch complete in {duration}s. {len(items_clean)} items for LLM analysis.")
    return raw_output


if __name__ == '__main__':
    main()
