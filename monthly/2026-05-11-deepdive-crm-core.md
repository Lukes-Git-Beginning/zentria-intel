---
year: 2026
week: 20
modul: crm-core
created: 2026-05-11
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 48
tokens_input: ~290000
tokens_output: ~9800
rotation_position: 1/15
---

# Deepdive: crm-core (Mo W20/2026)

> **Erster Deepdive der Rotation.** Modul-Liste aus `settings.yaml` `intel-monday-deepdive.rotation_modules` (15 Module). Naechstes Modul gemaess Rotation: **dialer** (KW21).

> **Stand Cosmi-CRM (2026-05-10):** Backend `internal/crm/` produktiv mit 11 Sub-Packages, 38 gRPC-Methoden, Migration 081 + 106/111 (Tenant-Retrofit) live. Pilot-Launch geplant fuer 2026-07-01.

---

## State-of-the-Art

Der CRM-Markt befindet sich Mai 2026 in einer **doppelten Disruption**: (a) Outcome-based AI-Pricing verdraengt Seat-basierte Modelle, (b) Model-Context-Protocol (MCP) wird der De-facto-Standard fuer Agent-CRM-Interaktion. Beide Veraenderungen sind innerhalb der letzten 30 Tage in den Markt geschossen.

### Top-5 Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. HubSpot (international, threat: high)**
- **Breeze Agents** produktiv: Prospecting Agent ($1/qualifizierter Lead), Customer Agent ($0.50/geloestes Gespraech). Outcome-based-Pricing seit 8. Mai 2026 offiziell — CEO Yamini Rangan: *"Customers pay when the agent works."* (Quelle: Diginomica 8. Mai).
- **Open MCP-Server live** seit Spring Spotlight 2026. Claude, ChatGPT, Gemini, Copilot koennen HubSpot-Daten direkt lesen/schreiben. API-Paritaet als oeffentliches Ziel.
- **AEO Agent** in Marketing Hub Pro/Enterprise (Mai 2026). +1.850% qualifizierte Leads aus Answer Engines (Q1/25 → Q1/26). HubSpot ist #1 bei "best CRM"-Queries in ChatGPT/Perplexity/Gemini.
- **Intelligence Layer** aus 280.000+ Kundenpatterns: Deal-Risk-Scoring, Champion-Activity-Tracking, Comparable-Deal-Pattern-Matching, Objection-Library.
- **Gap zu Cosmi:** AI-Agents, MCP-Server, Lead-Scoring, AEO-Sichtbarkeit, predictive Deal-Forecasting, Intelligence-Layer.

**2. Pipedrive (international, threat: high)**
- **Sequences** (E-Mail + Task-Cadences) produktiv. Pipedrive AI Email Writer integriert.
- **Deal Scoring** als Standardfeature: Win-Probability + Priorisierung per ML-Modell.
- **Sales Demo Software**: Engagement-Tracking integriert in CRM-Records.
- **Gap zu Cosmi:** Sequences, Deal-Scoring, AI-Email-Writer.

**3. monday.com (international, threat: high)**
- **monday AI / MyAI** durchgaengig im Sales-Pipeline integriert (AI-Drafting, AI-Summary, AI-Risk).
- **Hybrid Work-+CRM-Plattform**: Tasks/Projects/Deals teilen sich Boards — direkter Cosmi-Wettbewerber im Cross-Modul-Modell.
- Pricing-Stand DACH (lt. Cosmi PRICING.md): 10–24 EUR/User.
- **Gap zu Cosmi:** Native AI im Pipeline, Board-Cross-Modul, Mobile-App.

