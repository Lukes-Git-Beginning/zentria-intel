---
date: 2026-09-12
type: regulation
runtime_minutes: 17
items_scanned: 68
items_relevant: 12
sources_live_rss: 2
sources_ok_list: [bsi-warnungen, edpb-newsroom-partial]
sources_403_list: [oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
sources_supplemented_websearch: 10
kw: 37
---

# Regulation-Sweep KW37/2026 (Sa 12. September)

> **KW37-Scope:** 7. – 12. September 2026. Referenz-Sweep: KW36 (5. September). WebSearch-Supplements: 10. RSS-Live: BSI-WID (3 neue Cosmi-Stack-Treffer: NGINX Critical + Linux Kernel Critical + Redis HIGH); EDPB-Feed (2 Items: CNIL EXTIA + CNIL Hôpital Loire).
>
> **Woche mit drei direkten Cosmi-Stack-Security-Alarmen und einem DSGVO-Compliance-Signal.** KW37 bringt NGINX CVSS 9.2 (unauthenticated RCE — kein Patch eingespielt = Remote-Takeover möglich), einen aktiv exploitierten Linux-Kernel-CVE in der CISA KEV, ein HIGH-Advisory für Redis sowie das CNIL-Urteil gegen EXTIA mit direkter Cosmi-Implikation: CRM-Löschanfragen-Workflows müssen nachweislich funktionieren (Art. 12 + 17 DSGVO). ENISA EUMSS-Konsultation schloss am 13. September — keine Ergebnisse diese Woche. EDPB Plenum 17. September (5 Tage) — Breach-Template-Entscheidung erwartet.
>
> **🔴 NGINX: CVSS 9.2 — Unauthenticated Heap Buffer Overflow / RCE — BSI WID-SEC-2026-1995/2383 — sofort patchen**
>
> **🔴 Linux Kernel: CVE-2026-53362 — CISA KEV — aktiv exploitiert — Privilege Escalation — sofort patchen**
>
> **🟡 Redis: HIGH — CVE-2026-66373 — RCE via RESTORE double-free (authenticated) — auf Redis 8.8.0 upgraden**
>
> **🟡 CNIL EXTIA €300k (Sept 9): CRM-Löschanfragen-Workflow — direkte Cosmi-CRM-Implikation**

---

## DSGVO / Datenschutz

### 🟡 CNIL fines EXTIA €300.000 — Löschanfragen-Failure — Art. 12 + 17 DSGVO — direkte CRM-Implikation *(KW37 Neu)*

[EDPB Meldung — CNIL EXTIA](https://www.edpb.europa.eu/news/failure-to-respect-the-rights-of-individuals-the-cnil-fined-extia-300-000-eur_en) | [MLex — EXTIA Erasure](https://www.mlex.com/mlex/articles/2522938/extia-faces-300-000-french-gdpr-fine-over-erasure-request-failures) | [DSGVO-Portal — EXTIA Fine](https://www.dsgvo-portal.de/gdpr-fines/gdpr-fine-against-extia-2026-09-09-FR-5275.php) | [Measured Collective — HR Lessons](https://measuredcollective.com/cnil-fines-extia-300000-hr-erasure-requests/)

CNIL-Bescheid vom **9. September 2026** (Entscheidung vom 21. Juli 2026). EXTIA, eine IT- und Engineering-Dienstleistungsfirma, erhielt €300.000 Bußgeld wegen systematischem Versagen bei der Bearbeitung von Löschanfragen:

| Kennzahl | Wert |
|----------|------|
| Löschanfragen insgesamt 2024 | 265 |
| Nicht oder unzureichend bearbeitet | >75% |
| Ohne jede Reaktion | 166 |
| Unbearbeitet | 12 |
| Verspätet (teils Monate nach Frist) | 27 |
| Einschlägige DSGVO-Artikel | Art. 12 (Transparenz) + Art. 17 (Löschrecht) |

Erschwerend: CNIL hatte EXTIA bereits zweimal zuvor auf seine Pflichten hingewiesen. Bußgeld wegen "Verletzung wesentlicher Grundsätze zu den Rechten betroffener Personen."

*Cosmi-Implikation:* Direkter CRM-Kontext. Cosmi CRM verwaltet Kandidaten- und Kundendaten (Leads, Contacts, Deals) — genau der Datenbestand, der in EXTIA-Konstellation betroffen war. Der kritische Punkt: **nicht das Speichern ist das Problem, sondern das fehlende Workflow-Tracking von Löschanfragen**. Cosmi-CRM braucht: (1) Eingangskanal für Löschanfragen, (2) Frist-Tracking (1 Monat nach Art. 12), (3) Audit-Log des Ergebnisses. Falls nicht vorhanden: P1-Ticket. `#akut → sofort prüfen` **Modul:** CRM-Core / DSGVO / Legal.

---

### CNIL fines Hôpital Privé de la Loire €500.000 — Health Data Breach — Sept 9 *(KW37 Neu)*

[EDPB Meldung — CNIL Hôpital Loire](https://www.edpb.europa.eu/news/health-data-breach-the-cnil-fined-hopital-prive-de-la-loire-500-000-eur_en)

CNIL-Bußgeld **9. September 2026** wegen Health-Data-Breach (Art. 9 DSGVO — besondere Datenkategorien). Kein unmittelbarer Cosmi-Bezug — Cosmi verarbeitet keine Gesundheitsdaten per Default. Kontextueller Hinweis: CNIL und andere DPAs weiterhin aktiv im Enforcement, insbesondere Art. 9-Kategorien und Breach-Reaktionen.

*Cosmi-Implikation:* Keine Direktwirkung. Incident-Response-SOP weiterhin überfällig (→ EDPB Breach Template Plenum 17.09.). `#beobachten` **Modul:** DSGVO / Legal / Security.

---

### 🟡 DPF Schrems III — keine CJEU-Klageeinreichung — Carry-over Woche 11 *(KW37 unverändert)*

[activeMind.legal — DPF Supreme Court](https://www.activemind.legal/guides/dpf-supreme-court/) | [Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) | [DigitalSamba — DPF 2026](https://www.digitalsamba.com/blog/will-the-transatlantic-data-privacy-framework-hold) | [EuropeanMartech — DPF Status](https://europeanmartech.eu/blog/eu-us-data-privacy-framework-2026-status)

Keine Klageeinreichung durch noyb KW37. Carry-over **Woche 11** seit der Ankündigung (30.06.2026). DPF formal gültig. SCC-Fallback-Audit muss weiterlaufen.

*Cosmi-Implikation:* US-SaaS-Transfer-Inventar aktuell halten. SCC-Fallback-Audit weiterführen. `#followup → laufend` **Modul:** DSGVO / Legal / Infra.

---

### EDPB Guidelines 03/2026 — Web Scraping für Generative KI — Konsultation bis 30.10.2026 *(Carry-over — unverändert)*

[EDPB Konsultation](https://www.edpb.europa.eu/public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-generative-ai_en) | [Law & Technology](https://lawandtechnology.eu/en/edpb-anonymisation-web-scraping-generative-ai/)

Keine neuen KW37-Entwicklungen. EDPB Plenum 17.09. voraussichtlich kein Finalitätsbeschluss. Konsultation bis **30. Oktober 2026**. Lektüre weiterhin überfällig.

*Cosmi-Implikation:* Relevant für Enrichment-Pipeline und KI-Training auf externen Daten. `#followup → sofort nachholen` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB Anonymisierungsleitlinien 02/2026 — Konsultation bis 30.10.2026 *(Carry-over — unverändert)*

[Guidelines 02/2026 PDF](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf) | [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/anonymous-or-not-the-edpbs-new-draft-guidelines-on-anonymisation-102nbv5)

Keine neuen KW37-Entwicklungen. Konsultation bis **30. Oktober 2026**.

*Cosmi-Implikation:* Für Cosmi-Analytics und KI-Feature-Training auf aggregierten Kundendaten. `#beobachten → bis Oktober` **Modul:** DSGVO / Legal / AI-Features.

---

### 🟡 EDPB Breach-Notification-Template — EDPB Plenum 17. September — 5 Tage *(KW37 Deadline ESKALIERT)*

[EDPB Template Konsultation](https://www.edpb.europa.eu/public-consultations/template-for-personal-data-breach-notification_en) | [DLA Piper](https://privacymatters.dlapiper.com/2026/06/eu-edpb-common-template-for-breach-notifications-welcome-alignment-or-further-complexity/) | [National Law Review](https://natlawreview.com/article/edpb-adopts-common-data-breach-notification-template)

**Status KW37 — UPGRADE auf `deadline-5d`:** EDPB Plenum **17. September 2026** (5 Tage). Konsultation schloss 5. August — EDPB wertet Feedback aus. Das Plenum-Ergebnis könnte die Implementierungs-Timeline für alle EU-DPAs festlegen. Draft: 7 Sektionen, 126 Felder, Conditional Logic. SOP-Abgleich bis zum Plenum ist jetzt Pflicht.

*Cosmi-Implikation:* Cosmi Incident-Response-SOP mit Draft-Template abgleichen — überfällig seit KW35. `#followup → bis 16.09.` **Modul:** DSGVO / Legal / Security.

---

## AI Act

### 🟡 AI Act Art. 50(1) — Watermarking-Frist: 81 Tage bis 02.12.2026 — Enforcement Woche 6 *(KW37 — neue Frist-Eskalation)*

[CSA Research Note Art. 50](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/) | [EC Transparenz-FAQ](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | [EC Transparenz-Guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content) | [SSL.com — Art. 50 Guide](https://www.ssl.com/article/eu-ai-act-article-50-a-complete-guide-to-ai-transparency-compliance/) | [Goodwin — Not Delayed](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force)

**Art. 50(1) seit 02.08.2026 live — Woche 6.** Keine öffentlichen Bußgeldverfahren bekannt. KoKIVO bei der Bundesnetzagentur operativ. Erste formale Verfahren weiterhin für Q4/2026 erwartet.

**Neue Frist KW37:** Art. 50(1) enthält eine **4-monatige Übergangsfrist für Watermarking-Implementierung** (Kennzeichnungspflicht KI-generierter Inhalte), die am **02.12.2026** ausläuft — **81 Tage**. Bis zu diesem Datum müssen Watermarking-Mechanismen für KI-generierte Texte, Bilder, Audio und Video implementiert sein. Die Offenlegungspflichten (Chatbot-Erstkontext, Emotion-Recognition) galten von Anfang an ohne Übergangsfrist.

**Pflichten-Übersicht (Stand KW37):**
| Pflicht | Gilt seit | Übergangsfrist |
|---------|-----------|----------------|
| Chatbot / Voice-AI Erstkontext-Offenlegung | 02.08.2026 | Keine |
| Emotion-Recognition Hinweispflicht | 02.08.2026 | Keine |
| Deepfake-Kennzeichnung | 02.08.2026 | Keine |
| **Watermarking KI-generierter Inhalte** | **02.12.2026** | **81 Tage** |

*Cosmi-Implikation:* (1) Offenlegungspflichten: sofort falls Compliance-Screening noch offen. (2) Watermarking: bis 02.12.2026 implementieren — 81 Tage. Betroffene Cosmi-Module: Dialer-KI (Voice-AI), CRM-Widget, Helpdesk-Bot. `#akut → sofort (Offenlegung) + #followup → bis 02.12. (Watermarking)` **Modul:** AI Act / Legal / Product.

---

### AI Act Annex III HRAI — EC-Klassifikationsguidelines — Frist 02.12.2027 *(Carry-over — unverändert)*

[Inside Privacy — HRAI Guidelines](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-the-european-commission-publishes-draft-guidelines-on-hrais/) | [AMS — High-Risk HR Stack](https://www.amsinform.com/newsletter/the-eu-ai-act-and-your-hr-stack-whats-actually-classified-as-high-risk/)

Keine neuen KW37-Entwicklungen. Frist 02.12.2027.

*Cosmi-Implikation:* Cosmi-Schichten KI-Klassifikationsprüfung bis Q4/2026 einplanen. `#followup → Q4/2026` **Modul:** AI Act / Legal / Schichten.

---

## NIS2

### 🟡 NIS2 BSI Auditphase — stabil KW37 — keine neuen Eskalationen *(KW37 — stabil vs. KW36)*

[OpenKRITIS — DE NIS2](https://www.openkritis.de/eu/eu-nis-2-germany.html) | [Legiscope — NIS2 Enforcement Tracker](https://www.legiscope.com/blog/nis2-enforcement-tracker-2026.html) | [Advisori — BSI Auditing](https://www.advisori.de/en/blog/nis2-enforcement-2026-bsi-audit-fines)

KW37 ohne neue Eskalation. Auditphase läuft. §30 BSIG TOM-Dokumentation weiterhin gefordert.

*Cosmi-Implikation:* §30 BSIG TOM-Dokumentation aktiv vorantreiben. `#followup → TOM-Doku bis KW38` **Modul:** NIS2 / Legal / Management.

---

### ENISA EUMSS — Konsultation geschlossen 13. September 2026 — Ergebnisse ausstehen *(KW37 Status-Update)*

[ENISA — Have Your Say](https://www.enisa.europa.eu/news/have-your-say-on-the-certification-of-eu-managed-security-services) | [CSA Research — EUMSS](https://labs.cloudsecurityalliance.org/research/csa-research-note-enisa-eumss-certification-consultation-202/) | [Industrial Cyber — EUMSS](https://industrialcyber.co/managed-services/enisa-launches-draft-eumss-cybersecurity-certification-scheme-for-managed-security-services-seeks-feedback/) | [NOTIONES — Trusted MSSP](https://www.notiones.eu/2026/08/25/towards-trusted-managed-security-services-in-europe/)

**Status KW37:** Konsultationsfrist **13. September 2026 abgelaufen** (gestern). ENISA wertet Feedback der Stakeholder aus (Industrie, Behörden, Zertifizierungsstellen). Kein offizielles Ergebnis in KW37 veröffentlicht. Nächste Phase: ENISA veröffentlicht konsolidiertes Feedback und überarbeitetes Draft-Schema (Zeitlinie unbekannt).

*Cosmi-Implikation:* Konsultation abgeschlossen — falls Cosmi Security-Monitoring-Services für Kunden anbietet: EUMSS-Schema-Ergebnisse beobachten. Relevant im C5:2026 + NIS2-Supply-Chain-Kontext. `#beobachten → Q4/2026` **Modul:** NIS2 / Security / Infra.

---

### BSI C5:2026 — DACH-Zertifizierungsstandard — Audit-Pflicht ab 01.06.2027 *(Carry-over — unverändert)*

[BSI C5:2026 EN PDF](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf?__blob=publicationFile&v=7) | [GRClab — C5:2026](https://grclab.com/blog/c5-2026-the-new-standard-for-cloud-security-is-here)

Keine neuen KW37-Entwicklungen. Audit-Pflicht ab **01.06.2027**.

*Cosmi-Implikation:* Gap-Analyse starten (Container, Supply-Chain, Post-Quantum). `#followup → Q4/2026 Gap-Analyse` **Modul:** NIS2 / Security / Infra.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche KW37 — keine neuen Regelungen

[BMF FAQ e-Rechnung](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) | [truecommerce.de — Aktuelle Änderungen](https://www.truecommerce.com/de/blog/e-rechnungsstellung-in-deutschland-neueste-aenderungen-und-ergaenzungen/) | [e-rechnung.tools](https://www.e-rechnung.tools/ratgeber/e-rechnungspflicht)

Keine neuen Regelungen KW37. Fristen unverändert:

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen — aktiv |
| bis 31.12.2026 | Übergangsfrist Versand (Umsatz > €800k mit Zustimmung) |
| ab 01.01.2027 | **Versandpflicht** bei Umsatz > €800k Vorjahr |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

---

## ArbZG / Arbeitsrecht

### Stille Woche KW37 — ArbZG-Reform bleibt im Ruhezustand

[clockin.de — Reform 2026](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026) | [jusora.de — ArbZG 2026](https://www.jusora.de/wissen/arbeitszeitgesetz-reform-2026/)

Keine neuen Entwicklungen KW37. Koalitionsausschuss hat Reform aus 34-Maßnahmen-Paket ausgeschlossen (1./2. Juli 2026). Referentenentwurf feststeckend. Verabschiedung 2026 unwahrscheinlich. CJEU-Zeiterfassungspflicht gilt unabhängig.

*Cosmi-Implikation:* Monitoring auf Ruhezustand. `#beobachten → Q1/2027` **Modul:** ArbZG / Product / Schichten.

---

## eIDAS

### 🟡 EUDIW / DIdG — Bundestag-Verfahren läuft — kein Beschluss KW37 — EU-Deadline in 103 Tagen *(KW37 — stabil)*

[bmds.bund.de — DIdG](https://bmds.bund.de/service/gesetzgebungsverfahren/digitale-identitaetengesetz) | [Kabinettsbeschluss BMDS](https://bmds.bund.de/aktuelles/pressemitteilungen/detail/kabinett-beschliesst-gesetz-fuer-digitale-identitaeten) | [PayTechLaw — DIdG Key Provisions](https://paytechlaw.com/en/digital-identities-act-didg/) | [Governikus — DIdG](https://www.governikus.de/2026/06/19/digitale-identitaeten-gesetz-die-zukunft-der-digitalen-verwaltung/)

Kein Bundestag-Beschluss KW37. **103 Tage bis EU-Deadline 24.12.2026.**

| Meilenstein | Datum | Status |
|-------------|-------|--------|
| Kabinettsbeschluss DIdG | 20.05.2026 | ✅ |
| Bundestag-Lesung | laufend | Kein Beschluss KW37 |
| EU-Pflicht aller 27 Mitgliedsstaaten | 24.12.2026 | **103 Tage** |
| DE-Launch EUDIW | 02.01.2027 | **112 Tage** |

*Cosmi-Implikation:* ARF v3.0 + FCAF als technische Referenz. Q4-Sprint für Cosmi-Vertraege/Formulare einplanen. `#followup → Q4/2026` **Modul:** eIDAS / Product / Vertraege.

---

## BSI-Warnings — KW37 (7.–12. Sep. 2026)

> **KW37-Status: DREI COSMI-STACK-TREFFER — NGINX CRITICAL (CVSS 9.2), Linux Kernel CRITICAL (CISA KEV), Redis HIGH.** Daneben Go-Update (KW36-Advisories aktualisiert) und PostgreSQL JDBC (Medium). Patch-Priorität: NGINX + Linux Kernel sofort, Redis bald.

---

### 🔴 NGINX / NGINX Plus — CVSS 9.2 — Unauthenticated Heap Buffer Overflow / Remote Code Execution — BSI WID-SEC-2026-1995/2383

[B2B Cyber Security — NGINX Plus Vulnerabilities](https://b2b-cyber-security.de/en/nginx-plus-vulnerabilities-allow-DOS-and-code-execution/) | [Orca Security — CVE-2026-42533](https://orca.security/resources/blog/cve-2026-42533-nginx-heap-buffer-overflow/) | [CCB Belgium — NGINX Advisory](https://ccb.belgium.be/advisories/warning-multiple-vulnerabilities-nginx-leading-remote-code-execution-and-allowing-rate) | [CIS Advisory](https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-nginx-could-allow-for-remote-code-execution_2026-051) | [CSA Singapore — NGINX High](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2026-080/)

BSI WID-SEC-2026-1995 (Sept. 10) + WID-SEC-2026-2383 (Sept. 11), Schwere: **KRITISCH / HOCH**.

**Primäre CVE: CVE-2026-42533 — CVSS v4.0: 9.2 / v3.1: 8.1**

| Parameter | Wert |
|-----------|------|
| Angriffsvektor | Netzwerk — kein Auth erforderlich |
| Schwachstelle | Heap Buffer Overflow in `map`-Direktive (Regex, unnamed capture groups) |
| Impact | RCE (ohne ASLR) / DoS (Worker-Prozess-Crash) |
| Betroffene Versionen | NGINX Open Source 0.9.6–1.31.2; NGINX Plus < R37.0.3.1 / < R36 P7 |
| Patch | NGINX OS 1.31.3 (mainline) oder 1.30.4 (stable); NGINX Plus R37.0.3.1 / R36 P7 |
| Mitigation (temporär) | Auf named regex captures umstellen (begrenzte Wirkung) |

Weitere CVEs im Batch: CVE-2026-56434, CVE-2026-60005, CVE-2026-60065. NGINX Ingress Controller, Gateway Fabric, App Protect WAF ebenfalls betroffen.

*Cosmi-Implikation:* Falls Cosmi NGINX als Reverse Proxy / Load Balancer / Ingress Controller einsetzt (wahrscheinlich für API-Gateway oder Multi-Modul-Routing): **sofort patchen**. Internet-exponierte NGINX-Instanzen sind ohne Authentication angreifbar. `#akut → sofort` **Modul:** Infra / Security / Backend.

---

### 🔴 Linux Kernel — CRITICAL — CVE-2026-53362 — CISA KEV — aktiv exploitiert in the wild — Sept. 11

[Action1 — CVE-2026-23226 Privilege Escalation](https://www.action1.com/vulnerabilities/cve-2026-23226/) | [Northwave — Linux Kernel Privilege Escalation](https://northwave-cybersecurity.com/critical-linux-kernel-privilege-escalation) | [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | [Qualys — CVE-2026-46333](https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path)

BSI WID-SEC-2026-2640, aktualisiert **11. September 2026**, Schwere: **KRITISCH**.

**CVE-2026-53362** — Linux Kernel IPv6 Networking Subsystem:
- CISA added to Known Exploited Vulnerabilities catalog **27. August 2026**
- Federal agency remediation deadline war 30. August (CISA BOD 26-04 forensic triage)
- Lokale Privilege Escalation über IPv6 Networking Subsystem
- **Aktiv in echten Angriffen exploitiert**

*Cosmi-Implikation:* Linux-Host-Patching für alle Cosmi-Instanzen (Self-hosted Produktivumgebungen). Wenn Container-basiert: Basis-Image muss aktuelles Kernel-Patch aufweisen. `#akut → sofort` **Modul:** Infra / Security / Hosting.

---

### 🟡 Redis — HIGH — CVE-2026-66373 — RCE via RESTORE double-free (authenticated) — Sept. 11

[Redis Security Advisory — CVE-2026-66373](https://redis.io/blog/security-advisory-cve-2026-81934/) | [SentinelOne — CVE-2026-66373](https://www.sentinelone.com/vulnerability-database/cve-2026-66373/) | [GitHub Advisory GHSA-c964-568j-vxx7](https://github.com/advisories/GHSA-c964-568j-vxx7) | [Rapid7 — CVE-2026-66373](https://www.rapid7.com/db/vulnerabilities/cve-2026-66373/) | [Basefortify — Analyse](https://basefortify.eu/cve_reports/2026/07/cve-2026-66373.html)

BSI WID-SEC-2026-3077, aktualisiert **11. September 2026**, Schwere: **HOCH**.

| Parameter | Wert |
|-----------|------|
| CVE | CVE-2026-66373 |
| CVSS v3.1 | 7.5 (AV:N/AC:H/PR:L) |
| Typ | Double Free (CWE-415) via RESTORE + XGROUP DELCONSUMER |
| Auth erforderlich | Ja (Authenticated attacker, PR:L = Low Privilege) |
| Attack Complexity | Hoch (AC:H) |
| Impact | RCE möglich |
| Betroffene Versionen | Redis < 8.8.0 |
| Patch | Redis 8.8.0 |
| EPSS / CISA KEV | < 1% EPSS — nicht in KEV |
| Mitigation | `rename-command RESTORE ""` in redis.conf falls RESTORE nicht gebraucht |

Niedriges Real-World-Exploit-Risiko aktuell, aber HIGH-Klassifizierung und RCE-Potenzial erfordern zeitnahen Patch.

*Cosmi-Implikation:* Falls Cosmi Redis für Session-Caching, Queue-Backends oder Rate-Limiting einsetzt: auf Redis 8.8.0 upgraden. Bis dahin RESTORE-Befehl via Konfiguration deaktivieren falls nicht benötigt. `#followup → diese Woche` **Modul:** Infra / Security / Backend.

---

### Go/Golang — HIGH — KW37-Update der KW36-Advisories (WID-SEC-2026-0345/1006/2850)

[BSI WID-RSS](https://wid.cert-bund.de/content/public/securityAdvisory/rss)

WID-SEC-2026-0345, WID-SEC-2026-1006, WID-SEC-2026-2850 aktualisiert **11. September 2026** (HIGH). Keine neuen Go-CVEs gegenüber KW36 — Updates zu bereits bekannten Advisories. Arbitrary Code Execution, Memory Corruption, Security Bypass.

*Cosmi-Implikation:* Falls Go-Backend noch nicht gepatcht (KW36-Auftrag): sofort nachholen. `#akut → sofort falls offen` **Modul:** Infra / Security / Backend.

---

### PostgreSQL JDBC Driver — Medium — WID-SEC-2026-1754 — DoS — Sept. 11

[BSI WID-RSS](https://wid.cert-bund.de/content/public/securityAdvisory/rss) | [RedHat — RHSA-2026:3730](https://access.redhat.com/errata/RHSA-2026:3730)

BSI WID-SEC-2026-1754, Schwere: **MITTEL**. DoS-Schwachstelle im PostgreSQL JDBC Driver. Betrifft Java-Anwendungen, die über JDBC auf PostgreSQL zugreifen. Kein direkter Cosmi-Backend-Treffer (Cosmi nutzt Go-native PostgreSQL-Treiber, nicht JDBC). Relevant nur falls Cosmi Java-basierte Reporting- oder ETL-Tooling einsetzt.

*Cosmi-Implikation:* Kein direkter Treffer wenn reines Go-Backend. Tooling-Inventar prüfen. `#beobachten` **Modul:** Infra / DB.

---

### Weitere BSI-Advisories KW37

- **MongoDB WID-SEC-2026-3320** (HIGH, Sept. 11): Query-Bypass und Datenmanipulation — kein Cosmi-Stack-Treffer (PostgreSQL).
- **Docker WID-SEC-2026-2111/2602** (Medium, Sept. 11): DoS und Security-Bypass — relevant falls Cosmi Docker-basiertes Deployment nutzt. Prüfen.
- **MikroTik RouterOS WID-SEC-2026-3193** (CRITICAL, Sept. 11): Device-Takeover — kein Cosmi-Stack-Treffer.
- **Red Hat OpenShift WID-SEC-2026-1950** (Medium, Sept. 11): DoS — relevant bei OpenShift-Hosting.

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 22). Keine neuen EU-Acts via WebSearch KW37.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 21). Keine BfDI-Pressemitteilungen KW37.
- **BSI Pressemitteilungen** — RSS 404 (Woche 21). BSI-Content über WID-Feed + WebSearch abgedeckt.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 22). Keine neuen Regelungen KW37.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 22). Keine ArbZG-Neuigkeiten KW37.
- **ENISA** — RSS 404 (Woche 19). EUMSS-Konsultationsabschluss über WebSearch abgedeckt.
- **EDPB Newsroom** — RSS 403, aber 2 Items direkt abgerufen (CNIL EXTIA + CNIL Hôpital Loire, Sept. 9–11).
- **EDPS** — 403. Keine neuen EDPS-Publikationen KW37.
- **noyb** — Feed weiterhin leer. Keine CJEU-Klageeinreichung (Woche 11).

> **Wartungshinweis (Woche 22):** 6×404 + 1×403 persistent. WebSearch als Haupt-Kompensationskanal. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — sofort

- [ ] **NGINX Patch einspielen — CVSS 9.2 — Unauthenticated RCE — BSI WID-SEC-2026-1995/2383** — CVE-2026-42533 (Sept. 10/11). Alle NGINX Open Source < 1.31.3 und NGINX Plus < R37.0.3.1/R36 P7 betroffen. Kein Authentication erforderlich für Exploit. Upgrade auf NGINX OS 1.31.3 (mainline) oder 1.30.4 (stable). `#infra #security #backend` → **sofort**
- [ ] **Linux Kernel patchen — CRITICAL — CVE-2026-53362 — CISA KEV — aktiv exploitiert** — IPv6 Privilege Escalation, seit 27.08. in CISA KEV. Alle Cosmi-Produktionshosts (VMs + Container-Basis-Images) patchen. `#infra #security #hosting` → **sofort**
- [ ] **Go-Backend Sicherheitspatch — falls KW36-Auftrag noch offen** — WID-SEC-2026-0345 + WID-SEC-2026-1006 (KW37-Update Sept. 11). Arbitrary Code Execution. `#infra #security #backend` → **sofort falls offen**
- [ ] **AI Act Art. 50(1) Compliance-Screening — falls noch offen** — Woche 6. Vier KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Ausgaben). €15M/3% Bußgeldrahmen aktiv. `#aiact #legal #product` → **sofort falls offen**
- [ ] **CRM-Löschanfragen-Workflow prüfen — CNIL EXTIA-Urteil Sept. 9 — Art. 12+17 DSGVO** — EXTIA €300k wegen 75%+ Löschanfragen unbearbeitet. Cosmi-CRM verwaltet dieselben Datenkategorien (Leads, Candidates, Contacts). Prüfen: (1) Eingangskanal für Löschanfragen, (2) Frist-Tracking (1 Monat), (3) Audit-Log des Ergebnisses. Falls nicht vorhanden: P1. `#dsgvo #crm #legal` → **sofort prüfen**

### 🟡 Followup (KW37–KW38+)

- [ ] **Redis auf 8.8.0 upgraden — CVE-2026-66373 HIGH — RCE via double-free** — BSI WID-SEC-2026-3077 (Sept. 11). Authenticated attacker, AC:High. Bis Upgrade: `rename-command RESTORE ""` in redis.conf. `#infra #security #backend` → **diese Woche**
- [ ] **EDPB Breach Template — SOP-Abgleich vor EDPB-Plenum 17.09. (5 Tage)** — EDPB entscheidet Implementierungs-Timeline KW38. Draft (7 Sektionen, 126 Felder) mit Cosmi Incident-Response-SOP abgleichen — überfällig seit KW35. `#dsgvo #legal #security` → **bis 16.09.**
- [ ] **AI Act Art. 50(1) Watermarking — Frist 02.12.2026 — 81 Tage** — 4-Monats-Übergangsfrist läuft ab. Betroffene Cosmi-Module: Dialer-KI, CRM-KI-Ausgaben, Helpdesk-Bot. Watermarking-Mechanismus für KI-generierte Inhalte implementieren. `#aiact #legal #product` → **bis 02.12.2026**
- [ ] **EDPB Web Scraping Guidelines 03/2026 lesen** — war KW35-Deadline, weiterhin offen bis 30.10.2026. `#dsgvo #aifeatures` → **sofort nachholen**
- [ ] **NIS2 §30 BSIG TOM-Dokumentation abschließen** — Auditschreiben fordern Nachweise. `#nis2 #legal #security` → **bis KW38**
- [ ] **PostgreSQL 14 EOL-Migration — 61 Tage** — EOL 12.11.2026. Upgrade auf PostgreSQL 15 oder 17 als P0. `#infra #db` → **Sprint KW37/38 — P0**
- [ ] **BSI C5:2026 Gap-Analyse starten** — DACH-Enterprise-Vertragsvoraussetzung. Audit-Pflicht 01.06.2027. `#nis2 #security #infra` → **Q4/2026**
- [ ] **eIDAS DIdG + ARF v3.0 — Q4-Sprint planen** — 103 Tage bis EU-Deadline. `#eidas #product` → **Q4/2026**
- [ ] **AI Act Annex III HRAI — Cosmi-Schichten KI-Klassifikation** — EC-Guidelines offen, Frist 02.12.2027. `#aiact #legal #schichten` → **Q4/2026**
- [ ] **DPF SCC-Fallback-Audit weiterführen** — Schrems III Carry-over Woche 11. `#dsgvo #legal #infra` → **laufend**
- [ ] **ENISA EUMSS-Schema-Ergebnisse beobachten** — Konsultation schloss 13.09. Ergebnisse in Q4/2026 erwartet. `#nis2 #security` → **Q4/2026**
