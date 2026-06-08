---
year: 2026
week: 24
modul: helpdesk
created: 2026-06-08
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 47
tokens_input: ~270000
tokens_output: ~14800
rotation_position: 5/15
---

# Deepdive: helpdesk (Mo W24/2026)

> **Fuenfter Deepdive der Rotation.** Vorgaenger: `crm-core` (W19, 2026-05-11), `dialer` (W20, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01). Naechstes Modul gemaess Rotation: **formulare** (KW25, 2026-06-15). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-Helpdesk (2026-06-08):** Backend `backend/internal/helpdesk/` (9 Files, **2419 LOC** mit ~824 Test-LOC, Coverage 39.3%, **seit S1.4 done 2026-04-18**). 22 gRPC-RPCs hinter `modules.helpdesk`-Flag (default-OFF), 5 Domain-Models (Ticket, TicketMessage, TicketQueue, CannedResponse, SLAPolicy), SLA-Engine (24/7 simpel, **kein Business-Hours-Compute** trotz `business_hours JSONB`-Slot), Ticket-Merge via ILIKE-Prefix-Match (kein pg_trgm). Tenant-Isolation-Tests Phase 2+3 vorhanden. Frontend `desktop/src/renderer/src/modules/helpdesk/` (7 .tsx, **2043 LOC**, HelpdeskPage.tsx 996 LOC). **Strukturelle Diskrepanz #1:** HelpdeskPage.tsx importiert **`useHelpdeskStore` aus `stores/helpdesk.ts` (MOCK_TICKETS, MOCK_CATEGORIES, MOCK_KB_ARTICLES, MOCK_CANNED_RESPONSES, MOCK_ROUTING_RULES, MOCK_BUSINESS_HOURS, MOCK_HOLIDAYS)** — die TanStack-Query-Hooks (`useHelpdesk.ts`, 316 LOC, 28 Hooks) + Client (`helpdesk-client.ts`, 198 LOC) existieren, **werden aber von der UI nicht konsumiert**. **Strukturelle Diskrepanz #2:** Status-Enums driften zwischen Backend (`open/pending/solved/closed/merged`) und Frontend (`open/in_progress/waiting/resolved/closed`); Priority-Enums driften zwischen Backend (`low/normal/high/urgent`) und Frontend (`low/medium/high/critical`). **Strukturelle Diskrepanz #3:** Backend kennt keine KB-Articles (Wissensdatenbank-Tab im Frontend ist 100% Mock), kein CSAT-Schema (CSATWidget rendert Frontend-only), kein Routing-Rules-Schema (`TicketRoutingConfig` ist UI-Stub), keine Email-zu-Ticket-Pipeline.

> **Leit-Signal der Woche:** Drei Schockwellen kollidieren binnen 90 Tagen im Customer-Service-Software-Markt — (a) **Outcome-Based Pricing wird 2026 das neue Default-Modell**: Zendesk AI Agents auf $2/Resolution (vs zuvor per-Seat-Add-on), Intercom Fin $0.99/Outcome, Front Autopilot $0.89/Resolution, Freshdesk Freddy AI sessions $49/100 (~$0.50/Session) — Per-Seat-Anteil im SaaS-Markt kollabiert von 21% auf 15% in 12 Monaten (Bessemer-Atlas-Daten, Mai 2026), Hybrid (Base+Overage) ist neues Standard-Pattern mit 41% Adoption. (b) **AI-Helpdesk-Funktionen sind Tabellenstake**: Zammad 7.0 (4. Maerz 2026) brachte **AI-Summaries + Writing-Assistant + AI-Agents** mit Wahl-LLM-Provider (Zammad-AI EU-GDPR / OpenAI / Anthropic / Azure / Mistral / Ollama / Custom) zu €0.03/AI-Call — auch der DACH-Open-Source-Anker hat damit das Feature-Floor angehoben. Freddy/Copilot/Fin/Autopilot beanspruchen 67–80% Auto-Resolution. (c) **EU-AI-Act Article 50 in Kraft ab 2. August 2026**: Helpdesk-Chatbots fallen **NICHT** unter die "offensichtlich"-Ausnahme — explizite AI-Disclosure-UI ist Pflicht vor First-Message. Cosmi-Helpdesk hat heute **null AI-Funktion**, das ist heute Compliance-frei und morgen die zentrale Aufholbaustelle. **Dazu Sicherheitssignal:** Zammad 7.0.1 (8. April 2026) musste binnen **5 Wochen** nach AI-Launch eine Security-Release schieben mit **SSTI->RCE via AI Agent**, "Improper Access Control in AI Assistance Controller", SSRF-via-Webhooks, Missing-Auth in Ticket-Create. Lesson fuer Cosmi: AI-Endpoints sind Angriffsflaeche-Multiplikator, nicht nur Feature-Aufholbaustelle. **Dieser Bericht empfiehlt drei Pflicht-Stakes vor jeder AI-Helpdesk-Integration.**

---

## State-of-the-Art

Der Helpdesk-Markt Mitte 2026 ist nicht mehr "Zendesk vs Freshdesk vs Self-Host" — er ist **dreigleisig**: (1) **AI-Agent-First-Cloud** (Zendesk + AI Agents, Intercom Fin, Front Autopilot, Freshdesk Freddy AI, Kustomer, Decagon, Sierra), (2) **Co-Pilot-First-Cloud** (HelpScout AI Drafts, Front Copilot, Zendesk Copilot — Mensch im Loop, AI nur als Reply-Assistant), (3) **EU-Sovereign-Self-Host mit AI-Beimischung** (Zammad 7.0 mit Wahl-LLM, OTOBO mit Klassifikations-AI, Chatwoot). Cosmi-Helpdesk sitzt heute **in keiner dieser Kategorien** — Cosmi ist KMU-ERP-Modul mit Ticket+SLA+Queues+Canned-Responses, ohne AI-Layer, ohne Multi-Channel-Inbox, ohne KB-Backend. Das ist Architektur-Greenfield in einem Markt, der gerade jeden Monat eine Erwartungslinie verschiebt.

Drei strukturelle Veraenderungen treiben den Markt seit Februar 2026:

(a) **Outcome-Based Pricing entwertet Per-Seat-Helpdesk-Lizenzen.** Zendesk hat 2026 von "AI Agents pro Seat" auf **$2/successfully resolved ticket** umgestellt — der Standard-Tarif, mit Volumendiscount fuer Enterprise. Intercom Fin: **$0.99/Outcome** (Outcome = Customer-bestaetigt oder kein Eskalations-Wunsch), Voice + Vision + MCP/Connectors zu Shopify/Salesforce/Stripe/Jira. Front Autopilot: **$0.89/Resolution**. Freshdesk Freddy AI: 500 Sessions inklusive in Pro ($49/User-mo), danach **$49/100 Sessions (~$0.50)**. HelpScout AI Drafts: **$50/100 AI-Drafts** (anders gerechnet, weil Co-Pilot statt Auto-Resolver). Per-Seat-Anteil im SaaS-Markt: **21% -> 15% in 12 Monaten** (Bessemer Atlas Mai 2026), Hybrid (Base+Overage) ist neues Mehrheits-Pattern (41% Adoption). **Konsequenz fuer Cosmi-KMU-Pricing**: 4 EUR/Modul/User/Monat ist heute der KMU-attraktive Anker, **aber** die Konkurrenz pitcht jetzt "zahl-pro-AI-Resolution, nicht pro-Agent". Cosmi-Helpdesk-Module-Preis ohne AI-Layer wird in 6-12 Monaten als "alte Welt" wahrgenommen, **wenn nicht ein klares AI-Add-on-Pricing-Modell** (z.B. KMU-friendly: €0.20/AI-Draft, €0.50/AI-Resolution, EU-LLM-Provider Pflicht) jetzt entworfen wird — auch wenn der Service erst Q4 2026 / Q1 2027 lebt.

(b) **AI-First ist Tabellenstake.** Vor 12 Monaten war "AI Suggested Reply" das premium Add-on — heute ist es das Floor. Zammad — der DACH-Open-Source-Anker — hat **am 4. Maerz 2026 mit 7.0** AI-Features zum ersten Mal in den Standardbetrieb gebracht: AI-Summaries (Customer-Intent + Discussion-Points + Open-Questions + Next-Steps in einem Block), Writing-Assistant (Grammar/Tone/Expand/Simplify), **AI-Agents** (Auto-Routing, Auto-Categorizing, Auto-Titling — alles im Hintergrund), mit Wahl unter **7 LLM-Providern**: Zammad-AI (EU-Hosted, GDPR-konform), OpenAI, Anthropic Claude, Azure AI, Mistral AI, Ollama (lokal), Custom (OpenAI-Compatible). Preis: **€0.03/AI-Call**, AI als Add-on in Professional-v2/Plus-v2. Damit hat **der wichtigste Open-Source-DACH-Konkurrent das AI-Feature-Floor angehoben** — Cosmi-Helpdesk kann heute nicht mehr mit "wir sind Open-Source-DACH-Alternative" pitchen, ohne zumindest eine **AI-Wahl-Provider-Architektur** zu skizzieren. Cloud-Konkurrenten gehen weiter: Freddy AI Pro bringt **Sentiment-Analyse mit Auto-Priority-Update** (Negative Sentiment -> Priority=Urgent automatisch), Zendesk Voice AI Agents handhaben Telefon-Calls vollstaendig, Intercom Fin Voice + Vision macht Multimodal (Screenshots, Receipts, broken UI-States als Input).

(c) **EU-AI-Act Article 50 trifft am 2. August 2026 jeden Helpdesk-Chatbot.** Per European Commission Draft Guidelines (Mai 2026, finale Code-of-Practice erwartet Juni 2026): Helpdesk-Chatbots **qualifizieren NICHT** fuer die "obvious"-Ausnahme — selbst wenn der Bot offensichtlich als Chat dargestellt ist, ist ein expliziter **AI-Disclosure** vor dem ersten Interaktions-Schritt Pflicht. Disclosure-UI muss vor der ersten Nachricht erscheinen, dokumentier-/auditbar, mit Faehigkeit den Customer-Wechsel zu menschlichem Agent jederzeit zu triggern. **Praktische Implikation fuer Cosmi**: jede AI-Helpdesk-Funktion ab heute MUSS mit Disclosure-Schicht ausgeliefert werden — sonst Article-50-Bussgeld-Risiko (bis zu 15 Mio EUR oder 3% Welt-Umsatz). Cosmi hat einen **strukturellen Vorteil**, weil noch keine AI-Funktion existiert: Cosmi kann Disclosure-by-Design einbauen, bevor die erste AI-Funktion live geht. Konkurrenten haben die Disclosure-UI nachruesten muessen (Zendesk + Zammad muessen rueckwirkend ihre 2024-2025-Cloud-AI-Releases auditen).

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Zendesk (international, threat: HIGH als Markt-Standard, medium fuer DACH-KMU Direkt-Sale)**

Zendesk ist nicht direkter DACH-KMU-Konkurrent (US-Hosting, Cloud-only, Pricing-Eskalation), aber **das Feature-Erwartungs-Referenzmodell** — jeder Helpdesk-Buyer im DACH-Mittelstand sieht zumindest Zendesk-Demo, bevor er KMU-Alternative kauft.

