---
year: 2026
week: 26
modul: vertraege
created: 2026-06-22
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 51
tokens_input: ~310000
tokens_output: ~17800
rotation_position: 7/15
---

# Deepdive: vertraege (Mo W26/2026)

> **Siebter Deepdive der Rotation.** Vorgaenger: `crm-core` (W19, 2026-05-11), `dialer` (W20, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01), `helpdesk` (W24, 2026-06-08), `formulare` (W25, 2026-06-15). Naechstes Modul gemaess Rotation: **buchhaltung** (KW27, 2026-06-29). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-vertraege (2026-06-22):** Backend `backend/internal/vertraege/` (11 Files, **2425 LOC** mit ~1148 Test-LOC, Production-Code ~1277 LOC — `models.go` 109, `service.go` 474, `postgres_repository.go` 450, `worker.go` 148, `repository.go` 53, `event_emitter.go` 31, `errors.go` 12). **15 gRPC-RPCs** hinter `modules.vertraege`-Flag: 5 Contract-RPCs (Create/Update/Delete/Get/List), 3 Party-RPCs (Add/Remove/List), 4 Reminder-RPCs (Create/Update/Delete/List), 1 ExportContract (TXT-Stub — TODO Sprint 3 PDF), 1 SaveSignature (EES inline), 1 UploadDocument (deprecated — Client-Side-Presign-Flow via `route_files.go`). **3 Domain-Modelle**: Contract (mit ContractNumber, Type `rental/service/employment/nda/other`, Status `draft/active/expired/terminated`, StartsOn/EndsOn `*time.Time`, DocumentURL `*string` → MinIO-Path, **SignatureProvider `*string` mit Comment "Phase D: Skribble" — Placeholder, kein Code-Pfad**, SignatureData `*string` base64 PNG/SVG inline, SignedAt/SignedBy), ContractParty (Type `contact/company/external` + RoleInContract + SignedOn), ContractReminder (RemindAt + Type `renewal/expiry/payment/custom` + Subject/Message + Status `pending/sent/cancelled`). **Worker** `ReminderWorker`: 5-min-Poll fuer Due-Reminders, 60-min-Poll fuer Contract-Expiry, atomare `ClaimDueReminders` (Status=sent in Single-TX, idempotent), `EmitReminderEvent` → Notification-Service (`models.EventPayload` mit `EventVertraegeReminderDue` + DeepLink `/vertraege/{id}` + GroupKey `vertraege.reminder.{contract_id}`), `ExpireContracts` markiert abgelaufene Contracts auf `status=expired`. **Signatur-Stack**: NUR EES inline (Canvas-PNG/SVG, max 1 MiB, MIME-Prefix-Validation `data:image/png;base64,` oder `data:image/svg+xml;base64,`), KEINE Skribble/DocuSign/PandaDoc-Anbindung (Provider-Field ist Stub). Migrationen: 000089 (create vertraege), 000090 (seed permissions), 000143 (add signature columns zu rapporte/vermietung/vertraege gemeinsam). Frontend `desktop/src/renderer/src/modules/vertraege/`: 3 .tsx-Files **3404 LOC** (VertraegePage 2417 LOC Mono-File, ESignaturDialog 615 LOC, settings/VertraegeSettingsPanel 372 LOC) + Hook `useContractReminders.ts` + `api/vertraege-client.ts` (191 LOC) + `api/vertraege-types.ts` (146 LOC) + Stores `vertraege.ts` (848 LOC, Zustand+persist) + `vertraegePrefs.ts` (39 LOC) + `vertraegeSettings.ts` (97 LOC). Pricing-Anker (`KMU-Hub/.knowledge/pricing.md` Pattern): **2 EUR/User-Monat** als Cosmi-Modul-Anker — Skribble alleine startet bei CHF 9/Monat fuer Basis + CHF 1.80 pro QES.

> **Vier strukturelle Diskrepanzen zwischen Backend und Frontend identifiziert (Status: 2026-06-22).** **#1 Contract-Type-Union driftet schwer:** Backend `ContractType` whitelistet 5 generische Werte (`rental/service/employment/nda/other`), Frontend `Contract['type']` listet 6 deutsche Domain-Werte (`mietvertrag/liefervertrag/servicevertrag/arbeitsvertrag/lizenz/versicherung`) — **kein einziges Mapping**, kein Migration-Path, kein i18n-Layer. Ein Mietvertrag im Frontend kommt als `rental` aus dem Backend zurueck, ein Liefervertrag hat keine Backend-Repraesentation, ein Versicherungsvertrag landet als `other`. **#2 Multi-Signer-Workflow ist Frontend-only Mock:** Backend Contract hat Single-Signature (`SignatureData/SignedAt/SignedBy` als drei Felder), Frontend `ContractSigner[]` Array mit 5-stufigem Workflow-Status (`pending/sent/viewed/signed/declined`) + `order` + `signedVia: 'canvas' | 'dispatch'` + Per-Signer `signatureDataUrl`. Dispatch-Workflow (Email-Versand an externen Signer) existiert nur als Frontend-Stub. Backend kennt keinen Signer-Lifecycle — beim Reload verliert man den Multi-Signer-State, wenn nicht auf persist-Store gespeichert. **#3 Multi-Document-Anhang ist Frontend-only:** Backend Contract hat einen einzigen `DocumentURL *string` (MinIO-Path), Frontend `ContractDocument[]` Array (mit fileId, name, mimeType, size, addedAt). Der `documentRef` ist als `@deprecated`-Migration-Marker, das echte Multi-File-Feature lebt nur Frontend-seitig. **#4 CRM-/Deal-/Invoice-Linking ist Frontend-only Schicht:** Frontend `contactId/contactName/dealId/dealTitle/invoiceIds/invoiceNames` — Backend Contract-Model hat keine dieser Verknuepfungen, kein `entity_links`-Join-Table, kein RPC. Die "Vertraege-CRM-Brille" (W23-Milestone-Notiz, vgl. `milestones.md` "vertraege-API-Swap auf entity_links" als Backend-Bedarf) ist seit 2026-06-11 als offener Posten dokumentiert. **Konsequenz:** Die Lehre aus Helpdesk-Deepdive W24 (HelpdeskPage konsumiert Mocks) und Formulare-Deepdive W25 (FormField-Typen driften) ist hier am extremsten — vertraege hat eine **Frontend-Domain-Schicht, die Backend-Persistenz weit ueberholt**. Vor jedem CLM-Feature-Sprint (Templates, Bulk-Generation, AI-Klausel-Detektion) MUSS der Backend-Catch-Up-Sweep stattfinden, sonst wird jeder neue Feature auf Sand gebaut. Konkret: **(a) ContractType-Mapping-Tabelle als Migration 0225** (deutsche Domain-Codes als kanonische Werte, Backend-Migration old→new), **(b) `contract_signers` Tabelle + 5 neue RPCs** (CreateSigner/UpdateSignerStatus/SendDispatch/RevokeSigner/ListSigners) — strikt vor Skribble-Integration, **(c) `contract_documents` Many-to-One-Tabelle** mit FileId+OrderIndex, **(d) `vertraege_entity_links` Polymorphe-Tabelle** zu Contact/Deal/Invoice/Company/Project.

> **Leit-Signal der Woche:** **Heute (Mo 2026-06-22) trifft HubSpot Revenue Hub GA den Cosmi-vertraege-Markt** — siehe Morning-Pulse `daily/2026-06-22-morning.md` Item `MOR-2026-06-22-i04` als **COMPETITOR-SUPERIOR**: Quotes + Vertraege + Billing + AI in einem CRM-Hub, Free-Tier fuer Basis-Invoicing, Pro/Enterprise mit e-Signatur + Analytics, Breeze AI Assistant + Revenue Agent fuer automatisches Invoice-Follow-up. Das attackiert Cosmi-vertraege+crm-core+buchhaltung gleichzeitig — Hubspot baut den Cross-Modul-Hebel, den Cosmi-Sales-Doktrin als USP positioniert (vgl. Formulare-Deepdive W25 "Cross-Modul-Hebel ist USP gegen Standalone-Tools"). **Dritte Schockwellen treffen den Vertrags-Markt 2026** — (a) **Agentic CLM ist die Tabellenstake**: DocuSign Iris-AI-Engine + Iris-Agents (Jan/Maerz/Mai 2026), Ironclad Intake/Renewal/Cost-Savings/Archive-Agents (April-2026-Early-Access), LinkSquares All-Agentic CLM GA, Sirion Obligation-Tracking-Agents. Jeder dieser Anbieter pitcht "AI uebernimmt Review/Renewal/Risk-Flag/Obligation-Tracking ohne Mensch dazwischen". Cosmi-vertraege hat **null AI-Funktion** — kein Klausel-Extractor, kein Renewal-Brief-Generator, kein Risiko-Scorer. (b) **eIDAS 2.0 EUDI-Wallet trifft Dezember 2026 als 27-MS-Pflicht** — jedes EU-Land MUSS Wallets ausrollen, QES via Smartphone wird Standard, Relying-Parties (Telco/Health/Travel/Energy) muessen ab 2027 EUDI-Wallet-basierte Identifikation akzeptieren. Cosmi-Skribble-Provider-Field ist Placeholder seit Sprint-1 (Code-Comment "Phase D"), aber **die strategische Pflicht-Phase ist eIDAS-Wallet-Bereitschaft, nicht Skribble-Anbindung** — Skribble-Integration ist Sprint-Item, EUDI-Wallet-Akzeptanz ist Roadmap-Marker. (c) **EU-AI-Act Article 50 trifft am 2. August 2026 jede AI-Vertrags-Funktion** + **EU-Data-Act B2B-FRAND-Klauseln** trifft seit 12. September 2025 alle B2B-Daten-Sharing-Vertraege (alte Vertraege ab 12. September 2027): Cosmi-vertraege HEUTE: keine AI = compliance-frei, aber dann: jede zukuenftige AI-Klausel-Detektion (W22-W25-Pattern: Hilfe-Tools wollen AI haben) MUSS mit Article-50-Disclosure ("AI screens clauses") + Human-in-the-Loop ausgeliefert werden. Plus: **BGH 25.02.2026 II ZB 13/24** (Cross-Border-QES Anerkennung Oesterreich→Deutschland — wird abgelehnt wenn Verfahren nicht gleichwertig) + **BGH 11.03.2026 I ZR 202/25** (Textform-Einhaltung via Email-Austausch) sind die zwei juristischen Anker-Urteile 2026 fuer DACH-Vertragsdigitalisierung. **Dieser Bericht empfiehlt drei Pflicht-Stakes vor jeder Sprint-3-PDF-Renderer-Phase und vor jeder AI-Klausel-Phase.**

