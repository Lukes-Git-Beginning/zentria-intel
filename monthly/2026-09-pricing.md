---
year: 2026
month: 9
created: 2026-09-01
competitors_checked: 11
changes_detected: 4
scrape_ok: 8
scrape_blocked: 3
scrape_errors: 0
---

# Pricing-Diff September 2026

**Routine:** intel-monthly-pricing | **Run:** 2026-09-01 06:02 CEST | **Pool:** OK
**Geprüft:** 11 Konkurrenten | **Änderungen mit Signal:** 4 | **Website-Rauschen:** 4 | **Scrape OK:** 8 | **Geblockt:** 3 | **Fehler:** 0

---

## Änderungen mit Signal (4)

---

### Zendesk — Erste saubere Preis-Extraktion: €19 / €55 / €115 + "Suite Enterprise + Copilot" [International · Threat: HIGH]

**Pricing-URL:** https://www.zendesk.com/pricing/

**Diff (Schlüsselstellen):**
```diff
+# Preise für die beste KI-gestützte Lösung für den Kundenservice
+
+MonatlichJährlich
+20% Rabatt bei jährlicher Abrechnung
+
+### Support Team
+19 €  Kundendienst-Mitarbeiter:in/Monat, jährlich bezahlt
+
+### Suite Team
+55 €  Kundendienst-Mitarbeiter:in/Monat, jährlich bezahlt
+
+### Suite Professional
+115 €  Kundendienst-Mitarbeiter:in/Monat, jährlich bezahlt
+
+### Suite Enterprise + Copilot
+Vertrieb kontaktieren
```

**Vollpreise September 2026 (erstmals klar extrahiert):**

| Tier | Preis/Agent/Mo (jährlich) | Scope |
|---|---|---|
| Support Team | **€19** | Gemeinsamer Posteingang, grundlegender Support |
| Suite Team | **€55** | + Omnichannel, AI Agents |
| Suite Professional | **€115** | + Fortschrittliche Automatisierung, KI-Insights |
| Suite Enterprise + Copilot | **Custom** | + Copilot (AI-Assistent) direkt gebündelt |

**Interpretation:** Zwei Signale in einem: (1) Erstmals sind Zendesks konkrete Preise aus dem Playwright-Scrape sauber extrahierbar — bisherige Snapshots zeigten nur Navigations-HTML. Die Preise selbst sind nicht neu, aber die Extraktion ist jetzt stabil. (2) **Produktname-Signal**: Der Enterprise-Tier heißt jetzt explizit "Suite Enterprise + **Copilot**" — Copilot (Zendesks proaktiver AI-Assistent) ist nicht mehr Add-on, sondern namentlich im Enterprise-Plan verankert. Das ist die gleiche Institutionalisierungs-Logik wie HubSpots "Agent Hub" (August).

**Cosmi-Implikation:** Zendesk positioniert AI als Tier-Differenzierungsmerkmal: AI Agents ab Suite Team (€55), Copilot erst ab Enterprise. Das erzeugt eine deutliche Preislücke zwischen €55 und €115. Cosmi-Helpdesk konkurriert im €19–€55-Bereich; wenn AI-Features dort inkludiert sind, entsteht Preisdruck. Die Bundle-Logik "AI im Enterprise" ist ein Warnsignal für alle DACH-KMU-Anbieter: was heute Enterprise-Vorteil ist, wird in 12–18 Monaten Standard-Erwartung.

---

### monday.com — Automations/Integrations → "Workflows"; "Limited" von Basic AI Agent entfernt [International · Threat: HIGH]

**Pricing-URL:** https://monday.com/pricing

**Diff (Schlüsselstellen):**
```diff
-Automations (250 actions / month)
-Integrations (250 actions / month)
+3 workflows
+(250 actions / month)

-6 tools · 3,000 AI credits / month
+Premium AI (ohne Credits-Angabe im Header)

-AI agent workforce
-Limited
+AI agent workforce
 (ohne "Limited"-Qualifier)

-Enable agents, integrations, and custom apps to read and update monday data.
+Enable external agents, integrations, and custom apps to read and update monday data.
```

**Tier-Übersicht (unveränderte Preise):**

