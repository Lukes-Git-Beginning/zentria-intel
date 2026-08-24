---
year: 2026
week: 35
modul: crm-core
created: 2026-08-24
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 54
tokens_input: ~340000
tokens_output: ~11500
rotation_position: 1/15
zyklus: 2
delta_to: 2026-05-11-deepdive-crm-core.md
---

# Deepdive: crm-core (Mo W35/2026) — Zyklus 2

> **Zyklus 2, Modul 1/15.** Erster Deepdive der zweiten Rotation. Referenz-Vergleich: `monthly/2026-05-11-deepdive-crm-core.md` (Zyklus 1, W20). **Delta-Zeitraum: 15 Wochen (2026-05-11 → 2026-08-24).**
>
> **Stand Cosmi-CRM (2026-08-24):** Backend `internal/crm/` produktiv mit **12 Sub-Packages** (+1 `advisoryprotocol` seit W20), 4.177 Zeilen Service-Code, Migration-Head **297** (Prod-Kopf nach Backend-Nachtlauf 5, 2026-08-06). RLS in Production seit Welle 3.5 (2026-04-29) + Welle 4 (2026-08-03, 20 Tabellen). Pilot-Launch war fuer 2026-07-01 geplant — Status heute nicht dokumentiert im Knowledge-Vault.

---

## Executive Delta (W20 → W35)

**Der Markt ist in 15 Wochen von "AI-Baseline im CRM" zu "Multi-Agent-Orchestrierung + MCP-Ecosystem als Distribution" gesprungen.**

