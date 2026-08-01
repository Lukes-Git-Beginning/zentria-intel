---
year: 2026
month: 8
created: 2026-08-01
competitors_checked: 11
changes_detected: 2
scrape_ok: 8
scrape_blocked: 3
scrape_errors: 0
---

# Pricing-Diff August 2026

**Routine:** intel-monthly-pricing | **Run:** 2026-08-01 06:04 CEST | **Pool:** OK
**Geprüft:** 11 Konkurrenten | **Änderungen mit Signal:** 2 | **Website-Rauschen:** 5 | **Scrape OK:** 8 | **Geblockt:** 3 | **Fehler:** 0

---

## Änderungen mit Signal (2)

---

### HubSpot — "Breeze" → "Agent Hub": AI-Produktlinie umbenannt + AEO Beta [International · Threat: HIGH]

**Pricing-URL:** https://www.hubspot.com/pricing/sales

**Diff (Schlüsselstellen):**
```diff
-    * ### Breeze
-
-AI agents and features that power the entire platform
+    * ### Agent Hub
+
+Your central home for building and managing AI agents across the platform

-    * ### [Smart CRM AI-powered, flexible CRM software ](//www.hubspot.com/products/crm/ai-crm)
+    * ### [Agent Hub Your central home for building and managing AI agents across the platform ](//www.hubspot.com/products/artificial-intelligence)

+    * ### [AEO (Beta) Answer engine optimization tools that track and improve your brand's visibility in AI results ](//www.hubspot.com/products/aeo)
```

**Interpretation:** HubSpot hat "Breeze" (das bisherige Dach-Label für AI-Agents und Features) in **"Agent Hub"** umbenannt — ein signalstarkes Rebranding: Weg von "AI-Features unter einer Marke" hin zu einem expliziten "Hub für AI-Agenten-Management". Die neue Positionierung ("Your central home for building and managing AI agents") macht AI-Agents zur eigenständigen Kategorie analog zu Marketing Hub, Sales Hub etc. Zusätzlich: **AEO (Beta)** — "Answer Engine Optimization" — als neues Tool eingeführt, das Markenvisibilität in AI-Suchergebnissen (ChatGPT, Perplexity etc.) trackt. Konkrete Pricing-Seiten-Preise bleiben JS-gerendert und nicht extrahierbar.

**Cosmi-Implikation:** HubSpot institutionalisiert AI-Agents als eigenständiges Produkt-Hub — nach monday.com ("agents included") und Zendesk ("Resolution Platform") ist dies das dritte Tier-1-Signal in 2 Monaten, das AI-Agents vom Feature zum Kern-Produkt erhebt. Cosmi sollte prüfen, ob eine ähnliche "Hub"-Kommunikation für AI-Funktionalitäten sinnvoll ist. AEO als neue Kategorie ist strategisch interessant: SEO-Konkurrenten werden zu AI-Suchbarkeits-Tools — Cosmi-Positionierung im KMU-Segment könnte von AI-Suchbarkeit profitieren.

---

### sevDesk — "Black Cyber Deal" 60%-Rabatt weiterhin aktiv (seit Sommer-Anomalie) [DACH · Threat: HIGH]

**Pricing-URL:** https://sevdesk.de/preise/

**Diff (Schlüsselstellen):**
```diff
 Black Cyber Deal
 
 60% auf alles

+### Buchhaltung Pro
+
+Perfekt für alle, die ihre Buchhaltung automatisieren und ihr Unternehmen in Echtzeit überblicken.
+
+34,90 €
+
+34,90 €
+
+pro Monat (zzgl. MwSt.)
```

**Vollpreise (August 2026 bestätigt):**

| Tier | Vollpreis/Mo | Promotion-Preis (60%) | Scope |
|---|---|---|---|
| Rechnung | €12,90 | ~€5,16 | Unbegrenzt Rechnungen, Integrationen, Support |
| Buchhaltung | €25,90 | ~€10,36 | + Belege, Finanzen, Buchhaltung, EÜR |
| Buchhaltung Pro *(neu)* | €34,90 | ~€13,96 | + Automatisierung, Echtzeit-Überblick |