| Tier | Preis/Seat/Mo (jährlich) | Workflows/Mo | AI Credits/Mo |
|---|---|---|---|
| Free | €0 | — | Basic AI |
| Basic | €9 | — | 1.000 Credits |
| Standard | €12 | 3 workflows / 250 Actions | 2.000 Credits |
| Pro | €19 | 20 workflows / 25.000 Actions | 3.000 Credits |
| Enterprise | Custom | Unbegrenzt | Custom |

**Interpretation:** monday.com vereinheitlicht sein Automatisierungs-Paradigma: Die bisherige Trennung von "Automations" und "Integrations" (getrennte Limits) wird zu **"Workflows"** als einheitliches Konzept zusammengeführt. Das signalisiert eine Architektur-Vereinfachung und AI-Alignment — "Workflows" passt besser zur AI-Agent-Sprache ("AI workflow builder") als die technischen Begriffe "Automations/Integrations". Ebenfalls wichtig: Der "**Limited**"-Qualifier bei "AI agent workforce" im Basic-Tier ist weggefallen — das suggeriert, dass AI-Agents im Basic-Tier jetzt vollwertig zugänglich sind (oder die Einschränkung kommunikativ eliminiert wurde). "External agents" (vs. "agents") macht API-Zugang für Drittparteien expliziter.

**Cosmi-Implikation:** monday.com vereinfacht seine Messaging-Struktur und entfernt Limitation-Qualifier bei AI. Cosmi sollte ähnliche Klarheit anstreben: Weniger "mit Einschränkungen verfügbar" und mehr transparente Inklusion. Die Workflow-Terminologie ist eine Kategorie, die Cosmi für cross-modul-Automatisierung (z.B. CRM → Rechnungen → Schichten) nutzen könnte.

---

### weclapp — Feature-Liste umstrukturiert: "Angebote & Rechnungen" aus ERP Starter entfernt [DACH · Threat: HIGH]

**Pricing-URL:** https://www.weclapp.com/de/preise

**Diff (Schlüsselstellen):**
```diff
 ### ERP Starter
 Für (noch) kleine Teams, die durchstarten wollen.
 € 39 pro Monat/Nutzer*

   * __ Kontaktmanagement
-  * __ Angebote & Rechnungen

 ### ERP Dienstleistung
 € 86 pro Monat/Nutzer*
   * __ Alles aus ERP Starter
   * __ CRM
-  * __ Aufgaben, Kalender & Kampagnen

+🚀 [Jetzt zur Product Tour anmelden!]
+📑 weclapp x OMR Whitepaper: B2B Handel 2026
```

**Preise (unverändert):**

| Tier | Preis jährlich | Preis monatlich |
|---|---|---|
| ERP Starter | €39/Nutzer/Mo | €39/Nutzer/Mo |
| ERP Dienstleistung | €86/Nutzer/Mo | €95/Nutzer/Mo |
| ERP Handel | €163/Nutzer/Mo | €179/Nutzer/Mo |
| Enterprise | Individuell | Individuell |

**Interpretation:** Zwei strukturelle Änderungen in der Feature-Darstellung: (1) **"Angebote & Rechnungen" aus ERP Starter entfernt** — dies war eine der Kernfunktionen des Einstiegstarifs. Entweder wurde das Feature in ein höheres Tier verschoben, oder die Darstellung auf der Pricing-Page wurde reduziert (da ERP Starter laut "Nur monatlich buchbar"-Hinweis ohnehin eingeschränkt bleibt). Bedarf manueller Verifikation. (2) **"Aufgaben, Kalender & Kampagnen" aus ERP Dienstleistung entfernt** — ähnliches Muster. Zusätzlich: zwei neue Marketing-Banner deuten auf aktiven Herbst-Relaunch-Zyklus hin (Product Tour + OMR Whitepaper).

**Cosmi-Implikation:** Wenn weclapp "Angebote & Rechnungen" aus dem Starter-Tier entfernt hat (und nicht nur aus der Darstellung), wäre das eine messbare Feature-Degradation im DACH-ERP-Einstiegsmarkt. Cosmi-Buchhaltungsmodul könnte als vollständige Alternative positioniert werden. Manuelle Verifikation empfohlen vor nächstem Friday-Watch.