**4. Bexio (DACH, threat: high)**
- **Direkter DACH-Konkurrent #1** (Schweiz-Primary, DACH-Reach). CRM + Buchhaltung + Offerten integriert — der eine Vorteil, den Cosmi auch bietet.
- Keine sichtbaren AI-Agent-Announcements (Mai 2026). Bexio bleibt auf "klassischem" CRM mit starker DACH-Compliance (Schweizer Mehrwertsteuer, ESR, ZUGFeRD, eBill).
- Pricing-Stand (Cosmi-Knowledge): vergleichbar mit Pipedrive/Zoho-DACH-Range.
- **Gap zu Cosmi:** Markt-Etablierung in CH (Cosmi noch Pilot-Phase), Bank-Anbindung Schweiz, Treuhaender-Channel.
- **Cosmi-Vorteil ggue. Bexio:** Self-Hosted-Option, modulare Preismatrix ohne Tiers, EU-Datensouveraenitaet-Argument.

**5. Twenty (open-source, threat: medium — wachsend)**
- v2.0.0 (21. Apr 2026): **RFC 9728 MCP-Compliance** offiziell verankert. v2.1.1 (30. Apr): AI-Credit-Cap an Entry-Points chirurgisch eingebaut (siehe weekly W19 i12). v2.3.2 heute (11. Mai 2026): aktive Iteration, ~2 Releases/Tag in Spitzen.
- **Architektonisch sehr modern** (Postgres-First, GraphQL, MCP-Native, App-Store via npm).
- **15k+ GitHub-Stars**, rapide wachsend. Direkt-Konkurrent fuer "Cosmi als modernes Self-Hosted-CRM"-Positionierung.
- **Gap zu Cosmi:** MCP-Native-Architektur (v2.0 PKCE+RFC9728), Credit-Metering-Pattern, npm-App-Store, Page-Layout-SDK fuer Custom-Views.

### Erweiterte Lage — neu im Markt seit KW16

- **Intercom Fin for Sales** ($10/qualified Lead, $1/Disqualifizierung): Kunde definiert selbst "qualifizierter Lead" — kein Vendor-Definition. Direkter Blueprint fuer Cosmi-AI-Billing.
- **Zendesk Advanced AI in alle Plans** (Rollout heute, 11. Mai). Markt-Baseline-Shift: AI-Triage ist nicht mehr Premium, sondern Standard. Relevanz fuer Helpdesk-, aber semantischer Spillover ins CRM (Conversation-zu-Deal-Routing).
- **Elyos AI $13M Series A** (UK, 6. Mai). AI-Agents fuer europaeische Handwerksbetriebe. **Direkter Cosmi-Zielmarkt**. Wenn Elyos DACH-Expansion macht, ist Cosmi "Handwerks-CRM"-Story angreifbar.

### Sentiment-Signal

"Local AI needs to be the norm" (HN 727 Punkte, 9. Mai 2026): Privacy-by-Architecture-Sentiment im Aufwind. Verstaerkt Cosmi-USP "Self-Hosted/EU-Cloud" — **wenn** Cosmi auch On-Device-AI anbietet. Heute: nein.

---

## Cosmi-IST-Stand

### Backend `internal/crm/` (Stand Pilot-Vorbereitung)

11 Sub-Packages, 38 gRPC-Methoden:

| Package | Was es liefert |
|---|---|
| `contact` | CRUD, FindDuplicates (trigram+email+phone), MergeContacts, CSV/vCard Import+Export, Visibility-Scoping (shared/personal/owner), Batch-Enrichment |
| `company` | CRUD, AddTags/RemoveTags, GetCompanyContacts, Domain-Duplikat-Detection |
| `deal` | CRUD, MoveToStage, Multi-Currency (16 ISO-Codes inkl. CHF), Probability-Weighted Forecasting (statisch aus Pipeline-Stage), Event-Emitter fuer Stage-Changes |
| `pipelinestage` | CRUD, Won/Lost-Terminal-States, Reorder, Probability-Weight pro Stage |
| `activity` | CRUD, Complete/Uncomplete, AddTags, GetContactTimeline, CustomFields, Postgres-NOTIFY-Events |
| `report` | GetPipelineReport, GetConversionReport, GetActivityReport (Cycle-Time, Stage-Transitions) |
| `customfield` | Per-Entity-Type Custom-Fields (select/multiselect/text/number/date) |
| `savedfilter` | JSON-Filter pro User/Entity-Type, Default-Flag |
| `search` | Cross-Entity FTS (Contacts, Companies, Deals, Activities) mit Fair-Distribution-Limits |
| `tag` | Polymorphes Tagging mit Hex-Color, lazy-loaded |
| `consent` | DSGVO Art. 5/6/17: GrantConsent, RevokeConsent, ConsentHistory, RequestDeletion, ProcessDeletion + IP-Capture-Audit-Trail |

