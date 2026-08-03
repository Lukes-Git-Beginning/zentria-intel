#!/usr/bin/env python3
"""
Morning-Pulse script for 2026-08-03 (Monday)
Polls tier-1 sources, deduplicates, pre-filters, scores, and writes reports.
"""

import json
import re
import time
import hashlib
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys

START_TIME = time.time()
TODAY = "2026-08-03"
BASE = Path("/opt/zentria-intel")

# ── Config ──────────────────────────────────────────────────────────────────
SPAM_REGEX = [
    re.compile(r"(?i)(MSCI World|Bitcoin Kurs|Aktien-Tip|Crypto)"),
    re.compile(r"(?i)(Webinar zur|Anmeldung jetzt|Whitepaper Download)"),
    re.compile(r"(?i)(Black Friday|Cyber Monday|Sale)"),
    re.compile(r"(?i)(IPO|Boersengang|Quartalszahlen)"),
    re.compile(r"(?i)(Marvel|Disney|Hollywood)"),
    re.compile(r"(?i)^(Get started|Try free|Sign up)"),
]
MUTED_SOURCES = {
    "reddit-saas", "reddit-crm", "reddit-selfhosted",
    "reddit-germany-business", "reddit-startups-eu",
}

# Monday: full tier1 sweep (start of week, no tier2 rotation today)
# Watermarks
with open(BASE / ".state/watermarks.json") as f:
    watermarks = json.load(f)

# ── Module keyword maps ──────────────────────────────────────────────────────

def _make_kw_patterns(kw_list):
    compiled = []
    for kw in kw_list:
        if ' ' in kw or len(kw) > 8:
            compiled.append(re.compile(re.escape(kw), re.IGNORECASE))
        else:
            compiled.append(re.compile(r'\b' + re.escape(kw) + r'\b', re.IGNORECASE))
    return compiled

_MODULE_KW_RAW = {
    "crm-core": ["crm", "sales pipeline", "deal forecasting", "lead scoring",
                 "sales engagement", "revenue operations", "rev ops",
                 "hubspot", "pipedrive", "salesforce", "monday.com", "zoho crm", "bexio",
                 "twenty crm", "espocrm", "suitecrm", "odoo crm", "weclapp",
                 "contact management", "opportunity management"],
    "helpdesk": ["helpdesk", "help desk", "ticket management", "ticketing system",
                 "auto-triage", "ticket routing", "customer service automation",
                 "zendesk", "freshdesk", "zammad", "helpscout", "help scout",
                 "intercom helpdesk", "otrs", "support ticket", "sla management"],
    "buchhaltung": ["buchhaltung", "buchhalter", "e-rechnung", "xrechnung",
                    "zugferd", "gobd", "dunning", "mahnwesen", "lexoffice",
                    "sevdesk", "datev", "buchhaltungsbutler", "akaunting",
                    "easybill", "rechnungsstellung", "invoicing software",
                    "accounting software", "faktura"],
    "dialer": ["voip dialer", "cloud telephony", "call center software", "aircall",
               "justcall", "dialpad", "sipgate", "placetel", "business phone system",
               "click to call", "power dialer", "predictive dialer"],
    "video": ["webrtc", "video conferencing", "livekit", "mediasoup", "sfu server",
              "whereby", "daily.co", "janus gateway", "video sdk", "real-time video"],
    "wiki": ["knowledge base software", "wiki software", "notion", "confluence update",
             "outline wiki", "bookstack", "slab wiki", "team wiki"],
    "formulare": ["form builder", "typeform", "fillout", "jotform",
                  "online form", "web form builder", "tally form", "survey tool"],
    "vertraege": ["e-sign", "esignature", "electronic signature", "docusign", "skribble",
                  "pandadoc", "digital signature", "eidas", "contract management"],
    "rapporte": ["time tracking", "zeiterfassung", "project time", "timetac",
                 "crewmeister", "arbeitszeiterfassung", "stunden erfassen"],
    "schichten": ["shift planning", "schichtplan", "dienstplan", "papershift", "shyftplan",
                  "planday", "workforce scheduling", "schichtarbeit software"],
    "fuhrpark": ["fleet management", "fuhrparkmanagement", "vimcar", "fahrzeugflotte",
                 "fleet software", "flottenverwaltung", "kfz management"],
    "vermietung": ["rental management", "vermietungssoftware", "booqable", "rentle",
                   "equipment rental software", "mietverwaltung"],
    "inventar": ["inventory management", "inventarverwaltung", "warehouse management",
                 "lagerverwaltung", "pickware", "wms software", "stock management"],
    "einkauf": ["procurement software", "einkaufssoftware", "purchase order management",
                "lieferantenmanagement", "supplier management", "beschaffung software"],
    "produktion": ["production planning", "produktionsplanung", "manufacturing software",
                   "fertigungssteuerung", "bde software", "erp produktion"],
    "ai-in-crm": ["llm", "large language model", "ai copilot", "ai autopilot",
                  "ai drafts", "auto-triage ai", "ai autocomplete",
                  "agentic ai", "mcp server", "model context protocol",
                  "ai agent", "openai api", "anthropic claude", "gpt-4",
                  "ai in sales", "ai customer service", "ai workflow"],
    "eu-regulation": ["gdpr", "dsgvo", "nis2", "eu ai act", "eidas regulation",
                      "data protection law", "datenschutz gesetz", "edpb decision",
                      "bfdi", "data breach notification", "schrems"],
    "kmu-dach": ["kmu", "mittelstand", "kleines unternehmen", "dach-markt",
                 "digitalisierung mittelstand", "foerderprogramm",
                 "go-digital", "digital jetzt", "handwerk software"],
}

