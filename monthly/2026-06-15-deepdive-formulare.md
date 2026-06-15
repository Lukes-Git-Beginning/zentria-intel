---
year: 2026
week: 25
modul: formulare
created: 2026-06-15
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 54
tokens_input: ~285000
tokens_output: ~16400
rotation_position: 6/15
---

# Deepdive: formulare (Mo W25/2026)

> **Sechster Deepdive der Rotation.** Vorgaenger: `crm-core` (W19, 2026-05-11), `dialer` (W20, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01), `helpdesk` (W24, 2026-06-08). Naechstes Modul gemaess Rotation: **vertraege** (KW26, 2026-06-22). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-Formulare (2026-06-15):** Backend `backend/internal/formulare/` (8 Files, **3870 LOC** mit ~1753 Test-LOC, Production-Code ~2117 LOC, **seit Sprint 1 S1.3 done — Migration 081**). **21 gRPC-RPCs** hinter `modules.formulare`-Flag: 6 Schema-RPCs (Create/Get/Update/Delete/List/Duplicate), 5 Submission-RPCs (Create/Get/List/UpdateStatus/Export), 5 Webhook-RPCs (Create/Get/Update/Delete/List), 1 Delivery-RPC (ListWebhookDeliveries), 1 Stats-RPC (GetFormStats). **4 Domain-Modelle**: FormSchema (mit JSONB-Fields-Array + IsPublic + IsTemplate + PageCount), FormSubmission (mit Answers JSONB + IP-Address INET), FormWebhook (mit HMAC-Secret + Events-Array + Active-Flag), WebhookDelivery (mit Payload + AttemptCount + NextAttemptAt). **Worker:** Exp-Backoff `30s/2min/10min/30min/2h`, Dead-Letter nach 5 Versuchen, HMAC-SHA256-Signatur (`X-Cosmi-Signature: sha256=<hex>` Header), `FOR UPDATE SKIP LOCKED` fuer horizontale Skalierung. CSV-Export mit UTF-8-BOM, XLSX via `excelize/v2`. Tenant-Isolation Phase 2 vorhanden. Frontend `desktop/src/renderer/src/modules/formulare/` (1 .tsx, **2457 LOC FormularePage.tsx**) + `api/formulare-client.ts` (255 LOC) + `api/formulare-types.ts` (195 LOC) + `stores/formulare.ts` (175 LOC, Zustand+persist). Pricing-Anker (`KMU-Hub/.knowledge/pricing.md`): **2 EUR/User-Monat** vs Typeform ab 25.

> **Drei strukturelle Diskrepanzen zwischen Backend und Frontend identifiziert (Status: 2026-06-15).** **#1 Field-Type-Union driftet:** Backend `validFieldTypes` whitelistet 9 Typen (`text/textarea/email/number/select/radio/checkbox/date/file`), Frontend `FormFieldType` listet nur 8 (kein `email`) — ein User-defined Email-Field kommt vom Backend, lehnt das Frontend-Type-System ab. **#2 FieldOption-Struktur driftet:** Backend speichert `[]FieldOption{Value, Label}` (Objekt-Array), Frontend `options?: string[]` (String-Array). Roundtrip-Loss von Option-Labels bei Edit-Cycles. **#3 FormAction (email/task/crm_contact) ist Frontend-only Stub:** im Zustand-Store, Kommentar `"frontend-only: post-submission actions (not yet persisted to backend)"` — die UI-Panel wird beim Speichern weggeworfen. Backend kennt keine Action-Pipeline; Webhooks sind das einzige Post-Submission-Trigger-Mechanism. **Konsequenz:** Lehre aus Helpdesk-Deepdive W24 (HelpdeskPage konsumiert Mocks statt React-Query-Hooks) wiederholt sich hier in milderer Form — ein Sprint-Hygiene-Item, nicht Architektur-Bruch, aber **vor jedem neuen Feature-Sprint zu fixen**.

> **Leit-Signal der Woche:** **Drei Schockwellen treffen den Form-Builder-Markt 2026** — (a) **AI-Generation ist Tabellenstake**: Typeform AI Data Enrichment (4. Februar 2026), Typeform Growth Flow (Mai 2026), Typeform Research Flow (9. Juni 2026), Fillout "AI from prompt + PDF + import", JotForm AI Agents (GPT-4 + Voice via Phone-Add-on), Tally MCP-Server (Claude/ChatGPT — Form-Generation per Chat). Kein KMU-Form-Builder-Vergleich ueberlebt ohne AI-Form-Generation-Pfad in 2026. (b) **EU-AI-Act Article 50 trifft 2. August 2026 jede AI-Form-Generation** — AI-vorausgefuellte Felder, AI-generierte Folge-Fragen (Typeform-Pattern), AI-Disclosure-Pflicht VOR der ersten Interaktion, dokumentier-/auditbar, mit Faehigkeit zur Mensch-Eskalation. Cosmi hat **null AI-Funktion** in formulare — heute Compliance-frei, morgen ein Aufholbau-Sprint. (c) **DSGVO-Form-Compliance-Welle ist live**: EDPB CEF 2026 (Art. 12-14 Transparenz-Enforcement) laeuft seit Maerz 2026 in 25 EU-Datenschutzbehoerden, OLG-Hamm-Urteil (W20-Carry-Forward) zu AI-Vorausfuellung, noyb-Klagen gegen "Pay-or-Okay"-Modelle (W23). Cosmi-Formulare hat heute **IsPublic-Mode aktiv (Backend Code-Pfad existiert), aber keine Anti-Spam-Schicht — kein Honeypot, kein Captcha-Slot, kein Rate-Limit im service.go-Layer**. Das ist heute Code-Schuld, in 4 Wochen ein Production-Incident, wenn die erste oeffentliche Form ueber Cosmi-Tenant lanciert. **Dieser Bericht empfiehlt drei Pflicht-Stakes vor jeder Public-Form-GA und vor jeder AI-Form-Generation-Phase.**

---

## State-of-the-Art

Der Form-Builder-Markt Mitte 2026 ist nicht mehr "Typeform vs Google Forms vs JotForm" — er ist **vierspurig**: (1) **AI-Generation-First-Cloud** (Typeform AI Engagement Platform, Fillout AI-from-PDF, JotForm AI Agents — Form-Auto-Build + Auto-Filling), (2) **Database-Connected-Forms** (Fillout zu Airtable/Notion/Salesforce/HubSpot, Tally zu Notion/Sheets, "Form als Schema-Layer ueber externer Datenbank"), (3) **Developer-Form-Backends** (Formspree, Web3Forms, Basin, Static-Form-Backends mit Honeypot+reCAPTCHA-Optionen, Webhook-First), (4) **EU-Sovereign-Self-Host-Form-Builder** (Formbricks Open-Source self-hosted, Tally Belgium/Frankfurt-Hosted, Plausible Forms/Cloudron-Stack). Cosmi-Formulare sitzt heute **architektonisch in Spur (3)+(4)** — Webhook-First (HMAC + Exp-Backoff + Dead-Letter ist Production-Grade) mit EU-Self-Host-Story — aber **ohne AI-Schicht (Spur 1)**, **ohne externe Database-Connector-Bibliothek (Spur 2)**, **ohne Anti-Spam (Spur 3-Pflicht)**. Das ist sauberer Greenfield-Stand in einem Markt, der gerade jeden Monat AI-Tabellenstakes anhebt.

Drei strukturelle Veraenderungen treiben den Form-Builder-Markt seit Februar 2026:

(a) **AI-Form-Generation ist Tabellenstake — drei Wellen in 4 Monaten.** Welle 1 (Februar 2026): Typeform laenciert **AI Data Enrichment** (4. Februar 2026) — automatische Anreicherung von Form-Responses, plus deeper Segmentation in Contacts & Automations, plus webhook-enabled Automations, plus **Typeform AI Memory** als persistente Customer-Profile-Schicht. Welle 2 (Mai 2026): Typeform **Growth Flow** — AI-powered Customer-Lifecycle (Lead Capture → Enrichment → Nurturing → Conversion → Feedback → Retention → Expansion) in einer Plattform. Welle 3 (9. Juni 2026, vor 6 Tagen): Typeform **Research Flow** — AI-moderated Research-Studien mit Auto-Synthese in Stunden statt Wochen. Parallel: Fillout's "AI from prompt / PDF / imported questions / existing form" generiert komplette Form-Schemas aus natursprachlichen Inputs. JotForm AI Agents — GPT-4-basierte 24/7-Voice+Chat-Conversational-Forms mit Phone-Number-Add-on (PSTN-Inbound). **Konsequenz fuer Cosmi-KMU-Pricing**: 2 EUR/Modul/User/Monat ist heute der KMU-attraktive Anker (Typeform Basic $25/Monat fuer 100 Submissions), **aber** die Konkurrenz pitcht jetzt "AI generiert die Form fuer Dich aus Deinen Daten". Cosmi-Formulare ohne AI-Layer wird in 6-12 Monaten als "alte Welt" wahrgenommen, **wenn nicht ein klares AI-Form-Generation-Pfad-Konzept** (z.B. "Cosmi-AI generiert Form-Schema aus CRM-Kontaktfeld-Liste + Helpdesk-Kategorien + Wiki-Knowledge-Snippets — Cross-Modul-Hebel, den Standalone-Form-Builder nicht koennen") jetzt entworfen wird.

