# Routine: intel-weekend-regulation

Cron: `0 9 * * 6` (Sa 09:00 Berlin)
Modell: claude-sonnet-4-6
Max Output: 20000 Tokens
Max Runtime: 25 min
Pool-Threshold-Abort: 0.20

## Rolle

EU-Regulation-Sweep. Liest `sources/_regulation.yaml`-Quellen (EUR-Lex, BfDI, BSI, EDPB, BMWK, BMAS, ENISA, noyb), filtert Cosmi-Relevanz (DSGVO, AI Act, NIS2, XRechnung, GoBD, eIDAS, ArbZG), schreibt `daily/{YYYY-MM-DD}-regulation.md`.

## Workflow

1. Polle alle `sources/_regulation.yaml`-Quellen (Watermark-basiert wie intel-morning).
2. Pre-Filter: Spam, Marketing-Push raus.
3. Pro Item: Cosmi-Relevanz pruefen anhand `keywords`-Liste pro Quelle.
4. Bei Relevanz: kurze Zusammenfassung + Cosmi-Implikation + Modul-Tag.
5. Output: `daily/{YYYY-MM-DD}-regulation.md`.

## Output-Schema

```markdown
---
date: 2026-05-09
type: regulation
runtime_minutes: 18
items_scanned: 87
items_relevant: 12
---

# Regulation-Sweep KW19/2026 (Sa 09. Mai)

## DSGVO / Datenschutz

### EDPB Newsroom
- [Item-Title](url) — Cosmi-Implikation: ...
- ...

## AI Act

### EUR-Lex C-XXX/2026
- ...

## NIS2

...

## XRechnung / e-Rechnung / GoBD

...

## ArbZG / Arbeitsrecht

...

## eIDAS

...

## BSI-Warnings (CVE-Filter: postgres, crm, saas)

...

## Stille Bereiche

- ...

## Cosmi-Action-Items

(Falls etwas Akut: hier auflisten)
- [ ] AI-Act-Hochrisiko-Klassifikation pruefen (Sprint 4)
```

## Discord-Push

Wenn `DISCORD_WEBHOOK_REGULATION`: poste Status-Embed in `#regulation` plus pro Action-Item ein eigenes Embed mit `[ 🟡 Followup ]`-Button.

## Constraints

- Hard-Output-Cap 20000 Tokens.
- Anti-Slop: Wenn >0 EU-Acts diese Woche, mind. 1 mit Cosmi-Implikation. Wenn 0 Acts: Header "Stille Regulations-Woche".
- Telemetry in `.state/runs.jsonl`.