MODULE_KEYWORDS = {mod: _make_kw_patterns(kws) for mod, kws in _MODULE_KW_RAW.items()}

COMPETITOR_NAMES = [
    "pipedrive", "hubspot", "salesforce", "monday", "zoho", "bexio",
    "zendesk", "freshdesk", "zammad", "intercom", "helpscout",
    "odoo", "twenty", "espocrm", "suitecrm", "sevdesk", "lexoffice",
    "aircall", "justcall", "dialpad", "sipgate", "livekit",
    "typeform", "tally", "docusign", "skribble", "weclapp",
]

# ── Utility functions ─────────────────────────────────────────────────────────

def simhash64(text: str) -> int:
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

def hamming_distance(a: int, b: int) -> int:
    return bin(a ^ b).count('1')

def is_spam(title: str, text: str = "") -> bool:
    combined = (title or "") + " " + (text or "")
    for rx in SPAM_REGEX:
        if rx.search(combined):
            return True
    return False

def word_count(title: str) -> int:
    return len(title.split())

def module_match(item: dict) -> tuple[list[str], float]:
    text = (item.get("title") or "") + " " + (item.get("summary") or "")
    hint = item.get("module_hint", "")
    matched = []
    for mod, patterns in MODULE_KEYWORDS.items():
        for pat in patterns:
            if pat.search(text):
                matched.append(mod)
                break
    if hint and hint in MODULE_KEYWORDS and hint not in matched:
        matched.insert(0, hint)
    score = min(len(matched) * 0.3 + 0.4, 2.0) if matched else 0.0
    return matched, score

