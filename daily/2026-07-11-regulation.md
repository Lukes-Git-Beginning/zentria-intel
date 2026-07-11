---
date: 2026-07-11
type: regulation
runtime_minutes: 22
items_scanned: 85
items_relevant: 15
sources_live_rss: 1
sources_ok_list: [bsi-warnungen, noyb]
sources_403_list: [edpb-newsroom, oedp-eaid]
sources_404_list: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu]
websearch_supplements: 5
kw: 28
---

# Regulation-Sweep KW28/2026 (Sa 11. Juli)

> **KW28-Scope:** 5–11. Juli 2026. Referenz-Sweep: KW27 (4. Juli). Neue BSI-Items: ~35 (KRITISCH×3, HOCH-Welle Linux/NGINX/RabbitMQ). WebSearch-Supplements: 5 Policy-Updates.
>
> **🟢 EDPB ANONYMISIERUNGS-LEITLINIEN 02/2026 VERABSCHIEDET — 7. JULI 2026:** Das Sprint-Team hat geliefert. Neuer 3-Kriterien-Test (No-Isolation + No-Linkage + No-Inference), abgeleitet aus CJEU C-413/23 P. Öffentliche Konsultation bis **30. Oktober 2026**. Cosmi-Anonymisierungsroutinen müssen gegen diesen Standard validiert werden. Gleichzeitig: Web-Scraping-Guidelines für Generative AI + finale Blockchain-Guidelines verabschiedet.
>
> **🔴 AI ACT ART. 50 TRANSPARENZ — NUR NOCH 22 TAGE (02.08.2026):** OJ-Publikation des AI-Omnibus weiterhin ausstehend. Art. 50 Chatbot-Offenlegungspflicht gilt **unverändert** ab 02.08.2026. Kein Aufschub.
>
> **🔴 NIS2 BSI-REGISTRIERUNG: FRIST 31. JULI 2026 — NUR NOCH 20 TAGE:** Stand Ende Mai: ~18.500 von ~29.500 betroffenen Unternehmen registriert. ~11.000 fehlen noch. BSI wird nach der Frist konsequent durchsetzen.
>
> **🔴 BSI KW28 — GNU LIBC KRITISCH (CVSS 9.8, WID-SEC-2026-1190):** Remote/Unauthenticated-Angreifer kann Dateien manipulieren und beliebigen Code ausführen. Betrifft alle Linux/UNIX-Deployments. Plus: Python KRITISCH (Code Execution), Flowise KRITISCH (AI-Orchestration, RCE), NGINX HOCH (4 Advisories), RabbitMQ HOCH (Code Execution), Linux-Kernel-Welle (18+ Updates).

---

## DSGVO / Datenschutz

### 🟢 EDPB — Anonymisierungs-Leitlinien 02/2026 verabschiedet *(7. Juli 2026 — NEU)*

