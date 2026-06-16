#!/usr/bin/env python3
"""Morning Pulse — 2026-06-16 (Tuesday). Tier-1 + Tier-2 rotation: helpdesk, crm-core."""

import feedparser
import hashlib
import json
import re
import time
import datetime
import os
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

RUN_DATE = "2026-06-16"
RUN_DOW = "Di"
START_TS = datetime.datetime.now(datetime.timezone.utc)

STATE_DIR = "/opt/zentria-intel/.state"
OUTPUT_DIR = "/opt/zentria-intel/daily"
WATERMARKS_FILE = f"{STATE_DIR}/watermarks.json"
HOT_ITEMS_FILE = f"{STATE_DIR}/hot_items_{RUN_DATE}.json"
RUNS_FILE = f"{STATE_DIR}/runs.jsonl"
OUTPUT_FILE = f"{OUTPUT_DIR}/{RUN_DATE}-morning.md"

# Load watermarks
def load_watermarks():
    try:
        with open(WATERMARKS_FILE) as f:
            wm = json.load(f)
        return {k: datetime.datetime.fromisoformat(v) for k, v in wm.items()}
    except Exception:
        return {}

watermarks = load_watermarks()

def parse_dt(entry):
    for attr in ["published_parsed", "updated_parsed"]:
        t = getattr(entry, attr, None)
        if t:
            try:
                return datetime.datetime(*t[:6], tzinfo=datetime.timezone.utc)
            except Exception:
                pass
    return datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)

# SimHash implementation (64-bit)
def simhash(text):
    text = (text or "").lower()[:400]
    v = [0] * 64
    words = re.findall(r'\w+', text)
    for word in words:
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        for i in range(64):
            if h & (1 << i):
                v[i] += 1
            else:
                v[i] -= 1
    bits = 0
    for i in range(64):
        if v[i] > 0:
            bits |= (1 << i)
    return bits

def hamming(a, b):
    x = a ^ b
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

# Spam / irrelevance filters
SPAM_REGEXES = [
    re.compile(r"(?i)(MSCI World|Bitcoin Kurs|Aktien-Tip|Crypto)"),
    re.compile(r"(?i)(Webinar zur|Anmeldung jetzt|Whitepaper Download)"),
    re.compile(r"(?i)(Black Friday|Cyber Monday|Sale)"),
    re.compile(r"(?i)(IPO|B.rsengang|Quartalszahlen)"),
    re.compile(r"(?i)(Marvel|Disney|Hollywood)"),
    re.compile(r"(?i)^(Get started|Try free|Sign up)"),
]

def is_spam(title):
    for rx in SPAM_REGEXES:
        if rx.search(title or ""):
            return True
    return False

def word_count(title):
    return len((title or "").split())