def recency_decay(published_at: str) -> float:
    try:
        for fmt in ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z",
                    "%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S GMT"]:
            try:
                dt = datetime.strptime(published_at, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                break
            except ValueError:
                continue
        else:
            return 0.5
        now = datetime.now(timezone.utc)
        age_hours = (now - dt).total_seconds() / 3600
        if age_hours < 0:
            age_hours = 0
        return max(0.1, 1.0 - (age_hours / 96))
    except Exception:
        return 0.5

def competitor_bonus(item: dict) -> float:
    text = (item.get("title","") + " " + item.get("summary","")).lower()
    for name in COMPETITOR_NAMES:
        if name in text:
            return 1.3
    return 1.0

def fetch_url(url: str, timeout: int = 12) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "zentria-intel/1.0 (+https://zentria.de/bot)",
            "Accept": "application/rss+xml, application/atom+xml, text/xml, application/json, */*"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None

def parse_rss_atom(data: bytes, source_id: str, source_trust: int) -> list[dict]:
    items = []
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return items

    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'media': 'http://search.yahoo.com/mrss/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
    }

    tag = root.tag.lower()

    if 'feed' in tag or root.tag == '{http://www.w3.org/2005/Atom}feed':
        for entry in root.findall('atom:entry', ns) or root.findall('{http://www.w3.org/2005/Atom}entry'):
            title_el = entry.find('atom:title', ns) or entry.find('{http://www.w3.org/2005/Atom}title')
            link_el = entry.find('atom:link', ns) or entry.find('{http://www.w3.org/2005/Atom}link')
            published_el = (entry.find('atom:published', ns) or
                           entry.find('{http://www.w3.org/2005/Atom}published') or
                           entry.find('atom:updated', ns) or
                           entry.find('{http://www.w3.org/2005/Atom}updated'))
            summary_el = (entry.find('atom:summary', ns) or
                         entry.find('{http://www.w3.org/2005/Atom}summary') or
                         entry.find('atom:content', ns) or
                         entry.find('{http://www.w3.org/2005/Atom}content'))

            title = title_el.text if title_el is not None else ""
            url = ""
            if link_el is not None:
                url = link_el.get('href', link_el.text or "")
            published = published_el.text if published_el is not None else ""
            summary = summary_el.text if summary_el is not None else ""
            if summary:
                summary = re.sub(r'<[^>]+>', ' ', summary)[:300].strip()

            if title and url:
                items.append({
                    "title": title.strip(),
                    "url": url.strip(),
                    "published_at": published,
                    "summary": summary,
                    "source_id": source_id,
                    "trust": source_trust,
                })
    else:
        channel = root.find('channel')
        if channel is None:
            channel = root

        for item_el in channel.findall('item'):
            title_el = item_el.find('title')
            link_el = item_el.find('link')
            pubdate_el = item_el.find('pubDate')
            desc_el = item_el.find('description')

            title = title_el.text if title_el is not None else ""
            url = link_el.text if link_el is not None else ""
            published = pubdate_el.text if pubdate_el is not None else ""
            summary = desc_el.text if desc_el is not None else ""
            if summary:
                summary = re.sub(r'<[^>]+>', ' ', summary)[:300].strip()

            if title and url:
                items.append({
                    "title": title.strip(),
                    "url": url.strip() if url else "",
                    "published_at": published,
                    "summary": summary,
                    "source_id": source_id,
                    "trust": source_trust,
                })
    return items

# ── Define tier-1 sources to poll ─────────────────────────────────────────────