---

### sevDesk — "60% auf alles" Tagline verschwunden; Buchhaltungs-AI-Features aus Beta entlassen [DACH · Threat: HIGH]

**Pricing-URL:** https://sevdesk.de/preise/

**Diff (Schlüsselstellen):**
```diff
 Black Cyber Deal

-60% auf alles

 -{percentage}% mit {coupon}

+  * KI-gestützte Belegerfassung   ← kein "Beta:" mehr
+  * EÜR und GuV für deine Steuererklärung
+  * Online-Banking Verknüpfung
+  * Abschreibungen
+  * Auftragsbestätigungen
+  * Kassenbuchführung
```

**Vollpreise (unverändert):**

| Tier | Preis/Mo (zzgl. MwSt.) | Promotion-Mechanismus |
|---|---|---|
| Rechnung | €12,90 | `{percentage}% mit {coupon}` |
| Buchhaltung | €25,90 | `{percentage}% mit {coupon}` |
| Buchhaltung Pro | €34,90 | `{percentage}% mit {coupon}` |

**Interpretation:** Zwei Signale: (1) **"60% auf alles" entfernt**: Der Black Cyber Deal-Banner existiert noch, aber das aggressive "60% auf alles"-Claim ist aus dem Pricing-Text verschwunden. Der Countdown-Timer läuft weiter, der Rabatt-Mechanismus ist nun generisch als `{percentage}%` platzhalterisch implementiert — das deutet auf ein Kampagnen-System hin, das je nach Kampagne dynamisch befüllt wird. Der Dauerrabatt-Zustand aus dem Sommer könnte sich normalisiert haben. (2) **KI-Belegerfassung GA**: Was im Juli/August als "Beta:" markiert war, ist jetzt ohne Beta-Qualifier in der Buchhaltungs-Feature-Liste — "KI-gestützte Belegerfassung" ist General Availability. Das ist ein Produkt-Reifegrad-Signal.

**Cosmi-Implikation:** sevDesk bewegt sich auf GA-Status für AI-Features in der Buchhaltung — KI-Belegerfassung ist jetzt Standard im €25,90-Tier. Cosmi-Buchhaltungsmodul muss eine Antwort auf KI-Belegerfassung haben, um konkurrenzfähig zu bleiben. Die Normalisierung des Rabatts (weg von aggressivem "60% auf alles") ist ein positives Signal für den DACH-Marktpreis — Vollpreise bleiben stabil.

---

## Website-Rauschen (4 Diffs ohne Pricing-Signal)