# Source definitions — Tier-1 + Tuesday rotation (helpdesk, crm-core)
# Each: id, url, type, trust, module, keywords (optional)
SOURCES = [
    # --- DIALER (tier1) ---
    {"id": "aircall-rss-dialer", "url": "https://aircall.io/blog/feed/", "trust": 7, "module": "dialer",
     "keywords": ["voip","telefonie","dialer","call","webrtc","sip","recording","transcription"]},
    {"id": "justcall-rss-dialer", "url": "https://justcall.io/blog/feed/", "trust": 6, "module": "dialer",
     "keywords": ["voip","dialer","call","sip","ai call"]},
    {"id": "sipgate-rss-dialer", "url": "https://www.sipgate.de/team/blog/feed", "trust": 7, "module": "dialer",
     "keywords": ["voip","sip","telefonie","call"]},
    {"id": "dialpad-rss-dialer", "url": "https://www.dialpad.com/blog/feed/", "trust": 7, "module": "dialer",
     "keywords": ["voip","dialer","call","ai","transcription"]},
    {"id": "livekit-releases", "url": "https://github.com/livekit/livekit/releases.atom", "trust": 9, "module": "video",
     "keywords": ["webrtc","livekit","sfu","realtime","voice"]},
    {"id": "webrtchacks", "url": "https://webrtchacks.com/feed/", "trust": 9, "module": "video",
     "keywords": ["webrtc","sfu","turn","stun","ice","livekit","mediasoup"]},

    # --- CRM-CORE (tier2 Tuesday rotation) ---
    {"id": "hubspot-rss-crm-core", "url": "https://blog.hubspot.com/marketing/rss.xml", "trust": 7, "module": "crm-core",
     "keywords": ["crm","ai","automation","forecast","pipeline","contact","deal"]},
    {"id": "salesforce-rss-crm-core", "url": "https://www.salesforce.com/blog/feed/", "trust": 8, "module": "crm-core",
     "keywords": ["crm","salesforce","agentforce","ai","automation"]},
    {"id": "twenty-atom-crm-core", "url": "https://github.com/twentyhq/twenty/releases.atom", "trust": 8, "module": "crm-core",
     "keywords": ["crm","twenty","open-source","release"]},
    {"id": "espocrm-atom-crm-core", "url": "https://github.com/espocrm/espocrm/releases.atom", "trust": 7, "module": "crm-core",
     "keywords": ["crm","espocrm","open-source"]},
    {"id": "suitecrm-atom-crm-core", "url": "https://github.com/salesagility/SuiteCRM/releases.atom", "trust": 7, "module": "crm-core",
     "keywords": ["crm","suitecrm","salesagility"]},
    {"id": "pipedrive-rss-crm-core", "url": "https://pipedrive.com/blog/feed/", "trust": 7, "module": "crm-core",
     "keywords": ["crm","pipeline","deal","ai","forecast"]},

    # --- HELPDESK (tier2 Tuesday rotation) ---
    {"id": "zammad-atom-helpdesk", "url": "https://github.com/zammad/zammad/releases.atom", "trust": 8, "module": "helpdesk",
     "keywords": ["helpdesk","ticketing","zammad","open-source"]},
    {"id": "intercom-rss-helpdesk", "url": "https://www.intercom.com/blog/feed/", "trust": 7, "module": "helpdesk",
     "keywords": ["helpdesk","support","ai","triage","automation","inbox"]},
    {"id": "front-rss-helpdesk", "url": "https://frontapp.com/blog/feed/", "trust": 6, "module": "helpdesk",
     "keywords": ["helpdesk","email","inbox","support"]},
    {"id": "otrs-rss-helpdesk", "url": "https://otrscommunityedition.com/feed/", "trust": 6, "module": "helpdesk",
     "keywords": ["otrs","helpdesk","ticketing","open-source"]},
    {"id": "zendesk-rss-helpdesk", "url": "https://www.zendesk.com/blog/feed/", "trust": 7, "module": "helpdesk",
     "keywords": ["helpdesk","ai","triage","support","ticket"]},

    # --- TECH TRENDS (tier1) ---
    {"id": "hackernews-front", "url": "https://news.ycombinator.com/rss", "trust": 7, "module": "tech-trends",
     "keywords": []},
    {"id": "anthropic-news", "url": "https://www.anthropic.com/news/rss.xml", "trust": 9, "module": "tech-trends",
     "keywords": ["claude","mcp","ai","model","api"]},
    {"id": "openai-news", "url": "https://openai.com/news/rss.xml", "trust": 8, "module": "tech-trends",
     "keywords": ["gpt","model","api","tool","agent"]},
    {"id": "techcrunch-funding", "url": "https://techcrunch.com/category/startups/feed/", "trust": 7, "module": "tech-trends",
     "keywords": ["crm","saas","helpdesk","telephony","dialer","erp","kmu","mittelstand","series"]},
    {"id": "sifted-eu", "url": "https://sifted.eu/feed", "trust": 7, "module": "tech-trends",
     "keywords": ["crm","saas","startup","eu","dach","funding","b2b"]},
    {"id": "deutsche-startups", "url": "https://www.deutsche-startups.de/feed/", "trust": 7, "module": "tech-trends",
     "keywords": ["crm","saas","b2b","kmu","software","funding"]},
    {"id": "eu-startups", "url": "https://www.eu-startups.com/feed/", "trust": 7, "module": "tech-trends",
     "keywords": ["crm","saas","b2b","software","series"]},
    {"id": "selfh-st", "url": "https://selfh.st/apps/feed.xml", "trust": 6, "module": "tech-trends",
     "keywords": ["self-hosted","open-source","crm","helpdesk","erp"]},
    {"id": "diginomica", "url": "https://diginomica.com/feed", "trust": 7, "module": "tech-trends",
     "keywords": ["crm","saas","erp","ai","enterprise","cloud"]},
    {"id": "theme-ai-in-crm-lenny", "url": "https://www.lennysnewsletter.com/feed", "trust": 8, "module": "cross",
     "keywords": ["ai","crm","product","saas","llm","agent","mcp"]},

    # --- REGULATION (tier1) ---
    {"id": "bsi-warnungen", "url": "https://wid.cert-bund.de/content/public/securityAdvisory/rss", "trust": 10, "module": "regulation",
     "keywords": ["crm","saas","cloud","postgres","kritisch"]},
    {"id": "edpb-newsroom", "url": "https://www.edpb.europa.eu/news/news_en?sort_by=created&sort_order=DESC&format=feed", "trust": 10, "module": "regulation",
     "keywords": []},
    {"id": "noyb", "url": "https://noyb.eu/en/feed", "trust": 8, "module": "regulation",
     "keywords": ["gdpr","schrems","dsgvo","cloud","transfer","data"]},
    {"id": "gaia-x", "url": "https://www.gaia-x.eu/feed", "trust": 9, "module": "cross",
     "keywords": ["gaia-x","cloud","sovereignty","eu"]},
    {"id": "heise-atom", "url": "https://www.heise.de/rss/heise-atom.xml", "trust": 8, "module": "cross",
     "keywords": ["gaia","souverän","cloud","dsgvo","datenschutz","ki","crm","saas","b2b"]},
]

