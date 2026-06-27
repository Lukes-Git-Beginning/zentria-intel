---
date: 2026-06-27
type: regulation
runtime_minutes: 18
items_scanned: 55
items_relevant: 19
sources_live_rss: 1
sources_403: 2
sources_404: 6
sources_live_list: [bsi-warnungen]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 8
kw: 26
---

# Regulation-Sweep KW26/2026 (Sa 27. Juni)

> **KW26-Scope:** 21.–27. Juni 2026. Referenz-Sweep: KW25 (20. Juni). Neue BSI-Items: ~35 (KRITISCH/HOCH/MITTEL). WebSearch-Supplements: 8 Policy-Updates.
>
> **🔴 LITELLM CVE-2026-42271 AKTIV AUSGENUTZT (CISA KEV):** Command Injection → unauthentifizierter RCE. Sofort auf v1.83.7+ patchen falls LiteLLM im KI-Stack.
>
> **🔴 FLOWISE CVE-2026-40933 — 1-Click RCE:** Manipulierter Chatflow-Import kompromittiert Server vollständig. Sofort patchen falls Flowise im Workflow-Stack.
>
> **🟡 AI OMNIBUS — RATSFORMALABSTIMMUNG NOCH AUSSTEHEND:** Europaparlament hat am 16. Juni zugestimmt. EU-Rat erwartet für Juli 2026. Bis OJ-Publikation gilt rechtlich weiterhin 02.08.2026.
>
> **🟡 NOYB — TIKTOK/GRINDR/APPSFLYER:** Drittanbieter-Tracking sensibler Daten (sexuelle Orientierung) per App-SDK — direkte Analogie für CRM-Marketing-Pixel-Integrationen.
>
> **🟡 COOKIE-BANNER BLEIBEN:** EU-Mitgliedstaaten + Google blockieren vorgeschlagene Abschaffung im Digital Omnibus. Cookie-Audit nicht aufschieben.

---

## DSGVO / Datenschutz

### noyb — TikTok / Grindr / AppsFlyer: Tracking sensibler Daten via Drittanbieter-SDK *(KW26 NEU)*