Automation-Aktionen: `crm.update_deal_field`, `crm.create_contact` (2 Stueck).

### Knowledge-Layer

- `.knowledge/architektur.md`: CRM-Service Port :50052, Routes `route_crm.go` + 5 Sub-Files, Gateway-Proxy-Pattern eingehalten.
- `.knowledge/datenbank.md`: Migrations 000045+059 (Basistabellen) + 000106 (Tenant-Retrofit, 20 Tabellen) + 000111 (12 CRM-Aux tenant_id-Spalten + Indizes auf Tag/Consent).
- Coverage CRM-Sub-Packages: pipelinestage hat `cached_repository_test.go`, deal hat `event_emitter`, alle Packages haben Service-Tests.

### Stand der Konkurrenz-Vergleichs-Achsen

**Vorhanden:**
- Solides klassisches Sales-CRM-Fundament (Contact/Company/Deal/Activity, Pipeline, Tags, Custom Fields, Saved Filters, FTS-Search).
- DSGVO-First (Consent-Audit + Erasure-Flow).
- Multi-Tenant-Hardening (Sweep Welle 3 + 4B, 2026-04).
- Reporting (3 Reports: Pipeline, Conversion, Activity).
- Probability-Weighted-Forecasting (statisch).

**Fehlend:**
1. **AI-Layer komplett** — kein Lead-Scoring, keine Deal-Risk-Prediction, kein AI-Email-Drafting, keine Conversation-Intelligence.
2. **MCP-Server / Agent-Endpoint** — Konkurrenten (HubSpot, Twenty) haben dies bereits. Cosmi-MCP-Strategie ist nicht formalisiert (siehe Weekly W19 i02).
3. **Sequences / Cadences** — Pipedrive-Kernfeature seit Jahren, Cosmi: 0 Code.
4. **Email-Workflow im CRM** — Automation hat `email_actions.go`, aber nicht in CRM-Pipeline-Kontext integriert.
5. **Web-to-CRM Lead-Capture** — kein Form-zu-Contact-Auto-Mapping (Cosmi hat `formulare`-Modul, aber Lead-Capture-Bruecke ist nicht spezifiziert).
6. **Mobile-App** — Backend-only.
7. **Predictive Forecasting** — Probability ist statisch aus Pipeline-Stage, nicht ML.
8. **AEO-Sichtbarkeit** — Cosmi ist in AI-Suchmaschinen-Rankings nicht praesent.
9. **Outcome-Billing-Infrastruktur** — `backend/internal/billing/ai-credits/` existiert nicht.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | HubSpot | Pipedrive | monday.com | Bexio | Twenty |
|---|---|---|---|---|---|---|
| Pipeline-Mgmt (Stages, Deals, Drag&Drop) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Probability-Weighted Forecasting (statisch) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI-Deal-Forecasting / Risk-Score | ❌ | ✅ Breeze | ✅ Deal-Scoring | ✅ MyAI | ❌ | 🚧 v2.x AI |
| Lead-Scoring (Fit + Engagement) | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| AI-Email-Drafting | ❌ | ✅ Breeze | ✅ AI Writer | ✅ MyAI | ❌ | ✅ v1.22 |
| Email-Sequences / Cadences | ❌ | ✅ | ✅ | ✅ | ❌ | 🚧 Workflows |
| Conversation-Intelligence (Calls) | ❌ (separat dialer) | ✅ | ✅ Add-on | ❌ | ❌ | ❌ |
| Open MCP-Server | ❌ | ✅ Spring 2026 | ❌ | ❌ | ❌ | ✅ v2.0 RFC9728 |
| Outcome-based AI-Pricing | ❌ | ✅ $0.50/conv, $1/lead | ❌ | ❌ | ❌ | ✅ Credit-Cap v2.1 |
| Lead-Capture (Web-Form → CRM) | 🚧 (formulare-Modul, keine Bruecke) | ✅ | ✅ | ✅ | ✅ | 🚧 |
| Custom Fields | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Duplicate-Detection + Merge | ✅ (trigram+email+phone) | ✅ | ✅ | 🚧 | ✅ | 🚧 |
| GDPR Consent + Erasure | ✅ (Vorbild) | ✅ | ✅ | ✅ | ✅ DACH-spezifisch | 🚧 |
| Tenant-Isolation Hard-Mode | ✅ (Welle 4B) | n/a | n/a | n/a | n/a | ✅ |
| Self-Hosted Option | ✅ ORBIT | ❌ | ❌ | ❌ | ❌ | ✅ |
| DACH-Compliance (CHF, ZUGFeRD, GoBD) | ✅ (CHF in deal, GoBD Sprint 3) | 🚧 | ❌ | 🚧 | ✅ (USP) | ❌ |
| Mobile App | ❌ | ✅ | ✅ | ✅ | ✅ | 🚧 |
| Modulare Preismatrix (kein Tier) | ✅ (USP) | ❌ | ❌ | ❌ | ❌ | n/a (OSS) |
| Plugin-Marketplace / App-Store | 🚧 (WASM-Plan, Phase D) | ✅ 2.000+ Apps | ✅ | ✅ | 🚧 | ✅ npm-basiert |
| AEO-Sichtbarkeit (AI-Suche) | ❌ | ✅ #1 | 🚧 | 🚧 | ❌ | ❌ |