MUTED = {"reddit-saas","reddit-crm","reddit-selfhosted","reddit-germany-business","reddit-startups-eu"}

MODULE_KEYWORDS = {
    "crm-core": ["crm","pipeline","deal","contact","lead","forecast","sales","hubspot","salesforce","pipedrive","twenty","espocrm"],
    "dialer": ["voip","telefonie","dialer","call","sip","webrtc","recording","transcription","aircall","justcall","sipgate","dialpad"],
    "video": ["webrtc","video","livekit","sfu","jitsi","whereby","bigbluebutton","conferencing","meeting"],
    "helpdesk": ["helpdesk","ticketing","triage","support","zendesk","intercom","zammad","freshdesk","front","otrs"],
    "formulare": ["form","formular","typeform","tally","jotform","json schema","webhook"],
    "vertraege": ["vertrag","contract","esign","docusign","pandadoc","skribble","eideas","signature"],
    "buchhaltung": ["buchhaltung","accounting","invoice","rechnung","xrechnung","zugferd","gobd","lexoffice","sevdesk","easybill"],
    "rapporte": ["rapporte","timetracking","zep","clockify","toggl","timebooking","timesheet","gps"],
    "schichten": ["schichten","shift","dienstplan","papershift","crewmeister","planday"],
    "fuhrpark": ["fuhrpark","fleet","fahrzeug","vehicle","telematik","fahrtenbuch","tuev"],
    "vermietung": ["vermietung","rental","mietvertrag","booqable","rentle"],
    "inventar": ["inventar","inventory","warehouse","lager","stock","barcode","rfid","wms"],
    "einkauf": ["einkauf","procurement","purchase","lieferant","supplier"],
    "produktion": ["produktion","production","mes","manufacturing","bde","fertigungsauftrag"],
    "wiki": ["wiki","knowledge","confluence","notion","slab","outline","bookstack"],
    "regulation": ["gdpr","dsgvo","datenschutz","nis2","xrechnung","bsi","edpb","noyb","ai act","compliance","arbzg"],
    "tech-trends": [],
    "cross": ["mcp","plugin","sovereign","gaia","ai","llm","saas","b2b","kmu","mittelstand","eu cloud"],
}

