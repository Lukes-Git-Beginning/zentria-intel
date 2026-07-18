---
date: 2026-07-18
type: regulation
runtime_minutes: 18
items_scanned: 72
items_relevant: 14
sources_live_rss: 1
sources_ok_list: [bsi-warnungen, noyb]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 10
kw: 29
---

# Regulation-Sweep KW29/2026 (Sa 18. Juli)

> **KW29-Scope:** 12–18. Juli 2026. Referenz-Sweep: KW28 (11. Juli). BSI-neue Items: 5 (KRITISCH×2, HOCH×3). WebSearch-Supplements: 10.
>
> **🔴 AI ACT CODE OF PRACTICE — SIGNING-DEADLINE 22. JULI (4 TAGE):** Das EU AI Office fordert Unternehmen auf, den Code of Practice on Transparency bis **22. Juli 2026** zu unterzeichnen. Signaturen erhalten eine Konformitätsvermutung (Presumption of Conformity) für Art. 50(2) und 50(4) — Beweislastumkehr gegenüber Aufsichtsbehörden. Danach bleibt Beitritt möglich, aber ohne rückwirkende Schutzwirkung ab 02.08.2026.
>
> **🔴 AI ACT ART. 50 TRANSPARENZ — 15 TAGE (02.08.2026):** Chatbot-Offenlegungspflicht unverändert. AI Omnibus unterzeichnet 8. Juli, OJ-Publikation erwartet 18.–25. Juli. Kein Aufschub für Art. 50. Bußgeld bis €15M oder 3 % Jahresumsatz.
>
> **🔴 NIS2 BSI-REGISTRIERUNG — 13 TAGE (31. JULI 2026):** Letzter Sprint. BSI: konsequente Durchsetzung ab 1. August. Bußgeld bis €10M / 2 % globaler Umsatz (Essential Entities), bis €500k (Wichtige Einrichtungen) + §38-GF-Haftung.
>
> **🔴 DPF ESKALIERT — SCHREMS III IN VORBEREITUNG:** US Supreme Court (Trump v. Slaughter, 29. Juni, 6:3) erklärt Entlassungsschutz für FTC-Kommissare für verfassungswidrig. Untergräbt FTC-Unabhängigkeit, auf der die EU-DPF-Adequacy-Entscheidung beruht. noyb bereitet Schrems-III-CJEU-Klage vor. DPF formal noch gültig — SCC-Fallback jetzt dokumentieren.
>
> **🔴 BSI KW29 — POSTGRESQL KRITISCH (16. JULI):** Alle PostgreSQL-Hauptversionen mit Sicherheitspatch (18.4/17.10/16.14/15.18/14.23): 11 CVEs, darunter Authorization-Bypass und DoS via SSL/GSS. Dazu: Samba KRITISCH (Code Execution). NGINX Plus HOCH (neues Advisory). nginx-ui HOCH (Root Code Execution). Ubuntu HOCH.

---

## DSGVO / Datenschutz

### 🟡 EDPB — Forderung nach Rechtsgrundlage für regulator-übergreifenden Informationsaustausch *(17. Juli 2026 — NEU)*

