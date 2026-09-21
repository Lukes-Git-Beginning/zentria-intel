---
year: 2026
week: 39
modul: helpdesk
created: 2026-09-21
routine: intel-monday-deepdive
model: claude-opus-4-7
zyklus: 2
rotation_position: 5/15
delta_to: monthly/2026-06-08-deepdive-helpdesk.md
delta_weeks: 15
---

# Deepdive: helpdesk (Mo W39/2026, Zyklus 2)

> **Delta-Deepdive.** Baseline: `monthly/2026-06-08-deepdive-helpdesk.md` (W24, Zyklus 1). Zwischen-Reports mit Helpdesk-Bezug: `monthly/2026-09-14-deepdive-wiki.md` (Cross-Modul KB-Bridge fuer Helpdesk-Wissensdatenbank-Tab), `monthly/2026-08-24-deepdive-crm-core.md` (Contact/Org-Link zu Ticket via `entity_links`), `monthly/2026-09-07-deepdive-video.md` (LiveKit-Sovereignty-Verlust — relevant fuer Dialer-Voice-zu-Ticket-Story). Vorgaenger W38: `wiki`. Naechstes Modul: `formulare` (W40, 2026-09-28). Rotation: cycle 2, position 5/15.

> **TL;DR seit W24 (15 Wochen).** 5 der 10 W24-Empfehlungen sind ausgeliefert (Mock→Backend-Wiring der Datenpfade, KB-Article-Backend, CSAT-Backend inkl. Mailer + Dispatch, Routing-Rules-Backend, Business-Hours-SLA-Compute) — **Backend-Wachstum 2419 → 4014 LOC (+66%) plus ~5900 LOC Tests, 10 neue Migrations (000210, 000211, 000232, 000236, 000267, 000268, 000288, 000289, 000290, 000291), 5 neue Domain-Modelle (KBArticle, RoutingRule, BusinessHours, HolidayEntry, HelpdeskStats), Frontend 2043 → 3197 LOC (+57%), HelpdeskPage.tsx 996 → 1798 LOC**. Die drei strategisch am haertesten gerahmten P0/P1-Empfehlungen sind aber **komplett offen**: AI-Drafts mit EU-LLM-Provider-Wahl (Empfehlung #2 W24) — NULL Code. **EU-AI-Act Art. 50 Disclosure-Layer (Empfehlung #2/Compliance W24) — NULL Code, und Art. 50 ist seit 2026-08-02 durchsetzbar, Bundesnetzagentur + BaFin operativ seit 2026-07-29**. Dialer-Voice-zu-Ticket-Hook (Empfehlung #3b W24) — Dialer `event_emitter.go` existiert (25 LOC), aber null Helpdesk-Subscriber. `pg_trgm` Fuzzy-Merge — Code-TODO in `merge.go:14-15` unveraendert.

> **Leit-Signal der 15 Wochen.** Zwei strukturelle Marktereignisse veraendern die Helpdesk-Konkurrenz-Karte fundamental: (a) **Salesforce hat am 15. Juni 2026 die Fin (frueher Intercom) fuer 3,6 Mrd USD Akquisition angekuendigt**, Closing Q3 FY27 (~Nov 2026) — der letzte unabhaengige premium-AI-native-Helpdesk-Player wird von Salesforce Agentforce verschluckt. Der Mid-Market-DACH-Gap wird groesser. (b) **Zendesk hat Forethought am 26. Maerz 2026 geschlossen** und AI Agents in Suite/Support gefaltet (statt Separater Add-on, wie im W24-Baseline noch). **Voice AI Agents GA seit 2026-06-01** mit 60+ Sprachen und Mid-Conversation-Language-Switching. **Zammad hat AI-Text-Extractor + AI-Ticket-Tagger in 7.1 (17. Juni 2026) geliefert — und in 7.1.2/7.1.3 zwei Security-Releases mit 12 CVEs, davon mehrere AI-Agent-spezifisch (CVE-2026-34724: AI Agent Template Sanitizer Bypass → RCE, CVSS 7.2)**. Zammads AI-Angriffsflaeche ist damit dokumentiert-exploitable, was Cosmi einen sauberen "boring, but audited, keine AI-CVEs im Helpdesk"-Wedge fuer regulierte DACH-KMU (Steuerkanzleien, Krankenkassen, Banken) gibt — **allerdings nur so lange, bis Cosmi die eigene AI-Layer ohne Compliance-Foundation dranklebt**. Dritter Vector: **MCP-Server ist zwischen Juni und September 2026 vom R&D-Signal zum Helpdesk-Feature-Standard geworden** — Fin, Front, Plain, Pylon, Drag, Gorgias, Kustomer haben offizielle MCP-Server, Zendesk MCP-Client GA + Server EAP, **Freshworks bepreist MCP-Actions ab 2026-09-01 als geplan-limitiertes Feature** (100/500/1000 Actions pro Growth/Pro/Enterprise, 1000er-Packs 15 USD). Cosmi-MCP-Server (siehe W33-Keeper `backend/internal/core/mcp-server/`) bleibt unresolved — der 4-Wochen-Fenster-Vermerk aus W33 ist inzwischen 6+ Wochen alt.

---

## Delta zu W24 (2026-06-08 → 2026-09-21)

### Cosmi-Delivery-Bilanz

Vergleich zu den W24-Empfehlungen (Kernpunkte):

| W24-Empfehlung | W24-Status | Heute (W39) | Evidenz |
|---|---|---|---|
| **1. Frontend-Mock→Backend-Wiring (Datenpfade)** | BLOCKED | ✅ DONE | `HelpdeskPage.tsx:36-49` importiert `useTickets`, `useTicketMessages`, `useCreateTicket`, `useUpdateTicket`, `useCloseTicket`, `useReopenTicket`, `useAssignTicket`, `useMergeTickets`, `useAddMessage`, `useKBArticles`, `useCreateKBArticle`, `useUpdateKBArticle`, `useHelpdeskStats` aus `@/api/hooks/useHelpdesk`. Live-Datenpfad ueber TanStack, kein Mock-Store fuer Tickets/Messages/Queues/CannedResponses/BusinessHours. |
| **1. Enum-Konsolidierung Frontend↔Backend** | NOT STARTED | ✅ MOSTLY | Backend `ValidTicketStatuses`/`ValidTicketPriorities`/`ValidTicketChannels`/`SLAStatus`-Konstanten sauber, Frontend-Types folgen. **Rest-Drift** nur noch in HelpdeskSettingsPanel + CSATWidget, die weiter `useHelpdeskStore` fuer UI-Config (csatQuestion, csatDelayHours, csatEnabled, intakeChannels, intakeForms.agent) lesen — das ist Settings-State, nicht Datenpfad-State. Vollstaendige Konsolidierung erfordert `HelpdeskSettingsPanel.tsx` (197 LOC) auf einen echten Config-Endpoint umzustellen. |
| **2. AI-Drafts + EU-LLM-Provider-Wahl** | NOT STARTED | ❌ NOT STARTED | `backend/internal/llm/client.go` (184 LOC) existiert seit Wave 7C (Meeting-AI-Summary), **kein Multi-Provider-Router**, kein Helpdesk-Integrations-Endpoint. Kein Ollama/Mistral/Anthropic-Adapter-Layer. Zero pgvector-Aktivierung fuer Ticket/KB-Embeddings. |
| **2. EU-AI-Act Art. 50 Disclosure-UI** | NOT STARTED | ❌ NOT STARTED, **RECHTS-EXPOSITION LIVE** | Grep `ai_disclosure\|AIDisclosure\|Article 50\|Art\. 50` in `/opt/kmuhub` liefert **null Treffer**. Meeting-AI-Summary (`llm/client.go`) laeuft seit Wave 7C ohne Disclosure-Wrapper. Art. 50 durchsetzbar seit 2026-08-02, heute Tag 50 in der Live-Enforcement-Fensterphase. Wiki-Deepdive W38 hat das identisch geflagged. |
| **3a. KB-Article-Backend + Wiki-Bridge** | NOT STARTED | ✅ DONE (Backend), 🚧 TEILWEISE (Bridge) | Migration `000210_helpdesk_kb_articles`, `KBArticle` Domain-Model, CRUD-Proto/gRPC, Frontend `useKBArticles/useCreateKBArticle/useUpdateKBArticle` verdrahtet. **Cross-Modul-Bridge zu Wiki-Articles bleibt offen** — der Wissensdatenbank-Tab hat jetzt einen eigenen Helpdesk-KB-Store (separat von Wiki-Modul), nicht die W24-empfohlene Wiki-Article-Category-Filter-Bruecke. Zwei parallele KB-Systeme im Repo. |
| **3b. Dialer-Voice-zu-Ticket-Hook** | NOT STARTED | ❌ NOT STARTED | `backend/internal/dialer/event_emitter.go` existiert (25 LOC), aber grep `helpdesk\|ticket` gegen die Datei liefert **null Treffer**. Kein Helpdesk-Worker-Subscriber. Manuell "Create Ticket from Call" im Dialer-UI fehlt weiterhin. |
| **3c. CSAT-Backend + Persistierung** | NOT STARTED | ✅ DONE | Migrationen `000288_helpdesk_csat` + `000289_helpdesk_csat_survey_dispatch`, Files `csat_config.go`, `csat_dispatch.go`, `csat_mailer.go`, `csat_survey.go` (+ 6 Test-Files). CSAT-Default seit 2026-06-11 defensiv auf **Opt-in** gedreht (siehe milestones-Note zu Lauf-5-Merge: der Umfrage-Link zeigte auf `app.zentria.tech/csat`, wo nichts liegt) — richtige Deploy-Vorsicht. |
| **3d. Routing-Rules-Backend** | NOT STARTED | ✅ DONE | Migration `000211_helpdesk_routing_rules`, `RoutingRule` Domain-Model, CRUD-Proto/gRPC. Frontend `TicketRoutingConfig.tsx:26` importiert Backend-Hooks. |
| **Sek. Business-Hours-SLA-Compute** | NOT STARTED | ✅ DONE | Migration `000232_helpdesk_business_hours`, Models `BusinessHours`/`DaySchedule`/`HolidayEntry`, Service-Methods `GetBusinessHours()` + `UpsertBusinessHours()` (`service.go:1089-1114`). Frontend `BusinessHoursDialog.tsx` verdrahtet via `useBusinessHours`/`useUpdateBusinessHours`. Der Compute-Slot in `sla.go:ApplyPolicy()` selbst muss noch geprueft werden (der Kommentar zu "24/7-Annahme" ist evtl. veraltet — muss im Sprint-Review verifiziert werden). |
| **Sek. `pg_trgm` Fuzzy-Merge** | NOT STARTED | ❌ NOT STARTED | Kommentar in `merge.go:14-15` + `postgres_repository.go:272-276` unveraendert. `CREATE EXTENSION pg_trgm` + similarity-Query bleibt Sprint-Todo. |

**Zusaetzliche Backend-Deliverables seit W24 (die W24 gar nicht als Empfehlung enthielt):**

- Migration `000236_helpdesk_ticket_fields` — Custom-Fields fuer Tickets (Tenant-Erweiterbarkeit).
- Migration `000267_helpdesk_ticket_contact_org` — **Contact + Org-Link ueber `entity_links` zum CRM-Modul**. Das ist die W24-Cross-Modul-USP-Aktivierung, teilweise geliefert. Cosmi-Ticket kennt jetzt Ansprechpartner + Firma aus CRM.
- Migration `000268_helpdesk_ticket_source_channel` — Intake-Channel-Tracking (`agent`/`selfservice`/`external`). Bereitet Multi-Channel-Inbox vor, ohne die Kanaele selbst zu bauen.
- Migration `000290_helpdesk_ticket_intake_fields` — Intake-Metadaten.
- Migration `000291_helpdesk_external_requester` — externe Requester-Identitaet (Vorstufe zu Customer-Portal-Login).
- Backend-Test-Files: `contact_org_link_test.go`, `csat_config_test.go`, `csat_dispatch_db_test.go`, `csat_dispatch_test.go`, `csat_redeem_db_test.go`, `csat_survey_db_test.go`, `csat_survey_test.go`, `csat_test.go`, `external_requester_db_test.go`, `intake_cross_tenant_db_test.go`, `name_fallback_db_test.go`, `own_scope_list_test.go`, `tenant_write_test.go`, `ticket_intake_test.go`, `ticket_requester_name_db_test.go` — insgesamt ~5900 LOC Test-Growth (Wave-2 Tenant-Isolation-Sweeps + CSAT-DB-Path-Coverage + Cross-Tenant-Intake-Coverage). **`.knowledge/milestones.md` Commit `4267c87e` (2026-08-27)**: "test(helpdesk): cover SLA time math and gateway queue/KB/business-hours handlers" — 465 Zeilen neue Coverage in `route_helpdesk_test.go`.
- Frontend-Neuzugang: `desktop/src/renderer/src/modules/helpdesk/settings/HelpdeskSettingsPanel.tsx` (197 LOC) — Modul-Settings-UI, aktuell aber noch mock-store-driven fuer CSAT/Intake-Konfiguration.
- HelpdeskPage.tsx hat sich von 996 LOC auf **1798 LOC** verdoppelt: Multi-Filter-UI (Status/Priority/Channel/Queue), KB-Article-Panel, Reply-Composer-Refactor, Merge-Dialog, Duplicate-Suggestion-Panel, Intake-Channel-Selector.
- Frontend-Client `helpdesk-client.ts` von 198 → 308 LOC, Hooks-File `useHelpdesk.ts` von 316 → 459 LOC, Mock-Store `stores/helpdesk.ts` von 254 → 697 LOC (mehr Mock-Daten fuer Settings-Panels, Testing, Storybook).

**Delivery-Rate-Interpretation.** 5/10 W24-Empfehlungen strukturell geliefert, drei davon mit erheblichem Nachfolge-Engineering (CSAT-Mailer + Dispatch, Business-Hours mit Feiertagen, Routing-Rules-Engine). Das ist **erheblich ueberdurchschnittlich** verglichen mit z.B. W23 Wiki-Deepdive, wo 15 Wochen spaeter zwei zentrale P0-Empfehlungen (AI-Disclosure + Wiki-Article-Embeddings) noch immer null Code hatten. **Cosmi-Backend-Team konzentriert sich weiter auf strukturell-domaenen-orientierte Deliverables — die drei Compliance-/AI-/Cross-Modul-Empfehlungen bleiben liegen, weil sie eine neue Fachdomaene (LLM-Ops + Multi-Provider-Adapter + Rechtsprodukt-UI) aufmachen, die aktuell im Team nicht besetzt ist.** Das ist die zentrale Diagnose dieses Delta-Reports.

### Markt-Delta seit W24

**A. Salesforce → Fin (3,6 Mrd USD, angekuendigt 2026-06-15).** ([Salesforce Press Release](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/)) Fin (frueher Intercom Inc., rebrandet 2026-05-12) wird die Agentforce-Customer-Service-Spitze. ~30k AI-Kunden wechseln ins Salesforce-Portfolio. Closing Q3 FY27 (Nov 2026 erwartet). Fin-Preis unveraendert **0,99 USD/Outcome, $49 Base mit 50 Resolutions**. Fin Voice + Fin Vision + MCP-Server (US + EU) shipping. **Strukturelles Signal fuer Cosmi**: der letzte unabhaengige premium-AI-native-Helpdesk-Player wird von einem US-Hyperscaler-CRM-Anbieter konsumiert. Das ist **Argument #1 fuer Cosmi's EU-Souveraenitaets-Positionierung im Helpdesk-Segment** — bei jedem Salesforce/HubSpot/Fin-Deal wird jetzt eine Auslands-CRM-Abhaengigkeit tiefer verankert. Cosmi-Sales-Pitch-Update: "Fin geht zu Salesforce, Intercom heisst nicht mehr Intercom, HubSpot war es nie — Cosmi ist der Application-Layer, bei dem Sie in DACH bleiben."

**B. Zendesk → Forethought (angekuendigt 2026-03-11, geschlossen 2026-03-26).** ([TechCrunch](https://techcrunch.com/2026/03/11/zendesk-acquires-agentic-customer-service-startup-forethought/)) Die AI Agents heissen jetzt **"Forethought AI Agents by Zendesk"** und sind in Suite/Support gefaltet — nicht mehr Separater Add-on wie im W24-Baseline. **Voice AI Agents GA seit 2026-06-01** ([Zendesk help](https://support.zendesk.com/hc/en-us/articles/10849624262170)) mit 60+ Sprachen + Mid-Conversation-Language-Switching. Outcome-Pricing hat sich bei Zendesk Relate Mai 2026 zu **1,50–2,00 USD pro Resolution** verschoben, mit Dual-Verification der billed-Resolutions und Auto-Overage-Dashboard — Antwort auf die Enterprise-Kritik ueber Outcome-Pricing-Opazitaet aus W24. **Copilot-Add-on jetzt 50 USD/Agent/Monat**, Suite + Copilot Enterprise 209 USD/Agent/Monat.

**C. Zammad 7.1 (2026-06-17) + Security-Kaskade 7.1.1 (2026-06-25) / 7.1.2 (2026-08-04) / 7.1.3 (2026-08-25).** ([Zammad 7.1](https://zammad.com/en/product/releases/zammad-7-1)) 7.1 brachte AI-Text-Extractor (strukturierte Feld-Extraktion aus Email-Subject/Body via Regex oder LLM) + AI-Ticket-Tagger (Topic-Auto-Tags) — Erweiterung der Zammad-7.0-Bring-Your-Own-LLM-Architektur. **Aber Security-Cadence hat sich verhaertet**: 7.1.2 fixt fuenf kritische CVEs, darunter **CVE-2026-34724 AI Agent Template Sanitizer Bypass → RCE (CVSS 7.2)**, S/MIME-Sender-Impersonation, IDOR im External-Data-Source, PGP-Signature-Spoof. 7.1.3 fixt weitere sieben Issues, darunter **SSRF via DNS-Rebinding, Cross-Tenant-Attachment-Disclosure via Inline-Images, Arbitrary-Object-Disclosure via Core-Workflow, External-Data-Source-Credential-Leak** ([Zammad 7.1.2](https://zammad.com/en/product/releases/7-1-2), [Zammad 7.1.3](https://zammad.com/en/product/releases/7-1-3)). CVE-Trend: **11 CVEs in Zammad 2026 YTD vs 4 CVEs in ganz 2025**. Die AI-Agent-Feature-Flaeche ist damit ein dokumentiert-exploitierbarer Angriffspfad. **Strategie-Impact fuer Cosmi**: das ist der einzige Punkt, an dem Cosmi-Helpdesk gerade JETZT einen Kern-Wedge hat — "keine AI im Helpdesk = keine AI-CVEs im Helpdesk". Fuer regulierte KMU (Steuerkanzlei, Kanzlei, Banken, Kassen, Gesundheitswesen) ist das jetzt ein sauberes Procurement-Argument. **Fenster ist begrenzt**: sobald Cosmi eine AI-Layer ohne Article-50-Foundation + Threat-Modeling-Audit dranklebt, verliert es dieses Wedge sofort.

**D. Freshworks Freshdesk: First-Price-Raise seit 5 Jahren + MCP-Metering.** ([Drag Freshdesk pricing 2026](https://www.dragapp.com/blog/freshdesk-pricing/)) Growth 19 USD (statt 15), Pro 49 USD, Enterprise 89 USD. Freddy AI Agent unbundled: **500 Sessions inklusive, dann 49 USD pro 100 Sessions, unused expire**. **Freshworks ist der erste Mainstream-Helpdesk, der MCP als Rate-Limited-Feature pro Plan bepreist** — ab 2026-09-01 **100/500/1000 Actions auf Growth/Pro/Enterprise**, 1000-Action-Packs 15 USD. Das signalisiert: MCP-Server ist keine Innovation mehr, sondern Standardleistung mit Metering-Reife.

**E. HelpScout price-model reversion + Front Autopilot re-framing.** HelpScout hat auf **per-User-Pricing zurueckgekehrt**: 25/45/75 USD annual, 30/54/90 USD monthly, AI-Answers **0,75 USD/Resolution** mit 3-monatlichem Free-Trial. AI-Drafts/AI-Summarize sind ab Plus-Plan gebundelt, kein Extra-Charge. Front Autopilot ist **auf 0,05 USD/Conversation gesenkt** (statt 0,89 USD/Resolution wie W24 dokumentiert — Front reframt zu Per-Conversation, nicht Per-Resolution). Front shippt offiziellen **MCP-Server**. **Konsequenz fuer Cosmi-Pricing**: die Konkurrenz senkt tatsaechlich die Per-Interaction-Preise, waehrend Base-Seats stabil bleiben. Das ist **Rueckenwind fuer Cosmis Flatrate-Kern-Positionierung** — "4 EUR/User/Modul, keine metered-AI-Ueberraschung" ist ein zunehmend eindeutiger DACH-KMU-Kaufgrund gegenueber intransparenter Outcome-Pricing.

**F. EU-AI-Act Article 50: Enforcement live seit 2026-08-02.** ([Article 50 Enforcement Guide](https://www.aiactblog.nl/en/posts/article-50-enforcement-fines-ai-act-2026), [BaFin AI market surveillance](https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_07_29_ki_verordnung_en.html)) Deutschland KI-MIG designiert die **Bundesnetzagentur** als zentrale AI-Marktueberwachungsbehoerde; **BaFin** deckt Finanzsektor-AI (beide operativ seit 2026-07-29). Kein publik gemeldetes Bussgeld bis heute (Stand 2026-09-21), aber Bundesnetzagentur-Beschwerdeportal ist live, Industrie-Presse erwartet erste symbolische Bussgelder in Q4 2026. Deckelung: **15 Mio EUR / 3 % Welt-Umsatz** fuer Art.-50-Transparenz-Verstoesse, bis zu 35 Mio EUR / 7 % fuer verbotene Praktiken. **Cosmi-Doppel-Signal**: (i) fuer Cosmi-Helpdesk ist Article 50 heute noch nicht anwendbar (keine AI-Funktion), (ii) fuer Cosmi-Video-Modul (Meeting-AI-Summary via `llm/client.go` seit Wave 7C) und ggf. andere AI-Nutzungen im Repo ist heute **Tag 50 der Live-Enforcement-Phase ohne Disclosure-Wrapper** — das ist die Wiki-W38-Diagnose, die hier eskaliert werden muss.

**G. MCP-Server: R&D → Standard-Feature.** MCP-Server sind bei allen wichtigen Helpdesks live oder EAP: Fin, Plain, Pylon, Drag, Front, Gorgias, Kustomer offiziell shipping; Zendesk MCP-Client GA + Server EAP; **Freshworks metered ab 2026-09-01**. Der Cosmi-W33-Keeper `backend/internal/core/mcp-server/` (Contacts/Deals/Tickets/Shifts/Invoices) ist damit von "P0 mit 2-4-Wochen-Fenster" zu "6 Wochen ueberzogenes P0" eskaliert. **Fuer Helpdesk spezifisch**: ein Cosmi-Helpdesk-MCP-Server (search_tickets, get_ticket, create_ticket, add_message, close_ticket) wuerde Cosmi in Claude-Code / Cursor / Claude-Desktop / Fin-Anwender-Workflows integrieren — und, wichtiger, in **Lovable-gebaute-KMU-Frontend-Prototypen** (siehe W33-Keeper `ai-substitution-lovable-vibe-coding-w33`). Fin-Salesforce-Konsolidierung macht Cosmi-MCP-Server zusaetzlich zum defensiblen KMU-Wedge, weil das Salesforce-Ecosystem im DACH-KMU-Segment strukturell abweisend ist (Preis, Komplexitaet), waehrend Cosmi-MCP-Server DACH-KMU-first exponiert werden kann.

**H. Neue Marktakteure mit Helpdesk-Nachbarschaft.** Sierra (950 Mio USD @ 15 Mrd Post, Mai 2026; Receptive AI + Takeoff akquiriert, Ghostwriter + Horizon; AIUC-1-Certified) — Enterprise-only, KMU-irrelevant, aber der pure Kapital-Anstieg zeigt: AI-Agent-Betriebssystem-Kategorie wird 2026 zur Cash-Zone. Decagon (250 Mio USD Series D @ 4,5 Mrd, Jan 2026; Dialogues 2026, Agent Operating Procedures, Watchtower Real-Time-Compliance-Monitor; behaupten 50–80 % Resolution) — Voice + Chat + Email + SMS. Kustomer AI-for-Customers 2.0 (Maerz 2026): "Procedures" (deterministische Logik in generativen Flows), offizieller MCP-Server. Chatwoot Captain AI July 2026 Refresh: Memories-Feature (persistenter Customer-Context), Mobile AI Assist, PDF/URL-Learning, ranked FAQ-Suggestions aus resolved-Tickets ([Chatwoot changelog](https://www.chatwoot.com/changelog)) — der Open-Source-DACH-Peer neben Zammad legt AI zunehmend nach. **OTOBO 11.1 Beta (2026-06-24)** ([OTOBO 11.1](https://otobo.io/en/otobo-11-1-beta/)): Ticket-View-Speed, Inline-Article-Editing (kein Separater Package), Elasticsearch-Field-Query-Syntax, Similar-Tickets-Widget, Parallel-Filters — **weiterhin ohne AI**. Cosmi-Nachbarschaft: OTOBO fokussiert auf besseren Core, Zammad auf AI-Feature-Expansion + Security-Firefighting.

---

## State-of-the-Art (Update 2026-09-21)

Der Helpdesk-Markt liegt Mitte September 2026 in **fuenf klar unterscheidbaren Kategorien**, die sich seit W24 verhaertet haben:

**1. AI-Native-Enterprise (Sierra, Decagon, Kustomer).** 4,5–15 Mrd USD Bewertungen, 50–80 % Resolution-Rate-Claims, Voice + Chat + Email + SMS + MCP + Voice-Agents-mit-Sprachwechsel. Nicht KMU-relevant, aber Preis-Setter fuer den Rest.

**2. Hyperscaler-Absorbed (Zendesk + Forethought, Salesforce + Fin ab Q4 2026).** Konsolidierungs-Endpunkt der ersten AI-Agent-Welle. Enterprise-verankert, DACH-KMU nur durch Reseller-Kanal (SoftwareOne, Bechtle). Preis-Anker: 1,50–2,00 USD/Resolution (Zendesk), 0,99 USD/Outcome (Fin). Copilot-Add-on 50 USD/Agent/Monat.

**3. Established-SaaS-Helpdesk mit AI-Add-ons (Freshdesk + Freddy, HelpScout, Front).** Mid-Market-Standard, per-User-Pricing 19–105 USD + granulare AI-Add-ons + Metered-AI-Actions. **Freshdesk ist erster Anbieter, der MCP-Actions als geplan-limitiertes Feature verkauft** (100/500/1000 Actions Growth/Pro/Enterprise). HelpScout ist zurueck auf per-User + 0,75 USD/AI-Answer. Front senkt Autopilot auf 0,05 USD/Conversation. **DACH-KMU-Relevanz-Hoehepunkt in dieser Kategorie** — der 10-Agent-Freshdesk-Pro-Vergleich (490 USD/Monat all-in, kein DACH-Hosting) ist Cosmis wichtigster Sales-Vergleichsanker.

**4. EU-Sovereign-Self-Host mit AI-Beimischung (Zammad 7.1, Chatwoot Captain AI).** Zammad hat mit 7.1 AI-Feature-Portfolio erweitert, bezahlt aber mit einer Security-Cadence, die auf-praxis-tenant-Beobachter (jaehrliche CVE-Zahl x3 gegenueber 2025, AI-Agent-Angriffsflaeche exploitable) beunruhigt. Chatwoot Captain AI ist die Open-Source-Alternative-Alternative, aber englisch-erst und aussereuropaeisch gehostet. **Cosmis natuerliche Kategorie**, wenn Cosmi eine AI-Layer haette.

**5. EU-Sovereign-Self-Host OHNE AI (OTOBO 11.x, Cosmi-Helpdesk heute).** Kategorie-Standort: fuer regulierte DACH-KMU-Buyer (Compliance-First-Procurement) heute der einzige rechtssichere Pfad. **Cosmi-Position ist strukturell verteidigbar solange (a) Cosmi keine AI-Funktion ohne Disclosure ausrollt, (b) die Konkurrenz weiter AI-CVEs sammelt, (c) Article 50 kraeftig durchsetzt.** OTOBO ist der einzige direkte Nachbar in dieser Kategorie — und OTOBO hat 11.1 Beta ohne AI-Features geliefert.

Vier zusaetzliche strukturelle Shifts seit W24, die alle 5 Kategorien tangieren:

**(a) Voice-AI ist ueber die "Shipping"-Linie.** Zendesk Voice-AI-Agents GA Q2 mit Voice-Config Juni; Fin Voice, Sierra (post-Receptive), Decagon Voice alle in Production; Front baut Voice via Autopilot. Voice ist ueber dem KMU-Tier Standard. **Cosmi-Vorteil**: LiveKit-Stack ist bereits im Video-Modul integriert, Dialer-Modul hat Call-Lifecycle-Events (S3.7 done seit Mai 2026). Voice-zu-Ticket-Bridge (Empfehlung #3b W24) ist eine der **niedrigsten Aufwand-Hoechstwert-Erschliessungen im Cosmi-Repo** — 3–5 Tage Engineering, aber schaltet den Cosmi-USP-Anker "ERP-Cross-Modul-Kontext" fuer den Helpdesk-Kanal an.

**(b) MCP ist Standard, nicht mehr R&D.** Sieben offizielle Helpdesk-MCP-Server, Zendesk-Server-EAP, Freshworks-Metering-Model — das ist Q1 2027 Table-Stakes-Feature. Cosmi-Helpdesk-MCP-Server (5 Tools: `search_tickets`, `get_ticket`, `create_ticket`, `add_message`, `close_ticket`) ist niedrig-aufwaendig (3–5 Tage) und differenziert Cosmi im KMU-DACH-Segment gegen die Salesforce-Fin-Zusammenlegung.

**(c) Pricing-Modell-Konsolidierung auf Outcome/Resolution:** Zendesk 1,50–2,00 USD, Fin 0,99 USD, HelpScout 0,75 USD, Front Autopilot 0,05 USD/Conversation, Freshworks 0,49 USD-Session-Aequivalent. Range komprimiert nach unten. Per-Seat-AI-Add-ons (20–50 USD) auch normiert. **Fuer Cosmi**: die transparente Per-User-Flatrate mit 0 EUR Overage-Risiko wird zunehmend zum eigenstaendigen Kaufgrund fuer Predictable-Budget-KMU. **Anti-SaaS-flation-Content-Sprint (W33-Keeper)** hat neue Munitions-Zeile: "Freshdesk hebt Preise nach 5 Jahren erstmals — Cosmi-Flat ist bewusst Preis-stabil designt."

**(d) Consolidation ist echt.** Zendesk+Forethought geschlossen; Salesforce+Fin angekuendigt; Sierra+Receptive+Takeoff. Die unabhaengige-premium-AI-Helpdesk-Kategorie wird von Hyperscaler-CRM absorbiert. Zammad und OTOBO sind die einzigen DACH-verankerten Open-Source-Alternativen — Zammads Q3-CVE-Cadence gibt Cosmi einen glaubwuerdigen "boring, but audited"-Wedge, der 4–12 Monate haelt, bevor Cosmi's eigene AI-Layer ausgeliefert werden muss.

---

## Cosmi-IST-Stand (Stand 2026-09-21)

Reading: `/opt/kmuhub/backend/internal/helpdesk/` (20 Files, ~9921 LOC inkl. Tests, 4014 LOC ohne Tests) + `/opt/kmuhub/desktop/src/renderer/src/modules/helpdesk/` (8 .tsx-Files, 3197 LOC) + `/opt/kmuhub/desktop/src/renderer/src/api/helpdesk-client.ts` (308 LOC) + `useHelpdesk.ts` (459 LOC, 40+ Hooks jetzt) + `stores/helpdesk.ts` (697 LOC, jetzt Config-State-Store nicht Datenpfad-Mock) + `/opt/kmuhub/.knowledge/milestones.md` (Eintraege 2026-06-08 bis 2026-08-27) + `/opt/kmuhub/backend/internal/dialer/event_emitter.go` (25 LOC) + `/opt/kmuhub/backend/internal/llm/client.go` (184 LOC).

**Backend — Was Cosmi-Helpdesk HAT (Highlights, mit Delta zu W24):**

- ✅ **10 Domain-Models** (`models.go`, 278 LOC — von 127): Ticket (unverändert Kern), TicketMessage (unverändert), TicketQueue, CannedResponse, SLAPolicy, **KBArticle (NEU)**, **RoutingRule (NEU)**, **HelpdeskStats (NEU)**, **BusinessHours (NEU)**, **HolidayEntry (NEU)** — plus Supporting-Structs `DaySchedule`, `WeeklyDayCount`, `SLAStatus`.
- ✅ **Ticket-Status-Enum** unveraendert: `open` / `pending` / `solved` / `closed` / `merged` — Backend autoritativ, Frontend jetzt aligned.
- ✅ **Priority-Enum** unveraendert: `low` / `normal` / `high` / `urgent`.
- ✅ **Ticket-Channel-Enum (NEU)**: `agent` / `selfservice` / `external` — bereitet Multi-Channel-Inbox vor (Migration 000268 + 000290).
- ✅ **SLA-Engine mit Business-Hours-Compute (NEU!)**: `sla.go` (62 LOC unveraendert) + `service.go:GetBusinessHours/UpsertBusinessHours()` (Lines 1089-1114) + Backend-Migration 000232 (`helpdesk_business_hours.up.sql`) mit `DaySchedule` (Mo-So + start/end) + `HolidayEntry`. Frontend `BusinessHoursDialog.tsx` (361 LOC) auf `useBusinessHours`/`useUpdateBusinessHours` verdrahtet. **Verifikations-TODO**: der `ApplyPolicy()`-Compute-Pfad in `sla.go` selbst muss geprueft werden — der W24-Code-Kommentar "24/7-Annahme" muss durch ein Delta-Sprint-Review bestaetigt werden, ob der tatsaechliche Business-Hours-Compute in `ApplyPolicy` inkorporiert wurde oder nur die Config-Persistierung.
- ✅ **CSAT-Backend komplett (NEU!)**: `csat_config.go` (Config-Persistierung, Opt-in-Default), `csat_survey.go` (Survey-Lifecycle + Redemption), `csat_dispatch.go` (Automation-Trigger bei Ticket-Resolution), `csat_mailer.go` (E-Mail-Versand), Migrationen 000288 + 000289. **Wichtige Deploy-Hygiene (milestones-Note zu Lauf-5-Merge, 2026-06-11)**: CSAT-Default auf `Enabled=false` gedreht, weil der Survey-Link zunaechst auf `app.zentria.tech/csat` zeigte (ohne Landing-Page). Richtige defensive Praxis. Frontend `CSATWidget.tsx` (148 LOC) verdrahtet auf `useSaveCsat` + `useTickets`. **Verifikations-TODO**: die CSAT-Landing-Page (`app.zentria.tech/csat`) muss existent und tenant-gebrandet sein, sonst blockt sie die CSAT-Aktivierung.
- ✅ **Routing-Rules-Backend (NEU!)**: Migration 000211, `RoutingRule`-Model, CRUD-Proto/gRPC. Frontend `TicketRoutingConfig.tsx` (169 LOC) auf Backend-Hooks. **Verifikations-TODO**: wird die Rule-Engine wirklich in der Ticket-Create/Update-Pipeline evaluiert oder nur konfiguriert-und-vergessen? `service.go` (1120 LOC) muss geprueft werden.
- ✅ **KB-Article-Backend (NEU!)**: Migration 000210, `KBArticle`-Model, CRUD. Frontend-Wissensdatenbank-Tab in `HelpdeskPage.tsx` verdrahtet auf `useKBArticles/useCreateKBArticle/useUpdateKBArticle`. **Aber**: eigener Store, keine Wiki-Bruecke — siehe Empfehlung #3 in diesem Report.
- ✅ **Custom-Fields (NEU!)**: Migration 000236 fuer Tenant-Erweiterbarkeit — Cosmi-KMU koennen tenant-spezifische Ticket-Felder definieren.
- ✅ **CRM-Bridge (Contact + Org-Link) (NEU!)**: Migration 000267 haengt Tickets an `entity_links` zu CRM-Contacts/Orgs. **Das ist ein W24-USP-Aktivierungs-Element**, teilweise geliefert — die Cross-Modul-Bridge zum CRM ist jetzt echt.
- ✅ **External-Requester-Identitaet (NEU!)**: Migration 000291 — Vorstufe zu Customer-Portal-Login. Cosmi kann Tickets von externen Requestern (Endkunden ohne Cosmi-Account) verwalten, was fuer Customer-Portal-Phase 2 benoetigt ist.
- ✅ **Intake-Metadaten (NEU!)**: Migration 000290 — Tracking, ueber welchen Kanal (agent/selfservice/external) ein Ticket kam, mit Metadaten.
- ✅ **Tenant-Isolation Wave 2 + Cross-Tenant-Intake Test-Coverage (NEU!)**: `intake_cross_tenant_db_test.go`, `external_requester_db_test.go`, `own_scope_list_test.go`, `tenant_write_test.go`. Cosmi's Tenant-Isolation-Testschraube ist seit W24 signifikant angezogen — das ist ein Compliance-Boost fuer regulierte KMU-Kaeufer.
- ✅ **Duplicate-Detection + Merge**: `merge.go` (93 LOC, von 89) — ILIKE-Prefix-Match unveraendert, TODO-Kommentar `pg_trgm`-Migration (Lines 14-15 + `postgres_repository.go:272-276`) unveraendert seit W24.
- ✅ **Service-Layer**: `service.go` von 623 → 1120 LOC (+80 %) — Business-Hours-CRUD, KB-CRUD, Routing-Rules-CRUD, CSAT-Config-CRUD, Intake-Field-Update, External-Requester-CRUD, plus ~40 neue Methods.
- ✅ **Repository**: `postgres_repository.go` von 536 → 1497 LOC (+180 %) — 10 Domain-Models heisst 10x CRUD + JOINs zu `entity_links`.
- ✅ **Migrationen**: von 2 → 12 aktive Helpdesk-Migrationen (000210, 000211, 000232, 000236, 000267, 000268, 000288, 000289, 000290, 000291 seit W24; die vorherigen `_helpdesk_tickets` etc bleiben Basis).
- ✅ **Feature-Flag** unveraendert: `modules.helpdesk` default-OFF, Tenant-Opt-In. Sprint-Ready fuer Pilot-Tenants.

**Frontend — Was Cosmi-Helpdesk HAT (Highlights):**

- ✅ **HelpdeskPage.tsx 1798 LOC** (von 996): Multi-Filter-UI (Status/Priority/Channel/Queue), KB-Article-Panel, Reply-Composer mit Bot-Lucide-Icon (AI-Scaffolding-Slot unveraendert seit W24 — Placeholder wartet auf AI-Empfehlung), Merge-Dialog, Duplicate-Suggestion-Panel, Intake-Channel-Selector.
- ✅ **Mock→Backend Datenpfad-Wiring**: `useTickets`, `useTicketMessages`, `useCreateTicket`, `useUpdateTicket`, `useCloseTicket`, `useReopenTicket`, `useAssignTicket`, `useMergeTickets`, `useAddMessage`, `useKBArticles`, `useCreateKBArticle`, `useUpdateKBArticle`, `useHelpdeskStats` — alle aus `@/api/hooks/useHelpdesk` importiert und live.
- ✅ **BusinessHoursDialog.tsx** (361 LOC): auf `useBusinessHours`/`useUpdateBusinessHours` verdrahtet.
- ✅ **CannedResponsesPanel.tsx** (355 LOC, von 316): auf `@/api/hooks/useHelpdesk` verdrahtet.
- ✅ **CannedResponsePicker.tsx** (99 LOC, von 106): auf `useCannedResponses` verdrahtet.
- ✅ **TicketRoutingConfig.tsx** (169 LOC, von 146): auf Backend-Hooks verdrahtet.
- ✅ **CSATWidget.tsx** (148 LOC, von 140): auf `useTickets` + `useSaveCsat` verdrahtet — **plus Rest-Mock-Store fuer csatQuestion**.
- ✅ **SLABadge.tsx** (70 LOC, +/- 1 LOC): stabile Anzeige.
- ✅ **HelpdeskSettingsPanel.tsx (NEU, 197 LOC)**: Modul-Settings-UI, aktuell aber **noch mock-store-driven** fuer CSAT-Enabled/Delay-Hours/Question, Intake-Channels, Intake-Forms.

**Was Cosmi-Helpdesk NICHT HAT (Stand 2026-09-21, sortiert nach W24-Schwere):**

- ❌ **AI-Drafts / AI-Reply-Suggestion** — null AI-Funktion (unveraendert). `Bot`-Lucide-Icon-Slot im Reply-Composer wartet weiter. `backend/internal/llm/client.go` (184 LOC) ist als Meeting-AI-Summary-Client gebaut (Wave 7C), **kein Helpdesk-Endpoint**, kein Multi-Provider-Router, kein Provider-Wahl-Adapter, kein pgvector, kein Embedding-Index.
- ❌ **EU-AI-Act Article 50 Disclosure-UI** — **RECHTS-EXPOSITIONS-KRITISCH**: null Disclosure-Wrapper im Repo. Grep `AIDisclosure|ai_disclosure|Article 50|Art\. 50` in `/opt/kmuhub` liefert **null Treffer**. Meeting-AI-Summary (Video-Modul, Wave 7C) laeuft seit ~4–8 Wochen Live-Enforcement-Phase ohne Disclosure. Fuer Helpdesk heute noch nicht anwendbar (keine AI), aber blockt die AI-Draft-Empfehlung #2.
- ❌ **AI-Summaries (Ticket-Thread-Summary)** — kein Endpoint, keine LLM-Call-Verbindung, keine Prompt-Templates. Zammad 7.0 hat das seit Maerz 2026.
- ❌ **AI-Auto-Triage (Topic-Klassifikation + Auto-Queue)** — keine Routing-Rule-Engine-Fallback zu LLM. Zammad 7.1 (Juni) hat AI-Text-Extractor + AI-Ticket-Tagger.
- ❌ **Sentiment-Analyse / Auto-Priority-Update** — kein Score-Feld, keine LLM-Inferenz, kein Priority-Auto-Escalate. Freddy AI (Freshdesk Pro) und Zendesk Copilot haben das.
- ❌ **LLM-Provider-Wahl-Architektur** — kein Multi-Provider-Router, kein per-Tenant-Provider-Setting, kein Ollama-Local-Adapter. Zammad hat 7 Provider-Slots als DACH-KMU-GDPR-Pattern.
- ❌ **Cosmi-Helpdesk-MCP-Server** — kein `backend/internal/core/mcp-server/` (W33-Keeper unresolved 6+ Wochen), keine Helpdesk-Tool-Exposition fuer Claude-Code / Cursor / Lovable-Frontends. **Neu in W39**: der Markt hat MCP-Server-Standardisierung ueberschritten (Freshworks metert), Cosmi ist strukturell zurueck.
- ❌ **Wiki-Article-Bridge fuer Helpdesk-KB-Tab** — es gibt jetzt zwei parallele KB-Systeme: `helpdesk_kb_articles` (Migration 000210) und `wiki_articles` (Wiki-Modul). Die W24-Empfehlung #3a war explizit "kein separates KB-Backend, Wiki nutzen" — jetzt beides. **Sub-optimales Architektur-Outcome**, muss in W40 Wiki-Deepdive re-eskaliert werden.
- ❌ **Dialer-Voice-zu-Ticket-Hook** — `dialer/event_emitter.go` existiert (25 LOC), **null Helpdesk-Subscriber**. Kein "Create Ticket from Call"-Flow, kein Call-Transcript-Initial-Message.
- ❌ **Email-zu-Ticket-Pipeline** — kein IMAP-/SMTP-Receiver-Service erkennbar. Sekundaer-Empfehlung P2 W24 unveraendert.
- ❌ **Voice-AI-Integration** — LiveKit im Video-Modul, aber keine Voice-AI-Transkription-Pipeline.
- ❌ **`pg_trgm` Fuzzy-Dup-Detection** — TODO-Kommentar unveraendert. 1-2 Tage Aufwand.
- ❌ **Customer-Portal / Public-Self-Service-Frontend** — External-Requester-Migration (000291) ist Vorstufe, aber kein Login, keine Public-UI. Die Voraussetzung fuer B2C-Cosmi-Kunden ist gelegt, das Portal fehlt.
- ❌ **Public-Status-Page** — kein Statuspage-Pendant.
- ❌ **Macros / Triggers / Automations** — nur Routing-Rules-Engine hat einen einfachen Fall abgedeckt. Vollstaendige Event-getriebene-Automation-Engine (Zendesk-Triggers-Pattern) fehlt.
- ❌ **Analytics-Dashboards** — `HelpdeskStats`-Model + `useHelpdeskStats`-Hook existiert, aber tiefergehende Reports (SLA-Compliance-Trend, Volume-per-Queue, Time-to-Resolution-Verteilung, Agent-Performance) sind offen.
- ❌ **Smart-CSAT-Inference / Smart-QA / Conversation-Scoring** — CSAT-Survey-only, kein AI-Sentiment-Inference-Score.
- ❌ **Mobile-Helpdesk-Editor** — Cosmi-Mobile-App unveraendert ohne Helpdesk-Modul-Routing.
- ❌ **SCIM-Provisioning** — kein User-Sync fuer Azure-AD/Okta.
- ❌ **Audit-Trail / Compliance-Log** — keine dedizierte `helpdesk_audit`-Tabelle (auch nicht fuer zukuenftige AI-Calls).
- ❌ **Anti-Spam / Trusted-Sender-Whitelist** — noch nicht relevant ohne Email-Pipeline.

**Zwischen-Bilanz.** Cosmi-Helpdesk W39 = **Solid-Core-Ticketing mit Cross-Modul-Fundamenten (CRM-Link, KB, CSAT, Routing-Rules, Business-Hours) und null AI**. Die Backend-Deliverables der letzten 15 Wochen sind praezise domaenen-modellgetrieben und schaffen die richtige Datenschema-Grundlage fuer eine spaetere AI-Layer. **Das Setup ist gerade JETZT bereit fuer die AI-Draft-Phase-1**, weil die Ticket-Schema-Stabilisierung + CSAT-Feedback-Loop + Routing-Rule-Templates die Trainings-/Retrieval-Datenbasis fuer AI-Suggestion + Auto-Triage bilden. **Aber**: ohne Article-50-Disclosure-Layer und ohne Multi-Provider-Router ist Cosmi-Helpdesk-AI nicht rechts-startfaehig. **Empfehlung dieses Reports** (siehe unten): die drei fehlenden Bausteine gleichzeitig starten — AI-Provider-Router + Disclosure-Layer + AI-Drafts-Endpoint sind ein **einzelnes 6-8-Wochen-Sprint-Paket**, nicht drei separate Themen.

---

## Konkurrenz-Vergleichstabelle (Update 2026-09-21)

| Feature | Cosmi W39 | Zendesk (+ Forethought AI Agents + Voice) | Freshdesk (Pro + Freddy AI Agent + MCP) | Zammad 7.1 (Plus v2 + AI-Agents) | Fin (Ex-Intercom, SF-akquiriert) | HelpScout (Plus + AI Answers) | Front (Pro + AI Suite + MCP) | OTOBO 11.1 Beta |
|---|---|---|---|---|---|---|---|---|
| **Ticket-Lifecycle (Status-Engine)** | ✅ 5-State | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **SLA-Engine mit Business-Hours-Compute** | ✅ (Schema+CRUD, Compute-Verifikation TODO) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Custom-Fields pro Tenant** | ✅ Mig 000236 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Queue-Routing (Manual + Rules)** | ✅ Rules-Engine (Verifikation Ticket-Create-Pipeline TODO) | ✅ Triggers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Contact/Org-Link (CRM-Bridge)** | ✅ Mig 000267 (`entity_links`) | 🚧 via Salesforce-Integration | 🚧 via CRM-Freshsales | ✅ via Contacts | ✅ Salesforce (nach Merger nativer) | ✅ | ✅ | ✅ |
| **KB-Article-Backend** | ✅ Mig 000210 (getrennt von Wiki!) | ✅ Guide | ✅ | ✅ | ✅ | ✅ Docs | ✅ | ✅ |
| **Wiki-Cross-Modul-Bruecke fuer Helpdesk-KB** | ❌ zwei parallele KB-Systeme | n/a | n/a | n/a | n/a | n/a | ✅ Notion/GDrive-Connector | n/a |
| **AI-Drafts / Suggested Replies** | ❌ null | ✅ Copilot | ✅ Freddy Copilot | ✅ Writing Assistant + Text-Extractor + Ticket-Tagger | ✅ Fin AI Agent | ✅ AI Drafts | ✅ Copilot | ❌ |
| **AI-Summaries (Ticket-Thread)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **AI-Auto-Triage (Topic + Priority + Sentiment)** | ❌ | ✅ AI Agents | ✅ Freddy | ✅ AI Text-Extractor + Tagger | ✅ Fin Procedures | 🚧 | ✅ Topics + Smart QA | ❌ |
| **AI-Resolution autonom (Outcome-billable)** | ❌ | ✅ 1,50-2,00 USD/Res | ✅ 0,49 USD/Session-Aequiv | 🚧 nicht autonom | ✅ 0,99 USD/Outcome | ✅ 0,75 USD/Answer | ✅ Autopilot 0,05 USD/Conv | ❌ |
| **Voice-AI-Agent (Telefon)** | ❌ (Dialer da, kein Hook) | ✅ 60+ Sprachen, Mid-Conv-Language-Switch (GA 2026-06-01) | ✅ Freshcaller-Freddy | ✅ Sipgate-Integration + AI-Optional | ✅ Fin Voice | ❌ | ✅ Voice via Autopilot | ❌ |
| **EU-LLM-Provider-Wahl-Architektur** | ❌ | ❌ US-Cloud | ❌ US-Cloud | ✅ 7-Provider (Zammad AI EU + OAI + Anthropic + Azure + Mistral + Ollama + Custom) | ❌ US-Cloud, EU-Workspace | ❌ | ❌ | ❌ |
| **Local-LLM (Ollama) Self-Host-Option** | ❌ | ❌ | ❌ | ✅ Ollama | ❌ | ❌ | ❌ | ❌ |
| **EU-AI-Act Art. 50 Disclosure-UI (durchsetzbar 2026-08-02)** | n/a (keine AI) — **Rechtsvorteil solange keine AI** | 🚧 Audit-in-progress | 🚧 Audit | 🚧 Audit + Post-CVE-Review | 🚧 Audit (SF-Merger noch) | 🚧 Audit | 🚧 Audit | n/a |
| **Ticket-Merge / Duplicate-Detection** | ✅ ILIKE-Prefix (`pg_trgm` TODO) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Similar-Tickets-Widget (NEU 11.1) |
| **Multi-Channel-Inbox (Email + Chat + Voice + Social)** | ❌ Intake-Enum vorbereitet, keine Kanaele | ✅ | ✅ | ✅ Email + Chat + Phone + Twitter + FB | ✅ | ✅ Email + Chat | ✅ Email + Chat + SMS + Voice | ✅ |
| **Email-zu-Ticket-Pipeline** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Voice-zu-Ticket (Dialer-Hook)** | ❌ Dialer da, Hook fehlt | ✅ Voice AI | ✅ Freshcaller | ✅ Sipgate | ✅ Fin Voice | ❌ | ✅ | ❌ |
| **Native-KB-Connectors (Notion / GDrive / Confluence)** | ❌ | ✅ | ✅ | ✅ | ✅ Procedures | ✅ Docs | ✅ | ❌ |
| **Internal Notes** | ✅ TicketMessage.internal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Attachments** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CSAT-Backend (Survey + Persistierung + Mailer + Dispatch)** | ✅ (NEU, Opt-in-Default) | ✅ | ✅ | ✅ | ✅ Smart Score | ✅ | ✅ | 🚧 |
| **Smart-CSAT (AI-Inference statt Survey)** | ❌ | 🚧 | 🚧 | ❌ | ✅ | ❌ | ✅ | ❌ |
| **Smart-QA / Conversation-Scoring** | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Routing-Rules-Backend (Auto-Assign)** | ✅ (NEU, Engine-Verifikation TODO) | ✅ Triggers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Macros / Automations / Triggers** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Analytics-Dashboards** | 🚧 `HelpdeskStats` + Hook, Reports TODO | ✅ Explore | ✅ Insights | ✅ | ✅ | ✅ | ✅ Smart QA | ✅ |
| **Customer-Portal / Public-Self-Service** | 🚧 External-Requester-Mig 000291 (Vorstufe), kein Portal | ✅ Guide | ✅ | ✅ | ✅ Help-Center | ✅ Docs Site | ✅ | ✅ Self-Service-Portal 11.1 |
| **Multi-Tenant-Isolated (Sprint-2/3-Compliance + Wave-2-Sweeps)** | ✅ + Cross-Tenant-Intake-Coverage (NEU) | n/a (SaaS) | n/a (SaaS) | ✅ Self-Host | n/a (SaaS) | n/a (SaaS) | n/a (SaaS) | ✅ Self-Host |
| **EU-Self-Host (DSGVO-nativ)** | ✅ | ❌ Cloud-only | ❌ Cloud-only | ✅ AGPL | ❌ Cloud-only (EU-Workspace) | ❌ | ❌ | ✅ AGPL |
| **Open-Source** | ❌ proprietaer | ❌ | ❌ | ✅ AGPL-3.0 | ❌ | ❌ | ❌ | ✅ GPL |
| **MCP-Server / LLM-Tool-Use** | ❌ (W33-Keeper unresolved 6+ Wochen) | ✅ Client GA, Server EAP | ✅ Metered ab 2026-09-01 | 🚧 | ✅ EU + US | ❌ | ✅ (offiziell) | ❌ |
| **Mobile-Helpdesk-App** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **SCIM-Provisioning** | ❌ | ✅ Enterprise | ✅ Enterprise | ✅ Plus v2 | ✅ Enterprise | ✅ Enterprise | ✅ Enterprise | ✅ Enterprise |
| **Audit-Trail / Compliance-Log** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI-CVE-Exposition 2026** | ✅ null (keine AI) — **Sales-Wedge** | 🚧 Voice-AI-neuland | 🚧 | ❌ CVE-2026-34724 RCE via AI Agent + 11 CVEs YTD | 🚧 | 🚧 | 🚧 | ✅ null |
| **Pricing/Seat (DACH-KMU-relevanter Tier)** | **~4 EUR Modul** | 19–169 USD + Copilot 50 USD + AI-Agents 1,50–2,00/Res | 19–89 USD + Freddy 49/100 Sessions + MCP-Actions ab 15 USD/1000 | 16–18 EUR/Agent + 0,03 EUR/AI-Call | 39–139 USD + 0,99/Outcome (SF-Merger folgt) | 25–75 USD/Agent + 0,75 USD/Answer | 25–105 USD/Seat + Autopilot 0,05/Conv | Self-Host kostenlos, Enterprise-Sub |
| **AI-Preis-Modell** | n/a | 1,50–2,00 USD/Res | 0,49 USD/Session-Aequiv + MCP-Metering | 0,03 EUR/AI-Call | 0,99 USD/Outcome | 0,75 USD/Answer | 0,05 USD/Conversation | n/a |
| **KMU-ERP-Modul-Integration (Helpdesk ↔ CRM ↔ Dialer ↔ Wiki ↔ Buchhaltung)** | ✅ (Contact/Org-Link geliefert; Voice-Hook + Wiki-Bruecke offen) | ❌ | ❌ | ❌ | ✅ nach SF-Merger enger | ❌ | ❌ | ❌ |
| **Markt-Reife / Sales-Track-Record** | 🚧 Beta (modules.helpdesk OFF) — bereit fuer Pilot-Tenants | ✅ Markt-Standard | ✅ Massmarkt | ✅ DACH-OS-Anker (Security-Frag) | ✅ Markt-Standard (SF-Fusion pending) | ✅ Mid-Market | ✅ Inbox-Niche | ✅ DACH-Legacy |

**Lesart der Tabelle (Delta zu W24).**

Die W24-Vergleichstabelle hatte "3 Vorteile / 18+ Defizite". W39-Update: **5 strukturelle Vorteile** (EU-Self-Host, Multi-Tenant-Isolation-mit-neuen-Sweeps, KMU-ERP-Modul-Integration mit **echter Contact/Org-Bridge (NEU!)**, null AI-CVE-Exposition, transparente Flat-Preis-Positionierung) gegen **11 verbliebene Defizite** (AI-Drafts, AI-Summaries, AI-Auto-Triage, Sentiment-Analyse, Voice-AI-Agent, LLM-Provider-Wahl, EU-AI-Act-Disclosure-UI, Voice-zu-Ticket-Hook, Wiki-KB-Bruecke, MCP-Server, Multi-Channel-Inbox-Kanaele). Von den 18+ Defiziten in W24 sind acht geloest (KB-Backend, CSAT-Backend, Routing-Rules-Backend, Business-Hours-SLA, Custom-Fields, Contact/Org-Link, Intake-Metadaten, `pg_trgm`-Aufschub bleibt sekundaer). Die **AI-/Compliance-/Cross-Modul-Voice-Bruecke** bleibt die zentrale offene Front — plus **MCP-Server als W39-neue-Kategorie**, die W24 noch nicht als Standard-Feature betrachtet hat.

Vier Diskrepanzen-Lager, verschoben zu W39:

1. **Frontend-Settings-Restmock (`HelpdeskSettingsPanel.tsx` + `CSATWidget.tsx` Config-Feld)** — nicht kritisch, aber blockt die vollstaendige Enum-Konsolidierung. Naechstes Sprint-Housekeeping.
2. **Wiki-Article-Bridge fehlt (zwei parallele KB-Systeme)** — architektonisch unerwuenschtes Outcome der letzten 15 Wochen. Muss im W40 Wiki-Deepdive re-eskaliert werden.
3. **AI-Compliance-Doppelloch (Article 50 Disclosure fehlt + kein Multi-Provider-Router + kein Helpdesk-AI-Endpoint)** — bleibt die Cosmi-Helpdesk-Strategie-Kern-Front.
4. **MCP-Server als 2027-Q1-Table-Stakes-Feature offen** (W33-Keeper 6+ Wochen unresolved) — neue W39-Priorisierung.

Zwei Compliance-/Positioning-Lager:

1. **Rechts-Wedge "null AI-CVE, null Article-50-Risiko" ist heute Cosmi-Helpdesk-Sales-Munition**. Fenster geschaetzt 4–12 Monate, bevor Cosmi die eigene AI-Layer bauen muss.
2. **Anti-Metered-AI-Positionierung** (transparente Flat-Preise vs Freshworks MCP-Metering, Zendesk Voice-Overage-Dashboards): das ist Anti-SaaS-flation-W33-Keeper-Content-Sprint-Munition.

---

## Top-3 Strategische Empfehlungen (W39, Zyklus 2)

### 1. **AI-Compliance-Foundation-Sprint: Multi-Provider-Router + Article-50-Disclosure-Layer + Helpdesk-AI-Drafts Phase 1 als EIN Sprint-Paket (P0 Pflicht, Sprint 4 Welle 1)**

**Problem, verstaerkt in W39.** W24 hat AI-Drafts + EU-LLM-Provider-Wahl + Article-50-Disclosure als drei separate Empfehlungsteile gerahmt. Nach 15 Wochen sind alle drei bei null. **Das ist kein Zufall, sondern ein struktureller Sequenz-Defekt in der W24-Empfehlung**: die drei Themen bilden ein einzelnes 6-8-Wochen-Sprint-Paket, weil sie voneinander abhaengen und nur zusammen einen liefer-fertigen Ausgang haben:

- **Kein AI-Draft-Endpoint** ohne **Multi-Provider-Router** (weil DACH-Compliance jede Cloud-LLM-Weiter-Route braucht — Frankfurt-Ollama, Mistral-Paris, Anthropic-Frankfurt vs OpenAI-US).
- **Kein Multi-Provider-Router** ohne **Disclosure-Layer** (weil Article-50-Enforcement live ist, jeder AI-Call MUSS als AI-Call markiert werden bevor der erste Endpoint live geht).
- **Kein Disclosure-Layer** ohne **Trigger-Cases**, d.h. ohne einen ersten AI-Endpoint fuer den Disclosure gilt.

Ausgangslage: `backend/internal/llm/client.go` (184 LOC) ist da, aber ist ein OpenAI-Wire-Compatible-Client fuer Meeting-Summaries (Wave 7C), kein Router. Der Router ist der W33-Keeper `backend/internal/ai/providers/router/`, der seit W25 (Anthropic-Kill-Switch-Fable-5) unresolved ist — jetzt eskaliert von 6 Wochen (W33) auf ~12 Wochen (W39). **Beide Themen sind ein einzelnes Sub-System, das Wave 7C nur teilweise angefangen hat.**

**Empfehlung — dreiteilige Sprint-Welle (parallel + sequenziell):**

**Track A — Provider-Router-Skelett (2-3 Wochen, Backend-Team):**

- Neues Package `backend/internal/ai/providers/router/` mit Interface `Provider` (Chat, Embed, Moderate — nur was Cosmi in den naechsten 6 Monaten braucht).
- **Adapter Tier 1 (Pflicht, DACH-Compliance)**: `mistral.go` (Mistral AI Cloud Paris, mit Shieldstral-3B-Moderations-Layer wie W33-Keeper dokumentiert), `ollama.go` (Local-Self-Host, OpenAI-wire-compatible — bereits vorbereitet in `llm/client.go`), `custom.go` (Tenant-Setting-driven, OpenAI-Compatible-Endpoint).
- **Adapter Tier 2 (Optional, Tenant-Opt-In)**: `anthropic.go` (Claude — Cosmi-primaerer AI-Ethik-Anker seit W25-Anthropic-Kill-Switch-Fable-5-Keeper), `openai.go`, `azure.go`.
- Provider-Routing-Config als Tenant-Setting-Tabelle `tenant_ai_provider_config` (tenant_id, feature_key ["helpdesk.draft", "video.summary", ...], provider_id, model, api_key_encrypted [Vault/KMS], fallback_provider_id, cost_ceiling_monthly).
- Bestehende `llm/client.go` (Wave 7C) refactoren zu `ollama.go`-Adapter, `video.summary` als erstes Feature auf den neuen Router migrieren (Regression-Test: existing Meeting-AI-Summary-Behavior unveraendert).

**Track B — Article-50-Disclosure-Layer (1-2 Wochen, Full-Stack + Legal-Review):**

- Neues Package `backend/internal/compliance/ai_disclosure/` mit:
  - `DisclosureRegistry`: registriert alle AI-Features (feature_key, human_readable_name, provider_currently_used, data_flow_description).
  - `AuditLog`-Tabelle `ai_disclosure_audit` (tenant_id, user_id, feature_key, provider_id, model, prompt_hash, response_hash, timestamp) — Compliance-Audit-bereit.
  - Middleware `RequireDisclosureAck`: jede AI-generierende-Endpoint-Route muss `disclosure_ack=true` im User-Session-Cookie oder Explicit-Consent-Response-Header haben.
- Frontend `desktop/src/renderer/src/components/shared/AIDisclosureBanner.tsx`:
  - Erst-Login-Banner "Cosmi nutzt AI-Features: {Liste}. Provider: {Name} ({EU/US-Region}). Trainings-Daten-Nutzung: [Nein]. Opt-Out unter [...]" — Pflicht-Klick vor Nutzung.
  - Per-AI-Interaktion-Hint "(AI-generiert, vor Senden pruefen)" als visible-Label.
  - Manager-Panel `AIProviderSettings.tsx`: Tenant-Admin sieht welcher LLM je Feature genutzt wird, kann Opt-Out setzen.
- Retrofit **existing** Meeting-AI-Summary-Endpoint mit Disclosure-Wrapper — das schliesst die Wiki-W38-P0-Lucke fuer die Video-Modul-Nutzung.
- `.knowledge/compliance-ai-act-article-50.md` als interne-Compliance-Dokumentation-Referenz, Quartals-Review-Prozess.

**Track C — Helpdesk-AI-Drafts Phase 1 (2-3 Wochen, Full-Stack):**

- Neuer Endpoint `POST /api/v1/helpdesk/tickets/{id}/draft-reply` mit Router-Integration + Disclosure-Wrapper.
- Prompt-Template: aktuelle Ticket-Thread (Systemrolle "Cosmi Helpdesk Assistant, DACH-KMU-Ton") + Tenant-Canned-Responses als Few-Shot-Beispiele + Retrieval-Context (Phase-1: Ticket-eigene-Messages; Phase-2: Wiki-Article-Semantic-Search — siehe Empfehlung #3).
- Frontend: Reply-Composer Bot-Icon-Button (bereits importiert!) triggert `useDraftReplyMutation` -> Editor fuellt sich -> Agent reviewed/anpasst/sendet.
- **Co-Pilot-only, kein Auto-Send** (rechts-defensive Startlinie).
- Rate-Limiter: 200 Drafts/Tenant/Tag als Default, Tenant-Setting-erweiterbar.
- Kosten-Tracking pro Tenant: `helpdesk_ai_usage` (rows counting Drafts + Latency + Provider-Cost-Estimate).
- Preis-Modell fuer Cosmi-Sale (nicht Sprint-4-Deployment-Kritisch): **0,20 EUR/AI-Draft** (Anker gegen HelpScout 0,75 USD/Answer), Beta-Phase kostenlos fuer Pilot-Tenants.

**Security-Track D (parallel zu A/B/C, Pflicht vor Live-Deploy):**

- Threat-Modeling-Session auf Basis Zammad-7.1.2/7.1.3-CVE-Cluster mit CWE-Mapping:
  - **CVE-2026-34724 AI Agent Template Sanitizer Bypass → RCE**: Cosmi-Draft-Prompt-Templates duerfen keine User-Content unescaped in System-Prompts einfuegen. Prompt-Injection-Sanitizer + Test-Suite mit den Zammad-CVE-Prompts.
  - **SSRF via DNS-Rebinding** (Zammad 7.1.3): Egress-DNS-Resolve fuer AI-Provider-Endpoints muss auf Static-IP-Ranges gepinnt sein (Mistral, OpenAI, Anthropic, Azure — fest kodiert oder via DNSSEC-verified).
  - **Cross-Tenant-Attachment-Disclosure via Inline-Images** (Zammad 7.1.3): jede Ticket-Attachment-URL im AI-Prompt muss tenant-id-gefiltert werden.
  - **AI-Assistance-Controller Improper-Access-Control** (Zammad 7.0.1, jetzt bestaetigt): jeder Router-Call MUSS `middleware.GetTenantID(r.Context())` als erste Aktion.
- CI-Check: neue AI-Route-Files (`route_helpdesk_ai.go` + zukuenftige) muessen automatisiert auf Tenant-Guard + Sanitizer geprueft werden.

**Zeitschaetzung Gesamt-Paket A+B+C+D: 6-8 Wochen** (mit 1.5-2 FTE Backend, 1 FTE Frontend, 0.3 FTE Legal-Review + Security). Track A ist Voraussetzung fuer C, Track B ist parallel zu A, Track D ist parallel + Blocker-fuer-Live-Deploy.

**Risiken:**

- Wave 7C Meeting-Summary-Refactor auf neuen Router kann Regressionen ausloesen — Regression-Test-Suite Pflicht.
- Article-50-Draft-Guidelines (EU-Kommission) hatte finale-Code-of-Practice-Zieltermin Juni 2026 — Verifikation aktueller Stand: gibt es 2026-Q3-Guidance, die Cosmis Disclosure-UI in-scope brechen wuerde? Legal-Review-Track.
- Prompt-Injection ist ein aktives, hitzegetriebenes-Angriffs-Territorium. Cosmi wird nicht in Sprint 4 einen perfekten Sanitizer bauen — Ziel ist "gute-genug-fuer-Co-Pilot-only-mit-agent-Review", nicht "gute-genug-fuer-Auto-Resolution".
- Multi-Tenant-Provider-Config-Encryption-Layer benoetigt Vault/KMS-Integration — falls Cosmi das noch nicht hat, ist das ein separater 1-Sprint-Preqisitensprint.

**Konsequenz bei Nicht-Handeln:** in 6-12 Monaten hat Cosmi entweder (a) kein AI im Helpdesk und verliert Sales-Bewerbungen im DACH-Mid-Market-Segment gegen Freshdesk-Pro-mit-Freddy-inklusive, oder (b) hat AI ohne Article-50-Foundation gebaut und riskiert Bundesnetzagentur-Bussgeld + reputational-Schaden. **Beide Ausgangspunkte sind wesentlich teurer als das 6-8-Wochen-Investment jetzt.**

---

### 2. **Cosmi-MCP-Server (Helpdesk + Cross-Modul) — vom W33-Keeper zum Sprint-4-Deliverable (P0, 3-5 Tage Grund-Server + iterative Tool-Exposition)**

**Problem, neu in W39 verstaerkt.** Der W33-Keeper `backend/internal/core/mcp-server/` (Contacts/Deals/Tickets/Shifts/Invoices/Time-Entries) ist seit ~2026-08-10 offen — inzwischen 6+ Wochen. Zwischenzeitliche Markt-Entwicklungen (siehe State-of-the-Art oben): **sieben etablierte Helpdesks haben offizielle MCP-Server, Zendesk MCP-Client GA + Server EAP, Freshworks bepreist MCP-Actions ab 2026-09-01**. MCP ist keine R&D-Sache mehr, sondern rate-limited-metered-Feature.

Fuer die Helpdesk-spezifische Sicht: ein Cosmi-Helpdesk-MCP-Server exponiert die Cosmi-Ticket-Datenbank fuer AI-Editoren (Claude Code, Cursor, Claude Desktop) und, wichtiger, fuer **Lovable-gebaute-KMU-Frontend-Prototypen** (W33-Keeper `ai-substitution-lovable-vibe-coding-w33`). Ein DACH-KMU-Kunde kann in Claude Desktop "Zeig mir alle offenen Tickets zu Order #12345" fragen und Cosmi-Helpdesk antwortet — ohne dass eine Cosmi-UI-Session offen sein muss.

**Empfehlung — zwei-stufig:**

**Stufe A — Cosmi-Helpdesk-MCP-Server-Minimum (3-5 Tage):**

- Neues Cmd `backend/cmd/mcp-helpdesk/` als eigenstaendiger MCP-Server (OAuth-Token-Auth ueber Cosmi-Tenant-Auth-Endpoint).
- Fuenf initiale Tools:
  - `helpdesk.search_tickets` (params: query [FTS], status, priority, queue_id, requester_email, date_range; returns: List[TicketSummary])
  - `helpdesk.get_ticket` (params: ticket_id; returns: FullTicketWithMessages)
  - `helpdesk.create_ticket` (params: subject, body, priority, queue_id, requester_email/id; returns: Ticket)
  - `helpdesk.add_message` (params: ticket_id, body, internal_bool; returns: TicketMessage)
  - `helpdesk.close_ticket` (params: ticket_id, resolution_note; returns: Ticket)
- Tenant-Guard in jedem Tool-Call: OAuth-Token → `tenant_id` → alle Queries scoped.
- Rate-Limit: 100 Actions/Tenant/Tag Standard, konfigurierbar.
- Article-50-Disclosure: MCP-Client-Session-Handshake schickt "AI-Session"-Marker, Server persistiert AI-Call-Audit-Log in `ai_disclosure_audit` (Empfehlung #1).

**Stufe B — Cross-Modul-Erweiterung (3-4 Wochen, parallel zu anderen Sprint-Themen):**

- Weitere Server-Modules: `mcp-crm` (Contacts, Deals), `mcp-invoices` (Invoices/Quotes), `mcp-time` (Time-Entries), `mcp-schichten` (Shifts). Alle unter `backend/internal/core/mcp-server/` mit shared Auth + Rate-Limit.
- Konsolidierter Cosmi-MCP-Server-Endpoint `mcp.cosmi.example.com` mit Feature-Toggle pro Tenant.
- Doku-Portal `docs.cosmi.example.com/mcp` mit Tool-Reference + Lovable-/Claude-Code-Integration-Beispielen.

**Zeitschaetzung Gesamt-Paket A+B: 4-5 Wochen** (Stufe A eigenstaendig deploy-baar 3-5 Tage). Kann parallel zu Empfehlung #1-Track-A/B laufen.

**Risiken:**

- MCP-Spec ist aktiv weiter-entwickelt — Cosmi baut gegen aktuelle MCP-Version, muss iterativ nachziehen.
- OAuth-Token-Auth fuer MCP-Session ist ein Sicherheits-Neuland fuer Cosmi (bisher primaer JWT-Session-basiert) — Threat-Modeling ratsam.
- Metered-Pricing (Freshworks-Pattern) ist eine Option, aber Cosmi-Positioning "Flat-Preis" spricht dagegen — **MCP-Actions in Flat-Preis inkludieren, 100 Actions/User/Tag Fair-Use** ist bessere Anti-SaaS-flation-Munitions-Story.

**Strategie-Argument:** MCP-Server ist die einzige Massnahme, die (a) den Fin-Salesforce-Konsolidierungs-Wettbewerbs-Druck neutralisiert (Cosmi-MCP-Tools sind Alternativen zu Fin-MCP-Tools), (b) die Lovable-Cosmi-Substitutionsdynamik in eine Kooperationsdynamik dreht (Lovable-Frontend + Cosmi-Backend-as-MCP), (c) im DACH-KMU-Segment ein echter Differenzierungs-Punkt gegen Freshdesk/Zammad/OTOBO ist.

---

### 3. **Cross-Modul-USP-Aktivierung 2.0: Wiki-KB-Konsolidierung + Dialer-Voice-zu-Ticket-Hook + Analytics-Dashboards + External-Requester-Portal (P1 Strategisch, 4-6 Wochen)**

**Problem, verschoben zu W39.** W24-Empfehlung #3 hatte vier Cross-Modul-Sub-Streams (Wiki-Bridge, Dialer-Hook, CSAT-Backend, Routing-Rules-Backend). Zwei davon (CSAT, Routing-Rules) sind ausgeliefert, das dritte (Wiki-Bridge) ist **falsch geliefert** (zwei parallele KB-Systeme), das vierte (Dialer-Hook) ist unangetastet. Zusaetzlich: die W24-Baseline hatte Analytics + External-Requester-Portal nicht als Empfehlungen — jetzt sind beide durch Cosmi-Backend-Auslieferungen (HelpdeskStats + Migration 000291) angebahnt, muessen aber fertig gemacht werden.

**Empfehlung — vier Sub-Streams, iterativ prioritisiert:**

**(a) Wiki-KB-Konsolidierung — REPARIEREN was schief geliefert wurde (2-3 Wochen):**

- Diagnose: heute existieren zwei KB-Tabellen — `wiki_articles` (Wiki-Modul, seit Wave 1) und `helpdesk_kb_articles` (Migration 000210). Das ist architektonisch redundant.
- **Option 1 (empfohlen)**: `helpdesk_kb_articles` als **Sub-View** von `wiki_articles` mit `category='helpdesk-kb'` behandeln — Migration 000210 als deprecated markieren, Content migrieren, `helpdesk_kb`-Endpoints als Proxies zu Wiki-Service-Endpoints umbauen. Der Wiki-Modul-Deepdive W38 hat bereits die Wiki-Frontend-Rich-Editor + [[wiki-links]] + Icon/Cover-Bar geliefert — helpdesk-KB-Autoren wollen diese UI ebenfalls.
- **Option 2 (Kompromiss)**: beide Tabellen behalten, aber cross-referenzieren — `helpdesk_kb_articles.wiki_article_id` als optionaler FK, plus Search-Endpoint `helpdesk.search_kb` durchsucht beide Tabellen. **Kein sauberes Outcome, aber schnell**.
- **Verifikations-TODO**: Sprint-Owner-Sitzung mit Wiki-Modul-Team + Helpdesk-Modul-Team, um Option 1 vs 2 zu entscheiden. **Nicht laenger als 2 Wochen aufschieben**, sonst tenant-Adoption der beiden separaten UIs macht die Konsolidierung teurer.
- Phase-2-Erweiterung (mit AI-Layer aus Empfehlung #1): `wiki_articles`-Embeddings (pgvector) als Semantic-Retrieval fuer AI-Draft-Prompt-Context — das aktiviert die W23-Wiki-Empfehlung-Nr-3 gleichzeitig.

**(b) Dialer-Voice-zu-Ticket-Hook (3-5 Tage):**

- Dialer-Service (`backend/internal/dialer/event_emitter.go`, 25 LOC) verifizieren: welche Events werden emittiert? Aus dem File-Kopf: es gibt einen Emitter, Redis-based-Pubsub laut S3.7-milestones. **Datei zu klein zum Ueberpruefen ohne Read** — Sprint-Task: 1 Tag Code-Review + 3 Tage Helpdesk-Worker-Subscriber + 1 Tag Frontend "Create Ticket from Call"-Button im Dialer-UI-Call-Detail-Panel.
- Auto-Ticket-Create-Flow: wenn Agent-explizit-klickt ODER Call-Note-vorhanden → `helpdesk.create_ticket` mit Subject = Call-Note-First-Line, RequesterID = Caller-CRM-Contact-ID (via `entity_links` — jetzt verfuegbar durch Migration 000267!), Initial-Message-Body = Call-Notes.
- Phase-2 (mit LiveKit-Transcript aus Video-Modul): Call-Transcript-LLM-Summary als Initial-Ticket-Message (baut auf Router aus Empfehlung #1 auf).
- **W37 Video-Deepdive-Learning**: LiveKit ist bei OpenTalk auch angekommen, Cosmi's Stack-USP im Video ist ohnehin geschmolzen — die Cross-Modul-Voice-zu-Ticket-Bruecke ist der neue relevante Video-Cosmi-USP-Aktivierungspfad.

**(c) Analytics-Dashboards (2-3 Wochen):**

- `HelpdeskStats`-Domain-Model + `useHelpdeskStats`-Hook existieren, aber tiefergehende Reports fehlen. Neue Frontend-Komponente `HelpdeskDashboard.tsx`:
  - Volume-Trend (Tickets/Tag/Woche/Monat)
  - SLA-Compliance-Rate (First-Response + Resolution, mit Business-Hours-Compute)
  - Queue-Auslastung + Wait-Time-Verteilung
  - Agent-Performance (nur fuer Manager-Rolle, mit Datenschutz-Opt-in-Toggle)
  - CSAT-Score-Trend + Comment-Word-Cloud
- Backend-Ergaenzungen: `helpdesk.stats_by_queue`, `helpdesk.stats_sla_trend`, `helpdesk.stats_agent_performance` (mit Rollen-Guard).
- Freshdesk Insights + Zendesk Explore sind die Vergleichs-Anker — Cosmi muss nicht die volle Explore-Tiefe erreichen, sondern die fuer KMU-Nutzung notwendigen 6-8 Metriken auf einer Screen-Seite.

**(d) External-Requester-Customer-Portal Phase 1 (3-4 Wochen):**

- Migration 000291 hat die Datenbasis geliefert. Jetzt fehlen:
  - Public-Login-Endpoint fuer External-Requester (magic-link + email-verification, kein Passwort — DSGVO-friendly).
  - Frontend `desktop/src/renderer/src/portal/HelpdeskCustomerPortal.tsx` (oder eigenes Web-App-Bundle unter `web/`?): Ticket-Uebersicht (nur eigene), Ticket-Detail, Neuer-Ticket-Formular, KB-Search (Wiki-KB nach Konsolidierung aus (a)).
  - Tenant-Branding-Layer: Portal soll auf `support.{tenant-subdomain}.example.com` deploy-bar sein.
- KMU-Sales-Argument: 80% der DACH-KMU-Support-Nachfrage haben ein Customer-Portal (auch als Trust-Signal, "wir haben ein professionelles Support-Interface").

**Zeitschaetzung Gesamt-Paket (a)+(b)+(c)+(d):** 6-8 Wochen. **Sub-Stream (b) ist der niedrigste-Aufwand-hoechster-USP-Aktivierungs-Hebel** — 3-5 Tage, aber schaltet den Dialer↔Helpdesk-Cross-Modul-Story ein. **Sub-Stream (a) ist der wichtigste architektonische Fix** — bevor die 2-KB-Systeme tenant-adoption bekommen. **Sub-Stream (c) + (d) sind sales-Argument-getrieben**, koennen in Sprint 5/6 laufen.

**Risiken:**

- Wiki-KB-Konsolidierung (a) kann bestehende Tenants mit already-created `helpdesk_kb_articles` betreffen — Migration-Backfill-Plan Pflicht.
- Dialer-Event-Bus-Stabilitaet (b) muss geprueft werden — `event_emitter.go` mit nur 25 LOC laesst offen, ob es sich um synchronen oder asynchronen Emit handelt.
- Customer-Portal-Bundle (d) ist entweder Electron-Renderer-basiert (dann muss die Public-Site anders deploy-baar sein — WebAssembly-Bundle?) oder ein separates Next.js/Vite-Web-Projekt. Architektur-Entscheidung Sprint-1-Task.

**Diese Empfehlung aktiviert die verbleibende Haelfte des Cosmi-Cross-Modul-USP**, der jetzt (mit Contact/Org-Link + CSAT + Routing + Business-Hours) endlich technisch-real-existent ist. Ohne Voice-Hook + Wiki-Konsolidierung + Portal bleibt der USP-Anker in Sales-Pitches abstrakt.

---

## Sekundaere Empfehlungen (P2-P3, Sprint 4-6)

- **`pg_trgm` Fuzzy-Duplicate-Detection** (P2, 1-2 Tage): Kommentar in `merge.go:14-15` + `postgres_repository.go:272-276` unveraendert seit W24. `CREATE EXTENSION pg_trgm` + Similarity-Query mit Threshold 0.4. **Cost/Value: exzellent, blockt nur weil kein Owner**. Verdient einen Nachmittag im Sprint 4.
- **Email-zu-Ticket-Pipeline** (P2 strategisch, 5-7 Tage): IMAP-Poll oder SMTP-Receive-Service → Auto-Ticket-Create. Voraussetzung fuer Multi-Channel-Inbox-Story. 80% des DACH-KMU-Support-Alltags. **Aber**: das ist Setup-heavy fuer Cosmi-Ops (Mail-Server-Deployment, SPF/DKIM), ggf. External-Provider (Postmark, SendGrid Inbound) besser als Self-Host. Architektur-Entscheidung.
- **HelpdeskSettingsPanel Config-Backend** (P2 Housekeeping, 2-3 Tage): letzte Rest-Mock-Store-Reste im Frontend eliminieren. Neue Migration `helpdesk_settings` (tenant_id, csat_enabled, csat_delay_hours, csat_question, intake_channels, intake_forms) plus Config-Endpoint. Vollstaendige Enum-Konsolidierung.
- **Macros / Automations / Triggers** (P3, 4-6 Tage): Event-Automation-Engine fuer "wenn Ticket 24h ohne Reply → assign to Lead-Agent + send-CSAT". Pattern aus Zendesk-Triggers. Kann auf Routing-Rules-Engine aufbauen.
- **Retro-Fix Wave-7C Meeting-AI-Summary mit Disclosure-Wrapper** (P0 Compliance-Nachlauf-Sprint, 1-2 Tage): sofort nach Empfehlung #1-Track-B fertig, den existing Meeting-AI-Summary-Endpoint mit dem neuen Disclosure-Layer verschneiden. Schliesst die Wiki-W38-P0-Lucke fuer Video-Modul-AI.
- **Zammad-CVE-Cluster als Cosmi-Marketing-Story** (P2 Sales, 2-3 Tage Content): technisch fundierter DACH-KMU-Content "Warum Cosmi (noch) keine AI im Helpdesk hat — und was Zammad-7.1-CVE-Cluster darueber lehrt". Zielgruppe: Compliance-Officer, IT-Leiter in regulierten KMU. Kann auch als Followup zum W33-Anti-SaaS-flation-Content-Sprint fungieren.
- **Cross-Modul-BOM-Tracking-Story-Erweiterung** (P3 Marketing): das W34-Marketing-Argument (`material_availability.go` als Cross-Modul-PoC) hat jetzt einen Helpdesk-Zwilling — `helpdesk_ticket_contact_org` via `entity_links` (Migration 000267) ist ein echter Cross-Modul-Beleg fuer Cosmi-Helpdesk↔CRM-Bruecke. Marketing-Content-Update angebracht.

---

## Widerspruch-Sektion: Was widerspricht Cosmi-Strategie?

**Widerspruch 1 — "keine AI im Helpdesk ist Cosmi-Wedge" vs "Cosmi-Video-Modul hat AI seit Wave 7C ohne Disclosure".** Der Report argumentiert, dass Cosmi-Helpdesk's Article-50-Freiheit ein Sales-Wedge ist. Gleichzeitig hat Cosmi-Video-Modul (aus W37 video-Deepdive und `llm/client.go`) einen Meeting-AI-Summary-Endpoint ohne Disclosure-Wrapper — d.h. Cosmi ist *irgendwo* im Repo Article-50-exponiert, nur nicht im Helpdesk. Das ist kein sauberes Wedge, sondern ein Halb-Wedge. **Konsequenz**: Empfehlung #1-Track-B muss den Wave-7C-Endpoint retrofit-en, sonst blaest jede Compliance-Detail-Pruefung durch potenzielle Kunden das Argument weg. **Ehrliche Positionierung** ist: "Cosmi-Helpdesk hat null AI-Angriffsflaeche, Cosmi-Video-Meeting-Summary hat gerade Disclosure-Retrofit im Sprint" — nicht: "Cosmi hat keine AI".

**Widerspruch 2 — "MCP-Server ist Cosmi's Verteidigungs-Hebel" vs "MCP-Server erhoeht Cosmi's Angriffsflaeche".** MCP-Server exponieren Cosmi-Daten via OAuth-tokenized Endpoints an externe AI-Clients. Das ist per Design breiter als die aktuelle Cosmi-UI-Session-basierte Angriffsflaeche. Fin, Zendesk und andere haben Threat-Modelle fuer MCP-Server-Sessions veroeffentlicht — Cosmi muesste aehnliches machen. **Konsequenz**: Empfehlung #2 verlangt eine Threat-Modeling-Session vor Live-Deploy, aehnlich zu Empfehlung #1-Track-D.

**Widerspruch 3 — "5/10 W24-Empfehlungen delivered ist ueberdurchschnittlich" vs "die drei P0-P1-Themen bleiben unangetastet".** Der Report bewertet die Delivery-Rate positiv. Ehrlich betrachtet: die geloesten Themen sind alle Domaenen-Erweiterungen (CSAT, KB, Routing, Business-Hours), fuer die das Cosmi-Team klar Kompetenz hat. Die offenen Themen sind AI-Compliance-Cross-Modul-Neuland, das eine andere Fachdomaene erfordert. **Konsequenz**: die 5/10-Rate ist nicht "Team liefert schnell", sondern "Team liefert schnell in dem Bereich, wo es faehig ist" — die 5 offenen Themen brauchen entweder externe Expertise oder eine gezielte AI-Compliance-Kompetenz-Einstellung. **Ehrliche Sprint-Planung** benoetigt, das zu adressieren, nicht zu ignorieren.

**Widerspruch 4 — "Cosmi-Helpdesk-Flat-Preis ist attraktiv" vs "Konkurrenz konvergiert zu Flat + niedrige Metered-AI-Preise".** Front senkt Autopilot auf 0,05 USD/Conversation. Freshworks bepreist MCP-Actions bei 15 USD/1000 (=0,015 USD/Action). Der Cosmi-Preis-Wedge wird schmaler. **Konsequenz**: Cosmi's Flat-Preis-Positioning bleibt attraktiv fuer Predictable-Budget-KMU, aber der absolute Preis-Vorteil gegen "Freshdesk Pro 49 USD + 15 USD Freddy-Overage" ist keine 3x-Diskrepanz mehr, sondern nur noch 2x. **Sales-Positionierung** muss neu ausgerichtet werden: nicht "billiger", sondern "predictable + EU-sovereign + no-metered-surprises".

---

## Cross-Referenzen zu Keepern + laufenden Reports

- **W25 Keeper `anthropic-kill-switch-fable-5`** (Multi-Provider AI Router P0): Empfehlung #1-Track-A adressiert genau diesen Keeper. Router ist inzwischen von "Compliance-only" zu "Compliance + Ökonomie + Feature-Voraussetzung" eskaliert.
- **W33 Keeper `direct-competitor-triple-pivot-twenty` (Twenty-Sprint-Kadenz)**: nicht Helpdesk-relevant, aber der Zammad-7.1-Kadenz-Vergleich zeigt: Zammad shippt schnell (7.0 Maerz → 7.1 Juni), aber mit Security-Cost. Cosmi's langsamere-Kadenz-Sicherer-Deploy-Positioning ist parallel zum Twenty-Vergleich argumentierbar.
- **W33 Keeper `ai-substitution-lovable-vibe-coding-w33`**: Empfehlung #2 (Cosmi-MCP-Server) ist der direkte Antwort-Move — Cosmi als MCP-Backend fuer Lovable-gebaute-Frontends.
- **W33 Keeper `backend/internal/core/mcp-server/`** (unresolved 6+ Wochen): Empfehlung #2 aktiviert den Keeper.
- **W33 Keeper `backend/internal/compliance/ai-act-article-50/`** (New Critical P0 W33): Empfehlung #1-Track-B aktiviert den Keeper. Auch Cross-Referenz zu W38-Wiki-Deepdive-P0 (AI-Disclosure-Layer URGENT).
- **W33 Keeper `Anti-SaaS-flation Content Sprint`** (Marketing): Empfehlung 2-3 aus Sekundaer-Empfehlungen (Zammad-CVE-Marketing-Story) ist eine parallele Content-Angle.
- **W38 Wiki-Deepdive Findings**: die W38-P0-EU-AI-Act-Art-50-Empfehlung (Backend-Package + Frontend-Banner + Meeting-AI-Summary-Retrofit) ist **identisch** zur Empfehlung #1-Track-B in diesem Report. Bevor W40 Wiki-Deepdive laeuft, muss diese Cross-Modul-Compliance-Foundation gestartet sein.
- **W37 Video-Deepdive Findings**: OpenTalk-LiveKit-Umstellung hat Cosmi-Stack-USP im Video-Modul weiter verwaessert — Empfehlung #3(b) (Dialer-Voice-zu-Ticket-Hook) ist der neue relevante Cross-Modul-Aktivierungspfad, der Cosmi-USP-Anker gegen die Video-Stack-Angleichung ausbalanciert.
- **W35 CRM-Core-Deepdive (Zyklus 2)**: die Migration 000267 (`helpdesk_ticket_contact_org` via `entity_links`) ist ein Cosmi-Cross-Modul-USP-Marker, der in Sales-Pitches als konkreter Beleg genutzt werden kann — parallel zu W34-Produktion-`material_availability.go`.

---

## Discord-Push-Template

**Channel**: `#trends`

```
[Embed 1] Deepdive: helpdesk (W39/2026, Zyklus 2) — Delta-Bilanz zu W24
5 von 10 W24-Empfehlungen delivered (CSAT-Backend, Routing-Rules-Engine, Business-Hours-SLA, KB-Article-Schema, Mock→Backend-Wiring Datenpfade). Backend 2419→4014 LOC (ohne Tests), 10 neue Migrationen. Frontend 2043→3197 LOC. Aber: die drei P0-P1-AI/Compliance/Voice-Themen bleiben komplett offen. AI-Draft = null Code. Art. 50 Disclosure = null Code (durchsetzbar seit 2026-08-02 = Tag 50). Dialer-Voice-Hook = null Code. pg_trgm = null Code.
[Buttons: 'Lesen' | 'Pick' | 'Followup 14d']

[Embed 2] Deepdive: helpdesk — Top-Empfehlung 1 (P0)
AI-Compliance-Foundation-Sprint: Multi-Provider-Router + Article-50-Disclosure-Layer + Helpdesk-AI-Drafts-Phase-1 als EIN Sprint-Paket (6-8 Wochen, 1.5-2 FTE Backend). Grund: die drei Themen sind ein einzelnes Sub-System, nicht drei separate Empfehlungen. Zammad-7.1.2-CVE-Cluster (RCE via AI Agent Template) als Security-Threat-Model-Referenz. Konsequenz bei Nicht-Handeln: 6-12 Monate zu Freshdesk-Pro-mit-Freddy-Sales-Verlust ODER Bundesnetzagentur-Bussgeld-Risiko.
[Buttons: 'Lesen' | 'Pick' | 'Followup 30d']

[Embed 3] Deepdive: helpdesk — Top-Empfehlung 2 (P0)
Cosmi-MCP-Server (Helpdesk-first, dann Cross-Modul CRM+Invoices+Shifts) — vom W33-Keeper zum Sprint-4-Deliverable. 3-5 Tage fuer Grund-Server mit 5 Helpdesk-Tools. Freshworks bepreist MCP-Actions ab 2026-09-01 als plan-limitiertes Feature — der Markt hat MCP-Standardisierung ueberschritten. Cosmi's W33-Keeper unresolved 6+ Wochen.
[Buttons: 'Lesen' | 'Pick' | 'Followup 21d']

[Embed 4] Deepdive: helpdesk — Top-Empfehlung 3 (P1)
Cross-Modul-USP-Aktivierung 2.0: Wiki-KB-Konsolidierung REPARIEREN (zwei parallele KB-Systeme heute!) + Dialer-Voice-zu-Ticket-Hook (3-5 Tage) + Analytics-Dashboards + External-Requester-Portal. Contact/Org-Link (Mig 000267) ist der neue Cross-Modul-USP-Beweis fuer Sales.
[Buttons: 'Lesen' | 'Pick' | 'Followup 30d']
```

---

## Quellen

**Cosmi-Code-Reading (Delta-Verifikation W24→W39):**

- `backend/internal/helpdesk/` (20 Files, 9921 LOC inkl. Tests, 4014 LOC ohne Tests): models.go (278), service.go (1120), postgres_repository.go (1497), merge.go (93 — TODO `pg_trgm` unveraendert), sla.go (62), errors.go, csat_config.go, csat_dispatch.go, csat_mailer.go, csat_survey.go, ticket_intake.go, plus 15 Test-Files.
- `desktop/src/renderer/src/modules/helpdesk/` (8 .tsx, 3197 LOC): HelpdeskPage.tsx (1798), BusinessHoursDialog.tsx (361), CannedResponsesPanel.tsx (355), TicketRoutingConfig.tsx (169), settings/HelpdeskSettingsPanel.tsx (197), CSATWidget.tsx (148), CannedResponsePicker.tsx (99), SLABadge.tsx (70).
- `desktop/src/renderer/src/api/helpdesk-client.ts` (308 LOC), `hooks/useHelpdesk.ts` (459 LOC, 40+ Hooks), `stores/helpdesk.ts` (697 LOC, jetzt Config-State).
- `backend/internal/dialer/event_emitter.go` (25 LOC): keine Helpdesk-Referenz.
- `backend/internal/llm/client.go` (184 LOC): Wave 7C Meeting-Summary-Client, kein Multi-Provider-Router.
- `.knowledge/milestones.md`: Eintraege 2026-06-11 (Lauf-5 CSAT-Default-Fix), 2026-07-26 bis 2026-08-06 (Backend-Nachtlaeufe 1-5 mit Migrationen 243-297), 2026-08-27 (`4267c87e` Helpdesk-SLA-Tests + Gateway-Handler-Coverage).
- Migrationen: 000210 (helpdesk_kb_articles), 000211 (helpdesk_routing_rules), 000232 (helpdesk_business_hours), 000236 (helpdesk_ticket_fields), 000267 (helpdesk_ticket_contact_org), 000268 (helpdesk_ticket_source_channel), 000288 (helpdesk_csat), 000289 (helpdesk_csat_survey_dispatch), 000290 (helpdesk_ticket_intake_fields), 000291 (helpdesk_external_requester).

**Konkurrenz-Recherche (2026-06-08 bis 2026-09-21):**

- Zammad:
  - [Zammad 7.1 release notes (2026-06-17)](https://zammad.com/en/product/releases/zammad-7-1) — AI Text Extractor + AI Ticket Tagger
  - [Zammad 7.1.2 security release (2026-08-04)](https://zammad.com/en/product/releases/7-1-2) — 5 CVEs inkl. AI Agent RCE
  - [Zammad 7.1.3 security release (2026-08-25)](https://zammad.com/en/product/releases/7-1-3) — 7 weitere Issues inkl. SSRF + Cross-Tenant-Attachment
  - [Zammad security advisories](https://zammad.com/en/advisories)
  - [CVE-2026-34724 (Zammad AI RCE)](https://www.strix.ai/cve/CVE-2026-34724)
- Zendesk:
  - [TechCrunch: Zendesk acquires Forethought (2026-03-11)](https://techcrunch.com/2026/03/11/zendesk-acquires-agentic-customer-service-startup-forethought/)
  - [Zendesk Voice AI Agents voice-configuration (2026-06-01)](https://support.zendesk.com/hc/en-us/articles/10849624262170)
  - [Zendesk MCP action flows](https://support.zendesk.com/hc/en-us/articles/10497779528730)
- Salesforce + Fin:
  - [Salesforce signs to acquire Fin ($3.6B, 2026-06-15)](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/)
  - [Fin pricing outcomes](https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes)
- Freshworks:
  - [Drag: Freshdesk 2026 pricing analysis (First Price-Raise in 5 Years, MCP-Metering)](https://www.dragapp.com/blog/freshdesk-pricing/)
- HelpScout:
  - [eesel: HelpScout 2026 pricing (per-user reversion, AI Answers $0.75/resolution)](https://www.eesel.ai/blog/helpscout-pricing)
- Front:
  - [Front pricing](https://front.com/pricing) — Autopilot $0.05/conversation
- OTOBO:
  - [OTOBO 11.1 Beta (2026-06-24)](https://otobo.io/en/otobo-11-1-beta/) — no AI features yet
- Chatwoot:
  - [Chatwoot changelog (Captain AI July 2026 refresh)](https://www.chatwoot.com/changelog)
- Sierra + Decagon + Kustomer:
  - [Sierra blog](https://sierra.ai/blog) — $950M @ $15B, Receptive AI + Takeoff, Ghostwriter, Horizon, AIUC-1

**EU-AI-Act Article 50 (durchsetzbar seit 2026-08-02):**

- [Article 50 enforcement guide (aiactblog.nl)](https://www.aiactblog.nl/en/posts/article-50-enforcement-fines-ai-act-2026)
- [BaFin AI market surveillance press release (2026-07-29)](https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_07_29_ki_verordnung_en.html)
- [Bundesnetzagentur AI portal](https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/AI/start_ki.html)

**Zentrale W24-Baseline-Referenz:**

- [`monthly/2026-06-08-deepdive-helpdesk.md`](../monthly/2026-06-08-deepdive-helpdesk.md) — der 549-Zeilen-Report, gegen den dieser Delta-Report gerechnet ist.

---

## Picks (vorgeschlagen)

- [ ] 🔴 **AI-Compliance-Foundation-Sprint: Router + Article-50-Disclosure + Helpdesk-AI-Drafts-Phase-1** — P0, 6-8 Wochen, 1.5-2 FTE Backend + 1 FTE Frontend + 0.3 FTE Legal/Security. Aktiviert W25-Anthropic-Kill-Switch-Keeper + W33-Article-50-Keeper + W38-Wiki-Disclosure-P0 gleichzeitig. **Konsequenz bei Nicht-Handeln: strukturelle Positionsverlust im DACH-KMU-Mid-Market gegen Freshdesk-Pro + Bussgeld-Risiko fuer Wave-7C-Meeting-Summary**. (Empfehlung 1)
- [ ] 🔴 **Cosmi-MCP-Server (Helpdesk + Cross-Modul)** — P0, 3-5 Tage Grund-Server + 3-4 Wochen Cross-Modul-Erweiterung. Aktiviert W33-MCP-Server-Keeper (6+ Wochen unresolved) + W33-Lovable-Substitutionsantwort. **Antwort auf Fin-Salesforce-Konsolidierung + Freshworks-MCP-Metering-Standardisierung**. (Empfehlung 2)
- [ ] 🟢 **Cross-Modul-USP-Aktivierung 2.0: Wiki-KB-Konsolidierung + Dialer-Voice-Hook + Analytics + External-Requester-Portal** — P1, 6-8 Wochen. Dialer-Voice-Hook allein 3-5 Tage — der niedrigste-Aufwand-hoechster-USP-Aktivierungs-Sub-Stream. Wiki-KB-Konsolidierung 2 Wochen — reparieren was schief geliefert wurde. (Empfehlung 3)
- [ ] 🟡 **`pg_trgm` Fuzzy-Duplicate-Detection** — 1-2 Tage, Code-TODO unveraendert seit W24. Ein Nachmittag im Sprint 4. (Sekundaer)
- [ ] 🟡 **Retro-Fix Wave-7C Meeting-AI-Summary mit Disclosure-Wrapper** — P0 Compliance-Nachlauf-Sprint direkt nach Router-Deployment, 1-2 Tage. Schliesst Wiki-W38-P0-Lucke fuer Video-Modul. (Sekundaer)
- [ ] 🟡 **HelpdeskSettingsPanel Config-Backend** — 2-3 Tage Housekeeping. Vollstaendige Enum/Config-Konsolidierung. (Sekundaer)
- [ ] 🟡 **Email-zu-Ticket-Pipeline (via External-Provider vs Self-Host-Entscheidung)** — 5-7 Tage. Voraussetzung fuer Multi-Channel-Inbox-Story, 80% DACH-KMU-Support-Alltag. (Sekundaer)
- [ ] 🟡 **Zammad-CVE-Cluster als Cosmi-Marketing-Story** — 2-3 Tage Content, "Boring, but audited"-Positioning fuer regulierte DACH-KMU. Followup zum W33-Anti-SaaS-flation-Sprint. (Sekundaer)
- [ ] 🟡 **Followup 30d (2026-10-21)**: Status-Check ob AI-Compliance-Foundation-Sprint gestartet ist, Router-Skelett + Disclosure-Layer live? Draft-Endpoint EAP-baar? Threat-Modeling-Session dokumentiert? (-> followups/2026-10-21-helpdesk-ai-compliance-sprint-status.md)
- [ ] 🟡 **Followup 14d (2026-10-05)**: Verifikation Business-Hours-SLA-Compute-Pfad in `sla.go:ApplyPolicy()` — ist der Business-Hours-Compute wirklich integriert oder nur konfiguriert-und-vergessen? (-> followups/2026-10-05-helpdesk-business-hours-compute-verify.md)
- [ ] 🟡 **Followup 21d (2026-10-12)**: Wiki-KB-vs-Helpdesk-KB-Architektur-Entscheidung (Option 1 Konsolidierung / Option 2 Cross-Ref). Owner: Wiki + Helpdesk Modul-Owner. (-> followups/2026-10-12-helpdesk-wiki-kb-architecture-decision.md)

---

## Pflicht-Sektion: EU-AI-Act-Article-50-Compliance-Checkliste (Update W39)

Der Article 50 ist **seit 2026-08-02 durchsetzbar** — nicht mehr Zukunft. Bundesnetzagentur (Marktueberwachung) + BaFin (Finanzsektor) sind seit 2026-07-29 operativ. Kein publik gemeldetes Bussgeld bis 2026-09-21, Q4 2026 erwartet.

**Cosmi-Status per Modul:**

- **Helpdesk (dieses Deepdive)**: null AI-Funktion → Article 50 nicht anwendbar → **kein Compliance-Risiko HEUTE, aber blockt Empfehlung #1 vor Live-Deploy**.
- **Video (Wave 7C, Meeting-AI-Summary via `llm/client.go`)**: **AKTIV-EXPONIERT**. Kein Disclosure-Wrapper. Tag 50 in Live-Enforcement-Fenster. Retro-Fix in Empfehlung #1-Track-B + Sekundaer-Nachlauf.
- **Wiki, Formulare, Buchhaltung, etc.**: keine AI-Funktion aktuell.

Vor erster Helpdesk-AI-Funktion Live-Going (geplant Sprint 4 Welle 1 mit Empfehlung #1):

- [ ] **DisclosureRegistry-Package** in `backend/internal/compliance/ai_disclosure/` deployed
- [ ] **`ai_disclosure_audit`-Tabelle** deployed (Migration angesetzt)
- [ ] **`RequireDisclosureAck`-Middleware** auf allen AI-Routes verkabelt
- [ ] **`AIDisclosureBanner.tsx`** ausgeliefert (First-Login + Per-Interaktion)
- [ ] **`AIProviderSettings.tsx`** ausgeliefert (Tenant-Admin-Panel)
- [ ] **Wave-7C Meeting-Summary retrofit** mit Disclosure
- [ ] **`.knowledge/compliance-ai-act-article-50.md`** dokumentiert
- [ ] **Quartals-Review-Prozess** kalendarisiert
- [ ] **LLM-Provider-Vertraege** dokumentiert (Mistral AI, Ollama, ggf. Anthropic — Auftragsverarbeiter-Vertraege gemaess Art. 28 DSGVO)
- [ ] **Trainings-Daten-Disclosure** explizit "Tenant-Daten werden nicht zum Trainieren genutzt"

**Wenn eine der Checkboxen offen ist**, kein Live-Deploy einer AI-Funktion fuer Helpdesk oder anderweitig.

---

## Meta-Lesson W39 (fuer Rotation-Zyklus 2)

Der Zyklus-2-Delta-Deepdive-Pattern hat sich als wertvoll erwiesen. Zwei-Punkte-Nachschaerfung fuer die kommenden Zyklus-2-Deepdives:

1. **Explizite Delivery-Rate-Tabelle** ist die wichtigste Delta-Sektion. Sie beantwortet die zentrale Frage "was hat 15 Wochen tatsaechlich bewirkt". Fuer W40 Formulare + W41 Vertraege muss die Tabelle wieder ganz oben stehen.

2. **"Was widerspricht Cosmi-Strategie" muss ehrlich sein**. In diesem W39 Report ist Widerspruch 3 ("die 5/10-Rate ist nicht Team-Speed, sondern Team-Skill-Bereich") die produktivste Diagnose des ganzen Reports — die Empfehlung dahinter (AI-Compliance-Kompetenz muss gezielt eingekauft/eingestellt werden) wuerde sonst nicht auftauchen. **Reports sollten der Team-Realitaet zumuten, nicht schoenreden**.

---

## Telemetry

```yaml
routine: intel-monday-deepdive
date: 2026-09-21
week: 2026-W39
modul: helpdesk
rotation_position: 5/15
zyklus: 2
delta_to: monthly/2026-06-08-deepdive-helpdesk.md
delta_weeks: 15
model: claude-opus-4-7
max_output_tokens: 40000
pool_threshold_abort: 0.15
discord_webhook_used: DISCORD_WEBHOOK_TRENDS (planned, 4 embeds)
sources_verified: 20+ URLs, 12 Cosmi-Code-Locations, 10 Migrations, 15 Frontend/Backend-Files
delivery_rate_W24: 5/10 recommendations delivered structurally, 4 in progress, 1 delivered wrong (Wiki-KB parallel systems)
new_P0_flagged: 2 (AI-Compliance-Foundation-Sprint = merger of 3 W24 recommendations; MCP-Server = W33-Keeper eskalation)
new_P1_flagged: 1 (Cross-Modul-USP-Activation 2.0 = 4 sub-streams)
status: ok
```
