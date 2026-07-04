---
date: 2026-07-04
type: regulation
runtime_minutes: 20
items_scanned: 63
items_relevant: 16
sources_live_rss: 1
sources_403: 2
sources_404: 6
sources_live_list: [bsi-warnungen]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 9
kw: 27
---

# Regulation-Sweep KW27/2026 (Sa 4. Juli)

> **KW27-Scope:** 28. Juni – 4. Juli 2026. Referenz-Sweep: KW26 (27. Juni). Neue BSI-Items: ~12 (KRITISCH/HOCH/MITTEL). WebSearch-Supplements: 9 Policy-Updates.
>
> **🔴 DPF-KRISE — US SUPREME COURT ANNULLIERT FTC-UNABHÄNGIGKEIT:** SCOTUS-Urteil *Trump v. Slaughter* (Juni 2026) erklärt FTC-Unabhängigkeit für verfassungswidrig. Die EC hat die DPF-Adequacy-Entscheidung 259 Mal auf FTC-Unabhängigkeit gestützt. noyb fordert formale Rücknahme der Adequacy-Entscheidung (Brief 30. Juni). DPF formal weiterhin gültig — aber erhebliche Rechtsunsicherheit für alle EU-US-Datentransfers.
>
> **🔴 NIS2 BSI-REGISTRIERUNG: FRIST 31. JULI 2026 — NUR 27 TAGE:** Von ca. 29.500 betroffenen Unternehmen haben erst ~11.500 registriert. BSI verlängerte auf 31. Juli. Bußgeld bis €500.000 + persönliche Geschäftsführerhaftung (§38 BSIG).
>
> **🟢 AI ACT OMNIBUS: EU-RAT STIMMT AM 29. JUNI ZU — ANNEX III DEADLINE AUF 02.12.2027 VERSCHOBEN.** Trilateral­verfahren abgeschlossen. OJ-Publikation erwartet vor 02.08.2026. Art. 50 Transparenz-Pflicht (Chatbot-Offenlegung) bleibt 02.08.2026 — unverändert!
>
> **🔴 BSI KRITISCH — Node.js (WID-SEC-2026-0098):** Mehrere Schwachstellen inkl. RCE + Privilege Escalation. Backend-Services sofort aktualisieren.

---

## DSGVO / Datenschutz

### 🔴 noyb — US Supreme Court ruiniert EU-US-Datentransfers: DPF-Krise *(29.–30. Juni 2026)*