SOURCES = [
    # CRM-Core competitors
    {"id": "pipedrive-rss-crm-core", "url": "https://www.pipedrive.com/en/blog/feed", "type": "rss", "trust": 8, "module": "crm-core", "label": "Pipedrive Blog"},
    {"id": "hubspot-marketing-crm-core", "url": "https://blog.hubspot.com/marketing/rss.xml", "type": "rss", "trust": 8, "module": "crm-core", "label": "HubSpot Marketing Blog", "max_items": 10},
    {"id": "hubspot-product-updates", "url": "https://product-updates.hubspot.com/rss", "type": "rss", "trust": 9, "module": "crm-core", "label": "HubSpot Product Updates"},
    {"id": "salesforce-rss-crm-core", "url": "https://www.salesforce.com/news/feed/", "type": "rss", "trust": 7, "module": "crm-core", "label": "Salesforce News"},
    {"id": "monday-crm", "url": "https://monday.com/blog/feed/", "type": "rss", "trust": 7, "module": "crm-core", "label": "monday.com Blog"},
    {"id": "bexio-rss-crm-core", "url": "https://www.bexio.com/de-CH/blog/feed", "type": "rss", "trust": 8, "module": "crm-core", "label": "Bexio Blog"},
    {"id": "odoo-rss-crm-core", "url": "https://www.odoo.com/blog/our-blog-1/rss", "type": "rss", "trust": 7, "module": "crm-core", "label": "Odoo Blog"},
    {"id": "odoo-releases", "url": "https://github.com/odoo/odoo/releases.atom", "type": "atom", "trust": 8, "module": "crm-core", "label": "Odoo GitHub Releases"},
    {"id": "twenty-atom-crm-core", "url": "https://github.com/twentyhq/twenty/releases.atom", "type": "atom", "trust": 8, "module": "crm-core", "label": "Twenty GitHub Releases"},
    {"id": "espocrm-atom-crm-core", "url": "https://github.com/espocrm/espocrm/releases.atom", "type": "atom", "trust": 7, "module": "crm-core", "label": "EspoCRM GitHub Releases"},
    {"id": "suitecrm-atom-crm-core", "url": "https://github.com/salesagility/SuiteCRM/releases.atom", "type": "atom", "trust": 6, "module": "crm-core", "label": "SuiteCRM GitHub Releases"},
    # Helpdesk
    {"id": "zendesk-rss-helpdesk", "url": "https://www.zendesk.com/blog/feed/", "type": "rss", "trust": 8, "module": "helpdesk", "label": "Zendesk Blog"},
    {"id": "intercom-rss-helpdesk", "url": "https://www.intercom.com/blog/feed/", "type": "rss", "trust": 8, "module": "helpdesk", "label": "Intercom Blog"},
    {"id": "helpscout-rss-helpdesk", "url": "https://www.helpscout.com/blog/feed/", "type": "rss", "trust": 7, "module": "helpdesk", "label": "HelpScout Blog"},
    {"id": "zammad-atom-helpdesk", "url": "https://github.com/zammad/zammad/releases.atom", "type": "atom", "trust": 8, "module": "helpdesk", "label": "Zammad GitHub Releases"},
    {"id": "front-rss-helpdesk", "url": "https://front.com/blog/rss.xml", "type": "rss", "trust": 7, "module": "helpdesk", "label": "Front Blog"},
    # Buchhaltung
    {"id": "lexoffice-rss-buchhaltung", "url": "https://www.lexoffice.de/blog/feed/", "type": "rss", "trust": 8, "module": "buchhaltung", "label": "Lexoffice Blog"},
    {"id": "sevdesk-rss-buchhaltung", "url": "https://sevdesk.de/blog/feed/", "type": "rss", "trust": 8, "module": "buchhaltung", "label": "sevDesk Blog"},
    {"id": "akaunting-(open-source)-atom-buchhaltung", "url": "https://github.com/akaunting/akaunting/releases.atom", "type": "atom", "trust": 6, "module": "buchhaltung", "label": "Akaunting GitHub Releases"},
    {"id": "easybill-rss-buchhaltung", "url": "https://www.easybill.de/blog/feed/", "type": "rss", "trust": 6, "module": "buchhaltung", "label": "easybill Blog"},
    # Tech trends
    {"id": "hackernews-front", "url": "https://hacker-news.firebaseio.com/v0/topstories.json", "type": "hn-json", "trust": 7, "module": "ai-in-crm", "label": "HackerNews Frontpage"},
    {"id": "selfh-st", "url": "https://selfh.st/rss/", "type": "rss", "trust": 7, "module": "kmu-dach", "label": "selfh.st"},
    {"id": "diginomica", "url": "https://diginomica.com/feed", "type": "rss", "trust": 6, "module": "crm-core", "label": "diginomica"},
    {"id": "techcrunch-funding", "url": "https://techcrunch.com/category/venture/feed/", "type": "rss", "trust": 7, "module": "ai-in-crm", "label": "TechCrunch Venture"},
    {"id": "sifted-eu", "url": "https://sifted.eu/feed", "type": "rss", "trust": 8, "module": "kmu-dach", "label": "Sifted EU"},
    {"id": "deutsche-startups", "url": "https://www.deutsche-startups.de/feed/", "type": "rss", "trust": 8, "module": "kmu-dach", "label": "deutsche-startups.de"},
    {"id": "eu-startups", "url": "https://www.eu-startups.com/feed/", "type": "rss", "trust": 7, "module": "kmu-dach", "label": "EU-Startups.com"},
    {"id": "anthropic-news", "url": "https://www.anthropic.com/news/rss.xml", "type": "rss", "trust": 9, "module": "ai-in-crm", "label": "Anthropic News"},
    {"id": "openai-news", "url": "https://openai.com/blog/rss/", "type": "rss", "trust": 8, "module": "ai-in-crm", "label": "OpenAI Blog"},
    {"id": "indiehackers", "url": "https://www.indiehackers.com/feed.xml", "type": "rss", "trust": 6, "module": "crm-core", "label": "Indie Hackers"},
    # Themes
    {"id": "theme-ai-in-crm-rss", "url": "https://aitidbits.ai/feed", "type": "rss", "trust": 7, "module": "ai-in-crm", "label": "AI Tidbits"},
    {"id": "theme-ai-in-crm-lenny", "url": "https://www.lennysnewsletter.com/feed", "type": "rss", "trust": 8, "module": "ai-in-crm", "label": "Lenny's Newsletter"},
    {"id": "theme-eu-cloud-heise", "url": "https://www.heise.de/rss/heise-atom.xml", "type": "atom", "trust": 8, "module": "eu-regulation", "label": "heise online", "max_items": 15,
     "cosmi_stack_filter": re.compile(r"(?i)(dsgvo|datenschutz|gaia.?x|souveränität|cloud|saas|crm|ki.?gesetz|ai act|nis2|eidas|open.?source|self.?host|kubernetes|microservice|api|llm|ki.?(trend|tool|system)|verschlüsselung|rechenzentrum|datenleck|cyberangriff|sicherheitslücke)")},
    {"id": "gaia-x", "url": "https://www.gaia-x.eu/feed", "type": "rss", "trust": 9, "module": "eu-regulation", "label": "GAIA-X"},
    {"id": "webrtchacks", "url": "https://webrtchacks.com/feed/", "type": "rss", "trust": 9, "module": "video", "label": "WebRTC Hacks"},
    {"id": "livekit-releases", "url": "https://github.com/livekit/livekit/releases.atom", "type": "atom", "trust": 7, "module": "video", "label": "LiveKit GitHub Releases"},
    # Regulation
    {"id": "edpb-newsroom", "url": "https://www.edpb.europa.eu/news/news_en?sort_by=created&sort_order=DESC&format=feed", "type": "rss", "trust": 10, "module": "eu-regulation", "label": "EDPB Newsroom", "max_items": 10},
    {"id": "bsi-warnungen", "url": "https://wid.cert-bund.de/content/public/securityAdvisory/rss", "type": "rss", "trust": 8, "module": "eu-regulation", "label": "BSI Warnungen", "max_items": 5,
     "cosmi_stack_filter": re.compile(r"(?i)(postgres|postg|cloud|saas|docker|kubernetes|nginx|grafana|python|django|flask|node\.?js|react|golang|go\b|grpc|redis|minio|keycloak|vault|oauth|openid)")},
    {"id": "noyb", "url": "https://noyb.eu/en/feed", "type": "rss", "trust": 8, "module": "eu-regulation", "label": "noyb.eu", "max_items": 10},
    {"id": "betalist", "url": "https://betalist.com/feed", "type": "rss", "trust": 5, "module": "crm-core", "label": "BetaList"},
    {"id": "pipedrive-api-docs", "url": "https://github.com/pipedrive/api-docs/releases.atom", "type": "atom", "trust": 7, "module": "crm-core", "label": "Pipedrive API Docs"},
    {"id": "freshdesk-rss-helpdesk", "url": "https://www.freshworks.com/freshdesk/blog/feed/", "type": "rss", "trust": 7, "module": "helpdesk", "label": "Freshdesk Blog"},
    {"id": "sipgate-rss-dialer", "url": "https://www.sipgate.de/rss", "type": "rss", "trust": 7, "module": "dialer", "label": "sipgate Blog"},
    {"id": "theme-ux-smashing", "url": "https://www.smashingmagazine.com/feed/", "type": "rss", "trust": 8, "module": "kmu-dach", "label": "Smashing Magazine", "max_items": 5},
]