- **AI Agents Outcome-Pricing**: $2 / erfolgreich aufgeloestes Ticket (Standard), Volumen-Discount Enterprise. Anspruch: bis zu 80% Chat-/Email-Deflection ohne menschlichen Agent.
- **AI Copilot**: $50/Agent/Monat als Add-on; Suite + Copilot Professional $155/Agent (annual), Suite + Copilot Enterprise $209/Agent. Liefert AI-Summaries, Suggested Replies (aus historischer Resolution), Drafts, Tone-Adjustment.
- **Voice AI Agents** — vollstaendige Telefon-Call-Aufloesung ohne Agent.
- **G2/Capterra-Pain-Points 2026**: "Pricing eskaliert schnell wenn echte Bedarfe kommen", "Storage-Surprises", "Add-on-Costs", "AI-Outcome-Pricing unpredictable", "Copilot $50 ist all-or-nothing (kein Select-User-Tarif)".
- **Pricing-Basis**: Suite Team $19, Suite Growth $55, Suite Professional $115, Suite Enterprise $169 / User / Monat (annual). Copilot + AI-Agents on top.
- **Gap zu Cosmi**: AI Copilot komplett, AI Agents komplett, Voice AI, Multi-Channel-Inbox (Email/Chat/Voice/Social), Sentiment-Analyse, Self-Service-KB-Backend, Analytics, Macros, Triggers, Automations.
- **Strategischer Hinweis**: **Cosmi gewinnt nicht ueber "AI besser als Zendesk"** — Zendesk hat 18+ Monate Vorsprung und Outcome-Pricing-Glaubwuerdigkeit. **Cosmi gewinnt ueber "Helpdesk-in-CRM-in-Dialer-in-Wiki-in-Rechnung im KMU-Preis-Sweet-Spot"**: Ticket wird aus Dialer-Call auto-erstellt, referenziert CRM-Deal, verlinkt auf Wiki-Knowledge-Artikel, generiert Rechnung-Position bei Resolution. Das ist Cosmi-USP, Zendesk kann das strukturell nicht. **Aber:** AI-Drafts MUESSEN ab Q1 2027 verfuegbar sein, sonst greift der "Cosmi-fuehlt-sich-nicht-modern-an"-Effekt.

**2. Freshdesk + Freddy AI (Freshworks, international, threat: HIGH im DACH-KMU)**

Freshdesk ist der **direkteste Preis-Konkurrent** fuer Cosmi-Helpdesk im DACH-KMU-Segment. Growth-Tier $15/Agent/Monat deckt 90% der SMB-Bedarfe ab.

- **Freddy AI Agent** — automatisierte Chat/Email-Resolution, Sentiment-Analyse mit Auto-Priority-Update (negative-tone -> urgent), Suggested-Replies, Ticket-Thread-Summaries, KB-Content-Generation. **In Pro ($49/User) und Enterprise ($79/User) inklusive**, mit 500 Free Sessions im Pro-Tier, danach $49/100 Sessions (~$0.50/Session).
- **Freddy Copilot** — Agent-Assist, $29/Agent/Monat Add-on (annual). Drafts, Tone-Adjust, Refine, KB-Suggestions.
- **G2/Capterra-Pain-Points 2026**: "Email-Notification-Probleme + Formatting-Issues", "Pricing fuer Advanced-Features steigt schnell", "Reporting-Features komplex", "advanced features only in higher tiers".
- **Pricing**: Free Tier (bis 2 Agents, Email+KB), Growth $15, Pro $49 (Freddy AI Agent inkl), Enterprise $79 / User-Monat (annual).
- **Tech-Stack**: Cloud-only, AWS-Hosting (EU-Region verfuegbar fuer DACH-Compliance), Multi-Channel (Email, Chat, Social, Phone).
- **Gap zu Cosmi**: Freddy AI Agent komplett, Sentiment-Analyse, Multi-Channel-Inbox, Phone-Integration (Freshcaller-Bundle), Mobile Apps, Analytics-Dashboards, Customer-Portal, Public-Self-Service-KB.
- **Strategischer Hinweis**: **Freddy AI Pricing-Bundle ist das wichtigste Anti-Cosmi-Pattern**: "Pro $49/User incl AI Agent, 500 Sessions free" — fuer einen 10-Agent-KMU sind das **$490/Monat all-in mit AI**. Cosmi muss in DACH-Sales-Pitch zeigen: "Cosmi-Helpdesk 4 EUR + Cosmi-Dialer 6 EUR + Cosmi-CRM 8 EUR = 18 EUR/User x 10 Agents = 180 EUR — und Du behaeltst Self-Host-Daten in Frankfurt." Das ist die richtige Pitch-Folie. **Aber:** AI-Drafts/Sentiment-Analyse muessen in 2026-H2 Roadmap auftauchen, sonst geht der Preis-Vergleich an Freshdesk verloren ("$49 Pro mit AI vs Cosmi ohne AI").

**3. Zammad 7.0 (Open-Source + Cloud, DACH-Anker, threat: HIGH als Architektur- und Sales-Konkurrent)**

Zammad ist Cosmis **naechster direkter Architektur-Konkurrent im DACH-Open-Source-Helpdesk-Markt**. G2-Rating 4.6, "High Performer" im Helpdesk-Segment. Released **7.0 am 4. Maerz 2026** — erstmals AI-Features im Standardbetrieb.

- **AI-Summaries** (Customer-Intent + Discussion-Points + Open-Questions + Recommended-Next-Steps).
- **Writing Assistant** (im Editor: Grammar-Fix, Tone-Adjust, Expand-Drafts, Simplify-Complex).
- **AI Agents** (im Hintergrund: Auto-Routing, Auto-Categorizing, Auto-Titling).
- **7 LLM-Provider-Wahl** (Pflicht-Pattern!): Zammad AI (EU-Hosted, GDPR-konform), OpenAI, Anthropic Claude, Azure AI, Mistral AI, Ollama (lokal Self-Host), Custom (OpenAI-API-Compatible — Google Gemini, etc).
- **AI-Add-on Preis**: **€0.03/AI-Call** — sehr KMU-freundlich, kein Per-Seat-AI-Add-on.
- **Speicher**: Plus-v2 jetzt 150 GB statt 50 GB (Anfang 2026 v2-Plan-Update).
- **CRITICAL SECURITY LESSON 7.0.1 (8. April 2026)** — binnen 5 Wochen nach 7.0-Launch wurden gefixt: **SSTI -> RCE via AI Agent**, "Improper Access Control in AI Assistance Controller", **SSRF via Webhooks**, "Missing Authorization in Ticket Create Endpoint", CSRF in OAuth-Callbacks, Origin-Validation in SSO, "Information Disclosure in Ticket Detail View", "Improper Neutralization of HTML Tags in Ticket Articles".
- **G2/Capterra-Pain-Points 2026**: "Performance-Probleme bei hoher Ticket-Volumina", "API faehig aber begrenzt fuer komplexere Setups", "Lokalisierungs-Qualitaet variabel je Sprache", "keine echten AI-Agents (Resolution autonom) — alles Co-Pilot, finale Antwort vom Menschen".
- **Pricing**: Self-Host Community kostenlos (AGPL-3.0); Hosted Starter v2 / Professional v2 (€16-€18/Agent/Monat) / Plus v2; Self-Hosted-Subscription mit "Self-Service" / "On-Premise" Support-Modellen.
- **Gap zu Cosmi**: AI-Features (Summaries/Writing-Assist/AI-Agents) komplett, 7-LLM-Provider-Wahl-Architektur, Multi-Channel (Email, Chat, Phone via Sipgate-Integration, Twitter, Facebook, Telegram), Customer-Portal, Knowledge-Base-Backend, Mobile-Apps, On-Prem-Air-Gap-Doku.
- **Strategischer Hinweis (WICHTIGSTER PUNKT DIESES REPORTS):** **Zammad 7.0 ist das richtige Vorbild fuer Cosmi-Helpdesk-AI-Architektur.** Die 7-LLM-Provider-Wahl-Architektur (EU-Hosted GDPR + Big-3-Cloud + Local-Ollama + Custom) ist das **DACH-KMU-Compliance-Pattern**, das Cosmi 1:1 adoptieren muss. Cosmi-Postgres-Stack laesst sich **pgvector** + **Ollama-Local-Inference** ohne neuen DB-Service direkt aktivieren — gleiches Architektur-Tooling wie Wiki-Empfehlung. **Cosmi-Differenzierung gegen Zammad**: Helpdesk-IM-Cosmi-ERP-Module-Bundle (Ticket triggert Dialer-Call-Schedule, referenziert CRM-Deal, verlinkt Wiki-Article) — Zammad ist Standalone-Helpdesk, kein ERP-Modul. **WARNUNG**: Zammads 7.0.1-CVE-Cluster zeigt: **AI-Features sind Angriffsflaeche-Multiplikator** (SSTI -> RCE!). Cosmi-AI-Helpdesk-Phase-1 MUSS mit pen-test-equivalentem Audit + Threat-Modeling starten. Insbesondere: alle AI-Eingabe-Templates und LLM-Prompt-Slots als untrusted-Input behandeln (Server-Side-Template-Injection), AI-Webhook-Egress whitelisten (SSRF-Schutz).

**4. Intercom + Fin (international, threat: medium fuer DACH-KMU — Markt-Erwartungs-Setter)**

Intercom ist seit Q4 2024 das **AI-Agent-Resolution-Marktdominanz-Standardmodell**. Fin reportet **40+ Millionen aufgeloeste Conversations** und **67% Resolution-Rate ueber 30 Tage** (Dezember 2025-Daten).

- **Fin AI Agent** — Outcome-Based: **$0.99/Outcome** (egal welcher Intercom-Plan). "Outcome" = Customer-bestaetigte-Resolution ODER Customer-Exit-ohne-Eskalations-Wunsch. **Nie Charge fuer Failed-Procedures** oder explizite Human-Handover-Requests.
- **Fin Procedures** — Natural-Language-Workflows fuer Multi-Step-Operations mit Tool/Data-Connector-Use. Ersetzt das alte "Tasks"-Konzept.
- **Fin Voice** — Voice-Input fuer Telefon-AI-Agent.
- **Fin Vision** — Image-Input (Screenshots, Receipts, broken-UI-States als Customer-Input).
- **MCP / Data-Connectors** — Shopify, Salesforce, Stripe, Jira, etc. — Fin ist Action-Taking-Agent, nicht nur Knowledge-Bot.
- **Pricing-Basis**: Essential $39, Advanced $99, Expert $139 / Seat / Monat. **Fin standalone** als Add-on auf existierender Stack via API (auch ohne Intercom-Helpdesk: $0.99/Outcome).
- **Gap zu Cosmi**: Action-Taking-AI-Agent (Cosmi koennte aehnliche-Pattern bauen mit Cosmi-Modul-MCP-Server), Voice + Vision, MCP-Connectors-Bibliothek, Procedures-NL-Workflows.
- **Strategischer Hinweis**: **Intercom Fin ist das richtige Vorbild fuer Cosmi-Helpdesk-AI-Resolution-Pricing-Modell**: pay-per-outcome ist KMU-attraktiv (kein Risiko, kein Up-Front). Cosmi sollte fuer eigene-AI-Resolution-Phase ein **€0.50/Resolution-Modell** evaluieren (Half-Price-Anker gegen $0.99) — angebunden an EU-LLM-Provider-Wahl. **Fin-MCP-Connectors-Pattern (Shopify/SF/Stripe/Jira)** ist ein wichtiger Markt-Signal: Action-Taking-Agents sind die naechste Welle. Cosmi koennte als MCP-Server selbst auftauchen (Cosmi-Helpdesk-Tools fuer Claude-Code/Cursor) — das wuerde die Cosmi-Helpdesk-Daten in Developer-Tools-Workflow integrieren.