---

## State-of-the-Art

Der Vertrags-/CLM-Markt Mitte 2026 ist nicht mehr "DocuSign vs Adobe Sign vs HelloSign" — er ist **vierspurig**: (1) **Agentic-CLM-First-Cloud** (DocuSign Iris Agents, Ironclad Intake/Renewal/Cost-Savings/Archive-Agents, LinkSquares All-Agentic-CLM, Sirion Obligation-Tracking-Agents — AI-Agenten uebernehmen Review/Redlining/Obligation-Tracking/Renewal-Briefs), (2) **AI-Assisted-Authoring + Klausel-Detektion** (PandaDoc AI-Contract-Review mit Non-Standard-Klausel-Flag, DocuSign AI-Contract-Review + Playbook-Review, Concord AI-Copilot, **HubSpot Revenue Hub Breeze AI** — Quote-to-Cash-in-CRM), (3) **DACH-eIDAS-QES-Spezialisten** (Skribble Swiss/EU-eIDAS+ZertES-Dual-Anbieter mit DE/CH-Hosting, Bundesnetzagentur-QTSPs wie D-Trust/Bundesdruckerei, Swisscom als Schweizer-Trust-Anker), (4) **DACH-KMU-Vertragsverwaltung-Light** (ContractHero 390 EUR/Monat ISO-27001 DE-Hosting, fynk 89-379 EUR Wien-based, top.legal als GDPR-by-Design-Player, otris als deutsch-staatlicher Mittelstand-Anbieter). Cosmi-vertraege sitzt heute **architektonisch in Spur (4)** — DACH-KMU-Vertragsverwaltung mit Reminder-Worker + EES-Canvas + MinIO-Document-Path — aber **ohne AI-Layer (Spur 1+2)**, **ohne QES/AES-Anbindung (Spur 3)**, **ohne Klausel-Library**, **ohne PDF-Renderer**. Das ist sauberer Greenfield-Stand in einem Markt, in dem AI-Tabellenstakes monatlich angehoben werden und der eIDAS-2.0-Wallet-Stichtag fixiert ist.

Drei strukturelle Veraenderungen treiben den Vertrags-Markt seit Januar 2026:

(a) **Agentic CLM ist Tabellenstake — vier Wellen in 6 Monaten.** Welle 1 (Januar 2026): **DocuSign launcht "Next-Gen eSignature" mit Iris-AI-Engine** — Iris erkennt Agreement-Type automatisch, platziert Felder, generiert AI-Assisted-Signer-Summary fuer den Unterzeichner (Schluessel-Klauseln auf Plain-Language uebersetzt). Welle 2 (Maerz 2026): **DocuSign AI-Contract-Review + Playbook-Review** — Iris flaggt riskante Sprache, schlaegt chirurgische Edits vor, drafted neue Klausel-Sprache aus Chat — auch ohne fertiges Playbook. Welle 3 (April 2026): **Ironclad Acting-Capabilities Early-Access** — Intake-Agent, Renewal-Agent (generiert Renewal-Briefs aus Vertrags-Historie), Cost-Savings-Agent (analysiert Vendor-Vertraege auf Volume-Discounts/Rebates/Bundling), Archive-Agent (extrahiert Metadata + verifiziert User-Input). Welle 4 (Mai 2026): **DocuSign Momentum-Konferenz** — IAM-Agents (Intake/Triage/Smart-Redlining/Relationship-Intelligence) gehen in Beta, IAM for Sales global GA, IAM for HR Early-Access ab Juni, US-Rollout-Start Juli 2026. **Parallel: LinkSquares All-Agentic CLM GA**, **Sirion Obligation-Tracking Real-Time-Agents**, **PandaDoc AI-Contract-Risk-Anomaly-Detection** (Non-Standard-Klauseln vor Signatur flaggen, kontextuelle Klausel-Verstaendnis statt Keyword-Match). **Konsequenz fuer Cosmi-vertraege**: 2 EUR/User-Monat Modul-Anker ist heute KMU-attraktiv (DocuSign Personal $10-15/User-Monat fuer 5 Envelopes), **aber** die Marktrethorik hat sich verschoben: Anbieter pitchen nicht mehr "e-Sign + Document Storage", sondern "AI uebernimmt Review/Renewal/Risk". Cosmi-vertraege ohne **mindestens** AI-Klausel-Extraction + Renewal-Brief-Generation + Risiko-Highlight wird in 12 Monaten als "Aktenordner-digital" wahrgenommen — bestes Pricing reicht nicht, wenn die Konkurrenz behauptet, drei Headcounts zu ersetzen. Der **Cosmi-Cross-Modul-AI-Pfad** ist die einzige nachhaltige Antwort: Cosmi-AI nutzt CRM-Kontakt-Historie + Helpdesk-Vorgaenge + Wiki-Knowledge-Snippets, um Vertrags-Klauseln zu kontextualisieren — Standalone-CLM-Anbieter (Ironclad/PandaDoc/Concord) koennen das strukturell nicht, weil sie keine CRM-Tabelle haben.

(b) **eIDAS 2.0 + EUDI-Wallet sind das zweite Sprint-Item nach AI** — und Skribble/Swisscom/D-Trust haben den DACH-Vorlauf. Die EU-Trusted-List (LOTL) vom 22. Mai 2026 listet zertifizierte QTSPs pro Mitgliedstaat; in Deutschland regelt die Bundesnetzagentur die QTSPs (Bundesdruckerei/D-Trust als Anker), in der Schweiz ZertES + Swisscom als groesster qualifizierter Trust-Anbieter (auf DE-eIDAS-Niveau anerkannt). **Skribble ist DACH-Marktfuehrer fuer das Dual-Regime** — eIDAS + ZertES auf einer Plattform, **DE/CH-Hosting waehlbar** (kritisch fuer Cosmi-EU-Sovereign-Story), 4000+ DACH-Firmen einschliesslich SBB/DATEV/Baloise. Pricing: CHF 9/Monat Basis, **CHF 1.80 pro QES, CHF 1.00 pro AES** — usage-based, fuer KMU planbar. **API v2 (Release 25.06.2024)** liefert genau das, was Cosmi-vertraege als Provider-Stub angekuendigt hat: REST-API + Webhooks (Success/Error/Update-Callbacks) + Microsoft-Connector (Power-Automate/Logic-Apps). **EU-Dezember-2026-Pflicht**: alle 27 MS muessen EUDI-Wallets ausrollen, QES via Smartphone wird Standard, **2027 Akzeptanz-Pflicht fuer Relying-Parties** (Telco/Health/Travel/Energy). **Praktische Implikation fuer Cosmi-vertraege**: (i) Skribble-Integration als Provider-Adapter ist Sprint-3 reif (Stub-Field ist schon im Model), (ii) zweite EUDI-Wallet-Akzeptanz-Phase ab Q2 2027 als Roadmap-Marker, (iii) Cross-Border-QES-Risiko via **BGH 25.02.2026 II ZB 13/24** — eine oesterreichische QES wurde NICHT anerkannt, weil das Verfahren nicht gleichwertig zum deutschen war. Lesson: Cosmi-vertraege MUSS QES-Workflow nicht nur signieren, sondern den **Provider und das Verfahren ins Audit-Log schreiben** (welcher QTSP, welche Identifikationsstufe, welches Format).