**Interpretation:** Zwei Signale in einem Diff: (1) Der "Black Cyber Deal 60% auf alles" aus Juli **läuft noch immer** — ungewöhnlich für einen Promotion-Countdown, der eigentlich zeitbegrenzt war. Entweder wurde die Aktion verlängert oder der Countdown ist ein dauerhaftes Conversion-Element. (2) **Neuer Tier "Buchhaltung Pro" bei €34,90/Mo** erstmals klar extrahierbar — war im Juli-Snapshot durch Truncation-Artefakt hinter dem Schnitt. Vollpreise unverändert.

**Cosmi-Implikation:** sevDesk hat nun 3 Buchhaltungs-Tiers: €12,90 / €25,90 / €34,90. Cosmi-Buchhaltungsmodul konkurriert direkt in diesem Stack. Wichtig: Die "60%-Promotion" als Dauerzustand wirft Fragen zur Preisstrategie auf — wenn der Rabatt dauerhaft läuft, ist €5–14/Mo der faktische Marktpreis. Cosmi sollte Vollpreise kommunizieren und den Mehrwert über CRM-Integration + DSGVO-by-Design herausstellen, nicht über Aktionspreise.

---

## Keine Änderungen — Preise stabil (1)

**Zoho CRM** — Preise unverändert. Cookie-Consent-Wall weiterhin aktiv, aber Seitenstruktur vollständig geladen. Bekannte Preise Q3: Standard ~€14 | Professional ~€23 | Enterprise ~€40 | Ultimate ~€52/User/Mo.

---

## Website-Rauschen (5 Diffs ohne Pricing-Signal)

Diese Konkurrenten zeigten Diffs, aber ausschließlich durch Content-Rotation, URL-Änderungen oder Snapshot-Truncation-Artefakte — keine Preisänderungen:

| Konkurrent | Diff-Ursache | Bewertung |
|---|---|---|
| **monday.com** | Truncation-Artefakt: Snapshot-Schnitt verschoben; vollständigere Enterprise-Support-Beschreibung sichtbar. Preise unverändert: Free €0 / Basic €9 / Standard €12 / Pro €19/Seat/Mo. | Kein Signal |
| **Bexio** | `/de-CH/preise` liefert weiterhin 404-Seite; Anmeldeformular geändert: "Telefonnummer" → "E-Mail" + neues Feld "Department". Keine Pricing-Seite zugänglich. | Strukturell — URL-Konsolidierung CH bleibt unklar |
| **weclapp** | Kunden-Story-Rotation in Nav: "Lebensmittel-Branche" → "Kosmetik-Branche". Preise unverändert: ERP Starter €39 / Dienstleistung €86/€95 / Handel €163/€179. | Kein Signal |
| **Lexoffice** | eKomi-Bewertungszähler: 2.429 → 2.439 (+10 Bewertungen). Preise unverändert: S €7,90 / M €12,90 / L €21,90 / XL €32,90. 50%-Aktionsrabatt (3 Mo.) weiterhin aktiv. | Kein Signal |
| **Zendesk** | "AI Masterclass 2026" von live auf On-Demand umgestellt; URL-Slug `/why-zendesk/customers/` → `/customer/`; Sprach-Dropdown: "Dansk/Svenska" → "English (Denmark)/English (Sweden)". | Infrastruktur-/Event-Update, kein Pricing |

---

## Scraping-Probleme (3 geblockt)

| Konkurrent | Status | Details |
|---|---|---|
| Pipedrive | **Geblockt (Cloudflare)** | 195 KB Challenge-Seite — persistenter Block seit Mai 2026 |
| Salesforce | **Geblockt (Akamai)** | 311 Bytes — vollständiger CDN-Block |
| Odoo | **Leer** | 108 Bytes — Pricing-Plan ohne Login-Session inhaltslos |

