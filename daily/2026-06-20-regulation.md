---
date: 2026-06-20
type: regulation
runtime_minutes: 19
items_scanned: 47
items_relevant: 14
sources_live_rss: 1
sources_403: 3
sources_404: 6
sources_live_list: [bsi-warnungen]
sources_403_list: [edpb-newsroom, oedp-eaid, edpb-website]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
kw: 25
---

# Regulation-Sweep KW25/2026 (Sa 20. Juni)

> **KW25-Scope:** 14.–20. Juni 2026. Referenz-Sweep: KW24 (13. Juni). Neue RSS-Items: 11 BSI. WebSearch-Supplements: 3 Policy-Updates, 2 noyb-Items.
>
> **🔴 NGINX CVE-2026-42945 AKTIV AUSGENUTZT:** Sofortiger Patch-Bedarf auf API-Gateway, Reverse Proxy.
>
> **🟡 AI OMNIBUS EP-VOTE 16. JUNI:** Europaparlament hat 423:57 zugestimmt — nur noch Ratsformalabstimmung ausstehend. Compliance-Planung kann jetzt auf neue Fristen ausgerichtet werden.
>
> **✅ FRIST-ENTSCHÄRFUNG:** AI-Act Hochrisiko-Konsultation bis **23. Juli 2026** verlängert (war 23. Juni). 33 Tage mehr Zeit.

---

## DSGVO / Datenschutz

### EDPB 120. Plenum — 08.–09. Juni 2026 *(via WebSearch — Feed weiterhin 403)*

Das 120. Plenum des EDPB hat nach den verfügbaren Suchquellen drei wesentliche Ergebnisse produziert:

**1. Klarheit bei Datenverarbeitung zu wissenschaftlichen Forschungszwecken**
Der EDPB hat neue Guidance zur Verarbeitung personenbezogener Daten für wissenschaftliche Forschung verabschiedet (Art. 89 DSGVO). Präzisierungen zu: Archivierungszwecken, kompatible Weiterverarbeitung, Pseudonymisierungsanforderungen.

*Cosmi-Implikation:* Wenn Cosmi Nutzungsdaten für Produkt-Analytics, A/B-Tests oder ML-Training nutzt, kann ein "Forschungs"-Frame nach Art. 89 DSGVO strukturiert werden — aber nur mit robuster Pseudonymisierung und klarer Zweckbindung. Nicht als Freifahrtschein verwenden. **Modul:** DSGVO / Legal / Analytics. `#beobachten`

