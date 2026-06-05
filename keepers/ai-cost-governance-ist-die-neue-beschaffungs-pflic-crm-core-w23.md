---
id: W23-T05-i01
slug: ai-cost-governance-ist-die-neue-beschaffungs-pflic-crm-core-w23
created: '2026-06-05'
weekday: friday
modules:
- crm-core
- buchhaltung
- einkauf
- inventar
- produktion
themes: []
n_sources: 0
trend_score: 5
decision: keep
---

**Drei Daten-Punkte aus drei verschiedenen Tagen** beschreiben dasselbe Phänomen: Die "Unlimited AI für alle"-Phase 2024-2025 endet abrupt. Outcome-Metriken werden Procurement-Voraussetzung.

**Datenpunkt 1: Diginomica "Token Gesture" (Mi 03.06.):**

| Unternehmen | Vorfall |
|---|---|
| **Uber** | Verbraucht gesamtes $3,4 Mrd. 2026-AI-Budget bis April. 95% Ingenieure nutzen AI-Tools, 70% Commits AI-generiert. Kosten ~$2.000/Entwickler/Monat. |
| **Microsoft** | Zieht Claude Code für ~100.000 Ingenieure zurück — Kosten nicht mehr rechtfertigbar. |
| **Walmart** | Setzt Quotas für Code Puppy nach vorher unlimitiertem Zugang. |
| **Anonym** | $500 Mio. Rechnung für 30 Tage unbegrenzten Claude-Zugang für alle Mitarbeiter. |

Gegenposition: Jensen Huang (NVIDIA): *"Jeder Token ist Umsatz, ich wäre tief besorgt wenn ein $500K-Ingenieur weniger als $250K in Tokens verbraucht."* Marc Benioff (Salesforce): plant $300 Mio./Jahr Anthropic-Ausgaben, evaluiert Outcome-Based-Pricing. Uber COO: *"Wenn man keine messbaren Verbindungen zwischen AI-Produktivität und tatsächlich gelieferten Features herstellen kann, ist die Ausgabe nicht zu rechtfertigen."*