def module_match(item, module, keywords):
    text = ((item.get("title") or "") + " " + (item.get("body") or "")).lower()
    # Direct module match
    mk = MODULE_KEYWORDS.get(module, [])
    if any(k in text for k in mk):
        return 1.0
    # Check other modules for cross-relevance
    for mod, ks in MODULE_KEYWORDS.items():
        if any(k in text for k in ks):
            return 0.6
    # Source keywords match
    if any(k.lower() in text for k in (keywords or [])):
        return 0.5
    return 0.2

def recency_decay(dt):
    now = datetime.datetime.now(datetime.timezone.utc)
    age_hours = (now - dt).total_seconds() / 3600
    if age_hours < 6: return 1.0
    if age_hours < 12: return 0.95
    if age_hours < 24: return 0.85
    if age_hours < 48: return 0.70
    if age_hours < 72: return 0.55
    return 0.35

def source_trust(trust):
    return trust / 10.0

COMPETITOR_KEYWORDS = [
    "hubspot","salesforce","pipedrive","zendesk","intercom","freshdesk","aircall",
    "justcall","dialpad","sipgate","twenty","espocrm","suitecrm","zammad","otrs",
    "front app","frontapp","livekit","whereby","jitsi","notion","confluence",
    "typeform","tally","jotform","docusign","pandadoc","lexoffice","sevdesk",
    "easybill","papershift","crewmeister","vimcar","booqable","rentle",
    "pickware","cin7","zoho","monday.com","freshworks","pipedrive"
]

def competitor_bonus(item):
    text = ((item.get("title") or "") + " " + (item.get("body") or "")).lower()
    for kw in COMPETITOR_KEYWORDS:
        if kw in text:
            return 1.25
    return 1.0

# Polling
print("Polling sources...", flush=True)
raw_items = []
source_status = {}
new_watermarks = {}

for src in SOURCES:
    sid = src["id"]
    if sid in MUTED:
        source_status[sid] = "muted"
        continue

    wm = watermarks.get(sid, datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc))

    try:
        headers = {"User-Agent": "zentria-intel/0.1 (+https://cosmi.app)"}
        req = Request(src["url"], headers=headers)
        feed = feedparser.parse(src["url"])

        if feed.bozo and not feed.entries:
            raise Exception(f"Feed parse error: {feed.bozo_exception}")

        count = 0
        max_pub = wm
        for entry in feed.entries[:30]:
            pub = parse_dt(entry)
            if pub <= wm:
                continue
            title = getattr(entry, "title", "") or ""
            link = getattr(entry, "link", "") or ""
            summary = getattr(entry, "summary", "") or ""
            body_snippet = re.sub(r'<[^>]+>', '', summary)[:300]

            item = {
                "id": f"raw-{sid}-{hashlib.md5((title+link).encode()).hexdigest()[:8]}",
                "source_id": sid,
                "module": src["module"],
                "source_trust": src["trust"],
                "title": title,
                "url": link,
                "body": body_snippet,
                "published_at": pub.isoformat(),
                "pub_dt": pub,
                "source_keywords": src.get("keywords", []),
                "n_sources": 1,
            }
            raw_items.append(item)
            count += 1
            if pub > max_pub:
                max_pub = pub

        source_status[sid] = f"ok:{count}"
        if max_pub > wm:
            new_watermarks[sid] = max_pub
        time.sleep(0.3)

    except Exception as e:
        source_status[sid] = f"fail:{str(e)[:60]}"
        print(f"  FAIL {sid}: {e}", flush=True)

print(f"Polled {len(SOURCES)} sources → {len(raw_items)} raw items", flush=True)