**5. HelpScout AI Drafts (international, threat: low — Architektur-Vorbild fuer Co-Pilot-First)**

HelpScout ist **NICHT** direkter DACH-KMU-Cosmi-Konkurrent (US-Markt-Fokus, Englisch-Sprach-Optimierung), aber **Architektur-Vorbild fuer Co-Pilot-First-Pattern** (Human im Loop, AI als Reply-Helper).

- **AI Drafts** — GPT-5.1-basiert, generiert vollstaendige Reply-Drafts aus historischen Conversations + Docs-KB-Articles. Agent reviewed, personalisiert, sendet.
- **GDPR-Compliant**, "no data shared to train OpenAI models" (Opt-Out Default), strict access controls.
- **Pricing**: **$50/100 AI-Drafts** (in 100er-Increments billable), Max-Monthly-Spending-Limit konfigurierbar.
- **Verfuegbar**: In Plus + Pro Plans, in contact-based-billing-Plans inklusive.
- **Gap zu Cosmi**: AI-Drafts mit historischem-Conversation+KB-Training, GPT-5.1-Quality-Bar, Docs-KB-Integration als Trainings-Datenbasis.
- **Strategischer Hinweis**: **HelpScout-Pattern (Co-Pilot statt Auto-Resolver) ist der KMU-Compliance-friendliche-Pfad** — kein autonomes AI-Action, also weniger Article-50-Risiko, weniger Mis-Resolution-Risk. **Cosmi-Helpdesk-Phase-1 (Q4 2026 / Q1 2027) sollte mit AI-Drafts-Only starten** (nicht direkt Auto-Resolution). Disclosure: "AI-generated draft, review before send" als Agent-UI-Hint. Trainings-Basis: tenant-eigene historische Tickets + Wiki-Articles (Cross-Modul-Hebel — siehe Wiki-Deepdive).

**6. Front + Autopilot (international, threat: medium — Inbox-First-Pattern)**

Front ist im DACH-KMU-Mittelstand bei Email-affinen-Teams (Agenturen, Consulting, B2B-Service) verbreitet, oft als Shared-Inbox-Tool statt klassischem-Helpdesk eingefuehrt.

- **AI Suite** — Topics (Auto-Categorization), Copilot (Reply-Drafting), **Autopilot (Omnichannel-AI-Agent, $0.89/Resolution)**, Smart QA (Conversation-Scoring ohne Manual-Scorecards), Smart CSAT (Satisfaction-Inference ohne Survey).
- **Native Knowledge-Connectors (neu 2026)** — Notion, Google Drive, Confluence direkt anbindbar. AI nutzt Knowledge-where-it-lives.
- **Pricing**: Starter $25, Professional $65, Enterprise $105 / Seat / Monat. AI-Suite: Copilot $20/Seat, Smart QA $20/Seat, Smart CSAT $10/Seat (alles Add-ons; Enterprise = Suite inkl). **Autopilot Resolutions billed at $0.89**.
- **Gap zu Cosmi**: Inbox-First-Pattern (vs Ticket-First), Smart QA / Smart CSAT (Conversation-Scoring ohne Manual-Survey — wichtig!), Native-KB-Connector-Architektur (Notion/GDrive/Confluence), Voice-Channel.
- **Strategischer Hinweis**: **Smart-CSAT (Satisfaction-Inference ohne Survey)** ist das KMU-Quick-Win-Feature, das Cosmi adoptieren sollte — Cosmi-CSATWidget rendert heute nur Frontend-Survey-UI ohne Backend-Scoring. **Smart-QA** (Conversation-Quality-Scoring) ist ein Differenzierungs-Hebel: AI auditieren-Conversation und scoren-Quality fuer Manager-Reports. Beide Features benoetigen Sentiment-Analyse + LLM-Summarization — passend zum spaeteren Cosmi-Helpdesk-AI-Stack. **KB-Connector-Pattern** (Notion/GDrive/Confluence native) zeigt Markt-Erwartung: Helpdesk-AI braucht Knowledge-Quelle — Cosmi-Wiki-Module ist die Quelle, aber Integration muss explizit gebaut werden (Wiki-Article-Embeddings als Helpdesk-AI-Context).

**7. OTOBO + OTRS (DACH-Open-Source, threat: low — Legacy-Konkurrent)**

OTOBO ist die Open-Source-Community-Fortsetzung von OTRS (Rother OSS, Bayern). DACH-orientiert, deutsche-Doku, Enterprise-Heritage.

- **OTOBO 11** — in Entwicklung (Stand Mai 2026), neue Settings, Performance-Optimierungen, Partner-Solution-Integration.
- **AI Plugin** — Klassifikation + Priorisierung von Tickets (Konfuzio-Integration). Nicht so weitreichend wie Zammad-7.0.
- **Architektur**: Perl-Backend, Datenbank-agnostisch (MySQL/Postgres), klassisches-Ticket-Modell mit Queue/SLA/Templates.
- **Pricing**: Community-Edition kostenlos, Enterprise-Support-Subscription.
- **G2/Capterra-Position**: niedrigerer Trust-Score (5/10 in Sources.yaml), kleinere User-Base als Zammad, gilt als "Legacy"-Helpdesk.
- **Gap zu Cosmi**: nicht primaer relevant — Cosmi-Helpdesk sollte OTOBO nicht aktiv-imitieren (Perl-Backend, klassische-Ticket-Welt).
- **Strategischer Hinweis**: **OTOBO ist relevant als Sales-Funnel-Quelle**: bestehende OTRS-/OTOBO-DACH-Nutzer evaluieren Modernisierungs-Alternativen. Cosmi-Helpdesk-Sales-Pitch sollte "OTRS-Modernisierung mit KMU-ERP-Integration" als spezifische-Funnel-Zielgruppe behandeln. **Marketing-Angle**: "OTRS hat Sie 10 Jahre lang ge-ticket-trackt — Cosmi ticket-trackt UND verbindet zu CRM/Dialer/Wiki/Rechnung."

### Markt-Mega-Trends (Mai/Juni 2026)

- **Outcome-Based Pricing**: $0.89-$2.00/Resolution-Pricing wird Marktstandard. Per-Seat-SaaS kollabiert 21% -> 15% in 12 Monaten (Bessemer Atlas Mai 2026). Hybrid (Base + Overage) bei 41% Adoption. **AI-Customer-Service-Markt projiziert auf $15.12 Milliarden in 2026** (Zendesk-Estimate: bis zu 80% Auto-Resolution-Rate).
- **EU-AI-Act Article 50 (2. August 2026)**: Helpdesk-Chatbots Pflicht-Disclosure vor First-Interaction. Code-of-Practice finale Juni 2026.
- **LLM-Provider-Wahl-Architektur**: Zammad-7.0-Pattern (7 Provider) wird das DACH-KMU-GDPR-Compliance-Pattern. Cosmi muss aehnliche Architektur planen.
- **Action-Taking-Agents via MCP**: Intercom-Fin / Zendesk-AI-Agents / Front-Autopilot fuehren MCP-/Data-Connector-Patterns ein. Action-Taking statt nur Knowledge-Retrieval ist die naechste Phase.
- **Co-Pilot vs Auto-Resolver**: HelpScout/Front-Copilot setzen Human-in-Loop-Pattern fort, waehrend Zendesk/Intercom Auto-Resolution treiben. **Beide Pfade haben Markt-Validierung** — KMU-Cosmi-Phase-1 sollte Co-Pilot starten (weniger Compliance-Risk, weniger Mis-Resolution-Risk).
- **Sicherheit von AI-Endpoints**: Zammad-7.0.1-CVEs (SSTI->RCE via AI, SSRF via Webhooks, Missing-Auth) zeigen: AI ist Angriffsflaeche-Multiplikator. Threat-Modeling Pflicht vor Launch.

---

## Cosmi-IST-Stand

Stand 2026-06-08, Reading `backend/internal/helpdesk/` (9 Files, 2419 LOC) + `desktop/src/renderer/src/modules/helpdesk/` (7 Files, 2043 LOC) + `desktop/src/renderer/src/api/helpdesk-client.ts` (198 LOC) + `desktop/src/renderer/src/api/hooks/useHelpdesk.ts` (316 LOC, 28 Hooks) + `desktop/src/renderer/src/stores/helpdesk.ts` (254 LOC, Mock-Store).

**Backend (Production-ready, S1.4 done seit 2026-04-18, Coverage 39.3% laut milestones):**

- **5 Domain-Models** (`models.go`, 127 LOC):
  - `Ticket`: UUID-PK, tenant_id, subject, status, priority, assignee_id (nullable), requester_id, queue_id (nullable), due_at (nullable), merged_into_id (nullable), first_response_at (nullable), resolved_at (nullable), created_at, updated_at.
  - `TicketMessage`: ticket_id FK, author_id, body, internal bool, attachments []string, created_at.
  - `TicketQueue`: name, default_assignee_id (nullable), sla_policy_id (nullable).
  - `CannedResponse`: name, body.
  - `SLAPolicy`: name, first_response_mins, resolution_mins, business_hours `map[string]any` (**Schema-Slot vorhanden, NICHT compute-genutzt**).
- **Status-Enum (Backend)**: `open`, `pending`, `solved`, `closed`, `merged`. Validation-Map in `ValidTicketStatuses`.
- **Priority-Enum (Backend)**: `low`, `normal`, `high`, `urgent`. Validation-Map in `ValidTicketPriorities`.
- **SLA-Engine** (`sla.go`, 62 LOC):
  - `ApplyPolicy`: due_at = now + first_response_mins (wenn FirstResponseAt nil), sonst now + resolution_mins. **24/7-Annahme** — keine Business-Hours-Subtraktion, obwohl `business_hours JSONB` im SLAPolicy-Modell existiert. TODO-Kommentar im Code: "future implementation can subtract non-business minutes from the window".
  - `ComputeStatus`: `breached` (now >= due_at), `at_risk` (now >= due_at - 20% window), `on_track` (else).
- **Duplicate-Detection + Merge** (`merge.go`, 89 LOC):
  - `DetectDuplicates`: ILIKE-Prefix-Match auf ersten 5 Worten des Subjects, scoped auf gleichen Requester. **Kommentar: "If pg_trgm is enabled in the DB, replace with a similarity query for better fuzzy results."** — pg_trgm NICHT aktiviert.
  - `MergeTickets`: validiert source != target, source != bereits-merged, target existiert. Reassigned alle Messages source->target, setzt source.status='merged' + source.merged_into_id=targetID.
