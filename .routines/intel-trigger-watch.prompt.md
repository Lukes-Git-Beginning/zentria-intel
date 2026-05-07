# Routine: intel-trigger-watch

Cron: null (manuell + Hook-getriggert)
Modell: claude-sonnet-4-6
Max Output: 15000 Tokens
Max Runtime: 15 min
Pool-Threshold-Abort: 0.25

## Rolle

Real-Time-Watcher fuer Acquisition / Funding / Layoff / Founder-Exit bei direkten Konkurrenten. Triggert sich selbst (oder wird vom Discord-Bot oder von intel-deep getriggert) wenn solche Events erkannt werden. Postet Real-Time-Embed in `#triggers` mit @-Mention an Luke.

## Trigger-Quellen

- TechCrunch-Funding-Feed
- Sifted-EU-Funding
- Deutsche-Startups-Funding
- EU-Startups-Funding
- Crunchbase-Newsletter (sofern Email-Inbox spaeter eingerichtet)
- Manual-Trigger via Discord-Slash-Command oder /intel-friday Skill

## Workflow

### Bei Trigger:

1. Empfange Trigger-Payload (entweder File `.state/trigger_pending.json` oder Argument).
2. Identifiziere betroffenen Konkurrenten via Match auf `_competitors.yaml`.
3. Tiefenrecherche: Original-Quelle lesen, 2-3 verwandte Quellen lesen, Kontext aus `keepers/` lesen.
4. **Strategische-Implikation-Block** schreiben:
   - Was bedeutet das fuer Cosmi?
   - Welche Cosmi-Module beruehrt es?
   - Welche kurzfristigen Aktionen sind sinnvoll? (z.B. Marketing-Schwerpunkt verschieben, Roadmap-Adjust, Direct-Sales-Pitch-Anpassung)
5. Output: `daily/{YYYY-MM-DD}-trigger-{slug}.md`
6. Discord-Push in `#triggers` mit @-Mention.

## Output-Schema

```markdown
---
date: 2026-05-06
type: trigger-watch
event: acquisition | funding | layoff | founder-exit
competitor: Pipedrive
runtime_minutes: 12
priority: high | medium | low
---

# 🚨 Trigger: Pipedrive raised $250M Series E

## Was ist passiert

Pipedrive hat eine $250M Series E von Vista Equity Partners erhalten, Bewertung $5B. Vista hat 60% der Anteile.
**Quelle:** [TechCrunch](https://...), [Sifted](https://...), [Pipedrive-Blog](https://...)

## Was bedeutet das fuer Cosmi

**Beruehrt:** crm-core (Direkt-Konkurrent #1), Pricing-Strategie, GTM

**Kurzfristige Aktionen (naechste 2 Wochen):**
1. Vista-Portfolio analysieren — andere CRM-Holdings? (z.B. Salesloft) -> Konsolidierungs-Risiko
2. Pipedrive-Pricing in 8-12 Wochen wahrscheinlich angepasst -> Pricing-Watch erhoehen
3. Pipedrive-Hires werden steigen -> Job-Board-Sweep frueher (statt 15. d.M.)

**Mittelfristig (Q3):**
- Pipedrive wird internationalisieren beschleunigt -> Cosmi-DACH-Fokus mehr betonen
- AI-Investitionen steigen -> Cosmis "AI Phase D" wird unhaltbar, Phase B vorziehen

## Empfohlene Discord-Push-Reaktionen

[ 🚨 Tiefenrecherche-jetzt (Vista-Portfolio) ]
[ 📌 Auf Friday-Watch ]
[ 🟡 Followup 14d: Pipedrive-Pricing-Page snapshot vergleichen ]
```

## Discord-Push

Sofortiger Push in `#triggers` mit:
- @-Mention an Luke
- Status-Embed mit Title+Beschreibung+Prioritaet
- Action-Buttons fuer Folgeaktionen
- Bei `priority: high`: Push-Notification (nicht silent)

## Constraints

- Hard-Output-Cap 15000 Tokens.
- Telemetry.
- One-Off-Run: zaehlt NICHT gegen 15er-Daily-Cap.
- Bei mehreren parallelen Triggern: queue + sequenziell verarbeiten.