(c) **EU-AI-Act Art. 50 + EU-Data-Act + DSGVO-Vertrags-Form-Anker treffen jetzt zusammen.** **EU-AI-Act Article 50 trifft am 2. August 2026** (4 Wochen + 6 Tage von heute): jede AI-Funktion in Vertragsmanagement (AI-Klausel-Extraction, AI-Redlining, AI-generierte Klausel-Vorschlaege, AI-Risiko-Flag, AI-Renewal-Briefs) faellt unter Transparenz-Pflicht — User MUSS informiert werden, dass AI im Spiel ist, Disclosure-Pattern wie "AI Assistant" oder "Powered by AI", **Bussgeld bis €15 Mio oder 3% Welt-Umsatz**. EU-Code-of-Practice on Transparency (2. Draft 3. Maerz 2026, Final-Version Juni 2026) ergaenzt um machine-readable Marks fuer AI-Generated-Content. **EU-Data-Act greift seit 12. September 2025 fuer alle NEUEN B2B-Daten-Sharing-Vertraege** mit FRAND-Pflicht (Fair-Reasonable-And-Non-Discriminatory), umkehrte Beweislast fuer Datenhalter, plus EU-Kommission hat Model-Contractual-Terms (MCTs) und Standard-Contractual-Clauses (SCCs) unter Art. 41 EU-Data-Act veroeffentlicht. Ab **12. September 2027** auch fuer Pre-Existing-Vertraege. Cosmi-vertraege koennte hier **strategischen Vorteil bauen**, indem es EU-MCT/SCC-Templates als Standard-Klausel-Bibliothek bereitstellt (vor Skribble/PandaDoc, die das heute nicht haben). **DSGVO-Form-Anker**: BGH 11.03.2026 I ZR 202/25 bestaetigt Textform durch Email-Austausch (relevant fuer Reminder-Email-Versand), § 126a BGB verlangt fuer elektronische Form QES jedes Vertragspartners — Cosmi-EES-Canvas reicht NICHT fuer Form-pflichtige Vertraege (Buergschaft, Verbraucherdarlehen). **Praktische Implikation fuer Cosmi**: jede AI-Vertrags-Funktion ab heute MUSS mit Disclosure-Schicht ausgeliefert werden. Cosmi hat **strukturellen Vorteil**, weil noch keine AI-Funktion existiert: **Disclosure-by-Design** kann jetzt eingebaut werden, bevor die erste AI-Phase live geht. Konkurrenten muessen rueckwirkend ihre Q1/Q2-2026-AI-Releases auditieren.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. DocuSign (international, threat: HIGH als Markt-Standard + AI-Agentic-Leader, medium fuer DACH-KMU-Direkt-Sale)**

DocuSign ist nicht direkter DACH-KMU-Konkurrent (US-Cloud, kein Self-Host, Pricing-Eskalation, Auto-Renewal-Beschwerden), aber **das Feature-Erwartungs-Referenzmodell** — jeder Vertrags-Software-Buyer im DACH-Mittelstand sieht zumindest DocuSign-Demo, bevor er KMU-Alternative kauft. Markenfuehrer fuer "e-Signature is solved, now we do AI". Globaler #1 mit Iris als Markenname fuer AI-Engine seit Januar 2026.

- **Iris-AI-Engine 2026 (Jan/Maerz/Mai-Releases)**: AI-Assisted-Signer-Experience (Plain-Language-Summary + Key-Terms-Highlight), automatische Field-Placement und Agreement-Type-Erkennung, AI-Contract-Review mit Risk-Language-Flag + chirurgischen Edit-Suggestions + Klausel-Drafting aus Chat (auch ohne Playbook). **Agentic Layer**: Intake-Agent, Triage-Agent, Smart-Redlining-Agent, Relationship-Intelligence-Agent, Renewal-Agent, Obligation-Tracking-Agent. Agent-Studio fuer Custom-Agents nach Business-Rules.
- **IAM-Platform (Intelligent Agreement Management)**: einheitlicher Cloud-Stack fuer Create → Negotiate → Sign → Manage, IAM for Sales global GA Mai 2026, IAM for HR Early-Access Juni 2026.
- **G2/Capterra-Pain-Points 2026**: "Pricing zu hoch fuer kleine Teams oder Occasional-User", "Expensive" oder "Pricing issues" in ~1/4 kritischer G2-Reviews. **Trustpilot 75% 1-Star** (1168 Reviews) dominiert **Auto-Renewal-Beschwerden** und schwierige Cancellation-UX. Renewal-Preis-Erhoehungen bis 20% auf Unlimited-Plaenen. **Support hinter Paid-Tiers gegated** mit signifikanten Luecken.
- **Pricing-Basis (2026)**: Personal $10-15/Monat (Annual/Monthly), Standard hoeher, Business Pro hoeher, Enterprise verhandelbar — auto-renewal als Default mit Reminder-Probleme.
- **Gap zu Cosmi**: Iris-AI-Engine komplett (Field-Placement + Agreement-Type-Erkennung + AI-Signer-Summary), AI-Contract-Review + Playbook-Review, Agent-Studio mit Custom-Agents, native CLM-Workflow (Intake/Triage/Redlining/Approval/Obligation/Renewal), Iris-Agents fuer Renewal-Brief + Cost-Savings + Archive, IAM-Cross-Module (Sales/HR), AI-Plain-Language-Summary fuer Signer, Multi-QTSP-EU-Trust-Service-Integration.
- **Strategischer Hinweis (WICHTIGSTER AI-PUNKT DIESES REPORTS)**: **Cosmi gewinnt nicht ueber "AI besser als Iris"** — DocuSign hat 6+ Monate Iris-Vorsprung, Engineering-Tiefe und Milliarden-Vertragsdaten als Trainings-Basis. **Cosmi gewinnt ueber "Vertraege-in-CRM-in-Helpdesk-in-Wiki-in-Buchhaltung im KMU-Preis-Sweet-Spot"**: ein Service-Vertrag triggert HelpdeskPriorisierung + CRM-Renewal-Pipeline + Wiki-Onboarding-Doku-Verlinkung + Buchhaltung-Recurring-Rechnung — das ist Cosmi-USP, DocuSign IAM kann das strukturell nicht (kein eigenes Helpdesk, kein eigenes Wiki). **Aber:** AI-Klausel-Extraction + Renewal-Brief-Generator + Risiko-Highlight MUSS ab Q1 2027 verfuegbar sein — sonst greift der "Cosmi-fuehlt-sich-nicht-modern-an"-Effekt, wie schon bei Helpdesk-Deepdive W24 (AI-Drafts als Stake), Formulare-Deepdive W25 (AI-Form-Generation als Stake), Wiki-Deepdive W23 (AI-Search als Stake) als Pattern erkannt.

**2. Skribble (Schweiz/DACH, threat: HIGH als direkter QES/AES-Provider fuer Cosmi-eSignatur-Phase, medium als Standalone-Konkurrent)**

Skribble ist Cosmis **wichtigster strategischer Vertrags-Partner-Kandidat im DACH-Markt** — nicht primaerer Konkurrent, sondern der **richtige Provider hinter dem `SignatureProvider`-Stub** im Cosmi-Backend-Model. Schweizer Sitz, eIDAS + ZertES Dual-Compliance, 4000+ DACH-Firmen einschliesslich SBB/DATEV/Baloise/Helsana. Browser-only, kein Installation. Swisscom als Trust-Anker hinter QES.

- **Drei Signatur-Tiers (one platform)**: EES (Einfache E-Signatur), AES/FES (Fortgeschritten via Email/SMS-OTP), QES (Qualifiziert via Video-Identifikation oder Bank-ID) — Eskalation in einer UI.
- **Hosting-Wahl DE oder CH** — kritisch fuer Cosmi-EU-Sovereign-Pitch, GDPR-konform + Swiss FDPA, **Daten in DE oder CH only**.
- **API v2 (Release 25.06.2024, weiter aktiv)**: REST-API, OAuth, drei Callback-Typen (Success/Error/Update-Webhooks), `document_id` aus Callback fuer signed-Document-Download, Microsoft 365/Google Drive/Power-Automate-Connectors.
- **G2/Capterra-Pain-Points 2026**: "Setup-Komplexitaet von QES-Account zu finalem Use", "User mussten zahlen, um Vertraege zu signieren — nicht customer-vertrags-tauglich fuer alle Setups", "Identitaets-Verifikation fuer QES teils komplex bei bestimmten Address-/Bank-Daten-Kombis (wird vom Support geloest)", "Dokumenten-Upload teils clunky", "Free-Tier mit 2 Signaturen pro Monat zu klein", "Reporting + Recharging fehlen", "On-Glass-Signing fehlt".
- **Pricing (2026)**: ab **CHF 9/Monat** Basis-Paket, **CHF 1.80 pro QES, CHF 1.00 pro AES** — usage-based, KMU-planbar, dreistufige Plaene Fair/Business/Enterprise.
- **Tech-Stack**: Cloud-only, DE/CH-Hosting, **kein Self-Host-Pfad** — relevant fuer Cosmi-Self-Hosted-Customers.
- **Gap zu Cosmi**: native QES/AES-Anbindung (Cosmi hat nur EES-Canvas), eIDAS-konformer Audit-Log mit QTSP-Trace, Video-Identifikation, Bank-ID-Identifikation, Microsoft-365/Google-Drive-Integration, Multi-Signer-Workflow mit Order + Status-Lifecycle.
- **Strategischer Hinweis (WICHTIGSTER PROVIDER-PARTNERSHIP-PUNKT DIESES REPORTS)**: **Skribble ist NICHT der Cosmi-Standalone-Konkurrent, sondern der richtige Provider hinter `SignatureProvider="skribble"`.** Cosmi-vertraege-Strategie sollte sein: **(i) Skribble als Default-QES/AES-Provider** integrieren (Sprint-3-Item), **(ii) D-Trust/Bundesdruckerei als zweiter Provider** (Deutschland-Only-Customer waehlen heimischen Trust-Anbieter), **(iii) Cosmi-EES-Canvas bleibt fuer Innerbetriebliche-Vertraege** (Mitarbeitendenverein, Spesenformular, Material-Empfangsbestaetigung) — wo QES rechtlich nicht erforderlich ist. Cross-Modul-Hebel: Cosmi-Vertrags-Signing nutzt CRM-Kontakt fuer Vorausfuellung + Helpdesk-Ticket fuer Audit-Trail-Aufzeichnung — Skribble-standalone kann das nicht. **Cosmi-Modul-Pricing-Spannung**: 2 EUR/User-Monat Cosmi-Modul + Skribble-Pass-Through-Costs (CHF 1.80/QES) wirkt fair, wenn klar gepitcht — Skribble-CHF-9-Basis verschwindet, weil Cosmi-Tenant gebuendelt einkauft.

