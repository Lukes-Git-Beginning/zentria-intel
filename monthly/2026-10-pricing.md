---
year: 2026
month: 10
created: 2026-10-01
competitors_checked: 11
changes_detected: 3
---

# Pricing-Diff Oktober 2026

## Aenderungen erkannt

### Bexio — Pricing-Page 404 (de-CH)
**Diff:**
```diff
- [Kostenlos testen] (Modal-Overlay auf /de-CH/preise)
+ Houston, wir haben ein 404 Problem — Die angeforderte Seite wurde in unserem bexio-Universum nicht gefunden.
```
**Interpretation:** Die Schweizer Pricing-URL `https://www.bexio.com/de-CH/preise` gibt jetzt einen 404 zurück. Im Competitors-YAML war bereits vermerkt, dass die de-DE-URL seit 2026-07-01 auf 404 läuft — nun ist offenbar auch die de-CH-URL betroffen. Bexio scheint seine Pricing-Seiten zu restrukturieren oder hinter ein Login/Formular zu verlagern.

**Cosmi-Implikation:** Bexio (threat_level: high, buchhaltung + crm-core) könnte gerade eine Pricing-Umstrukturierung oder einen Re-Launch vorbereiten. Beim nächsten Monitoring: Startseite und /de-CH/preise-Redirect prüfen. Kein direkter Preisvergleich möglich bis Seite wieder erreichbar ist.

---

### HubSpot — Erstmalige vollständige Pricing-Erfassung
**Diff:**
```diff
- [Nur Navigation / kein Pricing-Content geladen — JS-Rendering unvollständig]
+ Free: €0/mo
+ Starter: €7/mo/seat
+ Professional: €90/mo/seat
+ Enterprise: €150/mo/seat
+ Bundle-Promo: Revenue Hub Professional €57/mo/seat (war €95), Enterprise €98/mo/seat (war €140)
```
**Interpretation:** Vorgänger-Snapshot hatte nur Navigation-Markup (JS-Rendering unvollständig). Neuer Scrape liefert erstmals vollständiges Pricing. Tatsächliche Preisänderung vs. Oktober-Vorjahr nicht verifizierbar — es gilt ab jetzt: Starter **€7/seat**, Professional **€90/seat**, Enterprise **€150/seat** als Baseline.

Bemerkenswert: aktive Promo „Buy Sales Hub, get Revenue Hub Professional für €57/mo/seat (war €95/mo/seat)" — ~40% Rabatt auf Revenue Hub bei Sales Hub-Kauf. Bundling-Strategie zur Plattformausweitung.

**Cosmi-Implikation:** HubSpot Starter bei €7/seat ist ein aggressiver Einstiegspreis für KMU. Cosmi-COSMI-Sales (ca. €19/seat) braucht klare Differenzierung: DACH-Compliance, Modularität, keine Onboarding-Pflichtgebühr (HubSpot verlangt €1.470 einmalig für Professional Onboarding). USP-Kommunikation gegenüber HubSpot-Vergleichen stärken.

---

### Zoho CRM — Erstmalige vollständige Pricing-Erfassung
**Diff:**
```diff
- [Nur Navigation + Cookie-Consent — kein Pricing geladen]
+ Standard: €14/Benutzer/Monat
+ Professional: €23/Benutzer/Monat
+ Enterprise: €40/Benutzer/Monat
+ Ultimate: €52/Benutzer/Monat
+ Free (Starter): €0/Benutzer/Monat
```
**Interpretation:** Analog zu HubSpot: Vorgänger-Snapshot war leer (Cookie-Overlay blockierte Content). Neue Baseline gesetzt. Zoho CRM positioniert sich im DACH-Markt mit Standard ab **€14/Benutzer/Monat** — erheblich unter den meisten DACH-Spezialisten.

