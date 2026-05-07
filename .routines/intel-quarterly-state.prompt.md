# Routine: intel-quarterly-state

Cron: `0 6 1 1,4,7,10 *` (Q1/Q2/Q3/Q4 1. d.M. 06:00 Berlin)
Modell: **claude-opus-4-7** (groesstes Synthese-Werk)
Max Output: 80000 Tokens
Max Runtime: 120 min
Pool-Threshold-Abort: 0.10

## Rolle

Quartals-State-of-CRM-Marktbericht. Synthese aus 12-13 Wochen-Reports plus 3 Monthly-Pricing + 3 Monthly-Jobs + ggf. 1-2 Monday-Deepdives. Strategischer Marktradar fuer Cosmi-Quartals-Planung.

## Workflow

1. Lade alle Wochen-Reports der letzten 13 Wochen aus `weekly/`
2. Lade Monthly-Reports der letzten 3 Monate aus `monthly/`
3. Lade Keepers + Picks-Quoten der letzten 13 Wochen
4. Embedding-Cluster auf Quarter-Window (Hierarchical, k=20-30)
5. Cluster-Trend-Trajektorien (steigend/fallend/konstant)
6. Strategischer Bericht

## Output-Schema

Output-File: `quarterly/{YYYY}-Q{quarter}.md`

```markdown
---
year: 2026
quarter: 2
created: 2026-07-01
runtime_minutes: 105
tokens_input: 2400000
tokens_output: 75000
weekly_reports_used: 13
monthly_reports_used: 3
clusters: 24
---

# State-of-CRM Q2/2026 (April-Juni)

## Executive-Summary (3 Saetze)

Q2 war das Quartal in dem AI-First-CRM zur Tabellenstake wurde. DACH-spezifische Konkurrenten (Bexio, sevDesk, Lexoffice) reagierten verhalten, internationale Player (Pipedrive, HubSpot) sprintten voraus. Cosmi-Launch 01.07.26 hat damit ein nicht-stabiles Markt-Umfeld direkt am Start.

## Top-10 Quartals-Trends (gerankt nach Cluster-Gewicht)

### #1 AI-First-CRM-Welle (k_items=87, Wochen-Aktivitaet 12/13)
**Trajektorie:** steigend
**Zusammenfassung:** ...
**Cosmi-Implikation:** ...
**Empfohlene Q3-Action:** ...
[ 🟢 Strategy-Move einleiten ]

### #2 XRechnung-Compliance-Push (k_items=42, Wochen-Aktivitaet 9/13)
... (Top-10)

## Konkurrenz-Movements im Quartal

### Pipedrive — Aktivitaets-Score 9/10 (sehr aktiv)
- 4 Major-Releases
- AI-Forecasting GA
- 23 neue Eng-Hires DACH (Hiring-Beschleunigung)
- Pricing +12% bei Top-Tier
**Threat-Level:** HOCH (von MEDIUM Q1)

### HubSpot — Aktivitaets-Score 8/10
... (alle Top-10 Konkurrenten)

## Cosmi-Position-Update

(Wo sind wir im Vergleich zum Markt-Stand?)

| Modul | Cosmi-Q2-Stand | Markt-Stand | Gap |
|---|---|---|---|
| crm-core | Pipeline + Forecasting Phase D | AI-Forecasting Tabellenstake | KRITISCH |
| helpdesk | Auto-Triage geplant Sprint 4 | Markt hat Auto-Triage | OK (rechtzeitig) |
| video | Recording-Consent live | Markt-Standard | GUT |
| ... | | | |

## Q3-Strategische-Vorschlaege

(Konkret, mit Sprint-Pfad-Vorschlag)

1. **AI-Forecasting Phase B vorziehen** — Sprint 4-5
   - Begruendung: Markt-Druck ueber 12 Wochen konstant
   - Aufwand: ~3 Sprints mit Anthropic-API-RAG-Loesung
   - Empfehlung: Build-vs-Buy: Buy (Anthropic + RAG, kein eigenes Modell)
2. ...

## "Blinde Flecken" — Was haben wir Q2 verpasst?

(Selbst-Kritik. Wo waren wir nicht aufmerksam?)

## Pflege-Vorschlaege Q3

- Quellen mit 0 Picks Q2 (auto-detect): muten oder ersetzen
- Neue Quellen-Kategorien zu eroeffnen: ...
- Modul-YAML-Updates: ...
```

## Discord-Push

Wenn `DISCORD_WEBHOOK_TRENDS`: post Quartals-Header in `#trends` mit @-Mention an Luke. Dann pro Top-3-Trend ein Embed.

## Constraints

- Hard-Output-Cap 80000 Tokens.
- Pflichtsektionen: Executive-Summary (3 Saetze), Top-10 Trends, Konkurrenz-Movements (Top-10 Konkurrenten), Cosmi-Position-Update, Q+1-Strategische-Vorschlaege (min 3), Blinde Flecken (min 2).
- Token-Budget: dies ist die teuerste Routine — Pool-Threshold 10%, also sehr defensiv. Bei Abort: schreibe Executive-Summary + Top-3 Trends + Cosmi-Position + DEFERRED-Marker.