**3. PandaDoc (international, threat: medium fuer DACH-KMU — Mid-Market-AI-Vorbild)**

PandaDoc ist der **Mid-Market-CLM-Veteran** mit starkem AI-Contract-Review-Layer 2026, primaer US-/EU-Cloud, KEIN Self-Host. G2-Rating 4.7/5 ueber 3406 Reviews. Stark im Sales-Engagement-Markt (Proposals + Vertraege + Payment-Collection).

- **AI Contract Management 2026**: Risk/Anomaly-Detection (non-standard Klauseln + missing Terms + Deviationen vor Signatur flaggen), AI-Klausel-Verstaendnis kontextuell (nicht Keyword-Match), Data-Extraction (Dates/Obligations/Payment-Terms aus signierten Vertraegen), automated Monitoring fuer Renewal-Windows.
- **Sales-Funnel-Native**: Proposals + Quotes + Vertraege + Payment-Collection (Stripe-Native) + CRM-Integrationen (HubSpot, Pipedrive, Salesforce — letzteres Business-Tier+ als Add-on), Pricing-Tables, Native E-Signature.
- **G2/Capterra-Pain-Points 2026**: "Plans werden full-year-upfront billed, Seat-Counts gelockt — Monthly-Billing-Option fehlt", "Pricing-Page ein Chaos", "Form-Field-Alignment driftet bei dynamischen Feldern", "Signer-Experience clunky — UI fuer Sender ok, fuer Empfaenger nicht", "Kein direkter Customer-Support-Kontakt".
- **Pricing (2026)**: Free $0, Launch $9/User-Monat (pay-as-you-go), Starter $19/User-Monat, **Business $49/User-Monat** (CRM-Integrationen + Pricing-Tables + Payment-Collection), Enterprise (Custom).
- **Tech-Stack**: Cloud-only, US-/EU-Hosting-Optionen, kein Self-Host, kein QES-DACH-Trust-Layer.
- **Gap zu Cosmi**: AI-Klausel-Detektion (Risk/Anomaly/Non-Standard-Flag), AI-Data-Extraction (Dates/Obligations/Payment-Terms), Sales-Funnel-Tooling (Proposals/Quotes mit Pricing-Tables), Native-Payment-Collection (Stripe), Multi-Native-CRM-Integration (HubSpot/Pipedrive/Salesforce), Renewal-Window-Monitoring mit Auto-Alerts.
- **Strategischer Hinweis**: **PandaDoc ist der Sales-fokussierte CLM-Anbieter fuer Mittelstand und Mid-Market** — das ist NICHT Cosmi-Sweet-Spot (DACH-KMU mit 2-50 Mitarbeitenden), aber das Quote-to-Cash-Pattern ist exakt das, was **HubSpot Revenue Hub seit heute (W26-Mo) attackiert**. Cosmi-Cross-Modul-Pfad: Cosmi-vertraege + Cosmi-buchhaltung + Cosmi-crm-core liefert Quote-to-Cash-in-einem-Cosmi-Hub — das gleiche Wertversprechen wie HubSpot Revenue Hub, ABER mit EU-Sovereign-Stack und ohne Vendor-Lock-in. **Sprint-Anker**: AI-Klausel-Extraction + Data-Extraction (Dates/Obligations/Payment-Terms) als Phase-1-AI-Sprint nach Backend-Catch-Up-Sweep — das ist die KMU-attraktive AI-Funktion, die PandaDoc als Tabellenstake gesetzt hat.

**4. Ironclad (international, threat: low fuer DACH-KMU — Enterprise-CLM, aber wichtiges Agent-Vorbild)**

Ironclad ist der **Enterprise-CLM-Anbieter** mit fokussiertem AI-Agentic-Pfad — NICHT direkter DACH-KMU-Konkurrent (Enterprise-Pricing, keine KMU-Tier), aber **das wichtigste Agentic-CLM-Architektur-Vorbild** fuer Cosmi-Roadmap.

- **Acting Capabilities (Early-Access ab 15. April 2026)**: Intake-Agent (in Early-Access), Renewal-Agent (Renewal-Briefs aus Vertrags-Historie + Key-Context), Cost-Savings-Agent (Vendor-Vertraege auf Volume-Discounts/Rebates/Bundling analysieren), Archive-Agent (Metadata-Extraction + User-Verifikation-Prompts), Jurist-Agent (Legal-Reasoning + Klausel-Validierung). Acts Ironclad Assistant orchestriert Agenten.
- **Renewal-Dashboard 2026**: zentrale UI fuer alle anstehenden Renewals + AI-generierten Briefing.
- **Markt-Positionierung**: Top-of-Mind fuer In-House-Legal-Teams (US-Marktfuehrer), starke Salesforce-/CRM-Integration, **Enterprise-Pricing nicht oeffentlich**, typisch $30k-200k/Jahr.
- **Gap zu Cosmi**: Renewal-Agent mit AI-Brief-Generation, Cost-Savings-Agent (Volume-Discount-Detection in Vendor-Vertragsbestand), Intake-Agent fuer automatisches Vertrags-Ingest mit Klausel-Klassifikation, Jurist-Agent fuer Legal-Reasoning, Archive-Agent fuer Metadata-Extraction, Acts-Assistant fuer Agent-Orchestrierung, Renewal-Dashboard mit AI-Summary.
- **Strategischer Hinweis**: **Ironclad ist Cosmi-Roadmap-Vorbild, nicht direkter Konkurrent**. Sprint-Anker fuer Cosmi: **Renewal-Brief-Generator als erster AI-Agent** — Cosmi-Reminder-Worker laeuft bereits in Production-Grade (5min-Poll + Atomic-Claim + EventEmitter), die Erweiterung waere ein `RenewalBriefAgent` der vor jedem Reminder ein 3-Saetze-Brief generiert (was steht im Vertrag, was ist Verlauf, was empfehle ich). Cosmi-Cross-Modul-Hebel: Brief nutzt CRM-Account-Manager + Helpdesk-Vorgaenge + Buchhaltung-Zahlungshistorie + Wiki-Knowledge-Snippets — Ironclad-Renewal-Agent kann nur Vertrags-Historie sehen, nicht Helpdesk + Wiki.

**5. PandaDoc (oben) + ContractHero/fynk (DACH-KMU-direkter Konkurrent, threat: HIGH fuer 50-100-Mitarbeiter-Sweet-Spot)**

**ContractHero (German, threat: HIGH fuer Mittelstand 30-100 Mitarbeiter)**

ContractHero ist Cosmis **direktester DACH-KMU-Vertrags-Konkurrent oberhalb 30 Mitarbeitenden**. Deutsche Firma, DE/CH-Hosting, ISO-27001-zertifiziert, fokussiert auf Vertragsmanagement-Light (nicht volles CLM).

- **Features**: AI/OCR fuer Vertrags-Ingest, Klausel-Highlight, Reminder + Renewal-Tracking, Volltext-Suche, Audit-Log.
- **Pricing (2026)**: **Essential ab 390 EUR/Monat** (Flat-Rate, klein), Professional + Enterprise on request, kein Free-Plan.
- **Gap zu Cosmi**: AI/OCR-Ingest (Cosmi hat null), Klausel-Highlight, ISO-27001-Marker, deutsche Kunden-Referenzen.
- **Strategischer Hinweis**: ContractHero deckt das KMU-Segment **30-100 Mitarbeitende** ab — Cosmi-Sweet-Spot ist 2-50, das Overlap ist **5-30 Mitarbeitende** (Cosmi-Upper-Range + ContractHero-Lower-Range). ContractHero-Pricing 390 EUR/Monat fuer Essential ist deutlich teurer als Cosmi 2 EUR/User/Monat — Cosmi gewinnt klar im Preis, aber **nur wenn Funktion-Parity erreicht ist** (AI-OCR + Klausel-Highlight + Volltext-Suche).

**fynk (Wien-based, threat: HIGH fuer KMU 10-50)**

fynk ist Cosmis **direktester Konkurrent im 10-50-Mitarbeitenden-Sweet-Spot** im DACH-Markt. Wiener Sitz, trusted.de-Testsieger 2026 (Note 1.2), komplett deutschsprachig.

- **Features**: kompletter Contract-Lifecycle (Creation → Analyse), Vertrags-Templates, AI-Klausel-Detektion, Reminder, e-Signatur-Integration.
- **Pricing (2026)**: **Essential 89 EUR/Monat**, Growth 249 EUR/Monat, Advanced 379 EUR/Monat, Pro on request, **20% Annual-Discount**, Free-Basic-Plan.
- **Tech-Stack**: Cloud-only, EU-Hosting (Wien).
- **Gap zu Cosmi**: AI-Klausel-Detektion, Vertrags-Templates-Bibliothek, Free-Basic-Plan als Acquisition-Anker.
- **Strategischer Hinweis**: **fynk ist der gefaehrlichste direkte Konkurrent fuer Cosmi-vertraege im DACH-KMU-Segment** (10-50 Mitarbeitende). Wiener-Sitz = EU-Sovereign, deutschsprachig, Free-Tier als Acquisition-Tool, AI-Klausel-Detektion als Feature. Cosmi-Differenzierungs-Anker MUSS Cross-Modul-Hebel sein: fynk standalone fuer Vertrags-Funktion, Cosmi als Vertrags-IN-CRM-IN-Helpdesk-IN-Buchhaltung. **Warnung**: wenn Cosmi-Sales standalone-vertraege pitcht, verliert es gegen fynk — exakt das gleiche Pattern wie Formulare-Deepdive W25 (Cosmi-Formulare verliert standalone gegen Tally-Free).