[EDPB Pressemitteilung — Cross-regulatory information sharing](https://www.edpb.europa.eu/news/edpb-calls-for-legal-basis-for-cross-regulatory-information-sharing_en) — EDPB, 17. Juli 2026

Das EDPB fordert einen klaren Rechtsrahmen, der den Informationsaustausch zwischen Datenschutzbehörden, Finanzaufsehern und Wettbewerbsbehörden ermöglicht — unter Wahrung der DSGVO. Hintergrund: zunehmende Überschneidungen bei regulatorischen Verfahren (AI Act, DORA, DSA, DMA).

*Cosmi-Implikation:* Für SaaS-Unternehmen, die unter mehrere EU-Regulierungen fallen (DSGVO + NIS2 + AI Act), steigt das Risiko koordinierter Aufsichtsverfahren. Langfristig beobachten. **Modul:** DSGVO / Legal. `#beobachten`

---

### 🟡 EDPB Binding Decision 1/2026 — Cookie-Banner-Durchsetzung bestätigt *(publiziert 14. Juli 2026 — NEU)*

[EDPB Binding Decision 1/2026 — Belgian DPA / noyb Cookie Complaint](https://www.edpb.europa.eu/news/edpb-requires-belgian-dpa-to-handle-the-merits-of-noyb-cookie-banner-complaint_en) — EDPB, verabschiedet 28. Mai / publiziert 14. Juli 2026

Das EDPB verpflichtet die belgische Datenschutzbehörde, eine noyb-Beschwerde gegen irreführende Cookie-Banner in der Sache zu prüfen (statt auf "mangelnde Ressourcen" zu verweisen). Die EDPB bestätigt: Cookie-Compliance gilt einheitlich für alle Organisationen — keine Ausnahme für Unternehmen mit hohem Beschwerdeaufkommen. noyb feiert dies als Präzedenzfall für ganz Europa.

**Anforderungen die bestätigt werden:**
- "Ablehnen" muss gleich prominent und einfach sein wie "Zustimmen"
- Dark Patterns (Pre-Ticked Boxes, versteckte Reject-Buttons) sind nicht konform
- Alle Cookie-Kategorien müssen einzeln abwählbar sein

*Cosmi-Implikation:* Falls Cosmi eigene Marketing-Seiten, Kundenportale oder Login-Flows mit Cookie-Consent-Bannern betreibt: sofortiger Compliance-Check. Besondere Aufmerksamkeit auf Analytics-Cookies (GA4, Mixpanel o.ä.) und Tracking-Pixels. `#followup` **Modul:** DSGVO / Legal / Product.

---

### 🔴 DPF ESKALIERT — SCOTUS Trump v. Slaughter + Schrems III angekündigt *(KW29 KRITISCH-UPGRADE)*

[noyb DPF-Analyse](https://noyb.eu/en) | [activemind: SCOTUS DPF Analyse](https://www.activemind.legal/guides/dpf-supreme-court/) | [Latombe-Klage (CJEU pending)](https://btlj.org/2026/02/third-times-the-charm-the-fate-of-the-eu-u-s-data-privacy-framework/)

**Neuer Eskalationsgrund KW29:**

Am **29. Juni 2026** urteilte der US Supreme Court (6:3, Trump v. Slaughter): Gesetzliche Einschränkungen, die den Präsidenten an der Entlassung von FTC-Kommissaren hindern, sind verfassungswidrig. Direkte Konsequenz: Die **Unabhängigkeit der FTC** — auf der die EU-Kommission ihre DPF-Adequacy-Entscheidung 2023 aufgebaut hat — ist rechtlich untergraben.

**noyb-Reaktion (KW29):** Ankündigung einer **Schrems-III-CJEU-Klage** binnen Wochen bis Monaten. Schrems: "Keine andere US-Behörde kann diesen Mangel beheben."

**Aktuelle Risikolandschaft:**

| Klage | Status | Erwartetes Urteil |
|-------|--------|-------------------|
| Latombe v. EC (CJEU) | Pending | Q4/2026–Q1/2027 |
| Schrems III (noyb) | Angekündigt, noch nicht eingereicht | 2027–2028 |
| DPF Adequacy-Entscheidung | Formal gültig | — |

*Cosmi-Implikation:* DPF-Risiko ist von `mittel` auf `hoch` eskaliert. Das SCC-Fallback-Audit aus KW27 ist jetzt dringend: (1) US-SaaS-Transfers inventarisieren, (2) SCCs als Primärmechanismus dokumentieren (DPF nur noch als Ergänzung behandeln), (3) Supplementary Technical Measures (Verschlüsselung, Pseudonymisierung) evaluieren. Timing: noyb-Klage kann binnen Wochen eingereicht werden. **Modul:** DSGVO / Legal / Infra. `#followup`

---

### BfDI — Führungswechsel: Prof. Dr. Moritz Hennemann gewählt *(KW29 — NEU)*

Prof. Dr. Louisa Specht-Riemenschneider zieht sich aus gesundheitlichen Gründen zurück. Der Bundestag hat **Prof. Dr. Moritz Hennemann** als Nachfolger gewählt. Specht-Riemenschneider bleibt bis **30. September 2026** im Amt. Hennemann ist Datenschutzrechtler mit Schwerpunkten Plattformregulierung und algorithmische Entscheidungsfindung.

*Cosmi-Implikation:* Mögliche Verschiebung der deutschen Durchsetzungsschwerpunkte (weg von Telekommunikation, stärker Richtung Plattformen / Algorithmen). Beobachten. `#beobachten`

---

## AI Act

### 🔴 AI Act Code of Practice on Transparency — Signing-Deadline **22. Juli 2026** *(KW29 NEU — 4 TAGE)*

[EU AI Act Service Desk — Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) | [TechTimes Chatbot Disclosure](https://www.techtimes.com/articles/318822/20260622/eu-ai-act-chatbot-disclosure-deepfake-labeling-july-22-signatory-deadline.htm) | [OriginBrief AI Policy Weekly 13. Juli](https://www.originbrief.app/en/reports/ai-regulation-policy/2026-07-13/weekly)

**Bis KW29 unbekannte Deadline:** Das EU AI Office bietet Unternehmen bis **22. Juli 2026** die Möglichkeit, den Code of Practice on Transparency for AI-Generated Content zu unterzeichnen.

**Warum das relevant ist:**

| Vorteil für Signatoren | Details |
|------------------------|---------|
| **Presumption of Conformity** | Gilt für Art. 50(2) Wasserzeichen und Art. 50(4) KI-Content-Kennzeichnung |
| Beweislastumkehr | Regulierer muss beweisen, dass man NICHT konform ist (statt umgekehrt) |
| Regulatorische Sicherheit | Für 3-Monats-Übergangsfrist (bis 02.12.2026) besonders wertvoll |

**Nach dem 22. Juli:** Beitritt weiterhin möglich, aber ohne rückwirkende Konformitätsvermutung ab 02.08.2026.

*Cosmi-Implikation:* **Entscheidung bis Dienstag 22. Juli.** Prüfen: (1) Setzt Cosmi Art. 50(2)-pflichtige Systeme (synthetische Stimmen, Deepfakes, KI-generierte Bilder) ein? (2) Nutzt Cosmi GenAI für Content-Erstellung, den Endkunden sehen? Wenn ja: Code of Practice unterzeichnen als kostengünstige regulatorische Absicherung. Unterzeichnung verpflichtet zu Transparenz-Maßnahmen, schützt aber gleichzeitig vor Bußgeldern. **Modul:** AI Act / Legal / Product. `#akut → bis 22. Juli`

---

### 🔴 AI-Omnibus: OJ-Publikation erwartet diese Woche — Art. 50 in 15 Tagen *(KW29 KRITISCH)*

[Gibson Dunn — AI Omnibus Key Amendments](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) | [Addleshaw Goddard — Formally Adopted](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/) | [Freshfields AI Act Unpacked #34](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber)

**Stand 18. Juli:** Rat-Beschluss 29. Juni, Unterzeichnung 8. Juli. OJ-Eintrag erwartet 18.–25. Juli. Inkrafttreten 3 Tage nach OJ-Publikation.

**Fristenübersicht nach Omnibus:**

| Pflicht | Frist | Δ gg. KW28 |
|---------|-------|------------|
| **Art. 50 Transparenz** (Chatbot-Offenlegung) | **02.08.2026 — 15 TAGE** | –7 Tage |
| Art. 50(2)+(4) KI-Content-Wasserzeichen / Kennzeichnung | bis **02.12.2026** (Übergangsfrist 3 Mon.) | NEU KLAR |
| **Annex III Standalone-Hochrisiko** | **02.12.2027** | = |
| Annex I Hochrisiko (in regulierten Produkten) | 02.08.2028 | = |
| GPAI-Pflichten | seit 02.08.2025 in Kraft | = |
| Sanktionen Art. 50 | **€15M oder 3 % Jahresumsatz** | NEU bestätigt |

*Cosmi-Implikation:* Keine Änderung zur Vorwoche — Chatbot-Offenlegung muss bis **02.08.2026** live sein. 15 Tage verbleiben. Falls noch nicht umgesetzt: Notfall-Sprint jetzt. **Modul:** AI Act / Legal / Product. `#akut`

---

## NIS2

### 🔴 NIS2 BSI-Registrierung — Frist 31. Juli 2026 — **13 Tage — letzter Sprint** *(KW29 KRITISCH)*

[Creditreform Compliance — NIS2 letzte Frist](https://www.creditreform-compliance.de/aktuelles/nis2-das-bsi-setzt-die-letzte-frist-registrierung-bis-zum-31-juli-2026/) | [Solidaris — Letzte Chance](https://www.solidaris.de/aktuelles/letzte-chance-bsi-setzt-neue-frist-bis-31-juli-2026-fuer-nis-2-registrierung/) | [portal.bsi.bund.de](https://portal.bsi.bund.de)

Keine neuen Registrierungszahlen diese Woche. Stand Ende Mai: ~18.500/29.500. Frist läuft unverändert am 31. Juli ab.

**Bußgeldstruktur (KW29 — präzisiert):**

| Kategorie | Maximales Bußgeld |
|-----------|-------------------|
| Wichtige Einrichtungen | bis **€500.000** (§ 60 BSIG) |
| Essential Entities | bis **€10.000.000 oder 2 %** globaler Jahresumsatz |
| GF-Haftung | §38 BSIG — persönlich, uneingeschränkt |

*Cosmi-Implikation:* Keine Änderung — Registrierung via [portal.bsi.bund.de](https://portal.bsi.bund.de) bis **spätestens 28. Juli (Puffer)**. Wenn noch nicht geprüft ob Cosmi als Managed-IT-Dienst, Cloud-Provider oder digitale Infrastruktur fällt: sofort klären. **Modul:** NIS2 / Legal / Management. `#akut`

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche — keine neuen Regelungen KW29

Fristen-Status (unverändert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) — Pflicht |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt (Umsatz ≤ €800k bis 31.12.2027) |
| ab 01.01.2027 | **Versandpflicht** Umsatz > €800k Vorjahresumsatz |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

> **Neu auf dem Radar (KW29):** Der **EU Data Act** tritt am **12. September 2026** mit seinen Kern-Datenzugangs-Pflichten in Kraft. Betrifft Cloud- und SaaS-Anbieter: Datenzugang, Portabilität und Switching müssen API-seitig ermöglicht werden. Für Cosmi-CRM relevante Prüfung: Sind Export-APIs und Daten-Portabilitätsfunktionen konform? **56 Tage.** `#followup`

---

## ArbZG / Arbeitsrecht

### Stille Woche — kein Parlamentsbeschluss KW29

BMAS-Referentenentwurf (Wechsel von Tages- zu Wochenarbeitszeit-Obergrenzen) weiterhin in der Diskussion. Gewerkschaften lehnen ab, Arbeitgeberverbände befürworten. Kein Bundestagsbeschluss erwartet vor Herbst 2026.

---

## eIDAS

### Stille Woche — Digitale-Identitäten-Gesetz in Kraft (Mai 2026)

Das Bundeskabinett hat am 20. Mai 2026 das **Digitale-Identitäten-Gesetz** verabschiedet, das die EUDI-Wallet-Implementierung in Deutschland regelt. ARF v2.8.0 ist operativ. Deutschland-Launch EUDIW: **02. Januar 2027** (168 Tage).

Keine neuen technischen Specifications KW29.

---

## BSI-Warnings — KW29 (12.–18. Juli 2026)

> **KW29-Überblick:** Ruhigere Woche als KW28 — aber mit bedeutendem PostgreSQL-Patch-Release (16. Juli) und Samba-KRITISCH. NGINX-Advisory-Serie setzt sich fort. nginx-ui als Management-Interface verdient besondere Aufmerksamkeit (Root-Execution-Vektor).

---

### 🔴 KRITISCH — Sofortiger Handlungsbedarf

| Advisory | Produkt | Angriffsvektor | Datum | Status |
|----------|---------|----------------|-------|--------|
| [PostgreSQL Release](https://www.postgresql.org/about/news/postgresql-184-1710-1614-1518-and-1423-released-3297/) | **PostgreSQL** (alle Versionen) | Authorization Bypass, DoS (SSL/GSS) | 16. Jul | **NEU** |
| [WID-SEC-2026-1686](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1686) | **Samba** | Remote: Code Execution + DoS | 14. Jul | **NEU** |

> **🚨 PostgreSQL Security Release (KRITISCH, 16. Jul):** Betrifft **alle** in der Praxis eingesetzten PostgreSQL-Versionen (14–18). 11 CVEs: (1) Missing authorization in `CREATE TYPE` ermöglicht Timing-basierten MD5-Passwort-Recovery-Angriff; (2) Uncontrolled recursion in SSL/GSS negotiation (DoS). Sofort auf **18.4 / 17.10 / 16.14 / 15.18 / 14.23** updaten — Patches seit 16. Juli verfügbar. **Direkt Cosmi-relevant** wenn PostgreSQL als primäre Datenbank eingesetzt wird.
>
> **🚨 Samba WID-SEC-2026-1686 (KRITISCH):** Remote Code Execution und Denial of Service. Relevant für alle Linux-Server mit Samba-Fileserving oder AD-Kompatibilität. Sofort patchen.

---

### 🟠 HOCH — Cosmi-relevante Infrastruktur

| Advisory | Produkt | Angriffsvektor | Datum | Status |
|----------|---------|----------------|-------|--------|
| [WID-SEC-2026-2383](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2383) | **NGINX Plus** | Code Execution | 15. Jul | **NEU** |
| [WID-SEC-2026-2390](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2390) | **nginx-ui** | Root-Level Code Execution | 15. Jul | **NEU** |
| [WID-SEC-2026-2393](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2393) | **Ubuntu Linux** (ubuntu-pro-client) | Code Execution (Admin) | 16. Jul | **NEU** |

> **NGINX Plus WID-SEC-2026-2383 (HOCH, NEU):** Weiteres Advisory für NGINX Plus in Ergänzung zu den 4 KW28-Advisories. Falls NGINX Plus im Stack: alle offenen Advisories (WID-SEC-2026-0860/1995/1661/1527/2383) gemeinsam patchen.
>
> **nginx-ui WID-SEC-2026-2390 (HOCH, NEU):** nginx-ui ist ein Web-Management-Interface für NGINX-Konfiguration. Root-Level-Code-Execution-Schwachstelle ist besonders gefährlich, da Management-Interfaces oft weitreichende Berechtigungen haben. Falls nginx-ui für Server-Management eingesetzt: sofort prüfen und patchen oder deaktivieren.
>
> **Ubuntu linux WID-SEC-2026-2393 (HOCH):** ubuntu-pro-client mit Code-Execution-Schwachstelle (Admin-Rechte). Falls Ubuntu-Server-Fleet mit ubuntu-pro: sofort patchen.

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (14. Woche). AI-Omnibus-OJ-Eintrag: noch nicht verifiziert, Publikation diese Woche erwartet.
- **BfDI Pressemitteilungen** — RSS 404 (13. Woche). BfDI-Führungswechsel via WebSearch abgedeckt.
- **BSI Pressemitteilungen** — RSS 404 (13. Woche).
- **e-Rechnung Bund (BMWK)** — RSS 404 (14. Woche). Keine neuen XRechnung-Regelungen KW29.
- **BMAS (Arbeitsrecht)** — RSS 404 (14. Woche). ArbZG-Reform ohne Bundestags-Beschluss.
- **ENISA** — RSS 404 (11. Woche). Keine neuen NIS2-Leitlinien KW29.
- **EDPB Newsroom** — RSS 403 Forbidden. EDPB-Inhalte via WebSearch (Binding Decision 1/2026 Cookie, Cross-regulatory info sharing).
- **EDPS** — 403 Forbidden.
- **noyb** — RSS zugänglich, aber neue Inhalte nur via WebSearch rekonstruierbar. DPF-SCOTUS-Reaktion + Schrems-III-Ankündigung erfasst.

> **Wartungshinweis (Woche 14):** 6×404 + 2×403 weiterhin. EDPB Direct-Scraping als Fallback weiterhin ausstehend. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — innerhalb der nächsten 14 Tage

- [ ] **AI Act Code of Practice on Transparency unterzeichnen (Entscheidung bis 22. Juli — 4 Tage)** — EU AI Office Code of Practice on Transparency for AI-Generated Content. Signatoren erhalten Presumption of Conformity für Art. 50(2)+(4). Prüfen: Setzt Cosmi Art. 50(2)-pflichtige Systeme ein (synthetische Sprache, GenAI-Content der Endkunden erreicht)? Wenn ja: kostenlose regulatorische Absicherung. `#aiact #legal #product` → **bis 22. Juli**
- [ ] **AI Act Art. 50 Transparenz — 15 Tage — GO/NO-GO-Check** — Chatbot/Assistent-Offenlegung: Alle Touchpoints live? App-Widget, Support-Chat, E-Mail-Automation, API-Kunden. Frist: **02.08.2026** — kein Aufschub. Bußgeld: bis €15M oder 3 % globaler Umsatz. `#aiact #legal #product` → **bis 25. Juli**
- [ ] **NIS2 BSI-Registrierung — 13 Tage — letzter Aufruf** — Frist **31. Juli 2026**. Registrierung via [portal.bsi.bund.de](https://portal.bsi.bund.de) mit Puffer bis **28. Juli**. Essential Entities: bis €10M / 2 % globaler Umsatz + GF-Haftung. `#nis2 #legal #management` → **bis 28. Juli**
- [ ] **PostgreSQL sofort patchen (KRITISCH, 16. Juli)** — Update auf 18.4 / 17.10 / 16.14 / 15.18 / 14.23. Authorization Bypass + SSL/GSS DoS. Falls PostgreSQL als Primär-DB: Notfall-Update heute. `#security #infra` → **sofort**
- [ ] **Samba patchen (KRITISCH, WID-SEC-2026-1686)** — Remote Code Execution + DoS. Falls Samba im Stack: sofort patchen. `#security #infra` → **sofort**
- [ ] **DPF SCC-Fallback-Audit starten (Eskalation KW29)** — SCOTUS Trump v. Slaughter untergräbt FTC-Unabhängigkeit. Schrems III angekündigt. SCCs jetzt als Primärmechanismus für alle US-Datenübertragungen dokumentieren (nicht mehr nur als Fallback). `#dsgvo #legal #infra` → **bis 25. Juli**

### 🟡 Followup (KW30+)

- [ ] **nginx-ui patchen oder deaktivieren (HOCH, WID-SEC-2026-2390)** — Root Code Execution in NGINX-Management-Interface. Falls nginx-ui im Stack: kritisches Patch-Risiko. `#security #infra`
- [ ] **NGINX Plus WID-SEC-2026-2383 patchen (HOCH, NEU)** — 5. NGINX-Advisory in 2 Wochen. Alle NGINX/NGINX-Plus-Advisories KW28–29 zusammen abarbeiten. `#security #infra`
- [ ] **Ubuntu ubuntu-pro-client patchen (HOCH, WID-SEC-2026-2393)** — Falls ubuntu-pro aktiv auf Servern. `#security #infra`
- [ ] **EDPB Data Breach Notification Template (Konsultation bis 05.08.2026)** — Template herunterladen, Incident-Response-SOP vergleichen, Lücken schließen. `#dsgvo #security`
- [ ] **EU Data Act — September 12, 2026 (56 Tage)** — Cloud/SaaS-Datenzugang und Portabilitätspflichten. Cosmi-CRM: Export-APIs auf Data-Act-Konformität prüfen (Switching-Möglichkeit für Kunden). `#legal #product #infra`
- [ ] **EDPB Cookie-Banner-Compliance-Check (Binding Decision 1/2026)** — Alle Cosmi-eigenen Consent-Flows: "Ablehnen" gleich prominent wie "Akzeptieren"? Kein Dark-Pattern. `#dsgvo #legal #product`
- [ ] **AI-Omnibus OJ täglich prüfen** — Erwartet 18.–25. Juli. Sobald publiziert: finale Compliance-Roadmap mit Annex-III-Datum 02.12.2027 einfrieren. `#aiact #legal`
- [ ] **Schrems III / DPF Monitoring** — noyb-Klageeinreichung beobachten. EC-Statement nach SCOTUS-Urteil verfolgen. `#dsgvo #legal #infra`
- [ ] **BfDI Schwerpunktverschiebung beobachten** — Prof. Hennemann (Algorithmen / Plattformen) ab 01.10.2026. DSGVO-Durchsetzungsfokus in Deutschland könnte sich verschieben. `#dsgvo #legal`
- [ ] **EDPB Anonymisation Guidelines Konsultation** — bis 30. Oktober 2026. Eigene Implementierungsansätze dokumentieren. `#dsgvo #legal`
- [ ] **EUDIW Relying-Party-Vorbereitung** — Deutschland-Launch 02.01.2027 (168 Tage). Sprint-Planung Q4. `#eidas #product`
- [ ] **`sources/_regulation.yaml` Pflege (Woche 14)** — EDPB Direct-Scraping-Fallback testen. `#maintenance`
