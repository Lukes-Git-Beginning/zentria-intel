---
date: 2026-08-08
type: regulation
runtime_minutes: 22
items_scanned: 58
items_relevant: 12
sources_live_rss: 1
sources_ok_list: [bsi-warnungen]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
sources_supplemented_websearch: 11
websearch_supplements: 11
kw: 32
---

# Regulation-Sweep KW32/2026 (Sa 8. August)

> **KW32-Scope:** 2.–8. August 2026. Referenz-Sweep: KW31 (1. August). WebSearch-Supplements: 11. RSS-Live: BSI-WID (Nginx/Redis/Linux Kernel — Patch-Batch 08.08.).
>
> **Status-Konsolidierungs-Woche nach dem KW31-Sprint.** Keine neuen Enforcement-Explosionen — aber drei laufende Fäden, die Nacharbeit erfordern.
>
> **🔴 ART. 50(1) AKTIV — ERSTE WOCHE OHNE PUBLIKUMS-VERFAHREN, ABER BUNDESNETZAGENTUR OPERATIV:** Transparenzpflicht seit Samstag (02.08.) erzwingbar. Keine ersten öffentlichen Bußgeldverfahren in KW32 bekannt. Bundesnetzagentur nimmt offiziell Beschwerden entgegen (Anlaufstelle seit Ende Juli aktiv). Compliance-Prüfung aller KI-Touchpoints war Cosmi-Aufgabe bis 02.08. — Status verifizieren.
>
> **🟡 AI ACT OMNIBUS HOCHRISIKO-AUFSCHUB — RECHTSVERBINDLICH SEIT 27.07.2026:** Annex-III-Hochrisiko-Systeme (Personalauswahl, Kredit-Scoring, Biometrie etc.) haben Frist bis **02.12.2027** (statt 02.08.2026). 16-Monate-Aufschub ist in Kraft (Reg. 2026/1744 seit 27.07.). Relevant falls Cosmi HR-KI-Features unter Annex III fallen.
>
> **🟡 EDPB BREACH TEMPLATE — KONSULTATION GESCHLOSSEN (05.08.2026):** 7-Abschnitte-Template (126 Felder) für Art.-33-Meldungen ist in der finalen Kommentierungsphase. Kein Final-Dokument noch. Nationaler Implementierungszeitplan offen. Cosmi-SOP-Abgleich mit Draft-Template (04.08.-Aufgabe) jetzt dokumentieren.
>
> **🟡 NIS2 KLARSTELLUNG — 31. JULI WAR KEIN GESETZLICHER STICHTAG:** BSI-Portal ist weiterhin offen. Verspätete Registrierung löst nicht automatisch Bußgeld aus — liegt im BSI-Ermessen. Aber: gesetzlicher Friststart war 06.03.2026 (3-Monats-Frist §33 BSIG). Sofortige Selbst-Registrierung ist stärkster Mitigationsfaktor.
>
> **🔴 BSI KW32 — NGINX RCE + REDIS HEAP OVERFLOW (08.08.2026):** Debian-Sicherheits-Batch 08.08.2026: Nginx (RCE/DoS/Memory Disclosure) + Redis (Heap Overflow im RESTORE-Befehl) + Linux Kernel (Privilege Escalation) + Thunderbird (RCE). Sofort patchen.

---

## DSGVO / Datenschutz

### 🟡 EDPB Art.-33-Breach-Template — Konsultation geschlossen 05.08.2026 — Kein Final-Template *(KW32 STATUS)*