[EDPB Guidelines 02/2026 on Anonymisation v1.0](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf) — EDPB, 7. Juli 2026 | [Pressemitteilung](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en) | [TechTimes-Analyse](https://www.techtimes.com/articles/320015/20260709/eu-anonymization-rules-tightened-ai-inference-attacks-drive-new-three-test-standard.htm) | [RD Privacy Watch](https://www.rdprivacywatch.com/article/b5c19848-ce93-4104-976e-8c40fa01c9d8)

Das EDPB-Sprint-Team hat — wie angekündigt — die lang erwarteten Anonymisierungs-Guidelines im Sommer 2026 abgeschlossen. Grundlage: CJEU-Urteil C-413/23 P EDPS v SRB (4. September 2025) und weitere CJEU-Rechtsprechung.

**Kerninhalte:**

| Kriterium | Definition |
|-----------|-----------|
| **No Record Isolation** | Einzelne Datensätze können nicht aus dem Datensatz isoliert werden |
| **No Linkage** | Datensätze lassen sich nicht mit anderen Datensätzen verknüpfen |
| **No Inference** | Aus den Daten können keine Rückschlüsse auf Individuen gezogen werden |

Alle drei Kriterien müssen erfüllt sein, damit Daten als anonym gelten. Falls auch nur ein Kriterium nicht erfüllt ist, gilt das Datum weiterhin als personenbezogen und fällt unter die DSGVO.

**Zwei Bewertungsansätze:**
- *Contextual Approach*: Berücksichtigt unterschiedliche Capabilities verschiedener potentieller Re-Identifikatoren (realistischer, aber aufwändiger)
- *Simplified Approach*: Ignoriert diese Unterschiede — konservativer, einfacher zu implementieren

**Wichtig für KI-Anwendungen:** Die Guidelines berücksichtigen explizit moderne Inference-Angriffe. Ein Datensatz der bisher als "anonym" galt (z. B. aggregierte Metriken) kann nach dem neuen 3-Kriterien-Test als nicht-anonym eingestuft werden, wenn Inference-Angriffe via ML möglich sind.

**Status:** Öffentliche Konsultation bis **30. Oktober 2026**. Nach Finalisierung: bindender Rahmen für alle EU-Anonymisierungsansätze.

*Cosmi-Implikation:* **Sofortiger Review aller Anonymisierungsroutinen.** Betroffen: (1) Reporting/Analytics-Datenexporte, (2) Churn-Prediction und Lead-Scoring-Trainings-Datasets, (3) Kundendaten in Development/Staging-Umgebungen, (4) alle "aggregierten" Metriken die an Kunden exportiert werden. Der Simplified Approach bietet einen pragmatischen Einstieg. Bis 30. Oktober 2026 können Konsultations-Kommentare eingereicht werden — eigene Implementierungsansätze dokumentieren und ggf. kommentieren. **Modul:** DSGVO / Legal / Product / Data. `#akut`

---

### 🟡 EDPB — Web-Scraping-Guidelines für Generative AI verabschiedet *(7. Juli 2026 — NEU)*

[EDPB Pressemitteilung — Web Scraping for Generative AI](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en) — EDPB, 7. Juli 2026

Gleichzeitig mit den Anonymisierungs-Guidelines hat das EDPB Leitlinien zu Web Scraping im Kontext von Generativer KI verabschiedet.

**Kernanforderungen:**
- DSGVO gilt, sobald Web Scraping personenbezogene Daten umfasst (auch als Zwischenprodukt beim Training)
- Gültige Rechtsgrundlage nach Art. 6 DSGVO erforderlich (+ Art. 9(2) für besondere Kategorien)
- Zweckbindung (Purpose Limitation) und Transparenz müssen eingehalten werden
- Datenherkunft dokumentieren, Timestamps aufzeichnen
- Datenminimierung: Nur scrapen was für den Zweck notwendig ist
- Vor Training: Datenvalidierung zur Einhaltung des Genauigkeitsprinzips

**Besondere Kategorien:** Wenn Scraping auf besondere Datenkategorien stößt (Gesundheit, Politische Meinung, etc.), müssen sowohl Art. 6 als auch Art. 9(2)-Ausnahme vorliegen.

*Cosmi-Implikation:* Falls Cosmi Web Scraping für Lead-Enrichment, Firmendaten-Anreicherung oder KI-Modell-Training einsetzt: Rechtsgrundlagen und Dokumentation prüfen. Transparency-Pflicht kann problematisch sein wenn Scraping-Targets keine Datenschutzhinweise erhalten. **Modul:** DSGVO / Legal / Product / AI. `#followup`

---

### EDPB — Blockchain-Leitlinien: Finale Version verabschiedet *(7. Juli 2026 — NEU)*

[EDPB Blockchain Guidelines — Finale Version](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en) — EDPB, 7. Juli 2026

Finale Version nach öffentlicher Konsultation. Klärt DSGVO-Compliance-Anforderungen für verschiedene Blockchain-Architekturen (Public, Private, Consortium-Chains) und die Implikationen für Personendatenverarbeitung.

*Cosmi-Implikation:* Nur relevant falls Cosmi Blockchain-basierte Audit-Trails, NFT-Verträge oder DLT-Zahlungsmodule plant. Für Standard-CRM-Betrieb: `#beobachten`

---

### DPF-Krise — EC hält weiterhin an Adequacy-Entscheidung fest *(Carry-over, Monitoring)*

[CJEU-Klage Latombe — Pending](https://btlj.org/2026/02/third-times-the-charm-the-fate-of-the-eu-u-s-data-privacy-framework/) | [DPF Program Overview](https://www.dataprivacyframework.gov/Program-Overview)

**Aktuelle Lage (KW28):** Die Europäische Kommission hat die DPF-Adequacy-Entscheidung **nicht zurückgezogen**. DPF ist formal weiterhin gültig. Keine neuen Statements der EC diese Woche.

**CJEU-Klage:** Philippe Latombe (Oktober 2025 filed) — Voraburteil erwartet Ende 2026 / Anfang 2027.
**noyb:** Keine neuen Artikel seit 29. Juni 2026. Angekündigte CJEU-Klage (Zeitrahmen 2–3 Jahre): noch nicht eingereicht.
**~2.800 Organisationen** halten aktive DPF-Zertifizierungen (Stand 2026).

*Cosmi-Implikation:* DPF bleibt riskant. Das Sofort-Audit aus KW27 (US-SaaS-Abhängigkeiten inventarisieren, SCCs als Fallback) bleibt aktuell. EC-Druck durch Latombe-Klage und noyb steigt — OJ-Entscheidung kann binnen Wochen kommen. **Modul:** DSGVO / Legal / Infra. `#beobachten`

---

## AI Act

### 🔴 AI-Omnibus: OJ-Publikation weiterhin ausstehend — Art. 50 in 22 Tagen *(KW28 KRITISCH)*

[Addleshaw Goddard: AI Omnibus formally adopted](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/) | [Gibson Dunn Analyse](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) | [Consilium 29. Juni](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/)

Stand: EU-Rat stimmte **29. Juni 2026** zu. OJ-Publikation steht aus — Inkrafttreten 3 Tage nach OJ-Eintrag. Täglich überwachen.

**Fristen (nach Omnibus — sobald OJ publiziert):**

| Pflicht | Frist |
|---------|-------|
| **Art. 50 Transparenz** (Chatbot-Offenlegung) | **02.08.2026 — UNVERÄNDERT, 22 TAGE** |
| Art. 50(2) Wasserzeichen (für Systeme vor 02.08 auf dem Markt) | bis 02.12.2026 Übergangsfrist |
| **Annex III Standalone-Hochrisiko** (Lead-Scoring, Recruiting, Kreditscoring) | **02.12.2027** (+16 Mon.) |
| Annex I Hochrisiko in regulierten Produkten | 02.08.2028 |
| GPAI-Pflichten | Bereits in Kraft (seit 02.08.2025) |

*Cosmi-Implikation:* **Art. 50 gilt ab 02.08.2026 — das ist in 22 Tagen.** Chatbot-Offenlegung muss live sein. Prüfen: (1) Zeigt der Cosmi-Chatbot/Assistent klar an, dass Nutzer mit einem KI-System interagieren? (2) Gilt das für alle Touchpoints (App, Support-Widget, E-Mail-Responses)? Annex-III-Assessment kann bis 02.12.2027 intern gestemmt werden — aber Dokumentation jetzt fertigstellen. **Modul:** AI Act / Legal / Product. `#akut`

---

## NIS2

### 🔴 NIS2 BSI-Registrierung: Nachfrist läuft ab — **31. Juli 2026** *(KW28 ESKALIERT — 20 Tage)*

[Solidaris: Letzte Chance NIS2](https://www.solidaris.de/aktuelles/letzte-chance-bsi-setzt-neue-frist-bis-31-juli-2026-fuer-nis-2-registrierung/) | [IT-Boltwise: BSI Nachfrist](https://www.it-boltwise.de/nis-2-registrierung-bsi-verlaengert-frist-bis-31-juli-2026.html) | [locaterisk.com](https://locaterisk.com/en/nis2-bsi-registrierung-frist-2026/)

**Stand KW28:** ~**18.500** Unternehmen registriert (Stand Ende Mai 2026) von ~**29.500** betroffenen. **~11.000 Unternehmen fehlen noch.** Das BSI hat angekündigt, nach dem 31. Juli konsequent durchzusetzen.

**Konsequenzen bei Nichtregistrierung nach 31. Juli:**
- Bußgeld bis **€500.000** (§ 60 BSIG)
- **Persönliche Haftung** der Geschäftsführung (§38 BSIG)
- Keine weitere Verlängerung erwartet

*Cosmi-Implikation:* Falls Cosmi als Anbieter von Managed IT-Diensten, Cloud-Computing-Diensten oder digitaler Infrastruktur unter NIS2 (§28 BSIG) fällt: Registrierung über [portal.bsi.bund.de](https://portal.bsi.bund.de) bis **spätestens 25. Juli (Puffer)**. GF-Haftung ist ernst zu nehmen. **Modul:** NIS2 / Legal / Management. `#akut`

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche — keine neuen Regelungen KW28

Fristen-Status (unverändert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) — Pflicht |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz >800.000 € Vorjahresumsatz |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

---

## ArbZG / Arbeitsrecht

### Stille Woche — Mindestlohn-Anpassungen vom 1. Juli gelten (Carry-over)

Keine neuen Entwicklungen KW28. ArbZG-Reform weiterhin politisch diskutiert, kein Parlamentsbeschluss. Minijob-RV-Pflicht (ab 01.07.2026) und Pflege-Mindestlöhne gelten — siehe KW27-Sweep.

---

## eIDAS

### Stille Woche — Deutschland-Launch EUDIW 02.01.2027 unverändert

Keine neuen Entwicklungen KW28. Large Scale Pilots laufen. Technische Implementing Regulations verfügbar. EUDI-Wallet-Launch Deutschland: 02.01.2027.

---

## BSI-Warnings — KW28 (5.–11. Juli 2026)

> **KW28-Überblick:** Massive Update-Welle zum Wochenschluss (10. Juli). 3 kritische Advisories, davon 2 mit Remote/Unauthenticated-Vektor. Linux-Kernel-Welle mit 18+ Updates. Besonders relevant für SaaS: GNU libc (CVSS 9.8, alle Linux-Deployments), NGINX (Web-Server, 4 Advisories), RabbitMQ (Message Queue, NEU, Code Execution).

---

### 🔴 KRITISCH — Sofortiger Handlungsbedarf

| Advisory | Produkt | CVSS | Angriffsvektor | Datum | Status |
|----------|---------|------|----------------|-------|--------|
| [WID-SEC-2026-1190](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1190) | **GNU libc** | 9.8 | Remote/Unauth: File Manipulation, DoS, RCE | 10. Jul (UPDATE) | KRITISCH |
| [WID-SEC-2022-0253](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2022-0253) | **Python** | k.A. | Remote/Unauth: Arbitrary Code Execution | 10. Jul (UPDATE) | KRITISCH |
| [WID-SEC-2025-2048](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2025-2048) | **Flowise** (AI-Orchestration) | k.A. | Remote/Unauth: Code Execution + Info Disclosure | 10. Jul (UPDATE) | KRITISCH |

> **🚨 GNU libc WID-SEC-2026-1190 (KRITISCH, CVSS 9.8, 10. Jul):** CVEs: CVE-2026-5358, CVE-2026-5450, CVE-2026-5928. Betrifft GNU libc ≤ 2.43 auf allen Linux/UNIX-Systemen (inkl. Red Hat, Fedora, SUSE). Remote/Unauthenticated-Angreifer kann Dateien manipulieren, DoS auslösen und ggf. Code ausführen. **Betrifft alle Linux-basierten Backend-Dienste** — sofort Distribution-Patch einspielen (distro-seitiger Fix verfügbar über Paketmanager).
>
> **🚨 Python WID-SEC-2022-0253 (KRITISCH, 10. Jul — Update):** Remote/Unauthenticated Code Execution. Ältere Advisory-Nummer (2022) bedeutet: vorhandene Advisory erhielt neues CVE/Update. Falls Python im Backend oder für Skripte eingesetzt: Python-Version prüfen und aktualisieren.
>
> **🚨 Flowise WID-SEC-2025-2048 (KRITISCH, 10. Jul — Update):** Flowise ist eine Open-Source AI-Orchestrierungsplattform (LLM Chains, Agents). Remote/Unauth: Code Execution + Information Disclosure. Falls Cosmi Flowise für KI-Workflow-Automatisierung nutzt: sofort patchen oder isolieren.

---

### 🟠 HOCH — Cosmi-relevante Infrastruktur

| Advisory | Produkt | Datum | Angriffsvektor | Status |
|----------|---------|-------|----------------|--------|
| [WID-SEC-2026-0860](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0860) | **NGINX** | 10. Jul | Remote/Unauth: DoS, Data Manipulation | UPDATE |
| [WID-SEC-2026-1995](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1995) | **NGINX Plus** | 10. Jul | Remote/Unauth: DoS | UPDATE |
| [WID-SEC-2026-1661](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1661) | **NGINX** | 10. Jul | Remote/Unauth | UPDATE |
| [WID-SEC-2026-1527](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1527) | **NGINX** | 10. Jul | Remote/Unauth | UPDATE |
| [WID-SEC-2026-2268](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2268) | **RabbitMQ** | 10. Jul | Remote/Unauth: Code Execution + Priv. Escalation | **NEU** |
| [WID-SEC-2026-1401](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1401) | **Next.js** | 10. Jul | Remote | UPDATE |
| [WID-SEC-2026-2267](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2267) | **n8n** (Workflow Automation) | 10. Jul | k.A. | **NEU** |
| [WID-SEC-2026-2265](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2265) | **GitLab** | 10. Jul | k.A. | **NEU** |
| [WID-SEC-2026-2263](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2263) | **LiteLLM** (AI Proxy) | 10. Jul | k.A. | **NEU** |
| [WID-SEC-2026-2262](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2262) | **Progress MOVEit** | 10. Jul | k.A. | **NEU** |
| [WID-SEC-2026-2009](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2009) | **GCP/GKE containerd** | 10. Jul | Remote/Auth: Code Execution | **NEU** |
| [WID-SEC-2026-1187](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1187) | **Ruby/Rails** | 10. Jul | Remote | UPDATE |
| Linux Kernel (18+ Advisories) | **Linux Kernel** | 10. Jul | Priv. Escalation, DoS, Code Exec | UPDATES |

> **NGINX x4 (HOCH):** Vier parallel aktualisierte Advisories für NGINX/NGINX Plus. Falls NGINX als Reverse Proxy oder Web-Server im Stack: alle NGINX-Versionen prüfen und aktualisieren.
>
> **RabbitMQ WID-SEC-2026-2268 (NEU, HOCH):** Unauthentifizierter Remote-Angreifer kann Code ausführen und Privileges eskalieren. Message-Queue-Infrastruktur sofort patchen wenn RabbitMQ eingesetzt wird.
>
> **n8n WID-SEC-2026-2267 (NEU, HOCH) + LiteLLM WID-SEC-2026-2263 (NEU, HOCH):** Beides Tools die häufig in KI-gestützten Integrationsarchitekturen eingesetzt werden. Patchen wenn im Stack.
>
> **Progress MOVEit WID-SEC-2026-2262 (NEU, HOCH):** MOVEit war 2023 Ziel eines massiven Supply-Chain-Angriffs. Neues Advisory — falls MOVEit für Dateiübertragung oder in Sub-Processor-Ketten: sofort prüfen.
>
> **Linux-Kernel-Welle (18+ Updates, HOCH):** Dritte massive Kernel-Update-Welle in KW26–28. Kumulativer Patch-Rückstand erhöht Risiko erheblich. Unmanaged-Update-Policy auf automatische Security-Updates umstellen.

---

### MITTEL — Monitoring

| Advisory | Produkt | Datum |
|----------|---------|-------|
| [WID-SEC-2026-2231](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2231) | **Django** | 10. Jul |
| [WID-SEC-2026-0297](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0297) | **Django** | 10. Jul |
| [WID-SEC-2026-1038](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1038) | **Apache Tomcat** | 10. Jul |
| [WID-SEC-2026-0863](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0863) | **BIND** | 10. Jul |
| [WID-SEC-2026-1437](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1437) | **Golang** | 10. Jul |
| [WID-SEC-2026-2052](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2052) | **cURL** | 10. Jul |
| [WID-SEC-2026-2194](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2194) | **Erlang/OTP** | 10. Jul |

---

## Stille Bereiche

- **EUR-Lex** — RSS weiterhin 404 (13. Woche). AI-Omnibus OJ-Eintrag: noch nicht in EUR-Lex nachweisbar. Publikation erwartet vor 02.08.2026.
- **BfDI Pressemitteilungen** — RSS 404 (12. Woche).
- **BSI Pressemitteilungen** — RSS 404 (12. Woche). BSI-Content nur via Warnungs-Feed verfügbar.
- **e-Rechnung Bund (BMWK)** — RSS 404 (13. Woche). Keine neuen XRechnung-Regelungen KW28.
- **BMAS (Arbeitsrecht)** — RSS 404 (13. Woche). ArbZG-Reform weiterhin ohne Parlamentsbeschluss.
- **ENISA** — RSS 404 (10. Woche). Keine neuen NIS2-Leitlinien KW28.
- **EDPB Newsroom** — RSS 403 Forbidden (weiterhin). Inhalte via WebSearch: Anonymisation + Web Scraping + Blockchain Guidelines (7. Juli) via Websearch rekonstruiert.
- **EDPS** — 403 Forbidden. Keine neuen Meldungen KW28.
- **noyb** — RSS zugänglich, aber kein neuer Artikel seit 29. Juni 2026. DPF-Klage angekündigt, noch nicht eingereicht.

> **Wartungshinweis (Woche 13):** 6 von 10 Quellen 404 + 2 von 10 zusätzlich 403. Prio-Empfehlung — Woche 14: EDPB Direct-Scraping als Fallback für den 403-Feed testen. `#maintenance`

---

## Cosmi-Action-Items

### 🔴 Akut — diese Woche / bis 31. Juli

- [ ] **EDPB Anonymisation Guidelines 02/2026 lesen und Audit starten** — Neu verabschiedet 7. Juli 2026. 3-Kriterien-Test (Isolation / Linkage / Inference) auf alle Cosmi-Anonymisierungsroutinen anwenden: Reporting-Exports, Analytics-Datensätze, Dev/Staging-Datenbanken, KI-Trainings-Datasets. Simplified Approach als pragmatischer Einstieg. `#dsgvo #legal #product #data` → **bis 25. Juli**
- [ ] **AI Act Art. 50 Transparenz — 22 Tage — LIVE-CHECK** — Chatbot/Assistent-Offenlegung prüfen: Werden alle Nutzer (inkl. B2B-Kunden des CRM) klar informiert, dass sie mit einem KI-System interagieren? Alle Touchpoints: App-Widget, Support-Chat, E-Mail-Automation. Frist: **02.08.2026** — kein Aufschub. `#aiact #legal #product` → **bis 25. Juli**
- [ ] **NIS2 BSI-Registrierung — 20 Tage — letzte Chance** — Frist **31. Juli 2026**. ~11.000 Unternehmen noch offen. Bußgeld bis €500k + GF-Haftung. Falls Cosmi als IT-/Cloud-Dienstleister NIS2-pflichtig: Registrierung via [portal.bsi.bund.de](https://portal.bsi.bund.de) mit Puffer bis **25. Juli**. `#nis2 #legal #management` → **bis 25. Juli**
- [ ] **GNU libc patchen (KRITISCH, CVSS 9.8)** — WID-SEC-2026-1190. Betrifft alle Linux-Services. Distro-Patch einspielen (apt/yum). CVE-2026-5358, CVE-2026-5450, CVE-2026-5928. `#security #infra` → **sofort**
- [ ] **Python patchen (KRITISCH)** — WID-SEC-2022-0253. Falls Python für Backend-Services oder Scripts: sofort auf aktuelle Version aktualisieren. `#security #infra` → **sofort**
- [ ] **AI-Omnibus OJ täglich prüfen** — Sobald in EU-OJ publiziert (erwartet vor 02.08): Compliance-Roadmap auf Annex III = 02.12.2027 finalisieren. Bis dahin: alte Fristen gelten rechtlich. `#aiact #legal` → **täglich**

### 🟡 Followup (KW29+)

- [ ] **NGINX patchen (HOCH, 4 Advisories)** — WID-SEC-2026-0860/1995/1661/1527. Alle NGINX/NGINX-Plus-Instanzen updaten. `#security #infra`
- [ ] **RabbitMQ patchen (HOCH, NEU)** — WID-SEC-2026-2268. Remote/Unauth Code Execution + Priv. Escalation. Falls RabbitMQ im Stack: kritisch. `#security #infra`
- [ ] **EDPB Web Scraping Guidelines für GenAI prüfen** — Konsultation bis 30. Oktober 2026. Relevant für Lead-Enrichment-Features, KI-Trainings-Daten-Prozesse. `#dsgvo #legal #product`
- [ ] **DPF Audit fortsetzen** — Laufende Monitoring-Aufgabe: SCCs als Fallback für US-SaaS-Transfers dokumentieren. noyb-CJEU-Klage pending. `#dsgvo #legal #infra`
- [ ] **Linux-Kernel-Welle einspielen (HOCH, 18+ Updates)** — Automatische Security-Updates für Kernel evaluieren um kumulativen Rückstand zu vermeiden. `#security #infra`
- [ ] **LiteLLM + n8n + GitLab patchen (HOCH, NEU)** — WID-SEC-2026-2263/2267/2265. Falls im Stack. `#security #infra`
- [ ] **EDPB Anonymisation Guidelines Konsultation** — Bis 30. Oktober 2026. Eigene Implementierungsansätze dokumentieren, Kommentar einreichen falls sinnvoll. `#dsgvo #legal`
- [ ] **EDPB Data Breach Notification Template** — Konsultation läuft bis 05.08.2026. Template herunterladen, Incident-Response-SOP aktualisieren. `#dsgvo #security`
- [ ] **EUDIW Relying-Party-Vorbereitung** — Deutschland-Launch 02.01.2027 (174 Tage). Vertragsmodul-Planung Sprint 6+ datieren. `#eidas #product`
- [ ] **`sources/_regulation.yaml` Pflege** — Woche 13: 6×404 + 2×403. EDPB Direct-Scraping testen; BMAS-Alternativ-URL recherchieren. `#maintenance`
- [ ] **e-Rechnung GTM Q3** — YouGov-Studie (74 % unvorbereitet) weiterhin aktuell. Versandpflicht >€800k in ca. 6 Monaten. `#gtm #e-rechnung`
