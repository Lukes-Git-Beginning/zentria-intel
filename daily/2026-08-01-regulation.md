---
date: 2026-08-01
type: regulation
runtime_minutes: 19
items_scanned: 72
items_relevant: 15
sources_live_rss: 2
sources_ok_list: [bsi-warnungen, noyb]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 13
kw: 31
---

# Regulation-Sweep KW31/2026 (Sa 1. August)

> **KW31-Scope:** 26. Juli – 1. August 2026. Referenz-Sweep: KW30 (25. Juli). WebSearch-Supplements: 13. RSS-Live: BSI-WID (5 Cosmi-Stack-Advisories — **Go/NGINX/libc kritisch**), noyb (keine neue Klage).
>
> **🔴 AI ACT ART. 50(1) MORGEN (02.08.2026) — FINAL COUNTDOWN:** Transparenzpflicht für Chatbots, virtuelle Assistenten und Voice Agents tritt morgen Früh in Kraft. Bundesnetzagentur + BaFin übernehmen Enforcement in Deutschland (KI-MIG seit 29.07. in Kraft). Bußgeld: bis **€15M oder 3 % globaler Jahresumsatz**. Kein Aufschub.
>
> **🔴 KI-MIG DEUTSCHLAND — IN KRAFT 29. JULI 2026:** Deutsches KI-Marktüberwachungsgesetz (KI-MIG) trat am 29. Juli 2026 in Kraft. Bundesnetzagentur = zentrale KI-Aufsicht über alle Sektoren. BaFin = Finanzsektor (Chatbot-Disclosure, Kredit-Scoring). Bis Montag (02.08.) sind Behörden aktiv und können Ermittlungen einleiten.
>
> **🔴 NIS2 BSI-REGISTRIERUNGSFRIST ABGELAUFEN (31. JULI 2026):** Gestern um Mitternacht ist die letzte Nachfrist abgelaufen. BSI wechselt in Durchsetzungsmodus. ~18.500 von ~29.500 betroffenen Unternehmen haben registriert — ~11.000 Unternehmen im Rückstand. Bußgeld läuft.
>
> **🔴 BSI ADVISORIES KW31 — GO-BACKEND + NGINX + LIBC KRITISCH:** Drei Advisories direkt Cosmi-Stack-relevant: Golang Go HIGH (30.07.), NGINX/NGINX-Plus HIGH (30.07.), GNU libc CRITICAL (30.07.). Sofort patchen.
>
> **🟡 ArbZG REFERENTENENTWURF BMAS — 17. JUNI 2026 (UPGRADE VON KW30):** BMAS hat am 17. Juni 2026 den Referentenentwurf veröffentlicht (KW30 hatte nur "erwartet Herbst 2026"). Kernpunkte: Pflicht zur **elektronischen** Zeiterfassung + wöchentliche Höchstarbeitszeit per Tarifvertrag. Übergangsfrist nach Unternehmensgröße. Direkt relevant für Cosmi-Schichten.
>
> **🟡 EDPB Guidelines 03/2026 Web Scraping für GenAI (NEU):** EDPB hat am 7. Juli 2026 neue Leitlinien zu Web Scraping im Kontext generativer KI verabschiedet. Web Scraping personenbezogener Daten für GenAI-Training = DSGVO-pflichtig. Konsultation bis 30.10.2026.

---

## DSGVO / Datenschutz

### EDPB Guidelines 03/2026 — Web Scraping für Generative AI (7. Juli 2026) — Konsultation bis 30. Oktober *(KW31 NEU)*