**6. HubSpot Revenue Hub (international, threat: HIGH — Cross-Modul-Cosmi-Killer-Vektor heute GA)**

Heute (2026-06-22, W26-Mo) launcht HubSpot Revenue Hub GA — siehe Morning-Pulse `daily/2026-06-22-morning.md` `MOR-2026-06-22-i04` **COMPETITOR-SUPERIOR**: Quotes + Vertraege + Billing + Payments + Breeze AI Assistant + Revenue Agent in einem CRM-Hub. **Direktes Cosmi-Cross-Modul-Wertversprechen wird hier als CRM-Hub konsolidiert.**

- **Revenue Hub-Features (GA 2026-06-22)**: Quote-to-Cash-Workflow, AI-generierte Quotes/Vertraege, Vertrags-e-Signatur native, Billing-Engine (Recurring + One-Time), Payment-Processing, Revenue-Agent fuer automatische Invoice-Follow-ups, Breeze AI Assistant fuer Conversational-Vertrags-Operationen.
- **Pricing**: Free Tier fuer Basis-Invoicing, Pro/Enterprise fuer Vertraege + Analytics. **Detaillierte Pricing-Tier-Analyse durch intel-deep angefordert** (siehe Morning-Pulse).
- **Tech-Stack**: HubSpot-Cloud (US/EU-Hosting verfuegbar), kein Self-Host.
- **Strategischer Hinweis (WICHTIGSTER COMPETITOR-SUPERIOR-PUNKT DIESES REPORTS)**: **HubSpot Revenue Hub ist der direkte Angriffsvektor auf Cosmi-Cross-Modul-USP** (crm-core + vertraege + buchhaltung). Bisher hat HubSpot CRM + Marketing dominiert, aber Vertrags-Engine + Billing-Engine als separate Tools gelassen. **Mit Revenue Hub GA wird das Cosmi-Wertversprechen "Vertraege in CRM in Buchhaltung integriert" angreifbar.** Cosmi-Differenzierungs-Anker: (i) **EU-Sovereign-Stack** (HubSpot ist US, CLOUD-Act-Ausgesetzt — siehe Cosmi-W23-Keeper `ai-cost-governance-ist-die-neue-beschaffungs-pflic-crm-core-w23.md`), (ii) **Self-Host-Pfad** verfuegbar (HubSpot ist Cloud-only), (iii) **Modul-Pricing** statt Hub-Bundling (Kunde zahlt nur fuer vertraege wenn er das Modul aktiv nutzt — HubSpot Revenue Hub erzwingt CRM-Tier-Upgrade). **Pflicht-Sprint vor Sales-Push**: HubSpot Revenue Hub Pricing-Tier-Analyse + Vertragsmodul-Gap-Check (siehe `daily/2026-06-22-morning.md` Empfehlung an intel-deep).

---

## Cosmi-IST-Stand

**Production-Grade Komponenten (was schon laeuft, Stand 2026-06-22):**

- **Contract-Lifecycle-CRUD** vollstaendig: `CreateContract` (mit Contract-Number-Unique-Check), `UpdateContract` (partial mit Field-Pointers + ClearEndsOn), `DeleteContract` (nur Draft-Status), `GetContract` (mit Parties + Reminders embedded), `ListContracts` (paginiert, Filter auf Status/Type/StartsAfter/Before/EndsAfter/Before/ContactID).
- **Party-Management**: Add/Remove/List mit drei PartyTypes (contact/company/external), Role-Required, Signed-On optional. ExternalName fuer Nicht-CRM-Parteien.
- **Reminder-Engine in Production-Grade**: `ReminderWorker` mit 5-min-Poll fuer due Reminders + 60-min-Poll fuer Contract-Expiry. `ClaimDueReminders` ist atomar (Single-TX, Status=sent), idempotent, horizontal-skalierbar. `EmitReminderEvent` schickt `models.EventPayload` an Notification-Service mit `EventVertraegeReminderDue` Event-Type + DeepLink `/vertraege/{contract_id}` + GroupKey `vertraege.reminder.{contract_id}` (fuer Notification-Bundling). Vier Reminder-Types: renewal/expiry/payment/custom. **System-Context-Wrapping** (`database.WithSystemContext(ctx)`) fuer Worker-Auth.
- **Auto-Expiry-Engine**: `ExpireContracts` markiert Contracts mit `ends_on < now` und `status=active` auf `status=expired`. Log-Eintrag mit Count.
- **Contact-360-Filter**: `ListContractsInput.ContactID` filtert Vertraege wo mind. eine Partei diesen Contact hat — Cross-Modul-Hebel zwischen vertraege und crm-core ist BEREITS angelegt.
- **EES Inline-Signatur**: `SaveSignature` mit MIME-Prefix-Validation (`data:image/png;base64,` oder `data:image/svg+xml;base64,`), Size-Limit 1 MiB, SignedBy-Required. Audit-Log via `slog.Info`.
- **Tenant-Isolation Phase 2** (`tenant_isolation_phase2_test.go` 75 LOC) — Test-Coverage fuer Cross-Tenant-Zugriff-Verweigerung.
- **Document-Upload via Client-Side-Presign**: Frontend nutzt `POST /api/v1/files/presign-upload` mit `scope=vertraege`, dann direkter PUT zu MinIO, dann PATCH Contract.document_url — alter `UploadDocument`-RPC ist als **deprecated** markiert (Code-Pfad bleibt fuer Kompatibilitaet).
- **Frontend EES-Canvas-Dialog**: `ESignaturDialog.tsx` (615 LOC) mit `SignatureCanvas` Component, Signer-Lifecycle-UI (pending/sent/viewed/signed/declined), Timeline-Builder mit i18n, Order-Field fuer Multi-Signer.
- **Frontend Reminder-Hook**: `useContractReminders.ts` als React-Query-Hook fuer Reminder-Polling im UI.
- **Frontend Settings-Panel**: `VertraegeSettingsPanel.tsx` (372 LOC) fuer Modul-Konfiguration (Reminder-Defaults, Type-Defaults).
- **Stores**: `stores/vertraege.ts` (848 LOC) als zentraler Zustand+persist-Store mit Mock-Daten-Hybrid (CRM-Links, Templates, Multi-Signer — siehe Drift-Analyse oben), `vertraegePrefs.ts` (39 LOC) fuer User-Praeferenzen, `vertraegeSettings.ts` (97 LOC).
- **Pricing-Anker**: Cosmi-Modul-Pricing-Pattern 2 EUR/User/Monat (analog zu Formulare-W25). Skribble-Pass-Through bei Provider-Integration: +CHF 1.80/QES, +CHF 1.00/AES.

**Geplante / Stub-Komponenten (was angekuendigt aber NICHT lebt):**