> Legende: ✅ produktiv · 🚧 angekuendigt/teilweise · ❌ fehlt · n/a nicht zutreffend

---

## Cosmi-Schwachpunkte (Priorisierung)

**Strukturelle Schwachstellen (Bedrohungsklasse A — Markt-Baseline):**
1. **Keine AI-Layer im CRM.** Stand 11. Mai 2026 ist AI in CRM bei HubSpot/Pipedrive/monday/Twenty Marktbaseline, nicht Premium. Cosmi geht ohne AI-Feature in den Pilot (1. Juli 2026). Kundenseitige Erwartung: AI-Email-Draft beim Compose, AI-Risk-Badge auf Deal-Card, AI-Next-Action-Suggestion. Diese drei Touchpoints sind das Minimum.
2. **Kein MCP-Endpoint.** Wenn HubSpot Spring 2026 zur Plattform wird, auf der Agents laufen, dann werden Customer-Workflows ueber HubSpot-MCP geroutet. Cosmi verliert in jedem solchen Workflow den Datenkontakt. Loesung: `backend/internal/crm/mcp/` mit Read-Only-Endpoint (List/Search/Get-Deals/Contacts) als MVP.
3. **Kein Lead-Scoring / Lead-Capture-Bruecke.** Cosmi hat `formulare` und `crm`, aber keine Bruecke. KMU-Nutzer erwartet: Website-Formular → CRM-Contact + Initial-Score + Pipeline-Eintritt mit Auto-Assignment.

