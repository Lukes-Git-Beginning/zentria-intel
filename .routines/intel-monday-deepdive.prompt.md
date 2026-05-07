# Routine: intel-monday-deepdive

Cron: `0 8 * * 1` (Mo 08:00 Berlin)
Modell: **claude-opus-4-7** (Strategie-Tiefe)
Max Output: 40000 Tokens
Max Runtime: 60 min
Pool-Threshold-Abort: 0.15

## Rolle

Modul-Rotation. Jede Woche ein anderes Cosmi-Modul (von 14) wird **strategisch tief recherchiert** — nicht nur News, sondern Marktstand, Konkurrenz-Vergleich, Cosmi-Schwachpunkte. Alle 14 Wochen rotiert das Modul durch.

## Rotations-Logik

1. Lies `~/Documents/zentria-intel/.state/deepdive_rotation.json` (Format: `{"last_module": "crm-core", "last_week": "2026-W19"}`)
2. Naechstes Modul aus `settings.yaml` `intel-monday-deepdive.rotation_modules`-Liste wraehlen
3. Update State-File am Ende des Runs

## Workflow

1. Lies `sources/<modul>.yaml` und `_competitors.yaml` (Modul-Konkurrenten).
2. Polle alle Modul-spezifischen Quellen + GitHub-Releases der letzten 8 Wochen.
3. Suche G2-/Capterra-Reviews der Top-5 Modul-Konkurrenten (via Headless-Chromium).
4. Existing Cosmi-Status pruefen: Lies `KMU-Hub/.knowledge/<modul-relevante-notes>.md` und `backend/internal/<modul>/` (Code-Stand).
5. Tiefenbericht schreiben.

## Output-Schema

Output-File: `monthly/{YYYY-MM-DD}-deepdive-{modul}.md` (in `monthly/` weil rotiert pro Modul max alle 14 Wochen, also "monatlich-ish")

```markdown
---
year: 2026
week: 20
modul: crm-core
created: 2026-05-13
runtime_minutes: 52
tokens_input: 380000
tokens_output: 35000
---

# Deepdive: crm-core (Mo W20/2026)

## State-of-the-Art

(Was machen die Top-5 Konkurrenten gerade? Bullet-Liste pro Konkurrent: Was haben sie, was Cosmi nicht hat)

## Cosmi-IST-Stand

(Aus Knowledge-Vault + Code-Lesen. Was gibts, was fehlt.)

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Pipedrive | HubSpot | monday | Bexio | weclapp |
|---|---|---|---|---|---|---|
| Pipeline-Mgmt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI-Forecasting | ❌ | ✅ Q3 | ✅ | 🚧 Beta | ❌ | ❌ |
| Lead-Scoring | 🚧 | ✅ | ✅ | ✅ | ❌ | ❌ |
| ... | ... | ... | ... | ... | ... | ... |

## Top-3 Strategische Empfehlungen

1. **AI-Forecasting Phase D vorziehen** — Markt forciert
2. ...

## Quellen

(Top-Quellen die diesen Bericht stuetzen)

## Picks (vorgeschlagen)

[ ] 🟢 AI-Forecasting Pflicht-Roadmap-Move
[ ] 🟡 Lead-Scoring-Vergleich vertiefen (-> followup 30d)
```

## Discord-Push

Wenn `DISCORD_WEBHOOK_TRENDS`: poste Deepdive-Header + Top-3-Empfehlungen-Embeds in `#trends` mit Buttons.

## Constraints

- Hard-Output-Cap 40000 Tokens.
- Pflichtsektionen: State-of-the-Art, Cosmi-IST-Stand, Vergleichstabelle (min 6 Zeilen), 3 Empfehlungen.
- Telemetry.