**2. Anonymisierungs-Guidelines — Beschleunigt durch Sprint-Team**
Der EDPB hat ein dediziertes Sprint-Team gebildet, das die lang erwarteten finalen [Anonymisierungs-Guidelines](https://www.edpb.europa.eu/our-work-tools/our-documents_en) bis **Sommer 2026** abschließen soll. Der Zeitplan wurde konkret beschleunigt (nach ursprünglich Jahren der Arbeit).

*Cosmi-Implikation:* Sobald die Guidelines finalisiert sind, definieren sie verbindlich, wann Testdaten, Audit-Logs, Export-Dumps als "anonym" gelten. Cosmi's Datenlösch-/Anonymisierungsroutinen im Backend sollten nach Publikation gegen diese Standards validiert werden. **Modul:** DSGVO / Legal / Infra. `#followup`

**3. Erstes Europäisches Datenschutzsiegel genehmigt**
Der EDPB hat das erste "European Data Protection Seal" als Übertragungsinstrument nach Art. 46 DSGVO genehmigt. Dieses ermöglicht Drittstaaten-Datentransfers ohne SCCs, sofern der Empfänger das Siegel trägt.

*Cosmi-Implikation:* Relevant für Sub-Processor-Kette — wenn Cosmi US-SaaS-Tools (CRM-Integration, Email-Infrastruktur) nutzt, könnten Anbieter mit diesem Siegel zukünftig SCCs ersetzen. Auf Verfügbarkeit für bestehende Sub-Processors prüfen. **Modul:** DSGVO / Legal / Sub-Processor. `#beobachten`

---

### noyb — LinkedIn Art. 15 DSGVO: Betroffenenrechte hinter Paywall

[LinkedIn locks your GDPR rights behind a paywall](https://noyb.eu/en/linkedin-locks-your-gdpr-rights-behind-paywall) — **05. Mai 2026**, Österreichische DSB

LinkedIn verlangt ein kostenpflichtiges Premium-Abo, um Besucherprotokolldaten des eigenen Profils einzusehen — obwohl Art. 15 DSGVO diesen Zugang kostenlos garantiert. noyb hat Beschwerde bei der österreichischen DSB eingereicht und fordert Geldstrafen. Der Widerspruch ist eklatant: LinkedIn verkauft dieselben Daten gegen Geld und verweigert sie gleichzeitig als kostenlose DSGVO-Auskunft.

*Cosmi-Implikation:* Kein "Pay or Consent" für DSGVO-Auskunftsrechte. Art.-15-Anfragen (Datenauskunft) müssen kostenlos und ohne Funktionseinschränkung erfüllbar sein. Wenn Cosmi für Premium-Nutzer andere Datenexport-Optionen anbietet als für Free-Tier: Rechtsgrundlage und Zugänglichkeit prüfen. **Modul:** DSGVO / Legal / Product. `#followup`

---

### noyb — CRIF Sammelklage: Scoring ohne Wissen *(09. Juni 2026, Carry-over)*

[Secret scoring: Join the CRIF class action now!](https://noyb.eu/en/secret-scoring-join-crif-class-action-now) — **09. Juni 2026**

CRIF (österreichisches Kreditauskunftsunternehmen) hat eine Datenbank mit nahezu allen Erwachsenen in Österreich aufgebaut und weist ihnen ein Scoring zu — obwohl 90 % dieser Personen keinerlei Kredithistorie bei CRIF haben. Die Daten wurden ursprünglich zu Marketingzwecken erhoben und zweckfremد für Bonitätsbewertungen genutzt. noyb koordiniert unter [crif.noyb.eu](https://crif.noyb.eu) eine Sammelklage auf Schadensersatz. Vorwürfe: fehlendes Consent, zweckfremde Verarbeitung, keine Benachrichtigung der Betroffenen.

*Cosmi-Implikation:* **Direktes Analogierisiko für CRM-Lead-Scoring.** Wenn Cosmi aus öffentlichen Quellen (LinkedIn, Handelsregister, Web-Scraping) Kontaktdaten anreichert und daraus Scores/Segmente bildet — identisches Muster wie CRIF. Rechtsgrundlage für Lead-Scoring validieren: Legitimate Interest reicht allein nicht. Betroffenenbenachrichtigung und Opt-Out sicherstellen. **Modul:** DSGVO / Legal / CRM / Product. `#akut`

---

### noyb — Schibsted „Pay or Okay" *(Carry-over KW23)*

- Beschwerdegegenstand: Norwegisches News-Publisher-Netzwerk bietet "Zustimmung zu Tracking ODER Abo" an
- noyb + NCC (Datatilsynet Norway) gemeinsame Beschwerde (03. Juni 2026)
- Cookie-Banner-Audit (Reject-Button-Äquivalenz) bei Cosmi noch offen. **Modul:** DSGVO / Frontend. `#followup`

---

## AI Act

### 🟡 AI Omnibus — Europaparlament stimmt zu: 423:57 (16. Juni 2026)

Das Europaparlament hat am **16. Juni 2026** den Digital Omnibus on AI mit **423 Ja-Stimmen, 57 Nein, 174 Enthaltungen** verabschiedet. Damit fehlt nur noch die formale Ratsentscheidung (erwartet: vor 02. August 2026).

**Was ändert sich konkret:**

| Obligation | Alte Frist | Neue Frist (nach OJ-Publikation) |
|-----------|-----------|----------------------------------|
| Hochrisiko AI Annex III (Standalone) | 02.08.2026 | **02.12.2027** |
| Hochrisiko AI Annex I (regulierte Produkte) | 02.08.2026 | **02.08.2028** |
| GPAI (General Purpose AI) | unverändert | unverändert |
| Verbotene AI Praktiken | unverändert | unverändert |

**Achtung:** Bis zur Publikation im EU-Amtsblatt gilt rechtlich weiterhin das 02.08.2026-Datum.

*Cosmi-Implikation:* Die neue Frist 02.12.2027 gibt Cosmi **18 zusätzliche Monate** für die Implementierung von Hochrisiko-Anforderungen (Technische Dokumentation, Konformitätsbewertung, Marktzugang-Meldung). Das Assessment bleibt dennoch sinnvoll — Ergebnis-Dokumentation jetzt als Basis. Sobald OJ-Publikation erfolgt, Compliance-Roadmap auf 02.12.2027 finalisieren. **Modul:** AI Act / Legal / Product. `#beobachten`

---

### ✅ AI-Act Hochrisiko-Klassifikation — Konsultation verlängert bis 23. Juli 2026

Die EU-Kommissions-Konsultation [Draft Guidelines for High-Risk AI Classification](https://digital-strategy.ec.europa.eu/en/consultations/targeted-consultation-draft-guidelines-classification-high-risk-artificial-intelligence-systems) (Art. 6 AI Act) wurde um **4 Wochen** verlängert — neue Frist: **23. Juli 2026, 22:00 CET**.

Begründung: Branchenverbände und NGOs haben mehr Beratungszeit gefordert.

*Cosmi-Implikation:* Der Zeitdruck vom letzten Sweep fällt weg. Dennoch sinnvoll: Assessment-Dokumentation intern abschließen (Lead-Scoring, KI-Chatbot, Churn-Prediction gegen Anhang III prüfen). Deadline jetzt **23. Juli** — 33 Tage mehr. Optional: Stellungnahme einreichen (Cosmi-Positionierung als EU-KI-konformes CRM). **Modul:** AI Act / Legal / Product. `#followup`

---

## NIS2

### BSI NIS-2 Portal Schritt 2 — seit 01. Juni aktiv *(Carry-over)*

*Keine neuen NIS2-Meldungen in KW25.* BSI-Pressemitteilungen-Feed weiterhin 404, ENISA 404. Schritt-2-Vollregistrierung (Pflichtangaben: Adresse, CISO-Kontaktdaten, statische IP-Ranges) weiterhin offen.

*Cosmi-Implikation:* Falls Cosmi als IT-Dienstleister/SaaS für regulierte Sektoren NIS-2-pflichtig → Schritt-2-Registrierung prüfen. **Modul:** NIS2 / Legal / Security. `#followup`

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche *(Woche 10 ohne e-Rechnung-bund.de RSS)*

*e-Rechnung-bund.de RSS weiterhin 404 (10. Woche in Folge). Kein neuer XRechnung/GoBD-Content via verfügbarer Quellen.*

Fristen-Erinnerung (unverändert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz >800.000 € |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

*Cosmi-Implikation:* GTM-Kampagne Q3 2026 — Positionierung als XRechnung-/ZUGFeRD-Lösung weiterhin in Planung. **Modul:** Buchhaltung / e-Rechnung / GTM. `#followup`

---

## ArbZG / Arbeitsrecht

### Stille Woche *(Woche 10 ohne BMAS RSS)*

*BMAS-RSS weiterhin 404. Kein ArbZG-Content in KW25.*

---

## eIDAS

### EUDI Wallet — September 2026 Frist in ~10 Wochen *(Carry-over)*

September-2026-Frist für Mitgliedsstaaten — NL/MT/BG im Rückstand (Realitätsstatus KW23). Massenadoption realistisch Q1/Q2 2027.

*Cosmi-Implikation:* eSignatur/eIDAS-Integration (Vertragsmodul) auf Sprint 6+ — vertretbar. **Modul:** eIDAS / Verträge / Auth. `#beobachten`

---

## BSI-Warnings — KW25 (14.–20. Juni 2026)

Zeitraum: **13.–19. Juni 2026** (neue Items seit letztem Sweep)

### 🔴 KRITISCH — sofortiger Handlungsbedarf

| Advisory | Produkt | Severity | Datum |
|----------|---------|----------|-------|
| WID-SEC-2026-???? | **GNU libc** | **KRITISCH** | 18. Jun |
| WID-SEC-2026-???? | **Drupal Core** | **KRITISCH** | 19. Jun |
| WID-SEC-2026-???? | **Splunk Enterprise** | **KRITISCH** | 19. Jun |

> **GNU libc KRITISCH:** Betrifft praktisch jeden Linux-Host. Docker-Base-Images, Alpine/Debian/Ubuntu prüfen und neu bauen. Remote-Exploitbarkeit je nach Distribution — sofortige Prüfung.
>
> **Splunk Enterprise KRITISCH:** Falls Cosmi Splunk für SIEM/Logging verwendet → sofortige Prüfung Patch-Status.

---

### 🟠 HOCH — Cosmi-relevante Infrastruktur

| Advisory | Produkt | Severity | Datum | Angriffsszenario |
|----------|---------|----------|-------|-----------------|
| [WID-SEC-2026-1995](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1995) | **NGINX / NGINX Plus** | **HOCH** | 18. Jun (NEU) | Remote: CVE-2026-42945 — **AKTIV AUSGENUTZT** |
| [WID-SEC-2026-1544](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1544) | **PostgreSQL** | **HOCH** | 18. Jun (Update) | Remote: CVSS 8.8 — SQL Injection, Code Execution, Info Disclosure |
| [WID-SEC-2026-1824](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1824) | **Apache HTTP Server** | **HOCH** | 18. Jun (NEU) | Remote: Mehrere Schwachstellen |
| [WID-SEC-2026-0861](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0861) | **Linux Kernel** | **HOCH** | 19. Jun (Update) | Remote/Lokal: DoS, Privilege Escalation |
| [WID-SEC-2026-1279](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1279) | **Linux Kernel** | **HOCH** | 18. Jun (Update) | Lokal: Mehrere Schwachstellen |

> **🚨 NGINX CVE-2026-42945 (WID-SEC-2026-1995) — AKTIV AUSGENUTZT:** Dieses Advisory ist neu seit letzter Woche und nach Recherche wird CVE-2026-42945 aktiv im Netz ausgenutzt. Der Angriffsvektor liegt im `ngx_http_rewrite_module` — speziell präparierte HTTP-Requests können Remote-Code-Execution oder DoS auslösen. API-Gateway und Reverse-Proxy-Instanzen sofort patchen. Kein WIP — sofortige Maßnahme.
>
> **PostgreSQL WID-SEC-2026-1544 (CVSS 8.8 — aktualisiert 18. Jun):** Remote-Angreifer können SQL Injection, Code Execution und Information Disclosure kombinieren. Advisory wurde am 18. Juni erneut aktualisiert (nach 07. Juni Update). Patch-Status verifizieren — insbesondere bei Postgres-Versionen < aktuelles Minor Release. Cosmi's DB-Hosts priorisiert patchen.
>
> **Apache HTTP Server (WID-SEC-2026-1824 — NEU):** Neues Advisory 18. Juni. Falls Apache im Stack (als Alternative zu NGINX oder für Legacy-Komponenten) — prüfen und patchen.

---

### MITTEL — Monitoring

- **GeoServer** (mittel, 19. Jun) — Falls im Geo-Stack
- **OpenSSL** (hoch/mittel, 18. Jun+) — OpenSSL-Updates auf allen Hosts einspielen
- **Squid** (mittel, 19. Jun) — Falls Proxy im Stack

---

## Stille Bereiche

- **EUR-Lex** — RSS-Feed weiterhin 404 (10. Woche). AI-Omnibus OJ-Eintrag via WebSearch: noch nicht publiziert.
- **BfDI Pressemitteilungen** — RSS 404 (9. Woche). Kein BfDI-Content.
- **BSI Pressemitteilungen** — RSS 404 (9. Woche). BSI-Content nur via Warnungs-Feed.
- **e-Rechnung Bund (BMWK)** — RSS 404 (10. Woche).
- **BMAS (Arbeitsrecht)** — RSS 404 (10. Woche).
- **ENISA** — RSS 404 (seit KW19 = 7. Woche).
- **EDPB** — Feed-URL 403 Forbidden (war KW24 XML-Fehler, jetzt 403). Website ebenfalls 403. Plenum-Ergebnisse via WebSearch rekonstruiert.
- **EDPS** — 403 Forbidden (war KW24 noch erreichbar). Letzter bekannter Artikel: 22. Mai 2026.
- **noyb** — Feed erreichbar, letzter Artikel 09. Juni (CRIF-Sammelklage). Keine neuen Posts KW25.

> **Wartungshinweis (Woche 9–10):** 6 von 10 Quellen 404, 2 von 10 jetzt zusätzlich 403. Quellen-Upgrade dringend — `sources/_regulation.yaml` braucht neue URLs. EDPB: alternativen Feed-Endpunkt suchen (oder Scraping EDPB-Newsseite direkt). Prio-Liste: EDPB > BMAS > BMWK/e-Rechnung > ENISA > BfDI.

---

## Cosmi-Action-Items

### 🔴 Akut — diese Woche

- [ ] **NGINX CVE-2026-42945 sofort patchen** — WID-SEC-2026-1995 (HOCH, NEU, **aktiv ausgenutzt**). API-Gateway und Reverse Proxy auf aktuelles NGINX-Release patchen. Kein Aufschub. `#security #infra` → **sofort**
- [ ] **GNU libc patchen** — KRITISCH, alle Linux-Hosts betroffen. Docker-Base-Images neu bauen (alpine/debian). `#security #infra` → **heute**
- [ ] **PostgreSQL patchen** — WID-SEC-2026-1544, CVSS 8.8, erneut aktualisiert 18. Jun. DB-Hosts auf aktuelles Minor Release bringen. `#security #infra #db` → **diese Woche**
- [ ] **CRIF-Sammelklage-Analogie prüfen** — Cosmi's Lead-Scoring: Rechtsgrundlage validieren, falls Kontaktdaten aus externen Quellen (Web, LinkedIn, Handelsregister) angereichert werden. Opt-Out und Benachrichtigungspflicht sicherstellen. `#dsgvo #legal #crm` → **bis 30. Juni**

### 🟡 Followup (KW26+)

- [ ] **AI Omnibus Compliance-Roadmap aktualisieren** — Sobald Ratsformalabstimmung + OJ-Publikation (erwartet vor 02.08.2026): Compliance-Zieldaten auf Annex-III-Standalone = 02.12.2027, Annex-I = 02.08.2028 setzen. `#aiact #legal #product`
- [ ] **AI-Act Hochrisiko-Assessment dokumentieren** — Frist jetzt **23. Juli** (verlängert). Lead-Scoring, Chatbot, Churn-Prediction gegen Anhang III abschließend bewerten. Ergebnis schriftlich fixieren. Optional: Stellungnahme einreichen. `#aiact #legal #product` → **bis 15. Juli (Puffer)**
- [ ] **EDPB Anonymisierungs-Guidelines** — Kommen bis Sommer 2026. Nach Publikation: Cosmi's Anonymisierungsroutinen (Test-Daten, Audit-Logs, Exports) validieren. `#dsgvo #legal #infra`
- [ ] **Art.-15-Auskunfts-Prozess validieren** (noyb/LinkedIn-Analogie) — DSGVO-Auskunftsanfragen kostenlos und ohne Feature-Lock erfüllbar? Automatisierter Export-Flow prüfen. `#dsgvo #legal #product`
- [ ] **Apache HTTP Server prüfen** — WID-SEC-2026-1824 (HOCH, NEU). Falls Apache im Stack → patchen. `#security #infra`
- [ ] **OpenSSL + Squid** — Updates auf allen relevanten Hosts einspielen. `#security #infra`
- [ ] **Splunk Enterprise** — Falls im Stack: kritisches Advisory prüfen und patchen. `#security #infra`
- [ ] **AI Omnibus OJ-Eintrag überwachen** — EUR-Lex auf Amtsblatt-Publikation. Formaler Start der Fristen ab OJ-Datum. `#aiact`
- [ ] **EDPB Europäisches Datenschutzsiegel** — Sub-Processor-Liste prüfen: Welche US-Anbieter könnten Siegel erwerben und SCCs ersetzen? `#dsgvo #sub-processor`
- [ ] **`sources/_regulation.yaml` Pflege** — 6×404 + 2×403 = 8 von 10 Quellen ausgefallen. Neue Feed-URLs recherchieren: EDPB, BMAS, BMWK/e-Rechnung, ENISA, BfDI. `#maintenance`
- [ ] **Cookie-Banner-Audit** (noyb/Schibsted Carry-over) — Reject-Button visuell equivalent zu Accept? `#dsgvo #frontend`
- [ ] **NIS2 BSI-Portal Schritt-2-Registrierung** prüfen (ab 01.06. offen). `#nis2`
- [ ] **BfDI Tätigkeitsbericht 2025 lesen** (Carry-over KW22). `#dsgvo`
- [ ] **eIDAS-Integration Sprint 6+** — September-Frist Tracking. `#eidas #product`
