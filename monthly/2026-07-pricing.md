---
year: 2026
month: 7
created: 2026-07-01
competitors_checked: 11
changes_detected: 4
scrape_ok: 6
scrape_blocked: 3
scrape_partial: 2
---

# Pricing-Diff Juli 2026

**Routine:** intel-monthly-pricing | **Run:** 2026-07-01 06:05 CEST | **Pool:** OK
**Geprüft:** 11 Konkurrenten | **Änderungen:** 4 | **Scrape OK:** 6 | **Geblockt:** 3 | **Partial:** 2

---

## Änderungen erkannt (4)

---

### monday.com — AI Agents jetzt in allen Paid-Tieren enthalten [International · Threat: HIGH]

**Pricing-URL:** https://monday.com/pricing

**Diff (Schlüsselstellen):**
```diff
-# Plans for every team.
+# Plans for every team,
+people and agents included.

 Free €0 / Basic €9/seat / Standard €12/seat / Pro €19/seat

+AI agent workforce
+  Agents take on specialized tasks and support multiple functions
+  for automated execution at scale
+
+Orchestrate workflows that connect agents and AI and watch work
+get done across every team
+
+Enable agents, integrations, and custom apps to read and update
+monday data. Buy more as needed
```

**Preise:** Unverändert — Free €0 | Basic €9/Seat/Mo | Standard €12 | Pro €19

**Interpretation:** monday.com hat die Pricing-Page-Headline geändert von "Plans for every team" zu "Plans for every team, **people and agents included**". AI-Agents ("AI agent workforce") sind jetzt explizit Bestandteil aller Paid-Tier-Beschreibungen — nicht mehr optionales Add-on, sondern im Tier-Bundle kommuniziert. Der "Basic AI"-Label ist neu im Tier-Stack aufgetaucht.
**Cosmi-Implikation:** monday.com führt die Branche im AI-Agent-Bundling — nach den AI-Credits im Juni (€20–€30 Wert je Tier) jetzt explizites "agents included"-Messaging. Cosmi muss eigene AI-Agent-Roadmap in der Tier-Kommunikation verankern. Risiko: Kunden erwarten bald, dass SaaS-Plattformen AI-Agents "mitliefern", nicht separat verkaufen.

---

### sevDesk — "Black Cyber Deal" Promotion aktiv: bis zu 60% Rabatt [DACH · Threat: HIGH]

**Pricing-URL:** https://sevdesk.de/preise/

**Diff (Schlüsselstellen):**
```diff
-[Juni-Baseline: JS-Lazy-Load — kein Pricing-Inhalt extrahierbar]
+# Wir haben den passenden Tarif für dein Unternehmen
+
+Sichere dir jetzt bis zu **50% Rabatt** auf deinen Wunschtarif [Countdown aktiv]
+
+Black Cyber Deal — 60% auf alles
+
+12,90 €/Mo   (Rechnungen-Tier, Vollpreis)
+25,90 €/Mo   (Buchhaltung-Tier, Vollpreis)
```

**Vollpreise (erstmals sauber extrahiert):**

| Tier | Vollpreis/Mo | Aktionspreis (60% Rabatt) | Scope |
|---|---|---|---|
| Rechnungen | €12,90 | ~€5,16 | Unbegrenzt Rechnungen, Integrationen, Support |
| Buchhaltung | €25,90 | ~€10,36 | + Belege, Finanzen, Buchhaltung, EÜR |

**Interpretation:** Juni-Baseline hatte keinen verwertbaren Preisinhalt (JS-Lazy-Load). Heute erstmals saubere Extraktion: Vollpreise €12,90/€25,90. Dazu läuft eine "Black Cyber Deal"-Aktion mit Countdown-Timer — ungewöhnlich für Juli (Cyber-Deals normalerweise November). Entweder Sommer-Rabatt mit neuem Namen oder Reaktion auf Marktdruck. Der "60% auf alles"-Anspruch ist bemerkenswert aggressiv.
**Cosmi-Implikation:** sevDesk positioniert sich mit diesem Deal aggressiv am Einstiegsmarkt (~€5–€10/Mo). Cosmi-Buchhaltungsmodul sollte Vollpreise kommunizieren und Mehrwert gegenüber €12,90 sevDesk-Tier herausstellen (DACH-Compliance, CRM-Integration, API-Tiefe). Aktionspreise sind temporär — Vollpreisvergleich bleibt relevant.