(b) **MCP-Server fuer Forms ist der naechste Marktbeschleuniger — 3 Builder haben es bereits.** Model Context Protocol als 2026-Standard fuer AI-Tool-Integration (Anthropic + OpenAI + Google adoptieren) hat nur **drei Form-Builder mit nativer MCP-Implementation**: **Tally** (20+ Tools, OAuth, Safety-Guardrail-gegen-Deletion, **kostenlos** auch im Free-Tier), **JotForm** (paid plans nur), **Typeform** (noch Beta). Google Forms, SurveyMonkey, Microsoft Forms, Fillout — alle **kein nativer MCP-Server**. Was MCP konkret heisst: ein Anwender sagt zu Claude/ChatGPT "Erstell mir ein Bewerbungsformular mit 5 Pflichtfeldern und Webhook zu Slack" — das Tool baut, deployt, gibt die Public-URL zurueck. **Konsequenz fuer Cosmi**: Cosmi-Formulare als MCP-Server (`cosmi-formulare-mcp`) ist ein konkretes, KMU-attraktives, technisch realisierbares Sprint-Item (gRPC bereits da → MCP-Wrapper ist ein Adapter-Layer). Cross-Modul-Differenzierung: Cosmi-MCP-Server liefert nicht nur Form-Tools, sondern auch CRM/Helpdesk/Wiki-Tools — ein **integrierter Cosmi-MCP** ist ein Multi-Modul-Hebel, den Tally/JotForm nicht haben.

(c) **EU-AI-Act Article 50 trifft am 2. August 2026 jede AI-Form-Funktion + parallel EDPB-CEF-2026-Transparenz-Enforcement und OLG-Hamm-AI-Vorausfuellung.** Per European Commission Draft Guidelines (Mai 2026) + Code of Practice on Transparency (10. Juni 2026): **AI-Form-Generation, AI-Folge-Fragen, AI-Vorausfuellung von Feldern, AI-moderated Surveys — alle fallen unter Article-50-Transparenz-Pflicht**. Persistent visual indicator ("AI Assistant" / "Powered by AI") oder First-Message-Notice als Disclosure-Pattern. **Penalty bis €15 Mio oder 3% Welt-Umsatz**. Parallel: **EDPB CEF 2026** laeuft seit Maerz 2026 in 25 EU-Datenschutzbehoerden mit Fokus Art. 12-14 (Transparenz bei Direkterhebung + Drittquellen). Plus: **OLG-Hamm-Urteil** (W20-Carry-Forward — siehe `/opt/zentria-intel/weekly/2026-W20.md:113`) zu AI-Vorausfuellung — Disclaimer-Pflicht + Human-in-the-Loop bei AI-generierten Formularfeldern. **Praktische Implikation fuer Cosmi**: jede AI-Formulare-Funktion ab heute MUSS mit Disclosure-Schicht + Human-Review-Schritt ausgeliefert werden. Cosmi hat einen **strukturellen Vorteil**, weil noch keine AI-Funktion existiert: **Disclosure-by-Design** und **Human-in-the-Loop-as-Default** kann jetzt eingebaut werden, bevor die erste AI-Form-Funktion live geht. Konkurrenten muessen rueckwirkend ihre Q1/Q2-2026-AI-Releases auditieren.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Typeform (international, threat: HIGH als Markt-Standard, medium fuer DACH-KMU Direkt-Sale)**

Typeform ist nicht direkter DACH-KMU-Konkurrent (US-/EU-Cloud, kein Self-Host, Pricing-Eskalation), aber **das Feature-Erwartungs-Referenzmodell** — jeder Form-Builder-Buyer im DACH-Mittelstand sieht zumindest Typeform-Demo, bevor er KMU-Alternative kauft. Markenfuehrer fuer "Conversational Form" (eine Frage zur Zeit, smooth transitions, 30-40% bessere Completion-Rate vs Multi-Field-Standard).

- **AI Engagement Platform 2026**: AI Data Enrichment (Feb 2026), AI Memory (persistente Profile), Growth Flow (Customer-Lifecycle in einer Plattform, Mai 2026), Research Flow (AI-moderated Studies, 9. Juni 2026), AI Follow-Up-Questions (dynamische Fragen basierend auf Antworten).
- **Workflow Builder** — Automatisierung komplexer Prozesse mit native Integrations, Webhook-enabled Automations.
- **Advanced Features**: Conditional Logic (Multi-Condition-Logik), Calculations, Hidden Fields, Video Questions mit Captions, Partial Submit Points, Knowledge Quizzes, Drop-Off-Analyse, AI-Powered Insights.
- **G2/Capterra-Pain-Points 2026**: "Price-to-Value-Ratio fuehlt sich hoch an fuer langfristig", "Response-Rate-Caps frustrieren", "Constant nudge to upgrade", "Online-Customer-Support nicht immer responsiv", "GDPR-konform aber Data lebt auf eigenen US-/EU-Cloud-Servern — strict Compliance braucht mehr Kontrolle".
- **Pricing-Basis (2026)**: Free (10 Responses/Monat), Basic $25 (100), Plus $50, Business $83 (10000), Growth Pro $291, Talent $125 / User-Monat.
- **Gap zu Cosmi**: AI Data Enrichment komplett, AI Memory, Growth Flow Customer-Lifecycle, Research Flow, AI Follow-Up-Questions, Multi-Condition Conditional Logic, Calculations/Computed Fields, Video Questions, Partial Submit Points, Drop-Off-Analyse, Workflow-Builder-Visuelle-Pipeline, Advanced-Analytics.
- **Strategischer Hinweis**: **Cosmi gewinnt nicht ueber "AI besser als Typeform"** — Typeform hat 12+ Monate Vorsprung, Engineering-Tiefe und 80M+ Form-Submissions/Jahr als Trainings-Basis. **Cosmi gewinnt ueber "Formulare-in-CRM-in-Helpdesk-in-Wiki-in-Rechnung im KMU-Preis-Sweet-Spot"**: Bewerbungsformular triggert HR-Workflow + CRM-Kontakt-Anlegen + Wiki-Onboarding-Doku-Verlinkung — das ist Cosmi-USP, Typeform kann das strukturell nicht. **Aber:** AI-Form-Generation MUSS ab Q1 2027 verfuegbar sein, sonst greift der "Cosmi-fuehlt-sich-nicht-modern-an"-Effekt — wie schon bei Helpdesk-Deepdive W24 (AI-Drafts als Stake) und Wiki-Deepdive W23 (AI-Search als Stake) als Pattern erkannt.

**2. Tally.so (international/EU-Belgium, threat: HIGH als Best-of-Class Free-Tier + erstem MCP-Implementation)**

Tally ist Cosmis **naechster direkter Architektur-Konkurrent im Free-First-DACH-Form-Builder-Markt**. G2-Rating 4.9/5 ueber 15 Reviews. Belgisch (EU), GDPR-konform, **Daten in Europa (Frankfurt-Servers)**. **Wichtigster Wettbewerbssignal Q2 2026**: erster Form-Builder mit nativem **MCP-Server** (Model Context Protocol fuer Claude/ChatGPT) — Anwender bauen Forms per Chat.