[EDPB Guidelines 03/2026 on web scraping for generative AI](https://www.edpb.europa.eu/public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-generative-ai_en) | [EDPB Pressemitteilung Juli 2026](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en) | [RD Privacy Watch](https://www.rdprivacywatch.com/article/b5c19848-ce93-4104-976e-8c40fa01c9d8)

Das EDPB hat in seiner Plenar-Sitzung vom 7.–8. Juli 2026 die Leitlinien 03/2026 zu Web Scraping im Kontext generativer KI verabschiedet. Kernaussage: **Web Scraping personenbezogener Daten für das Training von Large Language Models und anderen Generative-AI-Systemen fällt unter die DSGVO** — unabhängig davon, ob die Daten öffentlich zugänglich sind.

**Compliance-Rahmen:**
- Rechtsgrundlage nach Art. 6 DSGVO erforderlich (Einwilligung, berechtigtes Interesse etc.)
- Einwilligung ist keine pauschale Erlaubnis für Scraping (EDPB blockt diesen Ausweg)
- Für besondere Kategorien (Art. 9) gelten Zusatzanforderungen
- Technische Maßnahmen gegen Scraping (robots.txt etc.) müssen respektiert werden

Dokument: 22 Seiten, Konsultation bis **30. Oktober 2026**.

*Cosmi-Implikation:* Relevant falls Cosmi eigene GenAI-Komponenten trainiert oder Drittanbieter-LLM-Dienste nutzt, die Kundendaten verarbeiten. SaaS-Dienste, die User-Daten in KI-Modelle einspeisen (Helpdesk-AI, CRM-Empfehlungen, Rapporte-Summarization), müssen DSGVO-konforme Rechtsgrundlage nachweisen können. Web-Scraping-Funktionen in Cosmi (falls vorhanden, z.B. Lead-Enrichment) auf GDPR-Konformität prüfen. `#beobachten` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB Blockchain Guidelines — Finale Version verabschiedet (Juli 2026) *(KW31 NEU)*

[EDPB — Blockchain Guidelines Final](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en) | [Guidelines on anonymization, AI web scraping, blockchain](https://www.mlex.com/mlex/articles/2498541/guidelines-on-anonymization-ai-web-scraping-blockchain-adopted-by-edpb)

Das EDPB hat im Juli 2026 die finalen Blockchain-Leitlinien verabschiedet (keine weitere Konsultation mehr). Inhalt: DSGVO-Compliance für verschiedene Blockchain-Architekturen — öffentliche, private, permissioned. Kernproblem: Unveränderlichkeit der Blockchain vs. Löschrechte nach Art. 17 DSGVO.

*Cosmi-Implikation:* Für Cosmi als klassische PostgreSQL-Backend-Lösung derzeit kein direkter Handlungsbedarf. Falls Cosmi-Vertraege-Modul oder Buchhaltung zukünftig Smart-Contract-Elemente integriert: EDPB-Blockchain-Guidelines lesen. `#beobachten` **Modul:** DSGVO / Legal / Product.

---

### 🟡 EDPB Data-Breach-Notification-Template — Konsultation schliesst in 4 TAGEN (05.08.2026) *(KW30 Carry-over — DRINGEND)*

[EDPB — Template for personal data breach notification](https://www.edpb.europa.eu/public-consultations/template-for-personal-data-breach-notification_en)

**4 Tage bis Konsultationsschluss (05. August 2026).** Template herunterladen, mit Cosmi-Incident-Response-SOP abgleichen, Lücken identifizieren. Nach Finalisierung gilt dieses harmonisierte Format für Art.-33-Meldungen in allen 27 EU-Staaten. Jetzt kommentieren wenn Lücken sichtbar — Eingaben werden publiziert.

*Cosmi-Implikation:* SOP-Abgleich bis spätestens Montag 04.08. (um 1 Tag Puffer zu haben). `#followup → bis 04.08.2026` **Modul:** DSGVO / Legal / Security.

---

### 🟡 EDPB Cross-Regulatory Cooperation — Dublin Meeting 16.–17. Juli *(KW31 NEU)*

[Gibson Dunn — Data Protection July 2026](https://www.gibsondunn.com/gibson-dunn-europe-data-protection-july-2026/)

Das EDPB forderte auf einem hochrangigen Meeting in Dublin (16.–17. Juli 2026) eine klare Rechtsgrundlage für den Informationsaustausch zwischen Regulierungsbehörden mit unterschiedlichen Zuständigkeiten (DSA, DMA, AI Act, DSGVO). Trend: Zunehmende Vernetzung zwischen Datenschutz-, Wettbewerbs- und KI-Aufsichtsbehörden in der EU.

*Cosmi-Implikation:* Signalwirkung für Cosmi: Datenschutz- und AI-Act-Compliance werden in Zukunft gemeinsam geprüft (cross-regulatory audits). BfDI/LDA-Anfragen könnten AI Act-Implikationen mit einbeziehen. `#beobachten` **Modul:** DSGVO / AI Act / Legal.

---

### 🟡 DPF Schrems III — Keine neue Klageeinreichung KW31 *(Carry-over)*

[Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) | [activeMind.legal](https://www.activemind.legal/guides/dpf-supreme-court/) | [Freshfields — DPF survives first challenge](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-us-data-privacy-framework-survives-its-first-judicial-challenge-but-more-are-102l4m1)

Keine neue noyb-Klageeinreichung KW31. DPF formal gültig. noyb: Schrems-III-Einreichung "binnen Wochen bis Monaten". SCOTUS-Entscheidung Trump v. Slaughter (FTC-Unabhängigkeit) bleibt der Trigger. EC hat auf noyb-Brief vom 30. Juni nicht reagiert.

*Cosmi-Implikation:* SCC-Fallback-Audit weiterhin dringend. US-SaaS-Transfers inventarisieren. `#followup` **Modul:** DSGVO / Legal / Infra.

---

## AI Act

### 🔴 KI-MIG — Deutsches KI-Marktüberwachungsgesetz — In Kraft 29. Juli 2026 *(KW31 HEADLINE)*

[KI-MIG in Kraft: Bundesnetzagentur wird zentrale KI-Aufsicht](https://www.blogspan.net/ki-mig-bundesnetzagentur-ki-aufsicht/) | [TechTimes — Germany gets AI Regulator](https://www.techtimes.com/articles/322313/20260730/germany-gets-ai-regulator-wildberger-says-control-still-five-minutes-midnight.htm) | [TechTimes — BaFin Finanzsektor](https://www.techtimes.com/articles/322089/20260729/germany-arms-bafin-police-ai-credit-scoring-bank-chatbot-disclosure.htm) | [Gleiss Lutz — KI-MIG](https://www.gleisslutz.com/en/know-how/federal-government-draft-bill-implement-eu-artificial-intelligence-act)

Das **KI-Marktüberwachungsgesetz (KI-MIG)** trat am **29. Juli 2026** in Kraft — drei Tage vor dem AI-Act-Art.-50-Deadline. Es schafft Deutschlands nationale Durchführungsstruktur für den EU AI Act.

**Enforcement-Struktur ab sofort:**

| Behörde | Zuständigkeit |
|---------|--------------|
| **Bundesnetzagentur** | Zentrale KI-Marktüberwachung (alle Branchen), nationales Koordinierungszentrum, Single Point of Contact, Beschwerdeanlaufstelle |
| **BaFin** | Finanzsektor (Chatbot-Disclosure, Kredit-Scoring-Algorithmen, Versicherungspreismodelle) |
| Sonstige Sektoraufsichten | Medizinprodukte, Fahrzeuge etc. |

BaFin hat **29. Juli 2026** mit Finanzsektor-Überwachung begonnen. Fokus: Transparenzpflichten bei Chatbots, Kreditwürdigkeit, Lebens-/Krankenversicherung-Pricing.

*Cosmi-Implikation:* **Als DACH-SaaS-Anbieter ist Cosmi ab sofort unter Bundesnetzagentur-Aufsicht für AI-Act-Compliance.** Falls Cosmi-Kunden im Finanzsektor Cosmi-KI-Features einsetzen: auch BaFin-relevant. Ab morgen (02.08.) können beide Behörden aktiv Ermittlungen einleiten. Bundesnetzagentur-Marktüberwachungs-Seite bookmarken: [Marktüberwachung KI](https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/AI/14_MarketSurveillance/start.html). `#akut` **Modul:** AI Act / Legal / Product.

---

### 🔴 AI Act Art. 50(1) Chatbot-Offenlegung — MORGEN (02.08.2026) *(KW31 — LETZTER TAG)*

[CSA Research Note — Art. 50 Takes Effect](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/) | [EC FAQ Art. 50](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | [Bratby Law — Art. 50](https://bratby.law/ai-act-transparency-obligations-2026/) | [Pebblous — Practical Guide](https://blog.pebblous.ai/blog/eu-ai-act-transparency-august-2026/en/)

**Heute ist der letzte Tag** vor dem Inkrafttreten der Art.-50(1)-Transparenzpflichten. Ab morgen 00:00 Uhr kann die Bundesnetzagentur Enforcement-Maßnahmen einleiten.

**Was ab 02.08.2026 gilt:**
- **Art. 50(1):** Chatbots, virtuelle Assistenten, Voice Agents, Customer-Service-Automation, E-Mail-Bots → **erster Kontakt** muss KI-Natur offenlegen. Automatisch, unumgehbar.
- **Art. 50(3):** KI-generierte Deepfake-Bild/Video/Audio-Inhalte müssen als "maschinell erzeugt" kenntlich gemacht werden.
- *Nicht* ab 02.08: Art. 50(2)/(4) Wasserzeichen/Content-Labeling → Übergangsfrist bis 02.12.2026 (aus Omnibus).

Enforcement DE: **Bundesnetzagentur** (allgemein) + **BaFin** (Finanzsektor). Bußgeld: **€15M oder 3 % globaler Jahresumsatz**.

*Cosmi-Implikation:* **HEUTE Go/No-Go finalisieren.** Alle Touchpoints checken: (a) App-Widget / KI-Assistent im CRM-Core, (b) AI-Telefon-Dialer, (c) Helpdesk-Chatbot, (d) Formulare-KI, (e) API-Kunden die Cosmi-KI einbetten. Offenlegungstext muss beim ersten Interaktionspunkt erscheinen — nicht nach Anmeldung, nicht nach 3 Klicks. `#akut → bis 02.08.2026` **Modul:** AI Act / Legal / Product.

---

### 🟡 AI Act Art. 50(2)/(4) Wasserzeichen/Deepfake-Labeling — 02.12.2026 (123 Tage) *(Carry-over)*

Übergangsfrist aus AI Act Omnibus (Reg. 2026/1744, in Kraft 27.07.). C2PA-Standard als Wasserzeichen-Pflicht — Technologie-Gap noch vorhanden.

*Cosmi-Implikation:* Prüfen ob Cosmi KI-generierte Audio/Video/Bild-Inhalte an Endkunden ausliefert. Falls ja: C2PA-Integration bis Dezember. `#beobachten → bis 02.12.2026` **Modul:** AI Act / Legal / Product.

---

## NIS2

### 🔴 NIS2 BSI-Registrierung ABGELAUFEN (31.07.2026) — Enforcement-Modus ab August *(KW31 STATUSWECHSEL)*

[BSI NIS2 Registration Guide](https://nisd2.eu/en/wiki/scope/nis2-registration) | [Reed Smith — Last Deadline](https://www.reedsmith.com/our-insights/blogs/viewpoints/102n52v/nis2-in-germany-last-deadline-for-registration/) | [BornCity — NIS2-Lücke](https://borncity.com/blog/2026/07/30/das-problem-der-nis-2-registrierungsluecke-meldung-bis-31-juli-2026-moeglich/) | [Morrison Foerster — Enforcement](https://www.mofo.com/resources/insights/251208-flipping-the-nis2-switch-what-germanys-implementation)

**Statuswechsel:** Die NIS2-Registrierungspflicht ist seit gestern (31.07.2026 Mitternacht) in die vollständige Durchsetzungsphase eingetreten.

| Zeitstempel | Ereignis |
|-------------|---------|
| 06.03.2026 | Gesetzlicher Registrierungsstichtag |
| ~11.500/29.500 | Registriert zum ursprünglichen Stichtag |
| ~18.500/29.500 | Registriert Ende Mai 2026 |
| 31.07.2026 (gestern) | Letzte BSI-Nachfrist abgelaufen |
| **01.08.2026 (heute)** | **BSI im vollständigen Enforcement-Modus** |

**Bußgeldrisiko für nicht registrierte Unternehmen:** Wichtige Einrichtungen bis €500.000 (§60 BSIG), Essential Entities bis €10M/2% globaler Jahresumsatz, §38 BSIG GF-Haftung persönlich/unbeschränkt.

*Cosmi-Implikation:* Falls Cosmi-Registrierung noch nicht abgeschlossen: **sofort** registrieren (Verzugszustand seit März). Falls Registrierung erfolgte: Anlagen I/II-Einstufung und BSI-Meldekanal dokumentieren. Nächste NIS2-Pflicht: Cybersicherheitsmaßnahmen nach §30 BSIG nachweisen. `#akut` **Modul:** NIS2 / Legal / Management.

---

### BSI C5:2026 Gap-Analyse — 10 Monate bis Audit-Relevanz (01.06.2027) *(Carry-over)*

BSI C5:2026 gilt für Audit-Engagements ab 01.06.2027. Neue Bereiche: Post-Quanten-Kryptografie, Container-Management, Confidential Computing, EUCS-Alignment.

*Cosmi-Implikation:* Gap-Analyse starten. Für DACH-B2B-Kunden zunehmend Vertriebsvoraussetzung. `#beobachten → bis Q1/2027` **Modul:** NIS2 / Security / Infra.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche — keine neuen Regelungen KW31

Fristen-Status (unveraendert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen — Pflicht |
| bis 31.12.2026 | Übergangsfrist **Versand** — Papier/PDF (mit Zust.) noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz > €800k Vorjahresumsatz |
| ab 01.01.2028 | **Versandpflicht** alle B2B |
| dauerhaft | Kleinunternehmer §19 UStG — befreit |

**Hinweis XRechnung 4.0:** Neue Version in Vorbereitung. Wesentliche Änderung: Auflösung der starren 1:1:1-Zuordnung (eine Rechnung = eine Bestellung = eine Lieferung). Kein festes Datum bekannt, aber Cosmi-Buchhaltungsmodul sollte Design flexibel halten.

---

## ArbZG / Arbeitsrecht

### 🟡 ArbZG Referentenentwurf BMAS — 17. Juni 2026 — Elektronische Zeiterfassung + Wochenarbeitszeit *(KW31 UPGRADE)*

[Clockin — Referentenentwurf Details](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026) | [Betriebsratspraxis24 — Wöchentliche Höchstarbeitszeit](https://www.betriebsratspraxis24.de/arbeitszeit/referentenentwurf-woechentliche-hoechstarbeitszeit-nur-mit-tarifvertrag-18955/) | [Eversheds-Sutherland](https://www.eversheds-sutherland.com/de/germany/insights/update-zum-arbeitszeitgesetz-referentenent-wurf-zur-elektronischen-arbeitszeiterfassung) | [LTO — Bas kündigt an](https://www.lto.de/recht/nachrichten/n/bas-kuendigt-gesetzentwurf-arbeitszeitgesetz-an-juni-2026)

**KW30-Update:** BMAS hat bereits am **17. Juni 2026** einen Referentenentwurf veröffentlicht — KW30-Prognose "erwartet Herbst 2026" war überholt. Gesetzgebungsverfahren ist im Gang.

**Kernpunkte des Referentenentwurfs:**

| Regelung | Detail |
|---------|--------|
| **Elektronische Zeiterfassung** | Pflicht zur Aufzeichnung von Beginn, Ende und Dauer täglich — **elektronisch** |
| **Wöchentliche Höchstarbeitszeit** | Via Tarifvertrag statt täglich; einzelne Tage länger möglich, wenn Wochendurchschnitt stimmt |
| **Tägliche Ruhezeit** | 11h-Pflicht kann durch tarifliche Gesundheitsschutz-Regelungen entfallen |
| **Übergangsfristen** | Großunternehmen: 1 Jahr; bis 250 MA: 2 Jahre; Kleinbetriebe: 5 Jahre |

Wirtschaftsverbände und Gewerkschaften unzufrieden — politische Auseinandersetzungen im Herbst erwartet. Verabschiedung 2026 weiterhin möglich aber nicht sicher.

*Cosmi-Implikation:* **Schichten-Modul direkt betroffen:** (1) Wochenarbeitszeit-Tracking muss neben Tageserfassung implementiert werden — Datenbankschema jetzt erweitern bevor Gesetz gilt. (2) Elektronische Zeiterfassung als Pflicht = Cosmi-Schichten als Compliance-Tool positionieren (Vertriebsargument!). (3) Übergangsfrist-Logik per Unternehmensgrößen-Konfiguration ist Feature-Anforderung. Referentenentwurf jetzt lesen und Requirements-Backlog befüllen. `#followup` **Modul:** ArbZG / Legal / Schichten / Product.

---

## eIDAS

### 🟡 Deutsches Digitale-Identitäten-Gesetz — Kabinettsentwurf 20. Mai 2026 + EU eIDAS Framework August 2026 *(KW31 NEU)*

[Freshfields — EUDI Wallet](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/the-eudi-wallet-is-coming-what-businesses-need-to-know-102mvuy) | [WithPersona — DE/FR Sandbox](https://withpersona.com/blog/persona-supports-france-and-germany-eudi-wallets-for-secure-private-identity-verification/) | [Kennedys — EUDIW Framework](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-digital-identity-framework-introducing-the-new-eu-digital-identity-wallet/)

**Zwei parallele Entwicklungen KW31:**

1. **Deutsches Digitale-Identitäten-Gesetz:** Kabinettsentwurf 20.05.2026 verabschiedet. Implementiert alle drei Wallet-Modelle unter eIDAS 2. Keine Beschränkung der Wallet-Anzahl (keine numerischen Obergrenzen). Nächster Schritt: Bundestag.

2. **EU eIDAS Framework "kommt in Kraft August 2026":** Mehrere Quellen bestätigen August 2026 als EU-weiten eIDAS-2-Framework-Meilenstein (technische Standards, ARF v2.8.0 aktuell). Deutschland: Sandbox aktiv, Launch 02.01.2027 (154 Tage).

*Cosmi-Implikation:* Mit August als Aktivierungsmonat: Q3/2026 ist der richtige Moment, ARF v2.8.0 zu lesen und Relying-Party-Anforderungen für Cosmi-Vertraege/Formulare/e-Signing zu evaluieren. Q4-Sprint einplanen. `#beobachten → Q3/2026-Sprint` **Modul:** eIDAS / Product / Vertraege.

---

## BSI-Warnings — KW31 (26. Juli – 1. August 2026)

> **KW31-Highlight: Drei direkte Cosmi-Stack-Treffer.** Golang Go HIGH + NGINX/NGINX-Plus HIGH + GNU libc CRITICAL — alle vom 30. Juli 2026. Sofortiges Patch-Management erforderlich.

### 🔴 Cosmi-Stack-Advisories KW31

| Advisory | Produkt | Datum | Schwere | Risiko | Massnahme |
|----------|---------|-------|---------|--------|-----------|
| BSI WID KW31-A | **Golang Go** | 30.07.2026 | HIGH | Arbitrary Code Execution, Security Bypass | **Sofort patchen** — Go-Backend Cosmi |
| BSI WID KW31-B | **NGINX / NGINX Plus** | 30.07.2026 | HIGH | Data Manipulation, Code Execution, DoS | **Sofort patchen** — Reverse Proxy |
| BSI WID KW31-C | **GNU libc** | 30.07.2026 | CRITICAL | Remote File Manipulation, DoS, unspecified | **Sofort patchen** — Basis Linux-Library |
| BSI WID KW31-D | **Kubernetes** | 31.07.2026 | HIGH | Info Disclosure, Security Bypass | Patchen falls containerisiert |
| BSI WID KW31-E | **Linux Kernel** | 31.07.2026 | MEDIUM | Memory Corruption, Kernel Disclosure, DoS | Regulaer updaten |

> **GNU libc CRITICAL:** Remote-Code-Pfad potenziell vorhanden — höchste Priorität nach AI-Act-Deadline-Sprint. Go-Backend und NGINX ebenfalls sofort.

### Status KW29-Advisories

| Advisory | Produkt | Status |
|----------|---------|--------|
| PostgreSQL 18.4/17.10/16.14 | PostgreSQL | Patch seit 16.07. — falls noch nicht gepatcht: sofort |
| WID-SEC-2026-1686 | Samba | Weiterhin offen |
| nginx-ui | nginx-ui | Root-Exec-Risk — deaktivieren oder patchen |

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 16). AI-Omnibus und sonstige Publikationen via WebSearch abgedeckt.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 15). Keine BfDI-Pressemitteilungen KW31 via WebSearch identifiziert.
- **BSI Pressemitteilungen** — RSS 404 (Woche 15). BSI-WID-Advisory-Feed (WID) zugänglich — Advisories direkt abgerufen.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 16). Keine neuen XRechnung-Regelungen KW31.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 16). Referentenentwurf vom 17.06. via WebSearch abgedeckt.
- **ENISA** — RSS 404 (Woche 13). Keine neuen ENISA-Publikationen KW31 identifiziert.
- **EDPB Newsroom** — RSS 403. EDPB-Plenary-Output (Web Scraping, Blockchain Guidelines) via WebSearch und Direktlink abgedeckt.
- **EDPS** — 403 Forbidden. Keine neuen EDPS-Publikationen.
- **noyb** — RSS zugänglich; keine neue Klageinreichung KW31.

> **Wartungshinweis (Woche 16):** 6×404 + 2×403 persistent. BSI-WID-Direkt-Feed funktioniert als kompensierender Kanal. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — sofort / bis 02.08.2026

- [ ] **GNU libc CRITICAL patchen** — BSI Advisory 30.07.2026, CRITICAL. Remote-Angriffspfad. Sofort auf allen Produktionsservern patchen. Deployment-Freeze für AI-Act-Sprint kurz unterbrechen. `#security #infra` → **sofort**
- [ ] **Golang Go HIGH patchen** — BSI Advisory 30.07.2026, HIGH. Arbitrary Code Execution im Go-Backend. Go-Version updaten, Build-Pipeline neu starten. `#security #infra #backend` → **sofort**
- [ ] **NGINX / NGINX Plus HIGH patchen** — BSI Advisory 30.07.2026, HIGH. Data Manipulation + Code Execution. Reverse Proxy updaten. `#security #infra` → **sofort**
- [ ] **AI Act Art. 50(1) HEUTE FINALER GO/NO-GO** — Alle KI-Interaktions-Touchpoints: CRM-Widget, Dialer-AI, Helpdesk-Bot, Formulare-KI, API-Endpunkte. Offenlegungstext beim ersten Kontakt. Ab morgen 00:00 Uhr Bundesnetzagentur-Enforcement. `#aiact #legal #product` → **bis heute Abend**
- [ ] **NIS2 BSI-Registrierung sicherstellen** — Frist abgelaufen. Falls noch nicht registriert: jetzt. Falls registriert: Registrierungsnachweis dokumentieren. `#nis2 #legal` → **sofort**

### 🟡 Followup (KW32+)

- [ ] **EDPB Breach Template Konsultation — bis 04.08.** — Schliesst 05.08. Template herunterladen, Incident-Response-SOP abgleichen, ggf. kommentieren. `#dsgvo #security` → **bis 04.08.2026**
- [ ] **ArbZG Referentenentwurf (17.06.2026) lesen** — Schichten-Modul: Wochenarbeitszeit-Tracking als DB-Schema-Erweiterung vorbereiten. Elektronische Zeiterfassung als Compliance-Feature-Argument definieren. Übergangsfrist-Konfiguration als Product-Anforderung aufnehmen. `#arbzg #product #schichten` → **KW32-Sprint**
- [ ] **EDPB Web Scraping Guidelines 03/2026 prüfen** — Falls Cosmi-KI-Features User-Daten für Training oder Enrichment verarbeiten: DSGVO-Rechtsgrundlage explizit dokumentieren. Web-Scraping-Features in Lead-Modul (falls vorhanden) auf GDPR-Konformität prüfen. `#dsgvo #legal #ai-features` → **KW32**
- [ ] **KI-MIG Compliance-Dokumentation** — Bundesnetzagentur als zuständige Behörde in interne AI-Act-Compliance-Doku eintragen. Kontaktseite bookmarken. Falls KI-Features in Finanzsektor-Kunden eingesetzt werden: BaFin-Anforderungen prüfen. `#aiact #legal` → **KW32**
- [ ] **DPF SCC-Fallback-Audit abschliessen** — US-SaaS-Transfers inventarisieren, SCCs dokumentieren, STMs evaluieren. `#dsgvo #legal #infra` → **bis Schrems-III-Einreichung**
- [ ] **EUDIW ARF v2.8.0 lesen** — Relying-Party-Anforderungen für Cosmi-Vertraege/Formulare evaluieren. Q4/2026-Sprint einplanen (154 Tage bis DE-Launch 02.01.2027). `#eidas #product` → **Q3/2026**
- [ ] **Kubernetes + Linux Kernel KW31 patchen** — BSI Advisories HIGH/MEDIUM. Im regulären Patch-Zyklus dieser Woche. `#security #infra` → **KW32**
- [ ] **BSI C5:2026 Gap-Analyse starten** — 10 Monate bis Audit-Relevanz (01.06.2027). `#nis2 #security` → **Q3/2026**
- [ ] **EDPB Anonymisation Guidelines 02/2026 + 03/2026 beide lesen** — 3-Kriterien-Test für Anonymität, Web-Scraping-Framework. Konsultation bis 30.10.2026. `#dsgvo #legal` → **bis Oktober**