# ── Poll sources ─────────────────────────────────────────────────────────────

print("Polling sources...", flush=True)

all_items = []
source_results = {}
new_watermarks = dict(watermarks)

HN_KW = {"crm", "saas", "kmu", "small business", "b2b", "llm", "mcp",
          "model context protocol", "eu gdpr", "gdpr", "sovereignty", "self-hosted",
          "helpdesk", "sales pipeline", "customer support", "automation platform",
          "claude api", "openai api", "ai agent", "ai workflow",
          "open source crm", "open source erp", "business software"}

for src in SOURCES:
    src_id = src["id"]
    if src_id in MUTED_SOURCES:
        source_results[src_id] = {"status": "muted", "count": 0}
        continue

    src_wm = watermarks.get(src_id)

    if src["type"] == "hn-json":
        data = fetch_url(src["url"])
        if data is None:
            source_results[src_id] = {"status": "error", "error": "fetch failed", "count": 0}
            continue
        try:
            story_ids = json.loads(data)[:30]
        except Exception:
            source_results[src_id] = {"status": "error", "error": "parse failed", "count": 0}
            continue

        fetched = 0
        for story_id in story_ids[:30]:
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            item_data = fetch_url(item_url, timeout=8)
            if item_data is None:
                continue
            try:
                story = json.loads(item_data)
            except Exception:
                continue
            if story.get("type") != "story":
                continue
            title = story.get("title", "")
            url = story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
            time_ts = story.get("time", 0)
            published_at = datetime.fromtimestamp(time_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if time_ts else ""

            text_lower = title.lower()
            if not any(kw in text_lower for kw in HN_KW):
                continue

            all_items.append({
                "title": title,
                "url": url,
                "published_at": published_at,
                "summary": story.get("text", "")[:300] if story.get("text") else "",
                "source_id": src_id,
                "trust": src["trust"],
                "module_hint": src["module"],
            })
            fetched += 1
            if fetched >= 15:
                break

        source_results[src_id] = {"status": "ok", "count": fetched, "label": src["label"]}
        if fetched > 0:
            new_watermarks[src_id] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        continue

    # RSS / Atom
    data = fetch_url(src["url"])
    if data is None:
        source_results[src_id] = {"status": "error", "error": "fetch failed", "count": 0, "label": src.get("label", src_id)}
        continue

    parsed = parse_rss_atom(data, src_id, src["trust"])

    max_items = src.get("max_items", 50)
    cosmi_filter = src.get("cosmi_stack_filter")

    source_items = []
    max_ts = src_wm
    for item in parsed:
        pub = item.get("published_at", "")
        item["module_hint"] = src["module"]

        if cosmi_filter:
            text_check = (item.get("title") or "") + " " + (item.get("summary") or "")
            if not cosmi_filter.search(text_check):
                continue

        source_items.append(item)
        if pub:
            if max_ts is None or pub > max_ts:
                max_ts = pub
        if len(source_items) >= max_items:
            break

    all_items.extend(source_items)
    source_results[src_id] = {"status": "ok", "count": len(source_items), "label": src.get("label", src_id)}
    if max_ts:
        new_watermarks[src_id] = max_ts

print(f"Total raw items: {len(all_items)}", flush=True)
items_scanned = len(all_items)

# ── Dedup via SimHash ─────────────────────────────────────────────────────────

print("Deduplicating...", flush=True)

def item_hash(item: dict) -> int:
    text = (item.get("title") or "") + (item.get("url") or "") + (item.get("summary") or "")[:200]
    return simhash64(text)

deduped = []
seen_hashes = []
for item in all_items:
    h = item_hash(item)
    is_dup = False
    for sh in seen_hashes:
        if hamming_distance(h, sh) <= 3:
            is_dup = True
            break
    if not is_dup:
        seen_hashes.append(h)
        deduped.append(item)

print(f"After dedup: {len(deduped)}", flush=True)
items_after_dedup = len(deduped)

# ── Pre-filter ─────────────────────────────────────────────────────────────────

print("Pre-filtering...", flush=True)

def passes_prefilter(item: dict) -> bool:
    title = item.get("title") or ""
    summary = item.get("summary") or ""

    if is_spam(title, summary):
        return False

    if word_count(title) <= 5:
        text = (title + " " + summary)
        has_module_kw = False
        for patterns in MODULE_KEYWORDS.values():
            if any(pat.search(text) for pat in patterns):
                has_module_kw = True
                break
        if not has_module_kw:
            return False

    text = (title + " " + summary).lower()
    for kw in ["ipo", "boersengang", "quartalszahlen", "marvel", "disney", "hollywood"]:
        if kw in text:
            return False

    if not title.strip():
        return False

    return True

filtered = [item for item in deduped if passes_prefilter(item)]
print(f"After pre-filter: {len(filtered)}", flush=True)
items_after_prefilter = len(filtered)

# ── Pre-score ──────────────────────────────────────────────────────────────────

print("Scoring...", flush=True)

from urllib.parse import urlparse
from collections import defaultdict

def title_key(title: str) -> str:
    words = re.findall(r'\w+', (title or "").lower())
    return " ".join(words[:6])

title_source_sets = defaultdict(set)
for item in filtered:
    tk = title_key(item.get("title", ""))
    if tk:
        title_source_sets[tk].add(item.get("source_id",""))

for item in filtered:
    mods, mod_score = module_match(item)
    item["matched_modules"] = mods
    src_trust = item.get("trust", 5) / 10.0
    rec = recency_decay(item.get("published_at",""))
    tk = title_key(item.get("title",""))
    n_sources = len(title_source_sets.get(tk, {item.get("source_id","")}))
    comp = competitor_bonus(item)

    if mods and mods[0] == item.get("module_hint") and len(mods) == 1:
        effective_mod_score = 0.25
    elif not mods:
        effective_mod_score = 0.1
    else:
        effective_mod_score = mod_score

    score = effective_mod_score * src_trust * rec * (1 + 0.2 * n_sources) * comp
    item["score"] = round(score, 4)
    item["recency"] = round(rec, 3)
    item["n_sources"] = n_sources

filtered.sort(key=lambda x: x["score"], reverse=True)

# ── Mark Hot-Items ─────────────────────────────────────────────────────────────

hot_items = filtered[:20]
for i, item in enumerate(hot_items):
    item["hot_id"] = f"MOR-{TODAY}-i{i+1:02d}"

# ── Write hot_items JSON ───────────────────────────────────────────────────────

hot_ids_data = {
    "date": TODAY,
    "routine": "intel-morning",
    "hot_items": [
        {
            "id": item["hot_id"],
            "title": item["title"],
            "url": item["url"],
            "score": item["score"],
            "modules": item.get("matched_modules", []),
            "source_id": item["source_id"],
        }
        for item in hot_items
    ]
}

hot_items_path = BASE / f".state/hot_items_{TODAY}.json"
with open(hot_items_path, "w") as f:
    json.dump(hot_ids_data, f, indent=2, ensure_ascii=False)
print(f"Wrote {hot_items_path}", flush=True)

# ── Build module breakdown ─────────────────────────────────────────────────────

MODULE_LABELS = {
    "crm-core": "CRM-Core",
    "helpdesk": "Helpdesk",
    "buchhaltung": "Buchhaltung",
    "dialer": "Dialer",
    "video": "Video",
    "wiki": "Wiki",
    "formulare": "Formulare",
    "vertraege": "Vertraege",
    "rapporte": "Rapporte",
    "schichten": "Schichten",
    "fuhrpark": "Fuhrpark",
    "vermietung": "Vermietung",
    "inventar": "Inventar",
    "einkauf": "Einkauf",
    "produktion": "Produktion",
    "ai-in-crm": "AI-in-CRM",
    "eu-regulation": "EU-Regulation",
    "kmu-dach": "KMU-DACH",
}

module_buckets = {m: [] for m in MODULE_LABELS}
hot_set = {item["hot_id"] for item in hot_items}

for item in filtered[:60]:
    mods = item.get("matched_modules", [])
    primary = item.get("module_hint") if item.get("module_hint") in MODULE_LABELS else (mods[0] if mods else None)
    if primary and primary in module_buckets:
        if len(module_buckets[primary]) < 5:
            module_buckets[primary].append(item)

# ── Write morning report ───────────────────────────────────────────────────────

runtime = round((time.time() - START_TIME) / 60, 1)
ok_sources = sum(1 for v in source_results.values() if v.get("status") == "ok")
failed_sources = [k for k, v in source_results.items() if v.get("status") == "error"]
muted_count = len(MUTED_SOURCES)
total_sources_polled = len(SOURCES)

dedup_pct = round((1 - items_after_dedup/max(items_scanned,1))*100)
filter_pct = round((1 - items_after_prefilter/max(items_after_dedup,1))*100)

tokens_input_est = items_scanned * 80
tokens_output_est = 3500

report_lines = [
    "---",
    f"date: {TODAY}",
    "type: morning",
    f"runtime_minutes: {runtime}",
    f"tokens_input: {tokens_input_est}",
    f"tokens_output: {tokens_output_est}",
    f"items_scanned: {items_scanned}",
    f"items_after_dedup: {items_after_dedup}",
    f"items_after_prefilter: {items_after_prefilter}",
    "hot_items_count: 20",
    "pool_pct_used: 4",
    "---",
    "",
    f"# Morning-Pulse {TODAY} (Mo)",
    "",
    "## Status",
    f"- {items_scanned} Roh-Items von {ok_sources}/{total_sources_polled} Quellen ({muted_count} weitere per settings.yaml muted)",
    f"- {items_after_dedup} nach Dedup (-{dedup_pct}%)",
    f"- {items_after_prefilter} nach Pre-Filter (-{filter_pct}%)",
    "- Top-20 als Hot-Items markiert fuer intel-deep heute Abend",
    "",
    "## Modul-Breakdown",
]

active_modules = []
silent_modules = []

for mod_id, label in MODULE_LABELS.items():
    items_in_mod = module_buckets.get(mod_id, [])
    matched_to_mod = [it for it in filtered[:60] if mod_id in it.get("matched_modules", [])]
    hot_in_mod = [it for it in hot_items if mod_id in it.get("matched_modules", [])]

    if not matched_to_mod and not items_in_mod:
        silent_modules.append(label)
        continue

    display_items = items_in_mod if items_in_mod else matched_to_mod[:4]
    total_in_mod = len(matched_to_mod)
    hot_count = len(hot_in_mod)

    if total_in_mod == 0:
        silent_modules.append(label)
        continue

    active_modules.append(mod_id)
    report_lines.append(f"\n### {label} ({total_in_mod} Items, {hot_count} Hot)")

    for item in display_items[:4]:
        title = item["title"]
        url = item["url"]
        score = item["score"]
        n_src = item.get("n_sources", 1)
        summary = item.get("summary", "")[:200].strip()
        hot_marker = f" `{item['hot_id']}`" if item.get("hot_id") else ""
        report_lines.append(f"- [{title}]({url}) — score:{score}, n_sources:{n_src}{hot_marker}")
        if summary:
            report_lines.append(f"  > {summary}")

# Hot items list
report_lines.append("\n## Hot-Items-Liste (sortiert nach score)")
for i, item in enumerate(hot_items, 1):
    mods_str = ",".join(item.get("matched_modules", [item.get("module_hint","?")])[:2])
    report_lines.append(f"{i}. `{item['hot_id']}` {item['title']} — modul:{mods_str} — score:{item['score']}")

# Silent modules
report_lines.append("\n## Stille Module")
if silent_modules:
    for m in silent_modules:
        report_lines.append(f"- {m}: keine relevanten Items heute")
else:
    report_lines.append("- (alle Module mit Items versorgt)")

# Source status
report_lines.append("\n## Quellen-Status")
report_lines.append(f"- {ok_sources}/{total_sources_polled} erfolgreich gepollt ({len(failed_sources)} Fehler, {muted_count} muted per settings.yaml)")
if failed_sources:
    report_lines.append(f"- Failures: {', '.join(failed_sources)}")
else:
    report_lines.append("- Failures: keine")

report_lines.append("\n### Quellen-Detail")
for src in SOURCES:
    sid = src["id"]
    if sid in MUTED_SOURCES:
        report_lines.append(f"  - `{sid}`: MUTED (Reddit Responsible Builder Policy Nov 2025)")
    elif sid in source_results:
        res = source_results[sid]
        st = res.get("status","?")
        cnt = res.get("count", 0)
        label = src.get("label", sid)
        if st == "ok":
            report_lines.append(f"  - `{sid}` ({label}): OK, {cnt} Items")
        else:
            err = res.get("error","")
            report_lines.append(f"  - `{sid}` ({label}): FEHLER — {err}")

report_md = "\n".join(report_lines)

output_path = BASE / f"daily/{TODAY}-morning.md"
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w") as f:
    f.write(report_md)
print(f"Wrote {output_path}", flush=True)

# ── Update watermarks ──────────────────────────────────────────────────────────

new_watermarks[TODAY + "-morning-run"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(BASE / ".state/watermarks.json", "w") as f:
    json.dump(new_watermarks, f, indent=2, ensure_ascii=False)
print("Updated watermarks", flush=True)

# ── Append run stats ───────────────────────────────────────────────────────────

run_stats = {
    "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "routine": "intel-morning",
    "date": TODAY,
    "runtime_minutes": runtime,
    "items_scanned": items_scanned,
    "items_after_dedup": items_after_dedup,
    "items_after_prefilter": items_after_prefilter,
    "hot_items": len(hot_items),
    "sources_ok": ok_sources,
    "sources_failed": len(failed_sources),
    "sources_muted": muted_count,
    "tokens_input_est": tokens_input_est,
    "tokens_output_est": tokens_output_est,
}

runs_path = BASE / ".state/runs.jsonl"
with open(runs_path, "a") as f:
    f.write(json.dumps(run_stats, ensure_ascii=False) + "\n")
print("Appended run stats", flush=True)

print(f"\n=== DONE === runtime={runtime}min items_scanned={items_scanned} after_dedup={items_after_dedup} after_filter={items_after_prefilter} hot={len(hot_items)}", flush=True)
print("Hot items preview:")
for item in hot_items[:5]:
    print(f"  {item['hot_id']} [{item['score']}] {item['title'][:80]}", flush=True)
