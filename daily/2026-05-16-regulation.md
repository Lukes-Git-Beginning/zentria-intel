---
date: 2026-05-16
type: regulation
runtime_minutes: 14
items_scanned: 78
items_relevant: 11
sources_ok: 5
sources_failed: 5
kw: 20
---

# Regulation-Sweep KW20/2026 (Sa 16. Mai)

## DSGVO / Datenschutz

### Stille Regulations-Woche

EDPB, BfDI, noyb — keine neuen Einträge seit 09. Mai 2026.

- **EDPB**: Letzter Eintrag 05. Mai ("Europe Day 2026"). Feed erreichbar, keine neuen Inhalte.
- **BfDI**: RSS 404 (URL weiterhin defekt, bereits KW19 gemeldet).
- **noyb**: Letzter Eintrag 05. Mai (LinkedIn-Paywall-DSGVO-Beschwerde, bereits KW19 erfasst). Keine neuen Klagen oder Enforcement-Actions veröffentlicht.

> Die Wochen-Stille bei EDPB ist ungewöhnlich, könnte aber Vorbereitung auf größeres Enforcement-Paket (CEF 2026) sein — nächster regulärer Sweep Sa 23. Mai beobachten.

---

## AI Act

### Stille Regulations-Woche

EDPS — keine neuen Einträge seit 08. Mai 2026.

- **EDPS**: Letzter Eintrag 08. Mai ("Safe and Ethical AI", bereits KW19 erfasst). Feed erreichbar, keine neuen Inhalte diese Woche.
- AI-Act-Durchführungsverordnungen (Hochrisiko-Anhang, GPAI-Verhaltenskodex) weiterhin in Komitologie-Phase — keine OJ-Veröffentlichung via EUR-Lex verifiziert (Feed 404).

---

## NIS2

### ENISA — NIS2/Cybersecurity-Infrastruktur

