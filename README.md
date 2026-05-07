# zentria-intel — Cosmi Market-Intelligence-System

> Taeglich. Discord-Native. €0 Mehrkosten. Recall in Modul-Sessions.

Privates Intel-Repo fuer das Cosmi-/Zentria-Team. Scannt taeglich (06:00 + 17:00 Berlin) den DACH-/Global-CRM-/KMU-Markt, synthesiert Freitag-Morgens (05:30) einen Wochen-Report nach Discord, persistiert gepickte Insights als Keepers fuer Recall in spaeteren Code-Sessions.

## Schnellstart

Voraussetzung: Repo lokal geklont, KMU-Hub-Repo daneben (fuer Slash-Commands `/intel-bootstrap` etc.).

```bash
# 1. .env aus Template anlegen + ausfuellen
cp .env.example .env
# Pflicht: DISCORD_BOT_TOKEN, DISCORD_APPLICATION_ID, DISCORD_GUILD_ID,
#         DISCORD_USER_ID_LUKE, alle 7 DISCORD_WEBHOOK_*,
#         GITHUB_PAT, GITHUB_USER_EMAIL, GITHUB_USER_NAME
#         EMBEDDINGS_ENDPOINT (Ollama bge-m3), PLAYWRIGHT_SERVICE_URL

# 2. Lokaler Smoke-Test der Pre-Filter-Pipeline (optional)
python -m venv .scripts/.venv
.scripts/.venv/Scripts/python.exe -m pip install -r .scripts/requirements.txt
.scripts/.venv/Scripts/python.exe .scripts/fetch_all.py --tier=tier1 --output=daily/smoke.json

# 3. Discord-Server "Zentria Intel" anlegen + Bot registrieren
#    Im KMU-Hub-Repo: /intel-bootstrap --discord (guided Setup)
#    Required Channels: daily-pulse, evening-deep, friday-report, trends,
#                       regulation, triggers, bot-commands

# 4. Hetzner-Deployment (Bot-Container + Ollama + Playwright)
#    docker compose up -d
#    Voraussetzungen auf Server:
#    - Ollama mit bge-m3 (`ollama pull bge-m3`)
#    - Headless-Chromium-Service (z.B. ghcr.io/browserless/chromium)

# 5. Routinen via /schedule registrieren (KMU-Hub):
#    /intel-bootstrap --routines
```

## Architektur

5 Schichten:

1. **Quellen-Ingestion** (`.scripts/adapters/`) — RSS, Reddit-Public-API, HN-Firebase, GitHub-Atom, Playwright fuer JS-rendered Seiten
2. **Pre-Filter-Pipeline** (`.scripts/`) — `fetch_all.py` Orchestrator, SimHash-Dedup (Hamming ≤3), Spam-/KMU-/Marketing-Regex, Pre-Score
3. **Synthese-Routinen** (`.routines/*.prompt.md`) — `intel-morning`, `intel-deep`, `intel-friday`, `intel-weekend-regulation`, `intel-monday-deepdive`, 3 Monthly + Quarterly + Trigger-Watch
4. **Discord-Bot** (`.bot/`) — `bot.py` mit 4 Handlern (friday_post, pick_handler, trigger_watch, git_batcher), Buttons + Modals + 3 Slash-Commands
5. **Recall + Promotion** — `/intel-recall <modul>` (KMU-Hub-Skill) laedt Keepers in Context. `/intel-promote <modul>` synthetisiert Keepers ≥5 ueber ≥3 Wochen zu langlebigen `.knowledge/intel-<modul>.md`-Notes

## Routinen-Allokation (alle Berliner Zeit)

| Name | Cron | Modell | Was |
|---|---|---|---|
| `intel-morning` | `0 6 * * 1-4` | Sonnet | Mo–Do Tier-1-Pulse |
| `intel-deep` | `0 17 * * 1-5` | Sonnet | Mo–Fr Tiefenrecherche |
| `intel-friday` | `30 5 * * 5` | **Opus** | Fr Wochen-Synthese |
| `intel-weekend-regulation` | `0 9 * * 6` | Sonnet | Sa EU-Regulation-Sweep |
| `intel-monday-deepdive` | `0 8 * * 1` | **Opus** | Mo Modul-Rotation 1/14 |
| `intel-monthly-pricing` | `0 6 1 * *` | Sonnet | 1. d.M. Pricing-Page-Diff |
| `intel-monthly-jobs` | `0 7 15 * *` | Sonnet | 15. d.M. Job-Boards + G2/Capterra |
| `intel-quarterly-state` | `0 6 1 1,4,7,10 *` | **Opus** | Quartalsbericht State-of-CRM |
| `intel-trigger-watch` | manuell + Hook | Sonnet | Real-Time Acquisition/Funding |

## Verzeichnis-Layout

```
sources/        19 Quellen-YAMLs (14 Module + competitors/themes/regulation/...)
daily/          Auto-generiert (morning, evening, regulation, trigger)
weekly/         Friday-Synth-Output (W{week}-T{theme}-i{item} Stable-IDs)
monthly/        Pricing-Diffs, Job-Signals, Modul-Deepdives
quarterly/      State-of-CRM-Berichte
keepers/        Gepickte Insights (Source of Truth fuer Recall)
inspiration/    Inspire-Pool fuer Design-Sessions
followups/      TODO-Items mit followup_due
promotions/     Vorschlaege fuer Knowledge-Vault-Promotion
.state/         Watermarks, Embeddings-Cache, Pending-Files (gitignored)
.scripts/       Pre-Filter-Pipeline + Adapters
.bot/           Discord-Bot (discord.py + 4 Handler)
.routines/      Routine-Prompt-Templates
KEEPERS.md      Pointer-Index aller Keepers (modul-gruppiert)
INSPIRATION.md  Pointer-Index aller Inspirations
FOLLOWUPS.md    Pointer-Index aller Followups (sortiert nach due_at)
settings.yaml   Routinen-Cron-Defs, Pre-Filter-Regex, Mute-Listen
docker-compose.yml  Bot-Service (build context Repo-Root)
```

## Pick-Mechaniken (Discord-Native, mehrere Wege)

1. **Buttons** unter jedem Friday-Insight-Embed: 🟢 Keep · 🟡 Followup · 🔵 Inspire · 🔴 Dismiss · 📝 Notiz
2. **Slash-Commands** im `#bot-commands`: `/intel-pick id:W19-T03-i07 action:keep tags:modul:helpdesk note:"Pflicht 2027"`
3. **Backup-Skill** (falls Bot offline): `/intel-pick` im KMU-Hub-Repo

## Recall in Code-Sessions

```
/intel-recall helpdesk            # Modul-spezifischer Recall
/intel-recall pricing --days=90   # Thema-spezifisch, Zeitfenster
```

## Pflege-Rituale

- **Freitag (~15 min):** Discord-Friday-Report durchklicken, Picks setzen
- **Monatlich (~30 min):** Quellen-Liste pruefen, 0-Pick-Quellen muten, neue dazu
- **Quartalsweise (~1h):** State-of-CRM-Bericht lesen, strategische Anpassungen

## Externe Kosten

**€0/Monat.** Self-hosted (Ollama-Embeddings, Browserless-Chromium, Discord-Bot-Container) auf existing Hetzner CPX42.