- **`SignatureProvider` Field** — als Comment "Phase D: Skribble" markiert, kein einziger Provider-Adapter-Code-Pfad existiert. Default ist `nil`. **Sprint-3-Item**.
- **`ExportContract` als PDF-Renderer** — TODO-Comment im Code: "Sprint 3 — replace with PDF renderer (e.g. wkhtmltopdf or gotenberg)". Heute liefert es Plain-Text-Dump mit Title/Number/Type/Status/Dates/Parties-Liste.
- **Frontend Multi-Signer-Workflow** — `ContractSigner[]` Array mit Order/Status/Dispatch-vs-Canvas-Flag ist Frontend-only (vgl. Drift #2 oben).
- **Frontend ContractTemplate-Mock** — `MOCK_TEMPLATES` mit `tpl-miet`/`tpl-service`/etc. ist Frontend-only, Backend hat keine Template-Tabelle, keine Template-RPCs.
- **Frontend CRM-Linking** — `contactId/dealId/invoiceIds` ist Frontend-only (vgl. Drift #4 oben).
- **History-Action-Codes** — Frontend hat 12 stabile Action-Codes (`contract_created/updated/terminated/signed/reminder_triggered/document_added/removed/contact_linked/unlinked/deal_linked/unlinked/invoice_linked/unlinked`), Backend hat **keine** History-Tabelle — der Frontend-History-Store wird per Reload geleert (ausser persisted).

**Strukturelle Drift-Diagnose (Backend ↔ Frontend, kompakt):**

| Drift | Backend | Frontend | Konsequenz |
|---|---|---|---|
| **Contract-Type** | 5 generisch (`rental/service/employment/nda/other`) | 6 deutsch (`mietvertrag/liefervertrag/servicevertrag/arbeitsvertrag/lizenz/versicherung`) | Kein Mapping → Liefervertrag/Versicherung verlieren Backend-Repraesentation |
| **Signer** | Single (`SignatureData/SignedAt/SignedBy`) | `ContractSigner[]` mit Order + 5-Status-Workflow + Dispatch-vs-Canvas | Multi-Signer-State Frontend-only, Reload verliert State |
| **Dokumente** | Single `DocumentURL *string` (MinIO) | `ContractDocument[]` Array (FileId/Name/MimeType/Size/AddedAt) | Multi-Doc Frontend-only |
| **CRM-Links** | Keine (kein entity_links) | `contactId/dealId/invoiceIds[]` + Snapshot-Namen | Cross-Modul-Sales-Story nur Mock |
| **Templates** | Keine Tabelle, keine RPCs | `ContractTemplate` Frontend-Mock | Template-Feature Frontend-only |
| **History** | Keine Tabelle | `ContractHistoryEntry[]` mit 12 Action-Codes | Audit-Trail Frontend-persist-only |
| **Contract-Status** | `draft/active/expired/terminated` | `active/expiring/terminated/expired` | "expiring" Frontend-only Computed-State |

**Was Cosmi-vertraege HEUTE nicht hat (Cosmi-Lueckenliste vs. Markt):**

- **PDF-Renderer** (TXT-Stub vorhanden, TODO Sprint 3 mit wkhtmltopdf/gotenberg)
- **QES/AES-Provider-Integration** (Skribble/D-Trust/Swisscom — Provider-Field ist Stub)
- **AI-Klausel-Extraction** (PandaDoc/DocuSign/Ironclad-Tabellenstake)
- **AI-Risk/Anomaly-Detection** (DocuSign Iris AI-Contract-Review)
- **AI-Renewal-Brief-Generator** (Ironclad Renewal-Agent)
- **AI-Cost-Savings-Agent** (Ironclad Cost-Savings-Agent — Volume-Discount-Detection)
- **AI-Archive-Agent** (Ironclad — Metadata-Extraction + User-Verifikation-Prompt)
- **Vertrags-Template-Bibliothek** (Frontend-Mock, kein Backend)
- **Multi-Signer-Workflow** mit Dispatch (Email-Versand an externe Signer)
- **Klausel-Library** (Standard-Klauseln nach Vertrags-Typ, EU-MCT/SCC-Standards aus EU-Data-Act)
- **OCR-Vertrags-Ingest** (PDF hochladen → AI extrahiert Klauseln + Felder)
- **Negotiation-Workflow** (Redline-Editor + Track-Changes + Comment-Thread)
- **Approval-Chain** (Multi-Step-Genehmigung mit Conditional-Logic — z.B. "Vertraege >50k EUR brauchen 2. Approval")
- **Renewal-Dashboard** (zentrale UI fuer alle anstehenden Renewals + AI-Brief)
- **Audit-Log-Persistierung** (Backend hat slog.Info, aber keine queryable Audit-Tabelle)
- **Bulk-Contract-Generation** (1 Template + 100 CSV-Rows → 100 Vertraege)
- **EU-MCT-/SCC-Klausel-Templates** (EU-Data-Act-Compliance-Hebel)
- **EUDI-Wallet-Akzeptanz** (Dezember 2026 EU-Pflicht-Marker)
- **MCP-Server** (Vertrags-Operations per Claude/ChatGPT — Cross-Modul-Hebel)

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi-vertraege | DocuSign IAM | Skribble | PandaDoc | Ironclad | ContractHero | fynk | HubSpot Revenue Hub |
|---|---|---|---|---|---|---|---|---|
| Contract-CRUD | ✅ | ✅ | ❌ (kein CLM) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Party-Mgmt | ✅ (Backend) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reminder-Engine | ✅ Atomic-Claim | ✅ Iris-Agent | 🚧 Email-Only | ✅ | ✅ Renewal-Agent | ✅ | ✅ | ✅ Revenue-Agent |
| Auto-Expiry | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EES Inline (Canvas) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **QES/AES eIDAS** | ❌ (Provider-Stub) | ✅ multi-QTSP | ✅ DE+CH Dual | ⚠️ via Partner | ✅ multi-QTSP | ✅ | ✅ | ⚠️ HelloSign-Integration |
| **EUDI-Wallet (12/2026)** | ❌ | 🚧 angekuendigt | 🚧 angekuendigt | 🚧 | 🚧 | 🚧 | 🚧 | 🚧 |
| Multi-Signer-Workflow | 🚧 (Frontend-only) | ✅ | ✅ Order + Status | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Document-Anhang | 🚧 (Frontend-only) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI-Klausel-Extraction** | ❌ | ✅ Iris | ❌ | ✅ | ✅ Jurist-Agent | ✅ OCR+Highlight | ✅ | ✅ Breeze |
| **AI-Risk/Anomaly-Flag** | ❌ | ✅ Iris AI-Review | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ |
| **AI-Klausel-Drafting (Chat)** | ❌ | ✅ Iris Chat | ❌ | ✅ Limited | ✅ | ❌ | 🚧 | ✅ Breeze |
| **AI-Renewal-Brief-Generator** | ❌ | ✅ Iris-Agent | ❌ | ❌ | ✅ Renewal-Agent | ❌ | ❌ | ✅ |
| **AI-Cost-Savings-Agent** | ❌ | 🚧 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **AI-Archive-Agent (OCR-Ingest)** | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ AI-OCR | ✅ | ✅ |
| **AI-Plain-Language-Signer-Summary** | ❌ | ✅ Jan 2026 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Contract-Templates | 🚧 (Frontend-Mock) | ✅ 100+ | ❌ | ✅ 750+ | ✅ | ✅ | ✅ | ✅ |
| **EU-MCT-/SCC-Klausel-Library** | ❌ | 🚧 | ❌ | ❌ | 🚧 | ❌ | ❌ | ❌ |
| Bulk-Contract-Generation | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Approval-Chain | ❌ | ✅ Workflow-Builder | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ |
| Negotiation/Redlining | ❌ | ✅ Smart-Redline-Agent | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ |
| Renewal-Dashboard | 🚧 (Frontend-View) | ✅ | ❌ | ⚠️ | ✅ Apr 2026 | ✅ | ✅ | ✅ |
| Audit-Log (queryable) | 🚧 (slog only) | ✅ | ✅ | ✅ | ✅ | ✅ ISO-27001 | ✅ | ✅ |
| PDF-Renderer (Server) | 🚧 (TXT-Stub) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CRM-Linking | 🚧 (Frontend-only) | ✅ Salesforce-Native | 🚧 Connector | ✅ HubSpot/SF/PD | ✅ Salesforce | 🚧 | ✅ | ✅ Native |
| **MCP-Server (AI-Agent-API)** | ❌ | 🚧 | ❌ | ❌ | 🚧 | ❌ | ❌ | ❌ |
| Cross-Modul-Hebel (Helpdesk/Wiki) | 🚧 (Frontend-Stub) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ HubSpot-Hub |
| Self-Host-Pfad | ✅ (Modul-Flag) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| EU-DE-/CH-Hosting-Only | ✅ | ⚠️ optional | ✅ DE+CH dual | ⚠️ optional | ⚠️ optional | ✅ DE | ✅ Wien | ⚠️ optional |
| Free-Tier | ❌ (Modul-Pricing) | ❌ | ⚠️ 2 sig/Monat | ✅ Limited | ❌ | ❌ | ✅ Basic | ✅ Basis-Invoicing |
| KMU-Sweet-Spot (2-50 MA) | ✅ 2 EUR/User/Monat | ❌ ($10-15+) | ⚠️ CHF 9 + Usage | ⚠️ $9-49 | ❌ Enterprise | ❌ 390 EUR/Mo Flat | ✅ 89 EUR/Mo | ⚠️ Free + Lock-in |

**Legende**: ✅ vorhanden / 🚧 partial / ❌ fehlt / ⚠️ konditional

**Stake-Lesart**: Cosmi-vertraege hat 8 von 32 Feature-Zeilen voll und 6 partial — gegenueber 22-30 voller Zeilen bei den Leading-Konkurrenten. Die **strukturellen Vorteile** sind: Self-Host-Pfad (einzigartig), EU-DE-/CH-Hosting (geteilt mit Skribble/ContractHero/fynk), KMU-Pricing-Sweet-Spot. Die **strukturellen Luecken**: AI-Layer komplett, QES/AES-Provider-Integration, Multi-Signer-Backend, EU-MCT-Klausel-Library, MCP-Server.

---

## Top-3 Strategische Empfehlungen

### 1. 🟢 **Skribble-Provider-Integration als Sprint-3-Pflicht — vor jeder AI-Phase**

**Was**: `SignatureProvider` Field im Contract-Model ist seit Sprint-1 als "Phase D: Skribble" Comment-markiert. **Jetzt umsetzen**: Adapter-Layer `backend/internal/vertraege/providers/skribble/` mit Skribble-API-v2-Integration (REST + OAuth + 3 Webhook-Callback-Types), neue RPCs `RequestSignature(provider, signer_email, signer_name)` + `GetSignatureStatus(signature_request_id)` + `HandleProviderCallback(provider, payload)`, neuer Worker `SignatureWebhookWorker` analog zu `ReminderWorker`. **Migration 0225**: `contract_signers` Tabelle mit `id/tenant_id/contract_id/email/name/order/status/provider/provider_request_id/signed_at/signed_via/signature_data_url`. Backend muss endlich Multi-Signer-Workflow tragen (Frontend hat ihn schon, vgl. Drift #2). **Skribble als Default-Provider, D-Trust als zweiter (Deutschland-Only-Customer), EES-Canvas bleibt fuer Innerbetriebliche-Vertraege wo QES rechtlich nicht erforderlich**.

**Warum**: (a) Cosmi-Sales-Demo braucht "QES via Skribble Done" als Headline-Feature fuer DACH-KMU-Vertragsgespraeche — Skribble ist 4000+ DACH-Firmen-Referenz inkl. SBB/DATEV. (b) **§ 126a BGB** verlangt fuer elektronische Form QES jedes Vertragspartners — Cosmi-EES-Canvas reicht nicht fuer Form-pflichtige Vertraege (Buergschaft/Verbraucherdarlehen/...). Ohne QES-Provider-Anbindung schliesst Cosmi-vertraege diese Vertrags-Klassen aus. (c) **EUDI-Wallet ab Dezember 2026 als 27-MS-Pflicht** — Skribble + Swisscom + D-Trust werden Wallet-Akzeptanz vor Cosmi bauen. Wenn Cosmi auf Skribble setzt, kommt Wallet-Faehigkeit als Provider-Update-Path frei. (d) **BGH 25.02.2026 II ZB 13/24** Lehre: Cosmi-Audit-Log MUSS Provider + QTSP-Trace + Identifikationsstufe + Format speichern — sonst Risiko fuer Cross-Border-Anerkennung. (e) Multi-Signer-Workflow-Backend ist Voraussetzung fuer alle weiteren Sprint-Items (Approval-Chain, Negotiation, Dispatch-Email).

**Kosten/Aufwand**: 1-2 Sprints fuer Provider-Adapter + Worker + 5 neue RPCs + Migration + Frontend-Backend-Sync. Skribble-API-Setup ist gut dokumentiert (api-doc.skribble.com), DE-Hosting waehlbar, Sandbox-Environment vorhanden.

### 2. 🟡 **Backend-Catch-Up-Sweep VOR jeder neuen Feature-Phase — Frontend-Schicht ist 4 Drifts vor Backend**

**Was**: Drift-Analyse oben zeigt 7 strukturelle Backend-Frontend-Diskrepanzen. Catch-Up-Sweep als dedizierter Sprint **vor Skribble-Integration und vor AI-Phase**: **(a) ContractType-Migration 0226** — deutsche Domain-Codes als kanonische Werte (`mietvertrag/liefervertrag/servicevertrag/arbeitsvertrag/lizenz/versicherung/sonstiger`), Backend-Migration mit Mapping-Tabelle alt→neu, i18n-Layer im Service. **(b) contract_documents Tabelle Migration 0227** mit Many-to-One zu Contract: `id/tenant_id/contract_id/file_id/name/mime_type/size/order_index/added_at`. Migration der bestehenden `Contract.DocumentURL` auf `contract_documents` mit ContractCard-View. **(c) vertraege_entity_links Polymorphe-Tabelle Migration 0228** mit `id/tenant_id/contract_id/entity_type/entity_id/created_at` fuer Contact/Deal/Invoice/Company/Project-Links — der seit 2026-06-11 dokumentierte Backend-Bedarf "vertraege-API-Swap auf entity_links" (vgl. `milestones.md`). **(d) contract_history Tabelle Migration 0229** mit `id/tenant_id/contract_id/action_code/user_id/meta/created_at` als queryable Audit-Log statt slog-only. (e) FormularePage-Pattern aus W25: VertraegePage 2417 LOC Mono-File als Refactor-Schuld-Marker — vor AI-Phase aufteilen in `<ContractList>`, `<ContractDetail>`, `<ContractTimeline>`, `<ContractActions>`.

**Warum**: (a) Frontend-Domain-Schicht hat 4 vorgepreschte Features (Multi-Signer/Multi-Doc/CRM-Links/Templates), die ohne Backend-Persistierung Sand-Castles sind. Vor jedem neuen Sprint MUSS Backend-Persistierung nachgezogen werden, sonst wachsen die Drift-Probleme exponentiell. (b) Lehre aus Helpdesk-Deepdive W24 (HelpdeskPage konsumiert Mocks statt React-Query) und Formulare-Deepdive W25 (FormField-Typen driften) — vertraege ist drittes Modul mit gleichem Pattern. **Vor jedem neuen Feature-Sprint zu fixen** (W25-Wording uebernommen). (c) ContractType-Drift verhindert sauberes Reporting + Pipeline-Filter — Cosmi-Sales-Demos werden hier auffliegen, sobald Vertragsbestand divers genug ist. (d) Entity-Links sind Cross-Modul-USP-Voraussetzung — ohne Backend-Persistierung kann Cross-Modul-Hebel nicht gepitcht werden.

**Kosten/Aufwand**: 2 Sprints fuer 4 Migrationen + Repo-Schicht-Erweiterungen + Service-Validierungen + Frontend-Backend-Sync + VertraegePage-Refactor. Migration ist nicht-destruktiv (`document_url` bleibt, `contract_documents` ergaenzt; analog fuer andere).

### 3. 🟡 **AI-Klausel-Extraction + Renewal-Brief-Generator als Phase-1-AI-Sprint (Disclosure-by-Design)**

**Was**: Erster AI-Sprint nach Catch-Up-Sweep — **NICHT als "AI-Klausel-Detektion-Light", sondern als Cosmi-Cross-Modul-AI**: (a) `ClauseExtractionAgent` extrahiert aus PDF-Ingest die Top-5-Klauseln (Laufzeit/Kuendigungsfrist/Vergueutung/Datenschutz/Gerichtsstand) mit Klausel-Type-Klassifikation + Original-Text-Position. Storage in `contract_clauses` Tabelle. (b) `RenewalBriefAgent` triggert vor jedem Renewal-Reminder im Worker, generiert 3-Saetze-Brief: "Was steht im Vertrag?" + "Wie war die letzte Periode? (CRM-Kontakt-Historie + Helpdesk-Vorgaenge + Buchhaltung-Zahlungshistorie)" + "Was empfehle ich? (Renew/Renegotiate/Terminate)" — der Cross-Modul-Hebel ist das USP-Differenzial gegen Ironclad-Renewal-Agent (das nur Vertrags-Historie sieht). **Pflicht**: jeder AI-Output mit Article-50-Disclosure-Schicht ("AI Assistant") + Human-Review-Schritt + AI-Provider-Trace im Audit-Log (Provider/Modell/Prompt-Version) — wegen Anthropic-Mythos-Lockdown-Lehre (vgl. `keepers/anthropic-kill-switch-live-fable-5-mythos-5-weltwe-cross-w25.md`) Provider-Router-konform.

**Warum**: (a) AI ist Tabellenstake — DocuSign Iris + Ironclad Acting-Capabilities + PandaDoc AI-Review + ContractHero AI-OCR + fynk AI-Klausel-Detektion. Cosmi-vertraege ohne AI-Pfad in 12 Monaten = "Aktenordner-digital" Wahrnehmung. (b) Cross-Modul-Hebel ist Cosmi-USP — Renewal-Brief mit CRM/Helpdesk/Buchhaltung-Kontext kann nur Cosmi liefern, weil nur Cosmi die anderen Module besitzt. (c) **EU-AI-Act Art. 50 trifft 2. August 2026** — Disclosure-by-Design jetzt einbauen ist billiger als spaeter retrofittten. (d) Klausel-Extraction ist Voraussetzung fuer EU-MCT-/SCC-Klausel-Library (EU-Data-Act-Compliance-Hebel — Cosmi koennte hier vor Konkurrenz sein, weil keine US-CLM-Software EU-MCT-Klauseln vorinstalliert hat). (e) Provider-Router-Architektur (W23+W25-Carry-Forward) ist sowieso P0 wegen Anthropic-Lockdown — AI-Klausel-Sprint sollte parallel den Vertrags-Workload als ersten Cross-Provider-Test nutzen (Mistral fuer DE-Klauseln, Sonnet als Fallback).

**Kosten/Aufwand**: 3-4 Sprints fuer Klausel-Extraction-Pipeline (PDF→OCR→Embed→Classify→Store) + Renewal-Brief-Worker-Erweiterung + Disclosure-UI + AI-Audit-Log + Provider-Router-Anbindung. Hoechster Aufwand der drei Empfehlungen, aber hoechster strategischer Hebel.

---

## Quellen

**EU-Regulatorik (Pflicht-Anker fuer Vertrags-Compliance 2026):**

- [EU AI Act Article 50 — Transparency Rules Practical Guide](https://artificialintelligenceact.eu/transparency-rules-article-50/) — 2. August 2026 hard deadline
- [EU AI Act Article 50 Compliance Checklist — 2 August 2026 — ProofSnap](https://getproofsnap.com/eu-ai-act-deadline.html)
- [10 Takeaways: European Commission Draft Guidelines on AI Transparency — Global Policy Watch (Mai 2026)](https://www.globalpolicywatch.com/2026/05/10-takeaways-european-commission-draft-guidelines-on-ai-transparency-under-the-eu-ai-act/)
- [Code of Practice on Transparency of AI-Generated Content — EU Commission](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
- [EU Data Act New Model Contract Terms — Bryan Cave Leighton Paisner](https://www.bclplaw.com/en-US/events-insights-news/eu-data-act-new-model-contract-terms-and-standard-clauses-to-facilitate-data-sharing-and-cloud-switching.html)
- [EU Data Act in practice: Model Contractual Terms — Taylor Wessing](https://www.taylorwessing.com/en/global-data-hub/2025/eu-data-act---understanding-the-issues/gdh---the-eu-data-act-in-practice)
- [EU Digital Identity Wallet (EUDI) Regulation — EU Commission](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation)
- [eIDAS 2.0 Digital Identity Wallet Compliance 2026 — Yousign](https://yousign.com/blog/eidas-2-0-digital-identity-wallet-compliance-requirements)
- [eIDAS Dashboard — EU Trusted Lists Browser (LOTL Stand 22. Mai 2026)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [List of qualified trust service providers in the EU — EU Commission](https://digital-strategy.ec.europa.eu/en/policies/eu-trusted-lists)

**DACH-Rechtsprechung 2026:**

- [BGH 25.02.2026 II ZB 13/24 — Cross-Border-QES Anerkennung Oesterreich → Deutschland — NWB Urteile](https://datenbank.nwb.de/Dokument/1092767/)
- [§ 126a BGB — Elektronische Form — dejure.org](https://dejure.org/gesetze/BGB/126a.html)
- [BGH-Rechtsprechung 2026 — Pressemitteilungen](https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2026/2026004.html)

**Anbieter — Marktfuehrer (Iris/Ironclad/PandaDoc):**

- [DocuSign Iris Agreement AI Engine — Overview](https://www.docusign.com/products/platform/ai)
- [DocuSign January 2026 Release — Next-Gen eSignature with Iris](https://www.docusign.com/releases/january-2026)
- [DocuSign March 2026 Release — AI Contract Review + Playbook Review](https://www.docusign.com/releases/march-2026)
- [Momentum 2026: Agentic AI Transforms Agreements — DocuSign Blog](https://www.docusign.com/blog/momentum-2026)
- [DocuSign Iris Agents — Investor Press Release](https://investor.docusign.com/investors/press-releases/press-release-details/2026/Docusigns-New-AI-Translates-Legalese-and-Does-Your-Contract-Busywork/default.aspx)
- [Ironclad Acting Capabilities Early Access (15.04.2026)](https://ironcladapp.com/resources/articles/introducing-new-era-contract-intelligence)
- [What's New at Ironclad — April 2026 (Renewal/Cost-Savings/Archive-Agents)](https://ironcladapp.com/resources/webinars/whats-new-ironclad-april-2026)
- [LinkSquares All-Agentic CLM Platform GA — PR Newswire](https://www.prnewswire.com/news-releases/linksquares-announces-general-availability-of-all-agentic-clm-platform-302801781.html)
- [PandaDoc AI Contract Management](https://www.pandadoc.com/blog/contract-ai/)
- [PandaDoc March 2026 Release Notes](https://www.pandadoc.com/blog/whats-new-in-pandadoc-march-2026/)

**Anbieter — DACH-eIDAS / KMU-Spezialisten:**

- [Skribble Pricing (CH/DE/EU)](https://www.skribble.com/en-eu/pricing/)
- [Skribble Electronic Signature Software](https://www.skribble.com/en-eu/electronic-signature-software/)
- [Skribble API v2 Documentation](https://api-doc.skribble.com/)
- [Skribble Swisscom Trust Service Partner Integration](https://www.skribble.com/en-eu/swisscom-elektronic-signature/)
- [Skribble Reviews — Capterra 2026](https://www.capterra.com/p/203385/Skribble/reviews/)
- [ContractHero Pricing — OMR Reviews 2026](https://omr.com/en/reviews/product/contracthero-vertragsmanagement/pricing)
- [fynk Vertragsmanagement — trusted.de Test 2026 (Note 1.2)](https://trusted.de/fynk-vertragsmanagement)
- [Vertragsmanagement-Software DACH-Vergleich 2026 — Finban](https://www.finban.io/vertragsmanagement-software/vergleich)
- [top.legal CLM 50-100 Mitarbeiter Empfehlung 2026](https://www.top.legal/wissen/clm-software-fur-50-bis-100-mitarbeiter)

**Anbieter — Mid-Market-Konkurrenten:**

- [DocuSign Reviews G2 2026 (Pricing + Auto-Renewal-Pain)](https://www.g2.com/products/docusign/reviews)
- [PandaDoc Reviews G2 2026](https://www.g2.com/products/pandadoc/reviews)
- [Concord CLM Pricing 2026 + Reviews](https://signeasy.com/blog/business/concord-pricing)
- [Dropbox Sign (HelloSign) Pricing 2026](https://www.g2.com/products/dropbox-sign-formerly-hellosign/pricing)
- [Adobe Acrobat Sign Pricing 2026](https://signeasy.com/blog/business/adobe-sign-pricing)
- [Adobe Sign eIDAS Compliance Whitepaper](https://www.adobe.com/cc-shared/assets/pdf/trust/acrobat-sign-eidas-wp.pdf)

**MCP / AI-Standards:**

- [Model Context Protocol — Anthropic (Nov 2024 Launch)](https://www.anthropic.com/news/model-context-protocol)
- [MCP Standard 2026 — Enterprise AI Standard Adoption](https://www.coderio.com/blog/innovation/mastering-ai-integration-model-context-protocol/)

**Cosmi-interne Cross-References:**

- `daily/2026-06-22-morning.md` — HubSpot Revenue Hub GA als COMPETITOR-SUPERIOR (MOR-2026-06-22-i04)
- `weekly/2026-W25.md` — Anthropic-Mythos-Lockdown + Vertragsklausel-Pflicht "AI-Provider-Unabhaengigkeit"
- `monthly/2026-06-15-deepdive-formulare.md` — Backend-Frontend-Drift-Pattern als wiederkehrendes Modul-Hygiene-Item
- `monthly/2026-06-08-deepdive-helpdesk.md` — HelpdeskPage-Mocks-Pattern + AI-Drafts als Tabellenstake
- `KMU-Hub/.knowledge/milestones.md` — vertraege-API-Swap auf entity_links als 2026-06-11 dokumentierter Backend-Bedarf
- `KMU-Hub/backend/internal/vertraege/` — Production-Code-Stand (15 RPCs, 3 Domain-Models, Worker, EES inline)
- `KMU-Hub/backend/proto/vertraege/v1/vertraege.proto` — Authoritative RPC-Definition
- `KMU-Hub/desktop/src/renderer/src/modules/vertraege/` — Frontend-Schicht (VertraegePage 2417 LOC + ESignaturDialog 615 LOC + Settings 372 LOC)

---

## Picks (vorgeschlagen)

[ ] 🟢 **Skribble-Provider-Integration als Sprint-3-Pflicht** — Provider-Adapter `backend/internal/vertraege/providers/skribble/` + 5 neue RPCs (RequestSignature/GetSignatureStatus/HandleProviderCallback/CreateSigner/UpdateSignerStatus) + Migration 0225 `contract_signers` Tabelle + SignatureWebhookWorker. Provider als Default fuer DACH-KMU-Sales-Demos.

[ ] 🟢 **Backend-Catch-Up-Sweep VOR AI-Phase** — Migrationen 0226-0229: ContractType-Mapping (deutsche Domain-Codes), `contract_documents` Multi-Doc-Tabelle, `vertraege_entity_links` polymorph fuer CRM/Deal/Invoice/Project, `contract_history` queryable Audit-Log. VertraegePage 2417 LOC Mono-File-Refactor.

[ ] 🟡 **AI-Klausel-Extraction + Renewal-Brief-Generator als Phase-1-AI-Sprint** — `ClauseExtractionAgent` + `contract_clauses` Tabelle + `RenewalBriefAgent` Worker-Erweiterung + Article-50-Disclosure-UI + AI-Audit-Log mit Provider/Modell-Trace + Provider-Router-Anbindung (Mistral primary, Sonnet fallback wegen W23/W25-Anthropic-Lockdown).

[ ] 🟡 **HubSpot Revenue Hub Pricing-Tier-Analyse + Cosmi-Cross-Modul-USP-Refresh** — direktes Follow-Up auf `MOR-2026-06-22-i04`. intel-deep heute Abend (2026-06-22 17:00) sollte Revenue-Hub-Pricing dekonstruieren + Cosmi-Cross-Modul-Hebel-Re-Pitch erarbeiten. **GA-Tag ist heute, nicht in 2 Wochen — Sales-Doktrin braucht heute Abend updated Talking-Points.**

[ ] 🟡 **EU-MCT-/SCC-Klausel-Library als EU-Data-Act-Compliance-Hebel** — Standard-Klausel-Templates aus EU-Commission-MCT (Art. 41 EU-Data-Act) als vorinstallierte Cosmi-vertraege-Bibliothek. **Cosmi-Differenzierungs-Anker**: keine US-CLM-Software hat EU-MCTs vorinstalliert. Sprint nach AI-Phase-1, weil Klausel-Extraction-Pipeline als Vorbedingung.

[ ] 🟢 **PDF-Renderer Sprint 3 (Gotenberg empfohlen)** — ExportContract TXT-Stub durch Gotenberg-PDF ersetzen. Self-Hosted Gotenberg-Container in `docker-compose.prod.yml`, Service-Adapter `backend/internal/vertraege/renderer/gotenberg/`. **Voraussetzung fuer**: Skribble-Provider-Integration (Provider braucht PDF-Input statt TXT).

[ ] 🟡 **Cosmi-vertraege-MCP-Server (`cosmi-vertraege-mcp`)** — Tally-Pattern aus Formulare-Deepdive W25 auf vertraege uebertragen. gRPC-RPCs → MCP-Tools mappen (CreateContract → `cosmi-contract-create`, ListContracts → `cosmi-contract-list`, etc). Cross-Modul-Differenzierung: Cosmi-MCP-Server liefert nicht nur Vertrags-Tools, sondern auch CRM/Helpdesk/Wiki/Buchhaltung. Sprint nach AI-Phase-1.

[ ] 🟡 **Followup 30d (W30, 2026-07-20): EUDI-Wallet-Akzeptanz-Roadmap** — Skribble/Swisscom/D-Trust-Wallet-Plaene tracken. Cosmi-Provider-Adapter sollte Wallet-Pfad als Update-Path haben. Dezember-2026-Pflicht-Stichtag als Roadmap-Marker.

[ ] 🟡 **Followup 30d (W30, 2026-07-20): DocuSign Iris US-Rollout** — DocuSign hat fuer Juli 2026 angekuendigt, Iris-Agents in US auszurollen. EU-Rollout-Timing + Pricing-Tier-Repositionierung tracken. Wenn DocuSign Iris-Pricing fuer Enterprise-Tier ist, oeffnet sich Cosmi-KMU-Markt-Fenster.

[ ] 🟢 **Cross-Reference zu intel-deep heute Abend (2026-06-22 17:00)** — Vertragsmodul-Gap-Check gegen HubSpot Revenue Hub + Cosmi-Cross-Modul-USP-Story aktualisieren. Morning-Pulse hat das schon als Hot-Item markiert.