- [New CVE Numbering Authorities Under ENISA Root](https://www.enisa.europa.eu/news/new-cve-numbering-authorities-under-enisa-root) *(06. Mai 2026, knapp vor Cutoff — erstmals erfasst)* — ENISA übernimmt gemäß NIS2-Mandat (Art. 10) die Rolle als EU-Root-CVE Numbering Authority (CNA). Neue EU-CVE-IDs werden ab sofort unter ENISA-Root vergeben. **Cosmi-Implikation:** ENISA-Vulnerability-Feeds (CERT-Bund/WID bereits genutzt) werden zur primären EU-Pflichtquelle für NIS2-konforme Schwachstellen-Dokumentation. Monitoring-Pipeline auf direkten ENISA-CVE-Feed erweitern. **Modul:** NIS2 / Security.

> Weiterer ENISA-Content: Feed-URL weiterhin 404 (bereits KW19 gemeldet). ENISA-Webseite direkt zugänglich — kein weiterer neuer Content 09.–16. Mai.

---

## XRechnung / e-Rechnung / GoBD

### Stille Regulations-Woche

*Quelle: e-rechnung-bund.de RSS weiterhin 404. BMWK-Feed nicht erreichbar.*

Keine verifizierten Neuigkeiten zu XRechnung, ZUGFeRD oder GoBD. Pflicht zur e-Rechnung B2B ab 01.01.2027 unverändert — Cosmi-Implementierungsfrist läuft.

---

## ArbZG / Arbeitsrecht

### Stille Regulations-Woche

*Quelle: BMAS-RSS weiterhin 404.*

Keine verifizierten Neuigkeiten zu ArbZG, Mindestlohn oder Ruhezeit.

---

## eIDAS

*Keine dedizierte eIDAS-Quelle aktiv. Keine einschlägigen Treffer in EDPS/EDPB-Feeds.*

→ Stille Regulations-Woche für eIDAS.

---

## BSI-Warnings (CVE-Filter: postgres, crm, saas, cloud, node, nginx, docker)

Zeitraum: 09.–16. Mai 2026 (Patchday-Woche Microsoft + Linux-Kernel-Batch)

### CRITICAL

- **Node.js** — [WID-SEC-2026-0098](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0098) *(15. Mai)* — Mehrere Schwachstellen ermöglichen Code-Ausführung, Privilege Escalation und Security-Bypass. **Cosmi-Implikation:** Falls Node.js im Backend oder Build-Pipeline eingesetzt wird, sofort patchen. Betrifft auch vm2-Sandbox (nächster Eintrag). **Modul:** Security / DevOps.

- **vm2 (Node.js-Sandbox)** — [WID-SEC-2026-1349](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1349) *(15. Mai)* — Beliebige Code-Ausführung, DoS und Information-Disclosure möglich. Betrifft alle Umgebungen, die vm2 für Scripting oder Plugin-Isolation nutzen. **Modul:** Security / DevOps.

- **Microsoft Windows (Patchday Mai 2026)** — [WID-SEC-2026-1489](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1489) *(15. Mai)* — Kritische Sammlung: Code-Ausführung, Privilege Escalation, DoS, Bypass. Betrifft Windows-Server-Instanzen im Cosmi-Infra-Stack.

- **Cisco Catalyst SD-WAN Controller** — [WID-SEC-2026-1534](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1534) *(15. Mai)* — Remote-Angreifer können Admin-Rechte auf SD-WAN-Netzwerkkonfiguration erlangen. Relevant wenn Cosmi-Netzwerk SD-WAN-basiert.

### HIGH

- **PostgreSQL** — [WID-SEC-2026-1544](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1544) *(15. Mai)* — **Höchste Cosmi-Priorität.** SQL-Injection, beliebige Code-Ausführung, DoS und Information-Disclosure. Betrifft PostgreSQL direkt — Cosmi-Primär-Datenbank. Patch sofort einspielen und DB-Logs auf Anomalien prüfen. **Modul:** Security / DB / DevOps.

- **NGINX Open Source + NGINX Plus** — [WID-SEC-2026-1527](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1527) *(15. Mai)* — Remote-Angreifer können Protection-Maßnahmen umgehen, Code ausführen und DoS auslösen. Betrifft Cosmi-Reverse-Proxy / API-Gateway falls NGINX-basiert. **Modul:** Security / Infra.

- **Docker** — [WID-SEC-2026-0873](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-0873) *(15. Mai)* — Lokale Angreifer können Sicherheitsmaßnahmen umgehen und auf sensitive Informationen zugreifen. Betrifft Cosmi-Container-Runtime. **Modul:** Security / DevOps.

- **Linux Kernel** (3 Advisories) — [WID-SEC-2026-1555](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1555) / [WID-SEC-2026-1531](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1531) / [WID-SEC-2026-1530](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1530) *(15. Mai)* — DoS, Privilege Escalation, unspezifizierte Auswirkungen. Alle Cosmi-Linux-Hosts aktualisieren. **Modul:** Security / Infra.

- **MongoDB** — [WID-SEC-2026-1516](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1516) *(13. Mai)* — Remote-authentifizierte Angreifer können Code ausführen, Daten manipulieren und DoS auslösen. Betrifft Logging/Session-Stores falls MongoDB im Stack.

- **Apache Tomcat** — [WID-SEC-2026-1514](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1514) *(13. Mai)* — Security-Bypass, Information-Disclosure, Datenmanipulation, DoS. Relevant falls Java/Tomcat im Cosmi-Backend.

- **Nextcloud** — [WID-SEC-2026-1517](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1517) *(13. Mai)* — Security-Bypass, Information-Leakage, SQL-Injection. Relevant falls Cosmi intern Nextcloud nutzt (Dokumente, Wiki-Alternative). **Modul:** Security / Intern.

---

## Stille Bereiche

- **EUR-Lex** — Feed 404. COM/OJ-Neuigkeiten (AI Act Durchführungsverordnungen, Digital Omnibus) nicht verifiziert.
- **BfDI Pressemitteilungen** — RSS 404 (4. Woche in Folge; URL-Pflege erforderlich).
- **BSI Pressemitteilungen** — RSS 404 (4. Woche in Folge).
- **e-Rechnung Bund (BMWK)** — RSS 404 (4. Woche in Folge; e-Rechnungspflicht B2B 2027 nähert sich).
- **BMAS (Arbeitsrecht)** — RSS 404 (4. Woche in Folge).

> **Wartungshinweis:** 5 von 10 Quellen dauerhaft 404. Dringend alternative Feed-URLs recherchieren oder durch Web-Scraping-Fallback ersetzen. Empfehlung: `sources/_regulation.yaml` bis KW21 aktualisieren.

---

## Cosmi-Action-Items

### Akut (diese Woche)

- [ ] **PostgreSQL-Patch einspielen** (WID-SEC-2026-1544, HIGH): SQL-Injection + Code-Execution in Cosmi-Primär-DB. Patch-Stand prüfen, DB-Audit-Log aktivieren falls nicht aktiv. `#security #db #devops` → sofort
- [ ] **Node.js + vm2 patchen** (WID-SEC-2026-0098 + WID-SEC-2026-1349, CRITICAL): Code-Execution-Lücken. Node-Version im Cosmi-Backend und Build-Pipeline aktualisieren. `#security #devops` → sofort
- [ ] **NGINX patchen** (WID-SEC-2026-1527, HIGH): Reverse-Proxy/API-Gateway auf aktuelle NGINX-Version heben. `#security #infra` → diese Woche
- [ ] **Docker + Linux Kernel Updates** (HIGH): Alle Cosmi-Container-Hosts mit aktuellen Kernel- und Docker-Patches versorgen. `#security #infra` → diese Woche

### Followup (Sprint 4 / Q2 2026)

- [ ] **ENISA CVE-Root: Monitoring-Pipeline erweitern** — ENISA ist ab sofort EU-Root-CNA (NIS2 Art. 10). Direkten ENISA-CVE-Feed in `sources/_regulation.yaml` ergänzen und in wöchentlichen BSI-CVE-Sweep integrieren. `#nis2 #security`
- [ ] **`sources/_regulation.yaml` Pflege** — 5 Quellen dauerhaft 404 (BfDI, BSI-Presse, EUR-Lex, BMWK, BMAS). Alternative URLs für alle 5 recherchieren. Insb. BMWK/e-Rechnung dringend — B2B-Pflicht 2027. `#maintenance`
- [ ] **AI-Act-Hochrisiko-Klassifikation** (carry-over KW19) — Lead-Scoring, KI-Chatbot, Prognose-Features nach Anhang III AI Act evaluieren. EDPS Compass als Grundlage. `#aiact` → Sprint 4
- [ ] **DSR-Workflow-Audit** (carry-over KW19) — Art.-15-Auskunftsersuchen: 30-Tage-Frist und Vollständigkeit in Cosmi-CRM-Workflows validieren. `#dsgvo #crm`
