---
date: 2026-09-05
type: regulation
runtime_minutes: 14
items_scanned: 95
items_relevant: 14
sources_live_rss: 2
sources_ok_list: [bsi-warnungen, edpb-newsroom-partial]
sources_403_list: [oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
sources_supplemented_websearch: 13
kw: 36
---

# Regulation-Sweep KW36/2026 (Sa 5. September)

> **KW36-Scope:** 31. August – 5. September 2026. Referenz-Sweep: KW35 (29. August). WebSearch-Supplements: 13. RSS-Live: BSI-WID (2 direkte Cosmi-Stack-Treffer); EDPB-Feed (1 Item).
>
> **Woche mit zwei Security-Alarmen und einem Konsultationsdeadline.** KW36 bringt einen massiven PostgreSQL-Patch-Batch (11 CVEs, vier davon CVSS 8.8) sowie ein HIGH-Advisory für Go — beides direkter Cosmi-Stack. Dazu: ENISA EUMSS-Konsultation schließt am 13. September (8 Tage), Policy-Landscape sonst stabil.
>
> **🔴 PostgreSQL: 11 CVEs gepatcht — 4×CVSS 8.8 — BSI-Warnung Sep 4 — 72h-Patchpflicht**
>
> **🔴 Go-Backend: HIGH Advisory BSI (Sep 4) — Arbitrary Code Execution — sofort patchen**
>
> **🟡 ENISA EUMSS-Konsultation: Frist 13. September 2026 — 8 Tage — lesen oder kommentieren**

---

## DSGVO / Datenschutz

### EDPB Ireland/DPC — Finale Entscheidung HSE (Health Service Executive) *(KW36 Neu)*

[EDPB — DPC HSE Final Decision](https://www.edpb.europa.eu/news/data-protection-commission-announces-final-decision-following-inquiry-into-the-health-service_en)

Die irische DPC hat am **3. September 2026** eine finale Entscheidung nach einer Untersuchung des irischen Health Service Executive (HSE) veröffentlicht. Gesundheitsdaten, Art. 9 DSGVO. Kein unmittelbarer Cosmi-Bezug — aber Indikator für anhaltend aktive DPC-Enforcement-Praxis (EDPB-RSS-Feed live).

*Cosmi-Implikation:* Keine Direktwirkung. Kontextueller Hinweis: Art. 9-Datenkategorien konsequent vermeiden im CRM-Kontext. `#beobachten` **Modul:** DSGVO / Legal.

---

### 🟡 DPF Schrems III — Weiterhin keine CJEU-Klageeinreichung — Carry-over Woche 9-10 *(KW36 unverändert)*

[activeMind.legal — DPF Supreme Court](https://www.activemind.legal/guides/dpf-supreme-court/) | [Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) | [Mishcon — Trump v. Slaughter](https://www.mishcon.com/news/is-this-the-end-of-the-dpf-trump-v-slaughter-and-the-potential-for-schrems-iii) | [Freshfields — DPF first challenge](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-us-data-privacy-framework-survives-its-first-judicial-challenge-but-more-are-102l4m1)

Keine Klageeinreichung durch noyb KW36. Carry-over Woche 9-10 seit der Ankündigung (30.06.2026). noyb-Brief an EC: FTC-Unabhängigkeit sei strukturell untergraben. DPF formal gültig. EU-Generalgerichtsentscheid (September 2025) bestätigte DPF nur auf Basis des Sachstands 2023 — Klagerisiko realer.

**Trigger-Chronologie:**
- 29.06.2026: US Supreme Court *Trump v. Slaughter* — FTC-Unabhängigkeit untergraben
- 30.06.2026: noyb kündigt CJEU-Klage an
- KW28–36: Keine Einreichungsbestätigung

*Cosmi-Implikation:* SCC-Fallback-Audit weiterführen. US-SaaS-Transfer-Inventar aktuell halten. `#followup → laufend` **Modul:** DSGVO / Legal / Infra.

---

### EDPB Guidelines 03/2026 — Web Scraping für Generative KI — Konsultation bis 30.10.2026 *(Carry-over — unverändert)*

[EDPB Konsultation](https://www.edpb.europa.eu/public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-generative-ai_en) | [Guidelines PDF v1.0](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf) | [LexisNexis](https://www.lexisnexis.com/en-gb/legal/news/edpb-adopts-guidelines-on-anonymisation-web-scraping-for-generative-ai-blockchain) | [Law & Technology](https://lawandtechnology.eu/en/edpb-anonymisation-web-scraping-generative-ai/)

Keine neuen KW36-Entwicklungen. Konsultation bis **30. Oktober 2026** offen. Nächstes EDPB-Plenum: **17. September 2026** (kein Finalitätsbeschluss erwartet vor Oktober). Einwilligung nach Art. 6(1)(a) nicht ausreichend für Web-Scraping im Maßstab.

*Cosmi-Implikation:* Lesen war KW35-Deadline — überfällig. Relevant für Enrichment-Pipeline und KI-Training auf externen Daten. `#followup → sofort nachholen` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB Anonymisierungsleitlinien 02/2026 — Konsultation bis 30.10.2026 *(Carry-over — unverändert)*

[Guidelines 02/2026 PDF](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf) | [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/anonymous-or-not-the-edpbs-new-draft-guidelines-on-anonymisation-102nbv5) | [RD Privacy Watch](https://www.rdprivacywatch.com/article/b5c19848-ce93-4104-976e-8c40fa01c9d8)

Keine neuen KW36-Entwicklungen. 3-Kriterien-Test (Isolation / Linkage / Inferenz). Konsultation bis **30. Oktober 2026**.

*Cosmi-Implikation:* Für Cosmi-Analytics und KI-Feature-Training auf aggregierten Kundendaten. `#beobachten → bis Oktober` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB Breach-Notification-Template — Konsultation geschlossen — EDPB entscheidet Implementierungs-Timeline *(KW36 Status-Update)*

[EDPB Template Konsultation](https://www.edpb.europa.eu/public-consultations/template-for-personal-data-breach-notification_en) | [DLA Piper](https://privacymatters.dlapiper.com/2026/06/eu-edpb-common-template-for-breach-notifications-welcome-alignment-or-further-complexity/) | [National Law Review](https://natlawreview.com/article/edpb-adopts-common-data-breach-notification-template) | [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/edpb-opens-public-consultation-on-new-personal-data-breach-notification-template)

Konsultation schloss am 5. August 2026. EDPB wertet Feedback aus und entscheidet über **Implementierungs-Timeline** für alle EU-DPAs — kein finales Template KW36. Draft: 7 Sektionen, 126 Felder, Conditional Logic, Tooltips. Nächstes Plenum 17. September 2026 — mögliches Update-Fenster.

*Cosmi-Implikation:* Draft-Template mit Cosmi Incident-Response-SOP abgleichen — weiterhin überfällig. `#followup → vor EDPB-Plenum 17.09.` **Modul:** DSGVO / Legal / Security.

---

## AI Act

### 🟡 AI Act Art. 50(1) — Enforcement LIVE — KW36 Woche 5 — kein öffentliches Verfahren — KoKIVO operativ *(KW36 — stabil)*

[CSA Research Note Art. 50](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/) | [Goodwin — Not Delayed](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) | [EC Transparenz-FAQ](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | [Bundesnetzagentur — AI](https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/AI/start_ki.html) | [GLACIS — KI-MIG Guide](https://www.glacis.io/guide-eu-ai-act-germany) | [Regulatory AI — Germany](https://www.regulatoryai.eu/ai-act-germany/)

**Art. 50(1) ist seit 02.08.2026 live — fünfte Woche.** Keine öffentlichen Bußgeldverfahren bekannt. KoKIVO bei der Bundesnetzagentur operativ. Erste formale Verfahren weiterhin für Q4/2026 erwartet. Compliance-Screening muss abgeschlossen und dokumentiert sein.

**Pflichten (unverändert):**
- Chatbots / Voice-AI: Erstkontext-Offenlegung vor erster Interaktion
- Deepfake / synthetische Medien: Kennzeichnung als KI-generiert
- Emotion-Recognition: Hinweispflicht an Betroffene

*Cosmi-Implikation:* Woche 5 ohne Eskalation. Falls Compliance-Screening noch offen: **absoluter Sofortauftrag.** €15M/3% Bußgeldrahmen vollständig aktiv. `#akut → sofort falls offen` **Modul:** AI Act / Legal / Product.

---

### AI Act Annex III HRAI — EC-Klassifikationsguidelines — HR-Software mit KI = hochriskant *(Carry-over — unverändert)*

[Inside Privacy — HRAI Guidelines](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-the-european-commission-publishes-draft-guidelines-on-hrais/) | [Crowell — HR AI 2026](https://www.crowell.com/en/insights/client-alerts/artificial-intelligence-and-human-resources-in-the-eu-a-2026-legal-overview/) | [HR-ON — EU AI Act HR](https://hr-on.com/eu-ai-act-for-hr-2026/) | [AMS — High-Risk HR Stack](https://www.amsinform.com/newsletter/the-eu-ai-act-and-your-hr-stack-whats-actually-classified-as-high-risk/)

EC Draft Guidelines (19.05.2026) weiterhin offen. Konsultation schloss 23.06.2026. Keine final-Verabschiedung KW36. Annex-III-Hochrisiko-Frist: **02.12.2027** (Omnibus Reg. 2026/1744).

**Kurzreferenz:**
| Anwendungsfall | Klassifikation |
|----------------|----------------|
| HR-Software mit KI-Screening (Lebensläufe, Skill-Matching) | Hochriskant — Annex III Nr. 4 |
| KI-Schichtplanung mit automatisierten Empfehlungen | Prüfen → potenziell hochriskant Nr. 4 |
| Helpdesk-Bot mit Human Escalation | Voraussichtlich nicht hochriskant |
| CRM Lead-Scoring ohne HR-Kontext | Voraussichtlich nicht hochriskant |

*Cosmi-Implikation:* Cosmi-Schichten KI-Klassifikationsprüfung bis Q4/2026 einplanen. `#followup → Q4/2026` **Modul:** AI Act / Legal / Schichten.

---

## NIS2

### 🟡 NIS2 BSI — Auditphase läuft — keine neuen Eskalationen KW36 — TOM-Pflicht unverändert *(KW36 — stabil vs. KW35)*

[Advisori — BSI Auditing & Fines](https://www.advisori.de/en/blog/nis2-enforcement-2026-bsi-audit-fines) | [Legiscope — NIS2 Enforcement Tracker](https://www.legiscope.com/blog/nis2-enforcement-tracker-2026.html) | [OpenKRITIS — DE NIS2](https://www.openkritis.de/eu/eu-nis-2-germany.html) | [Reed Smith — Germany NIS2](https://www.reedsmith.com/articles/germany-implements-nis2-immediate-effect-broad-scope-near-term-registration/)

KW36 ohne neue Eskalation gegenüber KW35. Auditphase läuft. EU-weit: 23 von 27 Mitgliedstaaten haben NIS2 vollständig transponiert. Erste Bußgelder: Belgien (€185.000), Italien (€450.000), Ungarn (€78.000). DE: BSI-Auditschreiben aktiv.

| Kennzahl | Stand KW36 |
|----------|------------|
| Unternehmen ohne Registrierung | ~18.500 (Frist war 06.03.2026) |
| Bußgeld besonders wichtige Einrichtungen | bis €10M / 2% globaler Umsatz |
| GF-Haftung | §38 BSIG, persönlich |
| EU-weite erste Bußgelder | Ja (BE, IT, HU) |

*Cosmi-Implikation:* Falls nicht registriert: sofort. Falls registriert: §30 BSIG TOM-Dokumentation aktiv vorantreiben — Auditschreiben fordern Nachweise. `#followup → TOM-Doku bis KW37/38` **Modul:** NIS2 / Legal / Management.

---

### 🟡 ENISA EUMSS — Konsultationsfrist läuft ab: **13. September 2026 — 8 Tage** *(KW36 DEADLINE ESKALIERT)*

[ENISA — Have Your Say](https://www.enisa.europa.eu/news/have-your-say-on-the-certification-of-eu-managed-security-services) | [Industrial Cyber — EUMSS](https://industrialcyber.co/managed-services/enisa-launches-draft-eumss-cybersecurity-certification-scheme-for-managed-security-services-seeks-feedback/) | [Certification Portal — EUMSS v1.1](https://certification.enisa.europa.eu/publications/draft-candidate-eumss-scheme-v11-public-review_en) | [NOTIONES — Trusted MSSP](https://www.notiones.eu/2026/08/25/towards-trusted-managed-security-services-in-europe/)

**Status KW36 — UPGRADE von `beobachten` auf `followup-deadline`:** Die öffentliche Konsultation zum Draft EU Managed Security Services Certification Scheme (EUMSS v1.1) schließt am **13. September 2026** — 8 Tage. Ziel: EU-weit einheitliche Zertifizierung für Managed Security Services Provider (MSSP). Verbindung: MSSP-Zertifizierung Pflicht innerhalb von 2 Jahren nach Verabschiedung für EU Cybersecurity Reserve-Teilnehmer.

*Cosmi-Implikation:* Falls Cosmi Monitoring- oder Security-Managed-Services anbietet: Draft-Schema lesen, Kommentar ggf. einreichen. Im NIS2-Supply-Chain-Kontext und BSI C5:2026-Umfeld relevant. Frist **13.09.2026**. `#followup → bis 13. September` **Modul:** NIS2 / Security / Infra.

---

### BSI C5:2026 — DACH-Zertifizierungsstandard — Audit-Pflicht ab 01.06.2027 *(Carry-over — unverändert)*

[BSI C5:2026](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_2025/C5_2025_node.html) | [C5:2026 EN PDF](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf?__blob=publicationFile&v=7) | [GRClab — C5:2026](https://grclab.com/blog/c5-2026-the-new-standard-for-cloud-security-is-here) | [CertHub — Readiness](https://www.certhub.de/en/blog-articles/bsi-c5-2026-audit-readiness-guide-cloud-providers)

C5:2026 final seit April 2026. Keine neuen KW36-Entwicklungen. Audit-Pflicht ab **01.06.2027**. Neue Schwerpunkte: Container-Management, Post-Quantum-Kryptographie, Supply-Chain-Nachweise, Confidential Computing. DACH-Enterprise-Kunden fordern Zertifizierung als Vertragsvoraussetzung.

*Cosmi-Implikation:* Gap-Analyse starten (Container, Supply-Chain, Post-Quantum). Early Adoption Q4/2026 empfohlen. `#followup → Q4/2026 Gap-Analyse` **Modul:** NIS2 / Security / Infra.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche KW36 — keine neuen Regelungen

[BMF FAQ e-Rechnung](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) | [truecommerce.de — Aktuelle Änderungen](https://www.truecommerce.com/de/blog/e-rechnungsstellung-in-deutschland-neueste-aenderungen-und-ergaenzungen/) | [IHK Dresden — e-Rechnung](https://www.ihk.de/dresden/hauptnavigation/recht-steuern/erechnung-6232764) | [e-rechnung.tools](https://www.e-rechnung.tools/ratgeber/e-rechnungspflicht)

Keine neuen Regelungen KW36. Fristen unverändert:

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen — aktiv |
| bis 31.12.2026 | Übergangsfrist Versand (Umsatz > €800k mit Zustimmung) |
| ab 01.01.2027 | **Versandpflicht** bei Umsatz > €800k Vorjahr |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

2026 bleibt entscheidendes Vorbereitungsjahr — technische Umsetzung in XRechnung/ZUGFeRD-Format jetzt fixieren.

---

## ArbZG / Arbeitsrecht

### Stille Woche KW36 — Koalitionsausschuss hat ArbZG aus 34-Maßnahmen-Paket AUSGESCHLOSSEN *(KW36 Status-Degradierung)*

[clockin.de — Reform 2026](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026) | [jusora.de — ArbZG 2026 Was gilt](https://www.jusora.de/wissen/arbeitszeitgesetz-reform-2026/) | [hrtime.de — ArbZG 2026](https://www.hrtime.de/blog/arbeitszeitgesetz-2026-alle-aenderungen/) | [energieundrecht — Referentenentwurf](https://www.energieundrecht.com/blog-arbeitsrecht-zivilrecht/arbeitszeitgesetz-reform-2026-referentenentwurf)

**KW36-Update — STATUS DEGRADIERT:** Der Koalitionsausschuss (CDU/CSU + SPD) hat am 1./2. Juli 2026 ein **34-Maßnahmen-Reformpaket** beschlossen — die **ArbZG-Reform kommt darin nicht vor**. Weder Arbeitszeiterfassungspflicht noch Wochenhöchstarbeitszeit wurden aufgenommen. Breite Koalitionsskepsis. Referentenentwurf (17.06.2026) feststeckend — Verabschiedung 2026 unwahrscheinlich.

*Cosmi-Implikation:* Cosmi-Schichten-Feature-Compliance-Argument (elektronische Zeiterfassung) verliert kurzfristigen Druck. Mittelfristig bleibt Thema relevant — CJEU-Vorgabe zu Arbeitszeiterfassung gilt unabhängig vom Gesetz. `#beobachten → Q1/2027` **Modul:** ArbZG / Product / Schichten.

---

## eIDAS

### 🟡 EUDIW / DIdG — Bundestag-Verfahren läuft — kein Beschluss KW36 — EU-Deadline in 110 Tagen *(KW36 — stabil)*

[bmds.bund.de — DIdG](https://bmds.bund.de/service/gesetzgebungsverfahren/digitale-identitaetengesetz) | [Bitkom — DIdG Stellungnahme](https://www.bitkom.org/Bitkom/Publikationen/Digitale-Identitaetengesetz) | [Governikus — DIdG](https://www.governikus.de/2026/06/19/digitale-identitaeten-gesetz-die-zukunft-der-digitalen-verwaltung/) | [netzpolitik.org — Digitale Brieftasche](https://netzpolitik.org/2026/mehr-als-ein-ausweis-das-soll-die-digitale-brieftasche-in-deutschland-koennen/) | [Corbado — Deadline 2026](https://www.corbado.com/blog/eudi-wallet-2026-deadline-rollout-eic-2026)

Kein Bundestag-Beschluss KW36. **110 Tage bis EU-Deadline 24.12.2026.**

| Meilenstein | Datum | Status |
|-------------|-------|--------|
| Kabinettsbeschluss DIdG | 20.05.2026 | ✅ |
| Bundestag-Lesung | laufend | Kein Beschluss KW36 |
| EU-Pflicht aller 27 Mitgliedsstaaten | 24.12.2026 | **110 Tage** |
| DE-Launch EUDIW | 02.01.2027 | **119 Tage** |

*Cosmi-Implikation:* ARF v3.0 + FCAF als technische Referenz. Q4-Sprint für Cosmi-Vertraege/Formulare einplanen. 119 Tage bis DE-Launch. `#followup → Q4/2026` **Modul:** eIDAS / Product / Vertraege.

---

## BSI-Warnings — KW36 (31. Aug. – 5. Sep. 2026)

> **KW36-Status: ZWEI DIREKTE COSMI-STACK-TREFFER** — PostgreSQL und Go betroffen. Beide BSI HIGH. 72h-Patchpflicht für PostgreSQL.

### 🔴 PostgreSQL — 11 CVEs gepatcht — 4×CVSS 8.8 — darunter 12 Jahre alte Logic-Flaw — BSI Sep 4

[BSI WID-SEC-2026-0409](https://wid.cert-bund.de/content/public/securityAdvisory/rss) | [LSI Bayern — WID-SEC-2026-0409](https://wid.lsi.bayern.de/portal/wid/securityadvisory?name=LSI-SEC-2026-0409) | [The Hacker News — 12-Year Flaw](https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html) | [Heise — Updates hochriskant](https://www.heise.de/en/news/PostgreSQL-Updates-patch-high-risk-security-vulnerabilities-11297673.html) | [CCB Belgium Advisory](https://ccb.belgium.be/advisories/warning-postgresql-patches-multiple-vulnerabilities-and-announces-eol-date-version-14) | [PostgreSQL Security](https://www.postgresql.org/support/security/) | [CyberKlartext — CVSS 8.8](https://cyberklartext.de/advisories/CK-052026-30220)

BSI WID-SEC-2026-0409, aktualisiert **4. September 2026**, Schwere: **HOCH**.

**11 CVEs, davon 4×CVSS 8.8:**

| CVE | CVSS | Beschreibung |
|-----|------|-------------|
| CVE-2026-6473 | 8.8 | Integer Wraparound → Heap-Undersizing → Code Execution |
| CVE-2026-6475 | 8.8 | Symlink Following → Superuser kann lokale Dateien überschreiben |
| CVE-2026-6477 | 8.8 | (Details aus Patch-Batch) |
| CVE-2026-6637 | 8.8 | Stack Buffer Overflow in refint-Contrib → Unprivileged RCE |
| CVE-2026-6471 | 7.2 | **12 Jahre alte** Logical Decoding Flaw → Replication-Role Code Execution |

**Betroffene Versionen:** PostgreSQL-Versionen vor dem aktuellen September-Patch-Release.
**BSI-Empfehlung:** Patch innerhalb **72 Stunden** einspielen.

**⚠️ PostgreSQL 14 EOL: 12. November 2026 — noch 68 Tage.** Dies ist der vorletzte oder letzte reguläre Patch-Zyklus vor EOL. Upgrade auf PostgreSQL 15 oder 17 ist jetzt nicht mehr aufschiebbar.

*Cosmi-Implikation:* Postgres-Patch sofort einspielen. Upgrade-Planung aus Sprint herauslösen und als P0 behandeln. `#akut → 72h` **Modul:** Infra / Security / DB.

---

### 🔴 Go-Backend — HIGH Advisory BSI — Arbitrary Code Execution — Sep 4

[BSI WID-SEC-2026-0345](https://wid.cert-bund.de/content/public/securityAdvisory/rss) | [BSI WID-SEC-2026-1006](https://wid.cert-bund.de/content/public/securityAdvisory/rss)

Zwei BSI-HIGH-Advisories für **Go/Golang**, aktualisiert 4. September 2026:

- **WID-SEC-2026-0345**: Mehrere Schwachstellen — "execute arbitrary code or circumvent security measures"
- **WID-SEC-2026-1006**: Memory Corruption, Arbitrary Code Execution, Security Bypass, DoS

*Cosmi-Implikation:* Falls Cosmi Go im Backend einsetzt: aktuelle Go-Version prüfen, offizielle Go-Security-Releases einspielen. `#akut → sofort` **Modul:** Infra / Security / Backend.

---

### Weitere BSI-Advisories KW36

- **Linux Kernel**: Mehrere HIGH-Advisories (DoS, Memory Corruption) — Sep 4
- **Dell Secure Connect Gateway (WID-SEC-2026-3184)**: Container Boundary Bypass, Remote Code Execution — HIGH
- Kein direkter Cosmi-Stack-Treffer (Nginx, Redis, Kubernetes) in KW36.

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 21). Keine neuen EU-Acts via WebSearch KW36.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 20). Keine BfDI-Pressemitteilungen KW36.
- **BSI Pressemitteilungen** — RSS 404 (Woche 20). BSI-Content über WID-Feed + WebSearch abgedeckt.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 21). Keine neuen Regelungen KW36.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 21). ArbZG-Reform aus Koalitionspaket ausgeschlossen (siehe oben).
- **ENISA** — RSS 404 (Woche 18). EUMSS-Deadline-Alert über WebSearch abgedeckt.
- **EDPB Newsroom** — RSS 403, aber 1 Item direkt abgerufen (DPC/HSE Sep 3).
- **EDPS** — 403. Keine neuen EDPS-Publikationen KW36.
- **noyb** — Feed weiterhin leer. Keine CJEU-Klageeinreichung (Woche 9-10).

> **Wartungshinweis (Woche 21):** 6×404 + 1×403 persistent. WebSearch als Haupt-Kompensationskanal. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — sofort / 72h

- [ ] **PostgreSQL Patch einspielen — 72h-Frist — 11 CVEs / 4×CVSS 8.8** — BSI WID-SEC-2026-0409 (4. Sep). CVE-2026-6637 ermöglicht unprivilegierten RCE; CVE-2026-6471 ist 12 Jahre alte Logical-Decoding-Lücke. Patch sofort. Parallel: PostgreSQL-14-Upgrade auf 15 oder 17 jetzt als P0 in Sprint aufnehmen — EOL 12.11. (68 Tage). `#infra #security #db` → **sofort / 72h**
- [ ] **Go-Backend Sicherheitspatch — 2 HIGH-Advisories BSI — RCE-Risiko** — WID-SEC-2026-0345 + WID-SEC-2026-1006 (4. Sep). Falls Go im Backend: aktuelle Go-Release-Version prüfen und einspielen. `#infra #security #backend` → **sofort**
- [ ] **AI Act Art. 50(1) Compliance-Screening — falls noch offen: absoluter Sofortauftrag** — Woche 5. Vier KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Ausgaben). €15M/3% Bußgeldrahmen aktiv. `#aiact #legal #product` → **sofort falls offen**

### 🟡 Followup (KW36-Deadline / KW37+)

- [ ] **ENISA EUMSS-Konsultation lesen — Frist 13. September (8 Tage)** — Draft EUMSS v1.1 vor Fristende lesen. Falls Cosmi Managed Security Services / Monitoring für Kunden anbietet: Kommentar prüfen. Relevant im C5:2026 + NIS2-Supply-Chain-Kontext. `#nis2 #security` → **bis 13.09.**
- [ ] **EDPB Breach Template — SOP-Abgleich vor EDPB-Plenum 17.09.** — Konsultation geschlossen. EDPB entscheidet Implementierungs-Timeline. Draft (7 Sektionen, 126 Felder) mit Cosmi Incident-Response-SOP abgleichen — überfällig seit KW35. `#dsgvo #legal #security` → **bis 16.09.**
- [ ] **EDPB Web Scraping Guidelines 03/2026 lesen** — war KW35-Deadline, weiterhin offen bis 30.10.2026. Enrichment-Pipeline und KI-Training. `#dsgvo #aifeatures` → **sofort nachholen**
- [ ] **NIS2 §30 BSIG TOM-Dokumentation vorantreiben** — Auditschreiben fordern Nachweise. Falls Registrierung noch offen: sofort. `#nis2 #legal #security` → **bis KW37/38**
- [ ] **PostgreSQL 14 EOL-Migration — 68 Tage** — EOL 12.11.2026. Upgrade-Pfad auf PostgreSQL 15 oder 17 jetzt als P0 fixieren. Letzter Community-Patch möglicherweise schon erfolgt. `#infra #db` → **Sprint KW37 — P0**
- [ ] **BSI C5:2026 Gap-Analyse starten** — DACH-Enterprise fordern Zertifizierung als Vertragsvoraussetzung. Audit-Pflicht 01.06.2027. `#nis2 #security #infra` → **Q4/2026**
- [ ] **eIDAS DIdG + ARF v3.0 — Q4-Sprint planen** — 110 Tage bis EU-Deadline. Enrollment-Regeln lesen. `#eidas #product` → **Q4/2026**
- [ ] **AI Act Annex III HRAI — Cosmi-Schichten KI-Klassifikation** — EC-Guidelines bestätigen HR-Software mit KI-Auswertung = hochriskant Annex III Nr. 4. Frist 02.12.2027. `#aiact #legal #schichten` → **Q4/2026**
- [ ] **DPF SCC-Fallback-Audit weiterführen** — Schrems III Carry-over Woche 9-10. US-SaaS-Transfer-Inventar aktuell halten. `#dsgvo #legal #infra` → **laufend**
- [ ] **ArbZG — Monitoring auf Ruhezustand setzen** — Koalitionsausschuss Juli 1-2 hat Reform ausgeschlossen. Verabschiedung 2026 unwahrscheinlich. CJEU-Zeiterfassungspflicht gilt unabhängig. `#arbzg #product #schichten` → **Q1/2027 wiederprüfen**