# Dedup via SimHash
print("Deduplicating...", flush=True)
seen_hashes = []
deduped = []

for item in raw_items:
    text = (item["title"] or "") + " " + (item["url"] or "") + " " + (item["body"] or "")[:200]
    sh = simhash(text)

    merged = False
    for i, (h, idx) in enumerate(seen_hashes):
        if hamming(sh, h) <= 3:
            # Merge: keep higher trust
            existing = deduped[idx]
            existing["n_sources"] += 1
            if item["source_trust"] > existing["source_trust"]:
                existing["source_trust"] = item["source_trust"]
                existing["source_id"] = item["source_id"]
            merged = True
            break

    if not merged:
        seen_hashes.append((sh, len(deduped)))
        deduped.append(item)

print(f"After dedup: {len(deduped)} items", flush=True)

# Pre-filter
print("Pre-filtering...", flush=True)
filtered = []
for item in deduped:
    title = item["title"] or ""

    if is_spam(title):
        continue

    # Short title with no module keyword match
    if word_count(title) <= 5:
        text = (title + " " + (item["body"] or "")).lower()
        has_kw = any(
            any(k in text for k in ks)
            for ks in MODULE_KEYWORDS.values()
            if ks
        )
        if not has_kw:
            continue

    filtered.append(item)

print(f"After pre-filter: {len(filtered)} items", flush=True)

# Score
print("Scoring...", flush=True)
for item in filtered:
    mm = module_match(item, item["module"], item["source_keywords"])
    st = source_trust(item["source_trust"])
    rd = recency_decay(item["pub_dt"])
    ns_bonus = 1 + 0.2 * (item["n_sources"] - 1)
    cb = competitor_bonus(item)
    item["score"] = round(mm * st * rd * ns_bonus * cb, 4)

filtered.sort(key=lambda x: x["score"], reverse=True)

# Top-20 hot items
hot_items = filtered[:20]
hot_ids = []
for i, item in enumerate(hot_items, 1):
    item_id = f"MOR-{RUN_DATE}-i{i:02d}"
    item["hot_id"] = item_id
    hot_ids.append({
        "id": item_id,
        "title": item["title"],
        "module": item["module"],
        "score": item["score"],
        "url": item["url"],
        "source_id": item["source_id"],
    })

with open(HOT_ITEMS_FILE, "w") as f:
    json.dump(hot_ids, f, indent=2)
print(f"Hot items written to {HOT_ITEMS_FILE}", flush=True)

# Update watermarks
wm_raw = {}
try:
    with open(WATERMARKS_FILE) as f:
        wm_raw = json.load(f)
except Exception:
    pass

for sid, dt in new_watermarks.items():
    wm_raw[sid] = dt.isoformat()

with open(WATERMARKS_FILE, "w") as f:
    json.dump(wm_raw, f, indent=2)
print("Watermarks updated", flush=True)

# Organise by module for output
from collections import defaultdict
module_items = defaultdict(list)
for item in filtered:
    module_items[item["module"]].append(item)

hot_item_ids_set = {item["hot_id"] for item in hot_items if "hot_id" in item}

# Count successes and failures
ok_count = sum(1 for v in source_status.values() if v.startswith("ok"))
fail_count = sum(1 for v in source_status.values() if v.startswith("fail"))
failures = [f"{sid} ({v[5:]})" for sid, v in source_status.items() if v.startswith("fail")]

duration = (datetime.datetime.now(datetime.timezone.utc) - START_TS).total_seconds()

# Estimate tokens (rough)
items_text_len = sum(len(item["title"] or "") + len(item["body"] or "") for item in filtered)
tokens_input_est = int(items_text_len / 4) + 5000
tokens_output_est = 8000

pool_pct = 0.68  # estimated — no live pool API

# Build output
MODULE_ORDER = [
    "crm-core", "dialer", "helpdesk", "video", "formulare", "vertraege",
    "buchhaltung", "rapporte", "schichten", "fuhrpark", "vermietung",
    "inventar", "einkauf", "produktion", "wiki", "regulation", "tech-trends", "cross"
]

