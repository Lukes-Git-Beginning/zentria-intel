---
date: 2026-09-19
type: regulation
runtime_minutes: 21
items_scanned: 62
items_relevant: 11
---

# Regulation-Sweep KW38/2026 (Sa 19. September)

## BSI-Warnings (CVE-Filter: postgres, crm, saas, gitlab, openssl)

### GitLab — CVSS 10.0 / 9.9 — CISA KEV — Aktiv exploitiert

- [CVE-2026-85706 — CVSS 10.0 — GitLab Path Traversal — Unauthenticated Arbitrary File Read](https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild/) — **Cosmi-Implikation:** Unauthentizierter Angreifer liest beliebige Dateien (Secrets, Tokens, Config) via einzelnen HTTP-Request. Gilt für GitLab CE/EE bis 19.1.7/19.2.5/19.3.1. CISA KEV 11.09.2026, aktive internet-weite Probing-Aktivität seit 11.09. **Sofortpatch auf 19.1.8 / 19.2.6 / 19.3.2.** → `[Infra, Security, CI/CD]` **AKUT**
- [CVE-2026-87719 — CVSS 9.9 — GitLab EE Insecure Deserialization — RCE](https://blog.rankiteo.com/git1789130145-gitlab-vulnerability-september-2026/) — Cosmi-Implikation: Code-Execution im GitLab-Backend. Mitigation: Patch wie oben. → `[Infra, Security]` **AKUT**

### OpenSSL — BSI WID-SEC-2026-1852

- [CVE-2026-34180 — OpenSSL d2i_X509 Out-of-Bounds — DoS / Memory Disclosure](https://vuldb.com/vuln/369570) — Cosmi-Implikation: Remote-DoS oder Memory-Leak in TLS-Stack. CVSS ADP CISA: 7.5. Betroffen: OpenSSL ≤3.0.20/3.4.5/3.5.6/3.6.2/4.0.0. Patch im nächsten Maintenance-Window. → `[Infra, Security, Backend]` **Followup**

### PostgreSQL 14 — EOL-Eskalation KW38

- [PostgreSQL 14 EOL 12.11.2026 — 54 Tage — 14.24 ist LETZTER Patch — kein 14.25 mehr](https://www.herodevs.com/blog-posts/postgresql-14-eol-nov-2026-44-cves-this-year-one-patch-left) — Cosmi-Implikation: 44 CVEs in 2026 YTD; nach EOL kein Sicherheitspatch mehr. 14.24 (13.08.2026) ist confirmed letztes Release. Quartalspatch-Zug kommt erst nach EOL — **14.25 erscheint nicht mehr.** Upgrade auf PostgreSQL 17 ist P0. → `[Infra, DB]` **AKUT (Eskalation von Followup)**

---

## DSGVO / Datenschutz

### EDPB Plenum 17.09.2026

- [EDPB Plenum 17.09.2026 — Breach-Notification-Template finalisiert — Implementierungs-Timeline entschieden](https://www.cnil.fr/en/edpb-meets-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification-template) — Cosmi-Implikation: Gemeinsames Breach-Notification-Template (7 Sektionen, 126 Felder) gilt für alle EU-DPAs. Consultation-Phase endete 05.08. Plenum hat Implementierungs-Timeline festgelegt (offizielle Minutes ausstehend, ~2-3 Wochen). Cosmi SOP-Alignment mit Template-Struktur überfällig seit KW35. → `[DSGVO, Legal, Security]` **AKUT**

### CNIL EXTIA — Carry-over KW37 (Priorität unverändert AKUT)

- [CNIL EXTIA €300.000 — Art. 12+17 DSGVO — Löschanfragen — CRM-Direktimplikation](https://www.edpb.europa.eu/news/failure-to-respect-the-rights-of-individuals-the-cnil-fined-extia-300-000-eur_en) — 265 Löschanfragen unbearbeitet. Cosmi verarbeitet gleiche Datenkategorien (Leads, Kontakte, Kandidaten). Maßnahmen noch offen: Intake-Kanal, 1-Monats-Frist-Tracking in CRM-Core, Audit-Log. → `[CRM-Core, DSGVO, Legal]` **AKUT**

### GDPR-Enforcement-Signal: Uber €825 Mio.

- [Uber €825 Mio. Bußgeld August 2026 — Art. 44ff. EU→US-Transfer](https://www.enforcementtracker.com/) — Cosmi-Implikation: Größtes Einzel-Bußgeld 2026. DPA-Fokus auf US-Transfers bleibt hoch. US-SaaS-Transfer-Inventar muss aktuell bleiben. → `[DSGVO, Legal, Infra]` **Beobachten**

### DPF / Schrems III — Carry-over Woche 12

- [DPF Schrems III — keine CJEU-Klage KW38 — DPF formal valide](https://globaldatashield.com/blog/eu-us-data-privacy-framework-2026) — noyb-Brief 30.06.2026 an EC (FTC-Unabhängigkeit) unbeantwortet. DPF überstand EU General Court Sept. 2025. SCC-Fallback-Audit weiterführen. → `[DSGVO, Legal, Infra]` **Beobachten**

---

## AI Act

### EUR-Lex / KoKIVO

- [AI Act Art. 50(2) — Watermarking-Deadline 02.12.2026 — 74 Tage — Enforcement-Woche 7](https://artificialintelligenceact.eu/transparency-rules-article-50/) — Cosmi-Implikation: Machine-readable Marking für KI-generierte Inhalte muss bis 02.12. implementiert sein. Chatbot-Disclosure + Deepfake-Labeling bereits aktiv seit 02.08.2026. KoKIVO bisher keine öffentlichen Verfahren (Woche 7). Fines: bis €15 Mio. oder 3% Jahresumsatz. Cosmi muss klären: welche AI-Outputs sind watermarking-pflichtig? → `[AI Act, Legal, Product]` **Followup**

---

## NIS2

### BSI / ENISA

- [NIS2 BSI-Prüfungen aktiv — OpenKRITIS Konferenz 28.09.2026 Siegburg](https://skill-sprinters.de/blog/compliance/nis2-bsi-pruefung-2026-was-mittelstand-vor-bussgeldern-schuetzt/) — Cosmi-Implikation: BSI inspiziert aktiv Mittelstand seit Mai 2026. NIS2UmsuCG gilt seit 06.12.2025 ohne Übergangsfrist. OpenKRITIS Jahreskonferenz am 28.09. → Sektorale Handlungsempfehlungen nächste Woche erwartet. Cosmi SaaS könnte als "wichtige Einrichtung" qualifizieren — Selbstbewertung ausstehend. → `[NIS2, Security, Infra]` **Beobachten**
- ENISA EUMSS v1.1 Konsultation geschlossen 13.09.2026 — Feedback-Auswertung läuft, Ergebnisse Q4/2026. Kein Handlungsbedarf KW38.

---

## XRechnung / e-Rechnung / GoBD

Keine neuen Regelungen in KW38. 2026 verbleibt Übergangsjahr: Empfangspflicht aktiv seit 01.01.2025, Versandpflicht optional bis Ende 2026 (mit Zustimmung). Ab 2027 für Unternehmen >800k Vorjahresumsatz: ausschließlich E-Rechnung im B2B. GoBD: XML-Originale 10 Jahre unveränderbar archivieren.

---

## ArbZG / Arbeitsrecht

Keine neuen BMAS-Pressemitteilungen in KW38. Referentenentwurf zur elektronischen Arbeitszeiterfassung läuft weiter im Gesetzgebungsverfahren. Keine neuen Fristen oder Pflichten.

---

## eIDAS

- [DIdG Digitale Identitätengesetz — Erste Bundestag-Lesung 23.09.2026 (KW39)](https://www.bundestag.de/dokumente/textarchiv/2026/kw39-de-digitale-identitaetengesetz-1211256) — Cosmi-Implikation: Erste Lesung am kommenden Mittwoch, Ausschuss Digitales und Staatsmodernisierung federführend. EU-Deadline EUDIW: 24.12.2026 (96 Tage). DE-Start Q1 2027 (105 Tage). Cosmi muss als Relying Party EUDIW-Anbindung in Q4-Sprint einplanen (Formulare, Vertragsabschluss). → `[eIDAS, Product, Vertraege]` **Followup**

---

## Stille Bereiche

- **BfDI**: RSS-Feed weiterhin nicht erreichbar (404). Keine Pressemitteilungen KW38 via Websearch gefunden.
- **EUR-Lex**: Feed nicht erreichbar (404). Keine relevanten COM-Dokumente zu Cosmi-Themen KW38 via Websearch.
- **BMAS/ArbZG**: Keine neuen Pressemitteilungen KW38.
- **noyb RSS**: Feed nicht erreichbar. Keine Neuigkeiten zu Schrems III KW38.

---

## Cosmi-Action-Items

- [x] (Status) NGINX CVE-2026-42533 (CVSS 9.2) aus KW37 — Patch-Status prüfen: 1.31.3 mainline / 1.30.4 stable
- [x] (Status) Linux Kernel CVE-2026-53362 CISA KEV aus KW37 — Patch-Status prüfen (Deadline BOD 26-04 überfällig)
- [ ] **AKUT** GitLab auf 19.1.8 / 19.2.6 / 19.3.2 patchen — CVE-2026-85706 CVSS 10.0, aktiv exploitiert (CISA KEV)
- [ ] **AKUT (P0 eskaliert)** PostgreSQL 14 → 17 Upgrade vor 12.11.2026 (54 Tage) — 14.24 ist letzter Patch
- [ ] **AKUT** DSGVO Löschanfragen-SOP in CRM-Core implementieren (CNIL EXTIA Carry-over KW37)
- [ ] **AKUT** Cosmi Incident-Response SOP an EDPB Breach-Notification-Template (7 Sektionen) ausrichten — Minutes abwarten, dann anpassen
- [ ] **Followup** AI Act Art. 50 Watermarking-Implementierung (74 Tage bis 02.12.2026) — Klärung: welche Cosmi-AI-Outputs sind marking-pflichtig?
- [ ] **Followup** DIdG erste Lesung 23.09. verfolgen — EUDIW-Anforderungen für Q4-Sprint (Relying Party)
- [ ] **Followup** OpenSSL CVE-2026-34180 (WID-SEC-2026-1852) im nächsten Maintenance-Window patchen
- [ ] **Beobachten** NIS2 Selbstbewertung: qualifiziert Cosmi als "wichtige Einrichtung"? (BSI-Prüfungen aktiv)
