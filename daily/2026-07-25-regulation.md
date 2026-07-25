---
date: 2026-07-25
type: regulation
runtime_minutes: 17
items_scanned: 73
items_relevant: 13
sources_live_rss: 1
sources_ok_list: [bsi-warnungen, noyb]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 12
kw: 30
---

# Regulation-Sweep KW30/2026 (Sa 25. Juli)

> **KW30-Scope:** 19.–25. Juli 2026. Referenz-Sweep: KW29 (18. Juli). WebSearch-Supplements: 12. RSS-Live: BSI-WID (Neuadvisories KW30: keine Cosmi-Stack-Treffer), noyb.
>
> **🔴 AI ACT OMNIBUS — AMTSBLATT 24. JULI 2026 (GESTERN): INKRAFTTRETEN 27. JULI 2026 (MONTAG):** Regulation (EU) 2026/1744 wurde gestern im Amtsblatt der EU (OJ L) veröffentlicht. Inkrafttreten: **Montag, 27. Juli 2026**. Art. 50 Transparenz-Deadline bleibt **02.08.2026 — 8 TAGE**. Art. 50(2)/(4) Wasserzeichen/Deepfake-Labeling: 3-Monats-Übergangsfrist bis **02.12.2026** (Omnibus-Bonus). Annex-III-Hochrisiko (Standalone): verschoben auf **02.12.2027**. Bußgeld Art. 50: bis **€15M oder 3 % globaler Jahresumsatz** — bestätigt.
>
> **🔴 AI ACT ART. 50 CHATBOT-OFFENLEGUNG — 8 TAGE (02.08.2026):** Final-Sprint. Alle KI-Interaktions-Touchpoints müssen beim ersten Kontakt als KI identifizierbar sein. Kein Aufschub. Enforcement durch Marktüberwachungsbehörden in allen 27 EU-Staaten ab 02.08.2026.
>
> **🔴 NIS2 BSI-REGISTRIERUNG — 6 TAGE (31. JULI 2026) — LETZTE CHANCE:** Absolut letzte Frist. BSI: konsequente Durchsetzung ab 01. August. Nur ~18.500 von 29.500 erwarteten Unternehmen registriert. Keine weitere Verlängerung. Bußgeld bis €10M/2 % (Essential Entities) + §38-GF-Haftung. Empfehlung: mit Puffer bis **28. Juli**.
>
> **🟡 DPF SCHREMS III — KEINE NEUE ENTWICKLUNG KW30:** noyb-Brief an EC 30. Juni 2026 (SCOTUS Trump v. Slaughter). Klageeinreichung 'binnen Wochen'. DPF formal noch gültig. SCC-Fallback-Audit aus KW29 jetzt abschließen.
>
> **🟡 EDPB DATA-BREACH-TEMPLATE-KONSULTATION — 11 TAGE (05.08.2026):** Konsultation schliesst 5. August. Template herunterladen, mit Incident-Response-SOP abgleichen.

---

## DSGVO / Datenschutz

### 🟡 EDPB Data-Breach-Notification-Template (Art. 33 DSGVO) — Konsultation schliesst 05. August *(11 Tage — KW29 carry-over)*