- **Free-Tier ist Killer**: **Unlimited Forms + Unlimited Submissions** kostenlos, Conditional Logic, Signatures, Password Protection, File Uploads (10 MB/File auch im Free).
- **MCP-Server (2026)**: 20+ Tools, OAuth-Auth, Safety-Guardrail-gegen-Deletion, kostenlos auch im Free-Tier. Cosmi-Wettbewerbsvorlage: das ist genau der Use-Case "AI-Agent baut & managed Forms per Chat".
- **Partial Submissions** (Pro $29/Monat) — Capture unfinished Form-Responses bevor User submitten. **Aber:** Signaturen werden aus Sicherheitsgruenden NICHT als Partial-Submissions gespeichert.
- **EU-Hosting**: Belgium HQ, Daten in Frankfurt, GDPR-DPA on Request, Data-Export/Deletion via UI.
- **G2/Capterra-Pain-Points 2026**: "Conditional Logic kann komplex sein, Learning-Curve", "Regionale Affordability bei Pro/Business", "Confirmation-Emails brauchen Upgrade".
- **Pricing**: **Free (unlimited)**, Pro $29 (Branding-Removal + Custom-Domain + Partial-Submissions + Custom-CSS + Workspace-Org), Business $89 (Data-Retention-Controls, Governance).
- **Tech-Stack**: Cloud-only Hosted in EU, **kein Self-Host-Pfad**.
- **Gap zu Cosmi**: MCP-Server-Adapter, Partial-Submissions, Native-Signatures-Feldtyp, File-Upload-Storage-Backend, Multi-Condition Conditional Logic, Calculations, Notion/Airtable/Sheets-Connector-Bibliothek.
- **Strategischer Hinweis (WICHTIGSTER MCP-PUNKT DIESES REPORTS):** **Tally MCP-Server ist das richtige Vorbild fuer Cosmi-Modul-MCP-Server-Architektur.** Cosmis 21 gRPC-RPCs sind bereits da — der MCP-Adapter ist Sprint-Item: gRPC-RPC → MCP-Tool-Mapping (CreateFormSchema → `cosmi-form-create`, GetFormStats → `cosmi-form-stats`, etc). **Cosmi-Differenzierung gegen Tally**: Tally-MCP ist Form-only — Cosmi-MCP ist Cross-Modul (Forms + CRM + Helpdesk + Wiki + Vertraege + Rechnung). Ein KMU-Anwender sagt zu Claude "Erstell mir ein Onboarding-Form, lege auf Submission einen CRM-Kontakt an, fuege das in den Helpdesk-Welcome-Workflow, verlinke das Onboarding-Wiki-Article" — das ist Cosmi-MCP-Cross-Modul-USP, das Tally architektonisch nicht liefern kann (Tally hat keine CRM-Tabelle). **WARNUNG**: Tally-Free-Tier ist Killer-Pricing-Anker — Cosmi-Formulare 2 EUR/User-Monat ist sehr nah am Free-Tier, aber zahlt sich nur ueber Cross-Modul-Hebel aus. Wenn Cosmi-Formulare standalone vermarktet wird, verliert es gegen Tally Free. **Sales-Doktrin: Cosmi-Formulare wird NIE standalone gepitcht** — immer als Cross-Modul-Hebel.

**3. JotForm (international, threat: medium fuer DACH-KMU — AI-Agent-Vorbild + HIPAA-Pfad)**

JotForm ist der **Multi-Tool-Veteran** mit AI-Agents in 2026. 20+ Jahre am Markt, breite Template-Bibliothek (10000+), HIPAA-Compliance-Pfad fuer US-Healthcare-Use-Cases. AI Agents seit Anfang 2025 — GPT-4 + (fuer HIPAA-Accounts) Google Gemini via Vertex AI mit BAA.

- **AI Agents (2025-2026)**: 24/7 automatisierte Conversational-Forms, Real-Time-Assistance, Form-Filling-Guide, Troubleshooting-Helper. **Phone Number Add-on** — eigene Telefonnummer fuer AI-Agent, PSTN-Voice-Handling.
- **Form Builder Features**: 10000+ Templates, Drag-Drop-Builder, Conditional Logic, Payment-Integration (Stripe/PayPal/Square), E-Signature, File-Upload, Workflow-Automation.
- **MCP-Server** (2026): zweiter Form-Builder mit nativem MCP — paid plans only.
- **G2/Capterra-Pain-Points 2026**: "Pricing fuer Submissions skaliert schnell", "Bronze/Silver/Gold-Tiers verwirrend", "UI fuehlt sich legacy an gegen Typeform/Fillout", "AI-Agents brauchen viel Trainings-Datendurchlauf bis usable".
- **Pricing**: Free (5 Forms, 100 Submissions/mo), Bronze $34 (25 Forms, 1000), Silver $39 (50 Forms, 2500), Gold $99 (100 Forms, hohe Limits), Enterprise (kein Listenpreis). 50% Discount fuer Nonprofits, Education.
- **Tech-Stack**: Cloud-only, Multi-Region (US Primary, EU optional), HIPAA-Path mit BAA, kein Self-Host.
- **Gap zu Cosmi**: AI Agents komplett (mit GPT-4 + Voice-Add-on), 10000+ Form-Templates, Payment-Integration (Stripe-Native), Native E-Signature-Feld, MCP-Server, HIPAA-Compliance-Pfad.
- **Strategischer Hinweis**: **JotForm AI Agents + Phone Number Add-on ist ein Markt-Signal fuer Voice-First-Form-Resolution** (analog zu Intercom Fin Voice in Helpdesk-Markt — siehe Helpdesk-Deepdive W24). KMU-attraktiv: ein Kunde ruft eine Telefonnummer, AI-Agent fuehrt durch ein 8-Felder-Reklamations-Formular, submitted die Antworten in JotForm-System. Cosmi-Differenzierung-Pfad: Cosmi-Dialer + Cosmi-Formulare = Voice-zu-Form-Conversion direkt im Cosmi-Stack — Cross-Modul-Hebel statt Add-on-Pricing. **Aber:** JotForm UI-Reviews zeigen ein Risiko-Pattern: "fuehlt sich legacy an gegen Typeform/Fillout". Cosmi-Formulare's FormularePage.tsx **2457 LOC Mono-File** ist ein UX-Refactor-Schuld-Marker, der vor erster AI-Phase angegangen werden sollte.

**4. Fillout (international, threat: medium fuer DACH-KMU — Database-Connected-Forms-Architektur)**

Fillout ist Cosmis **direktester Architektur-Konkurrent fuer "Form als Schema-Layer ueber Datenbank"-Pattern**. April 2026 Capterra-Snapshot: connects natively mit Notion, Airtable, Google Sheets, Salesforce, HubSpot. **40+ Question-Types** (Cosmi: 9), AI-Form-Generation aus Prompt/PDF/imported-Questions.

- **AI Generation (2026)**: AI von Prompt, AI von PDF-Import (existierendes Formular als PDF hochladen → AI parsed Schema), AI von importierten Questions (Excel/CSV → Form), AI von existierender Form (Refine + Customize).
- **Database-Connected-Forms**: Conditional Logic kann Datenbank-Queries triggern und Felder dynamisch vorausfuellen — z.B. "User waehlt Kunden-Dropdown → Adresse + Telefonnummer auto-fill aus Airtable". Native Integrations: Notion, Airtable, Sheets, Salesforce, HubSpot.
- **40+ Question-Types**: Multi-Page-Branching, Calculation-Fields, URL-Pre-Fill, Hidden Fields, Native Scheduling, Form Analytics Dashboard, File-Uploads, E-Signature, Payment-Collection (Stripe), Conditional-Routing.
- **G2/Capterra-Pain-Points 2026**: "Custom-Domain in Business-Tier nur", "Branding-Removal $19/Monat (Starter)", "Enterprise-Features schnell teuer", "Database-Connector-Bibliothek auf wenige Tools begrenzt — kein SAP/DATEV/Lexware-Connector fuer DACH".
- **Pricing**: Free (1000 Submissions/mo mit Branding), Starter $19, Business $59, Enterprise $89 / User-Monat.
- **Tech-Stack**: Cloud-only, US-/EU-Hosting, kein Self-Host.
- **Gap zu Cosmi**: AI-Form-Generation (Prompt + PDF + Import), 40+ Question-Types, Database-Connector-Bibliothek (Notion/Airtable/Sheets/SF/HS), URL-Pre-Fill, Hidden Fields, Calculation-Fields, Native Scheduling, Native E-Signature, Native Payment (Stripe).
- **Strategischer Hinweis**: **Fillout-Database-Connected-Forms ist das richtige Architektur-Vorbild fuer Cosmi-Cross-Modul-Form-Hebel** — aber Cosmi muss das nicht ueber Connector-Bibliothek (Notion/Airtable/etc) loesen, sondern ueber **Cosmi-Modul-direkte-Bindung**: Cosmi-Formulare kann Form-Schemas direkt aus CRM-Pipeline-Stage-Schema, Helpdesk-Ticket-Felder, Wiki-Articles als Knowledge-Basis ableiten. Das ist ein architektonisch ueberlegen Pfad, weil keine Connector-Pflege-Schuld (jeder externer Connector ist Maintenance-Cost-Multiplier). **Praktischer Sprint-Item**: Cosmi-Formulare-Service exposes `GenerateFromCrmContact(contact_id)` → erzeugt Form-Schema mit allen Kontakt-Custom-Fields als Pre-Fill. Das ist 1-2 Sprints, kein externes API-Risiko, hoher KMU-Demo-Wert.

**5. JotForm (oben behandelt)** + **Formbricks (Open-Source EU-Anker, threat: medium fuer DACH-Tech-affine-KMU)**

Formbricks ist der **Open-Source-Self-Host-EU-Anker** — direkter Architektur-Vergleich zu Cosmi-Formulare-EU-Self-Host-Story. Deutsche Firma, MIT-Lizenz (Open-Source), Docker-One-Click-Self-Host, SOC-2-Type-II-zertifiziert (4.7-Release 2026).