**Datenpunkt 2: Uber $1.500/Monat Hard-Cap pro Mitarbeiter (Do 04.06., Simon Willison/HN #400):**
- Bei zwei aktiven AI-Tools + $330k Durchschnittsgehalt: ~11% des Jahresgehalts als AI-Tool-Budget.
- Uber kalkulierte das 2025 — *"bevor irgendjemand vorhersagen konnte, wie populär Token-verbrauchende Coding-Agents werden."*
- Simon Willison liest das als impliziten Marktpreis für AI-Produktivität.

**Datenpunkt 3: HubSpot "AI Perception-Reality Gap" (Do 04.06.):**
- Customer Agent: **25% schnellere Ticket-Reaktionszeit, 70% Lösungsquote**
- Prospecting Agent: **76% mehr Leads, 80% mehr Meetings**
- Externe Wahrnehmung: 57% sagen, AI-Risiken überwiegen Benefits
- HubSpots Outcome-Pricing-Modell (**$0.50/conv, $1/lead** — seit April live) nachträglich als moralisch überlegen positioniert.
- Parallel: HubSpot AEO-Forschung (Listicles + Vergleichsseiten erhalten höchste Citation-Raten in ChatGPT/Gemini) — systematische SEO-Autorität für die Post-Google-Suchwelt.

**Cosmi-Implikation:** Vier Pflicht-Antworten:

1. **Cosmi-AI-Pricing-Klarheit BEFORE first AI-feature launch.** Wenn Kunden ab Q4 fragen: *"Was kostet Cosmi-AI pro Monat?"* — muss die Antwort **"Im Modul-Preis enthalten (Flat, vorhersagbar)"** sein. Credits-Pricing (siehe monday-Pivot W20-Keeper) ist für DACH-KMU-Zielgruppe ein Conversion-Killer. Sprachregelung: **"Cosmi-AI: Predictably affordable. Kein Token-Lottery."** Modul-Pfad: `marketing/pricing/cosmi-ai-flat-fee-positioning/`.

2. **AI-Outcome-Layer als Architektur-Voraussetzung.** HubSpot-25%/70%/76%/80%-Zahlen sind das neue Vendor-Pitch-Format. Cosmi-AI braucht von Anfang an Measurement-Layer:
   - **Helpdesk:** Resolution-Rate, Time-to-First-Response, Auto-Resolve-Rate
   - **CRM:** Forecast-Accuracy-Delta, Lead-Qualification-Conversion
   - **Buchhaltung:** Reconciliation-Time-Saved
   - **Cross:** Hours-Saved/Week pro User
   - Modul-Pfad: `backend/internal/analytics/ai-outcomes/`, `backend/internal/analytics/cost-transparency/`.

3. **ROI-Story-Pipeline für Sales:** Sobald ein First-Kunde Cosmi-AI nutzt, ist dessen Resolution-Rate-Story das wichtigste Marketing-Asset. Travelers-Pattern (siehe W23-T07): *"X% AI-Resolution-Rate, Y Stunden gespart/Woche"* — Cosmi muss diesen Case-Study-Workflow vor First-Kunde planen, nicht danach. Beta-Kunden-Vereinbarung muss Erlaubnis für Outcome-Datennutzung enthalten.

4. **AEO-Vertriebskanal aufbauen.** HubSpot publiziert Vergleichs-Content systematisch — Cosmi sollte **"Cosmi vs. HubSpot für DACH-KMU"** und **"Cosmi vs. Salesforce für DACH-KMU"** als strukturierte Listicles/Vergleichsseiten haben, sobald ChatGPT/Gemini diese als Antwort-Quelle nutzen. AEO ist kein Marketing-Add-on mehr, sondern der nächste SEO-Funnel.

**Modul-Pfad:** `backend/internal/analytics/ai-outcomes/`, `backend/internal/analytics/cost-transparency/`, `marketing/pricing/cosmi-ai-flat-fee-positioning/`, `marketing/content/cosmi-vs-hubspot-dach/`, `marketing/content/cosmi-vs-salesforce-dach/`, `marketing/aeo/comparison-page-templates/`.

**Quellen:** 9 Items aus 6 Quellen (Diginomica ×2 [Token Gesture, McKinsey Agentic Marketing], HubSpot-Blog ×2, Simon Willison Newsletter, HN-Thread).

**Trend-Score:** 0.87 (höchste Tages-Konvergenz unter Pricing-Trends; direkter Folge-Cluster zu W22-AI-Backlash).

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss

---

## Modul-Kapitel (alle 14 Cosmi-Module)

### crm-core (31 Items, 4 Cluster)

**Was lief diese Woche:**
- **Salesforce Connections 2026 + Contentful-Akquisition + Headless 360 Erklär-Kontroverse** sind der dominante Cluster (siehe Top-5 #1).
- **HubSpot doppelt offensiv:** Outcome-Pricing-Rechtfertigung ("Perception-Reality Gap") + AEO-Content-Forschung (Listicles/Produktseiten als Citation-Träger in ChatGPT/Gemini). Plus carry-over W22: HubSpot Capital Beta (eingebettete Finanzierung), HubSpot MCP Server GA, HubSpot Agent CLI Private Beta.
- **Pipedrive MCP** (W22 carry-forward) bleibt aktiv.
- **EspoCRM 9.3.8 Maintenance Release** — kein Feature-Highlight, kein AI-Counter-Move (bestätigt W20-Beobachtung).
- **Twenty (W20-Keeper)** — keine neuen Releases diese Woche; v2.8.0 (Webhook Tool Providers v2) bleibt der letzte materielle Schritt. Open-Source-CRM-Watch verlangsamt nach Sprint-Modus W21.
- **Salesforce kauft Contentful** ist Erweiterung des `direct-competitor-triple-pivot`-Keepers (W20) + des `eu-sovereignty-kipppunkt`-Keepers (W20) — US CLOUD Act bei deutschem Berliner GmbH-Status nach Closing.

**Items diese Woche:** W23-T01-i01 (Top-5), W23-T01-i02 (Headless 360 Verwirrung), W23-T01-i03 (HubSpot AEO), W23-T05-i01 (Top-5 Outcome-Pricing), plus Background-Items.

**Cosmi-Roadmap-Signal:** "AI-First-CRM" + "Cross-Modul-Kontext-Agent" sind die zwei zwingenden Architektur-Entscheidungen vor Cosmi-CRM-Launch (vor Sommer 2026). Modul-Pfad: `backend/internal/crm/agent-workflows/`, `backend/internal/crm/ai-forecast/`, `backend/internal/crm/cpq/` (Custom Quote Modules sind Tabellenstake nach HubSpot W22).

---

### dialer (0 substantielle Items, 0 Cluster, 4-TAGE-FEED-AUSFALL)

**Was lief diese Woche:** **Strukturell stille Woche durch Feed-Ausfall — kein verifizierbarer Markt-Stand.**

- **Aircall, JustCall, Sipgate-Feeds**: 404 an 4 aufeinanderfolgenden Werktagen (Mo-Do). LiveKit Redirect-Problem (`livekit.io` → `livekit.com`) und letzter Release v1.12.0 (19.05.) am Watermark.
- **Carry-forward W20-Keeper (`aircall-ai-voice-blitz-dialer-markt-ist-2026-markt-cross-w20.md`):** Tabellenstake-Anforderungen bleiben: Transkription, CRM-Sync, Call-Summary, AI-Voice-Agent.
- **Indirekte Bestätigung des Keepers** durch W23-T07-i01 (Travelers/OpenAI 85-90% AI-Voice-Resolution): das Voice-AI-Pattern, das W20 für den Dialer-Markt prognostiziert hatte, läuft 2026 in einem Nachbarmarkt (Insurance) live. Dialer-Roadmap-Implikation bleibt unverändert: Voice-AI + CRM-Integration vor Cosmi-Dialer-Launch.

**Tier-1-Pflege-Befund:** Quellen-Audit dringend nötig. Vorschlag aus Mi-Evening-Deep:
- Aircall Blog: `https://aircall.io/blog/feed/`
- JustCall: `https://justcall.io/blog/feed/`
- Sipgate: `https://www.sipgate.de/blog/feed`
- LiveKit: Update `sources/dialer.yaml` auf `https://livekit.com/blog/feed`

`sources/dialer.yaml` und `.state/watermarks.json` müssen vor W24 aktualisiert werden, sonst bleibt Dialer-Modul ein blinder Fleck.

---

### helpdesk (16 Items, 3 Cluster)

**Was lief diese Woche:**
- **Travelers/OpenAI AI-Voice-Claim-Assistant Countrywide-Rollout** (siehe W23-T07-i01 Hot-Cluster): 85-90% AI-Resolution-Rate als neue Branche-Benchmark.
- **Intercom: "Knowledge Management for AI Service Agent"** — Framework-Guide. Intercom positioniert sich nicht mehr als Tool, sondern als **Knowledge Infrastructure Platform**. Datenpunkt: 82% der Senior Leaders haben 2025 in AI-Service-Tools investiert, 87% planen es für 2026. 5-10h/Woche pro Contributor für KB-Maintenance ist die akzeptierte Investitionsgröße.
- **Front: "What to automate, and what to keep human"** — 3-Tier-Framework: **Automate** (Recherche/Signal-Detection), **Assist** (Triage/Priorisierung), **Own** (Beziehungsmomente). Direkt verwertbare Messaging-Vorlage für Cosmi-Sales-Collateral.
- **Front: "Customer Communication Platforms"** — B2B-Positionierungs-Guide gegen Zendesk/Freshdesk/Helpscout.
- **Zammad 7.0 Security Patches** (Mo) — Backportierte Sicherheitsfixes für 7.0 + 6.5. AI-Features (Ticket-Summaries, AI-Drafts) seit März 2026 in Produktion.

**Feed-Pflege-Notiz:** Front RSS gestern (Do 04.06.) erstmals 404 — neuer Failure. Intercom-Watermark steht, Zammad ohne neue Releases. Zendesk RSS hängt an .de-Redirect (3. Folgewoche).

**Cosmi-Roadmap-Signal:** Helpdesk ist das **operative AI-Battleground-Modul** der Woche (4 Items am Di-Evening). Cross-Modul-Knowledge-Layer (CRM-Deal-History + Schichten + Buchungshistorie + Helpdesk-Conv) ist der einzige skalierbare Moat gegen Intercom/Fin und Zendesk. Modul-Pfad: `backend/internal/helpdesk/ai/triage-draft/`, `backend/internal/helpdesk/ai/knowledge-context/`, `backend/internal/helpdesk/knowledge-graph/`.

---

### video (3 Items, 1 Cluster)

**Was lief diese Woche:**
- **Gemini Omni: AI-Avatar-Klon in 15 Minuten** (Lenny's Newsletter, Do) — Self-Service AI-Video-Avatars als Marketing-Asset. Commoditisierung sichtbar.
- **LiveKit:** kein neues Release seit v1.12.0 (19.05.). URL-Redirect `livekit.io` → `livekit.com`.

**Cosmi-Implikation:** Wenn AI-Avatar-Videos Commodity werden, muss Cosmi-Video-Modul-USP **anders** begründet werden: **DSGVO-konforme Aufzeichnung, EU-Server, Meeting-Integration mit CRM-Kontext** — nicht "auch Video", sondern "Video, das Cosmi-Daten kennt". Modul-Pfad: `backend/internal/video/dsgvo-compliant-recording/`, `backend/internal/video/cosmi-context-integration/`.

---

### wiki (2 Items, 1 Cluster — neu)

**Was lief diese Woche:**
- **Hyper (YC P26) "Self-Driving Company Brain"** (HN #57, Do) — Knowledge-Graph-Plattform für Unternehmenskontext (Slack, Dokumente, E-Mails → hybrides Memory: Episodes + Facts). YC-P26-Kohorte = Pre-Produkt, JS-only-Landing-Page (kein Deep-Fetch möglich).
- **Stanford CS336 CLAUDE.md viral** (HN #1, 350 Punkte, Di) — Agent-Instructions-as-Code wird akademisches Lehrmaterial.

**Cosmi-Implikation:** Hyper adressiert exakt das "Company Brain"-Problem, das Cosmi für KMU lösen will — aber horizontal, nicht vertikal. **Entscheidung jetzt nicht fällig**: Hyper ist Pre-Produkt. Monat-6-Followup-Marker setzen. CLAUDE.md-Vorlage für Cosmi-Agents würde Dev-Community direkt ansprechen. Modul-Pfad: `backend/internal/wiki/ai-knowledge/`, `docs/dev/cosmi-claude-md-template/`.

---

### formulare (3 Items, 1 Cluster)

**Was lief diese Woche:**
- **Cloudflare Turnstile WebGL-Fingerprinting** (Mo, HN #1 553 Punkte) — passive Browser-Fingerprinting ohne Consent. WebKit-Browser (Safari) blocken historisch, Turnstile schließt sie aus. **DSGVO-Frage akut im Licht von EDPB CEF 2026 Art. 12-14 Transparenz-Enforcement.**
- **NOYB vs. Schibsted "Pay or Okay"-Modell** (Do, NOYB direct) — 99% scheinbare Consent-Rate vs. 0,16-7% freiwillige Tracking-Zustimmung. Beschwerde bei Norwegischem Datenschutzrat eingereicht, NOYB koordiniert. Welle wandert Norden→Süden: Skandinavien → Benelux → DACH.

**Cosmi-Implikation:** Direkte Prüfpflicht: Ist Cloudflare Turnstile auf cosmi.app / Marketing-Site / Cosmi-Forms aktiv? Falls ja → explizite Einwilligung oder Wechsel (hCaptcha privacy-Modus, eigene Lösung). Cosmi-Formulare müssen DSGVO-konforme Defaults haben — kein Dark-Pattern. Modul-Pfad: `backend/internal/forms/captcha/`, `infrastructure/cloudflare/`, `backend/internal/forms/consent-management/`.

---

### vertraege (4 Items, 1 Cluster)

**Was lief diese Woche:**
- **Wordsmith (UK-Legal-AI): $70 Mio. Series B** (Do, Sifted) — AI-gestützte Rechtsrecherche und Contract Intelligence im EU-Markt. Direkt vergleichbar mit W20-Carry-forward Legora ($550 Mio. / $5,6 Mrd. Valuation).
- **eIDAS-Carry-forward (Sa-Reg):** EUDI Wallet bis September 2026 EU-MS-Pflicht — Large Scale Pilots laufen.
- **Anthropic Legal Connectors** (W22 carry-forward): 20+ MCP-Konnektoren + 12 Practice-Area-Plugins (CoCounsel, LexisNexis, Harvey, Ironclad, DocuSign, iManage, NetDocuments, Relativity etc.).
- **Carry-forward W22-Trend:** Anthropic Legal Industry Allianz + KPMG/PwC Enterprise-Deals.

**Cosmi-Implikation:** $70 Mio. Wordsmith + $550 Mio. Legora in zwei Wochen = Legal-Tech-AI EU-Markt ist **kapitalintensiv und schon dicht**. **Eigenentwicklung Contract-Intelligence in Cosmi ist gegen zwei gut-finanzierte Spezialisten nicht konkurrenzfähig.** Integrations-Strategie ist die richtige Architekturentscheidung: Cosmi liefert Business-Kontext (Kunde, Deal-Status, Verträge), Wordsmith/Legora liefert Contract-Intelligence via API. Modul-Pfad: `backend/internal/vertraege/integration/wordsmith-adapter/`, `backend/internal/vertraege/integration/legora-adapter/`, `backend/internal/vertraege/eidas/eudi-wallet-prep/`.

---

### buchhaltung (12 Items, 3 Cluster)

**Was lief diese Woche (hoch-aktive Woche):**
- **Easybill/YouGov-Studie: 74% nicht E-Rechnungs-2027-bereit** (siehe Top-5 #4).
- **Lexware "KI in der Steuerkanzlei"** (Di, Lexware-Blog) — EU AI Act Compliance-Guide. Lexware positioniert Steuerberater als "Compliance-Multiplikatoren". Direkte Konkurrenz nutzt AI-Act-Compliance aktiv als Kaufargument.
- **Gradient Labs $26 Mio. Series A verdoppelt** (Di, Sifted) — UK/EU-AI-Finance-Startup, CommerzVentures als Lead. Signal: DACH-Finanzakteure investieren EU-vertikale AI-Finanzlösungen.
- **Finanzamt 2.0 / Jahressteuergesetz 2026** (Di, Heise) — § 29c Abgabenordnung erlaubt Finanzbehörden erstmals KI-Training mit echten Bürger-Steuerdaten (Löschfrist 1 Jahr). Zweischneide-Signal: KI-Normalisierung im Steuer-Kontext + DSGVO-Skepsis-Treiber.
- **BSI WID-SEC-2026-1544 PostgreSQL** + **WID-SEC-2026-0873 Docker** (Sa-Reg) — Updated 29.05., Patch-Status-Verifikation Prio-1 für Cosmi-Buchhaltungs-Hosting.

**Cosmi-Implikation:** Buchhaltungsmodul-Launch hängt 2026 an XRechnung+ZUGFeRD-Implementierung. Steuerberater-Channel als Distributions-Pfad gezielt aufbauen — Lexware ist bereits aktiv. Cross-Modul-Compliance-Akte (AI-Act + DSGVO) als Differenzierung vs. Buchhaltungs-Only-Konkurrenten (sevDesk, Lexware/Lexoffice, BuchhaltungsButler, easybill, DATEV).

---

### rapporte (0 substantielle Items)

**Was lief diese Woche:** Stille Woche. Keine Tier-1-Quellen aktiv. Donnerstag-Tier-2-Rotation ohne Feed-Treffer. Carry-forward: AI-Cost-Governance-Trend impliziert "Cosmi-Rapporte mit AI-Auto-Generation" als Roadmap-Kandidat (Hours-Saved-Metrik = direktes ROI-Argument).

---

### schichten (0 substantielle Items)

**Was lief diese Woche:** Stille Woche. Carry-forward W22: ArbZG-Stille (BMAS-Feed 7. Woche 404 — `sources/_regulation.yaml`-Pflege nötig). Markt ruhig — Chance für First-Mover ohne Druck.

---

### fuhrpark (0 substantielle Items)

**Was lief diese Woche:** Stille Woche. **VW kappt API für Besitzer** (Di Morning, Heise, score 0.45) als einziges sekundäres Signal — Datensouveränitäts-Warnung: Hersteller können Datenzugriff einseitig entziehen. DSGVO-Argument für Cosmi-Fuhrpark-Modul: Daten bleiben beim KMU, nicht beim Hersteller.

---

### vermietung (0 substantielle Items)

**Was lief diese Woche:** Stille Woche. Markt ruhig — Chance für First-Mover ohne Druck (carry-forward W22-Beobachtung).

---

### inventar (0 substantielle Items)

**Was lief diese Woche:** Stille Woche. Carry-forward: Odoo (`primary_modules: [crm-core, buchhaltung, einkauf, inventar, produktion]`) als architektonischer Vergleich aktiv beobachten — Open-Source-Sprint W21 hat sich nicht wiederholt.

---

### einkauf (0 substantielle Items)

**Was lief diese Woche:** Stille Woche.

---

### produktion (0 substantielle Items)

**Was lief diese Woche:** Stille Woche.

---

## "Was andere besser machen" (Pflichtsektion, min 5)