[EDPB — Template for personal data breach notification](https://www.edpb.europa.eu/public-consultations/template-for-personal-data-breach-notification_en) — EDPB, verabschiedet 10. Juni 2026

Das EDPB hat ein einheitliches EU-weites Template für Datenschutzverletzungs-Meldungen nach Art. 33 DSGVO verabschiedet und zur öffentlichen Konsultation gestellt. Ziel: Harmonisierung der Breach-Notification über alle 27 Datenschutzbehörden. Das Template ist als IT-Tool konzipiert — DSBs werden es schrittweise implementieren. Kommentare müssen bis **05. August 2026** eingereicht werden. Eingereichte Kommentare werden auf der EDPB-Website publiziert.

*Cosmi-Implikation:* Template herunterladen und mit dem bestehenden Incident-Response-SOP abgleichen. Nach Finalisierung gilt das harmonisierte Format für alle Art.-33-Meldungen in der EU. Lücken jetzt schliessen ist einfacher als nach Inkrafttreten. `#followup` **Modul:** DSGVO / Legal / Security. → **bis 28. Juli (interne Deadline vor Konsultationsschluss)**

---

### EDPB Guidelines 02/2026 on Anonymisation — verabschiedet 7. Juli, Konsultation bis 30. Oktober 2026 *(KW30 NEU)*

[EDPB Guidelines 02/2026 on Anonymisation](https://www.edpb.europa.eu/public-consultations/guidelines-022026-on-anonymisation_en) — EDPB, 7. Juli 2026

Das EDPB hat neue Leitlinien zur Anonymisierung verabschiedet, die das veraltete WP29-Dokument von 2014 ersetzen. Hintergrund: CJEU-Urteil EDPS v. SRB (C-413/23 P, 4. September 2025), das klargestellt hat, dass pseudonymisierte Daten in bestimmten Kontexten kein personenbezogenes Datum darstellen müssen (relative Betrachtung).

**Drei-Kriterien-Test für echte Anonymität:**
1. Keine Isolation einzelner Datensätze
2. Keine Verknüpfung mit anderen Datensätzen
3. Keine Rückschlüsse auf natürliche Personen

Wenn alle 3 Kriterien erfüllt: Daten können als anonym gelten und fallen nicht unter die DSGVO. Konsultation bis **30. Oktober 2026**.

*Cosmi-Implikation:* Relevant für Analytics-Daten, archivierte CRM-Daten, Rapporte-Modul (Mitarbeiter-Performance-Daten), und Schichten-Historien. Anonymisierungsansätze gegen neuen 3-Kriterien-Test prüfen. Pseudonymisierung allein reicht unter bestimmten Umständen weiterhin als Schutzmaßnahme, aber die Grenze zu personenbezogenen Daten ist jetzt kontextabhängiger. `#beobachten` **Modul:** DSGVO / Legal / Product.

---

### 🟡 DPF SCHREMS III — Keine neue Entwicklung KW30 — SCC-Fallback weiterhin kritisch *(Carry-over KW29)*

[activeMind.legal — SCOTUS DPF Analysis](https://www.activemind.legal/guides/dpf-supreme-court/) | [Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/)

Keine neue noyb-Klage KW30 — aber Einreichung "binnen Wochen" angekündigt. noyb-Brief an EC vom 30. Juni 2026 nach SCOTUS Trump v. Slaughter (29.6., 6:3): FTC-Unabhängigkeit untergraben. noyb fordert Rückzug der DPF-Adequacy-Entscheidung. EC hat bisher nicht reagiert.

**Aktuelle Risikolandschaft:**

| Klage | Status | Erwartetes Urteil |
|-------|--------|-------------------|
| Latombe v. EC (CJEU) | Pending | Q4/2026–Q1/2027 |
| Schrems III (noyb) | Angekündigt, Einreichung binnen Wochen | 2027–2028 |
| DPF Adequacy-Entscheidung | Formal gültig | — |

*Cosmi-Implikation:* SCC-Fallback-Audit aus KW27/KW29 jetzt abschließen: (1) US-SaaS-Transfers inventarisieren (Intercom, HubSpot, Google Analytics etc.), (2) SCCs als Primärmechanismus dokumentieren, (3) Supplementary Technical Measures evaluieren. Timing kritisch: Schrems-III-Klage kann binnen Wochen eingereicht werden. `#followup` **Modul:** DSGVO / Legal / Infra.

---

### BfDI Hennemann — Durchsetzungsschwerpunkte 2026 bekannt *(KW30 NEU — Amtsübernahme 01.10.2026)*

[BfDI — Pressemitteilung: Bundestag wählt Hennemann](https://www.bfdi.bund.de/SharedDocs/Pressemitteilungen/DE/2026/10_BfDI-Wahl-Hennemann.html) | [netzpolitik.org](https://netzpolitik.org/2026/moritz-hennemann-neuer-bundesbeauftragter-fuer-datenschutz-und-informationsfreiheit-gewaehlt/)

Prof. Dr. Moritz Hennemann übernimmt das BfDI-Amt am **01. Oktober 2026** (Wahltermin 391:122:77). Specht-Riemenschneider bleibt bis 30.09.2026. Durchsetzungsschwerpunkte 2026 (aus Tätigkeitsbericht 2024):

| Schwerpunkt | Relevanz für Cosmi |
|-------------|-------------------|
| **KI-Tools im Beschäftigungskontext** | Schichten-Modul, CRM-Recruiting, AI-assisted Performance |
| **Cookie-Compliance** | Cosmi-Webpräsenz, Kundenportale |
| **Schrems-II-Konformität** | Alle US-SaaS-Transfers |
| **Meldepflicht-Disziplin (Art. 33)** | Incident-Response-SOP |

*Cosmi-Implikation:* KI-im-HR-Schwerpunkt direkt relevant: Falls Cosmi-Schichten oder CRM-Rapporte KI-gestützte Empfehlungen oder Bewertungen erzeugen, die HR-Entscheidungen beeinflussen, jetzt auf Art. 22 DSGVO + KI-im-HR-Leitlinien prüfen. `#beobachten` **Modul:** DSGVO / Legal.

---

## AI Act

### 🔴 AI Act Omnibus — Regulation (EU) 2026/1744 im Amtsblatt (24. Juli) — Inkrafttreten 27. Juli *(KW30 HEADLINE)*

[EUR-Lex — Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) | [Freshfields AI Act Unpacked #34](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber) | [Gibson Dunn — Key Changes](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)

**Das Warten ist vorbei:** Regulation (EU) 2026/1744 (Digital Omnibus on AI) wurde am **24. Juli 2026** im Amtsblatt der EU (OJ L) veröffentlicht. Inkrafttreten: **Montag, 27. Juli 2026**. Législation-History: EP 16.06., Rat 29.06., Unterzeichnung 08.07., OJ 24.07.

**Finale Fristen-Architektur (rechtlich bindend ab 27.07.2026):**

| Pflicht | Frist | Status KW30 |
|---------|-------|-------------|
| **Art. 50(1) Chatbot-Offenlegung** | **02.08.2026 — 8 TAGE** | UNVERAENDERT — AKUT |
| Art. 50(2) KI-Audio/Video/Bild Wasserzeichen | **02.12.2026** (3-Mon.-Übergangsfrist) | NEU BESTÄTIGT |
| Art. 50(4) Deepfake-Kennzeichnung | **02.12.2026** (3-Mon.-Übergangsfrist) | NEU BESTÄTIGT |
| GPAI-Pflichten | seit 02.08.2025 — bereits gültig | = |
| **Annex III Standalone-Hochrisiko** | **02.12.2027** (verschoben) | = |
| Annex I Hochrisiko in regulierten Produkten | 02.08.2028 (verschoben) | = |
| Sanktionen Art. 50 | **€15M oder 3 % globaler Jahresumsatz** | BESTÄTIGT |

**Wasserzeichen-Technologie-Gap (TechTimes, 21. Juli 2026):** Die EU-Kommission hat die Wasserzeichen-Pflicht (C2PA-Standard) ab 02.12.2026 bestätigt — aber die Marktadoption der Erkennungstechnologie hinkt der Regulierung hinterher. Der 3-Monats-Puffer dient auch als implizites Tech-Readiness-Fenster.

*Cosmi-Implikation:* **Finale Compliance-Roadmap jetzt einfrieren.** (1) Art. 50(1) Chatbot-Offenlegung: alle Touchpoints live bis 02.08.2026 — 8 Tage. (2) Art. 50(2)/(4) Wasserzeichen/Deepfake: Prüfen ob Cosmi KI-generierte Audio/Video/Bild-Inhalte an Endkunden ausliefert (z.B. AI-Rapporte, Video-Inhalte via Schichten/HR) — Deadline 02.12.2026. (3) Annex-III-Prüfung: Deadline jetzt 02.12.2027 — Planung Q3/2026 starten. `#akut` **Modul:** AI Act / Legal / Product.

---

### 🔴 AI Act Art. 50 Chatbot-Offenlegung — 8 Tage — Final-Sprint *(02.08.2026)*

[aiactblog.nl — Article 50 Deadline](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026) | [ComplianceHub.Wiki — Art. 50](https://compliancehub.wiki/eu-ai-act-article-50-transparency-digital-omnibus-2026/) | [technology.org — What Applies Aug 2](https://www.technology.org/2026/07/17/eu-ai-act-what-actually-applies-on-2-august-2026/)

**Was ab 02.08.2026 Pflicht ist:**

- **Art. 50(1):** Chatbots, virtuelle Assistenten, Voice Agents, Customer-Service-Automation, E-Mail-Automations → beim **ersten Kontakt** muss offengelegt werden, dass der Nutzer mit KI interagiert. Das System muss so designt sein, dass die Offenlegung automatisch und unumgehbar erfolgt.
- **Art. 50(3):** Deepfake-Bild/Video/Audio-Generierung muss als maschinell erzeugt kenntlich gemacht werden.
- *Nicht* ab 02.08: Art. 50(2)/(4) Wasserzeichen/Content-Labeling — dafür gilt die 3-Monats-Übergangsregel bis 02.12.2026.

Enforcement: Marktüberwachungsbehörden in allen 27 EU-Staaten, keine zentrale EU-Behörde. DE: Bundesnetzagentur.

*Cosmi-Implikation:* **8 Tage.** GO/NO-GO-Check: (a) App-Widget / KI-Assistent im CRM-Core, (b) AI-Telefon-Dialer-Assistent, (c) Helpdesk-Chatbot, (d) Formulare-KI, (e) API-Kunden die Cosmi-KI einbetten. Alle müssen Art.-50(1)-konform sein. Bußgeld bis €15M oder 3 % Jahresumsatz. `#akut → bis 02.08.2026` **Modul:** AI Act / Legal / Product.

---

## NIS2

### 🔴 NIS2 BSI-Registrierung — 6 TAGE — 31. Juli 2026 — KEINE WEITERE VERLÄNGERUNG *(KW30 KRITISCH-COUNTDOWN)*

[Creditreform Compliance — letzte Frist](https://www.creditreform-compliance.de/aktuelles/nis2-das-bsi-setzt-die-letzte-frist-registrierung-bis-zum-31-juli-2026/) | [Solidaris — Letzte Chance](https://www.solidaris.de/aktuelles/letzte-chance-bsi-setzt-neue-frist-bis-31-juli-2026-fuer-nis-2-registrierung/) | [portal.bsi.bund.de](https://portal.bsi.bund.de)

Keine neuen Registrierungszahlen KW30. Stand Ende Mai: **~18.500 von 29.500** Unternehmen registriert. BSI hat klar kommuniziert: 31. Juli ist absolute Letztfrist. Gesetzlicher Stichtag war bereits 6. März 2026 — wer jetzt nicht registriert, befindet sich seit März im Verzug.

**BSI-Bußgeldstruktur (final):**

| Kategorie | Maximales Bußgeld |
|-----------|-------------------|
| Wichtige Einrichtungen | bis **€500.000** (§ 60 BSIG) |
| Essential Entities | bis **€10.000.000 oder 2 %** globaler Jahresumsatz |
| GF-Haftung §38 BSIG | persönlich, unbeschränkt |

*Cosmi-Implikation:* **Mit Puffer bis Dienstag 28. Juli registrieren.** Falls noch nicht geprüft: Prüfen ob Cosmi als Managed-IT-Dienst, Cloud-Anbieter, SaaS-Plattform oder digitale Infrastruktur unter NIS2 fällt (Anhang I/II BSIG). Im Zweifelsfall registrieren — Nicht-Registrierung ist das grösste Risiko. `#akut → bis 28. Juli` **Modul:** NIS2 / Legal / Management.

---

### BSI C5:2026 — Neues Cloud-Sicherheits-Anforderungskatalog (Version 1.0.1) — Audit ab Juni 2027 *(KW30 NEU)*

[BSI C5:2026](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf) | [GRClab — C5:2026 Breakdown](https://grclab.com/blog/c5-2026-the-new-standard-for-cloud-security-is-here) | [CertHub — Audit Readiness](https://www.certhub.de/en/blog-articles/bsi-c5-2026-audit-readiness-guide-cloud-providers)

BSI C5:2026 ersetzt C5:2020 und gilt für Audit-Engagements ab **01. Juni 2027**. Jetzt Audit-Vorbereitungen starten.

**Neue Anforderungsbereiche:**

| Bereich | Änderung |
|---------|---------|
| **Post-Quanten-Kryptografie** | Erstmals explizit als Anforderung verankert |
| **Container-Management** | Deutlich detailliertere Anforderungen als C5:2020 |
| **Confidential Computing** | Neuer eigenständiger Anforderungsbereich |
| **EUCS-Alignment** | Enge Abstimmung mit EU-Zertifizierungsschema |

*Cosmi-Implikation:* Als DACH-SaaS-Anbieter mit Kunden in regulierten Sektoren (Healthcare, Finanz, öffentliche Hand) wird C5-Zertifizierung zunehmend zur Vertriebsvoraussetzung. Gap-Analyse gegen C5:2026 jetzt starten — 10 Monate bis erste Audit-Relevanz (Juni 2027). `#beobachten` **Modul:** NIS2 / Security / Infra.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche — keine neuen Regelungen KW30

Fristen-Status (unveraendert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) — Pflicht |
| bis 31.12.2026 | Übergangsfrist **Versand** — Papier/PDF (mit Zust.) noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz > €800k Vorjahresumsatz |
| ab 01.01.2028 | **Versandpflicht** alle B2B |
| dauerhaft | Kleinunternehmer §19 UStG — befreit |

Format-Klarstellung KW30: ZUGFeRD auf EN-16931-Profil ist äquivalent zu XRechnung 3.0.2 — kein separates Zertifizierungsaufwand bei ZUGFeRD-Nutzung.

> **EU Data Act-Reminder:** Ab **12. September 2026 (48 Tage)** gelten SaaS/Cloud-Datenzugangs- und Switching-Pflichten — auch für Cosmi-Buchhaltung/CRM. Export-APIs auf Data-Act-Konformität prüfen (max. 2 Monate Kündigungsfrist, Switching ohne Barrieren). `#followup`

---

## ArbZG / Arbeitsrecht

### BMAS-Gesetzentwurf zur ArbZG-Reform erwartet Herbst 2026 *(KW30 Statusupdate)*

[Hogapage — Merz erwartet ArbZG im Herbst](https://www.hogapage.de/nachrichten/arbeitswelt/reportagen/merz-erwartet-arbeitszeitgesetz-im-herbst/) | [LTO — Bas kündigt Entwurf an](https://www.lto.de/recht/nachrichten/n/bas-kuendigt-gesetzentwurf-arbeitszeitgesetz-an-juni-2026) | [clockin Blog — Referentenentwurf](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026)

Bundeskanzler Merz bestätigt Herbst 2026 als Zeitplan für den BMAS-Gesetzentwurf (Arbeitsministerin Bärbel Bas). Sozialpartnerdialog (Juli–Oktober 2025) ohne Einigung beendet — Positionen "sehr weit auseinander" (BMAS). Kernreform: Ablösung der täglichen 8h-Maximalgrenze durch **wöchentliche Höchstarbeitszeiten** im Einklang mit EU-Arbeitszeitrichtlinie.

Elektronische Arbeitszeiterfassung: Teil des Entwurfs. Übergangsfrist nach Unternehmensgröße geplant.

*Cosmi-Implikation:* Cosmi-Schichten-Modul: Wochenarbeitszeit-Tracking (statt täglicher Überschreitungsprüfung) muss technisch vorbereitet werden. Jetzt Feature-Anforderungen definieren, bevor Gesetz verabschiedet wird. Elektronische Zeiterfassung ist voraussichtlich Pflicht — Schichten-Modul als Compliance-Tool positionieren. `#beobachten → Herbst 2026 watchlist` **Modul:** ArbZG / Legal / Schichten.

---

## eIDAS

### EUDIW Deutschland-Launch 02.01.2027 (161 Tage) — Keine neuen ARF-Updates KW30

[eideasy.com — EUDIW Status by Country July 2026](https://www.eideasy.com/blog/eu-digital-identity-wallets-july-2026) | [corbado.com — EUDI Wallet 2026 Rollout](https://www.corbado.com/blog/eudi-wallet-2026-deadline-rollout-eic-2026)

Deutschland bestätigt Launch-Datum **02. Januar 2027**. Sandbox aktiv (Kategorie 1). ARF v1.5 weiterhin aktueller operativer Stand. ARF v1.6 als inkrementelles Update im nächsten Jahr erwartet. Keine neuen technischen Specifications KW30.

*Cosmi-Implikation:* **161 Tage bis Deutschland-Launch.** Relying-Party-Integration-Anforderungen aus ARF v1.5 jetzt evaluieren. Q4/2026-Sprint für EUDIW-Vorbereitung einplanen (Vertraege-Modul, e-Signing, Formulare). `#beobachten` **Modul:** eIDAS / Product.

---

## BSI-Warnings — KW30 (19.–25. Juli 2026)

> **KW30-Überblick:** Keine neuen Cosmi-Stack-spezifischen Kritisch-Advisories in KW30 identifiziert. **KW29-Advisories (PostgreSQL, Samba, NGINX-Plus, nginx-ui, Ubuntu) bleiben weiterhin offen falls noch nicht gepatcht.** BSI C5:2026 als neuer Compliance-Standard relevant (siehe NIS2-Abschnitt).

### Status offener KW29-Kritisch-Advisories

| Advisory | Produkt | Status | Massnahme |
|----------|---------|--------|-----------|
| PostgreSQL 18.4/17.10/16.14/15.18/14.23 | **PostgreSQL** | Patch seit 16.07. | Sofort updaten |
| WID-SEC-2026-1686 | **Samba** | Offen | Sofort patchen |
| WID-SEC-2026-2383 | **NGINX Plus** | Offen | KW28+KW29 Advisories zusammen |
| WID-SEC-2026-2390 | **nginx-ui** | Offen | Root-Exec-Risk — deaktivieren oder patchen |
| WID-SEC-2026-2393 | **Ubuntu** (ubuntu-pro-client) | Offen | Patchen |

> Falls PostgreSQL und Samba KW29 noch nicht gepatcht: jetzt umgehend. Cosmi läuft auf PostgreSQL als Primär-DB — dieser Patch hat höchste Priorität.

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 15). **AI-Omnibus (Reg. 2026/1744) via WebSearch verifiziert** — OJ L 24.07.2026 bestätigt.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 14). Hennemann-Wahl und Durchsetzungsschwerpunkte via WebSearch abgedeckt.
- **BSI Pressemitteilungen** — RSS 404 (Woche 14). C5:2026 via BSI-Direktdownload und WebSearch abgedeckt.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 15). Keine neuen XRechnung-Regelungen KW30.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 15). ArbZG-Reform über WebSearch abgedeckt.
- **ENISA** — RSS 404 (Woche 12). NIS360-Umfrage via WebSearch (ENISA.eu).
- **EDPB Newsroom** — RSS 403 Forbidden. EDPB-Inhalte (Anonymisation Guidelines, Breach Template) via WebSearch.
- **EDPS** — 403 Forbidden.
- **noyb** — RSS zugänglich; keine neuen Klageinreichungen KW30.

> **Wartungshinweis (Woche 15):** 6×404 + 2×403 persistent. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — innerhalb der nächsten 8 Tage

- [ ] **NIS2 BSI-Registrierung — bis 28. Juli (mit Puffer)** — Absolute Letztfrist 31. Juli, mit Sicherheitspuffer bis Dienstag 28. Juli. Falls noch nicht registriert: jetzt. Falls Einstufung unklar: Rechtsberatung sofort. `#nis2 #legal #management` → **bis 28. Juli**
- [ ] **AI Act Art. 50(1) Chatbot-Offenlegung — Go/No-Go bis 01.08.2026** — Alle KI-Interaktions-Touchpoints: App-Widget, Dialer-KI, Helpdesk-Bot, Formulare-KI, API-Endpunkte. Beim ersten Kontakt muss KI-Natur offengelegt werden. Frist: **02.08.2026**. `#aiact #legal #product` → **bis 01.08.2026**
- [ ] **AI Act Omnibus finale Compliance-Roadmap einfrieren (Reg. 2026/1744 in Kraft 27.07.)** — Art. 50(2)/(4) bis 02.12.2026: Prüfen ob Cosmi KI-generierten Audio/Video/Bild-Content an Endkunden ausliefert. Annex-III-Planung bis 02.12.2027: welche Cosmi-Module könnten als Hochrisiko-KI klassifiziert werden? `#aiact #legal #product` → **bis 01.08.2026**

### 🟡 Followup (KW31+)

- [ ] **DPF SCC-Fallback-Audit abschliessen** — US-SaaS-Transfers inventarisieren (Intercom, Google Analytics, Stripe etc.), SCCs als Primärmechanismus dokumentieren, Supplementary Technical Measures evaluieren. Schrems-III-Klage kann binnen Wochen kommen. `#dsgvo #legal #infra`
- [ ] **EDPB Data-Breach-Notification-Template — bis 05.08.** — Template herunterladen, Incident-Response-SOP abgleichen, Lücken schliessen. Konsultation schliesst 05.08.2026. `#dsgvo #security`
- [ ] **EU Data Act — 48 Tage (12.09.2026)** — Export-APIs und Daten-Portabilität in CRM, Buchhaltung, Schichten auf Data-Act-Konformität prüfen (max. 2 Monate Kündigungsfrist, Switching ohne Barrieren, keine Switching-Gebühren). `#legal #product #infra`
- [ ] **EDPB Anonymisation Guidelines 02/2026 lesen** — 3-Kriterien-Test gegen Cosmi-Anonymisierungsimplementierungen prüfen. Consultation bis 30.10.2026 — eigene Implementierung ggf. kommentieren. `#dsgvo #legal`
- [ ] **BfDI Hennemann — KI-im-HR-Prüfung (bis Oktober 2026)** — Schichten-Modul und CRM auf KI-gestützte Entscheidungen mit HR-Bezug prüfen. Art. 22 DSGVO (automatisierte Entscheidungsfindung) sicherstellen. `#dsgvo #legal`
- [ ] **BSI C5:2026 Gap-Analyse starten** — Neuer Standard gilt für Audits ab 01.06.2027. Post-Quanten-Kryptografie, Container-Mgmt, Confidential Computing. Für DACH-B2B-Kunden zunehmend als Nachweis gefordert. `#nis2 #security #infra`
- [ ] **ArbZG-Reform Watch (Herbst 2026)** — BMAS-Entwurf erwartet. Schichten-Modul: Wochenarbeitszeit-Tracking vorbereiten, Zeiterfassung-Compliance als Feature-Argument positionieren. `#arbzg #product #schichten`
- [ ] **EUDIW Relying-Party-Vorbereitung (161 Tage bis 02.01.2027)** — ARF v1.5 lesen, Integration-Anforderungen für Vertraege/Formulare/e-Signing evaluieren. Q4-Sprint einplanen. `#eidas #product`
- [ ] **ENISA NIS360 2026 — Umfrage prüfen** — Falls Cosmi als Essential Entity oder High-Criticality-Entity in NIS2-Scope: Teilnahme an ENISA-NIS360-Umfrage. `#nis2 #legal`
- [ ] **`sources/_regulation.yaml` Pflege (Woche 15)** — 6×404 + 2×403 persistent. EDPB-Direkt-Scraping-Fallback testen. `#maintenance`