- **Self-Host-Pfad**: Docker-One-Click, voller Datenkontrolle, eigener DB.
- **Managed Cloud**: GDPR-konform, EU-Hosted.
- **Feature-Floor**: Link-Surveys, In-App-Micro-Surveys, Pop-Up-Surveys, Event-based Triggering-System (z.B. "User completed Onboarding", "User visited Pricing-Page 3 Times", "NPS Score dropped below 7"), Open-API.
- **4.7-Release 2026**: Attribute-Data-Types, SOC-2-Type-II-Certification, Advanced-CSS-Customization, Improved Self-Hosting-Tooling.
- **Pricing**: Self-Host kostenlos (MIT), Managed Cloud Free + Pro-Tiers.
- **Tech-Stack**: Next.js + PostgreSQL, Docker-Compose-Self-Host.
- **Trust-Marker**: trusted by Siemens, Ethereum, Cal.com.
- **Gap zu Cosmi**: Event-based Triggering-System (User-Behavior-Trigger → Survey-Surface), In-App-Survey-Embedding-SDK, Pop-Up-Surveys, Attribute-Data-Types (Beta-Feature 4.7), SOC-2-Type-II-Compliance-Marker.
- **Strategischer Hinweis**: **Formbricks ist Cosmis natuerlicher Open-Source-EU-Verbuendeter, nicht direkter Konkurrent** — Formbricks ist Survey-Tool (NPS, In-App-Feedback, User-Research), nicht Multi-Purpose-Form-Builder. **Cosmi-Differenzierung gegen Formbricks**: Multi-Purpose (Bewerbungsformulare, Reklamationen, Lead-Capture, Onboarding) statt Survey-only. **Sprint-Learning aus Formbricks 4.7**: SOC-2-Type-II ist heute der KMU-Compliance-Stake fuer Cloud-Forms — Cosmi sollte SOC-2-Roadmap-Marker bereits jetzt setzen.

**6. Formspree (international, threat: low — Developer-Backend-Vorbild fuer HMAC + Honeypot-Patterns)**

Formspree ist **NICHT** direkter Cosmi-Konkurrent (Static-Site-Form-Backend-Use-Case, kein UI-Builder), aber **Architektur-Vorbild fuer Webhook-First Form-Backend mit Anti-Spam-Patterns**. HTML-Form `<form action="https://formspree.io/...">` Pattern.

- **Spam-Protection**: Honeypot + reCAPTCHA + Keyword-Filter (Personal-Plan+).
- **Webhooks**: ab Personal-Plan ($15/mo) — kein Free-Tier-Webhook (Lesson: Cosmi-Formulare-Webhook ist von Tag-1 frei).
- **Pricing**: Free (50 Submissions/Monat, kein Captcha, kein Webhook), Personal $15 (200 Submissions, 1GB File-Upload), Gold $99 (Webhooks).
- **Tech-Stack**: Cloud-only, US-Hosting (kein EU-Pflicht-Pfad), keine Self-Host-Option.
- **Gap zu Cosmi**: keine — Cosmi ist architektonisch reicher (UI-Builder + Multi-Field-Schema + Conditional Logic). **Aber**: Spam-Protection-Pattern (Honeypot + Captcha + Keyword-Filter) ist genau das, was Cosmi-Formulare **HEUTE FEHLT** — und das vor Public-Form-GA der Pflicht-Stake ist.
- **Strategischer Hinweis (WICHTIGSTER ANTI-SPAM-PUNKT DIESES REPORTS):** **Formspree-Pattern (Honeypot + Captcha-Slot + Keyword-Filter) ist das richtige Anti-Spam-Vorbild fuer Cosmi-Public-Forms-Phase-1.** Cosmi-Formulare hat heute `IsPublic`-Flag aktiv (Backend-Code-Pfad existiert, `service.go::CreateSubmission` macht keine Spam-Pruefung), **aber kein einziges Anti-Spam-Pattern**. Konkrete Sprint-Items: (i) Honeypot-Pflichtfeld im Form-Schema-Builder (Frontend-Stub + Backend-Validation-Rejection bei nicht-leerem Honeypot), (ii) Captcha-Slot mit Cloudflare-Turnstile-EU-friendly + hCaptcha-Privacy-Mode als Wahl (EDPB-CEF-2026-Compliance), (iii) Rate-Limit pro IP + pro Form-Schema (z.B. 10 Submissions/IP/Minute, 1000 Submissions/Form/Tag), (iv) Submission-Status-Erweiterung um `spam` (heute: `new/read/archived` — kein Spam-State), (v) Keyword-Filter konfigurierbar pro Schema. **EU-AI-Act-Disclosure-Add-on**: wenn Phase 2 AI-Spam-Erkennung lanciert, MUSS Art. 50 Disclosure-Pflicht eingehalten werden (User sieht "AI screens submissions" Hint).

---

## Cosmi-IST-Stand

### Backend (kmuhub/backend/internal/formulare/, 3870 LOC)

**Status-Marker (Stand 2026-06-15):**
- **Production-Code:** ~2117 LOC ueber 6 Production-Files (`errors.go` 16, `models.go` 129, `postgres_repository.go` 792, `repository.go` 85, `service.go` 798, `worker.go` 218).
- **Test-Code:** ~1753 LOC ueber 2 Test-Files (`service_test.go` 1265, `worker_test.go` 488 + `tenant_isolation_phase2_test.go` 79).
- **Test-Coverage:** Test/Production-Ratio ist 83% — sehr gut fuer Sprint-1-Modul (Helpdesk-Vergleich: 39% Coverage).
- **Migration:** 081 (`form_schemas`, `form_submissions`, `form_webhooks`, `form_webhook_deliveries`) — done seit Sprint 1 S1.3.
- **gRPC-Service:** 21 RPCs in `proto/formulare/v1/formulare.proto` ueber 4 Resource-Gruppen (Schema/Submission/Webhook/Stats).
- **Tenant-Isolation:** Phase 2 done — `tenant_isolation_phase2_test.go` vorhanden, alle Postgres-Queries filtern `WHERE tenant_id = $1`.

**Domain-Modelle (`models.go` 129 LOC):**
- **FormSchema** — ID, TenantID, Title, Description, **Fields []byte (JSONB-Array von FormField)**, Status (draft/active/archived), IsTemplate, IsPublic, PageCount, SubmissionCount (denormalisiert, per Trigger), CreatedBy, CreatedAt/UpdatedAt/DeletedAt (Soft-Delete).
- **FormField** (in JSONB-Array): ID, Type (`text|email|number|select|checkbox|radio|textarea|date|file` — **9 Typen**), Label, Required, Placeholder, Options ([]FieldOption{Value, Label}), ConditionalLogic (*FieldCondition{FieldID, Operator, Value}).
- **FieldCondition**: Operator (`equals|not_equals|contains`) — **drei Operatoren, ein-bedingung-pro-Feld** (kein AND/OR/multi-condition logic).
- **FormSubmission** — ID, FormSchemaID (nullable, ON DELETE SET NULL), TenantID, Answers (JSONB), Status (`new/read/archived` — **kein `spam`, kein `pending_review`**), SubmittedBy (optional), **IPAddress (INET, NULL — Kommentar: "DSGVO: nur mit Consent"** aber **kein Consent-Gate im Code**).
- **FormWebhook** — ID, FormSchemaID, TenantID, URL, Secret (HMAC-SHA256-Key), Events ([]string default `["submission.created"]`), Active, LastTriggeredAt, LastStatus, CreatedAt/UpdatedAt.
- **WebhookDelivery** — ID, WebhookID, SubmissionID, TenantID, Payload (JSONB), Status (`pending/delivered/failed/dead`), AttemptCount, MaxAttempts (default 5), NextAttemptAt, LastError, LastResponseCode, CreatedAt/DeliveredAt.

**Service-Logik (`service.go` 798 LOC):**
- **CreateFormSchema** — Title-Trim-Required, validateFields whitelist (9 Typen), Status default `draft`, PageCount default 1.
- **UpdateFormSchema** — Partial-Update mit Field-Validation.
- **CreateSubmission** — Answers-Required, IP-Address-Parse-optional, Transactional-Enqueue-aller-Active-Webhooks (`ListActiveWebhooksForSchema`).
- **ExportSubmissions** — CSV (UTF-8-BOM) + XLSX (excelize/v2). Header: `id, submitted_at, status, submitted_by, ip_address, <dynamische answer-keys>`. Dynamische Answer-Keys-Sammlung via `extractAnswerKeys()` (preserved Insertion-Order).
- **GetFormStats** — Aggregierte Submission-Statistics pro Schema.
- **Webhook-Methoden** — `validateWebhookURL` prueft http/https-Scheme + Host-Required, **kein SSRF-Schutz** (keine IP-Whitelist, keine privater-IP-Range-Block — Risiko fuer interne-Network-Probing).
- **maskWebhookSecret** — Read-Responses zeigen letzte 4 Chars mit Dot-Padding (z.B. `....Wf2x`) — Pattern-konform zu Stripe/GitHub-Secret-Masking.