**Strategische Schwachstellen (Bedrohungsklasse B — Differenzierung):**
4. **AEO-Unsichtbarkeit.** Cosmi hat keinen Eintrag in ChatGPT/Perplexity bei "DACH CRM Self-Hosted KMU"-Queries. HubSpots Methode (15+ Artikel in 10 Tagen + Schema-Markup) ist reproduzierbar mit deutlich kleinerem Aufwand fuer DACH-Nischenqueries.
5. **Outcome-Pricing-Infrastruktur fehlt.** Wenn Cosmi AI-Features released, ist Pauschal-Aufpreis bereits Markt-out. Architektur-Anforderung: Credit-Metering pro AI-Aktion, Customer-Definable-Thresholds (Intercom-Pattern).

**Operative Schwachstellen (Bedrohungsklasse C — Polish):**
6. **Reporting flach.** 3 Reports (Pipeline/Conversion/Activity) sind solide MVP, aber kein Revenue-Intelligence-Layer (Cohort, ARR, Churn-Prediction).
7. **Probability statisch.** `pipelinestage.probability` ist menschlich gesetzt, nicht ML-getrieben. HubSpot/Pipedrive lernen pro Customer.
8. **Conversation-zu-Deal-Routing fehlt.** Dialer und CRM sind getrennt — kein Call-zu-Deal-Auto-Logging mit Transcript-Search.

---

## Top-3 Strategische Empfehlungen

### 1. **MCP Read-Only-Server fuer CRM JETZT** (Sprint 4, Pilot-Vorlauf)

**Warum:** HubSpot/Twenty sind bereits MCP-served. Wenn DACH-KMU im Sommer 2026 Claude/ChatGPT mit CRM verbindet, ist Cosmi unsichtbar oder verliert Dateneck-Workflows. **Cosmi-USP "EU-Datensouveraenitaet" verlangt eigenen MCP-Server** — sonst verlaesst die Anfrage Cosmi.

**Scope:** `backend/internal/crm/mcp/` — Server mit 6 Tools (list_contacts, list_deals, get_deal, search_crm, get_pipeline_report, list_activities). Read-Only fuer Phase 1. PKCE-Auth (RFC 9728), Tenant-Isolation enforced via existing `middleware.GetTenantID(ctx)`. Twenty v2.0 als Referenz-Implementierung (open-source).

**Aufwand:** 5–7d (1 Backend-Engineer). Architektur-Lessons aus Twenty v1.22 (SSE streaming on POST) verwendbar.

**Wirkung:** Pilot-Kunden koennen Cosmi an Claude/ChatGPT haengen ohne Datenexport — direkt vermarktbar als "Self-Hosted MCP-CRM, EU-only".

### 2. **AI-Credits-Infrastruktur VOR ersten AI-Features** (Sprint 4)

**Warum:** Outcome-Pricing ist Marktkonvergenz (HubSpot 8. Mai, Intercom 7. Mai, Twenty v2.1.1 30. Apr, Notion 4. Mai, Zendesk 11. Mai — 5 unabhaengige Datenpunkte in 11 Tagen). Wenn Cosmi AI-Features released **ohne** Credit-System, wird sofort nachgebaut werden muessen, mit hohen Migration-Kosten. Heute: Schreib-Tisch, leer. In 6 Monaten: 3 AI-Features live mit Pauschal-Aufpreis und Pricing-Strafe.

**Scope:** `backend/internal/billing/ai-credits/` mit Schema (`tenant_ai_credit_pool`, `ai_credit_transaction`), Metering-Middleware (jede AI-RPC-Call decrementiert Pool), Threshold-Config pro Tenant (Customer-Definable, Intercom-Pattern), Discord-Webhook bei Pool-Low. Twenty v2.1.1 als Code-Referenz (`AI Credit-Cap an Entry-Points`).

**Aufwand:** 4–6d (1 Backend-Engineer + DB-Migration). Keine UI-Pflicht in Phase 1 (Admin-API + Telemetrie reichen).

