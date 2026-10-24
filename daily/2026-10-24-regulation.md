---
date: 2026-10-24
type: regulation
runtime_minutes: 14
items_scanned: 35
items_relevant: 6
kw: 43
sources_ok: [edpb-newsroom, bsi-warnungen, noyb, digital-strategy-ec, enisa]
sources_failed: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, oedp-eaid]
---

# Regulation-Sweep KW43/2026 (Sa 25. Oktober)

---

## DSGVO / Datenschutz — Kritisch

### BREAKING: EU-Rat billigt DSGVO-Aufweichung für KI — Article 88bis — Digital Omnibus

- [AI: EU Member States Approve "Digital Expropriation" for AI Companies](https://noyb.eu/en/ai-eu-member-states-approve-digital-expropriation-europeans-ai-companies) *(23.10.2026 — noyb)*
  — **Kritischer Entwicklungsstand.** Der EU-Rat hat am 23.10.2026 den Text des Digital Omnibus verabschiedet, der Artikel 88bis in die DSGVO einfügt. Der neue Artikel ermöglicht es Unternehmen, personenbezogene Daten „im Kontext von KI" ohne konkreten Zweck, ohne valide Rechtsgrundlage nach Art. 6 und ohne Einwilligung zu verarbeiten — solange eine „KI-Komponente" vorliegt. Konkret: Google, Meta, Microsoft dürfen historisch gesammelte Daten (über Jahrzehnte) für KI-Training nutzen. Max Schrems: „Digital Expropriation of Europeans." Kernproblem: (1) Art. 88bis legitimiert eine Technologie, nicht einen Zweck — Paradigmenbruch in der DSGVO-Dogmatik. (2) Definition „personenbezogene Daten" wird verengt — Online-Tracking-IDs könnten herausfallen. (3) Compliance-Entscheidungen werden auf Unternehmen übertragen, nicht auf Aufsichtsbehörden. Nächste Stufe: Trilog mit Europäischem Parlament (EP hat bislang strengere Position). Deutschland war unter den Befürwortern im Rat.
  — **Cosmi-Implikation:** Zweischneidig. Kurzfristig: Falls Art. 88bis gilt, entfällt für Cosmi-Kunden mit KI-Funktionen (Predict, Auto-Kategorisierung, NLP-Pipelines) ein Teil des Einwilligungsdrucks. Mittelfristig: **Cosmi-USP-Risiko.** Cosmi positioniert sich als „DSGVO-by-design"-Alternative zu US-Hyperscalern. Wenn DSGVO auf US-Standard abgesenkt wird, schrumpft der Compliance-Differenzierungsvorteil erheblich. Strategisch: Cosmi sollte diesen Trilog-Prozess beobachten. Falls EP den Art. 88bis kippt → USP stärker. Falls EP zustimmt → Neupositionierung erforderlich. Auch relevant: Schrems III-Risiko steigt, da US-Adequacy-Decision durch Trump v. Slaughter (FTC-Unabhängigkeit weggefallen) ohnehin unter Druck steht. **Modul: DSGVO, Legal, Product-Strategy, CRM-Core**

---

### Deutsche DPA: Politisches Microtargeting der Bundestagsparteien illegal — Art. 9 DSGVO

- [German DPA Finds Microtargeting by Major Political Parties Illegal](https://noyb.eu/en/noyb-win-german-dpa-finds-microtargeting-major-political-parties-illegal) *(21.10.2026 — noyb)*
  — Berliner Datenschutzbehörde hat festgestellt, dass politisches Microtargeting von SPD, Grünen, Linke und CDU bei der Bundestagswahl 2021 gegen DSGVO verstößt. Rechtsgrundlage: Verarbeitung politischer Überzeugungen = Art. 9-Daten (besondere Kategorie). Selbst wenn Nutzer „allgemein öffentlich zugängliche" Daten gepostet haben, berechtigt das nicht zur Profilierung für politisches Targeting. AfD-Fall noch offen.
  — **Cosmi-Implikation:** Direkte Relevanz für Cosmi CRM-Core. Wenn Cosmi-Kunden (insb. Agenturen, HR-Dienstleister, Verbände) Lead-Scoring oder Segmentierung auf Basis von Informationen betreiben, die politische Neigungen, Gewerkschaftszugehörigkeit oder religiöse Überzeugungen implizieren → Art. 9-Verstoß, auch wenn diese Daten nicht explizit als solche erhoben wurden. Prüfpunkt: CRM-Tagging-Freifelder, Custom-Fields — können dort indirekt Art.-9-Kategorien landen? Empfehlung: UI-Hinweis / Validierungsschicht in Custom-Field-Erstellung. **Modul: CRM-Core, DSGVO, Legal**

---

## AI Act

### EU-Kommission: KI-Adoption verdoppelt sich in fast allen EU-Sektoren — Hochrisikoklassifikation rückt näher

- [AI adoption more than doubles in almost every EU strategic sector](https://digital-strategy.ec.europa.eu/en/news/ai-adoption-more-doubles-almost-every-eu-strategic-sector) *(14.10.2026 — EU Digital Strategy)*
  — Kommissionsbericht: KI-Adoption stieg EU-weit auf ~18% über strategische Sektoren — Verdoppelung seit 2024. Gleichzeitig trat der AI Act Hochrisikoregulierungs-Teil (Annex III) für bestimmte Sektoren verschärft in Kraft. Relevant: KI in Personalentscheidungen, Kreditscoring, Kundenkommunikation.
  — **Cosmi-Implikation:** Wenn Cosmi KI-gestützte Funktionen (automatisches Lead-Scoring, Auto-Prioritisierung von Helpdesk-Tickets, Dienstplan-Optimierung via Schichten-Modul) als „Hochrisiko" nach AI Act Annex III (Beschäftigung, Kreditwesen) einzustufen ist, gelten verschärfte Transparenz-, Logging- und Konformitätspflichten. Prüfpunkt: Interne KI-Act-Hochrisiko-Klassifikation noch ausstehend (Sprint 4). **Modul: AI Act, CRM-Core, Schichten, Legal**

---

## NIS2 / Cybersicherheit

### ENISA: Threat Landscape 2026 — Supply-Chain-Abhängigkeiten als Hauptangriffsfläche

- [ENISA Threat Landscape 2026: How dependencies weaken our digital resilience](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience) *(22.09.2026 — ENISA)*
  — ENISA Threat Landscape 2026: Cyber-Abhängigkeiten (Supply Chain, Open-Source-Libraries, SaaS-Ketten) sind die primär wachsende Angriffsfläche. „Cyber dependencies expand the attack surface and require a new level of vigilance." Für SaaS-Anbieter unter NIS2 direkt relevant.
  — **Cosmi-Implikation:** Als Self-Hosted-SaaS-Anbieter trägt Cosmi Verantwortung für Third-Party-Dependencies im Go- und TypeScript-Stack. NIS2 Art. 21 verlangt Lieferkettenrisikomanagement. Empfehlung: Dependency-Audit (besonders Go-Module, npm-Packages) mit SBOM (Software Bill of Materials) dokumentieren. **Modul: NIS2, Security, Infra**

---

## BSI-Warnungen (CVE-Filter: postgres, crm, saas)

### BSI CERT-Bund: PostgreSQL — Mehrere kritische Schwachstellen (WID-SEC-2026-1544)

- [WID-SEC-2026-1544: PostgreSQL — Mehrere Schwachstellen](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1544) *(22.10.2026 — BSI CERT-Bund, Severity: HIGH)*
  — Mehrere Schwachstellen in PostgreSQL ermöglichen: (1) Ausführung beliebigen Programmcodes, (2) Denial-of-Service. Keine CVE-Nummern im Feed. Direkt betroffen: alle PostgreSQL-Versionen, die nicht auf den aktuellen Patch-Stand gebracht wurden.
  — **Cosmi-Implikation:** **Kritisch.** Cosmi nutzt PostgreSQL als primäre Datenbank für alle 15 Module. Sofortige Maßnahme: PostgreSQL-Version auf Self-Hosted-Instanzen prüfen und Patch einspielen. Für Cosmi-Kunden, die Cosmi Cloud nutzen: zentral prüfen und fixen. Empfehlung: In nächstem Sprint Patch-Protokoll für kritische Infra-Dependencies standardisieren. **Modul: Infra, Security, alle Module**

### BSI CERT-Bund: Atlassian Bamboo/Bitbucket/Confluence/Jira — Kritische Schwachstellen (WID-SEC-2026-4056)

- [WID-SEC-2026-4056: Atlassian Products — Multiple Vulnerabilities](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4056) *(23.10.2026 — BSI CERT-Bund, Severity: HIGH)*
  — Code-Execution, Privilege-Escalation, DoS und Daten-Manipulation in Bamboo, Bitbucket, Confluence und Jira. Relevant für Teams, die Atlassian-Stack im Zentria/Cosmi-Entwicklungsprozess nutzen.
  — **Cosmi-Implikation:** Falls Cosmi/Zentria Confluence oder Jira intern einsetzt → Sofort-Patch. Auch für Cosmi-Kunden relevant, die Atlassian-Tools parallel zu Cosmi betreiben und Integration-Punkte haben. **Modul: Security, Infra, DevOps**

---

## XRechnung / e-Rechnung / GoBD

### Stille Woche — Keine neuen Meldungen

- `e-rechnung-bmwk`-Feed weiterhin nicht erreichbar (HTTP 404). Keine neuen XRechnung- oder GoBD-Updates über alternative Quellen erfasst. Letzte relevante Aktivität: XRechnung 3.0 Inkraftsetzung KW36/2026.

---

## ArbZG / Arbeitsrecht

### Stille Woche — Keine neuen Meldungen

- `eaid-arbeitsrecht`-Feed (BMAS) weiterhin HTTP 404. Keine neuen ArbZG- oder Mindestlohnmeldungen über alternative Quellen.

---

## eIDAS

### Stille Woche — Keine neuen Meldungen

- Kein neues Material aus EDPS, EUR-Lex oder Digital-Strategy zu eIDAS 2.0 EUDI Wallet in dieser Woche.

---

## Stille Bereiche

| Quelle | Status | Letzter OK-Stand |
|--------|--------|-----------------|
| EUR-Lex RSS | Feed leer (kein Content) | KW40 |
| BfDI Pressemitteilungen | HTTP 404 | KW41 |
| BSI Pressemitteilungen | HTTP 404 | KW41 |
| e-rechnung-bund.de | HTTP 404 | KW36 |
| BMAS RSS | HTTP 404 | KW39 |
| EDPS (oedp-eaid) | HTTP 403 | KW38 |

**Strukturproblem:** Mehrere deutsche Behörden-Feeds dauerhaft nicht erreichbar. Empfehlung: Feed-URLs in `sources/_regulation.yaml` überarbeiten oder Web-Scraping auf HTML-Seiten umstellen (BfDI, BMAS, BSI Presse).

---

## Cosmi-Action-Items

- [ ] **KRITISCH: PostgreSQL-Patch einspielen** — BSI WID-SEC-2026-1544, alle Cosmi-Datenbankinstanzen (Cloud + Self-Hosted-Kunden informieren). Sprint-sofort. `Modul: Infra`
- [ ] **Atlassian-Stack patchen** — WID-SEC-2026-4056 (Confluence/Jira/Bitbucket/Bamboo). Falls intern genutzt: sofort. `Modul: DevOps`
- [ ] **Art. 88bis Trilog beobachten** — EU-Rat hat GDPR-KI-Aufweichung am 23.10 verabschiedet. Trilog mit EP läuft. Monatliches Update bis Jahresende. Strategisch: USP-Kommunikation prüfen, falls Art. 88bis in Kraft tritt. `Modul: Legal, Product-Strategy`
- [ ] **CRM Custom-Fields: Art.-9-Validierungsschicht prüfen** — Berliner DPA-Urteil zu politischem Microtargeting. Freifelder könnten indirekt Art.-9-Kategorien aufnehmen. UX-Review + optionaler Warnhinweis bei bestimmten Feldnamen/Werten. `Modul: CRM-Core`
- [ ] **AI-Act-Hochrisiko-Klassifikation fertigstellen** — Sprint 4 (weiterhin offen). Angesichts steigender KI-Adoption-Zahlen und rückendem Enforcement-Datum dringend. `Modul: Legal, AI Act`
- [ ] **Feed-URLs in `sources/_regulation.yaml` reparieren** — BfDI, BMAS, BSI-Presse, e-rechnung-bund dauerhaft 404. Neue URLs recherchieren oder auf HTML-Scraping umstellen. `Modul: Intel-Infra`