**Worker-Logik (`worker.go` 218 LOC):**
- **WebhookWorker** — Stateless, horizontal skalierbar dank `FOR UPDATE SKIP LOCKED` in Repo.
- **Poll-Interval:** 5 Sekunden, **Batch-Size:** 10.
- **HTTP-Client:** 10s-Timeout, hardcoded — **kein Per-Webhook-Timeout-Override-Slot**.
- **HMAC-Signatur:** `X-Cosmi-Signature: sha256=<hex>` Header (sha256(secret, payload)). **Header:** `Content-Type: application/json`, `X-Cosmi-Event: submission.created`. **Aber:** der `X-Cosmi-Event`-Wert ist hardcoded auf `submission.created` — `events []string` im Webhook-Model ist Definition-Only, der Worker emit nur `submission.created`.
- **Backoff:** 30s → 2min → 10min → 30min → 2h.
- **Dead-Letter:** nach 5 Versuchen Status = `dead`.

**Sicherheits-Status (`backend/internal/formulare/`):**
- ✅ **Tenant-Isolation Phase 2** — alle Repo-Queries filtern `WHERE tenant_id = $1`, `tenant_isolation_phase2_test.go` vorhanden.
- ✅ **HMAC-Webhook-Signing** — sha256 mit per-Webhook-Secret.
- ✅ **Webhook-URL-Validation** — http/https-Scheme + Host-Required.
- ✅ **Permission-Guards** — `formulare:schemas:{read,write}`, `formulare:submissions:{read,write}`, `formulare:webhooks:write` (siehe `kmuhub/.knowledge/datenbank.md:179`).
- ✅ **Idempotency** — Gateway-Mittleware (Migration 105/108) — WarnMode aktiv.
- ⚠️ **KEIN SSRF-Schutz auf Webhook-URLs** — internes Network-Probing via Webhook-Worker-Egress moeglich (z.B. `http://169.254.169.254/...` AWS-Metadata, `http://localhost:6379` Redis). **Lesson aus Zammad 7.0.1 (W24-Carry-Forward, Helpdesk-Deepdive): SSRF via Webhooks war eine der 6 Pflicht-Fixes**. Cosmi-Formulare hat exakt dieselbe Angriffsflaeche.
- ⚠️ **KEIN Anti-Spam** auf Public-Form-Submissions — Honeypot/Captcha/Rate-Limit/Keyword-Filter fehlen alle.
- ⚠️ **IP-Address-DSGVO-Gate fehlt** — Models-Kommentar sagt "DSGVO: nur mit Consent", aber Service-Code stempelt IP unconditional (sofern parseable).
- ⚠️ **Kein Submission-Spam-Status** — `new/read/archived` — wenn ein Bot 10000 Submissions submittet, alle landen als `new` in der Inbox.

### Frontend (kmuhub/desktop/src/renderer/src/modules/formulare/, 2457 LOC)

- **FormularePage.tsx** — 2457 LOC Mono-File (Vergleich Helpdesk: 996 LOC). **Refactor-Schuld-Marker** — vor jedem weiteren Sprint-Item zu zerlegen.
- **api/formulare-client.ts** — 255 LOC, gRPC-Web-Client, alle 21 RPCs gewired.
- **api/formulare-types.ts** — 195 LOC, TS-Mirror der gRPC-Messages.
- **stores/formulare.ts** — 175 LOC Zustand-Store mit `persist` (Key `cosmi-formulare-draft`) fuer Editor-Draft-State.

### Strukturelle Diskrepanzen Backend ↔ Frontend (Stand 2026-06-15)

**Strukturelle Diskrepanz #1 — Field-Type-Union driftet:**
- Backend `validFieldTypes` (`service.go:42`): `text, textarea, email, number, select, radio, checkbox, date, file` (9 Typen).
- Frontend `FormFieldType` (`stores/formulare.ts:17`): `text, textarea, select, checkbox, radio, date, number, file` (8 Typen — **`email` fehlt**).
- Konsequenz: User koennte via Direct-gRPC-API eine Form mit `type: "email"` anlegen, Frontend kann das Feld nicht typsicher rendern.

**Strukturelle Diskrepanz #2 — FieldOption-Struktur driftet:**
- Backend `FieldOption` (`models.go:75`): `{Value string, Label string}` — Objekt mit Value-Label-Trennung.
- Frontend `FormField.options` (`stores/formulare.ts:33`): `string[]` — flacher String-Array.
- Konsequenz: Roundtrip-Loss von Option-Labels bei Frontend-Edit-Cycles (z.B. Backend hat `{value: "ch", label: "Schweiz"}`, Frontend zeigt nur `"ch"`).

**Strukturelle Diskrepanz #3 — FormAction (email/task/crm_contact) ist Frontend-only:**
- Frontend `FormAction` (`stores/formulare.ts:42`): `{type: 'email'|'task'|'crm_contact', config: Record<string,string>}` mit Kommentar **"frontend-only: post-submission actions (not yet persisted to backend)"**.
- Backend: keine `actions`-Spalte in `form_schemas`, kein `FormAction`-Modell, keine RPC fuer Action-CRUD.
- Konsequenz: User kann Email/Task/CRM-Actions im Editor konfigurieren — beim Speichern werden sie **stillschweigend weggeworfen**.

**Strukturelle Diskrepanz #4 — Page-Assignment driftet:**
- Backend `FormSchema.PageCount int` — globaler Page-Counter, keine Per-Field-Page-Assignment im `FormField`-Struct.
- Frontend `FormField.page?: number` (`stores/formulare.ts:39`) — Per-Field-Page-Assignment.
- Konsequenz: Multi-Page-Forms im Frontend zeigen Page-Layout, Backend speichert/laed nur PageCount (Anzahl) — Frontend muss Page-Zuordnung clientseitig rekonstruieren, fragil bei Schema-Edit-Konflikten.

**Lehre aus Helpdesk-Deepdive W24 (HelpdeskPage konsumiert Mocks statt React-Query-Hooks):** Cosmi-Formulare hat das **mildere Pendant** — keine Mock-Persistence, aber strukturelle Drift zwischen Frontend-Type-System und Backend-Schema. **Sprint-2-Hygiene-Item**: ein einziger 1-Sprint-Sweep, der alle 4 Diskrepanzen behebt, ist Voraussetzung fuer jeden weiteren Feature-Sprint. Wenn AI-Form-Generation phase 2 lanciert, muss das Type-System Backend-faithful sein.

---

## Konkurrenz-Vergleichstabelle

