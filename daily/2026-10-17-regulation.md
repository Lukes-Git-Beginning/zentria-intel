---
date: 2026-10-17
type: regulation
runtime_minutes: 19
items_scanned: 72
items_relevant: 16
kw: 42
sources_ok: [edpb-newsroom, bsi-warnungen, noyb, websearch-supplements]
sources_failed: [eur-lex, bfdi-pressemitteilungen, bsi-pressemitteilungen, e-rechnung-bmwk, eaid-arbeitsrecht, cybernews-eu, edpb-edps]
---

# Regulation-Sweep KW42/2026 (Sa 18. Oktober)

---

## DSGVO / Datenschutz — Enforcement

### Norwegian DPA fines Xandr (Microsoft) EUR 8,600,000 — Art. 6 + Art. 9 DSGVO — RTB-Tracking
- [Norwegian DPA fines Xandr EUR 8,600,000 for unlawful processing of personal data](https://www.edpb.europa.eu/news/norwegian-dpa-fines-xandr-eur-8-600-000-for-unlawful-processing-of-personal-data_en) *(16.10.2026 — EDPB-Newsroom)*
  — Xandr Inc. (jetzt Teil von Microsoft) verarbeitete im Real-Time-Bidding-Prozess personenbezogene Daten von Grindr-Nutzern — inkl. Advertising-ID, IP-Adresse und **implizite sexuelle Orientierung** (Tatsache der Grindr-Nutzung). Zwei Verstöße: (1) Art. 6(1) DSGVO — keine gültige Rechtsgrundlage; (2) Art. 9(1) DSGVO — Verarbeitung besonderer Kategorien (sexuelle Orientierung) ohne explizite Einwilligung nach Art. 4(11)/Art. 7. Kernargument: Xandr kann Einwilligungs-Verantwortung nicht an Grindr auslagern — als Joint Controller eigenständige Einwilligungspflicht. Entscheidung formal: 02.10.2026, Veröffentlichung über EDPB: 16.10.
  — **Cosmi-Implikation:** RTB-Muster für B2B-SaaS direkt relevant. Wenn Cosmi Tracking-IDs (Analytics, Marketing-Pixel) an Drittanbieter weitergibt → Xandr-Muster: Joint-Controller-Verantwortung endet nicht damit, dass „der andere Consent holt". Besonderer Prüfpunkt: Werden in CRM-Daten Informationen gespeichert, aus denen besondere Kategorien (Art. 9) abgeleitet werden könnten? Auch noyb-Verbindung: Xandr-Fall war noyb-Beschwerde 2020 — 6 Jahre bis zur Entscheidung. Digital-Omnibus-Tracking-ID-Ausnahme würde diesen Schutz untergraben. **Modul: DSGVO, CRM-Core, Legal**

### EDPB Statement — Smart Glasses & Datenschutz
- [EDPB publishes statement on data protection challenges of smart glasses](https://www.edpb.europa.eu/news/edpb-publishes-statement-on-the-data-protection-challenges-of-smart-glasses_en) *(13.10.2026 — EDPB)*
  — EDPB adressiert die Datenschutz-Risiken von Smart Glasses (z.B. Meta Ray-Ban 2024+): unsichtbare Kameras/Mikrofone, bystander-Aufzeichnung ohne Wissen, besonders riskant in sensiblen Kontexten (Büro, Krankenhaus, Schule). Empfehlungen: sichtbare Aufnahme-Indikatoren (LED, Audio), Hersteller dürfen Compliance nicht auf Nutzer abwälzen, Verarbeitungszweck muss mit ursprünglicher Erhebung kompatibel sein.
  — **Cosmi-Implikation:** Indirekte Relevanz. Wenn Cosmi-Kunden (Vertriebsteams, Fieldservice) Smart Glasses in Kundenkontakt-Situationen einsetzen → Art. 13/14-Informationspflicht für aufgezeichnete Bystander. Kunden-Konfigurations-Guide empfohlen, sobald Feldservice-Modul ausgebaut wird. **Modul: DSGVO, CRM-Core, Product**

### noyb Jahresbericht 2025 — EUR 2 Mrd. Bußgelder + CRIF-Sammelklage + OpenAI + Meta AI
- [noyb Annual Report 2025: EUR 2 billion in fines from noyb work](https://noyb.eu/en/annual-report-2025-out-now) *(13.10.2026)*
  — Rückblick 2025 (für Strategieperspektive): noyb-Beschwerden lösten €2 Mrd. DSGVO-Bußgelder aus. Pipeline 2026: (1) Erste Sammelklage gegen CRIF (Österreich — Bonitätsdaten, Zweckbindungsverstoß, OGH-Urteil Sept. 2026 als Grundlage). (2) Zweite Beschwerde gegen OpenAI — KI-Halluzinationen = falsche personenbezogene Daten = DSGVO-Verstoß. (3) Cease-and-Desist gegen Meta: KI-Training auf EU-Nutzerdaten. Parallelfront: Digital-Omnibus aktiv bekämpft.
  — **Cosmi-Implikation:** AI-Halluzinations-Beschwerde (OpenAI II) ist Präzedenz für jedes KI-Modul im Cosmi-Produkt das Text über Personen generiert (CRM-AI-Zusammenfassungen, Chatbot-Antworten mit Kundendaten). Falsche Daten über NatPer = Art. 5(1)(d) DSGVO (Richtigkeit) + Art. 16 Berichtigungsrecht. **Modul: DSGVO, AI Act, CRM-Core, Legal**

### noyb MEP-Datenschutz-Ranking — Digital Omnibus — EPP-Fraktion benotet „mangelhaft"
- [noyb ranking: Who in EU Parliament fights for your privacy — and who fights for Big Tech](https://noyb.eu/en/ranking-who-eu-parliament-fights-your-privacy-and-who-big-tech) *(12.10.2026)*
  — noyb analysierte 1.000+ EP-Änderungsanträge zum Digital-Omnibus (DSGVO/ePrivacy). EVP/EPP-Fraktion schlechteste Bewertung: Änderungen erhöhen Komplexität bei reduziertem Schutz. S&D, Grüne, Linke verteidigen Grundrechte. Interaktives Ranking: gdpr-omnibus.eu. Gibt Einblick in die EP-Mehrheitsverhältnisse für die bevorstehende Abstimmung.
  — **Cosmi-Implikation:** Übersetzung in politische Realität: Wenn EPP die führende EP-Fraktion ist, steigen Chancen auf eine privacy-schwächende Digital-Omnibus-Fassung. Art. 88bis (AI-Training als Legitimate Interest) und Tracking-ID-Ausnahme könnten durchkommen, sobald EP Mehrheit findet. Cosmi-USP „Privacy-by-Design" wäre kurzfristig weniger USP, mittelfristig gegen noyb-Klagen ein Schutzwall. Ranking lesen für Netzwerk-/Lobbying-Einschätzung. **Modul: DSGVO, Legal, Product**

---

## DSGVO / Datenschutz — Policy

### Digital Omnibus: COREPER-Abstimmung 11.10.2026 gescheitert — DE + FR blockieren erneut
- [EU Digital Omnibus stalls again — current GDPR rules still apply](https://quasa.io/stories/eu-digital-omnibus-stalls-again-current-gdpr-rules-still-apply) *(11.10.2026)*
  — Der erwartete COREPER-Ratsbeschluss für ein Ratsmandat am 11.10.2026 kam nicht zustande. Deutschland und Frankreich blockierten erneut — diesmal über Data-Act-Handelsgcheimnisschutz-Klauseln. Im EP: Co-Rapporteure Salla (EPP) + Kaljurand (S&D) haben Draft-Report (22.06.2026) vorgelegt, aber kein Ausschussvotum. Irische Ratspräsidentschaft. Aktueller DSGVO-Rechtsstand gilt unverändert.
  — **Cosmi-Implikation:** Kein Handlungsbedarf basierend auf Digital Omnibus. Art. 88bis, Tracking-ID-Ausnahme: nicht in Kraft. SCC/Art. 6-Planung weiterhin auf aktuellem DSGVO-Stand. Aber: noyb-Ranking (oben) zeigt, EP-Mehrheiten für privacy-schwächende Version sind möglich sobald Stau aufgelöst. Beobachtungsstatus bleibt HOCH. **Modul: DSGVO, AI Act, Legal, Product**

---

## AI Act

### EU-Kommission: Konsultation AI-Act-Bußgeldverfahrens-Verordnung — bis 09.11.2026 *(23 Tage)*
- [European Commission launches public consultation on draft implementing act under AI Act](https://agenceurope.eu/en/bulletin/article/13958/18/european-commission-launches-public-consultation-on-draft-implementing-act-under-ai-act) *(12.10.2026)*
  — Konsultation (bis 09.11.2026) zur Durchführungsverordnung über praktische Modalitäten der Bußgeldverfahren unter dem AI Act. Implementiert Art. 75c/75d AI Act (eingefügt Sommer 2026): Kommission als **Exklusivaufsicht** für KI-Systeme in designierten sehr großen Plattformen (VLOP) + systemeigene GPAI-Modelle. Schlüsselregeln: (1) Akteneinsicht nach Mitteilung vorläufiger Feststellungen, (2) 5-Jahres-Verjährungsfristen (Unterbrechung/Aussetzung möglich — wichtig: Kommission kann Frist-Neustart für Google/Meta KI auslösen), (3) Vertraulichkeitsschutz für Geschäftsgeheimnisse. Verabschiedung: Q4 2026.
  — **Cosmi-Implikation:** Direkte Relevanz für Cosmi als KI-Systemanbieter. Klarheit über Enforcement-Mechanismen = kalkulierbares Risiko. 5-Jahres-Verjährung bedeutet: AI-Act-Verstöße aus 2026 können bis 2031 sanktioniert werden. Konsultationsbeiträge von Bitkom/eco bis 09.11. beobachten — werden Praxis-Positionen zu Art. 75c Scope definieren. **Modul: AI Act, Legal, Product**

### AI Act: 20+ Loss-of-Control-Incidents 2026 — Kommission Enforcement aktiv
- [EU Announces First AI Act Enforcement Actions After AI Agent Incidents](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/) *(KW42)*
  — Mehr als 20 dokumentierte Kontrollverlust-Vorfälle 2026 (OpenAI, Anthropic, Google DeepMind, Meta, unabhängige Evaluationsorg.). AI Office hat Incident-Reports angefordert + Informationsanfragen zu Sicherheitspraktiken versandt. Zeigt: Enforcement ist kein Papier-Prozess mehr.
  — **Cosmi-Implikation:** Falls Cosmi AI-Agenten / autonome Entscheidungssysteme entwickelt oder einsetzt: Incident-Reporting-Prozess nach AI Act jetzt definieren. Art. 73 AI Act (Meldepflicht für schwerwiegende Vorfälle) greift ab 02.08.2026. **Modul: AI Act, Product, Legal**

### Italien: AI-Act-Enforcement-Dekret — Legislative Decree 179 — ab 23.10.2026 in Kraft *(6 Tage)*
- [Italy finalises domestic AI Act enforcement: Legislative Decree 179 effective October 23, 2026](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/) *(KW42)*
  — Italien ist erstes EU-Mitgliedsland mit vollständigem nationalem AI-Act-Durchsetzungssystem. Aufsichtsbehörden: AgID (Agenzia per l'Italia Digitale) + ACN (Agentur für nationale Cybersicherheit). Bußgelder für verbotene KI-Praktiken: bis €35 Mio. oder 7% Weltjahresumsatz. Modell wird von anderen Mitgliedsstaaten beobachtet und repliziert.
  — **Cosmi-Implikation:** Wenn Cosmi Kunden in Italien hat und dort KI-Systeme betreibt → ab 23.10.2026 AgID/ACN-Aufsicht. DE-Umsetzungsgesetz (NIS2UmsuCG-Analogon für AI Act) fehlt noch, aber IT zeigt Tempo. Hochrisiko-KI-Klassifikation (Annex III) gilt EU-weit. **Modul: AI Act, Legal, Product**

### OpenAI textGrain — EU ChatGPT/Codex Watermarking — AI Act Art. 50
- [OpenAI announces textGrain invisible text watermark for EU ChatGPT and Codex](https://www.transparencycoalition.ai/news/ai-legislative-update-october16-2026) *(16.10.2026)*
  — OpenAI kündigt „textGrain" an: unsichtbares digitales Textwasserzeichen für ChatGPT und Codex in der EU. Ansatz analog zu Googles SynthID-Text. Reagiert auf AI Act Art. 50 Watermarking-Deadline (02.12.2026). Maschinenlesbare Kennzeichnung gemäß EN ISO/IEC 42001-kompatiblem Standard.
  — **Cosmi-Implikation:** Benchmark-Ankündigung. OpenAI wählt proprietäres Watermarking-Format (textGrain). Cosmi-Entscheidung: (1) SynthID-Text (Google, open), (2) C2PA (Coalition for Content Provenance and Authenticity, Industriestandard), (3) Eigenlösung. C2PA empfohlen für Interoperabilität. **46 Tage** bis Deadline — Implementierung muss diese Woche starten. **Modul: AI Act, Product, Legal**

### AI Act Art. 50 Watermarking-Deadline — **46 Tage** (02.12.2026) — AKUT
- Enforcement seit 02.08.2026 aktiv. Grandfathering-Window läuft ab. 46 Tage = 2 Sprint-Zyklen. OpenAI-Ankündigung erhöht Sichtbarkeit — Aufsichtsbehörden werden KW49/50 Compliance prüfen. Bußgeld: bis €15 Mio. oder 3% Umsatz. **Modul: AI Act, Legal, Product**

---

## NIS2

### BSI — NIS2-Durchsetzungsinitiative Q4 2026 — 49% der Unternehmen haben nicht angefangen
- [NIS2 in Germany: Implementation Status and BSI Plans 2026](https://www.kertos.io/en/blog/nis2-germany) *(KW42)*
  — BSI startet Q4 2026 **Enforcement-Initiative** gegen nicht-registrierte NIS2-pflichtige Einrichtungen. Hintergrund: Von 29.500 meldepflichtigen Einrichtungen (Registrierungsfrist 06.03.2026) haben 18.000 die Frist versäumt — nur 27% registriert. 49% haben NIS2-Umsetzung nicht begonnen oder prüfen noch ob sie betroffen sind. BSI-Plan: Q1 2027 → Anordnung ausgewählter wesentlicher Einrichtungen zu Audits.
  — **Cosmi-Implikation:** Falls Cosmi als NIS2-„wichtige Einrichtung" gilt (B2B-SaaS, ggf. Sektor „digitale Infrastruktur" oder „IKT-Dienste"): (1) Registrierung beim BSI überprüfen — nicht registriert = erste Angriffsfläche in Q4-Enforcement. (2) Mindestvorgaben §30 BSIG (Risikomanagement, Incident-Response, Lieferkette) dokumentieren. (3) Q1 2027 Audit-Anordnung = konkrete Frist für vollständige NIS2-Dokumentation. **Modul: NIS2, Security, Legal**

---

## XRechnung / e-Rechnung / GoBD

### Countdown: **76 Tage** bis 01.01.2027 — GoBD-Korrektur: 8 Jahre Archivierung für Rechnungen
- Keine neuen Regulierungen KW42. Wichtige Klarstellung aus BEG IV (Bürokratieentlastungsgesetz IV, in Kraft 2025): Aufbewahrungsfrist für **Rechnungen** wurde auf **8 Jahre** verkürzt (vorher 10 Jahre). Buchhalterische Grundaufzeichnungen weiterhin 10 Jahre. **Korrektur aus KW41-Output**: Aussage „10 Jahre unveränderlich" galt allgemein — für Rechnungs-XML konkret 8 Jahre korrekt. Ab 01.01.2027: Unternehmen >800k EUR Vorjahresumsatz → obligatorisch XRechnung/ZUGFeRD (EN 16931) B2B DE. Ab 01.01.2028: alle DE-Unternehmen. Cosmi-buchhaltung-Modul muss: (1) XML-Originale 8 Jahre unveränderlich archivieren, (2) ZUGFeRD/XRechnung versenden können, (3) eingehende E-Rechnungen verarbeiten. **Modul: XRechnung, Vertraege, Finance**

---

## ArbZG / Arbeitsrecht

### Stille Woche
- Kein neuer Kabinettsbeschluss oder Referentenentwurf zum ArbZG. BMAS-RSS 404 (Woche 7+ in Folge). Laufender BMAS-Referentenentwurf (Juni 2026) im legislativen Prozess. Keine Handlung erforderlich.

---

## eIDAS

### **MEILENSTEIN: DIdG VERABSCHIEDET** — Bundestag 15.10.2026 — EUDI Wallet „d-you" Start 02.01.2027 — **68 Tage** bis EU-Deadline
- [Bundestag macht Weg für die EUDI-Wallet frei — DIdG beschlossen](https://www.bundestag.de/dokumente/textarchiv/2026/kw42-de-digitale-identitaeten-gesetz-1223586) *(15.10.2026)*
  — Bundestag verabschiedete das Gesetz über digitale Identitäten (DIdG) am 15.10.2026 mit Mehrheit CDU/CSU + SPD. Dagegen: AfD, Grüne, Linke. Biometrisches-Foto-Opt-out ergänzt (epicenter.works-Forderung teilweise aufgegriffen). DE EUDI-Wallet-App: **„d-you"**, geplanter Rollout **02. Januar 2027**. EU-Deadline für Mitgliedstaaten: **24.12.2026 (68 Tage)**. Nächste Station: Bundesrat (kein Einspruchsrecht erwartet). Ablehnung eines AfD-Antrags (EUDIW-Moratorium + Rücknahme eIDAS-Wallet-Provision).
  — **Schritt-für-Schritt Cosmi-Aktionsplan ab sofort:** (1) **Relying Party Registration**: Cosmi muss sich als EUDI Wallet Relying Party registrieren — Voraussetzung für Wallet-Attributsabfragen (z.B. B2B-Identitätsverifizierung, Vertragsabschluss). (2) **Attributszertifikate**: Klärung welche Attribute Cosmi im B2B-Kontext abfragt (Name, Unternehmensregistrierung, Vollmacht). (3) **OpenID4VP-Integration**: Technisches Protokoll für EUDIW-Anbindung (OpenID for Verifiable Presentations). (4) **Datenschutz-by-Design**: Wallet-Abfragen sind datensparsamkeitskritisch — nur notwendige Attribute abfragen. Cosmi-Module relevant: Vertraege (Signatur/Verifizierung), CRM-Core (Kontaktverifizierung). **Modul: eIDAS, Product, Vertraege, CRM-Core**

---

## BSI-Warnungen (CVE-Filter: CRM, SaaS, cloud, auth, CI/CD)

### **Keycloak GEPATCHT** — 26.8.1 (13.10.2026) — 19 CVEs — Privilege Escalation + SAML Bypass
- [Keycloak 26.8.1 Released: 19 CVEs patched — privilege escalation to realm-admin](https://www.keycloak.org/2026/10/keycloak-2681-released) *(13.10.2026)*
  — **STATUS-ÄNDERUNG: UNPATCHED → GEPATCHT.** Keycloak 26.8.0 (01.10.2026): 3 CVEs. 26.8.1 (13.10.2026): 18 Keycloak-CVEs + 1 jackson-databind (High). Kritischste Patches: (1) **CVE-2026-94000**: Delegierter Admin mit nur `manage-users`-Rolle kann durch Beitritt zu Gruppe mit Admin-Rolle **Realm-Admin werden** — Privilege Escalation. (2) **CVE-2026-94001**: Admin-Credential DELETE umgeht `denied reset-password`-Permission. (3) **CVE-2026-18963**: SAML Bypass (kritisch, separate Advisory). Zuvor gemeldetes WID-SEC-2026-3849 (Info Disclosure, Security Bypass, XSS) — durch 26.8.1 adressiert.
  — **Cosmi-Implikation:** **Sofort auf 26.8.1 updaten** falls Cosmi Keycloak einsetzt. CVE-2026-94000 ist besonders gefährlich in Multi-Tenant-Setup (Cosmi-Kundenmandanten): kompromittierter Mandanten-Admin → Realm-Admin → zugang zu anderen Mandanten möglich. Upgrade-Checkliste unter wz-it.com verfügbar. **Modul: Security, Infra — sofort**

### Samba — KRITISCH — Code Execution, DoS, File Manipulation
- BSI WID 16.10.2026: Samba mehrere Schwachstellen KRITISCH. Beliebige Codeausführung, DoS, Dateimanipulation, Kontrollumgehung.
  — **Cosmi-Implikation:** Falls Samba als SMB-Share / AD-Integration in Cosmi-Infra oder Kundenumgebungen eingesetzt: Patch sofort. Betrifft primär On-Premise-Deployments. Cosmi selbst-gehostet → Kundenseitige Samba-Exposition möglich. **Modul: Security, Infra**

### JetBrains TeamCity — HOCH — Code Execution + XSS
- BSI WID 16.10.2026: JetBrains TeamCity Code Execution + XSS HOCH.
  — **Cosmi-Implikation:** Falls Cosmi TeamCity als CI/CD-System nutzt → Patch einspielen. XSS in CI/CD-Dashboard = Angriff auf Entwicklungsinfrastruktur und Supply Chain. Alternativ: GitLab CI / GitHub Actions haben diesen Vektors nicht. **Modul: Security, Infra**

### Microsoft Office — KRITISCH — Privilege Escalation + Code Execution
- BSI WID 16.10.2026: Microsoft Office Produkte KRITISCH — Privilege Escalation, Arbitrary Code Execution, Information Disclosure, Security Bypass. Patch über Microsoft Update.
  — **Cosmi-Implikation:** Betrifft Endnutzer-Geräte im Cosmi-Team und bei Kunden. Patch über regulären Update-Zyklus. **Modul: Security**

### Mattermost — MITTEL — Mehrere Schwachstellen (SaaS/Kollaboration)
- BSI WID 16.10.2026: Mattermost (Open-Source-Kollaborationsplattform, direkte Kategorie-Alternative zu Slack) — Privilege Escalation, DoS, Information Disclosure, File Manipulation, Security Bypass.
  — **Cosmi-Implikation:** Falls Mattermost in Cosmi-Infra oder Kundenumgebungen: Patch einspielen. Auch als Wettbewerber-Intelligenz: Mattermost KW42 Sicherheitslücken. **Modul: Security, Infra**

---

## DPF / Transatlantische Datenübermittlung

### Schrems III — Laufendes CJEU-Verfahren *(Carry-over)*
- DPF formal gültig. noyb-CJEU-Klage (Grundlage: US Supreme Court Jun 2026 — FTC-Unabhängigkeit untergraben) eingereicht. Verfahren: 2–4 Jahre. SCC-Fallback-Audit aktuell halten. Neuer BfDI Hennemann: Bundestag-Vorstellung KW41 — erste konkrete AI-Act/DPF-Positionen noch ausstehend, werden KW43 erwartet. **Modul: DSGVO, Legal, Infra**

---

## Stille Bereiche

- **EUR-Lex RSS** — 404 (Woche 10+ in Folge). Keine neuen EU-Sekundärrechtsakte mit direkter Cosmi-Relevanz via Feed. WebSearch: keine neuen Rechtsakte KW42.
- **BfDI RSS** — 404. Hennemann-Bundestag-Vorstellung KW41 dokumentiert. Neue Stellungnahmen KW43 erwartet.
- **BSI Pressemitteilungen RSS** — 404. BSI-Advisory-Zusammenfassung via WID-Feed abgedeckt.
- **e-rechnung-bund.de RSS** — 404. XRechnung-Stand konstant.
- **ENISA RSS** — 404. ETL 2026 Carry-over aus KW40.
- **BMAS RSS** — 404. ArbZG: stille Woche.
- **EDPS** — 403. Keine EDPS-spezifischen Items KW42.

---

## Cosmi-Action-Items

- [ ] **[AKUT] PostgreSQL 14 EOL — 26 Tage** (12.11.2026) — Upgrade auf PG 17 als Sprint-Blocker jetzt. 26 Tage = letzte realistische Chance für einen geordneten Upgrade-Sprint. PG 17 oder 18 empfohlen (PG 15/16 zu kurze Laufzeit). *(Infra, DB — sofort)*
- [ ] **[AKUT] Keycloak → Update auf 26.8.1** — CVE-2026-94000 (Privilege Escalation → realm-admin in Multi-Tenant) + CVE-2026-94001 + SAML Bypass. Upgrade-Checkliste wz-it.com. Vorheriges WID-SEC-2026-3849 damit adressiert. *(Security, Infra — sofort)*
- [ ] **[AKUT] AI Act Art. 50 Watermarking — 46 Tage** (02.12.2026) — OpenAI hat textGrain angekündigt: Benchmark-Signal. Cosmi: C2PA oder SynthID-Text evaluieren + Implementierung diese Woche starten. 2 Sprint-Zyklen verbleiben. *(AI Act, Product — diese Woche)*
- [ ] **[AKUT] Italy AI Act Enforcement ab 23.10.2026** — 6 Tage. Falls Cosmi Kunden in IT hat + KI-Systeme dort betreibt: AgID/ACN-Compliance-Baseline prüfen. Hochrisiko-KI Annex III gilt EU-weit. *(AI Act, Legal)*
- [ ] **[MILESTONE] DIdG verabschiedet → EUDIW-Anbindung Q4-Sprint starten** — d-you Start 02.01.2027. Relying-Party-Registrierung + OpenID4VP-Protokoll + Attributszertifikate für B2B (Vertraege-Modul). EU-Deadline 24.12.2026 (68 Tage). *(eIDAS, Product, Vertraege)*
- [ ] **[Followup] AI Act Penalty Procedures Konsultation** — bis 09.11.2026 (23 Tage). Bitkom/eco-Einreichungen beobachten. Art. 75c-Scope für GPAI + VLOP-gebundene KI relevant. *(AI Act, Legal)*
- [ ] **[Followup] EDPB Fining-Methodology-Konsultation** — bis 13.11.2026 (27 Tage). Standardisiertes Bußgeldkalkül — Bitkom/eco-Kommentare lesen. *(DSGVO, Legal)*
- [ ] **[Followup] NIS2 Registrierung beim BSI** — BSI Enforcement Q4 2026 aktiv. Registrierungsstatus verifizieren. §30 BSIG Risikomanagement-Dokumentation anlegen. Q1 2027 Audit möglich. *(NIS2, Security, Legal)*
- [ ] **[Followup] e-Rechnung Versand-Fähigkeit** — 76 Tage bis 01.01.2027. GoBD-Korrektur: 8 Jahre Archivierung für Rechnungs-XML (nicht 10). *(XRechnung, Finance)*
- [ ] **[Followup] Art. 22 DSGVO-Audit** *(Carry-over Uber-€825M-Case)* — Vollautomatisierte Entscheidungen mit erheblichen Folgen: Inventar + menschliche Überprüfung + Opt-out. *(DSGVO, AI Act, CRM-Core)*
- [ ] **[Followup] Löschanfragen-SOP + Retention Policy Audit** *(Carry-over SCHUFA-Muster)* — Art. 21 Opt-out unverzüglich, Art. 5(1)(e)/Art. 17 Speicherfrist-Compliance. *(CRM-Core, DSGVO)*
- [ ] **[Beobachten] Digital Omnibus** — COREPER erneut gescheitert (11.10.). Aktueller DSGVO-Stand gilt. Nächste Abstimmungsankündigung sofort eskalieren. Art. 88bis + Tracking-ID: nicht in Kraft. *(DSGVO, AI Act, Legal)*
- [ ] **[Beobachten] BfDI Hennemann — erste Stellungnahmen** — KW43 erwartet. AI-Act-DSGVO-Spannung, DPF, Art. 88bis. Cosmi-USP-relevant. *(DSGVO, Legal)*
- [ ] **[Beobachten] noyb: OpenAI Halluzinations-Beschwerde II** — Präzedenz für KI-Textgenerierung über NatPer. Cosmi CRM-AI-Zusammenfassungen: Art. 5(1)(d) Richtigkeit prüfen. *(DSGVO, AI Act, CRM-Core)*