**Wirkung:** Cosmi kann AI-Features als "1 Credit / Lead-Score-Berechnung" oder "5 Credits / AI-Email-Draft" launchen, Customer-Definable. Bessere Story als HubSpot-Outcome-Pricing (weil Self-Hosted-Variant ggf. kostenlos via On-Device-LLM).

### 3. **AEO-Content-Welle DACH-KMU-Queries** (Marketing, parallel)

**Warum:** HubSpot belegt #1-Position bei "best CRM"-Queries in AI-Suche. Bei "CRM Handwerk DACH Self-Hosted" oder "DSGVO-konformes CRM KMU Schweiz" oder "modulares CRM DACH ohne Tier" ist die Konkurrenz **markant duenner**. AEO ist hier Tor mit niedrigem Schwellwert. Wenn Cosmi nicht im Sommer 2026 startet, ist die Tuer in 12 Monaten zu (HubSpot-Pattern reproduzierbar fuer Nische).

**Scope:** 10–15 Artikel auf zentria.tech-Blog in 4 Wochen, alle mit:
- DACH-spezifische Long-Tail-Queries (Handwerk, Treuhaender, GmbH-Verwaltung, Schweizer KMU, GoBD-Konformitaet)
- Schema-Markup (Article + Product + FAQ)
- Klare AI-Crawler-Signals (canonical URLs, structured data, sitemaps)
- Echte Cosmi-Feature-Bezuege (kein Generic-Content)

**Aufwand:** 1 Content-Person + 1 Tech-SEO-Audit. Trackbar via AEO-Visibility-Tools (z.B. AthenaHQ, Profound).

**Wirkung:** Erste qualifizierte Pilot-Leads aus Answer-Engines wahrscheinlich Q3 2026. Strukturelle Sichtbarkeit baut sich exponentiell auf — fruehes Investment hat 12-Monats-Hebel.

---

## Quellen (Top-Quellen die diesen Bericht stuetzen)

**Cosmi-IST-Stand:**
- `/opt/kmuhub/.knowledge/architektur.md` (Service-Liste + CRM-Routes)
- `/opt/kmuhub/.knowledge/datenbank.md` (Migrations 045/059/106/111)
- `/opt/kmuhub/backend/internal/crm/{deal,contact,company,activity,...}/service.go`
- `/opt/kmuhub/backend/internal/automation/action/crm_actions.go`
- `/opt/kmuhub/docs/MODULES_SCOPE_MATRIX.md` + `docs/ROADMAP.md` + `docs/PRICING.md`

**Konkurrenz / Markt:**
- HubSpot Open Ecosystem Vision: https://blog.hubspot.com/marketing/our-vision-for-building-an-open-ecosystem-for-the-agent-era (04.05.2026, gefetcht)
- HubSpot CEO Outcome-Pricing: https://diginomica.com/customers-pay-when-agent-works-how-hubspot-ceo-yamini-plans-remove-every-blocker-ai-adoption (08.05.2026)
- Intercom Fin for Sales: https://www.intercom.com/blog/building-outcome-based-pricing-for-fin-for-sales/ (07.05.2026)
- Twenty Releases v2.0 / v2.1.1 / v2.3.2: https://github.com/twentyhq/twenty/releases (gefetcht, RFC 9728 MCP + Credit-Cap)
- Pipedrive Blog: https://www.pipedrive.com/en/blog (Sequences, Deal-Scoring, AI Email Writer)
- Zendesk Advanced AI Rollout: support.zendesk.com Article 10487730059034 (11.05.2026 Stichtag)
- Elyos AI $13M: sifted.eu (06.05.2026)
- "Local AI needs to be the norm": HN 727 Punkte (09.05.2026)