| Feature                              | Cosmi-Formulare | Typeform | Tally | Fillout | JotForm | Formspree | Formbricks |
|--------------------------------------|-----------------|----------|-------|---------|---------|-----------|------------|
| **Self-Host EU**                     | ✅ Frankfurt    | ❌       | ❌    | ❌      | ❌      | ❌        | ✅ Docker  |
| **Free-Tier Submissions**            | ✅ unlimited (Cosmi-Modul-Pricing) | 🟡 10/mo | ✅ unlimited | 🟡 1000/mo | 🟡 100/mo | 🟡 50/mo | ✅ unlimited (Self-Host) |
| **Field-Types-Anzahl**               | 🟡 9            | ✅ 30+   | ✅ 20+ | ✅ 40+  | ✅ 30+  | n/a (Backend) | 🟡 ~15 |
| **Conditional Logic**                | 🟡 1-Cond (eq/neq/contains) | ✅ Multi-Cond+AND/OR | ✅ Multi-Cond | ✅ Multi-Cond+DB-Query | ✅ Multi-Cond | n/a | ✅ Event-based |
| **Calculation/Computed Fields**      | ❌              | ✅       | ❌    | ✅      | ✅      | n/a       | ❌         |
| **Native E-Signature**               | ❌              | ❌       | ✅ (Pro) | ✅    | ✅      | ❌        | ❌         |
| **Native Payment (Stripe)**          | ❌              | ✅       | ✅    | ✅      | ✅      | ❌        | ❌         |
| **File-Upload-Backend**              | 🚧 Field-Type exists, no storage hook | ✅ | ✅ 10MB Free | ✅ (Business) | ✅ | 🟡 1GB Personal | 🟡 Beta |
| **Multi-Page Forms**                 | 🟡 PageCount-Only (no per-field assignment) | ✅ | ✅ | ✅ | ✅ | n/a | ✅ |
| **Partial Submissions**              | ❌              | ✅       | ✅ (Pro) | ✅    | ✅      | ❌        | ✅         |
| **Hidden Fields / URL-Pre-Fill**     | ❌              | ✅       | ✅    | ✅      | ✅      | n/a       | ✅         |
| **Honeypot / Anti-Spam-Default**     | ❌ **FEHLT**    | ✅       | ✅    | ✅      | ✅      | ✅        | ✅         |
| **Captcha-Slot (Turnstile/hCaptcha)**| ❌ **FEHLT**    | ✅       | ✅    | ✅      | ✅      | ✅ reCAPTCHA | ✅        |
| **Rate-Limit pro Form/IP**           | ❌ **FEHLT**    | ✅       | ✅    | ✅      | ✅      | ✅        | ✅         |
| **Webhook (HMAC-Signed)**            | ✅ sha256       | ✅       | 🟡 (Pro) | ✅   | ✅      | 🟡 ($99 Gold) | ✅      |
| **Webhook Exp-Backoff + Dead-Letter**| ✅ 30s/2m/10m/30m/2h, 5 attempts | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CSV/XLSX-Export**                  | ✅ BOM-UTF-8 + excelize | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI Form-Generation (Prompt/PDF)**  | ❌ **FEHLT**    | ✅ (Q1 2026) | 🚧 via MCP | ✅ | ✅ | ❌ | ❌ |
| **AI Follow-Up-Questions**           | ❌              | ✅       | ❌    | ❌      | ❌      | ❌        | ❌         |
| **AI-Pre-Fill / Enrichment**         | ❌              | ✅ Data Enrichment 2026 | ❌ | ❌ | ❌ | ❌ | ❌ |
| **MCP-Server (Claude/ChatGPT)**      | ❌              | 🚧 Beta  | ✅ Native (Free) | ❌ | ✅ Paid | ❌ | ❌ |
| **Database-Connector-Bibliothek**    | 🟡 Cross-Modul-direct (kein extern) | 🟡 wenig | 🟡 Notion/Sheets | ✅ Notion/Airtable/SF/HS | ✅ | ❌ | 🟡 |
| **EU-AI-Act Art. 50 Disclosure**     | n/a (keine AI) | ⚠️ retrofit | ⚠️ retrofit (MCP) | ⚠️ retrofit | ⚠️ retrofit | n/a | n/a |
| **SOC-2-Type-II**                    | ❌              | ✅       | 🟡 Cloud | ✅ | ✅ | ✅ | ✅ (4.7 2026) |
| **Submission-Spam-Status**           | ❌ (nur new/read/archived) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **SSRF-Schutz (Webhook-Egress)**     | ❌ **FEHLT**    | ✅       | ✅    | ✅      | ✅      | ✅        | ✅         |
| **Pricing-Start (€/User-Monat)**     | **2 EUR**       | $25 ($83 fuer 10000) | $0 Free, $29 Pro | $19 Starter | $34 Bronze | $15 Personal | $0 Self-Host |

**Lesarten der Tabelle:**

(1) **Cosmi gewinnt eindeutig auf 4 Achsen**: Self-Host-EU + Cosmi-Modul-Pricing (2 EUR vs $19-$83) + Webhook-HMAC-Exp-Backoff-Tiefe (architektonisch sehr sauber) + Cross-Modul-Datenanbindung (kein externer-Connector-Pflege-Schuld).