[EDPB — Template for personal data breach notification](https://www.edpb.europa.eu/public-consultations/template-for-personal-data-breach-notification_en) | [LexisNexis — EDPB adopts standardised template](https://www.lexisnexis.com/en-gb/legal/news/edpb-adopts-standardised-data-breach-notification-template) | [sota.io — Developer Guide](https://sota.io/blog/edpb-gdpr-art33-common-breach-notification-template-developer-guide-2026) | [bratby.law — Template summary](https://bratby.law/edpb-data-breach-notification-template/)

Die öffentliche Konsultation zum gemeinsamen EDPB-Template für Art.-33-Meldungen **ist am 5. August 2026 geschlossen**. Das 126-Felder-Formular (7 Abschnitte) wurde am 8. Juni 2026 als Version 1.0 verabschiedet und war bis gestern kommentierbar. Der EDPB wird nun Feedback auswerten — finales Template noch nicht publiziert.

**Was im Template steht (Stand Draft v1.0):**
- 7 Sektionen: (1) DPA-Identifikation, (2) verantwortliche Stelle, (3) Kontaktpunkt (DSB), (4) Phasen-Beschreibung des Vorfalls, (5) betroffene Personen + Kategorien, (6) Art des Risikos und Massnahmen, (7) Querschnittskommunikation
- Ziel: harmonisiertes Format für 27 EU-Staaten — derzeit 27 divergierende Nationale Formulare

Nationaler Implementierungszeitplan (wann BfDI/LDA das Template vorschreibt): noch nicht kommuniziert.

*Cosmi-Implikation:* Die **KW31-Aufgabe** war: Draft-Template bis 04.08. herunterladen und mit Cosmi-Incident-Response-SOP abgleichen. Falls noch nicht geschehen: jetzt nachholen. Lücken zwischen Cosmi-SOP und Template-Anforderungen dokumentieren und im nächsten Legal-Sprint schließen. Das Template wird nach Finalisierung de-facto verbindlich sein — frühzeitige Ausrichtung spart Anpassungsaufwand. `#followup` **Modul:** DSGVO / Legal / Security.

---

### 🟡 EDPB Anonymisierungsleitlinien 02/2026 — Konsultation läuft bis 30.10.2026 *(KW31 Carry-over)*

[EDPB — Guidelines 02/2026 on Anonymisation (PDF)](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf) | [Sidley — Data Matters](https://datamatters.sidley.com/2026/07/27/edpb-publishes-draft-guidelines-on-anonymisation/) | [Freshfields — Anonymous or not?](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/anonymous-or-not-the-edpbs-new-draft-guidelines-on-anonymisation-102nbv5) | [IAPP — EDPB draft](https://iapp.org/news/a/the-edpb-s-draft-anonymization-guidelines-what-they-mean-for-your-data-strategy)

Keine neuen Entwicklungen KW32. Konsultation läuft bis 30.10.2026. Kern: **3-Kriterien-Test** für echte Anonymität:
1. Keine **Record Isolation** möglich
2. Keine **Verknüpfung** (Linkage) mit anderen Datensätzen
3. Keine **Inferenz** über Individuen

Hintergrund: CJEU EDPS v SRB (September 2025) — pseudonymisierte Daten sind nicht automatisch für alle Empfänger personenbezogen.

*Cosmi-Implikation:* Relevant für Cosmi-Reporting, Analysemodule, Aggregation von Kundendaten für KI-Features. Wenn Cosmi Daten als "anonym" behandelt für interne Analysen: 3-Kriterien-Test dokumentieren. `#beobachten → bis Oktober` **Modul:** DSGVO / Legal / AI-Features.

---

### EDPB/EC Stakeholder-Konsultation — Datenschutz & Wettbewerb — Bewerbung bis 28.08.2026 *(KW32 NEU)*

Der EDPB und die Europäische Kommission haben für den **15. Oktober 2026** ein gemeinsames Remote-Stakeholder-Event zu Leitlinien über das Zusammenspiel von **Datenschutz und Wettbewerbsrecht** angekündigt. Call for Interest: bis **28. August 2026** (20 Tage).

*Cosmi-Implikation:* Für Cosmi als Daten-aggregierendes SaaS-CRM potenziell relevant — künftige Leitlinien könnten die Nutzung von Kundendaten für Marktanalyse, Benchmarking oder KI-Training im Licht des Wettbewerbsrechts einschränken. Teilnahme am Event oder Lektüre der Aufzeichnung empfohlen. `#beobachten` **Modul:** DSGVO / Legal.

---

### 🟡 DPF Schrems III — Keine Klage KW32 — Carry-over *(Woche 2 ohne Einreichung)*

[Captain Compliance — Schrems III](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) | [activeMind.legal — DPF Supreme Court](https://www.activemind.legal/guides/dpf-supreme-court/) | [Mishcon — Trump v. Slaughter](https://www.mishcon.com/news/is-this-the-end-of-the-dpf-trump-v-slaughter-and-the-potential-for-schrems-iii) | [Passcreator — Schrems III 2026](https://www.passcreator.com/en/blog/schrems-iii-2026-is-your-data-in-the-us-cloud-still-secure)

Weiterhin keine Klageeinreichung durch noyb. DPF formal gültig. Stand Mitte Juli: noyb kündigt Einreichung "in den kommenden Wochen" an. CJEU-Fall C-703/25 P (Latombe) läuft parallel. EC hat auf noyb-Brief (30.06.) weiterhin nicht reagiert.

*Cosmi-Implikation:* SCC-Fallback-Audit läuft (KW31-Aufgabe). US-SaaS-Transfers weiter inventarisieren. Kein Handlungsdruck diese Woche. `#followup` **Modul:** DSGVO / Legal / Infra.

---

## AI Act

### 🟡 AI Act Art. 50(1) — Erste Enforcement-Woche (02.–08.08.2026) — Bundesnetzagentur operativ *(KW32 STATUS)*

[Bundesnetzagentur — KI-Beschwerdestelle](https://www.all-ai.de/news/beitrage2026/ki-deutschland-beschwerden-1) | [ad-hoc-news — €35M Fines Enforceable](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/eu-s-ai-transparency-rules-now-fully-enforceable-with-fines-reaching/69912893) | [aiactblog.nl — What actually changed](https://www.aiactblog.nl/en/posts/article-50-applies-now-what-changed) | [it-boltwise — Bundesnetzagentur + BaFin](https://www.it-boltwise.de/ki-kennzeichnung-ab-august-bundesnetzagentur-und-bafin-setzen-eu-regeln-um.html)

Die erste Enforcement-Woche nach Inkrafttreten der Art.-50(1)-Transparenzpflichten (02.08.2026) ist ohne öffentliche Bußgeldverfahren verlaufen. Dies ist normal — Behörden priorisieren initial Orientierungsanfragen, Leitlinien und Beschwerde-Screening über sofortige Sanktionen.

**Stand KW32:**
- Bundesnetzagentur: **zentrale KI-Marktüberwachungsbehörde** + **nationale KI-Beschwerdestelle** aktiv. Erste Beschwerden werden bearbeitet.
- BaFin: Finanzsektor-Überwachung (Chatbot-Disclosure, Kredit-Scoring) seit 29.07. aktiv.
- Bußgeldrahmen unverändert: **€15M oder 3 % globaler Jahresumsatz** (Art. 50-Verstöße).
- **€35M oder 7 %** gilt nur für verbotene KI-Praktiken nach Art. 5.

**Was in der Praxis gemeldet wird:**
- Beschwerde-Richtung: vor allem Chatbots ohne Erstkontext-Offenlegung und Voice Agents ohne KI-Disclosure.
- Bundesnetzagentur prüft derzeit Markt — aktive Stichproben erwartet.

*Cosmi-Implikation:* Falls KW31-Compliance-Check nicht abgeschlossen: **jetzt finalisieren**. Alle KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Kunden) müssen beim **ersten Interaktionspunkt** KI-Natur offenlegen — vor Anmeldung, vor der ersten Antwort. Bundesnetzagentur-Beschwerdewelle in KW33/34 antizipieren wenn Early Movers Konkurrenten melden. `#akut → Compliance-Status verifizieren` **Modul:** AI Act / Legal / Product.

---

### 🟡 AI Act Omnibus — Hochrisiko-Aufschub RECHTSVERBINDLICH seit 27.07.2026 *(KW32 UPGRADE)*

[Gibson Dunn — Omnibus Agreement](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) | [Secure Privacy — New Deadlines](https://secureprivacy.ai/blog/eu-ai-act-digital-omnibus-the-new-high-risk-ai-deadlines-after-council-approval) | [FPF — Timeline Changes](https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/) | [Inside Privacy — AI Act Update](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)

Der AI Act Omnibus (Reg. 2026/1744) trat am 27.07.2026 in Kraft — damit ist der **Hochrisiko-Aufschub für Annex-III-Systeme auf 02.12.2027** rechtsverbindlich. Politische Einigung: 7. Mai 2026. Council-Bestätigung: 29. Juni 2026.

**Überblick Fristen-Architektur nach Omnibus:**

| Kategorie | Frist | Status |
|-----------|-------|--------|
| **Art. 50 Transparenz** (Chatbots, Deepfakes) | 02.08.2026 | **In Kraft — Enforcement läuft** |
| **Art. 50(2)/(4) Wasserzeichen/Content Labeling** | 02.12.2026 | 120 Tage |
| **Annex III Hochrisiko** (Personalauswahl, Biometrie, Kredit) | 02.12.2027 | 16 Monate Aufschub |
| **GPAI General-Purpose AI** | 02.08.2025 | bereits in Kraft (seit KW31/2025) |

**Annex III Hochrisiko — Cosmi-Relevanz-Prüfung:**
- Personalauswahl / HR (Art. 6(2), Anhang III 4a): Cosmi-Schichten hat Funktionen zur Mitarbeiterplanung — **prüfen** ob algorithmische Zuweisung oder Bewerbungs-Screening unter Annex III fällt
- Kredit-Scoring: nicht Cosmi-Core
- Biometrische Identifikation: nicht Cosmi-Core

*Cosmi-Implikation:* Hochrisiko-Klassifikationsprüfung für Schichten/HR-Features bis **Q1/2027** (früh genug vor Dezember-Frist). Falls Cosmi GPAI-Komponenten hostet (eigene Modelle): GPAI-Code-of-Practice beachten. `#followup → Q4/2026` **Modul:** AI Act / Legal / Product / Schichten.

---

## NIS2

### 🟡 NIS2 BSI — KLARSTELLUNG: 31.07. war KEIN gesetzlicher Stichtag — Portal weiterhin offen *(KW32 UPDATE/KORREKTUR)*

[ITMR-Legal — Registrierung verpasst: was jetzt](https://itmr-legal.de/blog/nis2-registrierung-verpasst) | [Shattered.io — NIS2 Bußgelder](https://shattered.io/de/nis2-umsetzung-deutschland-bsig-2026/) | [Advisori — BSI Actively Auditing](https://www.advisori.de/en/blog/nis2-enforcement-2026-bsi-audit-fines) | [Security Today — Enforcement Welle](https://www.securitytoday.de/2026/05/03/nis2-enforcement-welle-q2-2026-erste-eu-verfahren-laufen-was-dach-unternehmen-bei-der-eigenen-compliance-jetzt-pruefen-muessen/)

**Korrektur zu KW31:** Der 31. Juli 2026 war **kein gesetzlicher Fristablauf**, sondern ein kommuniziertes BSI-internes Ziel. Das BSI-Registrierungsportal ist **weiterhin geöffnet** und nimmt Neuregistrierungen entgegen.

**Tatsächliche Rechtslage:**
- **Gesetzlicher Stichtag:** 06.03.2026 (3-Monats-Frist nach §33 BSIG ab Portal-Öffnung 06.01.2026)
- **Bußgeldbefugnis:** Seit 06.03.2026 kann das BSI Bußgelder verhängen — aber: Ermessenssache
- **Mitigationsfaktor:** Selbst-initiierte, vollständige Spät-Registrierung ist stärkster Faktor gegen Strafverfolgung
- **Portal:** Weiterhin offen — kein "closed" per 31.07.

**Bußgeld-Rahmen (§65 BSIG — 7 Stufen):**

| Kategorie | Maximal |
|-----------|---------|
| Wichtige Einrichtungen (WE) | €500.000 (§60 BSIG) |
| Besonders Wichtige Einrichtungen (BWE) | €10M oder 2% globaler Umsatz |
| GF-Haftung §38 BSIG | persönlich, unbeschränkt |

*Cosmi-Implikation:* Falls Cosmi noch nicht registriert ist: **sofort registrieren** (Selbst-Initiative minimiert Bußgeldrisiko deutlich). Falls registriert: Nächster NIS2-Schritt = Cybersicherheitsmaßnahmen nach §30 BSIG dokumentieren (technische + organisatorische Maßnahmen). `#akut falls noch nicht registriert` **Modul:** NIS2 / Legal / Management.

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche KW32 — keine neuen Regelungen

Keine neuen XRechnung/GoBD/e-Rechnung-Regelungen KW32. Fristen-Status unverändert:

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen — Pflicht |
| bis 31.12.2026 | Übergangsfrist **Versand** — Papier/PDF mit Zustimmung erlaubt (Umsatz > €800k bis 31.12.2026) |
| ab 01.01.2027 | **Versandpflicht** bei Umsatz > €800k Vorjahr |
| ab 01.01.2028 | **Versandpflicht** alle B2B (inkl. Kleinbetriebe) |

---

## ArbZG / Arbeitsrecht

### Stille Woche KW32 — kein Bundestag/Kabinett-Schritt

Kein Gesetzgebungsfortschritt ArbZG KW32 sichtbar. Referentenentwurf vom 17.06.2026 im laufenden Konsultations- und Abstimmungsverfahren. Politische Auseinandersetzungen zwischen Wirtschaftsverbänden und Gewerkschaften dauern an. Verabschiedung 2026 bleibt möglich.

**Stand des Referentenentwurfs (Reminder):**
- Elektronische Zeiterfassung (Beginn/Ende/Dauer) wird Pflicht — täglich, elektronisch
- Wöchentliche Höchstarbeitszeit via Tarifvertrag (flexibler als bisher täglich)
- 11h-Ruhezeit kann via Tarifvertrag+Gesundheitsschutz entfallen
- Übergangsfristen: Großunternehmen 1 Jahr / ≤250 MA 2 Jahre / Kleinbetriebe 5 Jahre

---

## eIDAS

### EUDIW — Dezember 2026 EU-Pflicht, DE-Launch 02.01.2027 — Status unverändert *(Carry-over)*

[eidasreadiness.com — Timeline](https://eidasreadiness.com/eidas-2-timeline) | [Freshfields — EUDI Wallet coming](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/the-eudi-wallet-is-coming-what-businesses-need-to-know-102mvuy) | [eudi-wallet.eu — Hub](https://www.eudi-wallet.eu/)

Keine neuen KW32-Entwicklungen. EU-Pflicht: Dezember 2026 (alle 27 Mitgliedstaaten müssen mindestens 1 EUDIW bereitstellen). DE-Launch: 02.01.2027 (147 Tage). ARF v2.8.0 aktuell. Sandbox läuft.

*Cosmi-Implikation:* ARF v2.8.0 Relying-Party-Anforderungen für Cosmi-Vertraege/Formulare evaluieren — Q4-Sprint einplanen. `#beobachten → Q3/2026` **Modul:** eIDAS / Product / Vertraege.

---

## BSI-Warnings — KW32 (2.–8. August 2026)

> **KW32-Highlight: Debian-Sicherheits-Batch 08.08.2026** — Nginx (RCE/DoS), Redis (Heap Overflow), Linux Kernel (Privilege Escalation), Thunderbird (RCE), libheif (Heap OOB). Sofort patchen.

### 🔴 Cosmi-Stack-Advisories KW32

| Advisory | Produkt | Datum | Schwere | Risiko | Massnahme |
|----------|---------|-------|---------|--------|-----------|
| Debian DSA KW32-A | **Nginx** | 08.08.2026 | HIGH | Remote Code Execution, DoS, Memory Disclosure | **Sofort patchen** — Reverse Proxy |
| Debian DSA KW32-B | **Redis** | 08.08.2026 | HIGH | Heap Overflow im RESTORE-Befehl (CVE-2026-23479 u.a.) | **Sofort patchen** — falls Redis in Stack |
| Debian DSA KW32-C | **Linux Kernel** | 08.08.2026 | HIGH | Privilege Escalation, Memory Leaks, Crash | **Sofort patchen** — alle Produktionsserver |
| Debian DSA KW32-D | **Thunderbird** | 08.08.2026 | HIGH | Remote Code Execution | Patchen — falls Cosmi Mail-Client nutzt |
| Debian DSA KW32-E | **libheif** | 08.08.2026 | MEDIUM | Heap Out-of-Bounds Write (CVE-2026-47178) | Regulaer updaten |

### Weitere BSI-Advisories KW32 (kein direkter Cosmi-Stack-Treffer)

| Advisory | Produkt | Schwere | Cosmi-Relevanz |
|----------|---------|---------|----------------|
| WID-SEC-2026-2242 | IBM Operational Decision Manager | CRITICAL (CVSS 9.8) | Kein direkter Treffer — falls IBM-Middleware in Kundensystemen |
| WID-SEC-2026-2050 | IBM WebSphere / Liberty | CRITICAL (CVSS 9.3) | Kein direkter Treffer — Enterprise-Kundensegment |

### Status KW31-Advisories

| Advisory | Produkt | Massnahme-Status |
|----------|---------|-----------------|
| GNU libc CRITICAL (30.07.) | libc | Falls KW31-Patch noch ausstehend: **sofort** |
| Golang Go HIGH (30.07.) | Go | Falls KW31-Patch noch ausstehend: **sofort** |
| NGINX HIGH (30.07.) | NGINX | Durch KW32-Patch abgedeckt — verifizieren |
| Kubernetes HIGH (31.07.) | Kubernetes | Regulärer Patch-Zyklus |

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (Woche 17). Keine neuen EU-Acts via WebSearch KW32 identifiziert.
- **BfDI Pressemitteilungen** — RSS 404 (Woche 16). Keine BfDI-Pressemitteilungen KW32.
- **BSI Pressemitteilungen** — RSS 404 (Woche 16). BSI-WID-Advisory-Feed und Debian-Roundup als Kompensation.
- **e-Rechnung Bund (BMWK)** — RSS 404 (Woche 17). Keine neuen Regelungen.
- **BMAS (Arbeitsrecht)** — RSS 404 (Woche 17). Kein Bundestag-Schritt KW32.
- **ENISA** — RSS 404 (Woche 14). Keine neuen ENISA-Publikationen KW32.
- **EDPB Newsroom** — RSS 403. EDPB-Output via WebSearch abgedeckt (Breach Template Konsultation geschlossen).
- **EDPS** — 403. Keine neuen EDPS-Publikationen.
- **noyb** — RSS zugänglich; keine neue Klageinreichung KW32.

> **Wartungshinweis (Woche 17):** 6×404 + 2×403 persistent. Debian-Security-Roundup und WebSearch als Haupt-Kompensationskanäle. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — sofort

- [ ] **Nginx KW32 SOFORT patchen** — Debian DSA 08.08.2026: Remote Code Execution + DoS + Memory Disclosure. Reverse Proxy updaten, Deployment verifizieren. `#security #infra` → **sofort**
- [ ] **Redis KW32 SOFORT patchen** — Heap Overflow im RESTORE-Befehl (CVE-2026-23479 u.a.). Falls Cosmi Redis nutzt (Caching, Sessions, Queue): sofort updaten. `#security #infra` → **sofort**
- [ ] **Linux Kernel KW32 patchen** — Privilege Escalation + Memory Leaks. Alle Produktionsserver betroffen. `#security #infra` → **sofort**
- [ ] **KW31 Patches verifizieren** — GNU libc CRITICAL, Golang Go HIGH, NGINX HIGH (KW31-Batch) — Status auf allen Servern bestätigen. `#security #infra` → **sofort falls ausstehend**
- [ ] **NIS2 BSI-Registrierung** — Falls noch nicht registriert: Selbst-initiierte Spät-Registrierung jetzt durchführen (stärkster Mitigationsfaktor gegen Bußgeld). `#nis2 #legal` → **sofort**

### 🟡 Followup (KW33+)

- [ ] **Art. 50(1) Compliance-Status verifizieren** — Bundesnetzagentur nimmt Beschwerden entgegen. Alle KI-Touchpoints (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Kunden) auf Erstkontext-Offenlegung verifizieren. Screening-Log anlegen. `#aiact #legal #product` → **KW33**
- [ ] **EDPB Breach Template — SOP finalisieren** — Konsultation geschlossen. Draft-Template (7 Sektionen, 126 Felder) mit Cosmi-Incident-Response-SOP abgleichen. Lücken in Legal-Backlog aufnehmen. `#dsgvo #legal #security` → **KW33**
- [ ] **AI Act Hochrisiko-Klassifikation Cosmi-Schichten/HR-Features** — Prüfen ob Schichten-Algorithmen (Mitarbeiterzuweisung, automatische Planung) unter Annex III Art. 6(2) 4(a) fallen. Falls ja: Compliance bis 02.12.2027 planen. `#aiact #legal #schichten` → **Q4/2026**
- [ ] **EDPB/EC Stakeholder Event 15.10.2026 — Anmeldung bis 28.08.** — Event zu Datenschutz + Wettbewerbsrecht. Anmeldung oder Aufzeichnung einplanen falls Lead-Enrichment/Marktanalyse-Features geplant. `#dsgvo #legal` → **bis 28.08.2026**
- [ ] **DPF SCC-Fallback-Audit fortsetzen** — noyb-Klage erwartet. US-SaaS-Transfers inventarisieren, SCCs dokumentieren. `#dsgvo #legal #infra` → **bis Schrems-III-Einreichung**
- [ ] **Thunderbird KW32 patchen** — Falls Cosmi-Team Thunderbird nutzt: Update durchführen (RCE-Risiko). `#security` → **KW33**
- [ ] **EUDIW ARF v2.8.0 evaluieren** — Relying-Party-Anforderungen für Cosmi-Vertraege/Formulare. Q4-Sprint einplanen (147 Tage bis DE-Launch 02.01.2027). `#eidas #product` → **Q3/2026**
- [ ] **ArbZG-Referentenentwurf Schichten-Features** — Laufende Aufgabe: Wochenarbeitszeit-DB-Schema, elektronische Zeiterfassung als Compliance-Argument, Übergangsfrist-Konfiguration. `#arbzg #product #schichten` → **Q4/2026**
- [ ] **BSI C5:2026 Gap-Analyse starten** — 10 Monate bis Audit-Relevanz. DACH-B2B-Vertriebsvoraussetzung. `#nis2 #security` → **Q3/2026**
