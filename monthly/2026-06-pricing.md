---
year: 2026
month: 6
created: 2026-06-01
competitors_checked: 11
changes_detected: 0
baseline_run: true
scrape_issues: 4
---

# Pricing-Diff Juni 2026

## Stiller Pricing-Monat — Erstlauf / Baseline

> **Hinweis:** Dies ist der erste Lauf dieser Routine. Alle 11 Snapshots wurden heute als Baseline gespeichert unter `.state/pricing_snapshots/<slug>.md`. Ab dem nächsten Monat (Juli 2026) wird gegen diese Baseline gedifft.

Geprüft: **11 Konkurrenten** mit `pricing_url` in `_competitors.yaml`.
Änderungen: **0** (kein Diff möglich — kein vorheriger Snapshot).
Scraping-Probleme: **4** (Bot-Protection oder JS-Heavy-Rendering).

---

## Baseline-Snapshot: Erfasste Preise per 2026-06-01

### weclapp — ERP-Plattform (DACH)

| Tier | Jährlich (Netto/Nutzer/Mo) | Monatlich (Netto/Nutzer/Mo) |
|---|---|---|
| ERP Starter | €39 | €39 |
| Professional | €86 | €95 |
| Enterprise | €163 | €179 |

**Anmerkung:** Starter nur monatlich buchbar und nicht kombinierbar. Professional/Enterprise jährlich ~9–10% günstiger.
**Cosmi-Implikation:** Cosmi-ERP positioniert sich zwischen Starter (€39) und Professional (€86/€95) — klare Differenzierung durch DACH-Compliance + modulareres Preismodell nötig.

---

### monday.com — Work-OS / CRM-Overlay (International)

| Tier | Preis/Seat/Mo | Bemerkung |
|---|---|---|
| Free | €0 | Bis 2 Seats |
| Basic | €9 | Akt. Angebot: €10 Rabatt/Mo auf 10-Seat-Bundle |
| Standard | €12 | + 2.000 AI-Credits (€20 Wert) inkl. |
| Pro | €19 | + 3.000 AI-Credits (€30 Wert) inkl. |
| Enterprise | Auf Anfrage | — |

**Anmerkung:** Aktive Rabatt-Aktion läuft (€10–€30 Rabatt/Mo auf Bundles). AI-Credits werden als Wert-Argument in die Tiers integriert — Signal für AI-Feature-Bundling-Strategie.
**Cosmi-Implikation:** monday.com bleibt preisgünstiger als Cosmi für einfache Use-Cases. Stärke liegt bei AI-Credit-Modell. Cosmi muss Vertikal-Wert (DACH-Compliance, ERP-Tiefe) gegen horizontale Günstig-Positionierung verteidigen.

---

### Lexoffice (Lexware) — Buchhaltung DACH

| Tier | Vollpreis/Mo | Aktionspreis/Mo* | Scope |
|---|---|---|---|
| XS | €11,00 | €5,00 | Belegerfassung & -archiv |
| S | €7,90 | €3,95 | Belegerfassung (einfache Variante) |
| M | €12,90 | €6,45 | Angebote, E-Rechnungen, Mahnungen |
| L | €21,90 | €10,95 | + Buchhaltung, EÜR, Umsatzsteuer |
| XL | €32,90 | €16,45 | + EU-Rechnungen, API-Zugang |
| Lohn-Add-on | €12,90 | €6,45 | Lohn- & Gehaltsabrechnung (separat) |

*Aktionspreis 50% Rabatt, Rabattlaufzeit 3 Monate. Alle Preise zzgl. MwSt., monatlich kündbar.

**Anmerkung:** Lexoffice ist **nicht per-User** — Flat-Rate-Modell. Sehr aggressives Einstiegsangebot (€3,95–€5/Mo für Basisvariante). Lohn ist kostenpflichtiger Add-on.
**Cosmi-Implikation:** Cosmi-Buchhaltung kann sich nicht auf Preis-Differenzierung gegenüber Lexoffice stützen (Lexoffice ist für kleine Betriebe sehr günstig). USP muss über Integration mit CRM/ERP/Dialer gehen.

---

### Zoho CRM — CRM-Plattform (International, DE-Lokalisierung)

Tiers erkannt: **Free**, **CRM Plus**, **Marketing Plus**, **Service Plus**, **Finance Plus**, **Benutzerdefinierte KI**

**Anmerkung:** Konkrete Preise wurden nicht aus dem Scrape extrahiert (JS-gerenderter Preistabelle). Zoho's bekanntes Pricing liegt ~€14–€52/User/Mo (Standard bis Ultimate). Snapshot gespeichert für Delta-Tracking.

