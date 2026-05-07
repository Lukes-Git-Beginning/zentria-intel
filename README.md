# zentria-intel — Cosmi Market-Intelligence-System

> Taeglich. Discord-Native. €0 Mehrkosten. Recall in Modul-Sessions.

Privates Intel-Repo fuer das Cosmi-/Zentria-Team. Scannt taeglich (06:00 + 17:00 Berlin) den DACH-/Global-CRM-/KMU-Markt, synthesiert Freitag-Morgens (05:30) einen Wochen-Report nach Discord, persistiert gepickte Insights als Keepers fuer Recall in spaeteren Code-Sessions.

## Schnellstart

```bash
# 1. Repo lokal klonen (bereits geschehen, falls du dies liest)
git clone git@github.com:Lukes-Git-Beginning/zentria-intel.git ~/Documents/zentria-intel

# 2. Bootstrap im KMU-Hub-Repo
cd ~/Documents/KMU\ Hub
# In Claude Code:
/intel-bootstrap

# 3. Discord-Server "Zentria Intel" anlegen + Bot registrieren (User-Aktion):
# - https://discord.com/developers/applications -> New Application -> Bot -> Reset Token
# - Bot zum Server einladen mit Scope: bot, applications.commands
# - Webhook pro Channel anlegen, URLs in .env eintragen

# 4. Hetzner-Setup (User-Aktion auf Server):
# - .bot/ Container deployen
# - .scripts/headless-chromium/ Container deployen
# - bge-m3 Embedding-Service via Ollama starten

# 5. Routinen via /schedule registrieren (alle Berliner Zeit)
```

## Architektur

5 Schichten + 2 Stufe-5-Layer (siehe `~/.claude/plans/rein-theorpraktisch-wie-gro-luminous-cascade.md`):

1. **Quellen-Ingestion** — RSS, JSON, Reddit-Public-API, HN, ProductHunt, GitHub-Atom, Web-Scrape
2. **Daily-Scans** — `intel-morning` (Mo–Do 06:00) + `intel-deep` (Mo–Fr 17:00)
3. **Weekly-Synthese** — `intel-friday` (Fr 05:30, Opus)
4. **Pick-and-Save** — Discord-Bot mit Buttons/Modals/Reactions/Slash-Commands
5. **Recall** — `Skill(intel-recall, "<modul>")` plus PostToolUse-Auto-Hook auf Modul-Pfade
6. **Trend-Detection (S5)** — bge-m3 Embeddings, k-Means-Cluster, Anomalie-Detection
7. **Trigger-Watch (S5)** — Real-Time Acquisition/Funding/Layoff-Push in `#triggers`

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
sources/        Quellen-Konfiguration (1 YAML pro Modul/Thema)
daily/          Auto-generiert (morning, evening, regulation)
weekly/         Friday-Synth-Output
monthly/        Pricing-Diffs, Job-Signals
quarterly/      State-of-CRM-Berichte
keepers/        Lukes gepickte Insights (Source of Truth fuer Recall)
inspiration/    Inspire-Pool fuer Design-Sessions
followups/      TODO-Items mit due_at
promotions/     Vorschlaege fuer Knowledge-Vault-Promotion
.state/         Watermarks, Embeddings-Cache, Telemetry
.scripts/       Pre-Filter, Adapters, SimHash-Dedup
.bot/           Discord-Bot (discord.py, Docker)
.routines/      Routine-Prompt-Templates
KEEPERS.md      Pointer-Index aller Keepers
INSPIRATION.md  Pointer-Index aller Inspirations
FOLLOWUPS.md    Pointer-Index aller Followups (sortiert nach due_at)
settings.yaml   Routinen-Cron-Defs, Hard-Caps, Mute-Listen
```

## Pick-Mechaniken (Discord-Native, mehrere Wege)

1. **Buttons** unter jedem Friday-Insight-Embed: 🟢 Keep · 🟡 Followup · 🔵 Inspire · 🔴 Dismiss · 📝 Notiz
2. **Reactions** auf Embeds (ohne Notiz, schneller): 🟢🟡🔵🔴
3. **Slash-Commands** im `#bot-commands`: `/intel-pick id:W19-T03-i07 action:keep tags:modul:helpdesk note:"Pflicht 2027"`
4. **Backup-Repo-Skill** (falls Bot offline): `/intel-pick` im KMU-Hub-Repo

## Recall in Code-Sessions

```bash
# On-demand
/intel-recall helpdesk

# Auto-Hook (aktiv ab Tag 1):
# Read auf backend/internal/helpdesk/* triggert lautlos Top-3 Keepers in Context
```

## Pflege-Rituale

- **Freitag-Morgen (~15 min):** Discord-Friday-Report durchklicken, Picks setzen
- **Monatlich (~30 min):** Quellen-Liste pruefen, 0-Pick-Quellen muten, neue dazu
- **Quartalsweise (~1h):** State-of-CRM-Bericht lesen, strategische Anpassungen

## Externe Kosten

**€0/Monat.** Self-hosted auf existing Hetzner-CPX42 (Headless-Chromium, bge-m3, Discord-Bot-Container).

## Verwandte Pfade

- Plan: `~/.claude/plans/rein-theorpraktisch-wie-gro-luminous-cascade.md`
- Cosmi-Modul-Matrix: `~/Documents/KMU Hub/docs/MODULES_SCOPE_MATRIX.md`
- Cosmi-Strategie: `~/Documents/KMU Hub/docs/STRATEGY.md`
- Knowledge-Vault: `~/Documents/KMU Hub/.knowledge/`