- **Service-Layer** (`service.go`, 623 LOC): CreateTicket, GetTicket, ListTickets (pagination, status-filter), UpdateTicket, CloseTicket, ReopenTicket, AssignTicket, MergeTickets, AddMessage, ListMessages, CreateQueue/UpdateQueue/DeleteQueue/ListQueues, CreateCannedResponse/.../ListCannedResponses, CreateSLAPolicy/.../ListSLAPolicies, ApplySLAPolicy, GetSLAStatus.
- **Repository** (`postgres_repository.go`, 536 LOC): Postgres-Backend, parametrisiert auf `tenantID` in allen Query-Funktionen.
- **Multi-Tenant-Isolation Tests** (`tenant_isolation_phase2_test.go` + `tenant_isolation_phase3_test.go`, 79+64 LOC): Sprint-2-R2-Compliance + Sprint-3-RLS-Compliance.
- **HTTP-Gateway-Route**: `gateway/route_helpdesk.go` — 22 RPCs als REST mapped, hinter `modules.helpdesk`-Feature-Flag. (Default-OFF, Tenant-spezifisches Opt-In.)
- **Feature-Flag-State** (2026-06-08): Default-OFF, Tenants muessen `modules.helpdesk=true` explizit setzen.
- **gRPC-Tenant-Inbound-Interceptor**: `helpdesk_grpc.go` hat Tenant-ID-Parsing aus 13 Proto-Requests (W2D-C-Sweep, Mai 2026 — siehe milestones).

**Frontend (Desktop Electron, 7 .tsx-Files, 2043 LOC):**

- `HelpdeskPage.tsx` (996 LOC): 3-Tabs (`tickets` / `wissensdatenbank` / `statistik`), Ticket-List + Detail-View + Reply-Composer, importiert **`useHelpdeskStore` aus `@/stores/helpdesk`** (Zustand-Mock-Store). Status-Filter, Priority-Filter, Category-Filter. RichTextEditor-Reply, useAIStore-Import (AI-Scaffolding-Hook), Bot-Lucide-Icon.
- `SLABadge.tsx` (69 LOC) + `SLABreachBanner`: Visualisierung SLA-Status, ueber Mock-Store-Status-Felder.
- `CSATWidget.tsx` (140 LOC) + `CSATAggregate`: Frontend-only CSAT-Survey-UI — **keine Backend-CSAT-Tabelle**, Werte landen im Mock-Store.
- `CannedResponsesPanel.tsx` (316) + `CannedResponsePicker.tsx` (106): CRUD-UI fuer Templates, aktuell ueber Mock-Store. **Backend-CannedResponse-Service existiert, aber Frontend ruft ihn nicht.**
- `BusinessHoursDialog.tsx` (270): Konfiguration von Arbeitszeiten + Feiertagen. **Backend hat `business_hours JSONB`-Slot, aber SLA-Engine nutzt ihn nicht — Konfiguration landet ins Vakuum.**
- `TicketRoutingConfig.tsx` (146): Routing-Rules-UI. **Backend hat KEIN Routing-Rules-Schema**, der Dialog speichert nur in Mock-Store.

**Status-Enum-Frontend** (in `stores/helpdesk.ts`): `'open' | 'in_progress' | 'waiting' | 'resolved' | 'closed'`.
**Priority-Enum-Frontend**: `'low' | 'medium' | 'high' | 'critical'`.

**Cross-Layer-Wiring vorhanden (aber nicht aktiv):**