---

### Bexio — Pricing-URL 404: de-DE-Seite nicht mehr verfügbar [DACH · Threat: HIGH]

**Pricing-URL (alt):** https://www.bexio.com/de-DE/preise → **404 Not Found**

**Diff:**
```diff
-[Juni-Snapshot: bexio.com/de-DE/preise — Pricing-Elemente hinter JS-Wall, 124 Zeilen]
+# Houston, wir haben ein 404 Problem
+[Vollständige 404-Seite — ausschließlich /de-CH/-Links sichtbar]
```

**Interpretation:** Die `/de-DE/preise`-URL liefert 404. Die 404-Seite enthält ausschließlich `/de-CH/`-Links — Bexio hat die Deutschland-Lokalisierung unter `/de-DE/` vermutlich entfernt oder auf `/de-CH/` konsolidiert. Mögliche neue URL: `https://www.bexio.com/de-CH/preise`. Dies signalisiert eine Markt-Strategie-Änderung: Rückzug aus explizitem DE-Targeting, Fokus auf Schweiz-Branding.
**Cosmi-Implikation:** Bexio repositioniert sich als CH-Produkt. Für Cosmi-DACH: schärfere Differenzierung über "echtes DACH-Produkt" (DE+AT+CH) vs. CH-only Bexio möglich. Pricing-URL in `_competitors.yaml` auf `/de-CH/preise` aktualisiert.

---

### Zendesk — "Resolution Platform" AI-First Rebranding auf Pricing-Seite [International · Threat: HIGH]

**Pricing-URL:** https://www.zendesk.com/pricing/

**Diff (Schlüsselstellen):**
```diff
-[Juni: Suite Team/Growth/Professional/Enterprise Tier-Navigation, ~€55–€115/Agent/Mo]
+Zendesk Resolution Platform
+  "die einzige KI-First-Serviceplattform"
+
+Neue Produktkategorien ab Pricing-Seite:
+  AI Agents — "Lösen Sie selbst komplexeste Anliegen – autonom"
+  Copilot — "der einzige proaktive KI-Assistent"
+  Qualitätssicherung — "automatisches Scoring von AI Agents"
+  Workforce Management — "KI-gestützte Präzision"
```

**Interpretation:** Zendesk hat die Pricing-Seite auf "Resolution Platform" + "KI-First-Serviceplattform" umgestellt. AI Agents und Copilot sind jetzt eigenständige Produktkategorien ab der Pricing-Seite — veränderte Kaufreise. Konkrete Suite-Preise bleiben JS-gerendert, aber das Produkt-Framing hat sich fundamental verändert: von "Ticketing-Tiers" zu "AI-First-Resolution-Platform". AI-Features werden als Kern-Value-Prop, nicht als Add-on positioniert.
**Cosmi-Implikation:** Zendesk setzt Branchenstandard: AI-Agents werden zur Kernfunktion, nicht zum Upgrade. Cosmi-Helpdesk muss AI-Triage, Auto-Resolution und Copilot-Assistenz als Tier-Kern kommunizieren. Wenn Zendesk AI inklusive macht, erhöht sich der wahrgenommene Wert von AI-Helpdesk-Lösungen generell — Cosmi profitiert, wenn es frühzeitig positioniert ist.

---

## Keine Änderungen (2 / stabil geprüft)

**weclapp** — Preise unverändert: ERP Starter €39 | Professional €86/€95 (jährlich/monatlich) | Enterprise €163/€179

**Lexoffice** — Preise unverändert: XS €11/€5 | S €7,90/€3,95 | M €12,90/€6,45 | L €21,90/€10,95 | XL €32,90/€16,45. 50%-Aktionsrabatt (3 Mo.) weiterhin aktiv — unverändert seit Juni.

---

## Partial / Kein Diff möglich (2)