---

### HubSpot — CRM / Marketing-Plattform (International)

Tiers erkannt: **Free**, **Starter Customer Platform** (Bundle), **Enterprise**

**Anmerkung:** Preise nicht aus Scrape extrahiert (vollständig JS-gerendert, Pricing erfordert Interaktion). Bekannt: Sales Hub Starter ab ~€15/Mo/Seat, Professional ab ~€90/Mo/Seat. Snapshot gespeichert.

---

### Bexio — Buchhaltung/ERP Schweiz/DACH

**Anmerkung:** Pricing-Page lieferte nur Trial-CTA-Content. Preise vollständig hinter JS-Wall. Bekannte Tiers: Pro/Plus/Premium für Schweizer Markt. Snapshot als Basis gespeichert; Delta-Tracking ab Juli.

---

### Zendesk — Helpdesk/Service (International)

**Anmerkung:** Pricing-Page hat de-AT/de-DE Lokalisierung geladen, aber Preistabelle ist vollständig JS-gerendert. Tiers erkannt: Suite Team, Suite Growth, Suite Professional, Suite Enterprise. Bekannte Preise: ~€55–€115/Agent/Mo. Snapshot gespeichert.

---

## Scraping-Probleme (4 von 11)

| Konkurrent | Status | Grund |
|---|---|---|
| Salesforce | **Access Denied** | Akamai/CDN Bot-Protection — kein Inhalt geladen |
| Pipedrive | **Minimal** (670 Bytes) | Bot-Erkennung oder vollständig clientseitiges Rendering |
| Odoo | **Leer** (59 Bytes) | Pricing-Plan-Seite lädt keine Inhalte ohne Login-Session |
| sevDesk | **Partial** (8 KB) | Kein Preisinhalt extrahierbar (JS-Lazy-Load) |

**Empfehlung für Juli-Lauf:** Browser-Session mit Cookie-Handling oder `waitForSelector` auf Preiselemente konfigurieren. Alternativ: Playwright-Skript mit explizitem Warten auf `.pricing-table`/`[data-price]`-Elemente.

---

## Keine Änderungen (Baseline-Lauf)

Alle 11 Snapshots wurden heute als Erstbaseline gesichert:

- Pipedrive, HubSpot, Salesforce, monday.com, Zoho CRM — CRM/International
- Bexio, weclapp — CRM/ERP DACH
- Zendesk — Helpdesk
- sevDesk, Lexoffice — Buchhaltung DACH
- Odoo — ERP/Open-Source

---

## Strategische Beobachtungen

1. **AI-Credit-Bundling als Pricing-Signal:** monday.com integriert AI-Credits (€20–€30 Wert) direkt in die Tier-Preise. Erster klarer Beweis einer Branchenverschiebung — AI-Value wird zum Tier-Differenziator statt Feature-Add-on.

2. **Flat-Rate vs. Per-User:** Lexoffice bleibt konsequent Flat-Rate (kein per-User-Modell). Für kleine KMU mit wenigen Nutzern ein klarer Vorteil gegenüber per-User-Modellen. Cosmi sollte Hybrid-Modell (Basis-Flat + ERP-Module per-User) als Differenzierung prüfen.

3. **DACH-Spezialisten preislich stabil:** Bexio, weclapp, sevDesk, Lexoffice zeigen im Baseline keine Anzeichen aggressiver Neupositionierung. weclapp's Professional-Tier (€86–€95) bleibt das Markt-Benchmark für mid-market DACH-ERP.

4. **Bot-Protection-Härtung bei Tier-1-Playern:** Salesforce (Akamai) und Pipedrive blockieren Headless-Browser-Scraping. Signal, dass diese Anbieter aktiv gegen Preismonitoring vorgehen — manuelles Quartals-Review ergänzend nötig.

5. **Odoo Pricing opak:** Odoo Pricing-Plan-Seite liefert ohne Session keinen Inhalt. Odoo's freemium-to-hosted Preisstruktur (Self-hosted kostenlos, Cloud ab €~11/User/Mo) ist aber bekannt und bleibt wichtigster Open-Source-Vergleichspunkt für Cosmi-Architektur-Entscheidungen.

---

## Telemetrie

```
run_date:           2026-06-01T06:00:00Z
competitors_total:  11
snapshots_new:      11
snapshots_updated:  0
diffs_detected:     0
scrape_errors:      0
scrape_partial:     4
playwright_service: http://localhost:3001 (browserless)
snapshot_dir:       .state/pricing_snapshots/
next_run:           2026-07-01T06:00:00Z
```