| Konkurrent | Diff-Ursache | Bewertung |
|---|---|---|
| **HubSpot** | Rendering-Artefakt: Whitespace-Komprimierung, Nav-Struktur leicht geändert. Agent Hub, AEO Beta unverändert. Preise weiterhin JS-Only. | Kein Signal |
| **Zoho CRM** | Cookie-Consent-Banner-Redesign: neue Buttons "Alle Cookies akzeptieren / Nicht essenzielle Cookies ablehnen". Navigationskomprimierung. Preise unverändert: Standard ~€14 / Professional ~€23 / Enterprise ~€40 / Ultimate ~€52/User/Mo. | Kein Signal |
| **Lexoffice** | Reihenfolge-Tausch in der Preis-Darstellung: Aktionspreis jetzt VOR Vollpreis angezeigt (5,00 € vor 11,00 €). Preise unverändert: S €7,90 / M €12,90 / L €21,90 / XL €32,90. 50% Aktionsrabatt (3 Mo.) weiterhin aktiv. | Kein Signal |
| **Bexio** | 404-Seite (**„Houston, wir haben ein 404 Problem"**) ist verschwunden — Seite lädt jetzt ohne 404-Header. Aber: Inhalt ist weiterhin nur das generische Anmeldeformular, keine Pricing-Tabelle sichtbar. Neu: reCAPTCHA auf Signup-Form. | Strukturell — Pricing-URL möglicherweise reaktiviert, aber Inhalt noch nicht zugänglich. Manuelle Prüfung. |

---

## Scraping-Probleme (3 geblockt — unverändert seit Mai)

| Konkurrent | Status | Details |
|---|---|---|
| Pipedrive | **Geblockt (Cloudflare)** | 195 KB Challenge-Seite — persistenter Block seit Mai 2026 |
| Salesforce | **Geblockt (Akamai)** | 311 Bytes — vollständiger CDN-Block |
| Odoo | **Geblockt (403)** | 108 Bytes — Login-Session erforderlich |

**Empfehlung Oktober-Lauf:**
- Bexio: Neu prüfen, ob `/de-CH/preise` jetzt Pricing-Content liefert (404 ist weg) — evtl. JS-render-Wartezeit erhöhen.
- weclapp "Angebote & Rechnungen": Manuelle Verifikation, ob Feature aus Starter-Tier entfernt wurde oder nur aus der Feature-Liste auf der Pricing-Page.
- Discord-Webhook: Token in `.env` erneuern (seit August 403).

---

## Strategische Beobachtungen

1. **Zendesk institutionalisiert Copilot im Enterprise-Tier:** "Suite Enterprise + Copilot" als expliziter Produktname markiert, dass Zendesk AI-Agenten (Copilot) nicht als Upsell, sondern als Enterprise-Definitionsmerkmal positioniert. Nach HubSpot "Agent Hub" (August) und monday.com "Agents Included" (Juli/August) ist dies das vierte Tier-1-Signal in drei Monaten: **AI-Agents werden zum Enterprise-Definiendum**. Cosmi muss in Q4 eine klare AI-Positionierung haben — nicht als Feature-Liste, sondern als Tier-Differenzierung.

2. **monday.com "Workflows" als neue Kategorie-Sprache:** Die Zusammenführung von Automations+Integrations zu "Workflows" ist ein sprachliches Signal für AI-Paradigma-Shift. Workflows inkludieren Agents, Actions und Integrationen als einheitliches Konzept. Cosmi sollte prüfen, ob "Workflow"-Terminologie für cross-modulare Automatisierung (CRM→Buchhaltung→Schichten) eine stärkere Positionierung bietet als "Integrationen".

3. **sevDesk AI-Belegerfassung: GA-Status als Kategorie-Anhebung:** Mit der GA-Markierung von KI-Belegerfassung im Buchhaltungs-Tier (€25,90/Mo) ist AI-gestützte Buchhaltung jetzt im DACH-Preissegment unter €30/Mo Standard. Das setzt die Erwartungsleiste für alle DACH-Buchhaltungsanbieter — Cosmi inklusive. Wer AI-Belegerfassung nicht hat oder kommuniziert, ist im KMU-Buchhaltungsmarkt in 2026/27 nicht mehr auf Augenhöhe.

4. **Herbst-Relaunch-Zyklus beginnt:** weclapp's neue Marketing-Banner ("Product Tour", "OMR Whitepaper B2B Handel 2026"), sevDesks GA-Feature-Releases und Zendeks Preis-Sichtbarmachung deuten alle auf den klassischen Herbst-Relaunch-Zyklus (September/Oktober) hin, den der August-Report antizipiert hat. Oktober-Lauf wird voraussichtlich mehr strukturelle Pricing-Änderungen zeigen.

5. **Bexio: Watchlist** — Vierter Monat, in dem Bexio keine zugängliche Pricing-Seite liefert, aber erstmals ist die 404-Seite verschwunden. Das Schweizer Marktlayout könnte sich im Oktober klären. Bexio bleibt strategisch relevant (CH-Markt).

---

## Telemetrie

```
run_date:             2026-09-01T06:02:14Z
competitors_total:    11
scrape_ok:            8
scrape_blocked:       3  (pipedrive, salesforce, odoo)
scrape_noise:         4  (hubspot, zoho, lexoffice, bexio — diffs ohne Pricing-Signal)
changes_with_signal:  4  (zendesk, monday, weclapp, sevdesk)
snapshots_updated:    8
discord_pushed:       0  (webhook 403 — token erneuern)
playwright_service:   http://localhost:3001
snapshot_dir:         .state/pricing_snapshots/
duration_seconds:     41.8
next_run:             2026-10-01T04:00:00Z
```
