---
date: 2026-08-15
type: regulation
runtime_minutes: 19
items_scanned: 65
items_relevant: 11
sources_live_rss: 1
sources_ok_list: [bsi-warnungen]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
sources_supplemented_websearch: 10
websearch_supplements: 10
kw: 33
---

# Regulation-Sweep KW33/2026 (Sa 15. August)

> **KW33-Scope:** 9.–15. August 2026. Referenz-Sweep: KW32 (8. August). WebSearch-Supplements: 10. RSS-Live: BSI-WID (PostgreSQL-Massenpatch, Linux Kernel CRITICAL).
>
> **Woche der BSI-Schwergewichte.** Keine neuen Policy-Explosionen in KW33 — aber PostgreSQL hat am 13. August den größten Sicherheits-Patch-Batch seiner Geschichte herausgegeben.
>
> **🔴 POSTGRESQL REKORD-CVE-BATCH — 28 SCHWACHSTELLEN, 9×ARBITRARY CODE EXECUTION (13.08.2026):** Direkter Cosmi-Datenbankstack-Treffer. 17 der 28 CVEs haben CVSS ≥ 8.0. Patch auf 18.6 / 17.11 / 16.15 / 15.19 / 14.24 — sofort. Zudem: PostgreSQL 14 EOL am 12.11.2026 (noch 89 Tage).
>
> **🔴 BSI LINUX KERNEL CRITICAL — WID-SEC-2026-2640 (14.08.2026):** Update auf Critical hochgestuft — Information Disclosure + weitere Vektoren. Alle Produktionsserver.
>
> **🟡 eIDAS ARF v3.0 ERSCHIENEN — UPGRADE VON v2.8.0:** Neue Conformance Assessment Framework. Germany + France Sandbox-Leader. Cosmi-Relying-Party-Gap-Analyse auf v3.0 aktualisieren.
>
> **⚠️ ANMELDEFRIST EDPB/EC EVENT 15.10. LÄUFT AB 28.08. — NOCH 13 TAGE:** Stakeholder-Event Datenschutz × Wettbewerbsrecht. Für Cosmi-Daten-Aggregation und KI-Features potenziell strategisch.

---

## DSGVO / Datenschutz

### 🟡 EDPB Guidelines 03/2026 — Web Scraping für Generative KI — Konsultation läuft bis 30.10.2026 *(KW33 NEU / KW32 verpasst)*