| Achse | Stand W20 (2026-05-11) | Stand W35 (2026-08-24) | Cosmi-Delta |
|---|---|---|---|
| AI-Layer in CRM | HubSpot Breeze/Twenty v2.0 Vorreiter | **Marktbaseline** — Salesforce Agentforce +205% ARR YoY (W33), HubSpot Agent Hub GA-Beta (23.07.), Twenty `/chat` GA (v2.31) | ❌ 0 AI-Features in `internal/crm/`. `internal/llm/` existiert (`client.go` 183 LoC), **nicht gewired** |
| MCP-Server | HubSpot Spring-Preview + Twenty v2.0 RFC 9728 | **Linux Foundation AAIF Governance**, 97M+ Installs, HubSpot GA (April), Salesforce Tableau MCP (Summer '26), Google SAM OSS (18.08.) | ❌ 0 MCP-Endpoints. W33/W34/W35 dritte, vierte, fuenfte Woche ohne Architektur-Entscheid |
| Outcome-Pricing | HubSpot 8.05. offiziell, Intercom Fin, Twenty v2.1.1 Credit-Cap | **HubSpot Credits GA** ($0.50/res, $1/lead), Rillet $100M Series C mit AI-nativer Pricing-Story | ❌ 0 Credit-Metering. `internal/billing/ai-credits/` existiert nicht |
| Multi-Agent | Nicht sichtbar | **HubSpot Agent Builder Public Beta** (Multi-Agent-Kontext-Framing), **Salesforce Agentforce Multi-Agent Orchestration** (Summer '26), Twenty Multi-Turn-SDK v2.29 | ❌ Kein Agent-Framework. Cross-Modul-Kontext-Moat strukturell vorhanden, aber ohne Kontext-API nicht kommunizierbar |
| Cosmi-USP (Cross-Modul-Kontext) | Implizit | **Aktiv angegriffen** — HubSpot Agent Hub bindet Marketing+Sales+Service ueber Shared-Context, Salesforce Agentforce vernetzt Domain-Packs | 🚧 W34-Top-5-Empfehlung: `backend/internal/ai/context-api/` als P0-Fundament — noch nicht angelegt |
| CRM-Modul-Fortschritt | 11 Sub-Packages, Migr. 111 | 12 Sub-Packages (+advisoryprotocol/Beratungsprotokoll ZFA), Migr. **297**, RLS live | ✅ Klassisches CRM-Fundament ist gewachsen, DSGVO-Layer robuster (RLS Foundation + Welle 4) |

**Bottom line:** Cosmi hat die 15 Wochen fuer Backend-Hardening (RLS, Tenant-Isolation, Migrations-Volumen) und Feature-Vertiefung (Beratungsprotokoll ZFA) genutzt. **Alle drei W20-Top-3-Empfehlungen sind offen** — MCP-Server, ai-credits-Infrastruktur, AEO-Content-Welle. Der Konkurrenz-Abstand hat sich strukturell vergroessert: nicht in Standard-CRM-Features (dort ist Cosmi solide), sondern in der **Agent-Era-Distribution-Schicht**.

---

## State-of-the-Art (Update W35)

### Top-6 Konkurrenten — Was sie heute haben, was Cosmi nicht hat

**1. HubSpot (international, threat: HIGH — verschaerft seit W20)**
- **Agent Hub + Agent Builder Public Beta** live seit **23.07.2026** (heute 4 Wochen alt): No-Code-Canvas fuer Multi-Agent-Konfiguration, Shared-Context ueber CRM-Objekte, Outcome-Pricing pro Aktion (HubSpot Credits). CPO Duncan Lennox positioniert Multi-Agent-Fragmentierung als aktive Kritik gegen Einzel-Agent-Ansaetze. **GA-Erwartung Q1 2027** — Third-Party-Agents dann offen.
- **HubSpot MCP-Server GA** seit April 2026 unter `mcp.hubspot.com` + One-Click-Claude-Connector. Developer-Platform fuer custom MCP-Servers geoffnet.
- **HubSpot Credits** (Outcome-Pricing) live: $0.50/Resolution, $1/qualifizierter Lead. Credits in Pro/Enterprise-Abo enthalten, Toppup verfuegbar. Beschaffungs-Erwartung im Mid-Market Standard.
- **CRM-API-Write-Validation Enforcement** ab API-Version 2026-09 (Breaking Change 11.08.): Admin-konfigurierte Validation-Rules auf Create/Update enforced. Cosmi-Custom-Field-Validation-Layer sollte diesem Muster folgen.
- **AEO-Offensive kontinuierlich**: 5-Artikel-Woche (19.08.), Vertikal-Guides (Insurance nach Healthcare + Real Estate), AEO-Tool $45/Monat CRM-nativ (vs. Profound $82.50/Monat). SAIV/Citation-Rate als Standard-Metriken.
- **Gap zu Cosmi:** Agent-Framework, MCP-Server GA, Outcome-Credits, AEO-Sichtbarkeit + Tooling, Vertikal-Content.

**2. Salesforce (international, threat: HIGH — Agentic Enterprise Realization)**
- **Summer '26 Release** (Mitte Juni Prod-Rollout): **Agentforce Multi-Agent Orchestration** (Agenten arbeiten als Team mit Shared-Context ueber Kanaele), **Agentforce Self-Service** (Help-Agent-Setup in 6 Klicks), **Agentforce Voice** (Voice-Kanal auf jeder digitalen Front-Door), **Tableau MCP** (AI-Agents querien Tableau-Analytics direkt), **50+ IT-Service-Domain-Agents** in Slack/Teams out-of-box.
- **Agentforce Deployments +2x YoY** (Feb 2025 → Apr 2026, W34-Bestaetigung). $1.2B ARR (+205% YoY, W33-Datenpunkt).
- **Salesforce-Aktie -33% YTD 2026** trotz Agentic-Zahlen — Marktzweifel am Consumption-Pricing-Modell. Signal fuer Cosmi: Outcome-Story ist besser verkaufbar als Consumption.
- **Salesforce kauft Contentful** (W23-Keeper `direct-competitor-triple-pivot` Update): Berliner Standort → US CLOUD Act. **Direkte Verstaerkung der Cosmi-EU-Souveraenitaets-Story.**
- **Gap zu Cosmi:** Multi-Agent-Orchestration, MCP-Ecosystem (Tableau), Voice-Kanal, Domain-Agent-Packs, Enterprise-Reichweite.

**3. Twenty (open-source, threat: HIGH — beschleunigt seit W20 auf Sprint-Verdichtung)**
- **Release-Kadenz eskaliert:** W33 = 4 Releases in 47h, W34 = 4 Releases in 4 Werktagen, W35-Kickoff v2.33 + v2.34 (24.08.) in <24h. v2.20 → v2.34 in 15 Wochen — **kumulierte Feature-Erweiterung uebertrifft Cosmi-Roadmap-Delta.**
- **`/chat` GA** (v2.31.0, 12.08.): Konversationelles CRM-Interface mit Side-Panel-Artifacts (Datensaetze inline). **UX-Paradigmenwechsel** von "CRM-Tool mit Tabs" zu "AI-Arbeitspartner mit konversationellem Zugriff".
- **ORM v2** (v2.31.5, W34): Relation-keyed WHERE-Clauses via EXISTS-Subqueries — technisches Fundament fuer LLM-generierte Queries. `findAndCount` fuer ORM v2 in v2.31.6.
- **Multi-Turn-Agent-Support** in SDK v2.29 (11.08.): messages-Array fuer Multi-Turn-Konversationen, Recording-Widget-Typen, Role-Management-Tools fuer AI.
- **Stripe-Billing in Production-Debugging** (v2.32.1, 21.08. Fix fuer Credit-Upgrade-Blockade). Twenty hat **echte zahlende Kunden**.
- **i18n** (v2.33.0, 24.08.): Multi-Language-Support baut sich auf — DACH-Markt-Signal.
- **Gap zu Cosmi:** `/chat`-UI, ORM v2 mit Relation-EXISTS, Multi-Turn-Agent-SDK, Stripe-Billing-Layer, App-Store, Webhook-Tool-Providers.

**4. Pipedrive (international, threat: medium-high)**
- **Sequences GA** ("Smarter lead nurturing with Sequences in Pipedrive" Blog-Titel, 2026): E-Mail + Task-Cadences reifer.
- **Deal-Scoring** ("Smarter deal scoring in Pipedrive") — Win-Probability + Priorisierung als Standard-Feature aktiv beworben.
- **MCP-Server** (W22-Ankuendigung, W33-carry-forward).
- **Lead-Capture-Fokus** ("Lead capture strategies that fill your pipeline in 2026") — thematisch aktuell.
- **Anhaltendes Feed-Problem:** Pipedrive-RSS-Feed 408 seit mehreren Wochen (Morning-Poll W35). Blog-URL erreichbar. Feed-Wechsel noetig fuer kontinuierliche Observation.
- **Gap zu Cosmi:** Sequences, ML-Deal-Scoring, AI-Email-Writer, MCP-Server, Lead-Capture-Framework.

**5. Bexio (DACH, threat: HIGH — DACH-Direkt-Konkurrent, aber ohne AI-Sprung)**
- **Preiserhoehung 20%** (Starter → Advanced ab Maerz 2026, CHF 35 → CHF 42): Monetarisierungs-Druck auf Bestandskunden. **Direkte Cosmi-Vertriebs-Chance** fuer Preis-sensible Schweizer KMU.
- **AI-Investitionen im Peripherie-Bereich**: Automated Transaction Matching, intelligent Invoice Recognition, Predictive Cash Flow. **Nicht AI-first entwickelt** (Marktbeobachter-Zitat, siehe Quellen). Keine AI-Agent-Story.
- **Feed dauerhaft tot** (persistent seit 2026-07-01, jetzt Woche 8): de-DE + de-CH beide 403/404 in Morning-Polls. **Bexio-Wettbewerbsanalyse strukturell blind** — externe Content-Alternative (Bexio LinkedIn, Press-Releases) muss KW35 aktiviert werden.
- **DACH-Compliance-Alleinstellung** (Schweizer MwSt, ESR, eBill, ZUGFeRD) bleibt.
- **Gap zu Cosmi:** Markt-Etablierung in CH (Cosmi noch Pre-Launch), Treuhaender-Channel.
- **Cosmi-Vorteil ggue. Bexio:** Modulare Preismatrix ohne Tier, Self-Hosted-Option (ORBIT), EU-Datensouveraenitaet, breiterer Modul-Umfang (14 Module vs. Bexio-Kern).

**6. Rillet (angrenzend, threat: emerging — Buchhaltung, aber CRM-relevant durch Data-Extraction-Story)**
- **$100M Series C, $1B Valuation** (W34 Top-5 #1). 600+ Enterprise-Kunden, ARR in 3 Monaten verdoppelt, EY-Allianz.
- **"AI-nativer General Ledger"** positioniert als **"Operating System for Finance"** — extrahiert Finanzdaten automatisch aus Salesforce, Brex und Company-Stack.
- **Relevanz fuer CRM:** Rillet lebt vom CRM-Datenzugriff (Salesforce-Extraction). Wenn Cosmi keinen MCP-Server hat, wird Cosmi-CRM-Daten von Rillet-Analogen (die im Buchhaltungs-Markt entstehen) nicht integrierbar. **Signal-Wert:** AI-native Vendors setzen CRM-Datenzugriff als selbstverstaendlich voraus.

### Erweiterte Lage — Was neu im Markt seit W20 ist

- **MCP-Ecosystem-Standardisierung**: **Linux Foundation Agentic AI Foundation (AAIF)** hat MCP-Governance uebernommen (2026). **97M+ MCP-Installs** (Maerz 2026). **A2A-Protokoll (Agent-to-Agent) Q3-Roadmap**. MCP ist **kein optionaler Standard mehr**, sondern die Ecosystem-Baseline.
- **Google SAM (Sovereign Agent Mesh)** OSS Apache-2.0 (18.08.2026): Zero-Config, Zero-Trust P2P-Overlay fuer Agent-MCP-Discovery ueber Cloud, On-Prem, Laptop, Edge — ohne interne Endpoints exponieren zu muessen. OIDC → Biscuit-Datalog-Facts. **Default-Deny absolut.** Nicht offiziell von Google supportet, aber technisch die erste produktive Antwort auf die "MCP + Enterprise Security"-Frage.
- **Intercom Fin als Open-Agent-Plattform**: Laeuft als Service-Agent auf HubSpot + Freshworks ohne Migration (W33/W34/W35 Kontinuitaet). 76% Resolution-Rate ueber Voice/E-Mail/Chat/Social. **Anti-Lock-in als Brand-Claim.** Fuer Cosmi's Cross-Modul-Kontext-Moat gilt: der Moat funktioniert nur solange Cosmi-Daten nicht via MCP durch Fin erreichbar sind — und dann verliert Cosmi den Dateneck-Workflow.
- **Domyn "few quarters away from $1B ARR"** (W34, Sifted Paywall, W35-Follow-up offen): Europaeisches B2B-SaaS im CRM/Business-Ops-Space. DACH-KMU-Markt kann signifikante Player erzeugen — Cosmi ist nicht der einzige regionale Kandidat.
- **HubSpot Pipelines API V1 Sunset** (04.12.2026, angekuendigt 14.08.): Beispiel fuer HubSpot-Deprecation-Cadence. Cosmi-Integrations-Adapter muessen periodisch nachziehen — dokumentiertes Kompatibilitaets-Fenster ist Sales-Argument.
- **CADA (EU) + Anthropic Fable-5/Mythos-5 Kill-Switch** (W23/W25-Keeper): EU-Souveraenitaets-Story hat Rueckenwind, Multi-Provider-Imperativ fuer Cosmi-AI-Layer bleibt technischer Nord-Stern.

### Sentiment-Signal (Delta)

- **"Local AI needs to be the norm"** (W20-Signal HN 727 Punkte) hat sich in **10+ Datenpunkten** in 15 Wochen materialisiert (CADA, ENISA, Sovereign-Cloud-Push). Cosmi-USP "Self-Hosted / EU-Cloud" ist strukturell aufgewertet — **wenn Cosmi On-Device- oder EU-Hosted-LLM anbietet**. Heute: `internal/llm/client.go` ist Ollama-default konfigurierbar, aber nicht produktiv gewired.
- **"AI-Kosten-Explosion"** (W23-Keeper Uber/Microsoft/Walmart): "Unlimited AI"-Phase abgeschlossen. Outcome-Pricing wird Beschaffungs-Pflicht. **Cosmi-Pricing-Klarheit** ("Predictably affordable, kein Token-Lottery") muss VOR erstem AI-Feature stehen.

---

## Cosmi-IST-Stand (Delta zu W20)

### Backend `internal/crm/` — Was seit W20 dazu kam

**Neu:**
- **`advisoryprotocol/`** (Sub-Package 12, seit ~2026-06-10, Migration 137/138): Beratungsprotokoll ZFA — CRUD nur im Draft (410 nach Finalisierung), `POST /hand-over` setzt immutable (idempotent), PDF-Endpoint 501 (FE nutzt `window.print()`). RBAC `advisory-protocols:{read,write,delete}`. Route: `route_crm_advisory.go` mit separater Registrierung via `crmRoutes.RegisterAdvisoryRoutes(r, …)` nach dem Registrar-Loop in `main.go`.
- **RLS-Foundation live** (Migration 118 + 119, Welle 3.5 done 2026-04-29): `current_tenant_id/user_id/role`, `is_system_context`, `enable_tenant_rls()` Procedure. Repository-Tenant-Filter-Sweep auf `deal/activity/task/pipelinestage/chat-message/recording` mit `WHERE id=$1 AND tenant_id=$2` auf jedem UPDATE/DELETE/GetByID/Search-Pfad + `RowsAffected==0`-Sentinel.
- **RLS-Welle Nachtlauf 4** (2026-08-03, 20 Tabellen aktiviert, `knownRLSGaps` seit Migration 286 leer, 42 neue Routen). PR #17 → `da1073a4`, Prod-Kopf 287.
- **Backend-Nachtlauf 5** (2026-08-05/06, Migr. 288-297): Rest-Backlog. PR #18 → `9950f339`, **Prod-Kopf 297**. Deploy-Incident: 31 Min 503 durch veralteten API-Contract im Smoke-Skript → Auto-Rollback → Schema-Drift.
- **gRPC-Tenant-Spoof-Sweep** (Welle 3.5): `crm_grpc.go` liest `tenant_id` aus `middleware.GetTenantID(ctx)` statt `req.GetTenantId()` — verhindert Tenant-Spoof bei Service-zu-Service-Calls oder kompromittiertem Gateway.

**Unveraendert seit W20 (aber jetzt RLS-abgesichert):**

| Package | Was es liefert (Aug 2026 Status) | LoC service.go |
|---|---|---|
| `contact` | CRUD, FindDuplicates (trigram+email+phone), MergeContacts, CSV/vCard Import+Export, Visibility-Scoping (shared/personal/owner), Batch-Enrichment | 768 |
| `deal` | CRUD, MoveToStage, Multi-Currency (16 ISO-Codes), Probability-Weighted Forecasting (statisch), Event-Emitter | 635 |
| `activity` | CRUD, Complete/Uncomplete, AddTags, GetContactTimeline, CustomFields, Postgres-NOTIFY-Events | 531 |
| `company` | CRUD, AddTags/RemoveTags, GetCompanyContacts, Domain-Duplikat-Detection | 469 |
| `advisoryprotocol` | **NEU** — Beratungsprotokoll ZFA, Draft/HandOver/PDF/Referral-Report | 466 |
| `pipelinestage` | CRUD, Won/Lost-Terminal-States, Reorder, Probability-Weight | 270 |
| `savedfilter` | JSON-Filter pro User/Entity-Type, Default-Flag | 193 |
| `customfield` | Per-Entity-Type Custom-Fields (select/multi/text/num/date) | 202 |
| `consent` | DSGVO Art. 5/6/17: GrantConsent/RevokeConsent, ConsentHistory, RequestDeletion + IP-Audit | 201 |
| `tag` | Polymorphes Tagging mit Hex-Color, lazy-loaded | 184 |
| `search` | Cross-Entity FTS (Contacts, Companies, Deals, Activities) mit Fair-Distribution-Limits | 133 |
| `report` | GetPipelineReport, GetConversionReport, GetActivityReport (Cycle-Time, Stage-Transitions) | 125 |

**Automation-Actions in `internal/automation/action/crm_actions.go`:** Weiterhin **2** — `crm.update_deal_field` + `crm.create_contact`. Kein neuer CRM-Action seit W20.

### AI / MCP / Credits — Was NICHT existiert

| W20-Empfehlung | Zielpfad | Stand W35 |
|---|---|---|
| **MCP Read-Only-Server** | `backend/internal/crm/mcp/` | ❌ nicht angelegt |
| **AI-Credits-Infra** | `backend/internal/billing/ai-credits/` | ❌ nicht angelegt |
| **Cross-Modul-Kontext-API** (neu W34) | `backend/internal/ai/context-api/` | ❌ nicht angelegt |
| **LLM-Provider-Client** | `backend/internal/llm/client.go` | ✅ existiert (183 LoC, Ollama-default, OpenAI-wire-format-kompatibel) — **aber in KEINEM Modul gewired** |
| **Plugin-SDK/WASM** (Phase D-Marker) | `backend/internal/plugin/` | ✅ existiert (config, hook, repository, sdk, wasm) — aber keine CRM-relevanten Plugins |

### Knowledge-Layer

- `.knowledge/api.md`: Advisory-Protocol-Endpoints dokumentiert (Neu seit W20).
- `.knowledge/datenbank.md`: Migrations bis Prod-Kopf 297 (W20-Referenz: 111). **~186 Migrations in 15 Wochen** — ausserordentliche DB-Evolutionsrate durch Nachtlaeufe.
- `.knowledge/security.md`: 51 KB (deutliche Erweiterung seit W20) — RLS-Standing-Guard, `knownRLSGaps` leer seit Migration 286.
- `.knowledge/milestones.md`: Sprint-4-Welle-1 (RLS Foundation), Marathon FE-Lane 2026-06-11, Backend-Nachtlaeufe 1-5 (2026-07-26 bis 2026-08-06).

### Stand der Konkurrenz-Vergleichs-Achsen (Delta zu W20-Tabelle)

**Neu vorhanden (seit W20):**
- **RLS in Production** (nicht mehr nur Tenant-Filter — jetzt Postgres-Row-Level-Security aktiv).
- **Beratungsprotokoll ZFA** (Vertikal-Feature Zahnaerzte-KMU — Cross-Modul-Wert fuer `formulare` + `helpdesk`).
- **Automatisierte Nachtlauf-Backend-Iteration** (`.planning/backend-block/loop/` mit `claude -p`-Ralph-Loop) — **strukturelles Delivery-Delta** vs. Konkurrenz.

**Fehlend (unveraendert seit W20 — jetzt kritisch):**
1. **AI-Layer komplett** — 15 Wochen ohne Feature. Konkurrenz-Gap hat sich vergroessert.
2. **MCP-Server / Agent-Endpoint** — HubSpot GA, Twenty produktiv, Salesforce ecosystem. Cosmi-Anschluss fehlt.
3. **Sequences / Cadences** — Pipedrive und HubSpot Standard.
4. **Email-Workflow im CRM** — `email_actions.go` existiert, nicht CRM-integriert.
5. **Web-to-CRM Lead-Capture** — `formulare` + `crm` beide da, Bruecke fehlt.
6. **Mobile-App** — Backend-only.
7. **Predictive Forecasting** — `pipelinestage.probability` statisch.
8. **AEO-Sichtbarkeit** — 0 DACH-Vertikal-Content-Programme (kein `cosmi-vs-hubspot-dach/`, kein `cosmi-vs-salesforce-dach/`).
9. **Outcome-Billing-Infrastruktur** — nicht existent, aber jetzt Beschaffungspflicht (siehe W23-Keeper).
10. **NEU: Cross-Modul-Kontext-API** — W34-Top-5 P0-Empfehlung, noch nicht angelegt. Kritisch fuer Cosmi's einzigen strukturellen USP-Moat.

---

## Konkurrenz-Vergleichstabelle (Update W35)

| Feature | Cosmi | HubSpot | Salesforce | Twenty | Pipedrive | Bexio | monday |
|---|---|---|---|---|---|---|---|
| Pipeline-Mgmt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Probability-Weighted Forecasting (statisch) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ML-Deal-Scoring / Risk | ❌ | ✅ Breeze | ✅ Einstein | 🚧 v2.x | ✅ Deal-Scoring | ❌ | ✅ MyAI |
| Lead-Scoring (Fit+Engagement) | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| AI-Email-Drafting | ❌ | ✅ Breeze | ✅ Einstein | ✅ v1.22+ | ✅ AI Writer | ❌ | ✅ |
| Email-Sequences / Cadences | ❌ | ✅ | ✅ | 🚧 Workflows | ✅ GA | ❌ | ✅ |
| Multi-Agent-Orchestration | ❌ | ✅ **Agent Builder Beta 23.07.** | ✅ **Summer '26 GA** | 🚧 Multi-Turn SDK v2.29 | 🚧 | ❌ | 🚧 |
| **MCP-Server (Open, RFC 9728)** | ❌ | ✅ **GA April 2026** (mcp.hubspot.com) | ✅ **Tableau MCP Summer '26** | ✅ **v2.0 GA + Multi-Turn SDK** | ✅ (W22-Ankuendigung) | ❌ | ❌ |
| Outcome-Pricing (Credit-Metering) | ❌ | ✅ **HubSpot Credits GA** | 🚧 Consumption-Model | ✅ v2.1.1 Credit-Cap + v2.32 Stripe | ❌ | ❌ | ❌ |
| Conversational-CRM-UI (`/chat`-Modus) | ❌ | 🚧 Breeze Copilot | 🚧 Agentforce Voice | ✅ **v2.31 GA** | ❌ | ❌ | ❌ |
| ORM/Query-Layer LLM-tauglich | ❌ | ✅ Native | ✅ | ✅ **v2 EXISTS-Subqueries** | ✅ | ❌ | ❌ |
| Lead-Capture (Web-Form → CRM) | 🚧 (formulare exist., keine Bruecke) | ✅ | ✅ | 🚧 | ✅ Framework | ✅ | ✅ |
| Custom Fields | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Duplicate-Detection + Merge | ✅ (trigram+email+phone) | ✅ | ✅ | 🚧 | ✅ | ✅ | 🚧 |
| GDPR Consent + Erasure | ✅ (Vorbild) | ✅ | ✅ | ✅ DACH-spez. | ✅ | ✅ | ✅ |
| Row-Level Security (Postgres RLS) | ✅ **Welle 3.5+4 live** | n/a | n/a | ✅ (Multi-Tenant) | n/a | n/a | n/a |
| Self-Hosted Option | ✅ ORBIT | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| DACH-Compliance (CHF, ZUGFeRD, GoBD, XRechnung) | ✅ (CHF live, GoBD-Track) | 🚧 | ❌ | ❌ | ❌ | ✅ (USP) | 🚧 |
| Beratungsprotokoll (Vertikal ZFA) | ✅ **NEU** | ❌ | 🚧 (Domain-Packs) | ❌ | ❌ | ❌ | ❌ |
| Mobile App | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ | ✅ |
| Modulare Preismatrix (kein Tier) | ✅ (USP) | ❌ (Pro/Ent) | ❌ | n/a (OSS) | ❌ | ❌ | ❌ |
| Plugin-Marketplace / App-Store | 🚧 (WASM-SDK exist., 0 Plugins) | ✅ 2.000+ Apps | ✅ AppExchange | ✅ npm-basiert | ✅ | 🚧 | ✅ |
| AEO-Sichtbarkeit (AI-Suche) | ❌ | ✅ **#1 + AEO-Tool $45/Mo** | 🚧 | ❌ | 🚧 | ❌ | 🚧 |
| DACH-Vertikal-Content-Programm | ❌ | ✅ (Healthcare/RE/Insurance) | ✅ (Domain-Packs) | ❌ | ❌ | ❌ | ❌ |
| Cross-Modul-Kontext-API | 🚧 (implizit vorhanden, nicht API-fied) | 🚧 (Agent Builder Q1'27 GA) | ✅ (Domain-Packs) | 🚧 (SDK) | ❌ | ❌ | ❌ |

> Legende: ✅ produktiv · 🚧 angekuendigt/teilweise · ❌ fehlt · n/a nicht zutreffend
> **Fett = kritisches Delta seit W20**

---

## Cosmi-Schwachpunkte (Update-Priorisierung W35)

**Bedrohungsklasse A — jetzt kritisch (Delta zu W20: haerter):**

1. **MCP-Server-Abwesenheit ist Distributions-Verlust.** MCP ist unter Linux Foundation AAIF governance mit 97M+ Installs. HubSpot GA seit April, Salesforce Tableau MCP live, Twenty produktiv, Anthropic-CRM-Connectors etabliert. **Wer keinen MCP-Anschluss hat, wird nicht integriert.** Cosmi verliert in jedem "Kunde haengt Claude/ChatGPT an sein CRM"-Workflow den Datenkontakt an HubSpot/Twenty. **5. Woche ohne Architektur-Entscheid.**

2. **Kein AI-Layer heisst kein modernes-CRM-Fenster mehr.** 15 Wochen ohne Feature. Salesforce Agentforce +205% ARR. HubSpot Agent Hub Beta seit 4 Wochen live. Twenty `/chat` GA. **Cosmi-Pilot ohne AI-Feature = Cosmi-Pilot als "Retro-CRM"** — auch bei perfekter DACH-Compliance-Story.

3. **Cross-Modul-Kontext-API fehlt trotz vorhandener Daten.** Cosmi's einziger strukturell-ueberlegener USP ("Cosmi-Helpdesk weiss was im CRM steht") ist ohne API nicht **kommunizierbar**, nicht **demonstrierbar**, nicht **MCP-anschluesbar**. W34-P0-Empfehlung, noch nicht angelegt.

**Bedrohungsklasse B — strukturelle Erosion (neu seit W20):**

4. **Twenty-Feature-Kadenz-Uneinholbarkeit.** v2.20 → v2.34 in 15 Wochen (14 Major-Versionen). Cosmi liefert im gleichen Zeitraum RLS + 1 Sub-Package + Migrations-Volumen. **Feature-Paritaet mit Twenty ist strategisch nicht mehr moeglich** — W33-Architekturentscheidung (Fork vs. Own vs. Non-Parity) muss in KW35 fallen.

5. **AEO-Zeitfenster schliesst sich.** HubSpot publiziert 5 AEO-Artikel pro Woche, hat AEO-Tool nativ integriert, systematisiert Vertikal-Content (Healthcare/RE/Insurance). **DACH-KMU-Nischen-Queries** ("CRM Handwerk DACH Self-Hosted", "DSGVO-konformes CRM KMU Schweiz") sind heute noch offen — in 6-12 Monaten wahrscheinlich nicht mehr.

6. **Bexio-Feed-Blindheit + Bexio-Preiserhoehung-Chance ungenutzt.** DACH-Direkt-Konkurrent #1 hat 20% Preiserhoehung Q1 2026. Cosmi-Marketing sollte "Bexio-Wechsler-Angebot" haben. Feed-Ersatz seit 8 Wochen offen.

**Bedrohungsklasse C — Polish + Operative (weiterhin offen aus W20):**

7. **Reporting flach** (3 Reports, kein Revenue-Intelligence-Layer). Unveraendert.
8. **Probability statisch.** Unveraendert.
9. **Conversation-zu-Deal-Routing fehlt** (dialer ↔ crm-bridge). Sipgate/HubSpot als DACH-Referenz-Pattern seit W35-Morning (2 Sipgate-Artikel in einer Woche).
10. **Automation-CRM-Actions bleibt bei 2** — nach 15 Wochen sollte hier Wachstum sein (z.B. `crm.assign_deal_owner`, `crm.move_stage_conditional`, `crm.trigger_advisory_protocol`).

---

## Top-3 Strategische Empfehlungen (Update W35)

### 1. **MCP Read-Only-Server + Cross-Modul-Kontext-API als Doppel-Sprint** (P0, KW36-KW38 = 3 Wochen)

**Warum jetzt:** Beide Fundamente sind seit W20 empfohlen (MCP) bzw. W34 (Context-API). Beide sind Voraussetzung fuer jede weitere AI-Roadmap-Entscheidung. Getrennt gebaut wird doppelte Arbeit — beide brauchen dieselbe Tenant-Isolation-Bruecke und dieselbe Datenmodell-Introspection. **Zusammen ist es ein Sprint mit einem einzigen Architektur-Review.**

**Scope Doppel-Sprint:**
- **Woche 1:** `backend/internal/ai/context-api/` — Read-only-Endpoint der fuer eine Entity (Contact/Company/Deal) alle Cross-Modul-Datenpunkte aggregiert liefert (CRM-Deal-History + Helpdesk-Tickets + Schichten + Rechnungen + Fuhrpark). REST + gRPC. Tenant-Isolation via `middleware.GetTenantID(ctx)`. Rate-Limit + Feld-Whitelist. Als **Backend-Fundament fuer 2** und **3**.
- **Woche 2:** `backend/internal/crm/mcp/` — MCP-Server mit 6 Read-Only-Tools: `list_contacts`, `list_deals`, `get_deal_with_context`, `search_crm`, `get_pipeline_report`, `list_activities`. PKCE-Auth (RFC 9728). `get_deal_with_context` ruft Context-API. Twenty v2.0 als Referenz-Implementierung.
- **Woche 3:** Integration-Testing gegen Claude Desktop + ChatGPT + Cursor. Dokumentation `docs/mcp/cosmi-crm-mcp.md`. Discord-Pilot-Ankuendigung.

**Aufwand:** 3 Wochen (1 Backend-Engineer). Sprint-Review am Ende von Woche 3.

**Wirkung:** (a) Pilot-Kunden koennen Cosmi an Claude/ChatGPT haengen — direkt vermarktbar als "Self-Hosted MCP-CRM, EU-only, mit Cross-Modul-Kontext (kein anderer hat das)". (b) Cross-Modul-Kontext-API ist Fundament fuer die "Cosmi vs. HubSpot Agent Builder"-Demo-Video-Story (siehe W34-T02-Empfehlung). (c) Freie Bahn fuer Empfehlung #2.

**Anti-Scope (bewusst nicht in Sprint 1):**
- **Write-Endpoints im MCP-Server** — Phase 2, erst nach Pilot-Erfahrung.
- **Multi-Modul-MCP** (Helpdesk, Buchhaltung, etc.) — sequenziell nach CRM-MCP validiert.
- **Agent-Builder-UI** — verfrueht ohne Nutzungsdaten.

### 2. **`backend/internal/billing/ai-credits/` + Cosmi-AI-Pricing-Positionierung (Doppelstrang)** (P0, parallel zu #1, 2 Wochen)

**Warum jetzt:** Ohne Credits-Metering wird jedes AI-Feature Pauschal-Aufpreis — Beschaffungs-Killer im Mid-Market 2026 (W23-Keeper: HubSpot Credits GA, Salesforce evaluiert Outcome, Rillet-Story). Gleichzeitig zeigt Salesforce-Aktien-Kurs (-33% YTD trotz Agentforce-ARR-Verdopplung), dass **Consumption-Pricing im Markt Skepsis erzeugt**. Cosmi hat die Chance einer **dritten Positionierung**: **Flat-Fee-Cosmi-AI (predictably affordable) mit Credit-Metering-Backend fuer Enterprise-Optionalitaet.**

**Scope:**
- **Backend (1 Woche):** Schema `tenant_ai_credit_pool` + `ai_credit_transaction` + `ai_credit_pricebook`. Metering-Middleware (jede AI-RPC decrementiert Pool). Customer-Definable-Thresholds (Intercom-Pattern). Discord-Webhook bei Pool-Low. Twenty v2.1.1/v2.32 als Code-Referenz.
- **Marketing (1 Woche, parallel):** Positioning-Doc `marketing/pricing/cosmi-ai-flat-fee-positioning/` — "Cosmi-AI: Predictably affordable. Kein Token-Lottery." Vergleichs-Landing-Page vs. HubSpot Credits (mit Rechenbeispiel), vs. Salesforce Consumption.

**Aufwand:** 2 Wochen (1 Backend + 1 Marketing/Content).

**Wirkung:** Cosmi kann AI-Features als "Im Modul-Preis enthalten" launchen fuer Standard-KMU, Credits-Optionalitaet fuer Enterprise/High-Volume-Kunden. **Bessere Story als HubSpot** (Self-Hosted-Variant kann ggf. kostenlos via On-Device-LLM auf `internal/llm/`).

### 3. **Twenty-Architektur-Entscheidung SCHRIFTLICH + AEO-Erst-Salvo** (P1, KW35 SOFORT + laufend)

**Warum jetzt:** **Twenty-Architektur-Entscheidung ist zweite Woche unentschieden** (W33/W34-Konvergenz). Ohne Entscheidung driftet Cosmi-Roadmap in undefinierbare Feature-Paritaets-Konkurrenz. AEO-Zeitfenster schliesst sich pro Monat weiter (HubSpot-Volumen). Beide Themen sind **1-Person-Woche** — kein Grund fuer weitere Verzoegerung.

**Scope Twenty-Doc (SOFORT diese Woche):**
- **`docs/architecture/crm-twenty-fork-vs-own-decision.md`** — Entscheidungs-Doc:
  - **Non-Parity fuer:** `/chat`-Modus (Cosmi hat andere UX-Story: Modul-Uebergreifende Views statt Konversation), Email-Canvas (Zielgruppe schreibt weniger Marketing-Emails), Call-Transcript-Widget (dialer separat).
  - **Own-Implementation fuer:** ORM-EXISTS-Subqueries (Postgres-native machbar), Multi-Turn-Agent (via `internal/llm/` + Kontext-API).
  - **Nicht relevant:** npm-App-Store, Slack-Integration (Cosmi hat eigenen Chat).
- Kein Fork-Zwang. Kein Feature-Paritaets-Zwang. **Klare Nicht-Positions-Erklaerung ist Wertversprechen.**

**Scope AEO-Erst-Salvo (KW35-KW38 = 4 Wochen):**
- **5 DACH-vertikale Guides:** "CRM fuer Handwerksbetriebe DACH Self-Hosted", "CRM fuer Zahnarztpraxen (mit Beratungsprotokoll ZFA)", "DSGVO-konformes CRM KMU Schweiz — Bexio-Alternative 2026", "CRM ohne Tier-Pricing DACH KMU", "Cosmi vs. HubSpot Agent Builder Cross-Modul-Kontext-Test".
- **Schema-Markup + Sitemap** + AEO-Visibility-Baseline (Profound-Alternative $45/Monat HubSpot als Vergleichstool, oder AthenaHQ). Vertikal-Guide zu Beratungsprotokoll ZFA nutzt echtes Cosmi-Feature — kein Generic-Content.

**Aufwand:** Twenty-Doc = 2 Tage (Product-Lead). AEO-5-Artikel = 4 Wochen (1 Content-Person + 0.5 Tech-SEO).

**Wirkung:** Twenty-Doc **beendet aktive Uneindeutigkeit** in der Roadmap. AEO-Salvo baut in 6-9 Monaten qualifizierten Lead-Traffic aus AI-Suche — **DACH-Nischen sind noch offen**.

---

## Quellen (Top-Quellen die diesen Bericht stuetzen)

**Cosmi-IST-Stand:**
- `/opt/kmuhub/backend/internal/crm/{contact,deal,activity,company,advisoryprotocol,...}/service.go` (LoC-Zaehlung 4.177 total, 12 Sub-Packages)
- `/opt/kmuhub/backend/internal/automation/action/crm_actions.go` (2 CRM-Actions verifiziert)
- `/opt/kmuhub/backend/internal/llm/client.go` (Ollama-default LLM-Client, NICHT wired)
- `/opt/kmuhub/.knowledge/milestones.md` (Backend-Nachtlauf 1-5, Migr. 297)
- `/opt/kmuhub/.knowledge/architektur.md` (route_crm_advisory.go)
- `/opt/kmuhub/.knowledge/api.md` (Advisory-Protocol-Endpoints)
- `/opt/kmuhub/.knowledge/security.md` + `.knowledge/datenbank.md` (RLS-Welle-3.5-4, Migr. 118/119/286/287/297)

**Konkurrenz / Markt (Delta seit W20):**
- Twenty Releases v2.20 → v2.34 (github.com/twentyhq/twenty/releases, gefetcht 2026-08-24)
- HubSpot Developer Changelog (developers.hubspot.com/changelog, gefetcht) — Agent CLI Public Beta 23.06., CRM-API-Write-Validation Enforcement 2026-09
- HubSpot Company News: "Meet Agent Hub and Agent Builder" (23.07.2026)
- CMSwire: "HubSpot Debuts Agent Hub to Unify AI Agents" (07-08/2026)
- Salesforce Summer '26 Product Release Announcement (Multi-Agent Orchestration, Agentforce Voice, Tableau MCP)
- Anthropic MCP Ecosystem: MCP unter Linux Foundation AAIF, 97M+ Installs (Stormy AI Blog + settlewithai.com, Q3 2026)
- Pipedrive Blog: "Smarter deal scoring", "Smarter lead nurturing with Sequences", "Lead capture strategies 2026" (Feed 408, Landing-Page gefetcht)
- Scalemetrics: Bexio Pricing 2026 (20% Erhoehung Maerz 2026)

**Interne Aggregations-Berichte (zentria-intel, Delta-Zeitraum):**
- `keepers/ai-cost-governance-ist-die-neue-beschaffungs-pflic-crm-core-w23.md` (Outcome-Pricing als Beschaffungs-Pflicht, 05.06.)
- `keepers/direct-competitor-triple-pivot-twenty-kommerzialis-cross-w20.md` (Phase 6 Update via W34)
- `keepers/eu-sovereignty-kipppunkt-5-signale-an-einem-tag-9--cross-w20.md`
- `weekly/2026-W33.md` (Twenty-Sprint-Kadenz-Eskalation Top-5 #1, Cosmi-MCP-Server-Empfehlung 3. Woche)
- `weekly/2026-W34.md` (HubSpot Agent Builder + Salesforce Agentforce +2x YoY Top-5 #2, Context-API-P0-Empfehlung, EspoCRM v10.0.3/4/5)
- `daily/2026-08-21-evening.md` (HubSpot Agent Hub seit 23.07. = 4 Wochen live, Google SAM 18.08.)
- `daily/2026-08-24-morning.md` (Twenty v2.33 + v2.34 in <24h, Intercom Fin auf HubSpot+Freshworks, Sipgate-HubSpot-Integration DACH)
- `monthly/2026-05-11-deepdive-crm-core.md` (Zyklus 1 Referenz — Delta-Basis)

---

## Picks (vorgeschlagen)

[ ] 🟢 **Doppel-Sprint: MCP Read-Only-Server + Cross-Modul-Kontext-API** (KW36-KW38, 3 Wochen, 1 Backend-Engineer) — **Bedrohungsklasse A**, seit W20 offen, jetzt strukturell kritisch. Fundament fuer AI-Roadmap, Context-Demo-Story und Cross-Modul-USP-Kommunikation.

[ ] 🟢 **AI-Credits-Infrastruktur + Cosmi-AI-Pricing-Positioning** (parallel, 2 Wochen) — **Bedrohungsklasse A**, seit W20 offen. Beschaffungs-Pflicht 2026, Chance einer Flat-Fee-Positionierung als drittes Modell zwischen HubSpot-Credits und Salesforce-Consumption.

[ ] 🟢 **Twenty-Architektur-Entscheidungs-Doc `crm-twenty-fork-vs-own-decision.md`** (KW35 SOFORT, 2 Tage, Product-Lead) — **Bedrohungsklasse B**, aktive Uneindeutigkeit muss enden. Explicit Non-Parity-Erklaerung ist strategisches Wertversprechen.

[ ] 🟡 **AEO-Erst-Salvo: 5 DACH-vertikale Guides** (KW35-KW38, 4 Wochen, Content-Person + 0.5 Tech-SEO) — **Bedrohungsklasse B**. Zeitfenster schliesst sich, DACH-Nischen noch offen. Beratungsprotokoll-ZFA-Guide nutzt echtes Cosmi-Feature.

[ ] 🟡 **`crm.assign_deal_owner`, `crm.move_stage_conditional`, `crm.trigger_advisory_protocol` als 3 neue Automation-Actions** (KW36, 1 Woche) — Automation-CRM-Actions steigen von 2 auf 5. Direkter Feature-Delta ggue. Pipedrive-Sequences-Story.

[ ] 🟡 **Bexio-Wechsler-Marketing-Kampagne** (KW35-KW36, 1 Person-Woche) — 20% Bexio-Preiserhoehung Q1 2026 als Vertriebs-Hebel. Landing-Page + LinkedIn-Content + Preisvergleichs-Rechner. → followup 30d fuer Conversion-Metrik.

[ ] 🟠 **Lead-Capture-Bruecke `formulare` → `crm`** (Sprint nach Doppel-Sprint, 1 Woche) — Forms-Submission triggert `crm.create_contact` + optional Initial-Stage-Move via Automation. Seit W20 offen. Nach Context-API besser integrierbar. **Bedrohungsklasse A (Markt-Erwartung).** → followup 30d.

[ ] 🟠 **AI-Email-Drafting im Compose (erster konkreter AI-Touchpoint)** (nach Credits-Infra, 2 Wochen) — Outcome: Credit-gemetert, On-Device-LLM-Fallback via `internal/llm/`. Erste Manifestation Cosmi-AI-Layer. → followup 60d.

[ ] 🟠 **Feed-Sanierung: Pipedrive-Blog-URL, Bexio-Content-Alternative, HubSpot-Marketing-CRM-Core-Feed** (KW35, 2 Tage, DevOps) — Beobachtungs-Blindflug seit 4-8 Wochen. `sources/crm-core.yaml` + `.state/watermarks.json`. Priorisiert vor W36-Morning-Run.

[ ] 🔵 **Domyn-Follow-up "few quarters away from $1B ARR"** — W35-Recherche zu Produkt-Details (t3n, deutsche-startups.de, Latka-Update). Wenn Domyn im CRM/Business-Ops-Space DACH-relevant → Konkurrenz-Aufnahme in `crm-core.yaml`. → followup 14d.

[ ] 🔵 **Google-SAM-Evaluation fuer Cosmi-MCP-Phase-C** — Zero-Trust P2P-Overlay. Nach MCP-Read-Only-Server-Live (Phase 1) und Multi-Modul-MCP (Phase 2). → followup 90d.

[ ] 🔵 **HubSpot Agent Builder Q1 2027 GA + Third-Party-Agents-Freigabe Beobachtung** — wenn HubSpot Third-Party-Agents zulaesst, ist Cosmi-Cross-Modul-Kontext-Story konkret angegriffen. **Zeitfenster fuer Cosmi's Demo-Video-Story ist bis dahin.** → followup 90d.

[ ] 🔵 **EspoCRM AI-Counter-Move Beobachtung** (W33/W34-Kommentar) — falls EspoCRM in naechsten 6-8 Wochen kein AI-Feature announced, kann Cosmi-CRM-AI als "erstes KMU-taugliches AI-CRM in DACH" positioniert werden. → followup 30d.

---

## Telemetrie

- **Routine:** intel-monday-deepdive
- **Modul:** crm-core (1/15 Rotation Zyklus 2)
- **Delta-Basis:** `monthly/2026-05-11-deepdive-crm-core.md` (Zyklus 1 W20 — 15 Wochen zurueck)
- **Quellen gepollt:** 11 Konkurrenz-Feeds (crm-core.yaml) — davon 6 OK (Twenty, EspoCRM, SuiteCRM, HubSpot-Marketing, Salesforce, Odoo-GitHub) + 5 FAIL (Pipedrive 408, Bexio 403, Odoo-Blog 403, HubSpot-Product-Updates 403, monday). Weekly-Reports W33 + W34 + Daily 08-21-evening + 08-24-morning ausgewertet. Interne Wissens-Dateien: 5 Cosmi-Knowledge + 12 Cosmi-Backend-Files.
- **Live-Webfetches:** 5 (Twenty-Releases, HubSpot-Changelog, Salesforce-Summer'26, Anthropic-MCP-Ecosystem, Bexio-Pricing-2026, Domyn-Recherche).
- **Konkurrenz-Datenpunkte (Delta W20→W35):** HubSpot 12, Twenty 14 (v2.20→v2.34), Salesforce 6, Pipedrive 3, Bexio 4, Intercom 3, Google SAM 1, Rillet 2 (adjacent), MCP-Ecosystem 4.
- **G2/Capterra-Reviews:** ❌ uebersprungen (Headless-Chromium nicht im Run-Scope, G2 blockt Bot-Scrapes).
- **W20-Pick-Status:** MCP-Server ❌ offen · AI-Credits ❌ offen · AEO ❌ offen · Lead-Capture-Bruecke ❌ offen · Cosmi-Progress war Backend-Hardening (RLS + Migrations 111 → 297 + advisoryprotocol).
- **Neu-identifizierte kritische Luecken (W35):** Cross-Modul-Kontext-API (W34-Referenz), Twenty-Architektur-Entscheidungs-Doc, Bexio-Wechsler-Kampagne.
- **Naechstes Modul gemaess Rotation:** **dialer** (KW36, Mo 2026-08-31).
- **State-File:** `.state/deepdive_rotation.json` aktualisiert.

---

*Generiert: 2026-08-24 — Zyklus 2, Modul 1/15. Delta-Vergleich zum W20-Deepdive (15 Wochen). Naechste Iteration desselben Moduls fruehestens KW50/2026 (14.12.2026).*