**Zoho CRM** — Cookie-Consent-Wall verhindert Preistabellen-Rendering. Kein Diff möglich. Bekannte Preise per Q2: Standard ~€14 | Professional ~€23 | Enterprise ~€40 | Ultimate ~€52/User/Mo.

**HubSpot** — Pricing-Tabelle weiterhin vollständig JS-gerendert. Strukturinhalt extrahiert (Tier-Labels Starter/Professional/Enterprise Sales Hub), keine Preiszahlen. Kein Diff-Signal.

---

## Scraping-Probleme (3 geblockt)

| Konkurrent | Status | Details |
|---|---|---|
| Pipedrive | **Geblockt (Cloudflare)** | Eindeutiger Block: "Sorry, you have been blocked" — 195 KB Challenge-Seite |
| Salesforce | **Geblockt (Akamai)** | 311 Bytes — vollständiger CDN-Block |
| Odoo | **Leer** | 108 Bytes — Pricing-Plan ohne Login-Session inhaltslos |

**Empfehlung für August-Lauf:**
- Bexio: URL auf `https://www.bexio.com/de-CH/preise` aktualisiert (in `_competitors.yaml` erledigt)
- Pipedrive/Salesforce: Browser-Fingerprint-Rotation oder manuelle Quartalsprüfung
- Zoho/HubSpot: `waitForSelector` auf Preis-Container konfigurieren (`.pricing-table`, `[data-price]`)
- Discord-Webhook: 403-Fehler — Token prüfen und in `.env` erneuern

---

## Strategische Beobachtungen

1. **AI-Agents-als-Standard-Erwartung beschleunigt sich:** monday.com setzt mit "people and agents included" einen neuen Messaging-Standard — AI Agents gehören wie Nutzer-Seats zur Basiskommunikation. Zendesk folgt mit "KI-First-Serviceplattform"-Rebranding. Damit haben zwei Tier-1-Platformen im Juli den Shift von "AI-Feature" zu "AI-Default" vollzogen. Cosmi muss diese Rhetorik im Q3-Messaging adaptieren — am besten vor Herbst-Relaunch-Welle der Konkurrenten.

2. **sevDesk-Sommerpromotion als Marktdruck-Signal:** "Black Cyber Deal" im Juli ist ungewöhnlich (normalerweise Q4). Mögliche Interpretation: Marktdruck durch günstigere Alternativen (Lexoffice Vollpreis €7,90 vs. sevDesk €12,90). Aggressive 60%-Promotion könnte Reaktion auf Churn-Druck sein. Cosmi sollte sevDesk nicht nach Aktionspreisen, sondern nach Vollpreisen vergleichen.

3. **Bexio zieht sich aus DE-URL-Struktur zurück:** `/de-DE/` → 404 signalisiert Fokussierung auf CH-Markt. Dies ist eine strategische Öffnung: Cosmi kann die DACH-Flächendeckung (DE + AT + CH) als klaren Vorteil kommunizieren gegenüber einem nun explizit CH-orientierten Bexio.

4. **Bot-Schutz bei Tier-1-Playern bleibt hart:** Pipedrive (Cloudflare), Salesforce (Akamai), Odoo (Session-Gate) — drei relevante Konkurrenten weiterhin nicht scrappable. Manuelles Q3-Review für diese drei empfohlen (September-Deepdive).

5. **DACH-Kernpreise stabil:** weclapp und Lexoffice zeigen keinerlei Preisbewegung. DACH-Sommerpreisruhe bestätigt sich — Herbst-Repricing-Welle (Sept/Okt) typisch. Nächste Intensiv-Review: Oktober-Lauf.

---

## Telemetrie

```
run_date:             2026-07-01T06:05:29Z
competitors_total:    11
scrape_ok:            6
scrape_blocked:       3  (pipedrive, salesforce, odoo)
scrape_partial:       2  (zoho, hubspot)
changes_detected:     4  (monday, sevdesk, bexio, zendesk)
snapshots_updated:    8
discord_pushed:       0  (webhook 403 — token prüfen)
playwright_service:   http://localhost:3001 (Chrome/147.0.7727.15)
snapshot_dir:         .state/pricing_snapshots/
duration_seconds:     75
next_run:             2026-08-01T04:00:00Z
```
