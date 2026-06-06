---
date: 2026-06-06
type: regulation
runtime_minutes: 16
items_scanned: 81
items_relevant: 12
sources_live_rss: 3
sources_404: 6
kw: 23
---

# Regulation-Sweep KW23/2026 (Sa 06. Juni)

> **KW23-Scope:** 01.–06. Juni 2026. Referenz-Sweep: KW22 (30. Mai). Neue Items: 7. Carry-over-Items: 5.
>
> **⚠️ Vorschau KW23-Folgewoche:** EDPB 120. Plenum + EDPS/BfDI/BayLfD Omnibus-Debatte — beide **08.–09. Juni** (Montag/Dienstag). Ergebnisse im nächsten Morning-Intel verfolgen.

---

## DSGVO / Datenschutz

### noyb — Schibsted „Pay or Okay"-Beschwerde *(neu — 03. Juni 2026)*

- [Nordic Media Giant Schibsted switches to "Pay or Okay" — complaint filed!](https://noyb.eu/en/nordic-media-giant-schibsted-switches-pay-or-okay-complaint-filed) *(03. Juni 2026, noyb + Forbrukerrådet)* — noyb und der norwegische Verbraucherschutzrat Forbrukerrådet haben gemeinsam Beschwerde gegen **Schibsted** (Betreiber von Aftenposten, VG, Dagbladet u. a.) eingereicht. Schibsted hat sein bisheriges Consent-Modell auf ein reines „Pay or Okay"-System umgestellt — Nutzer müssen zahlen oder Tracking akzeptieren, eine echte Ablehnoption entfällt. noyb-Argument: Die Einwilligung ist nicht freiwillig erteilt (Art. 7 DSGVO). **Cosmi-Implikation:** „Pay or Okay" bleibt noyb-Kernkampffeld. Jedes Cookie-Banner, das Reject nicht gleichwertig zu Accept anbietet (Größe, Farbe, Positionierung), ist Beschwerderisiko. Cosmi-Frontend-Audit: Accept- und Reject-Button müssen visuell equivalent sein. Urteil-Wirkung auf DE/AT/CH-Medienseiten ist Präzedenzfall für alle B2C-SaaS. **Modul:** DSGVO / Frontend / Legal. `#neu`

### GDPR Enforcement — Dutch AP: Yango €100 Mio. *(Mai 2026, erstmals KW23)*

- [Enforcement Tracker — Yango (AP Netherlands)](https://www.enforcementtracker.com/) *(Mai 2026)* — Die niederländische Datenschutzbehörde AP hat gegen **Yango** (europäischer Betreiber der gleichnamigen Taxi-App, Tochter von Yandex) eine DSGVO-Geldbuße von **€100 Mio.** verhängt — eines der höchsten Bußgelder gegen ein Nicht-US-Unternehmen. Verstoß: unzulässige Datenweitergabe an Russland (nationaler Sicherheitszweck), fehlende Rechtsgrundlage für internationale Transfers. **GDPR-Enforcement-Gesamtbild 2026 (YTD):** 143 Verfahren, Gesamtbußgelder €6,29 Mrd. kumuliert. **Cosmi-Implikation:** Internationaler Datentransfer bleibt der heißeste Enforcement-Bereich. Cosmi-Datenflüsse auf EU-Verbleib prüfen; Sub-Processor-Liste (AVV-Anhang) auf Drittstaaten-Empfänger scannen. WS: Yandex/russische Infrastruktur unter Sub-Processors? Falls ja: sofort eskalieren. **Modul:** DSGVO / Legal / Security. `#neu`

### EDPB 120. Plenum — 08.–09. Juni 2026 *(Carry-over — Ergebnisse noch ausstehend)*

Nächste Woche trifft das EDPB 120. Plenum (08.–09. Juni). Erwartete Tagesordnungspunkte basierend auf laufenden Arbeitsprogrammen:
- Ggf. Fortschrittsupdate Anonymisierungs-Guidelines (Sprint-Team)
- Mögliche Stellungnahme zu DSGVO-Auswirkungen des AI Omnibus
- Koordiniertes Enforcement 2026 (CEF Art. 12–14) — Status-Update

**Cosmi-Implikation:** Privacy Notice und DSR-Workflow müssen **vor Montag 08. Juni** auditiert sein (CEF-Enforcement-Welle läuft). 30-Tage-Frist für Art.-15-Auskunftsbegehren sicherstellen. **Modul:** DSGVO / Legal. `#frist-08-juni`

### EDPB CEF 2026 — Transparenz-Enforcement aktiv *(Carry-over KW21 — laufend)*

25 DPAs kontaktieren aktiv Unternehmen zu Art. 12, 13, 14 DSGVO (Datenschutzhinweispflichten). H1/2026 = Enforcement-Phase. **Cosmi-Implikation:** Privacy-Notice-Audit dringend; Rechtsgrundlagen, Zwecke, Empfänger, Speicherfristen vollständig und klar. Consent-Dokumentation validieren.

---

## AI Act

### ⚠️ FRIST IN 17 TAGEN: AI-Act Hochrisiko-Klassifikation — 23. Juni 2026

Die EU-Kommissions-Konsultation [Draft Guidelines for High-Risk AI Classification](https://digital-strategy.ec.europa.eu/en/consultations/targeted-consultation-draft-guidelines-classification-high-risk-artificial-intelligence-systems) *(Art. 6 AI Act, publiziert 19. Mai 2026)* läuft bis **23. Juni 2026, 22:00 CET** — noch **17 Tage**.

Dokument: 167 Seiten mit Schlüsselkonzepten und Praxisbeispielen (Hochrisiko vs. Nicht-Hochrisiko). Nicht rechtsverbindlich, aber maßgeblich für Compliance-Planung. Tatsächliche verbindliche Fristen:
- **Hochrisiko nach Anhang III (stand-alone):** 02. Dezember 2027
- **Hochrisiko nach Anhang I (in Produkte eingebettet):** 02. August 2028

**Cosmi-Implikation:** Lead-Scoring-Modul, KI-Chatbot, Prognose-Features einzeln gegen Anhang-III-Kriterien prüfen (Beschäftigung/HR, Kundenzugang, Sicherheitskomponenten). Guidelines lesen und intern bewerten. Selbst wenn kein Hochrisiko → Ergebnis **dokumentieren** (Nachweis bei DPA-Anfrage). Optional: Feedback einreichen (Positionierung als EU-KI-konformes CRM). **Modul:** AI Act / Legal / Product. `#frist-23-juni #akut`

### AI Omnibus — Formale Adoption bevorstehend *(Carry-over — Junispurt)*

Provisorische Einigung 07. Mai + Ratsdokument 9247/26 (13. Mai) liegen vor. Formale EP- und Ratsabstimmung erwartet **Juni–Juli 2026** (vor 02. August — sonst greifen alte Fristen). Noch kein OJ-Eintrag. Kernänderungen: Hochrisiko-Frist Dez. 2027, neue Verbote NCII/CSAM ab Dez. 2026. **Cosmi-Implikation:** EUR-Lex täglich nach OJ-Publikation überwachen. Compliance-Planung mit Zieldatum 02.12.2027 läuft. **Modul:** AI Act / Legal. `#beobachten`

---

## NIS2

### BSI NIS-2 Portal Schritt 2 — seit 01. Juni aktiv *(Carry-over — Handlungsbedarf)*

Schritt 2 der NIS-2-Vollregistrierung ist seit 01. Juni 2026 freigeschaltet. Pflichtangaben: Adresse, Kontaktdaten CISO/ISB, öffentlich erreichbare statische IP-Ranges. Portal bietet Art.-21-Risikomanagement-Guidance, Bedrohungslageberichte und anonyme Schwachstellenmeldung.

**Keine neuen NIS2-Meldungen in KW23** (BSI-Pressemitteilungen weiterhin 404; ENISA-Feed weiterhin 404).

**Cosmi-Implikation:** Falls Cosmi als IT-Dienstleister/SaaS für regulierte Sektoren NIS-2-pflichtig ist → Schritt-2-Registrierung sofort nachholen (Frist unklar, aber offen seit 01.06.). **Modul:** NIS2 / Legal / Security.

---

## XRechnung / e-Rechnung / GoBD

### Handelsverband Südwest — „Jetzt aktiv werden" *(neu — 03. Juni 2026)*

- [E-Rechnungspflicht ab 2027: Handelsunternehmen müssen jetzt aktiv werden](https://hv-suew.de/2026/06/03/e-rechnungspflicht-ab-2027-handelsunternehmen-muessen-jetzt-aktiv-werden/) *(03. Juni 2026)* — Handelsverband Südwest schlägt Alarm: YouGov-Umfrage zeigt, ein **Drittel der deutschen Unternehmen hat noch nie eine E-Rechnung verschickt**; 11 % nutzen Excel, 10 % Word für Rechnungserstellung — beide nicht EN-16931-konform. Bis 01.01.2027 (Umsatz >800.000 €) bzw. 01.01.2028 (alle B2B) ist XRechnung oder ZUGFeRD Pflicht. **Cosmi-Implikation:** Dieser Marktstand ist ein Cosmi-Verkaufsargument. 74 % der mittelständischen Cosmi-Zielkunden sind potenziell nicht bereit — Buchhaltungsmodul mit XRechnung/ZUGFeRD 2.4 als Alleinstellungsmerkmal kommunizieren. Kundenonboarding-Kampagne Q3 2026 planen. **Modul:** Buchhaltung / e-Rechnung / GTM. `#neu`

*e-Rechnung-bund.de RSS weiterhin 404 (7. Woche in Folge).*

Fristen-Erinnerung (unverändert):

| Datum | Pflicht |
|-------|---------|
| seit 01.01.2025 | **Empfang** strukturierter e-Rechnungen (alle B2B) |
| bis 31.12.2026 | Übergangsfrist Versand — Papier/PDF noch erlaubt |
| ab 01.01.2027 | **Versandpflicht** Umsatz >800.000 € |
| ab 01.01.2028 | **Versandpflicht** alle B2B |

---

## ArbZG / Arbeitsrecht

### Stille Woche

*BMAS-RSS weiterhin 404 (8. Woche in Folge). Kein WebSearch-Treffer für akute ArbZG-Neuigkeiten in KW23.*

---

## eIDAS

### EUDI Wallet — Fristdruck steigt, Mitgliedsstaaten im Rückstand *(neu — KW23)*

- [EUDI Wallet Deadline: Late 2026 Mandatory Rollout](https://www.deepidv.com/media/news/eudi-wallet-deadline-late-2026) — Frist: Mitgliedsstaaten müssen bis **September 2026** EUDI Wallets für Bürger bereitstellen. Realitätscheck KW23: **Niederlande** hat öffentlich signalisiert, die Frist nicht einhalten zu können. **Malta**: Wallet verfügbar, aber nicht voll funktionsfähig. **Bulgarien**: noch keine Entwicklungsarbeit begonnen. Europäische Kommission hat 7 neue Durchführungsverordnungen zu Trust Services verabschiedet; ARF-Spezifikationen werden noch überarbeitet.

**Cosmi-Implikation:** Septembe-Frist für viele Staaten faktisch unrealistisch → realistische Adoption eher **Q1/Q2 2027**. Cosmi-Roadmap für eSignatur/eIDAS-Integration (Vertragsmodul) auf **Sprint 6+** verschieben ist vertretbar; Markt wird erst 2027 reif. Tracking-Pflicht bleibt. **Modul:** eIDAS / Verträge / Auth.

---

## BSI-Warnings (CVE-Filter: postgres, crm, saas, cloud, nginx, docker, linux)

Zeitraum: **30. Mai – 05. Juni 2026**

### Neue / aktualisierte Advisories KW23

| Advisory | Produkt | Severity | Datum | Angriffsszenario |
|----------|---------|----------|-------|-----------------|
| [WID-SEC-2026-1544](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1544) | **PostgreSQL** | **HOCH** | 05. Jun (Update) | Remote: SQL-Injection, arbitrary code execution, DoS, Dateimanipulation, Security-Bypass — Update erneut geändert! |
| [WID-SEC-2026-1661](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1661) | **NGINX Open Source & Plus** | **HOCH** | 05. Jun | Remote: DoS, potenzielle Code Execution |
| [WID-SEC-2026-1527](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1527) | **NGINX Open Source & Plus** | **HOCH** | 05. Jun | Remote: Security-Bypass, Code Execution, Datenmanipulation, Info-Disclosure, DoS |
| [WID-SEC-2026-0860](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0860) | **NGINX & NGINX Plus** | **HOCH** | 05. Jun (Update) | Remote: DoS, Datenmanipulation, Security-Bypass, potenzielle Code Execution |
| [WID-SEC-2026-1584](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1584) | **Docker** | MITTEL | 05. Jun | Lokal: Code Execution mit Admin-Rechten, DoS, Datenmanipulation |

*Zusätzlich: mehrere Linux-Kernel-Advisories (HIGH/MITTEL) am 05. Juni — DoS, Privilege Escalation, Code Execution.*

> **⚠️ PostgreSQL-Advisory WID-SEC-2026-1544** wurde **erneut** am 05. Juni aktualisiert (3. Update seit KW20). Falls Patches noch nicht applied: **Prio 1 heute.**
>
> **NGINX**: 3 separate Advisories am gleichen Tag (05. Juni) — koordinierter Release-Batch. Alle NGINX-Instanzen (API-Gateway, Reverse Proxy) sofort aktualisieren.

**Cosmi-Implikation:** PostgreSQL-Patches sofort verifiziern. NGINX-Updates auf allen Servern ausrollen. Docker-Update einplanen. **Modul:** Security / Infra / DevOps. `#akut`

---

## Stille Bereiche

- **EUR-Lex** — RSS-Feed weiterhin 404 (7. Woche). AI-Omnibus-Status per WebSearch erfasst.
- **BfDI Pressemitteilungen** — RSS 404 (7. Woche). Kein neuer BfDI-Content via WebSearch.
- **BSI Pressemitteilungen** — RSS 404 (7. Woche). BSI-Content via WebSearch (NIS2-Schritt-2 bekannt aus KW22).
- **e-Rechnung Bund (BMWK)** — RSS 404 (7. Woche). e-Rechnung-News via WebSearch (Handelsverband Südwest).
- **BMAS (Arbeitsrecht)** — RSS 404 (8. Woche). Kein ArbZG-Content in KW23.
- **ENISA** — RSS 404 (seit KW19). Kein neuer ENISA-Content in KW23.
- **EDPB** — Feed erreichbar, aber keine neuen Artikel seit 22. Mai (Plenum 08.–09. Juni noch nicht stattgefunden).
- **EDPS** — Feed erreichbar, letzter Artikel 22. Mai.

> **Wartungshinweis (Woche 7):** 6 von 9 Quellen dauerhaft 404. `sources/_regulation.yaml` Pflege überfällig. Priorität: BMAS (ArbZG — 8. Woche!), BMWK/e-Rechnung, ENISA. Neue Feed-URLs recherchieren oder WebSearch-Fallback als primäre Quelle eintragen.

---

## Cosmi-Action-Items

### Akut (vor 08./09. Juni — EDPB-Plenum + Omnibus-Debatte)

- [ ] **Privacy Notice und DSR-Workflow auditieren** — EDPB-CEF-2026-Enforcement (Art. 12–14 DSGVO) läuft aktiv. Art.-15-Frist (30 Tage), Rechtsgrundlagen, Empfänger, Speicherfristen vollständig? Vor EDPB-Plenum 08.06. abschließen. `#dsgvo #legal` → **bis 08.06.**
- [ ] **PostgreSQL patchen** (WID-SEC-2026-1544 — erneutes Update 05. Jun, HIGH): Cosmi DB-Server sofort. SQL-Injection + Code Execution + Security-Bypass. `#security #infra` → **sofort**
- [ ] **NGINX patchen** (WID-SEC-2026-1661, -1527, -0860 — alle HIGH, 05. Jun): API-Gateway, Reverse Proxy, alle NGINX-Instanzen sofort updaten. `#security #infra` → **sofort**
- [ ] **Docker updaten** (WID-SEC-2026-1584 — MITTEL, 05. Jun): Lokale Code-Execution mit Admin-Rechten einplanen. `#security #devops` → **diese Woche**
- [ ] **AI-Act Hochrisiko-Assessment starten** — Frist **23. Juni (17 Tage!)**. 167-seitige Draft Guidelines lesen; Lead-Scoring, KI-Chatbot, Prognose-Features gegen Anhang-III-Kriterien bewerten; Ergebnis dokumentieren. `#aiact #legal #product` → **diese Woche starten**

### Followup (KW24+)

- [ ] **EDPB 120. Plenum Ergebnisse auswerten** (08.–09. Juni): Morning-Intel Mo/Di verfolgen. Anonymisierungsguidelines-Stand? Omnibus-Stellungnahme? `#dsgvo`
- [ ] **EDPS/BfDI/BayLfD Omnibus-Debatte 08. Juni** verfolgen. `#dsgvo #aiact`
- [ ] **AI Omnibus formale Adoption** — EUR-Lex auf OJ-Publikation überwachen. `#aiact`
- [ ] **Cookie-Banner-Audit** (noyb Schibsted-Beschwerde als Anlass): Reject-Button gleichwertig zu Accept? `#dsgvo #frontend`
- [ ] **Sub-Processor-Audit** (Yango-Bußgeld €100M als Anlass): AVV-Anhang auf Drittstaaten-Empfänger (inkl. russische Infrastruktur) prüfen. `#dsgvo #legal`
- [ ] **e-Rechnungs-GTM-Kampagne Q3 2026 planen** — 1/3 der DE-Unternehmen nie e-Rechnung versendet, Cosmi als Lösung positionieren. `#e-rechnung #gtm`
- [ ] **eIDAS-Integration auf Sprint 6+ verschieben** — EUDI-Wallet realistische Adoption Q1/Q2 2027 (NL/MT/BG im Rückstand). `#eidas #product`
- [ ] **`sources/_regulation.yaml` Pflege** — 6 von 9 Quellen 404. Alternative URLs KW24 recherchieren. `#maintenance`
- [ ] **BfDI Tätigkeitsbericht 2025 lesen** (Carry-over KW22) — AVV-Kette + MFA-Rollout validieren. `#dsgvo`
- [ ] **NIS2 BSI-Portal Schritt-2-Registrierung prüfen** (ab 01.06. offen) — falls Cosmi NIS-2-pflichtig. `#nis2`