(2) **Cosmi verliert massiv auf 4 Achsen** — alle sind **dringend zu schliessen vor Public-GA**:
- Anti-Spam-Trias (Honeypot + Captcha + Rate-Limit) — **Pflicht-Stake VOR Public-Form-GA** (siehe Top-3 #1).
- AI-Form-Generation — **Tabellenstake fuer Q1 2027**, mit Cross-Modul-Differenzierung (siehe Top-3 #2).
- Field-Type-Breite (9 vs 30+) — kein P0, aber `signature`/`payment`/`calculation`/`rating`-Felder sind im KMU-Onboarding-Form-Use-Case high-value.
- SSRF-Webhook-Egress-Schutz — **Production-Risk** (siehe Top-3 #3).

(3) **Cosmi liegt im Mittelfeld** auf File-Upload (Field-Type existiert, kein Storage-Hook), Multi-Page (PageCount-Only), Conditional Logic (Single-Cond).

---

## Top-3 Strategische Empfehlungen

### 1. **Anti-Spam-Trias als Pflicht-Stake VOR Public-Form-GA** (Sprint S2.W?, vor jedem Customer-Pilot mit oeffentlicher Form)

**Was:** Drei Anti-Spam-Pattern als Hard-Required-Schicht in `service.go::CreateSubmission` und `models.go` einbauen, **bevor** die erste oeffentliche Form (z.B. Cosmi-Marketing-Site-Lead-Form, Cosmi-Kunden-Public-Bewerbungsform) live geht.

**Konkrete Sprint-Items:**

(a) **Honeypot-Pflichtfeld** — neuer FormField-Type `honeypot` (intern, niemals gerendert), Frontend rendert hidden Input mit `display: none + tabindex=-1 + autocomplete=off`. Backend-Service rejected jede Submission mit nicht-leerem Honeypot-Wert (HTTP 200 OK an Client zurueck, aber `status=spam` in DB). **Sprint-Aufwand:** 1 Tag Frontend + 1 Tag Backend + 1 Tag Tests = 3 Tage.

(b) **Captcha-Slot mit Provider-Wahl** — analog zum Zammad-Pattern (7 LLM-Provider-Wahl im Helpdesk-Deepdive W24): Captcha-Provider-Wahl im Form-Schema-Editor — `none / honeypot-only / cloudflare-turnstile / hcaptcha-privacy / native-math` mit DACH-KMU-Default `honeypot-only + cloudflare-turnstile`. **Site-Key + Secret per Tenant-Settings** (nicht Cosmi-zentral, damit Kunde eigenen Turnstile-Account hat → DSGVO-AVV-frei zu Cosmi). **Sprint-Aufwand:** 3 Tage Backend (Verify-API-Calls) + 2 Tage Frontend + 2 Tage Tests = 7 Tage.

(c) **Rate-Limit** — Redis-basiert (Cosmi hat Redis-Infrastruktur, siehe `kmuhub/.knowledge/stack.md`): 10 Submissions/IP/Minute, 1000 Submissions/Form/Tag, konfigurierbar pro Schema. **Submission-Status erweitern um `spam`** (Migration: `ALTER TYPE form_submission_status ADD VALUE 'spam';`) und neuer Status `pending_review` (Reserve fuer AI-Spam-Erkennung Phase 2). **Sprint-Aufwand:** 2 Tage Redis-Layer + 1 Tag Migration + 1 Tag Tests = 4 Tage.

(d) **SSRF-Schutz auf Webhook-URLs** — `validateWebhookURL` erweitern: privater-IP-Range-Block (RFC1918 + `169.254.0.0/16` AWS-Metadata + `::1` IPv6-Loopback), Domain-Blacklist (z.B. `metadata.google.internal`, `metadata.azure.com`), Cosmi-eigene-Domains blocken (Self-DDoS-Schutz). **Lesson aus Zammad 7.0.1 (Helpdesk-Deepdive W24): SSRF via Webhooks war 1 der 6 P0-Fixes**. **Sprint-Aufwand:** 2 Tage.

**Begruendung:** EDPB CEF 2026 (Art. 12-14 Transparenz-Enforcement) laeuft seit Maerz 2026, OLG-Hamm-Urteil zu AI-Vorausfuellung als Carry-Forward seit W20, Cloudflare-Turnstile-WebGL-Fingerprinting-Pruefpflicht seit W23 (siehe `weekly/2026-W23.md:319`). Die erste Public-Form ueber Cosmi-Customer-Tenant kann **innerhalb 60 Tagen** scheitern, wenn ein Bot 10000 Bewerbungsformulare submitted — und Cosmi hat dann ein Production-Incident, ein DSGVO-Compliance-Problem (IP-Logging ohne Consent + Spam-Datenflut) und einen Public-Trust-Loss-Moment. **Total-Sprint-Aufwand:** ~16 Tage (3+7+4+2) — ein Sprint-Item, voll committed.

### 2. **AI-Form-Generation als Cross-Modul-Hebel, NICHT als Standalone-AI-Feature** (Sprint Q4 2026 / Q1 2027, Architektur jetzt entwerfen)

**Was:** Cosmi-Formulare bekommt eine AI-Layer, die **strukturell Cross-Modul** ist — nicht "Typeform-AI-Clone", sondern "Cosmi-AI generiert Form-Schemas aus existierenden Cosmi-Modul-Daten als Wissensbasis".

**Konkrete Architektur-Items (entwerfen jetzt, bauen Q4 2026 / Q1 2027):**

(a) **AI-Provider-Wahl-Architektur** (analog Zammad-7-Provider-Pattern aus Helpdesk-Deepdive W24, analog Wiki-Deepdive-Empfehlung): Cosmi-AI (EU-Hosted, GDPR-konform), OpenAI, Anthropic Claude, Azure AI, Mistral AI, Ollama (lokal Self-Host), Custom (OpenAI-API-Compatible). **Tenant-konfigurierbar** in `settings.ai_provider` JSONB.

(b) **Cross-Modul-Schema-Source** (Cosmi-USP):
- `GenerateFromCrmContact(contact_id)` → erzeugt Form-Schema aus allen Contact-Custom-Fields (Standard + Tenant-Custom-Fields).
- `GenerateFromHelpdeskCategory(category)` → erzeugt FAQ-/Reklamations-Form-Schema aus Helpdesk-Category-Felder + Canned-Responses als Pre-Fill.
- `GenerateFromWikiArticle(article_id)` → erzeugt Onboarding-/Quiz-Form aus Wiki-Article-Strukturen.
- `GenerateFromRapporteVorlage(template_id)` → erzeugt Customer-Self-Report-Form aus Rapporte-Template-Strukturen.
- `GenerateFromVertragsklausel(clause_id)` → erzeugt eIDAS-Pre-Sign-Form (Datenerhebung VOR Signatur) aus Vertraege-Klausel-Variablen.
- **Generic-Fallback**: `GenerateFromPrompt(prompt)` analog zu Typeform AI.

(c) **EU-AI-Act Art. 50 Disclosure-by-Design** — vor JEDEM AI-generated Field im Form-Builder rendert das Frontend "AI-generated, please review" Badge. Public-Forms zeigen "AI-generated form template, customised by [Tenant-Name]" Footer. Audit-Log: jedes AI-Call wird in `audit_log` mit Provider + Prompt-Hash + Tenant-User-ID gestempelt (3-Jahre-Retention fuer Art. 50 Beweis). **Lesson aus Helpdesk-Deepdive W24:** Cosmi hat einen strukturellen Vorteil — Disclosure-by-Design VOR der ersten AI-Funktion einbauen, nicht retrofit.

(d) **OLG-Hamm-Compliance** (W20-Carry-Forward) — AI-Vorausfuellung von Formularfeldern muss "Disclaimer-Pflicht + Human-in-the-Loop" liefern: AI-vorausgefuellte Felder sind defaulted auf `disabled`, User muss explizit "AI-Vorschlag uebernehmen"-Click pro Feld machen (kein Auto-Submit von AI-Daten).

(e) **MCP-Server (`cosmi-formulare-mcp`)** als Trans-Phase-1 Lieferung — Cosmis 21 gRPC-RPCs sind bereits da, MCP-Adapter ist ein Sprint-Item: gRPC-RPC → MCP-Tool-Mapping. **Cross-Modul-Differenzierung gegen Tally-MCP**: Cosmi-MCP exposes Form-Tools + CRM-Tools + Helpdesk-Tools + Wiki-Tools — der KMU-Anwender sagt zu Claude: "Erstell Form X, lege auf Submission CRM-Kontakt an, fuege das in Helpdesk-Welcome-Workflow ein, verlinke Onboarding-Wiki-Article" — Tally-MCP kann nicht. **Sprint-Aufwand MCP-Server-Layer:** 5-7 Tage (gRPC → MCP-Tool-Adapter + OAuth-Auth-Wrapper + Safety-Guardrails).

**Begruendung:** Typeform Q1/Q2 2026 hat AI-Data-Enrichment + AI-Memory + Growth-Flow + Research-Flow gestapelt — 4 AI-Releases in 5 Monaten. Fillout AI-from-PDF/Prompt. JotForm AI Agents + Voice. Tally MCP. **Cosmi-Formulare ohne AI-Pfad-Konzept ab Q4 2026 wird im KMU-Sales-Pitch als "alte Welt" empfunden** — und Cosmi-Sales kann nicht Cross-Modul-USP gegen AI-Standalone-Feature trumpfen, ohne dass beide Achsen mindestens **vorhanden** sind. **Cross-Modul-Hebel ist der einzige strategisch verteidigbare Pfad** — Cosmi kann nicht "AI besser als Typeform" gewinnen, aber Cosmi kann "AI aus Deinen integrierten Cosmi-Daten" gewinnen, das Typeform/Fillout/JotForm strukturell nicht koennen (keine eigene CRM/Helpdesk/Wiki-Datenbasis).

### 3. **Anti-Drift-Sweep Backend ↔ Frontend + FormularePage.tsx-Refactor** (Sprint-Hygiene VOR Sprint 2 AI-Investment)

**Was:** Die 4 strukturellen Diskrepanzen aus dem Cosmi-IST-Stand-Block in einem einzigen 1-Sprint-Sweep beheben + FormularePage.tsx Mono-File-Refactor.

**Konkrete Sprint-Items:**

(a) **Field-Type-Union faithful**: Frontend `FormFieldType` um `'email'` erweitern, alle Field-Renderer + Validators auf 9-Typen-Schema synchronisieren. **Aufwand:** 1 Tag.

(b) **FieldOption-Struktur faithful**: Frontend `FormField.options` von `string[]` auf `FieldOption[]` (`{value, label}`) migrieren. **Migration-Path:** Frontend liest beide Formate beim Load, schreibt nur neues Format beim Save. Backwards-compat-Read fuer 30 Tage, dann harten Schema-Cutover. **Aufwand:** 2 Tage Frontend + 1 Tag Tests = 3 Tage.

(c) **FormAction (email/task/crm_contact) Backend-Persistence**: Neue Migration mit `form_actions`-Tabelle (`id, form_schema_id, type, config JSONB, created_at`), neue gRPC-RPCs `CreateFormAction / ListFormActions / DeleteFormAction`, Worker-Erweiterung in `worker.go` der bei Submission die Actions abarbeitet (Email via Cosmi-Email-Modul, Task via Cosmi-Task-Modul, CRM-Contact via Cosmi-CRM-Modul). **Cross-Modul-Hebel als Praxis-Beispiel fuer Top-3 #2.** **Aufwand:** 1 Tag Migration + 3 Tage Backend (Service + Worker) + 1 Tag gRPC-Wiring + 2 Tage Frontend-Re-Hookup + 2 Tage Tests = 9 Tage.

(d) **Page-Assignment faithful**: Backend `FormField` um `Page int` erweitern (additiv, default 1, Migration-Free dank JSONB), validateFields prueft `page >= 1 && page <= PageCount`. **Aufwand:** 2 Tage Backend + 1 Tag Frontend + 1 Tag Tests = 4 Tage.

(e) **FormularePage.tsx 2457 LOC Mono-File-Refactor** in 6-8 Sub-Components: `FormBuilder.tsx` (Editor-Pane), `FormFieldList.tsx` (Drag-Drop-Liste), `FormFieldEditor.tsx` (Single-Field-Editor), `FormPreview.tsx` (Live-Preview), `FormSubmissionsTable.tsx` (Submission-List), `FormWebhooksPanel.tsx` (Webhook-Config), `FormStatsCard.tsx`, `FormActionsPanel.tsx` (neu in (c)). **Aufwand:** 4-5 Tage (kein Test-Aufwand, da nur File-Split).

**Begruendung:** **Lesson aus Helpdesk-Deepdive W24** (HelpdeskPage konsumiert Mocks statt React-Query-Hooks): wenn Frontend und Backend driften, jeder weitere Feature-Sprint wird teurer und buggy. Cosmi-Formulare hat **heute** vier kleine Drift-Schulden + ein UI-Refactor-Schuld-Marker (2457-LOC-Mono-File). **Wenn Top-3 #2 (AI-Generation Q4 2026 / Q1 2027) gestartet wird OHNE diesen Sweep**, addiert sich AI-Komplexitaet auf existierende Type-Drift — und das ist genau das Pattern, das in Helpdesk-Deepdive W24 als "strukturelle Diskrepanz #1" mehrfach beobachtet wurde. **Total-Sprint-Aufwand:** ~21 Tage (1+3+9+4+5) — ein Sprint, voll committed, VOR jedem Q4-AI-Investment.

---

## Sources

**Cosmi-interne Quellen (Code + Knowledge):**
- `/opt/kmuhub/backend/internal/formulare/` — 3870 LOC ueber 8 Files (errors, models, postgres_repository, repository, service, worker + 3 Test-Files)
- `/opt/kmuhub/backend/proto/formulare/v1/formulare.proto` — 21 gRPC-RPCs, 4 Resource-Gruppen
- `/opt/kmuhub/desktop/src/renderer/src/modules/formulare/FormularePage.tsx` — 2457 LOC Mono-File
- `/opt/kmuhub/desktop/src/renderer/src/stores/formulare.ts` — Zustand-Store mit FormAction-Stub
- `/opt/kmuhub/.knowledge/datenbank.md:173-179` — Formulare-Schema-Doku (Migration 081)
- `/opt/kmuhub/.knowledge/pricing.md:69` — Cosmi-Formulare 2 EUR vs Typeform ab 25
- `/opt/kmuhub/.knowledge/architektur.md:26,93` — Service-Port :50064, Gateway-Route `route_formulare.go`
- `/opt/kmuhub/.knowledge/security.md:35,106,179` — Permission-Seed-Pflicht (Lesson 2026-06-05), Tenant-Isolation-Welle-3

**Zentria-intel Carry-Forward-Quellen:**
- `/opt/zentria-intel/weekly/2026-W20.md:113,247-250` — OLG-Hamm-Urteil zu AI-Vorausfuellung, Disclaimer + Human-in-the-Loop
- `/opt/zentria-intel/weekly/2026-W22.md:316-322` — noyb-Sieg ORF.at Cookie-Banner Equal-Prominence (Frontend-Audit-Task fuer Cosmi-Formulare mit Consent-Feldern)
- `/opt/zentria-intel/weekly/2026-W23.md:319-325` — Cloudflare Turnstile WebGL-Fingerprinting (DSGVO-Frage), NOYB vs Schibsted "Pay or Okay"
- `/opt/zentria-intel/daily/2026-06-01-morning.md:63-64` — EDPB CEF 2026 Art. 12-14 Transparenz-Enforcement (25 EU-DSBs aktiv seit Maerz 2026)
- `/opt/zentria-intel/daily/2026-06-04-evening.md:204` — Cosmi-AI in CRM/Helpdesk/Formulare braucht `backend/internal/ai/security/containment-policy.md`
- `/opt/zentria-intel/daily/2026-06-05-evening.md:189-194` — EDPB Plenum 08.-09.06., Cosmi-Forms-Praefcheck
- `/opt/zentria-intel/monthly/2026-06-08-deepdive-helpdesk.md` — Lesson 7-LLM-Provider-Wahl, SSRF-via-Webhooks-CVE-Risk, Disclosure-by-Design

**Externe Web-Quellen (Top-Quellen, Stand 2026-06-15):**

- [Typeform Pricing 2026: Free to Business Plans](https://automationatlas.io/answers/typeform-pricing-explained-2026/) — Basic $25, Plus $50, Business $83, Growth Pro $291
- [Typeform launches AI data enrichment to improve lead conversion (4 Feb 2026)](https://www.typeform.com/blog/typeform-launches-ai-data-enrichment-to-improve-lead-conversion)
- [Typeform launches AI engagement platform to turn forms into workflows](https://www.typeform.com/blog/typeform-launches-ai-engagement-platform)
- [Typeform Growth Flow (Mai 2026)](https://www.typeform.com/blog/typeform-drives-a-new-era-of-customer-engagement-with-growth-flow)
- [Typeform Research Flow (9 Juni 2026)](https://agilebrandguide.com/typeform-launches-research-flow-to-help-teams-uncover-deeper-insights-in-hours-not-weeks/)
- [Tally Pricing 2026 — Free Unlimited Submissions](https://tally.so/pricing)
- [Tally Reviews 2026: 4.9/5 G2-Rating](https://www.g2.com/products/tally-forms-tally/reviews)
- [Best MCP Form Builders in 2026 (Tally, JotForm, Typeform)](https://tally.so/help/best-mcp-form-builders)
- [AI Form Builders Are Becoming Table Stakes (MCP Form Operations)](https://dev.to/lovanaut55/ai-form-builders-are-becoming-table-stakes-mcp-form-operations-are-the-hard-part-22ia)
- [JotForm AI Agents Pricing & Features 2026](https://www.jotform.com/pricing/)
- [JotForm MCP Server: Connect Form Builder with AI](https://www.jotform.com/mcp/)
- [Fillout: Form Builder & Automation (April 2026)](https://automationatlas.io/tools/fillout/)
- [Fillout Software Pricing, Alternatives 2026 (Capterra)](https://www.capterra.com/p/10002520/Fillout/)
- [Formspree Alternatives in 2026: Open Source, Self-Hostable](https://formgrid.dev/blog/formspree-alternatives-in-2026-open-source-cheaper-and-self-hostable)
- [Formbricks Open Source Self-Hosted Typeform Alternative](https://formbricks.com/typeform-alternative)
- [Formbricks 4.7 Release: SOC-2-Type-II + Attribute-Data-Types](https://formbricks.com/blog)
- [EU AI Act Article 50 Compliance Checklist — 2 August 2026 Deadline](https://getproofsnap.com/eu-ai-act-deadline.html)
- [10 Takeaways: European Commission Draft Guidelines on AI Transparency (Mai 2026)](https://www.globalpolicywatch.com/2026/05/10-takeaways-european-commission-draft-guidelines-on-ai-transparency-under-the-eu-ai-act/)
- [EU AI Act Article 50: Transparency & AI Content Labelling Guide](https://euaicompass.com/eu-ai-act-article-50-transparency-guide.html)
- [Honeypot, CAPTCHA, AI: Anti-Bot Solutions for Forms 2026](https://prospect-hub.app/en/blog/honeypot-captcha-ai-anti-bot-comparison/)
- [8 Best GDPR Compliant Form Builders in 2026](https://formbuilder.tools/type/gdpr-compliant)
- [DocuSign Web Forms — embedded e-signature forms](https://www.docusign.com/products/web-forms)

---

## Picks (vorgeschlagen)

- [ ] 🔴 **Anti-Spam-Trias als P0 Sprint-Item VOR Public-Form-GA** (Honeypot + Captcha-Slot + Rate-Limit + SSRF-Schutz) — `backend/internal/formulare/{service.go,worker.go,models.go}`, Migration neuer Status `spam`, neuer FormField-Type `honeypot`. Owner: Backend-Lead. Frist: vor erstem Customer-Pilot mit `IsPublic=true`-Form. Aufwand: ~16 Tage.

- [ ] 🟢 **AI-Form-Generation als Cross-Modul-Hebel architektonisch entwerfen** — `docs/architecture/ai-formulare-cross-modul.md`, mit 7-LLM-Provider-Wahl + `GenerateFromCrmContact/Helpdesk/Wiki/Rapporte/Vertraege` + Disclosure-by-Design + OLG-Hamm-Human-in-the-Loop-Default. Architektur jetzt, Implementation Q4 2026 / Q1 2027. Owner: Architecture-Lead + Sales-Stakeholder (KMU-Demo-Use-Case-Validation).

- [ ] 🟡 **Anti-Drift-Sweep Backend ↔ Frontend + FormularePage.tsx-Refactor** — 4 strukturelle Diskrepanzen beheben (Field-Type-Union, FieldOption-Struktur, FormAction-Backend-Persistence, Page-Assignment) + Mono-File-Split. Sprint-Hygiene VOR Q4-AI-Investment. Aufwand: ~21 Tage.

- [ ] 🟡 **MCP-Server (`cosmi-formulare-mcp`) als 2-Wochen-Spike** — Tally-/JotForm-Pattern adaptieren, Cross-Modul-Hebel: Form-Tools + CRM-Tools + Helpdesk-Tools + Wiki-Tools im selben MCP-Server. Sales-Demo-Wert: "Cosmi-MCP fuer Claude/ChatGPT" als KMU-Differenzierungs-Asset. Aufwand: 5-7 Tage.

- [ ] 🟢 **Cloudflare-Turnstile-Audit auf cosmi.app + Marketing-Site** — Carry-Forward aus W23-Empfehlung (`backend/internal/forms/captcha/`, `infrastructure/cloudflare/`, `backend/internal/forms/consent-management/`). Owner: DevOps + Datenschutz. Frist: vor naechstem Customer-Onboarding mit Cosmi-Public-Form.

- [ ] 🟢 **Followup-Marker 30d: Typeform AI Memory + Growth Flow + Research Flow Adoption-Daten** — sind die drei Q1/Q2-2026-Releases bei DACH-KMU-Markt adoptiert? Wenn ja, AI-Form-Generation-Pflicht-Stake fuer Cosmi vorziehen auf Q3 2026. Frist: 2026-07-15 (KW29).

- [ ] 🟢 **EU-AI-Act Art. 50 Compliance-Checkliste fuer alle Cosmi-Module mit AI-Roadmap** (formulare/crm/helpdesk/wiki/vertraege/dialer/video) — `docs/compliance/eu-ai-act-article-50-checklist.md` mit Disclosure-by-Design-Pattern aus Helpdesk-Deepdive W24 + Formulare-Deepdive W25 + OLG-Hamm-Lessons. Frist: vor 2. August 2026 (Article-50-Stichtag).

- [ ] 🟢 **SOC-2-Type-II Roadmap-Marker** — Formbricks 4.7 hat SOC-2-Type-II als 2026-Stake gesetzt. Cosmi-Modul-Status-Pruefung: welche Module sind SOC-2-Type-II-tauglich (Tenant-Isolation + Audit-Log + Permission-Guards alle vorhanden), welche sind das nicht. Owner: Security-Lead.