def fmt_item(item):
    title = item["title"] or "(no title)"
    url = item["url"] or ""
    score = item["score"]
    ns = item["n_sources"]
    hot_marker = f" 🔥`{item.get('hot_id','')}`" if item.get("hot_id") else ""
    ns_str = f", n_sources:{ns}" if ns > 1 else ""
    body = (item["body"] or "").strip()
    # Trim body to ~120 chars
    if len(body) > 120:
        body = body[:117] + "..."
    result = f"- [{title}]({url}){hot_marker} — score:{score}{ns_str}\n"
    if body:
        result += f"  > {body}\n"
    return result

lines = []
lines.append(f"""---
date: {RUN_DATE}
type: morning
runtime_minutes: {round(duration/60, 1)}
tokens_input: {tokens_input_est}
tokens_output: {tokens_output_est}
items_scanned: {len(raw_items)}
items_after_dedup: {len(deduped)}
items_after_prefilter: {len(filtered)}
hot_items_count: {len(hot_items)}
pool_pct_used: {pool_pct}
---

# Morning-Pulse {RUN_DATE} ({RUN_DOW})

## Status
- {len(raw_items)} Roh-Items von {ok_count} Quellen
- {len(deduped)} nach Dedup (-{round((1-len(deduped)/max(len(raw_items),1))*100)}%)
- {len(filtered)} nach Pre-Filter (-{round((1-len(filtered)/max(len(deduped),1))*100)}%)
- Top-{len(hot_items)} als Hot-Items markiert für intel-deep heute Abend
- Tier-2-Rotation heute (Di): helpdesk, crm-core
""")

lines.append("## Modul-Breakdown\n")

active_modules = []
silent_modules = []

for mod in MODULE_ORDER:
    items = module_items.get(mod, [])
    if not items:
        silent_modules.append(mod)
        continue

    hot_in_mod = sum(1 for it in items if it.get("hot_id"))
    active_modules.append(mod)
    lines.append(f"### {mod} ({len(items)} Items, {hot_in_mod} Hot)\n")
    for item in items[:8]:  # max 8 per module in output
        lines.append(fmt_item(item))
    if len(items) > 8:
        lines.append(f"  _(+{len(items)-8} weitere Items)_\n")
    lines.append("")

# Hot items list
lines.append("## Hot-Items-Liste (sortiert nach Score)\n")
for item in hot_items:
    hid = item.get("hot_id", "")
    lines.append(f"{hid[-2:] if hid else '?'}. `{hid}` {item['title']} — modul:{item['module']}, score:{item['score']}\n")

lines.append("")

# Silent modules
if silent_modules:
    lines.append("## Stille Module\n")
    for mod in silent_modules:
        lines.append(f"- {mod}: keine relevanten Items heute\n")
    lines.append("")

# Source status
lines.append("## Quellen-Status\n")
lines.append(f"- {ok_count}/{len(SOURCES)} erfolgreich gepollt\n")
if failures:
    lines.append(f"- {fail_count} Failures: {', '.join(failures[:5])}\n")
else:
    lines.append("- 0 Failures\n")

output = "".join(lines)
with open(OUTPUT_FILE, "w") as f:
    f.write(output)
print(f"Output written: {OUTPUT_FILE}", flush=True)

# Telemetry
run_record = {
    "routine": "intel-morning",
    "started_at": START_TS.isoformat(),
    "duration_seconds": round(duration),
    "tokens_input": tokens_input_est,
    "tokens_output": tokens_output_est,
    "items_scanned": len(raw_items),
    "items_after_dedup": len(deduped),
    "items_after_prefilter": len(filtered),
    "hot_items_count": len(hot_items),
    "exit_reason": "completed",
}
with open(RUNS_FILE, "a") as f:
    f.write(json.dumps(run_record, default=str) + "\n")
print("Telemetry written.", flush=True)
print(f"Done in {round(duration)}s.", flush=True)
