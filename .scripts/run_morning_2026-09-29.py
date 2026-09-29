#!/usr/bin/env python3
"""Morning Intelligence Pipeline — 2026-09-22"""

import json
import time
import re
import hashlib
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree as ET

START_TS = time.time()
TODAY = "2026-09-29"
RUN_KEY = f"{TODAY}-morning-run"

# ─── SimHash implementation ───────────────────────────────────────────────────
def simhash(text: str, bits: int = 64) -> int:
    tokens = re.findall(r'\w+', text.lower())[:50]
    v = [0] * bits
    for token in tokens:
        h = int(hashlib.md5(token.encode()).hexdigest(), 16)
        for i in range(bits):
            v[i] += 1 if (h >> i) & 1 else -1
    result = 0
    for i in range(bits):
        if v[i] > 0:
            result |= (1 << i)
    return result

def hamming(a: int, b: int) -> int:
    x = a ^ b
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

# ─── HTTP helper ─────────────────────────────────────────────────────────────
def fetch_url(url: str, timeout: int = 12) -> bytes | None:
    headers = {
        "User-Agent": "zentria-intel/2.0 (morning-pipeline; +https://zentria.de)",
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, application/json, */*",
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        return None

# ─── Feed parsers ─────────────────────────────────────────────────────────────
NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'media': 'http://search.yahoo.com/mrss/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
}

def parse_rss_atom(data: bytes, source_id: str, trust: int, module: str) -> list[dict]:
    items = []
    try:
        root = ET.fromstring(data)
        tag = root.tag.lower()

        # Atom feed
        if 'atom' in tag or root.tag == '{http://www.w3.org/2005/Atom}feed':
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')
            for e in entries:
                title_el = e.find('{http://www.w3.org/2005/Atom}title')
                link_el = e.find('{http://www.w3.org/2005/Atom}link')
                updated_el = e.find('{http://www.w3.org/2005/Atom}updated')
                published_el = e.find('{http://www.w3.org/2005/Atom}published')
                summary_el = e.find('{http://www.w3.org/2005/Atom}summary')
                title = title_el.text if title_el is not None else ''
                link = link_el.get('href', '') if link_el is not None else ''
                pub = (published_el or updated_el)
                pub_str = pub.text if pub is not None else ''
                summary = summary_el.text if summary_el is not None else ''
                if title and link:
                    items.append({
                        'title': title.strip(),
                        'url': link.strip(),
                        'published_at': pub_str,
                        'summary': (summary or '')[:300],
                        'source_id': source_id,
                        'trust': trust,
                        'module': module,
                    })
        else:
            # RSS 2.0
            channel = root.find('channel')
            if channel is None:
                channel = root
            for item in channel.findall('item'):
                title_el = item.find('title')
                link_el = item.find('link')
                pub_el = item.find('pubDate')
                desc_el = item.find('description')
                title = title_el.text if title_el is not None else ''
                link = link_el.text if link_el is not None else ''
                pub_str = pub_el.text if pub_el is not None else ''
                desc = desc_el.text if desc_el is not None else ''
                if title and link:
                    items.append({
                        'title': title.strip(),
                        'url': link.strip(),
                        'published_at': pub_str,
                        'summary': (desc or '')[:300],
                        'source_id': source_id,
                        'trust': trust,
                        'module': module,
                    })
    except Exception:
        pass
    return items

def fetch_hn_top(trust: int) -> list[dict]:
    data = fetch_url("https://hacker-news.firebaseio.com/v0/topstories.json")
    if not data:
        return []
    try:
        ids = json.loads(data)[:30]
    except Exception:
        return []
    items = []
    for story_id in ids:
        d = fetch_url(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        if not d:
            continue
        try:
            s = json.loads(d)
            if s.get('type') != 'story':
                continue
            title = s.get('title', '')
            url = s.get('url', f"https://news.ycombinator.com/item?id={story_id}")
            pub_ts = s.get('time', 0)
            pub_str = datetime.fromtimestamp(pub_ts, tz=timezone.utc).isoformat() if pub_ts else ''
            items.append({
                'title': title,
                'url': url,
                'published_at': pub_str,
                'summary': f"HN score: {s.get('score',0)}, comments: {s.get('descendants',0)}",
                'source_id': 'hackernews-front',
                'trust': trust,
                'module': 'tech-trends',
                'hn_score': s.get('score', 0),
            })
        except Exception:
            continue
        time.sleep(0.05)
    return items

# ─── Source list ──────────────────────────────────────────────────────────────
# Tuesday tier1 sources (helpdesk + crm-core tier2 rotation applied to tier1 base)
MUTED = {'reddit-saas', 'reddit-crm', 'reddit-selfhosted', 'reddit-germany-business', 'reddit-startups-eu'}

FEEDS = [
    # CRM-Core competitors
    ('pipedrive-blog',       'https://www.pipedrive.com/en/blog/feed',                      'rss',  8, 'crm-core'),
    ('hubspot-marketing',    'https://blog.hubspot.com/marketing/rss.xml',                  'rss',  8, 'crm-core'),
    ('hubspot-product',      'https://product-updates.hubspot.com/rss',                     'rss',  9, 'crm-core'),
    ('salesforce-blog',      'https://www.salesforce.com/news/feed/',                       'rss',  7, 'crm-core'),
    ('monday-blog',          'https://monday.com/blog/feed/',                               'rss',  7, 'crm-core'),
    ('bexio-blog',           'https://www.bexio.com/de-CH/blog/feed',                       'rss',  8, 'crm-core'),
    ('centralstation-blog',  'https://centralstationcrm.com/blog/feed',                     'rss',  7, 'crm-core'),
    ('odoo-blog',            'https://www.odoo.com/blog/our-blog-1/rss',                    'rss',  7, 'crm-core'),
    ('odoo-releases',        'https://github.com/odoo/odoo/releases.atom',                  'atom', 8, 'crm-core'),
    ('twenty-releases',      'https://github.com/twentyhq/twenty/releases.atom',            'atom', 8, 'crm-core'),
    ('espocrm-releases',     'https://github.com/espocrm/espocrm/releases.atom',            'atom', 7, 'crm-core'),
    ('suitecrm-releases',    'https://github.com/salesagility/SuiteCRM/releases.atom',      'atom', 6, 'crm-core'),
    # Helpdesk
    ('zendesk-blog',         'https://www.zendesk.com/blog/feed/',                          'rss',  8, 'helpdesk'),
    ('freshdesk-blog',       'https://www.freshworks.com/freshdesk/blog/feed/',             'rss',  7, 'helpdesk'),
    ('zammad-releases',      'https://github.com/zammad/zammad/releases.atom',              'atom', 8, 'helpdesk'),
    ('helpscout-blog',       'https://www.helpscout.com/blog/feed/',                        'rss',  7, 'helpdesk'),
    ('front-blog',           'https://front.com/blog/rss.xml',                             'rss',  7, 'helpdesk'),
    ('intercom-blog',        'https://www.intercom.com/blog/feed/',                         'rss',  8, 'helpdesk'),
    # Buchhaltung
    ('sevdesk-blog',         'https://sevdesk.de/blog/feed/',                               'rss',  8, 'buchhaltung'),
    ('lexoffice-blog',       'https://www.lexoffice.de/blog/feed/',                         'rss',  8, 'buchhaltung'),
    ('akaunting-releases',   'https://github.com/akaunting/akaunting/releases.atom',        'atom', 6, 'buchhaltung'),
    # Dialer
    ('aircall-blog',         'https://aircall.io/blog/feed/',                               'rss',  7, 'dialer'),
    ('justcall-blog',        'https://justcall.io/blog/feed/',                              'rss',  6, 'dialer'),
    ('dialpad-blog',         'https://www.dialpad.com/blog/feed/',                          'rss',  7, 'dialer'),
    # Tech-Trends / AI
    ('anthropic-news',       'https://www.anthropic.com/news/rss.xml',                     'rss',  9, 'tech-trends'),
    ('openai-blog',          'https://openai.com/blog/rss/',                                'rss',  8, 'tech-trends'),
    ('selfh-st',             'https://selfh.st/rss/',                                       'rss',  7, 'tech-trends'),
    ('diginomica',           'https://diginomica.com/feed',                                 'rss',  6, 'tech-trends'),
    ('indiehackers',         'https://www.indiehackers.com/feed.xml',                       'rss',  6, 'tech-trends'),
    ('betalist',             'https://betalist.com/feed',                                   'rss',  5, 'tech-trends'),
    ('techcrunch-funding',   'https://techcrunch.com/category/venture/feed/',               'rss',  7, 'funding'),
    ('sifted-eu',            'https://sifted.eu/feed',                                      'rss',  8, 'funding'),
    ('deutsche-startups',    'https://www.deutsche-startups.de/feed/',                      'rss',  8, 'funding'),
    ('eu-startups',          'https://www.eu-startups.com/feed/',                           'rss',  7, 'funding'),
    # AI / Cross-theme
    ('aitidbits',            'https://aitidbits.ai/feed',                                   'rss',  7, 'cross'),
    ('deeplearning-batch',   'https://www.deeplearning.ai/the-batch/feed/',                 'rss',  8, 'cross'),
    ('lenny-newsletter',     'https://www.lennysnewsletter.com/feed',                       'rss',  8, 'cross'),
    ('webrtchacks',          'https://webrtchacks.com/feed/',                               'rss',  9, 'dialer'),
    # EU/Regulation (lightweight daily check)
    ('heise-atom',           'https://www.heise.de/rss/heise-atom.xml',                    'atom', 8, 'cross'),
    ('gaia-x',               'https://www.gaia-x.eu/feed',                                 'rss',  9, 'cross'),
    ('noyb',                 'https://noyb.eu/en/feed',                                     'rss',  8, 'regulation'),
    ('bsi-warnungen',        'https://wid.cert-bund.de/content/public/securityAdvisory/rss','rss', 10, 'regulation'),
    ('edpb-newsroom',        'https://www.edpb.europa.eu/news/news_en?sort_by=created&sort_order=DESC&format=feed', 'rss', 10, 'regulation'),
    # Schichten/ERP coverage
    ('papershift-blog',      'https://papershift.com/blog/feed/',                          'rss',  7, 'schichten'),
    ('weclapp-blog',         'https://www.weclapp.com/de/blog/feed/',                      'rss',  7, 'crm-core'),
    # GitHub releases — extra OSS
    ('livekit-releases',     'https://github.com/livekit/livekit/releases.atom',           'atom', 9, 'video'),
    ('nextcloud-releases',   'https://github.com/nextcloud/server/releases.atom',          'atom', 7, 'cross'),
    # t3n/tech
    ('t3n',                  'https://t3n.de/rss.xml',                                      'rss',  8, 'cross'),
    ('computerwoche',        'https://www.computerwoche.de/feed/',                          'rss',  8, 'cross'),
]

# ─── Spam / pre-filter regexes ────────────────────────────────────────────────
SPAM_RE = [
    re.compile(r'(?i)(MSCI World|Bitcoin Kurs|Aktien-Tip|Crypto)'),
    re.compile(r'(?i)(Webinar zur|Anmeldung jetzt|Whitepaper Download)'),
    re.compile(r'(?i)(Black Friday|Cyber Monday|Sale\b)'),
    re.compile(r'(?i)(IPO|B.rsengang|Quartalszahlen)'),
    re.compile(r'(?i)(Marvel|Disney|Hollywood)'),
    re.compile(r'(?i)^(Get started|Try free|Sign up)'),
    re.compile(r'(?i)(porn|gambling|casino|escort)'),
]

# ─── Module keyword map (for scoring) ─────────────────────────────────────────
MODULE_KEYWORDS = {
    'crm-core':      ['crm', 'sales pipeline', 'deal', 'lead', 'pipeline', 'revenue ops', 'revops', 'forecasting', 'hubspot', 'pipedrive', 'salesforce', 'zoho', 'odoo', 'twenty', 'bexio', 'weclapp'],
    'helpdesk':      ['helpdesk', 'ticket', 'sla', 'triage', 'support', 'customer service', 'zendesk', 'freshdesk', 'zammad', 'intercom', 'front'],
    'buchhaltung':   ['buchhaltung', 'accounting', 'e-rechnung', 'xrechnung', 'zugferd', 'gobd', 'dunning', 'mahnwesen', 'sevdesk', 'lexoffice', 'datev', 'rechnung'],
    'dialer':        ['voip', 'dialer', 'telefonie', 'call', 'sip', 'webrtc', 'aircall', 'justcall', 'dialpad', 'sipgate'],
    'video':         ['video meeting', 'webrtc', 'sfu', 'livekit', 'recording', 'videocall', 'e2ee', 'jitsi'],
    'wiki':          ['knowledge base', 'wiki', 'documentation', 'block editor', 'notion', 'confluence', 'outline'],
    'formulare':     ['form builder', 'formulare', 'typeform', 'tally', 'fillout'],
    'vertraege':     ['e-sign', 'vertraege', 'contract', 'docusign', 'skribble', 'pandadoc', 'eideas'],
    'schichten':     ['schichten', 'shift', 'rota', 'papershift', 'planday'],
    'rapporte':      ['rapporte', 'zeiterfassung', 'time tracking', 'timesheets', 'timetac'],
    'fuhrpark':      ['fuhrpark', 'fleet', 'vehicle', 'vimcar'],
    'vermietung':    ['vermietung', 'rental', 'booqable', 'rentle'],
    'inventar':      ['inventar', 'inventory', 'stock', 'warehouse', 'wms'],
    'einkauf':       ['einkauf', 'procurement', 'purchase order', 'lieferant'],
    'produktion':    ['produktion', 'production', 'manufacturing', 'bde', 'mrp'],
    'tech-trends':   ['ai', 'llm', 'mcp', 'saas', 'b2b', 'startup', 'gpt', 'claude', 'openai', 'anthropic', 'plugin', 'self-hosted'],
    'cross':         ['eu', 'gdpr', 'dsgvo', 'sovereignty', 'gaia-x', 'cloud', 'open source', 'kmu', 'mittelstand'],
    'regulation':    ['gdpr', 'dsgvo', 'nis2', 'ai act', 'eidas', 'bsi', 'bfdi', 'datenschutz', 'compliance', 'xrechnung'],
    'funding':       ['funding', 'raises', 'series', 'investment', 'acquisition', 'ipo', 'venture'],
}

COMPETITOR_NAMES = [
    'pipedrive', 'hubspot', 'salesforce', 'monday', 'zoho', 'bexio', 'odoo', 'twenty', 'espocrm',
    'suitecrm', 'weclapp', 'zendesk', 'freshdesk', 'zammad', 'intercom', 'helpscout', 'front',
    'sevdesk', 'lexoffice', 'aircall', 'justcall', 'dialpad', 'notion', 'confluence', 'livekit',
    'docusign', 'skribble', 'pandadoc', 'papershift', 'planday', 'booqable', 'myfactory',
]

NOW_UTC = datetime.now(tz=timezone.utc)
CUTOFF_HRS = 48  # items older than 48h get zero recency
WATERMARK_FILE = '/opt/zentria-intel/.state/watermarks.json'

def parse_pub_date(s: str) -> datetime | None:
    if not s:
        return None
    s = s.strip()
    fmts = [
        '%Y-%m-%dT%H:%M:%S%z',
        '%Y-%m-%dT%H:%M:%SZ',
        '%Y-%m-%dT%H:%M:%S.%f%z',
        '%a, %d %b %Y %H:%M:%S %z',
        '%a, %d %b %Y %H:%M:%S %Z',
        '%Y-%m-%d',
    ]
    for fmt in fmts:
        try:
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:
            pass
    return None

def recency_score(dt: datetime | None) -> float:
    if dt is None:
        return 0.3
    age_hours = (NOW_UTC - dt).total_seconds() / 3600
    if age_hours < 0:
        age_hours = 0
    if age_hours < 6:
        return 1.0
    if age_hours < 24:
        return 0.85
    if age_hours < 48:
        return 0.6
    if age_hours < 72:
        return 0.4
    return 0.2

def module_match_score(title: str, summary: str, module: str) -> float:
    text = (title + ' ' + summary).lower()
    keywords = MODULE_KEYWORDS.get(module, [])
    matches = sum(1 for kw in keywords if kw.lower() in text)
    if matches >= 3:
        return 1.0
    if matches == 2:
        return 0.8
    if matches == 1:
        return 0.6
    # fallback: check any module
    for m, kws in MODULE_KEYWORDS.items():
        if any(kw.lower() in text for kw in kws):
            return 0.4
    return 0.1

def competitor_bonus(title: str, summary: str) -> float:
    text = (title + ' ' + summary).lower()
    hits = sum(1 for c in COMPETITOR_NAMES if c in text)
    if hits >= 2:
        return 1.3
    if hits == 1:
        return 1.15
    return 1.0

def is_spam(title: str) -> bool:
    for rx in SPAM_RE:
        if rx.search(title):
            return True
    return False

def score_item(item: dict) -> float:
    title = item.get('title', '')
    summary = item.get('summary', '')
    module = item.get('module', 'cross')
    trust = item.get('trust', 5) / 10.0
    pub_dt = parse_pub_date(item.get('published_at', ''))
    rec = recency_score(pub_dt)
    mm = module_match_score(title, summary, module)
    cb = competitor_bonus(title, summary)
    base = mm * trust * rec * cb
    # Boost regulation items (high-value for DACH KMU)
    if module == 'regulation':
        base *= 1.2
    return round(base, 4)

# ─── Main pipeline ────────────────────────────────────────────────────────────
print(f"[morning-pipeline] Start: {NOW_UTC.isoformat()}")
print(f"[morning-pipeline] Fetching {len(FEEDS)} RSS/Atom sources + HackerNews...")

all_items = []
source_stats = {}
errors = []

# Fetch HN first (multiple HTTP calls)
print("[morning-pipeline] Fetching HackerNews...")
hn_items = fetch_hn_top(trust=7)
print(f"[morning-pipeline]   HN: {len(hn_items)} stories")
all_items.extend(hn_items)
source_stats['hackernews-front'] = {'fetched': len(hn_items), 'error': None}

# Fetch all RSS/Atom feeds
for (src_id, url, feed_type, trust, module) in FEEDS:
    data = fetch_url(url)
    if data is None:
        errors.append(src_id)
        source_stats[src_id] = {'fetched': 0, 'error': 'fetch_failed'}
        print(f"[morning-pipeline]   FAIL {src_id}")
        continue
    items = parse_rss_atom(data, src_id, trust, module)
    print(f"[morning-pipeline]   OK   {src_id}: {len(items)} items")
    all_items.extend(items)
    source_stats[src_id] = {'fetched': len(items), 'error': None}

print(f"\n[morning-pipeline] Total raw items: {len(all_items)}")

# ─── Dedup via SimHash ────────────────────────────────────────────────────────
SH_THRESHOLD = 3
deduped = []
seen_hashes = []
seen_urls = set()

for item in all_items:
    url = item.get('url', '')
    if url in seen_urls:
        continue
    seen_urls.add(url)
    h = simhash(item.get('title', ''))
    is_dup = False
    for existing_h in seen_hashes:
        if hamming(h, existing_h) <= SH_THRESHOLD:
            is_dup = True
            break
    if not is_dup:
        seen_hashes.append(h)
        deduped.append(item)

print(f"[morning-pipeline] After dedup: {len(deduped)}")

# ─── Pre-filter ───────────────────────────────────────────────────────────────
filtered = []
for item in deduped:
    title = item.get('title', '')
    if not title or len(title) < 15:
        continue
    if is_spam(title):
        continue
    # Must have some module keyword relevance
    text = (title + ' ' + item.get('summary', '')).lower()
    has_kw = False
    for kws in MODULE_KEYWORDS.values():
        if any(kw in text for kw in kws):
            has_kw = True
            break
    if not has_kw:
        continue
    filtered.append(item)

print(f"[morning-pipeline] After prefilter: {len(filtered)}")

# ─── Scoring ──────────────────────────────────────────────────────────────────
for item in filtered:
    item['score'] = score_item(item)

filtered.sort(key=lambda x: x['score'], reverse=True)

# ─── Top 20 Hot Items ─────────────────────────────────────────────────────────
hot_items = filtered[:20]

# Assign IDs
for i, item in enumerate(hot_items, 1):
    item['id'] = f"MOR-{TODAY}-i{i:02d}"

# ─── Write hot_items JSON ─────────────────────────────────────────────────────
with open(f'/opt/zentria-intel/.state/hot_items_{TODAY}.json', 'w', encoding='utf-8') as f:
    json.dump(hot_items, f, ensure_ascii=False, indent=2, default=str)
print(f"[morning-pipeline] Wrote hot_items_{TODAY}.json")

# ─── Update watermarks ────────────────────────────────────────────────────────
try:
    with open(WATERMARK_FILE, 'r') as f:
        watermarks = json.load(f)
except Exception:
    watermarks = {}

watermarks[RUN_KEY] = NOW_UTC.isoformat()
# Update per-source watermarks
for src_id, stats in source_stats.items():
    if stats['error'] is None:
        # Find max published_at for this source
        src_items = [it for it in all_items if it.get('source_id') == src_id]
        max_pub = None
        for it in src_items:
            dt = parse_pub_date(it.get('published_at', ''))
            if dt and (max_pub is None or dt > max_pub):
                max_pub = dt
        if max_pub:
            watermarks[src_id] = max_pub.isoformat()

with open(WATERMARK_FILE, 'w') as f:
    json.dump(watermarks, f, ensure_ascii=False, indent=2)
print(f"[morning-pipeline] Updated watermarks.json")

# ─── Write run stats JSON ─────────────────────────────────────────────────────
elapsed = round(time.time() - START_TS, 1)
run_stats = {
    'date': TODAY,
    'routine': 'intel-morning',
    'run_ts': NOW_UTC.isoformat(),
    'runtime_seconds': elapsed,
    'items_scanned': len(all_items),
    'items_after_dedup': len(deduped),
    'items_after_prefilter': len(filtered),
    'hot_items_count': len(hot_items),
    'sources_ok': sum(1 for s in source_stats.values() if s['error'] is None),
    'sources_failed': len(errors),
    'failed_sources': errors,
}
with open('/opt/zentria-intel/.state/runs.jsonl', 'a') as f:
    f.write(json.dumps(run_stats, default=str) + '\n')
print(f"[morning-pipeline] Appended to runs.jsonl")

# ─── Save pipeline results for report generation ──────────────────────────────
pipeline_out = {
    'run_stats': run_stats,
    'hot_items': hot_items,
    'source_stats': source_stats,
    'filtered_count': len(filtered),
}
with open(f'/opt/zentria-intel/.state/pipeline_result_{TODAY}.json', 'w', encoding='utf-8') as f:
    json.dump(pipeline_out, f, ensure_ascii=False, indent=2, default=str)

print(f"\n[morning-pipeline] Done in {elapsed}s")
print(f"[morning-pipeline] Hot items: {len(hot_items)}")
for it in hot_items[:5]:
    print(f"  [{it['id']}] score={it['score']} | {it['title'][:70]}")