**Interne Aggregations-Berichte (zentria-intel):**
- `daily/2026-05-07-evening.md` (HubSpot Ecosystem-Vision, AEO-Strategie, Open-MCP)
- `daily/2026-05-08-evening.md` (HubSpot Marketing Hub AEO, LiveKit Sub-Sekunden-Latenz)
- `daily/2026-05-09-regulation.md` (EDPB DPIA-Template, AI-Act EDPS Compass)
- `daily/2026-05-11-morning.md` (Outcome-Pricing-Konvergenz, Elyos AI)
- `weekly/2026-W19.md` (HubSpot Open Ecosystem + Twenty AI-Credit-Cap, Cross-Module-Konvergenz)

---

## Picks (vorgeschlagen)

[ ] 🟢 **MCP Read-Only-Server fuer CRM** — Sprint-4-Aufnahme zwingend. Architektur-Spec + Twenty-Referenz-Read in 1d. Aufwand 5–7d Code. **Bedrohungsklasse A.**

[ ] 🟢 **`backend/internal/billing/ai-credits/`-Infrastruktur** — VOR erstem AI-Feature. Sprint 4. Twenty v2.1.1 als Code-Vorbild. **Bedrohungsklasse A.**

[ ] 🟡 **AEO-Content-Welle DACH-Nischen-Queries** — Marketing-Hebel. Erste 5 Artikel als Pilot in 2 Wochen, dann Visibility-Tracking. **Bedrohungsklasse B.**

[ ] 🟡 **Lead-Capture-Bruecke `formulare` → `crm`** — Spec + 1 Sprint Code. Forms-Submission triggert `crm.create_contact` + optional Initial-Stage-Move via Automation. **Bedrohungsklasse A (Markt-Erwartung).**

[ ] 🟡 **AI-Email-Drafting im Compose** — Erster konkreter AI-Touchpoint. Outcome: Credit-gemetert, On-Device-LLM-Fallback. Folge-Sprint nach Credits-Infra. → followup 30d.

[ ] 🟠 **ML-basiertes Deal-Probability-Modell** — ersetzt statische `pipelinestage.probability`. Setzt voraus, dass genug Deal-History pro Tenant existiert (also: post-Launch, fruehestens Q4 2026). → followup 90d.

[ ] 🟠 **Conversation-zu-Deal-Auto-Logging** (dialer ↔ crm-bridge) — kein Pilot-Blocker, aber Differenzierungs-Hebel ggue. monday/Bexio. → followup 60d.

[ ] 🔵 **Elyos-AI-Monitoring** — Pruefung in 30d ob DACH-Expansion oeffentlich angekuendigt. Wenn ja: Cosmi-Handwerks-Pitch-Refresh. → followup 30d.

[ ] 🔵 **HubSpot Breeze-Outcome-Pricing-Marktreaktion** — beobachten ob Bexio/weclapp/Pipedrive nachziehen. Wenn HubSpot solo bleibt: Cosmi kann differenzieren mit Seat-Modell. → followup 60d.

---

## Telemetrie

- **Routine:** intel-monday-deepdive
- **Modul:** crm-core (1/15 Rotation, erste Iteration)
- **Quellen gepollt:** 11 Konkurrenz-Feeds (crm-core.yaml) + 12 interne Wissens-Dateien + 4 Live-Webfetches (HubSpot, Pipedrive-Blog, Twenty-Releases, monday-Blog, Bexio-Blog)
- **Konkurrenz-Datenpunkte:** HubSpot 6, Twenty 6, Pipedrive 5, monday 2, Bexio 0 (Blog nicht informativ), Elyos 1, Intercom 3, Zendesk 1
- **G2/Capterra-Reviews:** ❌ uebersprungen (Headless-Chromium nicht im Run-Scope, G2 blockt Bot-Scrapes ohne JS)
- **Naechstes Modul gemaess Rotation:** **dialer** (KW21, Mo 18.05.2026)
- **State-File:** `.state/deepdive_rotation.json` aktualisiert

---

*Generiert: 2026-05-11 — Erster Deepdive der Rotation. Modul-Liste 15 (settings.yaml), naechste Iteration desselben Moduls fruehestens KW34/2026 (24.08.2026).*