[US Supreme Court just blew up EU-US Data Transfers](https://noyb.eu/en/us-supreme-court-just-blew-eu-us-data-transfers) — noyb, 29. Juni 2026 | [Techzine-Analyse](https://www.techzine.eu/news/privacy-compliance/142557/eu-us-data-privacy-framework-shaken-to-its-core/) | [activeMind.legal](https://www.activemind.legal/guides/dpf-supreme-court/)

Der US Supreme Court hat in *Trump v. Slaughter* (Juni 2026) entschieden, dass die Unabhängigkeit der FTC (Federal Trade Commission) verfassungswidrig ist. Das ist ein direkter Treffer für das **EU-US Data Privacy Framework (DPF)**: Die Europäische Kommission hat die aktuelle DPF-Adequacy-Entscheidung **259 Mal** auf die FTC-Unabhängigkeit gestützt. Die FTC ist die zentrale US-Aufsichtsbehörde, deren Unabhängigkeit die EC als äquivalent zum EU-Datenschutzstandard anerkannt hatte.

**Aktuelle Lage:**
- DPF bleibt formal gültig — keine Court-Entscheidung hat es annulliert
- noyb-Brief vom 30. Juni 2026 fordert EC auf, Adequacy-Entscheidung "geordnet zurückzuziehen"
- noyb plant CJEU-Klage (Zeitrahmen: 2–3 Jahre)
- SCCs und BCRs ebenfalls betroffen: Verweisen auf US-Oversight-Bodies (PCLOB, DPRC), die jetzt ebenfalls kompromittiert sind
- Max Schrems: *"Die Grundlage für jeden EU-US-Datentransfer-Deal ist tot."*

*Cosmi-Implikation:* **Sofort-Audit aller US-SaaS-Abhängigkeiten, die auf DPF basieren.** Priorität: Welche Cloud-Dienste (z. B. AWS, Google Workspace, Salesforce, HubSpot, Twilio, Stripe) nutzen DPF als Transferinstrument? SCCs (Standardvertragsklauseln) + Transfer Impact Assessment (TIA) als Fallback vorbereiten. Sub-Processor-Datenverarbeitungsverträge prüfen. DPO briefen. **Noch keine sofortige Handlungspflicht** (DPF gilt formal), aber Rechtsrisiko ist erheblich gestiegen — EC kann jederzeit unter politischem Druck reagieren. **Modul:** DSGVO / Legal / Infra / Sub-Processor. `#akut`

---

### EDPB — EDPB + AMLA entwickeln Joint Guidelines zu Information-Sharing-Partnerships *(1. Juli 2026)*

[EDPB and AMLA to develop Joint Guidelines on partnerships for information sharing](https://www.edpb.europa.eu/news/edpb-and-amla-to-develop-joint-guidelines-on-partnerships-for-information-sharing_en) — EDPB, 1. Juli 2026

EDPB und die neue EU-Behörde für Geldwäschebekämpfung (Anti-Money Laundering Authority, AMLA) haben eine Zusammenarbeit zur Entwicklung von gemeinsamen Leitlinien für "information sharing partnerships" angekündigt. Ziel: Klärung des Spannungsfelds zwischen DSGVO-konformem Datenschutz und AML-Meldepflichten bei grenzüberschreitenden Finanzdaten.

*Cosmi-Implikation:* Direkt relevant für CRM-Module mit Financial-Scoring, KYC/AML-Features oder Integration in Buchhaltungsprozesse. Joint Guidelines könnten neue Anforderungen an Datenweitergabe an Finanzaufsichtsbehörden stellen. **Modul:** DSGVO / Legal / CRM / Buchhaltung. `#beobachten`

---

### EDPB — Anonymisierungs-Guidelines: Sprint-Team, Fertigstellung Sommer 2026 *(Carry-over)*

[EDPB Anonymisation Sprint Team](https://www.edpb.europa.eu/news/news/2026/edpb-brings-clarity-data-processing-scientific-research-speeds-finalisation_en) — EDPB

EDPB hat ein dediziertes "Sprint Team" gebildet, um die lang erwarteten Anonymisierungs-Guidelines abzuschließen. Zeitplan: Sommer 2026 — d. h. nächste Wochen. Nach Publikation: verbindlicher Rahmen für alle EU-Anonymisierungsansätze.

*Cosmi-Implikation:* Veröffentlichung unmittelbar bevorstehend. Cosmi-Anonymisierungsroutinen (Reporting, Analytics, Churn-Modelle) nach Publikation gegen neue Standards prüfen. **Modul:** DSGVO / Legal / Product. `#followup`

---

### EDPB — Data Breach Notification Template: Konsultation bis 5. August 2026 *(10. Juni Plenum)*

[EDPB Data Breach Notification Template](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en) — EDPB, Konsultation offen

EDPB hat auf dem 10.-Juni-Plenum ein harmonisiertes Data-Breach-Notification-Template verabschiedet. Öffentliche Konsultation läuft bis **5. August 2026**. Nach Finalisierung: dieses Template wird Grundlage für alle Meldungen an Datenschutzbehörden — Cross-Border-Meldungen einfacher.

*Cosmi-Implikation:* Template herunterladen, Incident-Response-SOP gegen neues Format validieren. Konsultation bis 05.08 — Feedback einreichen falls sinnvoll. **Modul:** DSGVO / Security / Legal. `#followup`

---

## AI Act

### 🟢 AI Omnibus: EU-Rat stimmt am 29. Juni zu — neue Fristen ab OJ-Publikation *(KW26/27)*

[EU Council gives final green light — Consilium (29. Juni 2026)](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/) | [Gibson Dunn Analyse](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) | [ComplianceHub Wiki](https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/)

Trilateralverfahren abgeschlossen. Neue Fristen:

| Pflicht | Bisherige Frist | Neue Frist (nach OJ) |
|---------|----------------|----------------------|
| **Annex III Standalone Hochrisiko-KI** (Recruiting, Kreditscoring, Strafverfolgung, Bildung) | ~~02.08.2026~~ | **02.12.2027** (+16 Mon.) |
| **Annex I Hochrisiko in regulierten Produkten** (Medizinprodukte, Maschinen, KFZ) | ~~02.08.2027~~ | **02.08.2028** (+12 Mon.) |
| **GPAI-Pflichten** | 02.08.2025 | **unverändert** (bereits in Kraft) |
| **Art. 50 Transparenz** (Offenlegung bei KI-Interaktion, Chatbot-Pflicht) | 02.08.2026 | **unverändert — KEIN Aufschub!** |
| **Art. 50(2) Wasserzeichen** | 02.08.2026 | Übergangsfrist bis **02.12.2026** für Systeme, die vor 02.08 auf dem Markt waren |
| **Neue Verbote: Nudifier / CSAM** | — | Übergangszeit bis **02.12.2026** |

**OJ-Status:** Rat hat am 29. Juni zugestimmt. Tritt in Kraft 3 Tage nach OJ-Publikation. OJ-Eintrag erwartet vor 02.08.2026. Bis zur OJ-Publikation gelten **rechtlich die alten Fristen**.

*Cosmi-Implikation:*
- **Art. 50 Transparenz bleibt 02.08.2026** — prüfen, ob der Cosmi-Chatbot korrekt als KI-System offengelegt wird (Hinweispflicht an Nutzer). Das ist **nicht verschoben**.
- **Annex-III-Assessment** (Lead-Scoring, Churn-Prediction, Chatbot) → interne Dokumentation weiterhin bis Juli abschließen, dann offiziell auf 02.12.2027 umdatieren sobald OJ erschienen ist.
- **Compliance-Roadmap** kann intern vorbereitet werden — erst nach OJ-Datum (kommt kurzfristig) auf neue Fristen umschalten.
- **Modul:** AI Act / Legal / Product. `#akut`

---

## NIS2

### 🔴 NIS2 BSI-Registrierung: Nachfrist läuft ab — **31. Juli 2026** *(KW27 AKUT)*

[NIS2 Nachfrist BSI 31. Juli](https://locaterisk.com/en/nis2-bsi-registrierung-frist-2026/) | [IT-Daily](https://www.it-daily.net/shortnews/bsi-nis2-registrierung-bis-ende-juli) | [IHK Essen](https://www.ihk.de/meo/innovation1/aktuelles4/bsi-nis2-registrierung-7093952)

Von ca. **29.500 betroffenen Unternehmen** haben erst ~**11.500 registriert** (Stand: Anfang Juli). BSI-Präsidentin Claudia Plattner hatte die ursprüngliche Frist (6. März 2026) auf den **31. Juli 2026** verlängert. Diese Nachfrist läuft in **27 Tagen** ab.

**Konsequenzen bei Nichtregistrierung:**
- Bußgeld bis **€500.000** (§ 60 BSIG)
- **Persönliche Haftung** der Geschäftsführung (§38 BSIG)
- Registrierung via [portal.bsi.bund.de](https://portal.bsi.bund.de)

*Cosmi-Implikation:* Falls Cosmi als **IT-Dienstleister / Anbieter digitaler Infrastruktur** unter NIS2 fällt (§28 BSIG — "Anbieter von Managed IT-Diensten" oder "Anbieter von Cloud-Computing-Diensten" oder "Anbieter von Online-Marktplätzen/Suchmaschinen/sozialen Netzwerken"): BSI-Registrierung bis **31. Juli 2026** sicherstellen. Nichtregistrierung ist Bußgeldrisikotatbestand — kein Interpretationsspielraum. **Modul:** NIS2 / Legal / Management. `#akut`

---

## XRechnung / e-Rechnung / GoBD

### Fristen unverändert — keine neuen Regelungen KW27

Fristen-Status (unverändert seit KW19):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) — bereits Pflicht |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz >800.000 € Vorjahresumsatz |
| ab 01.01.2028 | **Versandpflicht** alle B2B (inkl. KMU) |

Hinweis: YouGov-Studie (KW26): 74 % der deutschen Unternehmen unvorbereitet → GTM-Fenster weiterhin offen.

---

## ArbZG / Arbeitsrecht

### Mindestlohn-Anpassungen: 1. Juli 2026 in Kraft *(KW27 NEU)*

[Mindestlohn Pflege Juli 2026](https://www.informationsportal.de/hkk/der-mindestlohn-in-der-pflege-steigt-zum-1-juli-2026/) | [Mindestlohn Haufe](https://www.haufe.de/personal/arbeitsrecht/aktueller-mindestlohn_76_456370.html)

Seit **1. Juli 2026** gelten neue Arbeitsrechtsregelungen:

| Änderung | Details |
|----------|---------|
| **Minijob RV-Pflicht** | Befreiungsmöglichkeit von der Rentenversicherung entfällt — alle Minijobber automatisch RV-pflichtig |
| **Gesetzl. Mindestlohn** | €13,90/h (seit 01.01.2026) — unverändert; nächste Erhöhung: €14,60/h ab 01.01.2027 |
| **Mindestlohn Pflege (einfach)** | €16,52/h (ab 01.07.2026) |
| **Mindestlohn Pflege (qualifiziert)** | €17,80/h (ab 01.07.2026) |
| **Mindestlohn Pflegefachkräfte** | €21,03/h (ab 01.07.2026) |
| **ArbZG-Reform** | politisch diskutiert, stand Juli 2026 nicht beschlossen |

*Cosmi-Implikation:* Falls Cosmi Schichtplanung/Zeiterfassungs-Module (Personalmodul) anbietet oder intern Minijobber beschäftigt: Lohnbuchhaltungs-Logik und Payroll-Sub-Processor-Einstellungen auf neue Sätze prüfen. Minijob RV-Änderung kann Abrechnungsfehler auslösen wenn nicht angepasst. **Modul:** ArbZG / Schichten / Produkt / Buchhaltung. `#followup`

---

## eIDAS

### EUDIW: Deutschland offiziell ab 2. Januar 2027 — Ökosystem finalisiert *(KW27)*

[BMDS EUDI Wallet](https://bmds.bund.de/themen/digitaler-staat/digitale-identitaeten/eudi-wallet) | [EC EUDI Wallet Home](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/694487738/EU+Digital+Identity+Wallet+Home)

Das Bundesministerium für Digitalisierung und staatliche Modernisierung hat bestätigt: Deutschland startet die EUDI Wallet offiziell am **2. Januar 2027**. Alle 27 EU-Mitgliedstaaten haben Ende 2026 als gesetzliche Frist (eIDAS 2.0, Verordnung EU 2024/1183). Large Scale Pilots aktiv. Aussteller, Wallet-Anbieter und Relying Parties finalisieren Implementierungen.

*Cosmi-Implikation:* Deutschland-Frist: 02.01.2027. Vertragsmodul (eSignatur-Integration, Relying-Party-Anbindung) Sprint 6+ — Planung auf Q1/Q2 2027 ausrichten. Technische Implementing Regulations für Trust Services seit KW26 verfügbar. **Modul:** eIDAS / Verträge / Auth. `#beobachten`

---

## BSI-Warnings — KW27 (28. Juni – 4. Juli 2026)

### 🔴 KRITISCH — Sofortiger Handlungsbedarf

| Advisory | Produkt | Angriffsvektor | Datum |
|----------|---------|----------------|-------|
| [WID-SEC-2026-0098](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0098) | **Node.js** | Remote: RCE + Privilege Escalation (mehrere CVEs) | 2. Jul (NEU, KRITISCH) |
| [WID-SEC-2026-2155](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2155) | **Adobe ColdFusion** | Remote, anonym: Beliebige Code-Ausführung | 3. Jul (NEU, KRITISCH) |

> **🚨 Node.js WID-SEC-2026-0098 (KRITISCH, 2. Jul):** Mehrere Schwachstellen ermöglichen RCE und Privilege Escalation durch Remote-Angreifer. Node.js wird für Backend-Services, API-Gateways und Build-Tooling verwendet. **Sofort auf aktuelle LTS-Version aktualisieren.** Betrifft auch node-basierte CLI-Tools (npm-dependencies prüfen).
>
> **🚨 Adobe ColdFusion WID-SEC-2026-2155 (KRITISCH, 3. Jul):** Unauthentifizierter Remote-Angreifer kann beliebigen Code ausführen. Falls ColdFusion in der Cosmi-Infrastruktur oder bei Kunden-Hosting relevant: sofort patchen oder isolieren. (Wahrscheinlichkeit gering bei modernem SaaS-Stack — prüfen.)

---

### 🟠 HOCH — Cosmi-relevante Infrastruktur

| Advisory | Produkt | Datum | Angriffsvektor |
|----------|---------|-------|---------------|
| [WID-SEC-2026-1433](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1433) | **PHP** | 3. Jul (NEU) | Remote: Code-Ausführung |
| [WID-SEC-2026-1852](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1852) | **OpenSSL** | 3. Jul (Update) | Remote/Lokal: Mehrere Schwachstellen (Carry-over) |
| [WID-SEC-2026-0873](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0873) | **Docker** | 3. Jul (Update) | Local: Security Bypass, Info Disclosure |
| [WID-SEC-2026-1346](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1346) | **Linux Kernel** | 3. Jul (Update) | Privilege Escalation, DoS, Code Execution |
| [WID-SEC-2026-1279](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1279) | **Linux Kernel** | 3. Jul (Update) | Mehrere Schwachstellen (Carry-over) |
| [WID-SEC-2026-2077](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2077) | **Linux Kernel** | 3. Jul (Update) | Mehrere Schwachstellen (Carry-over) |
| [WID-SEC-2026-1468](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1468) | **dnsmasq** | 3. Jul (NEU) | Remote: DoS |

> **PHP WID-SEC-2026-1433 (NEU, HOCH):** Mehrere Schwachstellen für Code-Ausführung. Falls PHP in Backend oder Hosting eingesetzt wird → aktualisieren.
>
> **OpenSSL/Docker/Linux-Kernel (Updates):** Dritte Aktualisierungswelle in Folge. Patch-Rückstand bei diesen Paketen erhöht kumulatives Risiko.

---

### MITTEL — Monitoring

| Advisory | Produkt | Datum |
|----------|---------|-------|
| [WID-SEC-2026-2052](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2052) | **cURL** | 3. Jul |
| [WID-SEC-2026-2065](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2065) | **cURL** | 3. Jul |
| [WID-SEC-2026-1437](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1437) | **Golang** | 3. Jul |
| [WID-SEC-2026-1653](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1653) | **Golang** | 3. Jul |

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (12. Woche). AI-Omnibus OJ-Eintrag: noch nicht publiziert (Rat stimmte 29. Juni zu; OJ-Eintrag steht aus).
- **BfDI Pressemitteilungen** — RSS 404 (11. Woche).
- **BSI Pressemitteilungen** — RSS 404 (11. Woche). BSI-Content nur via Warnungs-Feed.
- **e-Rechnung Bund (BMWK)** — RSS 404 (12. Woche). Keine neuen XRechnung-Regelungen.
- **BMAS (Arbeitsrecht)** — RSS 404 (12. Woche). ArbZG-Reform weiter in politischer Diskussion — kein Parlamentsbeschluss.
- **ENISA** — RSS 404 (9. Woche). Keine neuen NIS2-Leitlinien.
- **EDPB** — Feed 403 Forbidden. Neuste Meldung: 01.07.2026 (EDPB + AMLA Joint Guidelines). Inhalte via WebFetch rekonstruiert.
- **EDPS** — 403 Forbidden. Keine neuen Meldungen KW27.
- **noyb** — 1 neuer Artikel (29. Juni, DPF-Krise). Kein weiterer Post nach dem 29. Juni.

> **Wartungshinweis (Woche 12):** 6 von 10 Quellen 404 + 2 von 10 zusätzlich 403. Prio-Empfehlung: EDPB Direct-Scraping > BMAS-Alternative > BMWK/e-Rechnung-Alternative > ENISA-Alternative > EUR-Lex-OJ-Watcher. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — diese Woche / bis 31. Juli

- [ ] **DPF-Audit: US-SaaS-Abhängigkeiten inventarisieren** — Welche Services nutzen DPF als Transferrechtsgrundlage? (AWS, Google, Stripe, HubSpot, Twilio etc.) SCCs + TIA als Fallback vorbereiten. DPO briefen. noyb-Brief vom 30. Juni zeigt: politischer Druck auf EC steigt. `#dsgvo #legal #infra #sub-processor` → **diese Woche**
- [ ] **NIS2 BSI-Registrierung prüfen** — Frist **31. Juli 2026** (27 Tage). Falls Cosmi als IT-/Cloud-Dienstleister NIS2-pflichtig: Registrierung via portal.bsi.bund.de sicherstellen. Bußgeld bis €500k, persönliche GF-Haftung. `#nis2 #legal #management` → **bis 25. Juli (Puffer)**
- [ ] **AI Act Art. 50 Transparenz ab 02.08.2026 — NICHT VERSCHOBEN** — Chatbot-Offenlegung prüfen: Werden Nutzer klar informiert, dass sie mit einem KI-System interagieren? Pflicht gilt ab 02.08.2026 unverändert. `#aiact #legal #product` → **bis 31. Juli**
- [ ] **Node.js auf aktuelle LTS-Version aktualisieren** — WID-SEC-2026-0098 (KRITISCH, RCE + Privilege Escalation, 2. Jul NEU). Backend-Services, API-Gateways, Build-Tools. `#security #infra` → **sofort**
- [ ] **AI-Act Hochrisiko-Assessment fertigstellen** — Konsultationsfrist High-Risk-Klassifikation: **23. Juli 2026** (19 Tage). Lead-Scoring, Chatbot, Churn-Prediction gegen Anhang III schriftlich bewerten. `#aiact #legal #product` → **bis 15. Juli (Puffer)**

### 🟡 Followup (KW28+)

- [ ] **AI Omnibus OJ-Eintrag überwachen** — Rat stimmte 29. Juni zu. OJ-Publikation erwartet vor 02.08.2026. Sobald OJ: Compliance-Roadmap auf Annex-III-Standalone = 02.12.2027 finalisieren. `#aiact #legal`
- [ ] **Minijob RV-Pflicht prüfen** — Ab 01.07.2026 keine Befreiungsmöglichkeit mehr. Falls Cosmi intern Minijobber beschäftigt oder HR-Modul betrifft: Abrechnungslogik prüfen. `#arbzg #hr #produkt`
- [ ] **EDPB Anonymisierungs-Guidelines** — Sprint-Team → Sommer 2026. Sobald publiziert: Cosmi-Anonymisierungsroutinen validieren. `#dsgvo #legal #infra`
- [ ] **EDPB Data Breach Notification Template** — Konsultation bis 05.08.2026. Template herunterladen, Incident-Response-SOP aktualisieren. `#dsgvo #security`
- [ ] **EDPB AMLA Joint Guidelines** — Beobachten: Implikationen für CRM-KYC/AML-Features und Datenweitergabe-Prozesse. `#dsgvo #crm`
- [ ] **PHP + Docker + OpenSSL + Linux Kernel** — KW27-Updates einspielen (kontinuierlich). `#security #infra`
- [ ] **EUDIW Relying-Party-Vorbereitung** — Deutschland-Launch 02.01.2027. Vertragsmodul eSignatur-Integration auf Sprint 6+ datieren. Technische Specs (Implementing Regulations) jetzt verfügbar. `#eidas #product`
- [ ] **NIS2 Incident-Reporting-Templates** — In Incident-Response-SOP einarbeiten. `#nis2 #security`
- [ ] **`sources/_regulation.yaml` Pflege** — 6×404 + 2×403 (Woche 12). EDPB Direct-Scraping, BMAS-Alternativ-URL recherchieren. `#maintenance`
- [ ] **e-Rechnung GTM-Kampagne Q3** — YouGov-Studie (74 % unvorbereitet) weiterhin aktuell. Versandpflicht für >€800k in 6 Monaten. `#gtm #e-rechnung`
