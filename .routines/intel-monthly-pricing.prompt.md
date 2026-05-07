# Routine: intel-monthly-pricing

Cron: `0 6 1 * *` (1. d.M. 06:00 Berlin)
Modell: claude-sonnet-4-6
Max Output: 30000 Tokens
Max Runtime: 40 min
Pool-Threshold-Abort: 0.20

## Rolle

Pricing-Page-Diff. Liest alle `pricing_url`-Felder aus `_competitors.yaml`, scraped via Headless-Chromium, vergleicht mit letzter Snapshot, schreibt Diff-Report.

## Workflow

1. Pro Konkurrent mit `pricing_url`:
   - GET via `PLAYWRIGHT_SERVICE_URL` (JS-rendered)
   - HTML→Markdown
   - Lade alten Snapshot aus `.state/pricing_snapshots/<competitor>.md` falls vorhanden
   - Diff via `difflib.unified_diff`
2. Bei Aenderung: schreibe Diff-Block + interpretiere Bedeutung (Preis-Erhoehung? Neuer Tier? Feature-Move?)
3. Aktualisiere Snapshot
4. Output: `monthly/{YYYY-MM}-pricing.md`

## Output-Schema

```markdown
---
year: 2026
month: 5
created: 2026-05-01
competitors_checked: 28
changes_detected: 6
---

# Pricing-Diff Mai 2026

## Aenderungen erkannt

### Pipedrive — Tier "Advanced" +€2/Mo
**Diff:**
```diff
- Advanced: €17.50/User/Mo
+ Advanced: €19.50/User/Mo
```
**Interpretation:** ~12% Erhoehung. Vermutlich Inflations-Adjust + AI-Forecasting-Beta-Investment.
**Cosmi-Implikation:** Cosmi-COSMI-Sales (€19/User/Mo) liegt jetzt unter Pipedrive Advanced. USP-Kommunikation pruefen.

### sevDesk — Neuer Tier "S" eingefuehrt
... (analog)

## Keine Aenderungen (28 - 6 = 22)
- HubSpot, Salesforce, Zoho, Bexio, monday, ...

## Strategische Beobachtungen

- 4 Konkurrenten haben diesen Monat AI-Features in den Tier-Stack integriert (Bundle-Preise).
- DACH-Spezialisten (sevDesk, Lexoffice, Bexio) bleiben preislich stabil.
```

## Discord-Push

Wenn `DISCORD_WEBHOOK_TRENDS`: 1 Embed pro Aenderung in `#trends` mit Button `[ 📌 Auf Friday-Watch ]`.

## Constraints

- Hard-Output-Cap 30000 Tokens.
- Bei 0 Aenderungen: Header "Stiller Pricing-Monat" plus Telemetry.
- Snapshot-Pflege in `.state/pricing_snapshots/<slug>.md` (committed, damit Diff-History nachvollziehbar).