**Cosmi-Implikation:** Zoho Standard (€14) und Professional (€23) sind die günstigsten vollständigen CRM-Optionen im Vergleichsfeld. Cosmi muss DACH-spezifische Features (E-Rechnung, DATEV-Integration, deutsche Oberfläche, EU-Hosting) als Mehrwert klar herausstellen — rein preislich ist Zoho kaum zu unterbieten.

---

## Keine Aenderungen (8 Konkurrenten)

### Stabile Preise

| Anbieter | Tiers / Preise | Billing | Stand |
|---|---|---|---|
| **monday.com** | Free €0 · Basic €9 · Standard €12 · Pro €19 / Seat (10 Seats) | Jährlich | Bestätigt |
| **weclapp** | ERP Starter €39 · ERP DL €86 (jährl.) / €95 (monatl.) · ERP Handel €163 (jährl.) / €179 (monatl.) | Per User/Monat | Bestätigt |
| **Zendesk** | Support Team €19 · Suite Team €55 · Suite Professional €115 (jährl.) | Per Agent/Monat | Bestätigt |
| **sevDesk** | Rechnung €12,90 · Buchhaltung €25,90 · Buchhaltung Pro €34,90 | Monatlich | Bestätigt |
| **Lexoffice** | XS €5 (–50%) · S €6,45 (–50%) · M €10,95 (–50%) · XL €16,45 (–50%) zzgl. MwSt | Monatlich (kündbar) | Bestätigt, 50%-Rabatt-Promo aktiv |

### Nicht zugänglich — Cloudflare / Bot-Schutz (konsistent seit mehreren Monaten)

| Anbieter | Status | Letzter gültiger Snapshot |
|---|---|---|
| **Pipedrive** | Cloudflare-Block (Ray ID wechselt, Inhalt gleich) | Kein valider Snapshot vorhanden |
| **Salesforce** | Akamai Access Denied | Kein valider Snapshot vorhanden |
| **Odoo** | 403 Forbidden | Kein valider Snapshot vorhanden |

---

## Strategische Beobachtungen

1. **DACH-Spezialisten bleiben preislich stabil.** sevDesk, weclapp und Lexoffice haben im Oktober keine Preisanpassungen vorgenommen. Lexoffice hält die 50%-Rabatt-Promo aufrecht — möglicherweise dauerhaft als effektiver Einstiegspreis.

2. **HubSpot Bundling-Strategie.** Die Revenue Hub-Promo (€57 statt €95 bei Sales Hub-Kauf) zeigt HubSpots Platform-Lock-in-Strategie. KMU werden mit günstigem Sales Hub gelockt und dann mit Revenue Hub ans Ökosystem gebunden. Für Cosmi relevant: eigene Modular-Bundling-Kommunikation.

3. **Bexio pricing-seitig offline.** Zwei von zwei Bexio-URLs (de-DE seit Juli, de-CH jetzt) geben 404. Entweder ist ein Website-Relaunch im Gange oder das Pricing wurde intentional aus dem Public Web entfernt (Sales-Funnel-Strategie). Monitoring der Bexio-Startseite empfohlen.

4. **Zoho als Preis-Benchmark.** Mit €14/User/Monat (Standard) und €23 (Professional) ist Zoho die günstigste vollwertige CRM-Option im Tracking. Kunden, die Cosmi mit "aber Zoho ist billiger" vergleichen, müssen gezielt mit DACH-Compliance und Integrations-Depth adressiert werden.

5. **3 von 11 Konkurrenten dauerhaft nicht scrapebar.** Pipedrive, Salesforce und Odoo blockieren Bot-Zugriffe konsequent. Alternative Quellen prüfen: G2-Pricing-Daten, manuelle Quartals-Checks, LinkedIn-Announcements für Preisänderungen dieser Anbieter.

6. **monday.com Promo-Mechanismus aktiv.** Alle Tiers zeigen eine "Special offer: €10/€20/€30 off/month" — vermutlich saisonal oder laufend. Effektive Preise sind Basic €9 statt €19, Standard €12 statt €14, Pro €19 statt €22 (pro Monat, 10 Seats, jährlich).