**Empfehlung September-Lauf:**
- Pipedrive/Salesforce: Manuelle Quartalsprüfung (September-Deepdive-Slot); Browser-Fingerprint-Rotation unwahrscheinlich ausreichend bei Cloudflare Enterprise.
- Odoo: Cookie-Session-Persistenz im Playwright-Service konfigurieren.
- Bexio: Direkter Kontakt oder manuelle Prüfung `/de-CH/preise` — URL scheint kein pricing-spezifisches Verzeichnis zu sein.
- Discord-Webhook: 403 — Token in `.env` erneuern vor September-Lauf.

---

## Strategische Beobachtungen

1. **HubSpot "Agent Hub" markiert Reifepunkt der AI-Agent-Institutionalisierung:** Nach monday.com ("agents included" in Tier-Messaging, Juli) und Zendesk ("KI-First-Serviceplattform"-Rebranding, Juli) ist HubSpots "Agent Hub" das dritte Tier-1-Signal in zwei Monaten, das AI-Agents vom optionalen Feature zur Kern-Produkt-Kategorie erhebt. Der Markt konsolidiert sich auf eine Erwartung: Plattformen haben einen expliziten AI-Agent-Layer. Cosmi sollte vor dem Q4-Messaging-Zyklus prüfen, ob ein "Cosmi AI" oder "Cosmi Assist" als Label für AI-Funktionalitäten strategisch sinnvoll ist.

2. **AEO als neue Kategorie beobachten:** HubSpots "Answer Engine Optimization (Beta)" ist ein früher Indikator für eine neue Marktanforderung: Sichtbarkeit in AI-basierten Suchergebnissen (ChatGPT, Perplexity, Google AI Overview). Für DACH-KMU noch peripher, aber B2B-SaaS-Positionierung für AI-Suchbarkeit wird in 12–18 Monaten relevant. Cosmi-Marketing sollte dies auf dem Radar haben.

3. **sevDesk Promotion-Dauerhaftigkeit als Preisstrategie-Signal:** 60%-Rabatt seit mindestens Juli (und wahrscheinlich früher) läuft ohne erkennbares Ende — der faktische Marktpreis für Buchhaltungs-SaaS im DACH-Einstieg liegt damit bei €5–10/Mo. Dies setzt Druck auf alle DACH-Buchhaltungs-Konkurrenten. Cosmi-Buchhaltungsmodul muss Mehrwert über die reine Preisschwelle hinaus kommunizieren: CRM-native Buchführung, DSGVO-Hosting, cross-modul Kontext.

4. **Stiller Pricing-August im DACH-Kernmarkt:** Weclapp, Lexoffice, Zoho — alle preislich unverändert. DACH-Hochsommer-Preisruhe bestätigt sich. Klassisches Muster: Pricing-Revisionen folgen dem Herbst-Relaunch-Zyklus (September/Oktober). Nächste Intensiv-Review: Oktober-Lauf.

5. **Bexio bleibt strukturelles Rätsel:** Dritter Monat in Folge ohne zugängliche Pricing-Seite via Scraping (erst de-DE/404, jetzt de-CH/404). Entweder ist die Pricing-Seite hinter Login oder die URL-Struktur hat sich grundlegend geändert. Manuelle Prüfung im September-Deepdive empfohlen — strategisch relevant, da Bexio CH-Markt konsolidiert.

---

## Telemetrie

```
run_date:             2026-08-01T06:04:17Z
competitors_total:    11
scrape_ok:            8
scrape_blocked:       3  (pipedrive, salesforce, odoo)
scrape_noise:         5  (monday, bexio, weclapp, lexoffice, zendesk — diffs ohne Pricing-Signal)
changes_with_signal:  2  (hubspot, sevdesk)
snapshots_updated:    8
discord_pushed:       0  (webhook 403 — token erneuern)
playwright_service:   http://localhost:3001
snapshot_dir:         .state/pricing_snapshots/
duration_seconds:     37.2
next_run:             2026-09-01T04:00:00Z
```