- `api/helpdesk-client.ts` (198 LOC): typed fetch-wrapper, BASE = `/api/v1/helpdesk`, listTickets/getTicket/createTicket/updateTicket/closeTicket/reopenTicket/assignTicket/mergeTickets/listMessages/addMessage/listQueues/.../listSLAPolicies/applySLAPolicy/getSLAStatus.
- `api/hooks/useHelpdesk.ts` (316 LOC, 28 TanStack-Query-Hooks): useTicketsQuery, useTicketQuery, useCreateTicketMutation, useMessagesQuery, useAddMessageMutation, useQueuesQuery, useCannedResponsesQuery, useSLAPoliciesQuery, useSLAStatusQuery, etc.
- `api/helpdesk-types.ts`: TypeScript-Types parallel zu Backend-models.go — **abweichend in Status/Priority-Enums** (siehe Diskrepanz #2 oben).

**Wissensdatenbank-Tab im HelpdeskPage** (Tab `wissensdatenbank`): rendert `MOCK_KB_ARTICLES` aus `stores/helpdesk.ts`. **Es existiert KEINE Wiki-Integration**, obwohl Cosmi-Wiki-Modul mit Tags / Categories / FTS-Search seit S1.1 done ist (siehe Wiki-Deepdive 2026-06-01). **Cross-Modul-Backlink-Hebel "Helpdesk-Tab nutzt Wiki-Articles"** ist offen — die strategisch wichtigste Integration steht implementations-seitig auf Null.

**Pricing-Position** (geschaetzt aus Cosmi-Modul-Pricing-Linie, real-zu-verifizieren in `docs/PRICING.md`):

- Helpdesk: vermutlich **4 EUR/Modul/User/Monat** vs Freshdesk Pro $49 (mit AI), Zendesk Suite Team $19, Zammad Professional v2 ~€16-18. **Cosmi ist heute der billigste Player im Markt, aber ohne AI** — ein **Strategie-Risiko**, wenn der Markt 2026/2027 vollstaendig auf Outcome-Pricing umschwenkt.

**Was Cosmi-Helpdesk HAT (Highlights):**

- ✅ Multi-Tenant-Isoliert (Sprint-2-R2 + Sprint-3-RLS-Phase3 Compliance-Tests)
- ✅ SLA-Engine mit at_risk-Threshold (20% Warn-Window)
- ✅ Ticket-Merge mit Message-Reassign
- ✅ Duplicate-Detection (Subject-Prefix-Match)
- ✅ Queues (Routing-Bucket-Schema)
- ✅ Canned Responses (Backend-Schema + Service)
- ✅ Status-Lifecycle: open/pending/solved/closed/merged (mehr nuanciert als Frontend-Variante)
- ✅ Priority-Lifecycle: low/normal/high/urgent
- ✅ Erste-Response-Tracking (first_response_at) + Resolution-Tracking (resolved_at)
- ✅ Internal-Notes (TicketMessage.internal bool)
- ✅ Attachments-Liste (TicketMessage.attachments []string)
- ✅ Feature-Flag-isoliert (Default-OFF, sicherer Rollout)
- ✅ Tenant-Inbound-gRPC-Interceptor (W2D-C-Sweep, Mai 2026)
- ✅ Frontend-Client + TanStack-Hooks existieren (28 Hooks, 316 LOC) — Wiring-bereit, aber nicht aktiv

**Was Cosmi-Helpdesk NICHT HAT (Stand 2026-06-08):**

- ❌ **Frontend-Mock->Backend-Wiring** — HelpdeskPage konsumiert `useHelpdeskStore`-Mock, nicht TanStack-Hooks. **Single biggest gap**, vergleichbar zur Wiki-Mock->Backend-Migration.
- ❌ **Status-Enum-Sync Frontend<->Backend** — `in_progress/waiting/resolved` (Frontend) vs `pending/solved` (Backend). Type-Mismatch ist seit S1.4 (April 2026) im Code.
- ❌ **Priority-Enum-Sync Frontend<->Backend** — `medium/critical` (Frontend) vs `normal/urgent` (Backend).
- ❌ **Business-Hours-SLA-Compute** — Schema-Slot da (`SLAPolicy.BusinessHours map[string]any`), `ApplyPolicy` ignoriert es ("24/7-Annahme" Code-Kommentar).
- ❌ **pg_trgm Fuzzy-Dup-Detection** — heute nur ILIKE-Prefix-Match (Code-Kommentar: "replace with similarity query").
- ❌ **KB-Article-Backend** — Frontend-Wissensdatenbank-Tab ist 100% Mock. Wiki-Modul existiert, **Cross-Modul-Bridge fehlt komplett**.
- ❌ **CSAT-Backend** — CSATWidget rendert Frontend-only, keine Persistierung.
- ❌ **Routing-Rules-Schema** — TicketRoutingConfig-UI-Dialog speichert in Mock.
- ❌ **Email-zu-Ticket-Pipeline** — kein Mail-Receiver-Service erkennbar. Tickets entstehen nur via API-Create.
- ❌ **Voice-zu-Ticket** — Cosmi-Dialer-Modul existiert (S3.7), aber **kein Auto-Ticket-aus-Call-Hook**.
- ❌ **Multi-Channel-Inbox** — kein Chat, SMS, Social, Twitter, Telegram, WhatsApp.
- ❌ **AI-Drafts / AI-Reply-Suggestion** — null AI-Funktion, keine Embeddings, kein LLM-Call.
- ❌ **AI-Summaries** — kein Ticket-Thread-Summary.
- ❌ **AI-Auto-Triage** — keine Topic-Klassifikation, keine Auto-Queue-Zuordnung.
- ❌ **Sentiment-Analyse** — kein Auto-Priority-Update bei Negative-Tone.
- ❌ **LLM-Provider-Wahl-Architektur** — kein EU-LLM-Provider-Slot, kein Ollama-Local-Hook, kein OpenAI-API-Compatible-Adapter.
- ❌ **pgvector / Semantic-Search** — keine Wiki-Article-Embedding-Quelle fuer AI-Context.
- ❌ **EU-AI-Act-Article-50-Disclosure-UI** — heute nicht noetig (kein AI), aber Pflicht ab erster AI-Funktion.
- ❌ **Customer-Portal / Public-Self-Service-Front-End** — kein Self-Service-Login, keine Public-KB.
- ❌ **Public-Status-Page** — kein Cosmi-Pendant zu statuspage.io.
- ❌ **Macros / Triggers / Automations** — Backend hat keine Automation-Engine fuer Helpdesk-Events.
- ❌ **Analytics-Dashboards** — keine Helpdesk-Reports (Volume, Resolution-Time, SLA-Compliance).
- ❌ **CSAT-Inference / Smart-CSAT** (Front-Pattern) — Survey-only.
- ❌ **Smart-QA / Conversation-Scoring** (Front-Pattern) — kein Quality-Audit.
- ❌ **MCP-Server-Integration** — kein Cosmi-Helpdesk-MCP-Tools fuer Claude-Code/Cursor.
- ❌ **Mobile-Helpdesk-Editor** — Cosmi-Mobile-App noch nicht im Helpdesk-Modul-Routing.
- ❌ **SCIM-Provisioning** — User-Sync fuer Enterprise-Kunden.
- ❌ **Audit-Trail / Compliance-Log** — keine Helpdesk-Action-Log-Tabelle erkennbar.
- ❌ **Anti-Spam-Filter / Trusted-Sender-Whitelist** — keine Email-Pre-Filter-Schicht.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Zendesk (Suite+AI) | Freshdesk (Pro+Freddy) | Zammad 7.0 (Plus v2+AI) | Intercom + Fin | HelpScout (Pro+AI Drafts) | Front (Pro+AI Suite) |
|---|---|---|---|---|---|---|---|
| Ticket-Lifecycle (Status-Engine) | ✅ 5-State | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| SLA-Engine (First-Resp + Resolution) | ✅ 24/7 only | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Business-Hours SLA-Compute** | ❌ Slot da, kein Compute | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Queue-Routing (Manual) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI-Auto-Triage (Topic / Routing)** | ❌ | ✅ AI Agents | ✅ Freddy | ✅ AI Agents (auto-route+categorize+title) | ✅ Fin | 🚧 limitiert | ✅ Topics |
| Canned Responses / Macros | ✅ Schema | ✅ Macros | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI-Drafts / Suggested Replies** | ❌ | ✅ Copilot | ✅ Freddy Copilot | ✅ Writing Assistant | ✅ Fin | ✅ AI Drafts (GPT-5.1) | ✅ Copilot |
| **AI-Summaries (Thread-Summary)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Sentiment-Analyse / Auto-Priority** | ❌ | ✅ | ✅ Negative->Urgent | 🚧 | ✅ | 🚧 | ✅ Smart CSAT |
| **AI-Resolution autonom (Outcome-billable)** | ❌ | ✅ $2/Res | ✅ $0.50/Session | 🚧 nicht autonom | ✅ $0.99/Out | ❌ Co-Pilot only | ✅ Autopilot $0.89/Res |
| **EU-LLM-Provider-Wahl-Architektur** | ❌ | ❌ US-LLM | ❌ US-LLM | ✅ 7-Provider | ❌ | ❌ | ❌ |
| **Local-LLM (Ollama) Self-Host-Option** | ❌ | ❌ | ❌ | ✅ Ollama | ❌ | ❌ | ❌ |
| **EU-AI-Act-Art-50-Disclosure-UI (Aug 2026 Pflicht)** | n/a (kein AI) | 🚧 Audit | 🚧 Audit | 🚧 Audit | 🚧 Audit | 🚧 Audit | 🚧 Audit |
| Ticket-Merge / Duplicate-Detection | ✅ ILIKE-Prefix | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **pg_trgm Fuzzy-Dup-Detection** | ❌ | n/a | n/a | n/a | n/a | n/a | n/a |
| **Multi-Channel-Inbox (Email+Chat+Voice+Social)** | ❌ Email-Pipe fehlt | ✅ | ✅ | ✅ Email+Chat+Phone+Twitter+FB | ✅ | ✅ Email+Chat | ✅ Email+Chat+SMS |
| **Email-to-Ticket Pipeline** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Voice-to-Ticket (Dialer-Hook)** | ❌ Dialer da, Hook fehlt | ✅ Voice AI | ✅ Freshcaller | ✅ Sipgate | ✅ Fin Voice | ❌ | ✅ |
| **Knowledge-Base-Backend (KB-Article-Schema)** | ❌ Frontend-Mock | ✅ Guide | ✅ | ✅ | ✅ | ✅ Docs | ✅ |
| **Cross-Module Wiki-Article-Embedding als AI-Context** | ❌ Wiki da, Bridge fehlt | n/a | n/a | n/a | n/a | n/a | n/a |
| **Native-KB-Connectors (Notion/GDrive/Confluence)** | ❌ | ✅ | ✅ | ✅ | ✅ Procedures | ✅ Docs | ✅ |
| Internal Notes | ✅ TicketMessage.internal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Attachments | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CSAT-Backend (Survey + Score Persistierung)** | ❌ Frontend-only | ✅ | ✅ | ✅ | ✅ Smart Score | ✅ | ✅ |
| **Smart-CSAT (AI-Inference statt Survey)** | ❌ | 🚧 | 🚧 | ❌ | ✅ | ❌ | ✅ |
| **Smart-QA / Conversation-Scoring** | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Routing-Rules Backend (Auto-Assign) | ❌ Mock-UI only | ✅ Triggers | ✅ | ✅ | ✅ | ✅ | ✅ |
| Macros / Automations / Triggers | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Analytics-Dashboards | ❌ | ✅ Explore | ✅ Insights | ✅ | ✅ | ✅ | ✅ Smart QA |
| Customer-Portal / Public-KB | ❌ | ✅ Guide | ✅ | ✅ | ✅ Help-Center | ✅ Docs Site | ✅ |
| Public-Status-Page (Statuspage-Pendant) | ❌ | 🚧 Partner | ✅ | 🚧 | ✅ Statuspage | ❌ | ❌ |
| **Multi-Tenant-Isolated (Sprint-2/3-Compliance)** | ✅ R2+RLS-Phase3 | n/a (SaaS) | n/a (SaaS) | ✅ self-host | n/a (SaaS) | n/a (SaaS) | n/a (SaaS) |
| **EU-Self-Host (DSGVO-nativ)** | ✅ | ❌ Cloud-only | ❌ Cloud-only | ✅ AGPL | ❌ Cloud-only | ❌ Cloud-only | ❌ Cloud-only |
| Open-Source | ❌ proprietaer | ❌ | ❌ | ✅ AGPL-3.0 | ❌ | ❌ | ❌ |
| MCP-Server / LLM-Tool-Use | ❌ | 🚧 | 🚧 | 🚧 | ✅ Fin MCP-Connectors | ❌ | ❌ |
| Mobile-Helpdesk-App | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| SCIM-Provisioning | ❌ | ✅ Enterprise | ✅ Enterprise | ✅ Plus v2 | ✅ Enterprise | ✅ Enterprise | ✅ Enterprise |
| Audit-Trail / Compliance-Log | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Pricing/Seat (DACH-KMU)** | **~4 EUR Modul** | $19-$169 + AI Add-on | $15-$79 (Pro $49 inkl AI) | €16-18 + €0.03/AI-Call | $39-$139 + $0.99/Out | $25-$65 + $50/100 AI | $25-$105 + AI Add-ons + $0.89/Res |
| **AI-Resolution-Pricing-Modell** | n/a | $2/Resolution | $0.50/Session | €0.03/AI-Call | $0.99/Outcome | $0.50/AI-Draft | $0.89/Resolution |
| **KMU-ERP-Modul-Integration (Helpdesk↔CRM↔Dialer↔Wiki↔Buchhaltung)** | ✅ USP-Anker — implementations-offen | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Markt-Reife / Sales-Track-Record | 🚧 Beta (modules.helpdesk OFF) | ✅ Markt-Standard | ✅ Massmarkt | ✅ DACH-OS-Anker | ✅ Markt-Standard | ✅ Mid-Market | ✅ Inbox-Niche |

**Lesart der Tabelle:**

Cosmi-Helpdesk hat **3 strukturelle Vorteile** (EU-Self-Host, Open-Source-trotz-proprietaer-im-Bundle, Modul-Integration im KMU-ERP) gegen **18+ strukturelle Defizite** (AI-Drafts, AI-Summaries, AI-Triage, Sentiment-Analyse, EU-LLM-Provider-Wahl, Email-Pipeline, Voice-Hook, KB-Backend, CSAT-Backend, Routing-Rules-Schema, Multi-Channel, Business-Hours-SLA-Compute, Customer-Portal, Macros, Analytics, Mobile, SCIM, Audit-Trail). **Der Modul-Integration-Vorteil ist heute NUR ein theoretischer Anker** — die Cross-Modul-Bridge zum Wiki (Helpdesk-Wissensdatenbank-Tab nutzt Wiki-Articles als KB) ist nicht gebaut, die Cross-Modul-Bridge zum Dialer (Voice-Call -> Auto-Ticket) ist nicht gebaut. Das ist die **zentrale Diagnose dieses Deepdives**, identisch zur Wiki-Deepdive-Diagnose: **Cosmi-Helpdesk-USP ist konzeptionell stark, implementationsseitig nicht aktiviert.**

Vier Diskrepanzen-Lager (in absteigender Reihenfolge der Strategie-Schwere):

1. **Frontend-Mock-Store statt TanStack-Hooks** — HelpdeskPage konsumiert `useHelpdeskStore`-Mock, nicht die existenten 28 TanStack-Hooks. Das ist die identische Mock->Backend-Wiring-Schuld wie beim Wiki. **Pflicht-S3-Welle-1-Move.**
2. **Status/Priority-Enum-Drift Frontend<->Backend** — `in_progress/waiting/resolved/medium/critical` (Frontend) vs `pending/solved/normal/urgent` (Backend). **Beim Wiring sofort konsolidieren** — sonst Type-Errors bei jedem ersten API-Call.
3. **KB-/CSAT-/Routing-Rules-Backend-Defizit** — Frontend-UI vorhanden, Backend-Schema-Tabellen fehlen. Drei separate Backend-Schemas-erweitern noetig.
4. **Cross-Modul-Bridge fehlt (Wiki-Quelle / Dialer-Voice-Hook)** — Cosmi-USP wird heute nicht implementations-seitig geliefert.

Zwei Compliance-Lager:

1. **EU-AI-Act-Article-50-Disclosure-UI** — heute nicht noetig (kein AI), aber Pflicht ab erster AI-Funktion. **Disclosure-by-Design vor erstem AI-Feature einbauen.**
2. **Security-AI-Endpoints** — Zammad-7.0.1-CVE-Cluster (SSTI->RCE via AI, SSRF via Webhooks, Missing-Auth) ist ein klares Warnsignal: AI-Endpoints sind Angriffsflaeche-Multiplikator. **Threat-Modeling Pflicht vor AI-Helpdesk-Launch.**

---

## Top-3 Strategische Empfehlungen

### 1. **Frontend-Mock->Backend-Wiring + Enum-Konsolidierung (P0 Pflicht, Sprint 3 Welle 1)**

**Problem**: HelpdeskPage.tsx (996 LOC) konsumiert heute komplett `useHelpdeskStore` aus `stores/helpdesk.ts` (MOCK_TICKETS / MOCK_KB_ARTICLES / MOCK_STATS / MOCK_CATEGORIES / MOCK_CANNED_RESPONSES / MOCK_ROUTING_RULES / MOCK_BUSINESS_HOURS / MOCK_HOLIDAYS) — eine 254-LOC-Mock-Schicht. Die TanStack-Query-Hooks (`useHelpdesk.ts`, 316 LOC, 28 Hooks) + Client (`helpdesk-client.ts`, 198 LOC) existieren bereits seit S1.4-Welle-2 (April 2026), werden aber NICHT von der UI genutzt. Backend ist Production-ready hinter `modules.helpdesk`-Flag.

Zusaetzlich: Status-Enum-Drift (Frontend `in_progress/waiting/resolved`, Backend `pending/solved/merged`) und Priority-Enum-Drift (Frontend `medium/critical`, Backend `normal/urgent`) — Type-Errors garantiert bei erstem echten API-Call.

**Empfehlung**:
- **(a)** `stores/helpdesk.ts` als Mock-Schicht behalten fuer Storybook + Tests, aber HelpdeskPage.tsx umstellen auf TanStack-Hooks. Konkrete Reihenfolge: `useTicketsQuery` (Ticket-Liste), `useTicketQuery(id)` (Detail), `useMessagesQuery(ticketId)` (Replies), `useAddMessageMutation` (Reply senden), `useCreateTicketMutation` (Neuer-Ticket-Dialog), `useAssignTicketMutation`, `useMergeTicketsMutation`, dann Queues + Canned-Responses + SLA-Policies.
- **(b)** Status/Priority-Enums KONSOLIDIEREN: Backend ist autoritativ. Frontend-Typen muessen `pending/solved/merged` + `normal/urgent` adoptieren. UI-Display-Labels koennen via i18n auf "In Bearbeitung" / "Wartend" gemappt werden, aber die Werte sind backend-konform. Migration-Pfad: in `helpdesk-types.ts` umstellen, Type-Errors triagieren in HelpdeskPage.tsx (~30 erwartete Stellen).
- **(c)** Modul-Feature-Flag fuer Pilot-Tenants aktivieren (`modules.helpdesk=true` fuer 2-3 ausgewaehlte Test-Tenants), Smoke-Test-Suite erweitern um Helpdesk-CRUD-Flow.
- **(d)** CSAT-/KB-/Routing-Rules-Tabs **vorlaeufig hidden** bis Backend-Schema dafuer existiert (Empfehlung #3) — sonst suggeriert die UI Funktionalitaet, die nicht persistiert.

**Zeitschaetzung**: 4-6 Tage Frontend-Wiring + 1 Tag Enum-Konsolidierung + 1-2 Tage Smoke-Test-Update = **1 Sprint-Welle (5-7 Tage)**. Identisches Pattern wie Wiki-Mock->Backend-Migration, vermutlich schneller weil 28 Hooks bereits geschrieben und getypte.

**Risiken**:
- Status-Filter-Logik in HelpdeskPage hat hardcodierte Mock-Status-Werte (z.B. `'in_progress'` als Filter-Default), Konsolidierung auf `pending` ist UI-Breaking-Change. **Daher i18n-Display-Layer wichtig.**
- TanStack-Cache-Invalidierung nach Mutation muss korrekt verkettet werden (z.B. nach `useAddMessageMutation` muessen `messages(ticketId)` UND `ticket(id)` invalidiert werden — `updated_at` aendert sich).
- Backend-Migration-State pruefen: alle Postgres-Tabellen existieren? `helpdesk_tickets`, `helpdesk_messages`, `helpdesk_queues`, `helpdesk_canned_responses`, `helpdesk_sla_policies` — pruefen in `migrations/` falls nicht gefunden, dann Migration-Backfill noetig.

**Diese Empfehlung ist Pflicht vor jeder AI-Helpdesk-Funktion**, weil AI-Features auf den TanStack-Hooks-Layer aufsetzen sollen, nicht auf den Mock.

---

### 2. **AI-Drafts mit EU-LLM-Provider-Wahl-Architektur + Article-50-Disclosure-by-Design (P1 Strategisch, Sprint 3 Welle 2-3)**

**Problem**: Cosmi-Helpdesk hat heute **null AI-Funktion** (keine Embeddings, kein LLM-Call, keine Drafts-Suggestion, keine Sentiment-Analyse). Konkurrenz hat AI als Tabellenstake gesetzt: Zammad 7.0 (DACH-Open-Source-Anker!) bringt seit Maerz 2026 AI-Summaries + Writing-Assistant + AI-Agents mit 7-Provider-Wahl. Freshdesk Pro $49 inkl Freddy-AI. Zendesk Copilot $50/Agent. **Cosmi-Sales-Pitch ab Q4 2026 ohne AI-Layer wird strukturell schwer.**

Gleichzeitig: **EU-AI-Act Article 50 in Kraft ab 2. August 2026** — Helpdesk-Chatbots Pflicht-Disclosure vor First-Interaction. Cosmi muss Disclosure-UI-Schicht VOR der ersten AI-Funktion bauen.

Und: Zammad-7.0.1-CVE-Cluster (8. April 2026) zeigt: AI-Endpoints sind Angriffsflaeche-Multiplikator (SSTI -> RCE via AI Agent, SSRF, Missing-Auth-Audits). Threat-Modeling Pflicht vor Launch.

**Empfehlung — drei-stufige AI-Helpdesk-Phase**:

**Phase 1 (Sprint 3 Welle 2, Q3 2026): AI-Drafts mit Co-Pilot-Pattern**

- LLM-Provider-Wahl-Architektur einfuehren: Backend-Service `helpdesk-ai-service` mit Provider-Plugin-Interface (analog zu Zammad-7.0):
  - **Tier 1 (DACH-Compliance, Pflicht)**: EU-LLM (z.B. Mistral AI Cloud Paris-Hosted, oder Aleph-Alpha Luminous), Ollama-Local-Self-Host (Llama 3.1, Mistral 7B), OpenAI-API-Compatible-Custom (fuer Self-Host-LLM-Server der Kunden).
  - **Tier 2 (Optional, Tenant-Opt-In)**: OpenAI direct, Anthropic Claude, Azure OpenAI.
  - Tenant-Setting: `helpdesk.ai_provider` + `helpdesk.ai_api_key` (per-tenant-encrypted via Vault/KMS).
- Endpoint: `POST /api/v1/helpdesk/tickets/{id}/draft-reply` — gibt Draft-Suggestion zurueck basierend auf:
  - Tenant-eigenen historischen Tickets (mit pgvector-Embedding-Index ueber Ticket-Subject + Erste-Message + Resolution-Reply).
  - Tenant-eigenen Wiki-Articles (Cross-Modul-Bridge — siehe Empfehlung #3).
  - Aktueller Ticket-Thread-Context.
- Frontend: `Bot`-Icon-Button im Reply-Composer (Lucide-Icon bereits importiert in HelpdeskPage.tsx!) -> generiert Draft -> Editor fuellt sich -> Agent reviewed, anpasst, sendet. **Co-Pilot-only, kein Auto-Send.**
- **Article-50-Disclosure-UI (PFLICHT vor erstem AI-Endpoint-Live-Gehen)**:
  - Banner in Helpdesk-Settings: "AI-Provider: {Name}. Drafts werden von AI generiert. Daten werden via {Provider} verarbeitet (Region: {EU/US}). Opt-Out unter [...]."
  - In-Composer-Disclosure: "(AI-Draft, vor Senden pruefen)" als Text-Label, **Agent muss explizit auf 'Use AI Draft' klicken**.
  - Audit-Log-Tabelle `helpdesk_ai_calls`: tenant_id, user_id, ticket_id, provider, model, prompt_hash, response_hash, created_at — fuer Compliance-Audit + Cost-Tracking.
- Pricing: **€0.20/AI-Draft** (Cosmi-internal Cost-Plus-Marge vs Zammad €0.03/Call und HelpScout $0.50/Draft). Tenant-Setting fuer monatliches Budget-Limit.

**Phase 2 (Sprint 4, Q4 2026): AI-Summaries + Auto-Triage**

- **Ticket-Thread-Summary**: Endpoint `POST /api/v1/helpdesk/tickets/{id}/summary` — gibt Customer-Intent + Discussion-Points + Open-Questions + Next-Steps. UI: Sidebar im Ticket-Detail.
- **Auto-Triage** (Topic-Klassifikation): bei Ticket-Create LLM-Call zur Auto-Queue-Zuordnung + Auto-Priority-Vorschlag (Sentiment-basiert). UI: Vorschlag-Banner ("AI schlaegt Queue 'Technical' vor"). **Agent muss bestaetigen** — kein Auto-Assign-ohne-Confirm.
- Sentiment-Analyse-Hook: bei `useAddMessageMutation` Customer-Message-Sentiment-Score persistieren, Auto-Priority-Update bei Negative-Tone (mit Notification an Agent).

**Phase 3 (Q1 2027): Optionale Auto-Resolution (Outcome-Pricing)**

- **Optionaler** Auto-Resolver (Cosmi-Fin-Pendant) — nur fuer hochkonfigurierte Use-Cases (Tier-0-FAQs, Order-Status-Lookups via Cosmi-CRM-MCP-Tool-Use).
- Pricing: **€0.50/Resolution** (Half-Price-Anker gegen Intercom $0.99).
- Voraussetzung: vollstaendiges KB-Backend (Empfehlung #3) + Wiki-Article-Embeddings-Bridge + tenant-spezifische-Procedures (NL-Workflows).

**Security-Pflicht (vor Phase 1 Live-Going)**:

- Threat-Modeling-Session auf Basis Zammad-7.0.1-CVE-Liste (CWE-Mapping):
  - **SSTI -> RCE**: alle AI-Prompt-Templates als untrusted-Input behandeln. Kein `eval()`, kein dynamic-template-rendering der LLM-Antwort. Sanitization vor Persistierung in `ticket_messages.body`.
  - **SSRF via Webhooks**: Egress-Whitelist fuer AI-Provider-Endpoints in `helpdesk-ai-service`. Outbound nur zu zugelassenen Hosts (Mistral, OpenAI, Anthropic, lokaler Ollama).
  - **Missing-Auth-Audits**: jede neue AI-Endpoint-Route muss durch JWT-Tenant-Claim + RBAC-Check. CI-Check: `route_helpdesk_ai.go` muss `middleware.GetTenantID(r.Context())` als erste Aktion haben.
  - **Improper-Access-Control in AI-Assistance-Controller**: tenant-isoliert pruefen, dass Tenant-A nicht Tickets von Tenant-B als AI-Context bekommt. **Postgres-RLS-Check bei Embedding-Search** — pgvector-Query muss mit `tenant_id =` WHERE-Clause auf Embedding-Tabelle.

**Zeitschaetzung Phase 1**: 3-4 Sprints (Backend AI-Service + Provider-Plugin-Interface + pgvector-Schema + Disclosure-UI + Audit-Log + Frontend-Draft-Button + Security-Audit) = **6-8 Wochen**.

**Risiken**:
- LLM-Provider-Wahl-Architektur fuegt eine neue Backend-Service-Komponente hinzu — Compose-File-Aenderung, neue Migration, neue Tenant-Settings-UI.
- pgvector + Embedding-Pipeline ist NEUES Tooling im Cosmi-Stack (aktuell nur Postgres-FTS-german). Embedding-Modell-Wahl (BGE-M3 als Self-Host-Default? OpenAI ada-002 als Cloud-Default?) ist Architektur-Entscheidung.
- Cost-Tracking pro Tenant + Budget-Limits = neue Billing-Hooks. Risikofrei zu starten mit "AI-Drafts Beta, Tenant-Opt-In, kein Billing in Phase 1".

**Diese Empfehlung adressiert den groessten Markt-Risiko-Faktor**: Cosmi-Helpdesk ohne AI-Layer wird in 6-12 Monaten als "alte Welt" wahrgenommen, wenn Konkurrenz ihre AI-Outcome-Pricing-Modelle vollstaendig durchgesetzt hat.

---

### 3. **Cross-Modul-Bridge: Wiki-als-Helpdesk-KB + Dialer-Voice-zu-Ticket + CSAT-Backend (P1 Cosmi-USP-Aktivierung, Sprint 3 Welle 3 / Sprint 4)**

**Problem**: Cosmi-USP-Anker ("Helpdesk-im-CRM-im-Dialer-im-Wiki-Bundle") ist heute **rein konzeptionell**:
- Helpdesk-Frontend-Tab `wissensdatenbank` rendert `MOCK_KB_ARTICLES` aus dem Mock-Store. Wiki-Modul existiert (S1.1 done, Postgres-FTS-german, JSONB-Content) — **Brueckenbau zwischen beiden ist Null**.
- Cosmi-Dialer-Modul (S3.7 done, Mai 2026) verfolgt Calls, hat aber **kein Auto-Ticket-aus-Call-Hook**. Wenn Customer waehrend eines Dialer-Calls ein Support-Issue meldet, muss Agent manuell ein Ticket erstellen.
- CSATWidget rendert Frontend-only — kein Backend-CSAT-Score-Persistierung, kein Cross-Modul-Customer-Health-Score-Hebel.
- TicketRoutingConfig speichert Rules in Mock-Store — kein Backend-Routing-Rules-Schema, also kein Auto-Assign nach `subject contains "Rechnung"` -> `queue: Buchhaltung`.

Die Konkurrenz hat **Native-KB-Connectors** (Notion/GDrive/Confluence in Front, Salesforce/Shopify/Stripe/Jira in Intercom-Fin-MCP) als 2026-Standard etabliert. **Cosmi hat den natuerlichen Vorteil: eigene Wiki-/CRM-/Dialer-Module im selben Bundle.** Aber Native-Bridge-Implementation steht auf Null.

**Empfehlung**:

**(a) Wiki-Article-Bridge fuer Helpdesk-KB-Tab (4-6 Tage)**:
- Helpdesk-Frontend-Tab `wissensdatenbank` umstellen: statt `MOCK_KB_ARTICLES` -> Wiki-Backend-API-Call zu Wiki-Articles mit `category = 'helpdesk-kb'` ODER `tag = 'kb-article'`.
- Wiki-Backend-Query: bestehender Wiki-Service hat bereits Category- und Tag-Filter — neue Endpoint-Route in `route_helpdesk.go`: `GET /api/v1/helpdesk/kb-articles` -> proxied zu `wiki-service.ListArticles(category='helpdesk-kb')`.
- Frontend: `useHelpdeskKBQuery` als TanStack-Hook (delegiert an `useWikiArticlesQuery(category='helpdesk-kb')`).
- Beim Ticket-Detail-View: Sidebar mit "Verwandte Wiki-Articles" — Wiki-Postgres-FTS-Search auf Basis Ticket-Subject + Ticket-erste-Message als Query.
- **Phase-2-Erweiterung (mit AI-Layer aus Empfehlung #2)**: Wiki-Article-Embeddings (pgvector) als Semantic-Context-Retrieval fuer AI-Drafts.

**(b) Dialer-Voice-zu-Ticket-Hook (3-5 Tage)**:
- Dialer-Service emittiert seit S3.7 Call-Lifecycle-Events (call.started, call.answered, call.ended). 
- Helpdesk-Worker: subscriben auf Dialer-Call-End-Event, **wenn Call-Note-vorhanden** ODER **wenn Agent-explizit `Create Ticket`-Button im Dialer-UI klickt** -> Auto-Create-Ticket mit Subject = Call-Note-First-Line, RequesterID = Caller-CRM-Contact-ID, Initial-Message-Body = Call-Transcript (wenn Cosmi-LiveKit-Recording-Transcribe-Pipeline aktiv).
- Frontend-Dialer-UI: `Create Ticket from Call`-Button im Call-Detail-Panel. Klick fuehrt zu Cosmi-Helpdesk-Ticket-Erstellung mit pre-filled-Fields.
- **Phase-2 (Voice-AI)**: Call-Transcript-LLM-Summary als Initial-Ticket-Message.

**(c) CSAT-Backend-Schema + Persistierung (3-4 Tage)**:
- Neue Migration: `helpdesk_csat_ratings`-Tabelle (id, tenant_id, ticket_id FK, score INT 1-5, comment TEXT NULL, submitted_by uuid, submitted_at).
- Backend-Service: `Service.SubmitCSAT(ctx, ticketID, score, comment)` + `Service.GetCSATAggregate(tenantID, dateRange)`.
- REST-Endpoint: `POST /api/v1/helpdesk/tickets/{id}/csat`.
- Frontend: CSATWidget umstellen auf `useSubmitCSATMutation`. CSATAggregate-Komponente umstellen auf `useCSATAggregateQuery`.
- **Phase-2 (mit AI-Layer)**: Smart-CSAT-Inference (Front-Pattern) — LLM-Inferenz aus Conversation-Sentiment ohne Pflicht-Survey, als optionaler 2nd-Data-Stream.

**(d) Routing-Rules-Backend-Schema (4-6 Tage)**:
- Neue Migration: `helpdesk_routing_rules`-Tabelle (id, tenant_id, name, condition_jsonb {field, op, value}, action_jsonb {assign_queue, assign_agent, set_priority}, position INT, active BOOL).
- Backend-Service: Rule-Engine im Ticket-Create-Flow + Reassign-Flow. Erste Regel-die-matcht-gewinnt (position-sortiert).
- REST-Endpoints: `GET/POST/PUT/DELETE /api/v1/helpdesk/routing-rules`.
- Frontend: TicketRoutingConfig umstellen auf neue TanStack-Hooks.
- **Phase-2 (mit AI-Layer)**: AI-Auto-Triage (Empfehlung #2 Phase 2) als zusaetzlicher Routing-Schritt — wenn keine Regel matcht, LLM-Klassifikation vorschlagen.

**Zeitschaetzung Gesamtpaket (a)+(b)+(c)+(d)**: **3-4 Sprints / 6-8 Wochen**. Kann mit Empfehlung #2 parallelisiert werden (Backend-Schemas + Bridges sind LLM-unabhaengig).

**Risiken**:
- Wiki-Helpdesk-Bridge erfordert Wiki-Backend-Stabilitaet (Wiki-Frontend-Wiring laeuft separat parallel — siehe Wiki-Deepdive). Risiko: wenn Wiki-Wiring-Welle nicht zeitgleich faehrt, ist Helpdesk-KB-Tab leer (`category='helpdesk-kb'`-Articles existieren nicht ohne Wiki-Frontend zum Anlegen). **Mitigation**: Seed-Migration mit 5-10 KB-Sample-Articles fuer Pilot-Tenants.
- Dialer-Voice-zu-Ticket erfordert Dialer-Event-Bus-Stabilitaet (S3.7 done, RabbitMQ/Redis-Pubsub?). **Verifizieren** in `backend/internal/dialer/events.go`.
- Routing-Rules: Bei Multi-Regel-Konflikt (zwei Regeln matchen) ist erste-gewinnt einfach, aber Tenants koennten erwarten "alle anwenden". **MVP**: erste-gewinnt + position-Sortierung. Phase 2: rule_set_mode = first_match / all_match.
- CSAT-Trigger: Wann wird Survey angefragt? Bei Ticket-Resolution-Move-zu-`solved`? Mit Email-Survey-Sender (kein Email-Backend!) oder In-App-Notification? **Initiale Empfehlung**: In-App-Banner bei naechstem Login des Requesters, Email-Survey als Phase 2.

**Diese Empfehlung aktiviert Cosmis USP-Anker**, ohne den der Helpdesk-Modul-Preis-Vorteil gegen Freshdesk-Pro $49 (inkl AI) NICHT verteidigbar bleibt. **Modul-Integration-Differenzierung muss IMPLEMENTIERT werden, nicht nur in Sales-Pitches behauptet.**

---

## Sekundaere Empfehlungen (P2-P3, nicht Pflicht im Sprint 3)

- **Business-Hours-SLA-Compute** (P2, 2-3 Tage): `SLAPolicy.BusinessHours JSONB` ist Schema-Slot, aber `ApplyPolicy` ignoriert es. Implementierung: pro Tag (Mo-So) start/end-Time + Holiday-Override-Liste, due_at = now + Sum-of-business-minutes-bis-window-voll. Frontend-BusinessHoursDialog ist da, Backend-Compute fehlt. Quick-Win, hoher KMU-Wert (KMUs arbeiten meist 8-17h, nicht 24/7).
- **pg_trgm Fuzzy-Dup-Detection** (P2, 1-2 Tage): `merge.go` hat Code-TODO. `CREATE EXTENSION pg_trgm` + similarity-Query mit threshold 0.4. Reduziert Mis-Merges + verbessert UX.
- **Email-zu-Ticket-Pipeline** (P2 strategisch wichtig, 5-7 Tage): Email-Empfangs-Service (IMAP-Poll oder SMTP-Receive) -> Auto-Ticket-Create. Voraussetzung fuer Multi-Channel-Inbox-Story. Pflicht-Move falls Cosmi-KMU-Kunde "Customer-Email -> Support-Ticket"-Use-Case will (das ist 80% des DACH-KMU-Support-Bedarfs).
- **Macros / Automations / Triggers** (P3, 4-6 Tage): event-getriebene Auto-Actions (z.B. "wenn Ticket 24h ohne Reply -> assign to Lead-Agent + send-CSAT"). Pattern aus Zendesk Triggers.
- **Customer-Portal / Public-Self-Service-KB** (P3, 2-3 Sprints): Public-Endpoint mit Tenant-Branding fuer Customer-Login + Ticket-View + KB-Search. Wichtig fuer B2C-Cosmi-Kunden, optional fuer B2B-Mittelstand.
- **MCP-Server-Integration** (P3 Hebel, 3-5 Tage): Cosmi-Helpdesk-MCP-Server exponiert Tools (search_tickets, get_ticket_status, create_ticket) fuer Claude-Code / Cursor / Claude Desktop. Cosmi-User koennte mit AI-Editor in eigene Helpdesk-Daten querieren. Differenzierung gegen Konkurrenz (nur Intercom-Fin nutzt MCP heute, niemand exposed eigenen Helpdesk als MCP-Server).
- **Mobile-Helpdesk-Editor** (P3, ab Sprint 5): Cosmi-Mobile-App-Helpdesk-Modul (Ticket-Liste + Quick-Reply + Push-Notifications).
- **SCIM-Provisioning** (P3 Enterprise, 1-2 Wochen): User-Sync ueber Azure-AD / Okta. Nicht Pflicht fuer KMU-Kerngeschaeft.

---

## Discord-Push-Template

**Channel**: `#trends`

```
[Embed 1] Deepdive: helpdesk (W24/2026) — Top-Empfehlung
Frontend-Mock->Backend-Wiring + Status/Priority-Enum-Konsolidierung. HelpdeskPage.tsx (996 LOC) konsumiert heute Mock-Store, 28 TanStack-Hooks (316 LOC) liegen seit April 2026 ungenutzt. Type-Drift Frontend<->Backend in Status (in_progress vs pending) + Priority (medium vs normal). Pflicht-Move Sprint 3 Welle 1.
[Buttons: 'Lesen' (Datei) | 'Pick' (-> picks.jsonl) | 'Followup 14d' (-> followups/)]

[Embed 2] Deepdive: helpdesk — Strategie-Empfehlung 2
AI-Drafts mit EU-LLM-Provider-Wahl-Architektur + Article-50-Disclosure-by-Design (Pflicht ab 2026-08-02). Zammad 7.0 hat AI mit 7-Provider-Wahl ab Maerz 2026, Cosmi steht auf Null. Phase 1: AI-Drafts Co-Pilot, Phase 2: Summaries+Triage, Phase 3 (Q1 2027): Optional Auto-Resolution €0.50/Resolution. Security-Threat-Modeling Pflicht (Zammad-7.0.1-CVE-Cluster).
[Buttons: 'Lesen' | 'Pick' | 'Followup 30d']

[Embed 3] Deepdive: helpdesk — Strategie-Empfehlung 3
Cross-Modul-Bridge: Wiki-als-Helpdesk-KB + Dialer-Voice-zu-Ticket + CSAT-Backend + Routing-Rules-Backend. Aktiviert Cosmis USP-Anker, der heute rein konzeptionell ist. Vier Sub-Streams, parallelisierbar mit AI-Phase. KB-Tab haengt heute komplett im Mock.
[Buttons: 'Lesen' | 'Pick' | 'Followup 21d']
```

---

## Quellen

**Cosmi-Code-Reading (Tag 1)**:
- `backend/internal/helpdesk/` (9 Files, 2419 LOC): models.go, sla.go, merge.go, service.go, postgres_repository.go, errors.go, service_test.go, tenant_isolation_phase2_test.go, tenant_isolation_phase3_test.go.
- `desktop/src/renderer/src/modules/helpdesk/` (7 Files, 2043 LOC): HelpdeskPage.tsx, SLABadge.tsx, CSATWidget.tsx, CannedResponsesPanel.tsx, CannedResponsePicker.tsx, BusinessHoursDialog.tsx, TicketRoutingConfig.tsx.
- `desktop/src/renderer/src/api/helpdesk-client.ts` (198 LOC), `desktop/src/renderer/src/api/hooks/useHelpdesk.ts` (316 LOC), `desktop/src/renderer/src/stores/helpdesk.ts` (254 LOC).
- `.knowledge/api.md`, `.knowledge/milestones.md` (S1.4-Eintraege 2026-04-18, W2D-C-Sweep 2026-05-08).

**Konkurrenz-Recherche (Mai-Juni 2026)**:
- Zendesk: [Zendesk Copilot pricing 2026 guide (eesel)](https://www.eesel.ai/blog/zendesk-ai-copilot-add-on-pricing), [Zendesk AI Agents 2026 guide (Kustomer)](https://www.kustomer.com/resources/blog/zendesk-ai-agents-features/), [Zendesk pricing](https://www.zendesk.com/pricing/), [Zendesk Outcome-Based Pricing Deep Dive (eesel)](https://www.eesel.ai/blog/zendesk-outcome-based-pricing), [Futurum: Zendesk Bets on Autonomous AI Agents](https://futurumgroup.com/insights/zendesk-bets-on-autonomous-ai-agents-outcome-pricing-to-upend-service-models/).
- Freshdesk: [Freddy AI 2026 guide (myaskai)](https://myaskai.com/blog/freshdesk-freddy-ai-agent-complete-guide-2026), [Freshdesk pricing & plans](https://www.freshworks.com/freshdesk/pricing/), [Freddy AI pricing guide (eesel)](https://www.eesel.ai/blog/freshdesk-ai-pricing).
- Zammad: [Zammad 7.0 with AI features (zammad.com)](https://zammad.com/en/product/zammad-7-0), [Zammad 7.0.1 security release](https://zammad.com/en/product/releases/7-0-1), [Zammad releases page](https://zammad.com/en/product/releases), [Zammad pricing 2026 (chatarmin)](https://chatarmin.com/en/blog/zammad-pricing), [Zammad community forum: 7.0.1 / 6.5.4 security release](https://community.zammad.org/t/security-release-zammad-7-0-1-6-5-4/19986), [Zammad 2026 review (research.com)](https://research.com/software/reviews/zammad).
- Intercom: [Fin pricing](https://fin.ai/pricing), [Fin outcomes documentation](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes), [Fin 2026 guide (myaskai)](https://myaskai.com/blog/intercom-fin-ai-agent-complete-guide-2026), [Intercom pricing 2026 (featurebase)](https://www.featurebase.app/blog/intercom-pricing).
- HelpScout: [AI Drafts docs (helpscout)](https://docs.helpscout.com/article/1570-ai-drafts), [AI Drafts pricing](https://docs.helpscout.com/article/1539-ai-drafts-pricing-billing), [AI transparency](https://www.helpscout.com/company/legal/ai-transparency/), [HelpScout pricing 2026 (chatarmin)](https://chatarmin.com/en/blog/help-scout-pricing).
- Front: [Front pricing](https://front.com/pricing), [Front 2026 review (eesel)](https://www.eesel.ai/blog/front-review), [Freshdesk vs Front 2026 (eesel)](https://www.eesel.ai/blog/freshdesk-vs-front).
- OTOBO: [OTOBO open source ticketing](https://otobo.io/en/open-source-ticketing-system/), [Open source ticket systems comparison (otobo-docs)](https://otobo-docs.softoft.de/en/ecosystem/open-source-ticket-systems-comparison/), [OTOBO GitHub](https://github.com/RotherOSS/otobo).

**EU-AI-Act Article 50 (in Kraft 2. August 2026)**:
- [Article 50 transparency rules (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/transparency-rules-article-50/).
- [Article 50 full text](https://artificialintelligenceact.eu/article/50/).
- [Compliance checklist (ProofSnap)](https://getproofsnap.com/eu-ai-act-deadline.html).
- [10 takeaways: EU Commission draft guidelines (globalpolicywatch, Mai 2026)](https://www.globalpolicywatch.com/2026/05/10-takeaways-european-commission-draft-guidelines-on-ai-transparency-under-the-eu-ai-act/).
- [Article 50 chatbot checklist (kla.digital)](https://kla.digital/blog/eu-ai-act-article-50-checklist-chatbots-copilots-ai-agents).
- [EU AI Act & chatbots 2026 (heeya)](https://heeya.fr/en/blog/eu-ai-act-chatbot-compliance-2026).

**Pricing-Trend-Daten**:
- [AI pricing models 2026: per-seat vs per-use vs outcome (korixinc)](https://korixinc.com/learning-center/ai-pricing-models-2026).
- [Bessemer Atlas: AI pricing & monetization playbook](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook).
- [Per-resolution vs per-conversation AI pricing 2026 (fin.ai)](https://fin.ai/learn/per-resolution-vs-per-conversation-ai-pricing).
- [AI agent pricing comparison 2026 (fin.ai)](https://fin.ai/learn/ai-customer-service-agent-pricing-comparison).

**G2/Capterra-Reviews (Mai-Juni 2026 Snapshot)**:
- [Zammad G2 reviews](https://www.g2.com/products/zammad/reviews), [Zammad Capterra](https://www.capterra.com/p/207587/Zammad/), [Zendesk Capterra reviews 2026](https://www.capterra.com/p/164283/Zendesk/reviews/), [Freshdesk Capterra reviews 2026](https://www.capterra.com/p/124981/Freshdesk/reviews/), [Freshdesk vs Zendesk Capterra comparison 2026](https://www.capterra.com/compare/124981-164283/Freshdesk-vs-Zendesk).

---

## Picks (vorgeschlagen)

- [ ] 🔴 **Frontend-Helpdesk-Mock->Backend-Wiring + Enum-Konsolidierung** — Pflicht-Sprint-3-Welle-1, identisches Pattern wie Wiki-Wiring, 28 Hooks bereit. Status/Priority-Enum-Drift sofort konsolidieren. (Empfehlung 1)
- [ ] 🟢 **AI-Drafts mit EU-LLM-Provider-Wahl + Article-50-Disclosure-by-Design** — Pflicht-Roadmap-Move fuer Q3 2026. Zammad-7.0-Pattern (7 Provider) adoptieren, Threat-Modeling vor Launch. (Empfehlung 2 Phase 1)
- [ ] 🟢 **Cross-Modul-Bridge: Wiki-als-Helpdesk-KB + Dialer-Voice-zu-Ticket + CSAT-Backend + Routing-Rules-Backend** — Aktiviert Cosmis USP-Anker. Vier Sub-Streams, parallelisierbar. (Empfehlung 3)
- [ ] 🟡 **Business-Hours-SLA-Compute** — Schema-Slot da, Compute fehlt. Hoher KMU-Wert, Quick-Win (2-3 Tage). (Sekundaer)
- [ ] 🟡 **pg_trgm Fuzzy-Duplicate-Detection** — Code-TODO, 1-2 Tage. Reduziert Mis-Merges. (Sekundaer)
- [ ] 🟡 **Email-zu-Ticket-Pipeline** — Strategisch wichtig fuer Multi-Channel-Story, 5-7 Tage. (Sekundaer)
- [ ] 🟡 **MCP-Server-Integration (Cosmi-Helpdesk als MCP-Server)** — Differenzierung, 3-5 Tage. Niemand außer Intercom-Fin macht das heute. (Sekundaer)
- [ ] 🟡 **Followup 30d**: AI-Helpdesk-Markt erneut scannen (besonders Zammad 7.1, Outcome-Pricing-Trends, Article-50-Code-of-Practice finale Juni 2026). (-> followups/2026-07-08-helpdesk-ai-market-rescan.md)
- [ ] 🟡 **Followup 14d**: Status-Check ob Wiring-Welle Helpdesk gestartet ist und ob Wiki-Bridge-Plan synced ist. (-> followups/2026-06-22-helpdesk-wiring-status.md)

---

## Pflicht-Sektion: EU-AI-Act-Article-50-Compliance-Checkliste (Cosmi-Helpdesk)

Vor erster AI-Funktion live-going (geplant Q3 2026):

- [ ] **Disclosure-UI vor First-Interaction** — Banner in Customer-Portal: "AI-generated reply, vor Senden gepruefte". Im Agent-UI: "AI-Draft, review before send".
- [ ] **Human-Handover-Trigger** — Agent kann jederzeit AI-Draft verwerfen + manuell antworten. Customer kann im Customer-Portal "Speak to human" anfragen.
- [ ] **Audit-Log** `helpdesk_ai_calls` — provider, model, prompt_hash, response_hash, persistiert pro Tenant. Authorities-Audit-bereit.
- [ ] **LLM-Provider-Transparenz** — Tenant-Setting: welcher LLM wird genutzt, in welcher Region, mit welchen Daten-Verarbeitungs-Vertraegen.
- [ ] **Opt-Out-Pfad** — Tenant kann AI-Helpdesk-Features deaktivieren. Customer kann Opt-Out fuer AI-Handling beantragen.
- [ ] **Trainings-Daten-Disclosure** — explizit kommunizieren: "Tenant-Daten werden NICHT zum Trainieren der LLM-Modelle genutzt" (Pflicht-Pitch-Punkt fuer DACH-Compliance-Officer).
- [ ] **Documented Article-50-Audit-Program** — interner Audit-Plan, Quartals-Review, Documentation in `.knowledge/compliance-ai-act-article-50.md`.

---

## Telemetry

```yaml
routine: intel-monday-deepdive
date: 2026-06-08
week: 2026-W24
modul: helpdesk
rotation_position: 5/15
runtime_minutes: ~47
tokens_input: ~270000
tokens_output: ~14800
output_file: monthly/2026-06-08-deepdive-helpdesk.md
pool_threshold_abort: 0.15
discord_webhook_used: DISCORD_WEBHOOK_TRENDS (planned)
status: ok
```