[EDPB — Guidelines 03/2026 on web scraping for generative AI](https://www.edpb.europa.eu/public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-generative-ai_en) | [PDF v1.0 (07.07.2026)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf) | [Data Matters — Sidley](https://datamatters.sidley.com/2026/07/23/what-do-the-european-data-protection-boards-web-scraping-guidelines-mean-for-ai-training-datasets/) | [Bratby.law — Summary](https://bratby.law/edpb-web-scraping-generative-ai-guidelines/) | [EDPB-Newsroom](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en)

Am 7. Juli 2026 hat der EDPB zusammen mit den Anonymisierungsleitlinien auch **Guidelines 03/2026 zum Web Scraping für generative KI** (Version 1.0) angenommen. Die öffentliche Konsultation läuft bis **30. Oktober 2026**.

**Scope:** Automatisiertes Extrahieren personenbezogener Daten aus öffentlich zugänglichen Webquellen für Entwicklung und Training von GenAI-Modellen — direkt oder über Drittanbieter / Data Broker. Die DSGVO ist anwendbar. Sonderregeln für Forschung gelten nicht automatisch.

**Kernpositionen:**
- Web-Scraping von personenbezogenen Daten = DSGVO-Verarbeitungsvorgang → Rechtsgrundlage erforderlich
- Art. 6(1)(f) Berechtigtes Interesse: strenger Test — technische Schutzmaßnahmen (robots.txt-Respekt) sind Indiz
- Scraped Datasets von Data Brokern: Abnehmer muss Rechtmäßigkeit der Erhebung verifizieren
- Keine DSGVO-Ausnahme für "öffentlich zugängliche" Daten

*Cosmi-Implikation:* Falls Cosmi KI-Features mit externen Web-Daten (Lead-Enrichment, Firmen-Profiling, Marktdaten) trainiert oder anreichert: Guidelines lesen und Rechtsgrundlagen-Assessment durchführen. Relevant für Enrichment-Pipeline, nicht für klassische CRM-Kerndaten. Konsultationsende 30.10.2026 — Feedback über Branchenverbände möglich. `#followup` **Modul:** DSGVO / Legal / AI-Features / Product.

---

### 🟡 EDPB Anonymisierungsleitlinien 02/2026 — Konsultation läuft bis 30.10.2026 *(KW31 Carry-over — unverändert)*

[Guidelines 02/2026 on Anonymisation v1.0 (07.07.2026)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf) | [Sidley — Data Matters](https://datamatters.sidley.com/2026/07/27/edpb-publishes-draft-guidelines-on-anonymisation/) | [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/anonymous-or-not-the-edpbs-new-draft-guidelines-on-anonymisation-102nbv5)

Keine neuen Entwicklungen KW33. Konsultation läuft bis 30.10.2026. 3-Kriterien-Test (Record Isolation / Linkage / Inferenz) als Maßstab für echte Anonymität.

*Cosmi-Implikation:* Relevant für interne Analysen, Reporting, KI-Feature-Training mit aggregierten Kundendaten. 3-Kriterien-Dokumentation einplanen. `#beobachten → bis Oktober` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB Breach-Notification-Template — Finalisierung ausstehend *(KW32 Carry-over)*

Konsultation schloss am 5. August 2026. EDPB wertet Feedback aus. Kein Finaldokument noch. Nationaler Implementierungszeitplan (BfDI/LDA) nicht kommuniziert.

*Cosmi-Implikation:* Draft-Template (7 Sektionen, 126 Felder) mit Cosmi-Incident-Response-SOP abgleichen. KW32-Aufgabe nachholen falls noch offen. `#followup` **Modul:** DSGVO / Legal / Security.

---

### EDPB/EC Stakeholder-Event — Datenschutz & Wettbewerb — Anmeldung bis 28.08.2026 *(KW32 Carry-over — DRINGLICH)*

[EDPB — Event-Seite](https://www.edpb.europa.eu/home_en)

Remote-Event 15. Oktober 2026. Bewerbungsfrist: **28. August 2026** — noch 13 Tage. Thema: Leitlinien zum Zusammenspiel von Datenschutzrecht und Wettbewerbsrecht.

*Cosmi-Implikation:* Künftige Leitlinien könnten Nutzung von Kundendaten für Benchmarking, Marktanalyse oder KI-Training wettbewerbsrechtlich einschränken. Teilnahme einplanen. `#followup → bis 28.08.` **Modul:** DSGVO / Legal.

---

### 🟡 DPF Schrems III — Weiterhin keine Klageeinreichung — Carry-over Woche 3 *(KW33 unverändert)*

[Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) | [activeMind.legal](https://www.activemind.legal/guides/dpf-supreme-court/) | [Mishcon — Trump v. Slaughter](https://www.mishcon.com/news/is-this-the-end-of-the-dpf-trump-v-slaughter-and-the-potential-for-schrems-iii)

Weiterhin keine formale Klageeinreichung durch noyb beim CJEU. DPF formal gültig. noyb bereitet Klage vor ("binnen Wochen"). CJEU C-703/25 P (Latombe) läuft. Trigger: US Supreme Court Trump v. Slaughter (29.06.2026) — FTC-Unabhängigkeit untergraben.

*Cosmi-Implikation:* SCC-Fallback-Audit weiterführen. US-SaaS-Transfers inventarisieren. Schrems-III-CJEU-Urteil in 2–3 Jahren, aber DPF-Risiko ab Einreichungszeitpunkt erhöht. `#followup` **Modul:** DSGVO / Legal / Infra.

---

## AI Act

### AI Act Art. 50(1) — KW33: Keine öffentlichen Verfahren — Bundesnetzagentur Marktbeobachtung aktiv *(KW33 STATUS)*

[Bundesnetzagentur KI-MIG](https://www.glacis.io/guide-eu-ai-act-germany) | [KI-MIG Deutschland](https://consulting.tuv.com/aktuelles/ki-im-fokus/ki-mig-deutschland-umsetzung) | [aiactblog.nl — Art. 50 Enforcement](https://www.aiactblog.nl/en/posts/article-50-enforcement-fines-ai-act-2026) | [TechTimes — BaFin](https://www.techtimes.com/articles/322089/20260729/germany-arms-bafin-police-ai-credit-scoring-bank-chatbot-disclosure.htm)

Dritte Enforcement-Woche ohne öffentlich bekannte Bußgeldverfahren in Deutschland. Bundesnetzagentur führt aktive Marktbeobachtung durch. KI-MIG seit 29.07.2026 in Kraft. Behörden-Modus: Screening + Orientierungsanfragen. Erste formale Verfahren erwartet Q4/2026.

**Status der Enforcement-Infrastruktur:**
- Bundesnetzagentur: zentrale Marktüberwachung + Beschwerdestelle operativ
- BaFin: Finanzsektor (Chatbot-Disclosure, Kredit-Scoring) aktiv seit 29.07.
- Bußgeldrahmen: €15M/3% (Art. 50) | €35M/7% (Art. 5 verbotene Praktiken)

*Cosmi-Implikation:* KW32-Compliance-Screening-Auftrag noch offen? Alle KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Kunden) auf Erstkontext-Offenlegung testen. Marktbeobachtungs-Intensivierung durch Bundesnetzagentur erwartet. `#followup → KW34` **Modul:** AI Act / Legal / Product.

---

### AI Act Omnibus — Hochrisiko Annex III Aufschub bis 02.12.2027 — Status unverändert *(Carry-over)*

[Gibson Dunn — Omnibus](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) | [Secure Privacy](https://secureprivacy.ai/blog/eu-ai-act-digital-omnibus-the-new-high-risk-ai-deadlines-after-council-approval)

Keine neuen KW33-Ereignisse. Reg. 2026/1744 in Kraft seit 27.07.2026. Annex-III-Frist: 02.12.2027.

*Cosmi-Implikation:* Cosmi-Schichten HR-Features auf Annex-III-Relevanz prüfen (bis Q1/2027). `#followup → Q4/2026` **Modul:** AI Act / Legal / Schichten.

---

## NIS2

### NIS2 BSI — Enforcement-Phase aktiv nach 31. Juli — Portal weiterhin offen *(KW33 STATUS)*

[ITMR-Legal](https://itmr-legal.de/blog/nis2-registrierung-verpasst) | [Advisori — BSI Actively Auditing](https://www.advisori.de/en/blog/nis2-enforcement-2026-bsi-audit-fines) | [Shattered.io — NIS2 Bußgelder](https://shattered.io/de/nis2-umsetzung-deutschland-bsig-2026/) | [Security Today](https://www.securitytoday.de/2026/05/03/nis2-enforcement-welle-q2-2026-erste-eu-verfahren-laufen-was-dach-unternehmen-bei-der-eigenen-compliance-jetzt-pruefen-muessen/)

Der 31. Juli 2026 (informelles BSI-Ziel) ist verstrichen. BSI-Registrierungsportal bleibt geöffnet. Enforcement-Phase läuft seit Mai 2026. Ca. 18.500 von ~29.500 betroffenen Unternehmen haben die März-Frist verpasst.

**Bußgeld-Rahmen nach Fristablauf:**
- Nicht-Registrierung: bis €500.000 (Wichtige Einrichtungen)
- Nicht-Registrierung BWE: bis €10M oder 2% globaler Umsatz
- GF-Haftung: §38 BSIG, persönlich, unbeschränkt
- Spät-Registrierung = stärkster Mitigation-Faktor

Kein neues BSI-Enforcement-Kommuniqué KW33 identifiziert.

*Cosmi-Implikation:* Falls Cosmi noch nicht registriert: sofort. Falls registriert: Nächster Schritt = §30 BSIG Cybersicherheitsmaßnahmen dokumentieren (TOM). `#akut falls nicht registriert` **Modul:** NIS2 / Legal / Management.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche KW33 — keine neuen Regelungen

[e-Rechnung-Pflicht Übersicht (rechnex.de)](https://rechnex.de/blog/e-rechnung-pflicht-2025) | [BMF — FAQ e-Rechnung](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html)

Keine neuen Regelungen KW33. Fristen-Status unverändert:

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen — Pflicht |
| bis 31.12.2026 | Übergangsfrist **Versand** — Papier/PDF mit Zustimmung erlaubt (Umsatz > €800k bis 31.12.2026) |
| ab 01.01.2027 | **Versandpflicht** bei Umsatz > €800k Vorjahr |
| ab 01.01.2028 | **Versandpflicht** alle B2B (inkl. Kleinbetriebe) |

---

## ArbZG / Arbeitsrecht

### Stille Woche KW33 — kein Bundestag/Kabinett-Schritt

[Clockin — Referentenentwurf](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026) | [LTO — Zeitplan](https://www.lto.de/recht/nachrichten/n/bas-kuendigt-gesetzentwurf-arbeitszeitgesetz-an-juni-2026)

Kein parlamentarischer Fortschritt KW33. Referentenentwurf (17.06.2026) im Koalitions-Konsultationsverfahren. SPD-Fraktionschef Wiese zuversichtlich über CDU/CSU-SPD-Einigung. Verabschiedung 2026 noch möglich.

---

## eIDAS

### 🟡 EUDIW ARF v3.0 erschienen — Upgrade von v2.8.0 — Deutschland Sandbox-Leader *(KW33 NEU)*

[eideasy.com — EU Digital Identity Wallets August 2026](https://www.eideasy.com/blog/eu-digital-identity-wallets-august-2026) | [Biometric Update — ARF v3.0](https://www.biometricupdate.com/202607/conformance-framework-for-eu-digital-identity-wallets-arrives-with-arf-v3-0) | [Bundesdruckerei — EUDI Wallet](https://www.bundesdruckerei.de/en/innovation-hub/eudi-wallet-sicher-digital-identifizieren-europa) | [Persona — France & Germany Sandbox](https://withpersona.com/blog/persona-supports-france-and-germany-eudi-wallets-for-secure-private-identity-verification/)

**ARF v3.0 ist die relevante Referenz** — ersetzt v2.8.0 (Referenz in KW32-Sweep). Erschienen im Juli 2026. Neue Funktionale Konformitätsbewertungs-Framework (FCAF) mit wiederverwendbaren Testfällen. Alignment mit Commission Implementing Regulations (CIRs) 2024–2025. Tracker-Refresh: 3. August 2026.

**Status Deutschland (August 2026):**
- Deutschland und Frankreich führen EU bei EUDIW-Sandbox-Readiness an
- DE-Launch weiterhin: **02. Januar 2027** (140 Tage)
- EU-Pflicht: Dezember 2026 (alle 27 Mitgliedstaaten)
- Implementing Regulations aktualisiert: 15. Juli 2026

*Cosmi-Implikation:* Die KW32-Aufgabe (ARF v2.8.0 evaluieren) ist überholt — direkt mit **ARF v3.0 + FCAF** einsteigen. Relying-Party-Anforderungen für Cosmi-Vertraege und Formulare aktualisieren. Q4-Sprint einplanen. 140 Tage bis DE-Launch. `#followup → Q3/Q4/2026` **Modul:** eIDAS / Product / Vertraege.

---

## BSI-Warnings — KW33 (9.–15. August 2026)

> **KW33-Highlight: PostgreSQL Rekord-Patch-Batch 13.08.2026** — 28 CVEs, 9× Arbitrary Code Execution, direkter Cosmi-Datenbankstack-Treffer. Größter PostgreSQL-Security-Release aller Zeiten. Sofort patchen + Post-Update-Wartung durchführen.

### 🔴 KRITISCH — PostgreSQL Rekord-CVE-Batch (13.08.2026) — Direkter Cosmi-DB-Stack-Treffer

[PostgreSQL Release Notes 18.6](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/) | [PostgreSQL Security](https://www.postgresql.org/support/security/) | [HeroDevs — PostgreSQL 14 EOL](https://www.herodevs.com/blog-posts/postgresql-14-eol-nov-2026-44-cves-this-year-one-patch-left)

Am **13. August 2026** veröffentlichte das PostgreSQL Global Development Group die Versionen **18.6, 17.11, 16.15, 15.19, 14.24** sowie 19 Beta 3. Dies ist der **größte Sicherheits-Patch-Batch in der Geschichte von PostgreSQL**.

**Zahlen:**
- 28 CVEs gepatcht (Rekord)
- 17 CVEs mit CVSS ≥ 8.0
- 9 CVEs mit "executes arbitrary code" in der Beschreibung
- 110+ Bugfixes

**Kritische CVEs (CVSS 8.8) — Arbitrary Code Execution:**

| CVE | Beschreibung | CVSS |
|-----|-------------|------|
| CVE-2026-14662 | tsvector/tsquery integer wraparound → RCE | 8.8 |
| CVE-2026-14664 | Regexp heap buffer overflow → RCE | 8.8 |
| CVE-2026-14669 | `to_char(timestamptz)` heap buffer overflow → RCE | 8.8 |
| CVE-2026-14670 | plperl tied object heap buffer overflow → RCE | 8.8 |
| CVE-2026-14671 | refint plan cache type confusion → RCE | 8.8 |
| CVE-2026-14676 | pg_stat_statements heap buffer overflow → RCE | 8.8 |
| CVE-2026-14677 | 32-bit pltcl/plperl undersize allocations → RCE | 8.8 |
| CVE-2026-14680 | Type confusion via "internal" args → RCE | 8.8 |
| CVE-2026-15741 | Expression deparse → SQL Injection (EXTRACT) | 8.8 |
| CVE-2026-15742 | fuzzystrmatch integer wraparound → writes arbitrary addresses | 8.8 |
| CVE-2026-16238 | Type confusion in pg_restore_attribute_stats() → RCE | 8.8 |
| CVE-2026-16239 | Type confusion in cursor CLOSE + DECLARE → RCE | 8.8 |
| CVE-2026-18408 | psql `\unrestrict` → arbitrary code execution | 8.8 |
| CVE-2026-19385 | pg_dump heap buffer overflow → RCE | 8.8 |

**Weitere relevante CVEs:**

| CVE | Beschreibung | CVSS |
|-----|-------------|------|
| CVE-2026-6464 | psql COPY FROM STDIN → psql command injection | 8.1 |
| CVE-2026-14668 | ctid type confusion → arbitrary read | 8.1 |
| CVE-2026-14679 | Stack buffer overflow in argument match | 8.2 |
| CVE-2026-6471 | Logical decoding dlopen arbitrary file | 7.2 |

**Post-Update-Wartung ERFORDERLICH** (ohne Maintenance drohen Datenkonsistenzfehler):

```sql
-- 1. GIN-Indexes (PostgreSQL 14/15/16): bogus reltuples nach parallelen Builds prüfen
SELECT DISTINCT t.oid::regclass, t.reltuples
FROM pg_class t
JOIN pg_index i ON t.oid = i.indrelid
JOIN pg_class ic ON i.indexrelid = ic.oid
WHERE t.relhasindex AND ic.relam = 2742;
-- Dann: ANALYZE auf betroffene Tabellen

-- 2. btree_gist-Indexes: reindizieren (float4/float8 NaN-Handling)
REINDEX INDEX <index_name>;

-- 3. ltree-Indexes mit >14.653 Labels: reindizieren (Integer Overflow)
REINDEX INDEX <index_name>;
```

**⚠️ PostgreSQL 14 EOL: 12. November 2026 — noch 89 Tage.** Nach EOL keine Sicherheits-Patches mehr. Wenn Cosmi auf PostgreSQL 14 läuft: Upgrade-Plan auf 15 oder 17 sofort einleiten.

*Cosmi-Implikation:* **Direkter Datenbankstack-Treffer — höchste Priorität.** 14 CVEs mit arbitrary code execution betreffen den laufenden Datenbankserver. Sofort auf aktuelle Patchversion upgraden. Danach Pflege-SQLs ausführen. PostgreSQL-14-EOL in die Sprint-Planung aufnehmen. `#akut` **Modul:** Security / Infra / DB.

---

### 🔴 BSI Linux Kernel CRITICAL — WID-SEC-2026-2640 (14.08.2026) — UPDATE

[b2b-cyber-security.de — BSI Kernel Warning](https://b2b-cyber-security.de/en/bsi-sicherheitswarnung-mehrere-schwachstellen-im-linux-kernel/)

Das BSI hat am 14. August 2026 das Linux-Kernel-Advisory WID-SEC-2026-2640 auf **KRITISCH** hochgestuft. Schadensvektor: Informationsoffenlegung + weitere Angriffspfade. Multiple Kernel-Advisories am 14.08. aktualisiert (WID-SEC-2026-1232, -2077, -2056, -1870).

*Cosmi-Implikation:* KW32-Kernel-Patch verifizieren (war dort bereits HIGH). Falls Update ausstehend oder neues CRITICAL-Advisory nicht erfasst: sofort nachholen. Alle Produktionsserver betroffen. `#akut` **Modul:** Security / Infra.

---

### BSI-Advisories KW33 — weitere (kein direkter Cosmi-Stack-Treffer)

| Advisory | Produkt | Datum | Schwere | Cosmi-Relevanz |
|----------|---------|-------|---------|----------------|
| WID-SEC-2026-1544 (UPDATE) | Apache HTTP Server (multiple) | 14.08.2026 | HIGH | Kein Treffer (Cosmi nutzt Nginx) — Kundensysteme prüfen |
| WID-SEC-2026-1584 (UPDATE) | Docker / Kubernetes | 14.08.2026 | MEDIUM | Falls Cosmi Container-Infra nutzt: regulärer Update-Zyklus |
| WID-SEC-2026-2044 | Python/CPython | akt. | HIGH | Falls Python-Services in Cosmi-Stack: prüfen |
| WID-SEC-2026-2843 | OpenSSL | akt. | MEDIUM | DoS — regulärer Patch-Zyklus |

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 18). Keine neuen EU-Acts via WebSearch KW33.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 17). Keine BfDI-Pressemitteilungen KW33.
- **BSI Pressemitteilungen** — RSS 404 (Woche 17). BSI-WID-Advisory-Feed als Kompensation.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 18). Keine neuen Regelungen.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 18). Kein Bundestag-Schritt KW33.
- **ENISA** — RSS 404 (Woche 15). Keine neuen ENISA-Publikationen KW33.
- **EDPB Newsroom** — RSS 403. EDPB-Output via WebSearch abgedeckt.
- **EDPS** — 403. Keine neuen EDPS-Publikationen KW33.
- **noyb** — Kein RSS-Inhalt KW33. Schrems-III-Klage weiterhin nicht eingereicht.

> **Wartungshinweis (Woche 18):** 6×404 + 2×403 persistent. PostgreSQL-eigener Release-Feed + BSI-WID + WebSearch als Haupt-Kompensationskanäle. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — sofort

- [ ] **PostgreSQL SOFORT patchen** — 18.6 / 17.11 / 16.15 / 15.19 / 14.24 (je nach eingesetzter Hauptversion). 28 CVEs, 14× RCE (CVSS 8.8). Größter PostgreSQL-Security-Batch aller Zeiten. `#security #infra #db` → **sofort (13.08.2026)**
- [ ] **PostgreSQL Post-Update-Wartung** — GIN-Index-Tabellen per SQL prüfen + ANALYZE, btree_gist-Indexes REINDEX, ltree-Indexes ≥14.654 Labels REINDEX. Ohne Wartung: Datenkonsistenzfehler möglich. `#db #infra` → **sofort nach Patch**
- [ ] **PostgreSQL 14 EOL-Migration einleiten** — EOL 12.11.2026 (89 Tage). Upgrade-Pfad auf PostgreSQL 15 oder 17 in Sprint-Planung aufnehmen. `#infra #db` → **Sprint-Planung KW34**
- [ ] **Linux Kernel CRITICAL (WID-SEC-2026-2640) — Status verifizieren** — KW32-Patch-Status auf allen Produktionsservern bestätigen. Advisory am 14.08. auf CRITICAL hochgestuft. `#security #infra` → **sofort**

### 🟡 Followup (KW34+)

- [ ] **EDPB/EC Stakeholder Event 15.10. — Anmeldung bis 28.08.** — Datenschutz × Wettbewerbsrecht. Für Cosmi-Daten-Enrichment und KI-Features strategisch relevant. `#dsgvo #legal` → **bis 28.08.2026 (13 Tage!)**
- [ ] **eIDAS ARF v3.0 Gap-Analyse** — Neue Referenz (KW32 sprach noch von v2.8.0). FCAF-Anforderungen lesen, Cosmi-Vertraege-/Formulare-Relying-Party-Assessment aktualisieren. 140 Tage bis DE-Launch. `#eidas #product` → **Q3/2026**
- [ ] **EDPB Web Scraping Guidelines 03/2026 lesen** — Relevant falls Cosmi KI-Enrichment-Pipeline externe Web-Quellen oder Data-Broker-Datensätze nutzt. Rechtliche Basis prüfen. `#dsgvo #aifeatures #legal` → **KW35**
- [ ] **Art. 50(1) Compliance-Screening finalisieren** — Bundesnetzagentur aktive Marktbeobachtung. Alle KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API) auf Erstkontext-Offenlegung testen. Log anlegen. `#aiact #legal #product` → **KW34**
- [ ] **EDPB Breach Template — SOP-Abgleich** — Konsultation geschlossen. Draft-Template (7 Sektionen, 126 Felder) mit Cosmi-Incident-Response-SOP abgleichen. Lücken dokumentieren. `#dsgvo #legal #security` → **KW34**
- [ ] **NIS2 BSI-Registrierung** — Falls noch nicht registriert: Spät-Registrierung sofort (stärkster Mitigation-Faktor). Falls registriert: §30 BSIG TOM-Dokumentation starten. `#nis2 #legal` → **sofort falls ausstehend**
- [ ] **DPF SCC-Fallback-Audit weiterführen** — Schrems-III-Klage erwartet. US-SaaS-Transfers inventarisieren, SCCs dokumentieren. `#dsgvo #legal #infra` → **laufend**
- [ ] **AI Act Hochrisiko-Klassifikation Schichten/HR-Features** — Annex-III-Frist 02.12.2027, Planung bis Q1/2027. `#aiact #legal #schichten` → **Q4/2026**
- [ ] **ArbZG-Referentenentwurf Schichten-Features** — Koalitions-Konsultation läuft. Wochenarbeitszeit-Schema und elektronische Zeiterfassung als Compliance-Argument vorbereiten. `#arbzg #product #schichten` → **Q4/2026**
- [ ] **BSI C5:2026 Gap-Analyse** — DACH-B2B-Vertriebsvoraussetzung. `#nis2 #security` → **Q3/2026**