[TikTok unlawfully tracks your shopping habits – and your use of dating apps](https://noyb.eu/en/tiktok-unlawfully-tracks-your-shopping-habits-and-your-use-dating-apps) — noyb, Beschwerde bei österreichischer DSB

noyb hat Beschwerden gegen TikTok, Grindr und den israelischen Datenbroker AppsFlyer eingereicht. Kernvorwurf: TikTok hat via AppsFlyer (Marketing-SDK, in Grindr eingebettet) die Grindr-Nutzungsaktivität eines Users getrackt — ohne Wissen des Nutzers, ohne Rechtsgrundlage. Die Daten umfassen: genutzte Apps, In-App-Aktionen (z. B. Warenkorb-Hinzufügung), und damit indirekt die sexuelle Orientierung des Nutzers (Art. 9 Abs. 1 DSGVO). TikTok gestand erst nach mehrfacher Nachfrage, diese Daten zu besitzen. Zudem funktionierte das DSGVO-Auskunfts-Download-Tool nicht vollständig — nur "relevante" Daten wurden ausgegeben.

*Cosmi-Implikation:* **Direkte Analogie für CRM-App-Integrationen mit Third-Party-Tracking.** Falls Cosmi Meta Pixel, TikTok-SDK, Google Analytics 4 oder ähnliche Marketing-SDKs auf der App-Oberfläche oder in eingebetteten Tools nutzt: Diese Anbieter können via SDK-Kontext branchenspezifische oder verhaltensbezogene Daten ableiten, die als "besondere Kategorien" klassifiziert werden könnten. Tracking-SDK-Inventar prüfen — Rechtsgrundlage, Zweckbindung, Sub-Processor-Meldung. **Modul:** DSGVO / Legal / Product / Sub-Processor. `#akut`

---

### noyb — EU-Mitgliedstaaten + Google: Cookie-Banners sollen bleiben *(23. Juni 2026)*

[EU Member States and Google suddenly want to keep cookie banners](https://noyb.eu/en/eu-member-states-and-google-suddenly-want-keep-cookie-banners) — noyb, 23. Juni 2026

Die EU-Kommission hatte im Digital Omnibus vorgeschlagen, Cookie-Consent-Dialoge weitgehend abzuschaffen (Opt-out statt Opt-in für nicht-sensible Cookies). Mehrere EU-Mitgliedstaaten sowie Google setzen sich jetzt aktiv gegen diesen Vorschlag ein. noyb kritisiert, dass Google Cookie-Banners braucht, um das TCF (Transparency & Consent Framework) zur Legitimation massiver Datenverarbeitung zu betreiben. Das Resultat: Cookie-Banner-Pflicht wird im finalen Digital Omnibus wahrscheinlich abgeschwächt bestehen bleiben — nicht eliminiert.

*Cosmi-Implikation:* Cookie-Banners sind kein temporäres Problem, das sich "von selbst löst". Kein Abwarten auf Regulierungsvereinfachung. Das offene Cookie-Audit (Reject-Button-Äquivalenz, noyb/Schibsted-Analogie) jetzt angehen. **Modul:** DSGVO / Legal / Frontend. `#followup`

---

### EDPB — BCR Opinions 18/2026 & 19/2026: Rubrik Group (Controller + Processor) *(KW26)*

[EDPB Opinions Dokumente](https://www.edpb.europa.eu/our-work-tools/consistency-findings/opinions_en) — EDPB, Juni 2026

Der EDPB hat zwei Stellungnahmen zur niederländischen Aufsichtsbehörde herausgegeben: Opinion 18/2026 (Controller-BCR) und Opinion 19/2026 (Processor-BCR) der Rubrik Group. BCRs (Binding Corporate Rules) erlauben Drittstaaten-Datentransfers innerhalb eines Konzernverbunds ohne SCCs — vorausgesetzt, der EDPB genehmigt den Antrag.

*Cosmi-Implikation:* BCRs werden aktiv genehmigt. Für Sub-Processor-Kette (US-SaaS): Prüfen, welche bestehenden Anbieter BCRs halten — diese könnten SCCs als Übertragungsinstrument ersetzen. Ergänzt das Europäische Datenschutzsiegel (KW25) als zweiten alternativer SCC-Ersatz. **Modul:** DSGVO / Legal / Sub-Processor. `#beobachten`

---

### BfDI — Digital Omnibus greift bei Datenschutzfragen zu kurz *(Carry-over 08. Juni 2026)*

[BfDI Kurzmeldung: Digitaler Omnibus greift bei zentralen Datenschutzfragen zu kurz](https://www.bfdi.bund.de/SharedDocs/Kurzmeldungen/DE/2026/09_High_Level_Debatte-KM.html) — BfDI, 08. Juni 2026

Der BfDI kritisiert in einer High-Level-Debatte (gemeinsam mit EDPS und BayLfD, Bayerische Vertretung Brüssel) dass der Digital Omnibus strukturelle Machtungleichgewichte nicht adressiert, KMU-Interessen unzureichend berücksichtigt und Hersteller von digitalen Anwendungen zu wenig in datenschutzrechtliche Verantwortung nimmt. Eine substanzielle Vereinfachung des Datenschutzrechts für Unternehmen ist demnach nicht zu erwarten.

*Cosmi-Implikation:* Compliance-Planung nicht auf Entlastungen durch den Digital Omnibus setzen. DSGVO-Anforderungen bleiben in vollem Umfang bestehen. **Modul:** DSGVO / Legal. `#beobachten`

---

### EDPB — DPIA-Template Konsultation abgeschlossen (09. Juni) *(Carry-over KW25)*

[EDPB DPIA Template](https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2026/edpb-dpia-template_en) — EDPB, April–Juni 2026

Öffentliche Konsultation zum ersten harmonisierten EU-weiten DPIA-Template abgeschlossen (Frist 09. Juni 2026). Finalisierung steht aus. Nach Annahme wird dieses Template verbindliche Grundlage — alle nationalen DPIA-Templates müssen kompatibel sein.

*Cosmi-Implikation:* Sobald finales Template veröffentlicht: Bestehende Cosmi-DPIAs (Chatbot, Lead-Scoring, Churn-Prediction) gegen das neue Schema überprüfen und ggf. aktualisieren. **Modul:** DSGVO / Legal / Product. `#followup`

---

## AI Act

### 🟡 AI Omnibus — Ratsformalabstimmung erwartet Juli 2026

[EU Lawmakers Reach Provisional Agreement to Delay Key EU AI Act Obligations](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/) — Data Matters, 22. Juni 2026

Der EU-Rat hat das am 16. Juni 2026 vom Europaparlament (423:57) verabschiedete Digital Omnibus on AI noch **nicht formal angenommen**. Die Ratsformalabstimmung wird für Juli 2026 erwartet, mit OJ-Publikation danach — vermutlich noch vor dem 02.08.2026-Datum.

**Aktueller Rechtsstatus bis OJ-Publikation:**

| Obligation | Gilt rechtlich aktuell | Nach OJ (geplant) |
|-----------|------------------------|-------------------|
| Hochrisiko AI Annex III (Standalone) | 02.08.2026 | 02.12.2027 |
| Hochrisiko AI Annex I (regulierte Produkte) | 02.08.2026 | 02.08.2028 |
| GPAI / Verbotene Praktiken | unverändert | unverändert |

*Cosmi-Implikation:* **Weiterhin auf 02.08.2026 planen bis Ratsentscheidung offiziell.** Assessment-Dokumentation (Lead-Scoring, Chatbot, Churn-Prediction gegen Anhang III) intern abschließen. Konsultationsfrist High-Risk-Klassifikation: **23. Juli 2026** (noch ~26 Tage). Compliance-Roadmap formell erst nach OJ-Datum auf 02.12.2027 umstellen. **Modul:** AI Act / Legal / Product. `#akut`

---

## NIS2

### EU-weite Cyber-Übung (10.–11. Juni 2026) *(Carry-over KW25)*

[EU Council cybersecurity package review](https://industrialcyber.co/regulation-standards-and-compliance/eu-council-to-examine-cybersecurity-package-focused-on-enisa-nis2-simplification-and-supply-chain-security/) — Industrial Cyber

5.000 Experten aus EU-Mitgliedstaaten haben eine koordinierte Cyber-Übung auf Basis des EU Cyber Blueprint 2025 absolviert — erstes Aktivierungsdrill der EU Cybersecurity Reserve (Cyber Solidarity Act). Szenario: Koordinierte Cyberangriffe auf europäische Bahn- und Seeverkehrsnetze mit eskalierter Krisenwirkung.

*Cosmi-Implikation:* Demonstriert, dass EU-weite Incident-Response-Mechanismen jetzt aktiv exercised werden. Falls Cosmi NIS2-pflichtig: Incident-Response-Plan und Meldeketten testen. **Modul:** NIS2 / Security / Legal. `#beobachten`

### NIS2 Incident-Reporting-Templates verabschiedet *(KW26)*

Die NIS2-Kooperationsgruppe hat auf ihrer 39. Plenarsitzung in Zypern (Mai 2026) standardisierte Templates für Sicherheitsmeldungen verabschiedet. Einheitliches Format für alle Mitgliedstaaten — erleichtert Cross-Border-Meldungen.

*Cosmi-Implikation:* Falls Cosmi als IT-Dienstleister NIS2-pflichtig: Templates für Incident-Meldungen jetzt herunterladen und in Incident-Response-SOP einarbeiten. BSI-Portal Schritt-2-Registrierung (seit 01.06.2026 offen) weiterhin offen. **Modul:** NIS2 / Legal / Security. `#followup`

---

## XRechnung / e-Rechnung / GoBD

### YouGov/easybill-Studie: Nur 26 % der Unternehmen e-Rechnungs-bereit *(Juni 2026)*

[Nur jedes vierte deutsche Unternehmen ist bereit für die E-Rechnungspflicht ab 2027](https://www.easybill.de/ratgeber/studie-zur-e-rechnungspflicht/) — easybill, 02. Juni 2026

Repräsentative YouGov-Studie (im Auftrag von easybill): Weniger als 8 Monate vor der Versandpflicht für Unternehmen >800.000 € Vorjahresumsatz (01.01.2027):
- **Nur 26 %** der Unternehmen fühlen sich vollständig vorbereitet
- **Jedes dritte Unternehmen** hat noch **nie** eine E-Rechnung versendet
- Rund jedes fünfte Unternehmen nutzt noch manuelles Rechnungswesen

*Cosmi-Implikation:* **Enormes GTM-Fenster für Cosmi.** 74 % der deutschen Unternehmen sind unvorbereitet. Q3-Kampagne kann konkret auf Compliance-Dringlichkeit setzen: XRechnung-/ZUGFeRD-Empfang bereits Pflicht, Versand in 6 Monaten. Positionierung als "der einfachste Weg zur e-Rechnungs-Compliance" hat hohe Conversion-Relevanz. **Modul:** Buchhaltung / e-Rechnung / GTM. `#akut`

Fristen-Erinnerung (unverändert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz >800.000 € |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

---

## ArbZG / Arbeitsrecht

### Stille Bereiche *(Woche 11 ohne BMAS RSS)*

*BMAS-RSS weiterhin 404. Kein ArbZG-Content in KW26.*

---

## eIDAS

### Sieben neue Durchführungsverordnungen zu Trust Services verabschiedet *(KW26)*

[EU Digital Identity Wallet — Implementing Regulations](https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/694487738/EU+Digital+Identity+Wallet+Home) — EU-Kommission

Die EU-Kommission hat sieben neue Durchführungsverordnungen zu Trust Services (eSignaturen, Zertifikate, qualifizierte Vertrauensdienste) verabschiedet — konkretisiert die technischen Anforderungen für die EUDI Wallet-Implementierung. Wallet-Anbieter, Aussteller und Relying Parties testen aktiv Use Cases in Large Scale Pilots. Ende-2026-Frist für Mitgliedstaaten nähert sich (~26 Wochen).

*Cosmi-Implikation:* Technische Spezifikationen für Trust Services jetzt verfügbar — relevant für Vertragsmodul (eSignatur-Integration). Sprint 6+ Timeline vertretbar. EUDI Wallet Massenadoption bleibt Q1/Q2 2027. **Modul:** eIDAS / Verträge / Auth. `#beobachten`

---

## BSI-Warnings — KW26 (21.–27. Juni 2026)

### 🔴 KRITISCH — Sofortiger Handlungsbedarf

| Advisory | Produkt | CVE | Angriffsvektor | Datum |
|----------|---------|-----|---------------|-------|
| [WID-SEC-2026-1288](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1288) | **LiteLLM** | CVE-2026-42271 | Remote, unauthentifiziert — **AKTIV AUSGENUTZT (CISA KEV)** | 26. Jun (NEU) |
| [WID-SEC-2025-0568](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2025-0568) | **Flowise** | CVE-2026-40933 | Remote, 1-Click RCE via Chatflow-Import | 26. Jun (Update) |
| [WID-SEC-2025-2048](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2025-2048) | **Flowise** | Mehrere | Remote, Code Execution | 26. Jun (Update) |
| [WID-SEC-2026-2013](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2013) | **Gogs** | Mehrere | Remote, Code Execution | 25. Jun (NEU) |

> **🚨 LiteLLM CVE-2026-42271 (WID-SEC-2026-1288) — CISA KEV, AKTIV AUSGENUTZT:**
> Command Injection im Handling von Model-Namen/API-Parametern — unsanitized Input wird an System-Shell übergeben. Unauthentifizierter Remote-Angreifer kann OS-Commands mit LiteLLM-Service-Privilegien ausführen. **Fix: LiteLLM v1.83.7+** (zusätzliche Authorization-Controls: nur PROXY_ADMIN-Rolle für Test-Endpoints; Starlette-Dependencies aktualisiert). **Auch offen: CVE-2026-42208** (SQL Injection gegen Auth-Path, seit 09. Juni, Carry-over KW25 — [Sysdig-Blog](https://www.sysdig.com/blog/cve-2026-42208-targeted-sql-injection-against-litellms-authentication-path-discovered-36-hours-following-vulnerability-disclosure)). Falls Cosmi LiteLLM als KI-Gateway/Proxy einsetzt → sofort updaten, kein WIP.
>
> **🚨 Flowise CVE-2026-40933 (WID-SEC-2025-0568) — 1-Click RCE via Custom MCP stdio:**
> Der Import eines manipulierten Chatflows reicht aus, um Server-seitig beliebigen Code auszuführen (über `stdio`-Transport des Custom MCP Tools, das einen Child-Process ohne Sandboxing startet). Kein separates Exploit-Schritt nötig — Import allein triggert RCE. Falls Cosmi Flowise für LLM-Workflow-Automation nutzt → sofort patchen.

---

### 🟠 HOCH — Cosmi-relevante Infrastruktur

| Advisory | Produkt | Severity | Datum | Angriffsvektor |
|----------|---------|----------|-------|---------------|
| [WID-SEC-2026-1544](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1544) | **PostgreSQL** | HOCH | 26. Jun (Update) | Remote: SQL Injection, Code Execution, Info Disclosure (CVSS 8.8) |
| [WID-SEC-2026-0409](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0409) | **PostgreSQL** | HOCH | 26. Jun (Update) | Remote: Mehrere Schwachstellen |
| [WID-SEC-2025-0372](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2025-0372) | **PostgreSQL** | HOCH | 26. Jun (Update) | Remote: SQL Injection und Code Execution |
| [WID-SEC-2026-2004](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2004) | **Node.js** | HOCH | 26. Jun (**NEU**) | Remote: Mehrere Schwachstellen |
| [WID-SEC-2026-1852](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1852) | **OpenSSL** | HOCH | 25. Jun (Update) | Remote/Lokal: Mehrere Schwachstellen |
| [WID-SEC-2026-2077](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2077) | **Linux Kernel** | HOCH | 26. Jun (NEU) | Remote/Lokal: Mehrere Schwachstellen |
| [WID-SEC-2026-0873](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0873) | **Docker** | HOCH | 26. Jun (Update) | Remote: Mehrere Schwachstellen |
| [WID-SEC-2026-1527](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1527) | **NGINX** | HOCH | 26. Jun (Update) | Remote: Mehrere Schwachstellen (Carry-over) |
| [WID-SEC-2026-1824](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1824) | **Apache HTTP** | HOCH | 25. Jun (Update) | Remote: Mehrere Schwachstellen (Carry-over) |

> **PostgreSQL — dreifach aktualisiert (26. Jun):** Alle drei Advisories wurden erneut aktualisiert. CVSS 8.8 auf WID-SEC-2026-1544. DB-Hosts sofort auf aktuelles Minor-Release bringen.
>
> **Node.js WID-SEC-2026-2004 (NEU 26. Jun):** Erstes Node.js-Advisory dieser KW-Welle. Falls Cosmi Node.js für Backend-Services, API-Gateway oder Tooling nutzt → prüfen und patchen.
>
> **Docker WID-SEC-2026-0873 (aktualisiert 26. Jun):** Betrifft Docker-Daemon. Container-Infrastruktur prüfen — insbesondere Builds über CI/CD.

---

### MITTEL — Monitoring

| Advisory | Produkt | Datum |
|----------|---------|-------|
| [WID-SEC-2026-1971](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1971) | **CPython** (Python) | 26. Jun |
| [WID-SEC-2026-1454](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1454) | **Linux Kernel** | 26. Jun |

---

## Stille Bereiche

- **EUR-Lex** — RSS-Feed weiterhin 404 (11. Woche). AI-Omnibus OJ-Eintrag: noch nicht publiziert.
- **BfDI Pressemitteilungen** — RSS 404 (10. Woche). Content via bfdi.bund.de direkt.
- **BSI Pressemitteilungen** — RSS 404 (10. Woche). BSI-Content nur via Warnungs-Feed.
- **e-Rechnung Bund (BMWK)** — RSS 404 (11. Woche).
- **BMAS (Arbeitsrecht)** — RSS 404 (11. Woche).
- **ENISA** — RSS 404 (seit KW19 = 8. Woche).
- **EDPB** — Feed weiterhin 403 Forbidden. Inhalte via WebSearch rekonstruiert.
- **EDPS** — 403 Forbidden. Letzter bekannter Artikel: 22. Mai 2026.
- **noyb** — Letzter neuer Artikel: 23. Juni 2026 (Cookie-Banner EU-Widerstand). Kein weiterer Post KW26 nach 23. Juni.

> **Wartungshinweis (Woche 11):** 6 von 10 Quellen 404 + 2 von 10 zusätzlich 403. Quellen-Upgrade bleibt dringend. Prio: EDPB > BMAS > BMWK/e-Rechnung > ENISA > BfDI. Direkt-Scraping der Newsseiten oder alternative Feed-Endpunkte recherchieren.

---

## Cosmi-Action-Items

### 🔴 Akut — diese Woche

- [ ] **LiteLLM auf v1.83.7+ updaten** — CVE-2026-42271 (CISA KEV, AKTIV AUSGENUTZT, Remote RCE unauthentifiziert) + CVE-2026-42208 (SQL Injection Auth-Bypass). Falls LiteLLM als KI-Gateway/Proxy im Einsatz. `#security #infra #ai` → **sofort**
- [ ] **Flowise patchen** — CVE-2026-40933 (1-Click RCE via Chatflow-Import, kein Sandbox). Falls Flowise für Workflow-Automation genutzt. `#security #infra #ai` → **sofort**
- [ ] **PostgreSQL auf aktuelles Minor-Release** — 3× Advisory-Updates am 26. Jun, CVSS 8.8. DB-Hosts patchen. `#security #db #infra` → **diese Woche**
- [ ] **Node.js aktualisieren** — WID-SEC-2026-2004 (NEU, HOCH). Backend-Services und Tooling prüfen. `#security #infra` → **diese Woche**
- [ ] **AI-Act Hochrisiko-Assessment abschließen** — Konsultationsfrist **23. Juli 2026** (~26 Tage). Lead-Scoring, Chatbot, Churn-Prediction gegen Anhang III bewerten. Schriftlich dokumentieren. `#aiact #legal #product` → **bis 15. Juli (Puffer)**
- [ ] **Tracking-SDK-Inventar auditieren** (noyb/TikTok-Grindr-Analogie) — Welche Third-Party-Marketing-SDKs oder Pixel sind auf Cosmi-App/Frontend aktiv? Rechtsgrundlage, Zweckbindung, Sub-Processor-Einträge prüfen. `#dsgvo #legal #product #sub-processor` → **bis 04. Juli**
- [ ] **e-Rechnung GTM-Kampagne Q3 beschleunigen** — YouGov-Studie: 74 % unvorbereitet. Versandpflicht für große Unternehmen in 6 Monaten. Hohe Conversion-Relevanz. `#gtm #e-rechnung` → **Q3-Planung**

### 🟡 Followup (KW27+)

- [ ] **AI Omnibus OJ-Eintrag überwachen** — Ratsformalabstimmung Juli 2026. Sobald OJ: Compliance-Roadmap auf Annex-III-Standalone = 02.12.2027 finalisieren. `#aiact #legal`
- [ ] **Docker + NGINX + Apache + OpenSSL + Linux Kernel** — KW26-Updates einspielen. `#security #infra`
- [ ] **Cookie-Banner-Audit abschließen** — EU-Mitgliedstaaten blockieren Abschaffung; Cookie-Banners bleiben. Reject-Button visuell äquivalent zu Accept? `#dsgvo #frontend`
- [ ] **EDPB DPIA-Template** — nach Finalisierung: Cosmi-DPIAs (Chatbot, Lead-Scoring, Churn) gegen neues Schema validieren. `#dsgvo #legal`
- [ ] **EDPB BCR-Monitoring** — Sub-Processor-Inventar auf BCR-Inhaber prüfen (Alternative zu SCCs). Ergänzt Europäisches Datenschutzsiegel (KW25). `#dsgvo #sub-processor`
- [ ] **EDPB Anonymisierungs-Guidelines** — kommen bis Sommer 2026. Cosmi's Anonymisierungsroutinen nach Publikation validieren. `#dsgvo #legal #infra`
- [ ] **NIS2 BSI-Portal Schritt-2-Registrierung** — ab 01.06.2026 offen. Falls Cosmi als IT-Dienstleister NIS2-pflichtig. `#nis2 #legal`
- [ ] **NIS2 Incident-Reporting-Templates** — herunterladen und in Incident-Response-SOP einarbeiten. `#nis2 #security`
- [ ] **eIDAS-Integration Sprint 6+** — Implementing Regulations verabschiedet. Technische Spec jetzt verfügbar. `#eidas #product`
- [ ] **`sources/_regulation.yaml` Pflege** — 6×404 + 2×403. Neue Feed-URLs: EDPB, BMAS, BMWK/e-Rechnung, ENISA, BfDI. `#maintenance`
- [ ] **Art.-15-Auskunfts-Prozess validieren** — DSGVO-Auskunftsanfragen kostenlos und ohne Feature-Lock? `#dsgvo #legal #product`
- [ ] **BfDI Tätigkeitsbericht 2025 lesen** (Carry-over KW22). `#dsgvo`
