---
year: 2026
week: 42
modul: buchhaltung
created: 2026-10-12
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 52
tokens_input: ~360000
tokens_output: ~37500
rotation_position: 8/15
zyklus: 2
delta_to: monthly/2026-06-29-deepdive-buchhaltung.md
---

# Deepdive: buchhaltung (Mo W42/2026) — Zyklus 2 Delta zu W27

> **Zyklus-2-Delta-Deepdive #8** — Vorgaenger W27 (2026-06-29). 15 Wochen Entwicklung in Cosmi + Markt. Dieser Report ersetzt W27 nicht, sondern misst Delivery-Rate der W27-Empfehlungen und re-skaliert Markt-Signale. Vorgaenger-Zyklus-2-Delta-Reports: W35 crm-core (2026-08-24), W36 dialer (2026-08-31), W37 video (2026-09-07), W38 wiki (2026-09-14), W39 helpdesk (2026-09-21), W40 formulare (2026-09-28), W41 vertraege (2026-10-05). Naechstes Modul gemaess Rotation: **rapporte** (KW43, 2026-10-19).

> **TL;DR — Delivery-Rate W27→W41: 0.6/3 Green-Picks strukturell geliefert (20%)**. **#1 KI-OCR-Layer**: 0% geliefert — kein Mistral-Adapter, kein `backend/internal/biz/einvoice/ai_extraction/`, kein OCR-Pfad irgendwo im Repo. **#2 PEPPOL-Access-Point**: 20% geliefert — UBL-Generator (`generator_ubl.go:32`) kennt den PEPPOL-ProfileID `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` hardcoded, aber kein Access-Point, kein BIS-Billing-3.0-Versand, kein 4-Corner-Routing, kein peppol_messages-Audit-Log. **#3 Bank-Feed-Adapter**: 40% geliefert — `backend/internal/biz/banking/` existiert NEU (2.208 LOC prod + 2.519 LOC test = 113% Ratio, 15 Service-Methoden, MT940-Parser + CAMT.053-XML-Parser + Statement-Dedup + Transaction-Matching + Account-CRUD, Migrationen 000247 + 000258), **aber PSD2/finAPI explizit NICHT implementiert** — der Code dokumentiert selbst in `service_accounts.go:131-138`: *"There is no bank session behind this: the PSD2 handshake is simulated in the desktop client... lean: a flag, not a connection. Replace this with the FinAPI/PSD2 token exchange once a customer's account is actually to be polled."* Phase 5 explizit deferred.

> **Gleichzeitig: 7 NICHT-in-W27-prognostizierte Grossdeliveries** haben Backend-Volumen fast verdoppelt. **Produktion-LOC 17.4k → 31.008 (+78%)**, **Test-LOC 12.6k → 44.104 (+250%!)**, **Service-Methoden 50+ → 151 (+200%)**, **Migrationen 219 → 325 (+106 in 15 Wochen = 7/Woche)**, **Test-Ratio 141%** (hoechste aller Zyklus-2-Deepdive-Module nach vertraege W41 mit 220%). Neue Sub-Pakete: `banking/` (2208 LOC), `dashboard/` (492 LOC + Revenue-Forecast), `expense/` (543 LOC + Multi-Stage-Approval-Workflow), `recurring/` (838 LOC, idempotente Generation mit `finance_recurring_runs`-Ledger), `quote/` (1369 LOC, als eigenes Sub-Paket aus invoice/ ausgegliedert). **Bexio Welle 3b (Invoice-Pull) seit 2026-07-05 live** (Migration 000243, read-only-Mirror, delta-forward via LWW-Timestamp, Loop-Prevention via `source='bexio'`-Flag, Phase-0-4 abgeschlossen, G12-Blocker geschlossen, Darien-GoBD-Counter-Signature pending). **DATEV OAuth-Refresh via Singleflight per Tenant** (2026-08-22, commit `3b63d2c1`) + **Orphan-Upload-Log-Flagging** (2026-08-18, `ccee9d4f`). **Quote-to-Invoice-Race fixed via Partial-Unique-Index Migration 000324** (2026-08-24) — **vermutlicher Produktions-Bug in W27-W28** (6-Wochen-Fenster bevor Fix) sollte in Audit-Logs auf Duplikat-Rechnungen mit identischem `source_quote_id` geprueft werden. **GoBD-Lock-Barrier auf ALLE Status-Transitions** (seit 2026-07-05+, commit `a2ea5ab5`) + **Payment-Delete-Block auf GoBD-locked Invoices** (2026-08-22, `42439f4c`). **Dunning-E-Mail-Versand via Brevo-SMTP** (2026-07-05, `e375b6e4`). **Lexware org_id-Capture bei OAuth-Connect** (2026-09-09, `a0f28af9`). **Lexware-Scheduler stop re-resolving config under system context** (2026-08-23, `3dcb02f3`). **Invoice buyer VAT-ID auf PDFs** (2026-09-24, `6ae3a10a`). **Decimal-Round-on-Write-Path** fuer Line-Total (2026-08-12, `be1dea4d`). **E-Rechnung-Validation: Inbound-Reject bei Invalid-Totals** (2026-08-11, `b6da7373`). **Pattern bestaetigt (W39/W40/W41-wiederholt)**: Backend-Hygiene (Idempotenz, GoBD-Lock, Race-Fix, Test-Coverage) wird schnell geliefert, strategische Markt-Luecken (AI/PEPPOL/Bank-Feed-Connectivity/DCO-API/CH-Lohnbuchhaltung/MCP) null bis minimal.

> **Markt-Shift der 15-Wochen-Spanne: EU-Sovereign-AI-Triade materialisiert in 48 Stunden (6.-8. Oktober).** **Mistral Large 4 "le Chonk"** (2026-10-06, Paris, 49B active/1T total, EU-only-Training, **$1.36/$4.18 per MTok — unter Sonnet 4.6**, Open-Weight Apache 2.0 Release Ende Oktober, Benchmarks: Cybench 93%, Finance+Legal > GPT-6-Astra, Prompt-Injection-Resistance 93.3%). **Aleph Alpha Kolibri 78B** (2026-10-03 released, 2026-10-08 Benchmarks publik, Heidelberg, 78.1B total / 3.46B active MoE, trained on 768 B200 GPUs in DE+FI, **Apache 2.0 fully open-source**, **1M context window**, EU-AI-Act-konform mit vollstaendiger Daten-Provenance: 4.5M+ URL-Blocklist inkl. EU-Kommissions-Piraterie-Quellen, DE-Gesamt 70.8, AIME 2026 96.0 beats Qwen3.6/Nemotron3/Mistral Small 4). **Claude Haiku 5.5** (2026-10-08, **90% API-Preis-Reduktion auf $0.10/$0.50 unter 100k Tokens — identisch mit GPT-6-Luna**, 30% Latency-Reduktion vs Haiku 4.5, 2.5× faster Agent-Turns, Adjustable-Effort-Settings Low/Med/High/Xhigh/Max, **HubSpot-interne CRM-Benchmark 92.8% avg — best rating von jedem kleinen Modell**). **Konsequenz fuer Cosmi-buchhaltung**: Multi-Provider-Router-Entscheidung (W25-Keeper `anthropic-kill-switch-fable-5` + W33-Doppel-Eskalation) hat jetzt **drei konkrete EU-Sovereign-Candidates** (Mistral Large 4 cloud EU-FR + Kolibri 78B on-premise DE/FI + Haiku 5.5 primary EU-Hosting-opt). KI-OCR-Argument "zu teuer fuer DACH-KMU" ist mit Haiku 5.5 $0.10/MTok Cached-Input zusammengebrochen — bei 50-200 Belegen/Monat sind das 0.5-2 EUR Cosmi-Tenant-Kosten (nicht 4-16 EUR wie in W27 mit Mistral OCR 4 kalkuliert).

> **Markt-Shift #2: Lexware Office Preis-Umbau seit Sommer 2026.** **Alte Struktur (W27)**: Basis/Plus/XL = 7.90/12.90/24.90 EUR Netto. **Neue Struktur (Oktober 2026, Stand pricing_snapshots/lexoffice.md 2026-10-12)**: **S/M/L/XL vier Tiers** zu Standard-Preisen 7.90/12.90/21.90/32.90 EUR Netto (XL +32% zum W27-Preis), mit **50%-Promo-Preisen 3.95/6.45/10.95/16.45 EUR fuer die ersten 3 Monate**. **Neuer L-Tier eingefuehrt** zwischen Plus und XL (Buchhaltung + EUeR + Umsatzsteuer bei 21.90 EUR Netto). Steuerberater-Zugang in allen Tiers inklusive = Lexware verstaerkt den Multiplier-Channel bewusst. **W29-Positionierung**: Alexander Mayer (Lexware) formuliert *"Copilot, nicht Autopilot — nicht die Technologie ist das Problem, sondern das Vertrauen in Prozesse, Sicherheit und Kontrolle"* fuer Lexware NAVI (AI-Assistent). **W41-Erweiterung**: Lexware-Blog positioniert Skill-Stack-Enabler fuer DACH-Steuerkanzleien in fuenf IT-Kompetenzen (Data, AI+Prompting, Cybersecurity, Prozessautomatisierung, Cloud+Collaboration) — direktes Signal, dass Lexware Steuerberater als Rollout-Multiplikator positioniert. **Cosmi-Antwort-Pflicht**: Steuerberater-Partner-Programm-Draft als Content-Asset vor 01.01.2027.

> **Markt-Shift #3: Feed-Blackout 7+ Wochen bei sevDesk + Bexio verhindert Marktbeobachtung.** **sevDesk-Pricing-Page 403 Forbidden** (Cookie-Consent-Wall ohne Content, pricing_snapshots/sevdesk.md leer seit W29), **Bexio-Pricing-Page 404 Not Found** (sowohl de-DE als auch de-CH URL offline seit W29, pricing_snapshots/bexio.md zeigt 404-Fehler). Beide zusammen = **die zwei groessten DACH-KMU-Konkurrenten strukturell nicht trackbar**. Potenzielle Platform-Shifts, Pricing-Umbauten, AI-Feature-Launches werden ueber manuelle G2/LinkedIn/Trustpilot-Checks laufen muessen. **Priorisierte Mute-Reaktivierung** fuer sources/buchhaltung.yaml mit alternativen URL-Varianten (sevdesk.com, bexio.com en-GB) als Sprint-Mikro-Pflicht.

> **Markt-Shift #4: MCP-Welle verfestigt sich.** **HubSpot MCP live seit W40 UNBOUND** (Sep 16-18, Claude Skills Sales Plugin + ChatGPT SMB-Collection $50 Credit + Gemini + Microsoft Copilot = alle vier Agent-Platformen haben read+write MCP-Zugriff auf HubSpot-CRM-Entities, 134 Produkt-Updates in einer Woche). **Twenty v2.45.0 shipped native MCP-Server** (2026-10-05 bis 2026-10-08, 70 PRs in 4 Releases, inkl. Record-Level-Sharing + AI-Agent-Emails via `answerAsk` + Junction-Relations-GA). **OpenAI Decisions API Public Beta** (2026-10-07, $0.10/MTok fuer typed Routing, GPT-6-Luna-Derivat, 230ms Latency). **Konsequenz fuer Cosmi-buchhaltung**: W33-Keeper `backend/internal/core/mcp-server/` ist jetzt 10 Wochen ueberfaellig (vorher 6-8 Wochen). Buchhaltungs-spezifisches MCP-Scope (Invoice-Read-Write, Ledger-Query, Report-Generation) ist weder architektonisch skizziert noch im Repo angefangen. **Twenty-Fork-vs-Own-vs-Non-Parity-Entscheidung aus W33** jetzt mit dritter konkreter Twenty-Release-Welle validiert — Entscheidungsnotwendigkeit ist nicht hypothetisch.

> **Markt-Shift #5: E-Rechnungs-Compliance-Deadline-Konvergenz bei nur 81 Tagen bis DE-B2B-Sende-Pflicht.** Stand **2026-10-12**: **81 Tage bis 01.01.2027 Versand-Pflicht fuer DE-Unternehmen >800k EUR Umsatz** (XRechnung oder ZUGFeRD, Sende-Pflicht in Deutschland). **easybill-YouGov-Studie** (n=502 DACH-KMU, Juni 2026): **74% nicht bereit, nur 26% komplett bereit, 33% nie eine E-Rechnung versandt**. Top-Huerden: technische Implementierung (36%), rechtliche Unklarheit (29%), Wissensmangel (27%). **Lexware-Positionierung** nutzt dieses Fenster explizit mit Steuerberater-Content ("E-Rechnungspflicht ab 2025 Alles Wichtige auf einen Blick" als Blog-Entry in Navigations-Menue sichtbar in pricing_snapshots/lexoffice.md:876). **Cosmi-buchhaltung-Status**: Empfangs-Pfad vollstaendig (einvoice-Sub-Paket 2715 LOC + 2783 Test-LOC, Validation-Hardening 2026-08-11 `b6da7373` rejects Inbound mit Invalid-Totals, Parser-Hardening-Test + Validation.go NEU 2026-08-24), **Sende-Pfad explizit NICHT** (grep "Sende-Pflicht|outgoing.*xrechnung" = 0 Matches). UBL-Generator `generator_ubl.go` generiert valides XRechnung-UBL mit PEPPOL-ProfileID fuer Quote→Invoice-PDF-Erzeugung (lokal), aber **keine Transmission-Codepath** zu PEPPOL-Netzwerk oder e-invoicing-Portal.

> **Zwei weitere Compliance-Deadlines kommen gleichzeitig**: **51 Tage bis EU AI Act Art. 50 Grace-Period-Ende 2026-12-02** (Machine-Readable-Marking-Pflicht), **31 Tage bis PostgreSQL 14 EOL 2026-11-12** (CVE-2026-2006 RCE kritisch fuer Cosmi-Buchhaltungs-DB). Buchhaltungs-Modul ist durch **GoBD-Lock-Barrier + Audit-Log-Append-Only + SHA-256-Integrity-Check** gegen DB-Compromise relativ hart gebaut, aber eine ungepatchte PostgreSQL-14-Instanz unter Live-Last ist Compliance-Risiko erster Ordnung. **Visa/Mastercard-$100B+-Interchange-Fees-Litigation** (W40/W41, HN:505, 362 Comments) beschleunigt zusaetzlich SEPA-Instant-Pivot in EU — relevanter Zweit-Effekt fuer Bank-Feed-Prioritaet.

> **Dieser Bericht formuliert drei verbindliche Pflicht-Empfehlungen fuer W42-W45** (nicht 7+ Picks wie W27, weil die W27-Picks weiter die 3 primaeren Luecken sind): #1 **PEPPOL-Sende-Pfad-Minimal + DATEV-PEPPOL-AP-Fallback** als 81-Tage-Pflicht-Sprint (DE-B2B-Sende-Pflicht ab 01.01.2027). #2 **AI-Compliance-Foundation-Sprint cosmi-weit** (W39-W41-Keeper, 51 Tage bis Grace-Period-Ende) mit Priorisierung Haiku 5.5 Primary + Mistral Large 4 EU-Fallback + Disclosure-Layer-Package. #3 **Cosmi-MCP-Server mit Buchhaltungs-Scope** (W33-Keeper, 10 Wochen ueberfaellig) als Parallel-Sprint zu #2 mit Phase-1-Minimal (invoice-read-only + ledger-query + dashboard-summary als 5 MCP-Tools), weil MCP ohne Compliance = Rechtsrisiko. Alle drei nebeneinander = 10-12 Wochen Team-Last mit 2 Senior + 1 Mid, deshalb Pflicht-Entscheidung ueber Scope-Cut (Bank-Feed Phase-5-Deferral bestaetigen, CH-QR-Rechnung Phase-5-Deferral bestaetigen, DCO-API Phase-5-Deferral bestaetigen).

---

## Delivery-Rate W27 → W41 (zentrale Delta-Sektion)

### W27-Picks: Delivery-Status

| Pick | Prioritaet | Status W27→W41 | Konkrete Evidenz |
|---|---|---|---|
| **#1 KI-OCR-Layer Mistral-OCR-4 auf Eingangsbelege** | 🟢 Q3-2026-Pflicht | **0% geliefert** | `backend/internal/biz/einvoice/ai_extraction/` existiert NICHT. `backend/internal/ai/` existiert NICHT. `backend/internal/compliance/ai_disclosure/` existiert NICHT. Grep nach "Mistral|OCR|ocr_result" in buchhaltung-Scope = 0 Matches. **LLM-Client in `/opt/kmuhub/backend/internal/llm/` existiert** (318 LOC, Ollama-OpenAI-kompatibel), aber **ausschliesslich fuer Meeting-AI-Summary** (Wave-7C Video-Modul, deutscher Prompt), nicht fuer buchhaltung. 15 Wochen null Code. |
| **#2 PEPPOL-Access-Point Self-Hosted + TSP-Fallback** | 🟢 Q4-2026-Pflicht | **20% partial** | `backend/internal/biz/peppol/` existiert NICHT. Grep nach "PEPPOL" = 2 Matches: (a) `backend/internal/biz/einvoice/generator_ubl.go:32` hardcodet `peppolBillingProfileID = "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0"` als UBL-ProfileID (EN-16931-konform), (b) `testdata/ubl_minimal.xml` als Test-Fixture. **Konsequenz**: Cosmi-generiertes UBL ist PEPPOL-Format-konform, aber **kein Access-Point-Code**, keine Zertifikat-Pflege, kein BIS-Billing-3.0-Versand, kein peppol_messages-Audit-Log, keine SendInvoiceViaPeppol-RPC. |
| **#3 Bank-Feed-Adapter finAPI + Salt-Edge** | 🟢 Q4-2026/Q1-2027 | **40% strukturell geliefert** | `backend/internal/biz/banking/` NEU seit W27, 9 Prod-Files + 7 Test-Files, **2.208 Prod-LOC + 2.519 Test-LOC**, **15 Service-Methoden** (CreateStatement/GetStatement/ListStatements/UpdateStatementStatus/ListTransactions/MatchTransaction/ListMatches/GetTransactionBalance/CreateAccount/GetAccount/ListAccounts/UpdateAccount/ConnectAccount/DisconnectAccount/DeleteAccount), MT940-Parser + CAMT.053-XML-Parser + Statement-Dedup (per Hash) + Transaction-Matcher-Logic + Account-CRUD, Migrationen 000247 (`finance_bank_statements`) + 000258 (`finance_bank_accounts`). **ABER PSD2/finAPI-Connector explizit NICHT implementiert** — `service_accounts.go:131-138` dokumentiert selbst: *"There is no bank session behind this: the PSD2 handshake is simulated in the desktop client and the real integration is P5 (see the migration header)... lean: a flag, not a connection. Replace this with the FinAPI/PSD2 token exchange once a customer's account is actually to be polled -- the signature and the stored fields stay, only the body grows a real handshake."* Grep "finAPI|SaltEdge|PSD2|HBCI|FinTS" = 0 Code-Implementierung, nur dieser Kommentar. **Fazit**: File-Upload-Workflow fuer MT940/CAMT.053 funktioniert (grosse Delivery), Live-Bank-Polling bleibt Phase 5. |
| **#S2 CH-QR-Rechnung-Generator** | 🟡 S2 | **Teilweise frontend-only** | `QRRechnungPreview.tsx` existiert im Frontend (SwissQR-Code-SVG-Rendering), aber Backend `backend/internal/biz/ch_specifics/qr_invoice/` existiert NICHT. **Fazit**: UI-Komponente ohne Backend-ESR-Logik. |
| **#S2 CH-MWST-/AT-MWST-Saetze als Tenant-Stammdaten** | 🟡 S2 | **0% geliefert** | `tax`-Sub-Paket weiter 1 Prod-File + 2 Test-Files = 155 Prod-LOC + 294 Test-LOC (W27: 112/181 LOC, +38%). Tenant-Tax-Rates-Tabelle existiert NICHT. Nur DE-19%/7% konfiguriert. |
| **#S3 DATEV-Connect-Online-API-Adapter bidirektional** | 🟡 S3 | **0% DCO, aber OAuth-Hardening geliefert** | DATEV-Sub-Paket 11 Prod + 9 Test = 1.911/3.136 LOC (W27: 1.389/486, Prod +38%, Test +546%). Grep "DCO|connect_online|datev_api" in datev/ = 0 Matches auf API-Call-Implementierung, nur Referenz-Kommentar in `buchungsstapel.go`. **Neu geliefert**: OAuth-Singleflight-per-Tenant (2026-08-22, `3b63d2c1`) + Orphan-Upload-Log-Detection (2026-08-18, `ccee9d4f`) + Concurrent-OAuth-Refresh-Test. **Fazit**: EXTF-CSV-Export-Only bleibt, aber Export-Pfad ist stark haertert. |
| **#S3 Multi-Stage-Workflow-Approval Eingangsrechnungen** | 🟡 S3 | **Partial: fuer Expenses geliefert, fuer Eingangsrechnungen 0%** | `expense/` NEU seit W27, 4 Prod + 2 Test = 543/816 LOC, **9 Service-Methoden** inkl. Create/Approve/Reject/UpdateStatus/AssignAccount — vollstaendiger Approval-Workflow mit Status pending→approved/rejected und SKR03/04-Konto-Zuweisung-Post-Approval. Migration 000257. **ABER**: `finance_incoming_invoices.status`-Lifecycle bleibt linear received→reviewed→booked/rejected ohne Multi-Stage-Approval. Fuer AP-Automation fehlt die Approval-Schicht weiter. |
| **#S4 KI-Buchhaltungs-Copilot im UI** | 🟡 S4 | **0% geliefert** | Kein Tool-Calling-LLM, keine konversationale Buchhaltungs-RPC-Bridge, kein Read-Only-SQL-Abfrage-Interface. |
| **#S4 Modul-Naming-Konsolidierung** | 🟡 S4 low-prio | **0% geliefert** | Frontend-Ordner `modules/finanzen/` unveraendert (32 TSX/TS-Files + lib/-Subdir), Backend bleibt `biz/invoice/|creditnote/|dunning/|...`, Sources-YAML + Pricing + Feature-Flag bleiben `buchhaltung`. **Dreifach-Diskrepanz bleibt bestehen** — low-prio nicht gefaehrdet, aber auch weiter nicht geloest. |

### W27-NICHT-prognostizierte, aber geliefert

Diese Pattern wiederholt sich seit W35 — Zyklus-2-Deepdive-Autoren unterschaetzen Hygiene-Delivery. In buchhaltung-Fall ist der Bonus-Delivery **aussergewoehnlich gross** (vergleichbar mit W39-helpdesk, deutlich mehr als W41-vertraege).

**B1: Bexio Welle 3b Invoice-Pull (Read-Only-Mirror, seit 2026-07-05 live)**
- Migration 000243 (`add_bexio_invoice_pull`): Config-Flags `invoice_pull_enabled`, `interval_minutes`, `last_pull_at`
- `ListInvoices(updatedSince)` + `FieldMapper.MapInvoiceToKMUHub` + `invoice.Service.UpsertImported`
- Puller `InvoicePuller` mit Loop-Prevention via `source='bexio'`-Flag + LWW-Timestamp + Delta-Forward-Guard (nil-Cursor → seed now + return)
- Phase 2 Puller (commit `64366f27`), Phase 3a Proto/Gateway/OpenAPI (`7767c7cd`), Phase 3b Frontend (`e19a68fb` mit `bexio-types.ts` + `bexio-client.ts` + `useBexioUpdateSyncConfig`-Hook + Invoice-Pull-Toggle + Read-Only-Badge)
- Phase 4 Backend-Integration-Tests gruen + Prod-Route live (`GET /integrations/bexio/status` → 401 vor Auth)
- **Open**: Sandbox-Test (kein Test-Bexio-Account) + Darien-GoBD-Counter-Signature auf G12
- **Scope-Check-Status**: G1 OAuth-State-HMAC closed, G2 ContactService-Wiring closed, G3 Contact-Resolve closed, G5 Fail-fast-ohne-VAULT closed, G10 Sync-Core-Coverage 28%→42% closed, **G12 Invoice-Pull closed**. **6/12 Blocker durch, nicht wie W27 behauptet 6/12 + G12-Open**. W27 war chronologisch vor Welle 3b Deployment.

**B2: Separate `recurring/`-Sub-Paket mit idempotenter Generation (Migration 000246)**
- 4 Prod + 4 Test = 838/1586 LOC, 8 Service-Methoden (CreateRecurringInvoice/Get/List/GenerateInvoices/Pause/Resume/End/UpdateRecurringInvoice)
- `finance_recurring_invoices`-Tabelle (Template: Line-Items-JSONB, Tax-Breakdown, Interval, Status, Dates)
- `finance_recurring_runs`-Tabelle als Idempotency-Ledger (UNIQUE(tenant_id, recurring_id, period_date), emitted invoice_id)
- Scheduler polls `next_run <= today WHERE status='active'`, generiert Draft-Invoices, updated next_run
- **Distinkt von Quote-to-Invoice-Conversion** (die ist One-Shot via expliziter User-Aktion)
- Concurrent-Generation-Race ueber DB-UNIQUE-Constraint abgesichert

**B3: Neues `quote/`-Sub-Paket (aus invoice/ ausgegliedert, 1369/1686 LOC, 11 Methoden)**
- Create/Get/List/Update/ConvertToInvoice/Cancel/Accept/Reject/UpdateStatus/ListByContact/GetPDF
- Repo-Method `GetByID` performst LEFT JOIN LATERAL auf finance_invoices fuer `ConvertedInvoiceNumber`-Population
- **Quote-to-Invoice-Race Fix (Migration 000324, 2026-08-24)**: Partial-UNIQUE-Index `(tenant_id, source_quote_id) WHERE status <> 'cancelled'` auf DB-Ebene, nicht nur Application-Check
- Stornierte Invoice entfernt Zeile aus Index — Re-Conversion erlaubt
- Neue Tests `postgres_repository_converted_invoice_db_test.go` (Roundtrip + Cancellation + Re-Conversion)
- **Produktions-Risiko-Audit**: In W27-W28 (6 Wochen vor Fix) war Doppel-Konvertierung moeglich via Doppel-Click → zwei Invoices mit identischem `source_quote_id`. **Pflicht-Pruefung in Audit-Logs** auf solche Duplikate (SQL: `SELECT source_quote_id, COUNT(*) FROM finance_invoices WHERE source_quote_id IS NOT NULL GROUP BY source_quote_id HAVING COUNT(*) > 1`).

**B4: `banking/` NEU als 2.208-LOC-Sub-Paket (siehe Delivery-Rate oben)**
- Statement-Import MT940 + CAMT.053 funktioniert, kein Live-Polling
- Migrationen 000247 + 000258
- 15 Service-Methoden
- Transaction-Matcher-Logic ohne AI (`matcher.go` ~180 LOC, Heuristic-Score-based)
- **Praktischer Nutzen heute**: Steuerberater kann MT940/CAMT.053 aus Bank-Portal exportieren und in Cosmi hochladen → Transaktionen werden gegen Open-Items matcher. 60% des W27-UX-Pain-Points ist geschlossen.

**B5: `expense/` NEU als 543-LOC-Sub-Paket mit vollstaendigem Approval-Workflow**
- Status: pending → approved | rejected, mit SKR03/04-Konto-Zuweisung-Post-Approval, `ListExpensesByEmployee` + `ExportForAccounting`
- Migration 000257
- **GoBD-Luecke**: Receipt-Storage weiter nur als Filename-String (kein Document-Attachment, kein Belegbild-Archiv-Integration) — commented als "lean marker for GoBD archive integration" im Code. **Rechts-Risiko** fuer DE-Steuerprueffung bei Steuer-relevanten Belegen (Belegarchiv-Pflicht fuer tax-related Docs).

**B6: `dashboard/` NEU als 492-LOC-Sub-Paket (Revenue-Forecast)**
- 1 Service-Methode `GetDashboard(ctx, tenantID, dateFrom, dateTo) → *FinanceDashboard`
- Revenue (total invoiced, total paid), Pipeline (open quotes sum), Status-Breakdown, Recent-Invoices, Expiring-Quotes, Pending-Dunnings, **Revenue-Forecast (avg monthly revenue × remaining months in year)**
- Repository Redis-cached
- Currency-Fix 2026-07-18 (`0ce7935a`): Revenue/Pipeline-Sums skaliert auf Tenant-Default-Currency
- **Real-Postgres-Tests** 2026-08-24

**B7: Invoice-Number-Partial-Unique-Index (Migration 000323, 2026-08-17)**
- UNIQUE `(tenant_id, invoice_number) WHERE source = 'cosmi'`
- Scope exkludiert Bexio-Imports (die haben eigene Nummern-Sequenz)
- Verhindert Duplikat-Rechnungsnummern bei Race-Condition
- `fix(invoice): make invoice number unique index partial` commit `ccee9d4f`

**B8: GoBD-Lock-Barrier auf ALLE Status-Transitions + Payment-Delete-Block**
- `fix(payment): block payment delete on GoBD-locked` (2026-08-22, `42439f4c`)
- Status-Transitions werden rejected nach Fiscal-Year-Close
- **Produktions-Audit-ready** fuer DE-Steuerpruefung (GoBD §147 AO)

**B9: Dunning-E-Mail-Versand via Brevo-SMTP (2026-07-05, `e375b6e4`)**
- `dunning.Service.SendDunningNotice` versendet jetzt PDF-Attachment via Brevo SMTP (shared `systemMailer` mit Auth-Service)
- Fail-closed wenn Mailer-Konfiguration vorhanden aber fehlerhaft
- Fail-open wenn Host leer
- Mail-Dispatch-Capability wurde in W24-helpdesk-Deepdive gefordert (Pattern "Backend 2419→4014 LOC"), hier in buchhaltung mitgeliefert

**B10: Decimal-Round-on-Write-Path (2026-08-12, `be1dea4d`)**
- Line-Total wird auf Cents gerundet auf JEDEM Write-Path
- Vermeidet Floating-Point-Drift bei Multi-Line-Rechnungen
- Pflicht fuer GoBD-Nachweisbarkeit (gleiche Zahl bei Audit-Reproduktion)

**B11: E-Rechnung-Validation Inbound-Reject bei Invalid-Totals (2026-08-11, `b6da7373`)**
- `feat(einvoice): reject inbound e-invoices with invalid totals`
- Parser-Validation.go NEU, Parser-Inbound-Hardening-Test 24 KB
- Roundtrip-Outbound-Test NEU
- Write-Path-Net-Agreement-Test 3 KB NEU
- **Pattern-Analogon**: formulare W40 hat ebenfalls Backend-Sicherheit sehr schnell ausgeliefert — buchhaltung-Team zeigt gleiches Delivery-Pattern

**B12: Lexware-Erweiterungen**
- **org_id-Capture bei OAuth-Connect** (2026-09-09, `a0f28af9`) — Lexware-API-Field persistiert fuer Multi-Org-Setups
- **Scheduler stop re-resolving config under system context** (2026-08-23, `3dcb02f3`) — Race-Fix bei config-reload waehrend scheduler-run
- **Lexware-Prod-LOC 3030 → 3294 (+9%)**, Test 869 → 3343 (+285%) — vergleichbare Hygiene-Welle wie DATEV

**B13: Invoice-Buyer-VAT-ID-Rendering auf PDFs (2026-09-24, `6ae3a10a`)**
- EU-Cross-Border-Reverse-Charge-Compliance-Requirement
- Steuernummer + VAT-ID des Rechnungsempfaengers wird jetzt zuverlaessig auf PDF gerendert

**B14: Backend-Volumen-Explosion**
- **17.4k → 31.008 Prod-LOC** (+78%)
- **12.6k → 44.104 Test-LOC** (+250%)
- **50+ → 151 Service-Methoden** (+200%)
- **Test-Ratio 72% → 141%** (hoechste in Zyklus-2-Modulen nach vertraege-W41 220%)
- **Migrationen 219 → 325** (+106 in 15 Wochen = **7 pro Woche** — vgl. formulare W40: +3 Migrationen in 15 Wochen)

### Frontend-Delta (modules/finanzen/)

| Metrik | W27 | W41 | Delta |
|---|---|---|---|
| Files (top-level TSX/TS) | 30+ | 32 | +~2 (stabil, aber hoeher Hygiene) |
| Prod-LOC | 11.415 | 11.857 | +4% (sehr moderat, kein Mono-File-Wachstum wie vertraege W41) |

**Neue Komponenten (nicht in W27-Baseline):**
- `BankingWidget.tsx` + `BankTransactionDetailPanel.tsx` — Bank-Statement-Import-UI + Transaction-Detail + Matching
- `ExpenseFormDialog.tsx` + `ExpenseDetailPanel.tsx` — Expense-Formular + Review/Approval
- `HoursToInvoiceDialog.tsx` — Time-Tracking-zu-Invoice-Konvertierung (Rapporte-Cross-Modul-UI)
- `QRRechnungPreview.tsx` — SwissQR-Code-SVG-Rendering (CH-ESR-Rechnung, Frontend-only, kein Backend-ESR-Generator-Code)
- `QuoteFormDialog.tsx` + `QuoteDetailPanel.tsx` — Quote-Editor + Convert-to-Invoice-Button
- `RecurringDetailPanel.tsx` + `RecurringInvoiceDialog.tsx` — Recurring-Schedule-Management
- `EInvoiceIndicator.tsx` — Badge/Status fuer Inbound-E-Rechnungen (`source='bexio'` vs `source='external'`)
- `ReceiptPreviewDialog.tsx` — Expense-Receipt-Preview
- `PaymentRecordDialog.tsx` — Manuelle Zahlungseingabe-Dialog
- `CustomerAccountSection.tsx` — Customer-Aging + Open-Items
- `DunningDetailPanel.tsx` — Dunning-Notice-Detail
- `ExportDialog.tsx` — DATEV-/GoBD-Export-UI
- `lib/amounts-visibility.tsx`, `lib/customer-account.ts`, `lib/finance-export.ts`, `lib/mini-pdf.ts`, `lib/receipt-cache.ts`, `lib/skr-accounts.ts`

**Nicht geliefert im Frontend**: Keine AI-OCR-Upload-UI, keine PEPPOL-Konfigurations-Section, kein KI-Buchungsvorschlags-Review-UI, keine `IncomingInvoiceAIExtractionDialog.tsx`. Pattern wiederholt sich: UI folgt Backend, Backend hat kein AI/PEPPOL, Frontend hat kein AI/PEPPOL.

**Pattern-Beobachtung vs W40-formulare + W41-vertraege**: formulare hatte Frontend-Mono-Explosion (2457→5605 LOC +128%), vertraege hatte Mono-Wachstum (2417→2565 LOC +6%, Mono-File waechst statt Refactor), **buchhaltung-Frontend ist disziplinierter** — Tabs-Pattern aus W27 wurde beibehalten, +4% LOC in 15 Wochen bei 15+ neuen Komponenten = sauber modularisierte Erweiterung.

### Was widerspricht Cosmi-Strategie (ehrliche Spiegelung)

- **Backend-Team ist liefertsstark, aber nicht in strategischer Markt-Luecke**: 7 Grossdeliveries (banking/, expense/, recurring/, quote/, Bexio-Pull, DATEV-Hardening, GoBD-Lock-Barrier) + 106 Migrationen + Prod-LOC-Verdopplung + Test-Ratio-141%. Das ist das reifste Modul des Repos. **Aber die drei W27-Pflicht-Picks (AI-OCR, PEPPOL-Versand, Bank-Feed-Live-Polling) sind 15 Wochen null bis minimal geliefert.** Backend-Team arbeitet, aber am falschen Pferd fuer die naechsten 81 Tage.
- **Buchhaltung hat jetzt die reifste Infrastruktur UND die hoechste Compliance-Dringlichkeit UND die groesste strategische Markt-Luecke** — gleichzeitig. In W27 war das Modul "mit konkretester KI-Marktforderung", in W41 ist es "mit konkretester regulatorischer Marktforderung + konkretester KI-Marktforderung".
- **Pricing-Argument schmilzt weiter**: Lexware-Office-M-Tier 12.90 EUR (Standard) oder 6.45 EUR (Promo 3 Monate) mit Lexware NAVI + Steuerberater-Zugang + E-Rechnung-Komplett. Cosmi-Buchhaltung "in Vorbereitung" ohne Standalone-Preis (laut `/opt/kmuhub/.knowledge/pricing.md`). **Cosmi hat keinen aktiven Buchhaltungs-Standalone-Preis**, nur Bundles in Branchen-Paketen (Handwerk/Dienstleister/Handel-Pakete bei ~25-26 EUR/User/Monat). Lexware kann heute im Enterprise-Pitch sagen "bei uns bekommst du Buchhaltung + NAVI + E-Rechnung-Compliance + Steuerberater-Portal + Lohn-Optional fuer 12.90 EUR". Cosmi muss sagen "wir haben das Modul noch nicht standalone verkauft".
- **Expense-Receipt-Storage als Filename-String** ist GoBD-Risiko. Fuer Steuer-relevante Belege (Reisekosten mit Vorsteuer-Abzug, Bewirtungs-Belege, Fahrtkosten-Belege) ist Belegarchiv-Pflicht in Deutschland dokumentiert. Lean-Marker "nicht fertig" ist OK fuer MVP, aber vor Modul-GA muss Document-Attachment geliefert werden.
- **Quote-to-Invoice-Produktions-Bug in W27-W28** (6 Wochen vor Migration 000324): Doppel-Click = Doppel-Invoice war real moeglich. Audit-Query auf `finance_invoices` nach Duplikat-`source_quote_id` ist Pflicht-Aktion fuer Prod-Datenbank.
- **PostgreSQL 14 EOL in 31 Tagen** — Cosmi-Buchhaltungs-Deployment-Pfad: welche Prod-Instanz laeuft auf welcher Postgres-Version? Keine Memory, aber muss gepruefft sein. CVE-2026-2006 RCE auf PostgreSQL 14 ist aktiver Threat-Vector gegen die reifste Datenbank im Repo.
- **Lexware-NAVI-"Copilot-not-Autopilot"-Positioning ist schwer zu kontern** — Cosmi hat zwar als EU-Sovereign-Standalone-Suite-ohne-Lock-in strukturelle Vorteile, aber Lexware hat die bessere Narrative ("Steuerberater behalten Kontrolle, AI assistiert, Mensch entscheidet"). Cosmi's Erzaehlung muss nicht "wir haben die bessere AI" sein, sondern "unsere AI arbeitet auf eure Daten, nicht umgekehrt" + "unser Code ist auditierbar, Lexware ist Black-Box" + "unsere Daten verlassen eure Infrastruktur nicht, auch nicht bei On-Premise mit Kolibri 78B".

---

## State-of-the-Art 2026-10-12 — Delta zu W27

Der DACH-Buchhaltungs-Markt ist in 15 Wochen **weniger** gewachsen als die Vorgaenger-Deepdive-Module (vertraege W41 hatte 4 Markt-Shifts, helpdesk W39 hatte 7 Shifts, formulare W40 hatte 3 Shifts). Buchhaltung-Markt ist **relativ stabil**: Lexware hat NAVI-Positionierung geschaerft + Preisstruktur umgebaut + Content-Marketing-Push, sevDesk+Bexio sind feed-blind seit 7 Wochen, Candis/BuchhaltungsButler/easybill ohne Produkt-News, weclapp stabil. **Die groessten Veraenderungen sind nicht im Buchhaltungs-Markt selbst, sondern im angrenzenden AI-Modell-Markt** (EU-Sovereign-Triade in 48h) + **MCP-Standardisierungs-Welle** (HubSpot + Twenty + OpenAI Decisions API in 2 Wochen) + **Compliance-Deadline-Konvergenz** (81 Tage DE-B2B-Sende-Pflicht + 51 Tage AI-Act-Grace-Period + 31 Tage Postgres-14-EOL).

### Markt-Shift-#1: EU-Sovereign-AI-Triade materialisiert (6.-8. Oktober 2026)

Vor 15 Wochen (W27) war die KI-OCR-Argumentation fuer Cosmi-Buchhaltung: *"Mistral OCR 4 ($4/1000 Seiten, EU-Hosting, Apache 2.0 Open-Weight) hat die Cost-Barriere fuer DACH-KMU vor 4 Wochen kollabiert — 50-200 Belege/Monat sind 4-16 EUR Cosmi-Tenant-Kosten."* Diese Argumentation gilt weiter, aber **drei neue Modelle veraendern die Position fundamental in den letzten 7 Tagen**:

- **Mistral Large 4 "le Chonk"** (2026-10-06, Paris): 49B active von 1T total, trainiert ausschliesslich in EU-Datacenters, **Preis $1.36/$4.18 per Million In/Out-Tokens — unter Sonnet 4.6**, Open-Weight-Release geplant Ende Oktober (Apache 2.0). Benchmarks: Cybench 93%, Finance+Legal uebertrifft GPT-6-Astra, Prompt-Injection-Resistance 93.3%. **Fuer Cosmi-buchhaltung**: viable EU-Sovereign-Fallback im Multi-Provider-Router — bei AI-OCR-Fallback (wenn Haiku-5.5-Primary nicht verfuegbar) + bei Buchhaltungs-Copilot-Reasoning (Finance+Legal-Benchmark-Signal).
- **Aleph Alpha Kolibri 78B** (2026-10-03 released, 2026-10-08 Benchmarks publik, Heidelberg): 78.1B total / 3.46B active (MoE), trainiert auf 768 B200 GPUs in Deutschland+Finnland, **Apache 2.0 fully open-source**, **1M Context-Window**. **EU-AI-Act-konform mit vollstaendiger Daten-Provenance**: 4.5M+ URL-Blocklist inkl. EU-Kommissions-Piraterie-Quellen, alle Third-Party-Datasets manuell gepruefft auf Licensing + DSGVO. Benchmarks: AIME 2026 96.0 (schlaegt Qwen3.6, Nemotron3, Mistral Small 4), DE-Gesamt 70.8. **Fuer Cosmi-buchhaltung**: On-Premise-DE-trained Modell fuer DACH-Behoerden-Track + Sovereign-Deployments + Cosmi-Orbit (Self-Hosted-Variante). *"Cosmi mit Kolibri On-Premise = komplette LLM-Pipeline ohne US-Hyperscaler-Beruehrung, auditierbarer Trainings-Datensatz, Apache-2.0-Lizenz"* ist eine Verkaufsstory, die weder Lexware noch sevDesk haben koennen.
- **Claude Haiku 5.5** (2026-10-08): **90% API-Preis-Reduktion auf $0.10/$0.50 unter 100k Tokens — identisch mit GPT-6-Luna**, 30% Latency-Reduktion vs Haiku 4.5, bis zu 2.5× schnellere Agent-Turns, Adjustable-Effort-Settings Low/Med/High/Xhigh/Max. **HubSpot-interne CRM-Benchmark 92.8% avg — beste Rating von jedem kleinen Modell**. **Fuer Cosmi-buchhaltung**: Primary-Cloud-Modell fuer Belege-Triage + Routing + Draft-Generation. 50-200 Belege/Monat × 2000 Tokens/Beleg = 400k Tokens = **$0.04 pro Tenant-Monat** mit Haiku 5.5 Cached-Input. Das kollabiert die Cost-Barriere nochmal um Faktor ~100 vs der W27-Mistral-OCR-4-Kalkulation (4-16 EUR).

**Cosmi-Konsequenz**: Der Multi-Provider-Router (W25-Keeper, W33-doppel-eskaliert, immer noch 0% Code in `backend/internal/ai/providers/router/`) hat jetzt **drei konkrete EU-Sovereign-Candidates** mit klarer Rollen-Verteilung: Primary = Haiku 5.5, EU-Fallback = Mistral Large 4, On-Premise = Kolibri 78B. **Entscheidungsmatrix fuer Buchhaltung-Scope** (vgl. W41-friday-Report Decision-Matrix):

| Modell | Rolle | EU-Sovereign | API-Preis | On-Premise | DE-Qualitaet |
|---|---|---|---|---|---|
| Haiku 5.5 | Primary Cloud (Beleg-Triage, Konto-Vorschlag, Dunning-Entwurf) | nein (US-Firma, EU-Hosting-Opt) | $0.10/$0.50 | nein | mittel |
| Kolibri 78B | On-Premise/DACH-Behoerden/Cosmi-Orbit | ja (DE/FI, Apache 2.0) | self-hosted | ja | sehr gut |
| Mistral Large 4 | EU-Fallback im Router + Complex Reasoning (Buchhaltungs-Copilot-Antworten) | ja (FR) | $1.36/$4.18 | ab Ende Oktober Apache 2.0 | gut |

### Markt-Shift-#2: Lexware-Office-Preis-Umbau mit neuem L-Tier + 50%-Promo-Welle

**Vor 15 Wochen** (W27, aus `pricing_snapshots/lexoffice.md` als damaliger Baseline + Lexware-Blog-Erwaehnungen): Basis/Plus/XL = **7.90/12.90/24.90 EUR Netto**.

**Heute** (2026-10-12, aus `pricing_snapshots/lexoffice.md` Stand 2026-10-12 04:09 UTC):

| Tier | Beschreibung | Standard-Preis | 50%-Promo (3 Monate) | Delta zu W27 |
|---|---|---|---|---|
| **S** | Belegerfassung + Archiv (Grundfunktionen) | **7.90 EUR** | 3.95 EUR | neu benannt (frueher "Basis", gleicher Preis) |
| **M** | Angebote + (E-)Rechnungen + Mahnungen | **12.90 EUR** | 6.45 EUR | neu benannt (frueher "Plus", gleicher Preis) |
| **L** | Buchhaltung + EUeR + Umsatzsteuer | **21.90 EUR** | 10.95 EUR | **NEUER Zwischentier**, war in W27 nicht da |
| **XL** | EU- + Abschlagsrechnungen + Public-API | **32.90 EUR** | 16.45 EUR | **+32% zu W27-XL (24.90)**, API-Zugang jetzt XL-exklusiv |

**Zusaetzliche Erkenntnisse** aus pricing_snapshots/lexoffice.md:
- **Lohn & Gehalt (optional dazubuchen)**: 12.90 EUR Standard / 6.45 EUR Promo, skaliert mit Mitarbeiter-Zahl bis 50 Mitarbeiter
- **Steuerberater-Zugang in ALLEN Tiers inkludiert** (incl. S) — expliziter Multiplier-Channel-Push
- **Elektronische Pendelakte** (Steuerberater-Datenaustausch) in allen Tiers
- **E-Rechnung (Pflicht seit 01.01.2025) explizit featured in Navigations-Menue** als Blog-Entry "E-Rechnungspflicht ab 2025 Alles Wichtige auf einen Blick"
- **"Gesetzesaenderungen 2026 Aktuelle Aenderungen im Ueberblick"** als Content-Entry (Thought-Leadership-Positionierung)
- **Lexware Mobile App inkl. Belegscanner + Belegpruefung** in allen Tiers (= KI-OCR fuer Smartphone-Beleg-Foto)
- **GoBD-Langzeitbelegarchiv** in allen Tiers
- **Multibanking** (Bank-Feed-Anbindung) in allen Tiers mit Automatischem Zahlungsabgleich
- **BWA (Betriebswirtschaftliche Auswertung)** in L+XL mit Drill-Down + PDF-Export
- **Automatische Umsatzsteuerprognose** in allen Tiers
- **USt-Voranmeldung + Zusammenfassende Meldung** elektronisch mit einem Klick in allen Tiers
- **XRechnung erstellen + uebermitteln** in allen Tiers (= Sende-Pfad bereits GA bei Lexware)
- **Lohn-Mitarbeiter integriert bezahlen** direkt aus Lexware heraus
- **Automatische Verbuchung der Personalkosten** nach Lohn-Abrechnung

**Konsequenz fuer Cosmi**: Lexware-M (12.90 EUR) hat **mehr Features als Cosmi-Buchhaltung heute** (XRechnung-Sende + Bank-Feed-Live + KI-Belegscanner + GoBD-Archiv + USt-Prognose + Steuerberater-Portal + Mobile-App). Cosmi-Buchhaltung muss im Pitch sagen: *"wir haben weniger Features als Lexware-M fuer unseren TBD-Preis, aber weniger Features ist nicht unser Produkt-Unterschied — unser Produkt-Unterschied ist Cross-Modul-Context + EU-Sovereign-Self-Host + Open-Source-AI-Pipeline-Option."* Diese Erzaehlung muss konstruiert werden, sonst gewinnt Lexware jedes Side-by-Side.

### Markt-Shift-#3: Feed-Blackout bei sevDesk + Bexio (7+ Wochen) — strukturelles Beobachtungs-Problem

- **sevDesk-Pricing-Page**: `sevdesk.de/preise/` → 403 Forbidden (Cookie-Consent-Wall ohne Content, pricing_snapshots/sevdesk.md leer seit W29)
- **sevDesk-Blog-Feed**: `sevdesk.de/blog/feed/` → **404 persistent seit W29** (7 Wochen null Signal)
- **Bexio-Pricing-Page**: `bexio.com/de-DE/preise/` → 404 Not Found + `bexio.com/de-CH/preise/` → 404 Not Found seit W27, **beide offline seit 2026-07-01**
- **Bexio-Blog-Feed**: offline

**Beide zusammen sind die zwei groessten DACH-KMU-Konkurrenten im Buchhaltungs-Markt** — sevDesk mit ~90.000 Kunden, Bexio mit ~65.000 Kunden. **Strukturelles Markt-Beobachtungs-Problem** fuer Cosmi-Intel-System: Pricing-Shifts, AI-Feature-Launches, API-Erweiterungen, Partnerschafts-Ankuendigungen werden nicht erfasst. **Mikro-Sprint-Pflicht** fuer sources/buchhaltung.yaml:
- Alternative URL-Varianten pruefen (sevdesk.com, bexio.com/en-US, de-AT-URL-Variants)
- G2-Scraping als Fallback (sevDesk hat ~1500 G2-Reviews, Bexio ~400)
- LinkedIn-Company-Page-Scraping fuer Produkt-Announcements
- Trustpilot-DACH-Review-Delta fuer Preis-/Feature-Diskussionen
- Manuelle Quartals-Checks (Analyst parkt 15 min/Quartal auf sevdesk.de + bexio.com)

### Markt-Shift-#4: MCP-Welle verfestigt sich — Cosmi 10 Wochen ueberfaellig

**Vor 15 Wochen** (W27): kein Modul erwaehnt MCP explizit, Lovable-Series-C-$400M (W33-Keeper) war die erste strategische Markierung (W33, 2026-08-14).

**Heute** (2026-10-12):
- **HubSpot MCP live seit W40 UNBOUND** (Sep 16-18, 2026): Claude Skills Sales Plugin + ChatGPT SMB-Collection $50 Credit + Gemini + Microsoft Copilot = **vier Agent-Platformen haben read+write MCP-Zugriff** auf HubSpot-CRM-Entities (Landing-Pages, Campaigns, Quotes, Custom-Objects, Workflows), 134 Produkt-Updates in einer Woche. **HubSpot-Positionierung ist jetzt "Agentic Customer Platform" statt "CRM-Suite"**.
- **Twenty v2.45.0 shipped native MCP-Server** (2026-10-05 bis 2026-10-08): 70 PRs in 4 Releases, Record-Level-Sharing-Enterprise-grade, AI-Agent-Emails via `answerAsk`, Junction-Relations GA. **Twenty-Sprint-Kadenz-Trend aus W33-Keeper bestaetigt** mit konkreter MCP-Erweiterung.
- **OpenAI Decisions API Public Beta** (2026-10-07): $0.10/MTok fuer typed Routing, GPT-6-Luna-Derivat, 230ms Latency. **Pattern**: define Question + finite Answers → Classification at 10× Speed. Multi-Model-Routing wird kommerzielles Standard-Produkt.
- **Freshworks MCP-Metering** seit 2026-09-01 (100/500/1000 Actions in Growth/Pro/Enterprise, dokumentiert in W39-helpdesk-Report).

**Konsequenz fuer Cosmi-buchhaltung**: Buchhaltungs-MCP-Scope ist nicht trivial, aber **Phase-1-Minimal** waere konkret: 5 Tools (`invoice_read`, `invoice_list_by_contact`, `ledger_query_summary`, `dashboard_summary`, `incoming_invoice_list`) alle Read-Only, kein Write im MVP. Weil `biz/invoice/service.go` schon 21 Service-Methoden hat, ist der MCP-Adapter-Layer vorne drauf ~400-600 LOC = **3-5 Tage Aufwand**. **W33-Keeper `backend/internal/core/mcp-server/` ist 10 Wochen ueberfaellig**. Pattern wiederholt sich seit W38: jedes Modul-Deepdive-nachher-nachher-nachher nennt MCP-Luecke, kein Modul startet.

### Markt-Shift-#5: E-Rechnungs-Compliance-Deadline-Konvergenz

**Compliance-Deadlines Oktober-Dezember 2026 (Stand 2026-10-12)**:

| Datum | Event | Tage ab heute | Cosmi-Risk |
|---|---|---|---|
| **2026-11-12** | PostgreSQL 14 EOL | **31 Tage** | **HOCH** — CVE-2026-2006 RCE kritisch fuer Buchhaltungs-DB |
| **2026-12-02** | EU AI Act Art. 50 Grace-Period-Ende | **51 Tage** | **HOCH** — Machine-Readable-Marking-Pflicht fuer AI-Content, Wave-7C Meeting-AI-Summary ist naechster Compliance-Trigger-Punkt |
| **2027-01-01** | DE-B2B-E-Rechnung-Versand-Pflicht fuer Unternehmen >800k EUR Umsatz | **81 Tage** | **HOCH** — XRechnung/ZUGFeRD-Versand ist Pflicht-Stake, Cosmi hat UBL-Generator aber **kein Transmission-Codepath** zu PEPPOL/Portal/E-Mail-mit-Signature |
| **2028-01-01** | DE-B2B-E-Rechnung-Versand-Pflicht universal (alle Unternehmen) | **443 Tage** | MITTEL — alle Cosmi-Kunden mit DE-Sitz brauchen das |

**easybill-YouGov-Studie** (n=502 DACH-KMU, Juni 2026, dokumentiert in W23-Keeper `e-rechnungspflicht-2027-74-nicht-bereit`):
- **26% komplett bereit** fuer E-Rechnung ab 01.01.2027
- **33% haben nie eine E-Rechnung versandt**
- **74% Market-Gap** (zeitgebunden, 81 Tage bis Deadline)
- Top-Huerden: technische Implementierung (36%), rechtliche Unklarheit (29%), Wissensmangel (27%)

**Lexware-Positionierung** nutzt dieses Fenster explizit:
- Blog-Entry "E-Rechnungspflicht ab 2025 Alles Wichtige auf einen Blick" prominent im Navigations-Menue
- Blog-Entry "Gesetzesaenderungen 2026 Aktuelle Aenderungen im Ueberblick" als Thought-Leadership-Entry
- W29-Zitat Alexander Mayer (Lexware): *"Nicht die Technologie ist das Problem, sondern das Vertrauen in Prozesse, Sicherheit und Kontrolle"* — direkte Steuerberater-Compliance-Multiplikator-Positionierung
- W41-Erweiterung: Lexware-Blog positioniert fuenf IT-Kompetenzen (Data, AI+Prompting, Cybersecurity, Prozessautomatisierung, Cloud+Collaboration) fuer DACH-Steuerkanzleien — "Skill-Stack-Enabler"-Positioning als Multiplier

**Cosmi-Risiko**: Kein Standalone-Buchhaltungs-Preis + kein Versand-Pfad + kein Steuerberater-Portal + kein Content-Marketing-Asset fuer 2027-Deadline = **Cosmi verpasst dieses Window strukturell**, auch wenn Backend die technischen Fundament fuer Compliance (einvoice-Parser + ZUGFeRD-Output + GoBD-Archiv + Lexware-Integration) bereits hat.

### Markt-Shift-#6: Visa/Mastercard-$100B+-Interchange-Fee-Litigation beschleunigt SEPA-Instant

**W40 (2026-09-29, HN:505, 362 Comments)**: Visa/Mastercard-$100B+-Interchange-Fees-Litigation Settlement/Trial-Phase. **Konsequenz**: SEPA-Instant-Push in EU wird strukturell beschleunigt (regulatorischer Druck). **Fuer Cosmi-buchhaltung**: Bank-Feed-Prioritaet steigt — bei Payment-Methode-SEPA-Instant werden Zahlungs-Eingaenge in Sekunden statt Tagen matchen muessen. Buchhaltungs-Software ohne Live-Bank-Feed verliert in diesem Scenario deutlich an UX-Wert vs. Software mit finAPI-/Salt-Edge-Live-Polling.

### Konkurrenz-Analyse-Delta (nur relevante Changes seit W27)

**1. Lexware Office — Pricing-Umbau + NAVI-Positioning-Verschaerfung**

| Element | W27 | W41 | Delta |
|---|---|---|---|
| Pricing-Tiers | 3 (Basis/Plus/XL) | **4 (S/M/L/XL)** | neuer L-Tier bei 21.90 EUR |
| XL-Standard | 24.90 EUR | **32.90 EUR** | **+32%** |
| Promo-Preise | - | **50% Rabatt 3 Monate** | 3.95-16.45 EUR Entry-Preise |
| Steuerberater-Zugang | Enthalten | Enthalten in allen Tiers (inkl S) | explizit Multiplier-Push |
| NAVI-Positioning | "KI-Buchhaltungs-Co-Pilot" | **"Copilot, nicht Autopilot"** (W29 Alexander Mayer) | Vertrauens-Narrativ geschaerft |
| Content-Marketing | - | **E-Rechnung-2027-Blog prominent** + Gesetzesaenderungen-2026 + Skill-Stack-Steuerkanzleien | 2027-Deadline-Window-Push |

**Lexware-Konsequenz fuer Cosmi**: Lexware hat die DACH-KMU-Compliance-Narrative gewonnen. Cosmi muss nicht "besser als NAVI" sein, sondern eine andere Narrative haben. **Vorschlag**: *"Lexware liefert Compliance mit Lock-in. Cosmi liefert Compliance mit Self-Host-Option und Open-Source-AI-Pipeline (Kolibri 78B)."* Diese Narrative braucht marketing/positioning/eu-sovereign-buchhaltung/-Asset.

**2. sevDesk — Blackout, kein Signal**

- Pricing-Page 403, Blog-Feed 404 seit W29 (7 Wochen)
- G2 letzte Review mit AI-Belegerfassung-Mention: Q2 2026 (keine neuen Signale)
- **Keine Pricing-Deltas trackbar**
- Mikro-Sprint-Pflicht: alternative URL + G2-Scraping-Fallback

**3. Bexio — Blackout + CH-Markt-Status-unklar**

- Pricing-Pages 404 beide Varianten de-DE + de-CH seit 2026-07-01
- Blog-Feed offline
- **Cosmi-Bexio-Integration-Status**: Welle 3b (Invoice-Pull) live seit 2026-07-05 ist Cosmi's groesster Bexio-Delivery dieser Spanne — paradox, weil Cosmi mehr Bexio-Integration ausbaut, waehrend die Bexio-Marke selbst nicht mehr trackbar ist
- **Hypothese**: Bexio koennte URL-Migration + Rebranding (Swisscom-Owned, moegliche Umstellung auf "Bexio.app" oder internationale TLD) durchfuehren — unbestaetigt

**4. BuchhaltungsButler — stille Phase**

- Keine RSS-Updates in W28-W41 trackbar
- Pricing-Snapshot nicht in /opt/zentria-intel/.state/pricing_snapshots/ (nicht ueberwacht)
- Letzte W27-Baseline: 14.90/24.90/39.90 EUR Solo/Smart/Pro
- Keine neuen AI-Features kommuniziert

**5. Candis — stille Phase**

- Blog-Feed existiert in sources (candis.io/blog/rss), aber keine neuen W28-W41-Signale
- Pricing: 199 EUR/Monat fuer 10 Belege (W27, nicht neu-verifiziert)
- Keine Produkt-Shifts

**6. easybill — SKR03/SKR04-Content-Marketing-Push + YouGov-Studie**

- W31: SKR03/SKR04-Kontenrahmen-Content positioniert easybill als DATEV-Vermeidung (Steuerberater-unabhaengige Workflows)
- Juni 2026 YouGov-Studie bleibt zentrales Marktbeleg (74% unbereit)
- Pricing nicht trackbar in Zentria-Snapshots

**7. weclapp — stabil, keine Produkt-Shifts**

- Pricing stabil per Oktober-Snapshot: ERP Starter 39 EUR/User, ERP Dienstleistung 86 EUR/User (annual) / 95 EUR/User (monthly), ERP Handel 163/179 EUR/User, Enterprise custom
- Add-ons: Vertragsmanagement + Helpdesk + weclapp POS je 55 EUR/Monat
- Einzel-Modul Buchhaltung: 39 EUR/Monat (ab)
- DATEV-Integration + E-Rechnung in allen Paketen
- Keine neuen AI-Features kommuniziert in W28-W41

**8. Odoo — Pricing-Page blocked, assumed stable (24.90 USD/User)**

- 403 Forbidden auf Pricing-Page
- Keine neuen Deepdive-Signale

### Was fehlt im Markt-Teil (ehrliches Framing)

- **DATEV PEPPOL-AP Updates**: W27 dokumentierte "DATEV als PEPPOL-AP seit Q4 2025" — kein neuer Status-Signal in W28-W41 trackbar. Kann sich geaendert haben.
- **Lexware-NAVI-Preis-Position**: In Lexware-Office-Preisstruktur ist NAVI-AI inkludiert, aber kein expliziter Preis-Tag fuer AI-Features aufgelistet. Wie Lexware NAVI kommerziell abrechnet, ist unklar — moeglicherweise Enterprise-only ab L-Tier.
- **sevDesk-G2-Signale**: Keine systematische G2-Scrape in intel-System seit W27. Produkt-Shifts bei sevDesk nicht trackbar.
- **Pliant-Status**: W27 dokumentierte als Corporate-Card-Partner-Kandidat. Keine neuen Signale.

---

## Cosmi-IST-Stand 2026-10-12 — Delta zu W27

### Backend-Sub-Pakete `backend/internal/biz/` (W27 vs W41)

| Sub-Paket | W27 Files | W41 Files | W27 Prod LOC | W41 Prod LOC | W27 Test LOC | W41 Test LOC | W27 Methoden | W41 Methoden | Delta |
|---|---|---|---|---|---|---|---|---|---|
| `invoice` | 10 | 9+17 | 1944 | 2929 | 2160 | 5545 | 14 | 21 | **GoBD-Lock-Barrier auf alle Transitions, Quote-Conversion-Race-Fix, Buyer-VAT-ID-PDF-Rendering, Decimal-Round-on-Write, Payment-Stats-Fix** |
| `creditnote` | 7 | 4+6 | 958 | 965 | 1100 | 1706 | 7 | 7 | leicht wuensch, Tests +55% |
| `dunning` | 6 | 7+5 | 928 | 1342 | 1062 | 2689 | 7 | 14 | **Brevo-SMTP-E-Mail-Versand**, Document-Currency-Carry-Through |
| `einvoice` | 10 | 10+10 | 1194 | 2715 | 637 | 2783 | 4 | 4 | **Parser-Validation + Inbound-Reject bei Invalid-Totals**, Roundtrip-Outbound-Test, Write-Path-Net-Agreement |
| `datev` | 11 | 11+9 | 1389 | 1911 | 486 | 3136 | 0 | 0 | **OAuth-Singleflight-per-Tenant** (3b63d2c1), Orphan-Upload-Log-Flagging (ccee9d4f), Concurrent-OAuth-Refresh-Test |
| `gobdarchive` | 6 | 4+4 | 615 | 615 | 405 | 1159 | 7 | 8 | Test-Coverage +186% |
| `pdf` | 4 | 3+3 | 1095 | 968 | 210 | 869 | 0 | 0 | leicht geschrumpft (Dead-Code-Removal), Tests +314% |
| `payment` | 4 | 3+2 | 549 | 582 | 775 | 1418 | 4 | 5 | **Payment-Delete-Block auf GoBD-locked** (42439f4c) |
| `tax` | 2 | 1+2 | 112 | 155 | 181 | 294 | 0 | 0 | +38%, aber weiter nur DE-Saetze |
| `bexio` | 35 | 24+15 | 3607 | 4079 | 2763 | 3622 | n/a | 20 | **Welle 3b Invoice-Pull Phase 0-4 live** (2026-07-05), OAuth-State-HMAC, Sync-Core 28%→42% Coverage, Lexware-Org-ID-Capture |
| `lexware` | 25 | 22+12 | 3030 | 3294 | 869 | 3343 | n/a | 18 | **org_id-Capture** (a0f28af9), **Scheduler-Fix** (3dcb02f3), Tests +285% |
| **`banking`** 🆕 | - | 9+7 | - | **2208** | - | **2519** | - | **15** | **NEU — MT940 + CAMT.053 Parser, Statement-Dedup, Transaction-Matcher, Account-CRUD** |
| **`dashboard`** 🆕 | - | 4+3 | - | **492** | - | **852** | - | **1** | **NEU — Revenue-Forecast, Currency-Scoped Sums** |
| **`expense`** 🆕 | - | 4+2 | - | **543** | - | **816** | - | **9** | **NEU — Multi-Stage-Approval-Workflow, SKR03/04-Konto-Zuweisung** |
| **`quote`** 🆕 | - | 5+5 | - | **1369** | - | **1686** | - | **11** | **NEU — eigenes Sub-Paket, Conversion-Race-Fix via Migration 000324** |
| **`recurring`** 🆕 | - | 4+4 | - | **838** | - | **1586** | - | **8** | **NEU — Idempotente Generation, finance_recurring_runs-Ledger** |
| `hr` 🆕 (namespace, 7 sub-dirs) | - | 0+5 | - | 0 | - | 984 | - | 0 | separater HR-Namespace, 7 Sub-Pakete, nicht in buchhaltung-Scope |
| **TOTAL** | **120** | **127+110=237** | **17.4k** | **31.008 (+78%)** | **12.6k** | **44.104 (+250%)** | **50+** | **151 (+200%)** | **5 NEU-Sub-Pakete, 141% Test-Ratio** |

### Migrationen 220-325 (buchhaltung-relevant)

| Nr | Name | Datum | Scope |
|---|---|---|---|
| **000243** | `add_bexio_invoice_pull` | 2026-07-05 | Bexio Welle 3b Config: invoice_pull_enabled, interval_minutes, last_pull_at |
| **000246** | `finance_recurring_invoices` | ~2026-07 | Recurring-Schedule + runs-Ledger |
| **000247** | `finance_bank_statements` | 2026-08-03 | Bank-Statement-Import-Table (MT940/CAMT053-Payload-JSONB, Hash fuer Dedup) |
| **000257** | `finance_expenses` | ~2026-08 | Expense-Approval-Workflow-Table |
| **000258** | `finance_bank_accounts` | 2026-08-03 | Bank-Account-Master-Data (IBAN, BIC, connected-Flag) |
| **000323** | `finance_invoice_number_partial_unique` | 2026-08-17 | Partial-UNIQUE auf (tenant_id, invoice_number) WHERE source='cosmi' |
| **000324** | `finance_invoice_source_quote_id_unique` | 2026-08-24 | Partial-UNIQUE auf (tenant_id, source_quote_id) WHERE status <> 'cancelled' |

**6 kritische Buchhaltungs-Migrationen in 15 Wochen**, plus ~100 andere Projekt-Migrationen (RBAC-Phase1a Mig 256, Two-Factor-Policy 273, HR-Offboarding 281-282, etc.) die buchhaltung indirect beeinflussen koennen (RBAC-Manager-Rolle Mig 214 wurde durch Mig 256 moeglicherweise ueberschrieben — zu pruefen fuer Permissions-Regression).

### Frontend Delta (modules/finanzen/)

| Metrik | W27 | W41 | Delta |
|---|---|---|---|
| Top-Level TSX/TS-Files | 30+ | 32 | +~2 |
| Gesamt Prod-LOC | 11.415 | 11.857 | +4% |
| Dialoge | 4 | 11+ | +7 (QuoteFormDialog, ExpenseFormDialog, HoursToInvoiceDialog, RecurringInvoiceDialog, ReceiptPreviewDialog, PaymentRecordDialog, ExportDialog) |
| Panels | 2 | 7+ | +5 (BankTransactionDetailPanel, ExpenseDetailPanel, QuoteDetailPanel, RecurringDetailPanel, DunningDetailPanel) |
| Widgets | 0 | 2+ | +2 (BankingWidget, CustomerAccountSection) |
| Indicators/Previews | 0 | 2+ | +2 (QRRechnungPreview, EInvoiceIndicator) |
| Lib-Utilities | 0 | 6+ | +6 (amounts-visibility, customer-account, finance-export, mini-pdf, receipt-cache, skr-accounts) |

**Nicht geliefert im Frontend**: keine AI-OCR-Upload-UI, keine PEPPOL-Config-Section, kein IncomingInvoiceAIExtractionDialog, kein Buchhaltungs-Copilot-Chat-UI.

### Integrations-Status (Delta zu W27)

**Bexio (Delta +4 Weeks of Welle 3b):**
- G1 OAuth-State-HMAC closed (W27 Status "Open")
- G2 ContactService-Wiring closed (W27 "Open")
- G3 Contact-Resolve closed (W27 "Open")
- G5 Fail-fast-ohne-VAULT closed (W27 "Open")
- G10 Sync-Core-Coverage 28% → 42% closed (W27 "Open")
- **G12 Invoice-Pull closed** (W27 noch nicht als Scope-Check-Blocker auf dem Radar — Welle 3b war Juli-Deployment)
- **Scope-Check-Status: 6/12 Blocker durch** (W27: 5/12)
- Open: Sandbox-Test ohne Test-Bexio-Account + Darien-GoBD-Counter-Signature auf G12
- Produktions-Hit: Welle 3b deployed read-only Mirror, delta-forward, keine Historie, Loop-Prevention via source='bexio'-Flag

**Lexware (Delta +2 Hygiene-Enhancements):**
- org_id-Capture bei OAuth-Connect (2026-09-09, `a0f28af9`) — relevant fuer Multi-Org-Setups
- Scheduler stop re-resolving config under system context (2026-08-23, `3dcb02f3`) — Race-Fix
- Webhook-Realtime-Sync mit HMAC-SHA256 (seit R2-P0.6, W27 bereits dokumentiert) unveraendert
- Dunning-E-Mail-Versand via Brevo-SMTP (2026-07-05, `e375b6e4`) — neue Capability

**DATEV (Delta Export-Pfad-Haertung ohne DCO-API-Start):**
- OAuth-Singleflight-per-Tenant (2026-08-22, `3b63d2c1`) — Thundering-Herd-Prevention
- Orphan-Upload-Log-Flagging (2026-08-18, `ccee9d4f`) — Monitoring
- Concurrent-OAuth-Refresh-Test NEU
- EXTF-CSV-Export-Only bleibt — kein DCO (Connect-Online)-API-Code
- Berater-/Mandant-Nr-Header (Migration 219 W27-Delivery) stabil

### Was Cosmi-buchhaltung HEUTE kann (Positive Delta)

- ✅ Alles aus W27-IST-Stand (Outgoing-Invoice-Lifecycle, ZUGFeRD-Output, XRechnung-Import, GoBD-Archiv, DATEV-CSV-Export, Dunning-Engine, Multi-Currency-Foundation, Bexio-OAuth, Lexware-Webhook, Tax-Calculator-DE, Idempotency, RBAC)
- 🆕 **Bank-Statement-Import** (MT940 + CAMT.053) mit Statement-Dedup + Transaction-Matcher + Account-CRUD (banking/)
- 🆕 **Finance-Dashboard** mit Revenue + Pipeline + Status-Breakdown + Revenue-Forecast (dashboard/)
- 🆕 **Employee-Expense-Approval-Workflow** mit SKR03/04-Konto-Zuweisung-Post-Approval + GoBD-Account-Post-Assignment (expense/)
- 🆕 **Recurring-Invoice-Scheduler** mit idempotenter Generation via finance_recurring_runs-Ledger (recurring/)
- 🆕 **Quote-als-eigenes-Sub-Paket** mit Create/Convert/Accept/Reject + Quote-to-Invoice-Race-Prevention via Partial-UNIQUE-Index (quote/)
- 🆕 **Bexio-Invoice-Pull Read-Only-Mirror** (Welle 3b, 2026-07-05)
- 🆕 **GoBD-Lock-Barrier auf alle Status-Transitions** + **Payment-Delete-Block auf GoBD-locked**
- 🆕 **E-Rechnung Inbound-Reject bei Invalid-Totals** (einvoice/validation.go)
- 🆕 **Dunning-E-Mail-Versand via Brevo-SMTP**
- 🆕 **Lexware-org_id-Capture** + Scheduler-Config-Fix
- 🆕 **DATEV-OAuth-Singleflight + Orphan-Upload-Monitoring**
- 🆕 **Invoice-Nummer-Partial-UNIQUE-Index** (Mig 323)
- 🆕 **Quote-Conversion-Race-Fix** (Mig 324)
- 🆕 **Decimal-Round-on-Write-Path** (Mig unknown, commit be1dea4d)
- 🆕 **Buyer-VAT-ID-PDF-Rendering** fuer EU-Cross-Border-Reverse-Charge
- 🆕 **Frontend: BankingWidget, QRRechnungPreview, EInvoiceIndicator, HoursToInvoiceDialog, 15+ neue Komponenten**
- 🆕 **Test-Ratio 72% → 141%** (hoechstes der Zyklus-2-Modules nach vertraege 220%)
- 🆕 **106 Migrationen in 15 Wochen** (7/Woche vs. formulare 0.2/Woche)

### Was Cosmi-buchhaltung HEUTE WEITER NICHT kann (W27-Luecken + neue)

- ❌ **KI-OCR auf Eingangsbelege** — 15 Wochen null Code (W27-Pflicht-Pick #1)
- ❌ **KI-Kontierungs-Vorschlag** — null Code
- ❌ **KI-Anomaly-Detection auf Eingangsrechnungen** — null Code
- ❌ **KI-Dunning-Brief-Personalisierung** — null Code (Brevo-SMTP-Versand ist Templates-only)
- ❌ **Cashflow-Forecast** (Dashboard hat Revenue-Forecast, aber kein ML-basiertes Liquiditaets-Forecasting)
- ❌ **PEPPOL-Access-Point** — 20% partial (nur UBL-ProfileID im Generator hardcoded)
- ❌ **PEPPOL-Sende-Pfad** (DE-B2B-Sende-Pflicht ab 01.01.2027)
- ❌ **Bank-Feed PSD2/finAPI Live-Polling** — 40% strukturell (banking/ Sub-Paket exists, aber Live-Connect explicitly deferred Phase 5)
- ❌ **DATEV-API-Realtime-Sync (DCO)** — 15 Wochen null Code (W27-Pick #S3), nur EXTF+OAuth-Upload-API
- ❌ **CH-QR-Rechnung Backend** — Frontend-UI (QRRechnungPreview.tsx) existiert, Backend `backend/internal/biz/ch_specifics/qr_invoice/` existiert NICHT
- ❌ **CH-Lohnbuchhaltung ELM** — null Code
- ❌ **CH-MWST-/AT-MWST-Saetze als Tenant-Stammdaten** — null Code (nur DE-19/7)
- ❌ **OZG-Schnittstelle DE** — null Code
- ❌ **Multi-Stage-Workflow-Approval fuer Eingangsrechnungen** — 50% partial (expense/ hat Workflow, einvoice/ hat linear-Lifecycle)
- ❌ **Corporate-Card-Integration (Pliant/AmEx)** — null Code
- ❌ **Mobile-App-Beleg-Workflow** — Cosmi weiter Desktop-Electron + PWA, kein nativ-Mobile
- ❌ **Buchhaltungs-Copilot im UI** — null Code
- ❌ **MCP-Server fuer Buchhaltung** — null Code (W33-Keeper, 10 Wochen ueberfaellig)
- ❌ **AI-Act-Art-50-Disclosure-Layer** — null Code (W39-Keeper, Grace-Period-Ende 51 Tage)
- ❌ **Multi-Provider-AI-Router** — null Code (W25-Keeper doppel-eskaliert W33)
- ❌ **Expense-Receipt-Document-Storage** — nur Filename-String (GoBD-Risiko fuer Steuer-relevante Belege)
- ❌ **Modul-Naming-Konsolidierung** — Dreifach-Diskrepanz bleibt (frontend/finanzen vs backend/biz/invoice vs sources/buchhaltung)
- ❌ **Standalone-Buchhaltungs-Preis** — Modul "in Vorbereitung" laut pricing.md, kein aktiver Standalone-SKU

### Neue Beobachtungen 2026-10-12

- **Produktions-Audit-Pflicht**: SQL auf `finance_invoices` nach Duplikat-source_quote_id-Rows (Quote-Conversion-Race-Window W27-W28)
- **PostgreSQL-14-EOL-Pruefung in 31 Tagen**: welche Prod-Instanzen laufen auf Postgres 14? Pflicht-Pruefung vor 2026-11-12
- **GoBD-Receipt-Storage-Luecke in expense/**: Receipt-Document-Attachment-Delivery vor Modul-GA
- **Keine Standalone-Buchhaltungs-Preis-Entscheidung** = Cosmi kann die 81-Tage-E-Rechnung-Welle nicht monetarisieren, auch wenn Technik-Fundament da ist

---

## Konkurrenz-Vergleichstabelle 2026-10-12 (Delta zu W27)

Nur Zeilen mit DELTA vs. W27 oder neuen Spalten gezeigt. Fuer unveraenderte Zeilen siehe W27-Report.

| Feature | Cosmi W27 | Cosmi W41 | Lexware Office | sevDesk | BuchhaltungsButler | Bexio | weclapp | Candis | Odoo | Delta-Kommentar |
|---|---|---|---|---|---|---|---|---|---|---|
| **Pricing Standalone-SKU** | 6 EUR/User-Monat | **TBD "in Vorbereitung"** | 7.90-32.90 EUR/Monat (S/M/L/XL) | 9.90-49.90 EUR | 14.90-39.90 EUR | CHF 39-159 | 39-89 EUR/User | 199+ EUR | 24.90 USD/User | **Cosmi hat keinen Standalone-Preis — kritischer Positionierungs-Verlust** |
| **Promo-Preis (Entry)** | - | - | **3.95 EUR S mit 50%-Promo 3 Monate** | ? (Feed blockiert) | - | - | - | - | - | Lexware Entry-Barrier bei 3.95 EUR |
| **KI-OCR Belege** | ❌ | ❌ (W27-Pick #1 null geliefert) | ✅ NAVI + Mobile-App | ✅ (Feed blockiert) | ✅ | ✅ Bexio-AI | ⚠️ "Q2 2026" (Status unklar) | ✅ Kern-USP | ✅ Studio-AI | Alle Konkurrenten delivered, Cosmi weiter null |
| **KI-Kontierungs-Vorschlag** | ❌ | ❌ | ✅ NAVI | ✅ | ✅ Maerz 2026 | ✅ | ✅ | ✅ | ✅ | Alle delivered, Cosmi null |
| **Multi-Provider-AI-Router (EU-Sovereign)** | ❌ | ❌ (W25/W33-Keeper, 10+ Wochen ueberfaellig) | - (US-Hyperscaler-based) | - | - | - | - | - | - | **Cosmi-strategische-Nicht-Luecke** wenn geliefert |
| **PEPPOL-AP (Versand)** | ❌ | **⚠️ UBL-ProfileID hardcoded, kein Transmission** | 🚧 Q4-2026 (Roadmap) | ⚠️ via Crossinx-TSP | ⚠️ via Crossinx-TSP | ✅ CH-AP seit Q2-2025 | ⚠️ via Crossinx-TSP | ⚠️ via Partner | ✅ Native seit Odoo 17 | 20% statt 0% — minimal |
| **PEPPOL-AP (Empfang)** | ❌ | ❌ | 🚧 Q4-2026 | ✅ via TSP | ✅ via TSP | ✅ CH-AP | ✅ via TSP | ✅ via TSP | ✅ Native | Cosmi hat UBL-Parser, aber kein Access-Point |
| **E-Rechnung-Versand DE** | ❌ | ❌ (**81 Tage bis Pflicht**) | ✅ in allen Tiers (S/M/L/XL) | ✅ (Feed blockiert) | ✅ | ✅ CH-QR + DE-XRechnung | ✅ | ✅ | ✅ | **Pflicht-Stake fuer DE->800k-EUR-Umsatz** |
| **Bank-Feed PSD2/HBCI Live** | ❌ UI-Stub | ❌ **banking/ exists aber "flag, not connection"** | ✅ finAPI Multibanking | ✅ Native | ✅ Kern-USP | ✅ ISO-20022 + finAPI | ✅ | ➖ N/A | ✅ Plaid/Yodlee | Cosmi 40% statt 0% — strukturell |
| **Bank-Statement-Upload (MT940/CAMT.053)** | ❌ | ✅ **NEU banking/ (2208 LOC)** | ✅ (Multibanking exportiert MT940) | ✅ | ✅ | ✅ | ✅ | ➖ | ✅ | Cosmi hat jetzt File-Upload-Workflow |
| **Bank-Transaktion Auto-Match** | ❌ | ⚠️ **banking/matcher.go Heuristic** (Score-based, kein AI) | ✅ NAVI + Multibanking Automatischer-Zahlungsabgleich | ✅ | ✅ KI-Score | ✅ Bexio-AI | ✅ | ➖ | ✅ | Cosmi 50% strukturell, aber kein AI-Score |
| **Steuerberater-Zugang** | ⚠️ via DATEV-Export | ⚠️ via DATEV-Export + Lexware-Elektronische-Pendelakte-ReIntegration unklar | ✅ **in ALLEN Tiers inklusive** + Elektronische Pendelakte | ✅ sevDesk Berater | ✅ | ⚠️ Limited | ✅ **kostenlos als Einzellizenz** | ❌ | ⚠️ Add-on | Lexware + weclapp dominieren Multiplier-Channel |
| **Belegerfassung Mobile-App** | ❌ | ❌ | ✅ Lexware App (Belegscanner + Belegpruefung) | ✅ | ⚠️ Limited | ✅ | ✅ | ✅ Kern-USP | ✅ Odoo Mobile | Cosmi hat PWA, aber kein Mobile-Belegscanner |
| **Workflow-Approval Multi-Stage (Expenses)** | ❌ | ✅ **NEU expense/ (543 LOC, 9 Methoden)** | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited | ✅ | ✅ | ✅ Kern-USP | ✅ | Cosmi liefert fuer Expenses, nicht fuer Eingangsrechnungen |
| **Workflow-Approval Eingangsrechnungen** | ❌ Linear-Status | ❌ Linear-Status weiter | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited | ✅ | ✅ | ✅ Kern-USP | ✅ | Luecke bleibt bestehen |
| **Recurring Invoices (idempotent)** | ⚠️ im invoice/ eingewebt | ✅ **NEU recurring/ separates Sub-Paket mit finance_recurring_runs-Ledger** | ✅ Serienrechnungen | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ Subscriptions | Cosmi-Architektur sauberer als W27 |
| **Quote-to-Invoice-Race-Safe** | ❌ Read-then-Write-Race | ✅ **NEU Partial-UNIQUE-Index Mig 324** | ✅ (angenommen) | ✅ | ✅ | ✅ | ✅ | - | ✅ | Produktions-Bug-Fix W27-Baseline |
| **Dashboard mit Revenue-Forecast** | ⚠️ FinanceDashboard-Komponente | ✅ **NEU dashboard/ Backend (492 LOC) + Revenue-Forecast** | ✅ BWA | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ✅ | Cosmi hat jetzt Backend-Dashboard |
| **GoBD-Lock-Barrier auf ALLE Status-Transitions** | ⚠️ nur Invoice-Create | ✅ **ALLE Transitions, Payment-Delete-Block** | ✅ GoBD-Langzeitbelegarchiv | ✅ | ✅ | ✅ (FINMA) | ✅ | ✅ | ⚠️ via Add-on | Cosmi auf Enterprise-Niveau |
| **E-Rechnung Inbound Validation (Reject bei Invalid-Totals)** | ⚠️ Parser | ✅ **NEU validation.go + Reject** | ✅ (angenommen) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Haertung geliefert |
| **Bexio-Integration Welle 3b (Invoice-Pull)** | ⚠️ Welle 2-3a | ✅ **NEU Read-Only-Mirror, delta-forward** | n/a | n/a | n/a | self | n/a | n/a | n/a | **Cosmi-USP: einziges Nicht-Bexio-System das Bexio-Invoices read-only spiegelt** |
| **DATEV-OAuth-Singleflight** | ❌ | ✅ **NEU per-Tenant** | ✅ DCO-API-based (unklar wie) | ✅ DCO-API | ✅ DCO-API | ⚠️ ueber Drittanbieter | ✅ DCO-API | ✅ DCO-API | ⚠️ Community-Modul | Cosmi hat Export-Pfad gehaertet, aber bleibt EXTF-only |
| **MCP-Server (Buchhaltung-Scope)** | - | ❌ (W33-Keeper, 10 Wochen ueberfaellig) | ❓ (unklar) | ❓ | ❌ | ❓ | ❓ | ❓ | ❓ | HubSpot + Twenty haben MCP, Cosmi 0 |
| **AI-Act-Art-50-Disclosure-Layer** | - | ❌ (**51 Tage bis Grace-Period-Ende**) | ⚠️ (angenommen bei NAVI) | ? | ? | ? | ? | ? | ? | Cosmi-Compliance-Risiko ohne Delivery |
| **CH-QR-Rechnung Backend** | ❌ | ❌ (Frontend-UI-only) | ❌ (DE-fokussiert) | ❌ | ❌ | ✅ Kern-USP CH | ⚠️ via Drittanbieter | ❌ | ✅ via l10n_ch | Luecke bleibt |

**Legende**: ✅ Full implementiert, ⚠️ Eingeschraenkt/Partial, 🚧 Geplant, ❌ Fehlt, ➖ N/A fuer Kategorie

**Lesart der neuen Tabelle vs W27**:
- **Cosmi-Staerken (vergleichbar/besser als Markt)**: Bank-Statement-Upload (NEU), Recurring-Idempotenz (NEU-sauberer), Quote-Conversion-Race-Safe (NEU), GoBD-Lock-Barrier-All-Transitions (NEU), Dashboard-Backend+Revenue-Forecast (NEU), E-Rechnung-Validation (NEU), Bexio-Welle-3b-Mirror (NEU-USP), DATEV-OAuth-Hardening (NEU)
- **Cosmi-Luecken strukturell schlimmer als W27**: Kein Standalone-Preis (W27 hatte 6 EUR-Anker, jetzt "in Vorbereitung"), KI-OCR+Kontierung+Anomaly (null geliefert in 15 Wochen trotz W27-Pflicht-Pick), PEPPOL-Versand (81 Tage bis DE-Pflicht), MCP-Server (10 Wochen Keeper-ueberfaellig)
- **Cosmi-Luecken-Delta neutral**: Bank-Feed-Live-Polling (strukturell 40% geliefert, aber Phase 5 explicit deferred), DATEV-DCO-API (0% bleibt), CH-QR-Rechnung-Backend (0% bleibt), KI-Buchhaltungs-Copilot (0% bleibt)
- **Markt-Shift-Konsequenz**: Lexware hat **Preis+Positioning+Content-Marketing-Push** als Compliance-Multiplier-Multiplier-Multiplier gewonnen, Cosmi hat **Backend-Hygiene-Delivery** gewonnen — zwei verschiedene Spiele

---

## Top-3 Strategische Empfehlungen W42

### Empfehlung 1 (P0, 81-Tage-Deadline): PEPPOL-Sende-Pfad-Minimal + DATEV-PEPPOL-AP-Fallback-Option

**Was**: 
1. **PEPPOL-Sende-Pfad als Minimal-MVP** mit Pagero-TSP-Integration (schnellste Time-to-Market, 2-3 Wochen) **ODER** DATEV-PEPPOL-AP-Fallback-via-Berater (wenn Tenant bereits DATEV-Berater hat). 
2. `backend/internal/biz/peppol/` mit zwei Sub-Pfaden: `tsp_adapter/pagero.go` + `datev_berater_bridge.go`. 
3. `peppol_messages`-Tabelle als Audit-Log (Migration 0325+). 
4. Neue RPCs `SendInvoiceViaPeppol`, `GetPeppolMessageStatus`. 
5. Tenant-Konfiguration: `peppol_provider: 'pagero-tsp' | 'datev-via-berater' | 'none'`. 
6. Frontend `FinanzIntegrationenTab.tsx` erweitert um PEPPOL-Konfigurations-Section mit Provider-Wahl.

**Warum jetzt P0**:
- **81 Tage bis 01.01.2027 DE-B2B-Sende-Pflicht fuer Unternehmen >800k EUR Umsatz** — Cosmi-Mittelstand-Ziel-Segment betroffen.
- **easybill-YouGov**: 74% DACH-KMU unbereit — Markt-Fenster offen, aber zeitgebunden.
- **UBL-Generator mit PEPPOL-ProfileID existiert bereits** — nur Transmission-Layer fehlt (2-3 Wochen statt 5-6 wie in W27-geplant).
- **Lexware** hat Content-Marketing bereits auf 2027-Deadline positioniert — Cosmi muss liefern + Content-Asset-Marketing-Sprint parallel.
- **Self-Hosted-AP (ph-peppol-server/Mustang)** aus W27-Empfehlung ist **Phase 2 fuer Q1 2027** (wenn Volumen >1000 Dokumente/Monat/Tenant und Pro-Document-Kosten relevant werden). **Phase 1 MVP via TSP**, weil Zeit-druck + Zertifikat-Pflege-Minimierung.

**Sprint-Anker (konkret, 2-3 Wochen Backend + 1 Woche Frontend)**:
1. Provider-Entscheidung (0.5 PT Architecture-Review): Pagero vs. Crossinx vs. B2Brouter als TSP + DATEV-AP-via-Berater als zweiter Pfad. **Empfehlung**: Pagero (DACH-Prasenz, EU-Hosting, dokumentierte API, Per-Document-Pricing 0.10-0.30 EUR). DATEV-via-Berater als Zweit-Pfad fuer Tenants mit bestehendem DATEV-Berater.
2. `backend/internal/biz/peppol/tsp_adapter/pagero.go` — Pagero-REST-Client fuer Submit-Invoice-UBL (3-4 PT)
3. `backend/internal/biz/peppol/datev_berater_bridge.go` — DATEV-AP-Nutzung ueber DATEV-API-Config-Flag (2 PT, nutzt bestehende DATEV-OAuth-Infrastruktur)
4. Migration 0325+ `create_peppol_messages` + `add_peppol_config_to_tenants` (peppol_provider, peppol_id, smp_url) (1 PT)
5. RPCs `SendInvoiceViaPeppol`, `GetPeppolMessageStatus`, `ListPeppolMessages` (2 PT)
6. Frontend `FinanzIntegrationenTab.tsx` PEPPOL-Section + Discovery-Lookup-UI (3 PT)
7. **PEPPOL-Zertifikat-Bestellung bei TSP** (1-2 Wochen Lead-Time, parallel zu Development)
8. **Content-Marketing-Asset**: Landing-Page `/features/e-rechnung-2027/` mit Self-Service-Compliance-Check (via W23-Keeper `e-rechnungspflicht-2027-74-nicht-bereit`)

**Kosten-/Wert-Schaetzung**: 10-12 PT Backend + 3-4 PT Frontend + 2 PT Content = **2-3 Wochen total mit 1 Senior + 1 Mid + Marketing-Pair**. Recurring-Kosten: Pagero-Pricing + DATEV-AP (abhaengig von Berater-Setup). **ROI**: Compliance-Pflicht-Stake fuer DACH-Mittelstand ab 2027-01-01 + Marketing-Narrative "Cosmi ist bereit, 74% des Marktes nicht" + Steuerberater-Kanal-Entry via DATEV-PEPPOL-AP.

**Owner-Vorschlag**: Backend-Senior (TSP-Adapter + Migration), Backend-Mid (Frontend + Routes), PM (Content-Asset).

**Deadline-Rahmen**: Code live bis **2026-11-30** (3 Wochen vor Deadline fuer QA + Zertifikat-Aktivierung), Content-Asset live bis **2026-11-15** fuer Lead-Gen-Window.

### Empfehlung 2 (P0, 51-Tage-Deadline): AI-Compliance-Foundation-Sprint Cosmi-weit

**Was** (W39-Keeper eskaliert mit Buchhaltungs-Perspektive):
1. `backend/internal/ai/providers/router/` mit Haiku 5.5 Primary + Mistral Large 4 EU-Fallback + Kolibri 78B On-Premise-Option (W25-Keeper, W33-doppel-eskaliert, 10+ Wochen ueberfaellig)
2. `backend/internal/compliance/ai_disclosure/` Package mit Machine-Readable-Marking-Service + Audit-Log + Human-Review-Pflichtschritt-Enforcement (W39-Keeper, 51 Tage bis Grace-Period-Ende)
3. Retrofit Wave-7C Meeting-AI-Summary mit Disclosure-Layer (schliesst W38-Wiki-P0 + W39-Helpdesk-P0 + W41-Vertraege-P0 gleichzeitig)
4. **Buchhaltungs-spezifisch**: `backend/internal/biz/einvoice/ai_extraction/` mit Haiku 5.5 Primary + Mistral Large 4 Fallback als erste produktive AI-Feature im Buchhaltungs-Modul — **Beleg-Foto-OCR + Lieferant-/Datum-/Betrag-/Steuersatz-Extraction + Konto-Vorschlag mit Confidence-Score**, Disclosure-by-Design seit Tag 1, Human-Review-Pflicht vor `booked`-Status.
5. `ocr_correction_history`-Tabelle pro Tenant fuer aktive Lern-Schleife (Korrektur-Persistenz)
6. Frontend `IncomingInvoiceAIExtractionDialog.tsx` mit Drag-Drop-Upload-Pfad + AI-Pre-Fill-UI + Disclosure-Badge "AI-extrahiert — bitte pruefen"

**Warum jetzt P0 kombiniert**:
- **51 Tage bis EU AI Act Art. 50 Grace-Period-Ende 2026-12-02** — Machine-Readable-Marking-Pflicht aktiv.
- **Cosmi laeuft seit 2026-08-02 (71 Tage) Wave-7C Meeting-AI-Summary ohne Disclosure-Layer** — operatives Non-Compliance-Fenster seit W37 identifiziert, bisher ignoriert.
- **Haiku 5.5 bei $0.10/$0.50 Cached-Input** macht die Kosten-Barriere trivial: 50-200 Belege × 2000 Tokens = 400k Tokens = **$0.04 pro Tenant-Monat** (W27-Kalkulation war 4-16 EUR mit Mistral OCR 4, jetzt ca. 100× guenstiger).
- **Multi-Provider-Router ist Pflicht-Fundament** fuer Disclosure-Layer-Retrofit (ohne Router kein konsistenter Disclosure-Pfad ueber alle Features).
- **EU-Sovereign-Triade materialisiert heute** (Haiku 5.5 + Mistral Large 4 + Kolibri 78B) — Entscheidung-Window ist offen.
- **Pattern-Breaker**: Buchhaltung-Team ist das liefers-staerkste Backend-Team (+78% Prod-LOC in 15 Wochen) — hier anfangen mit AI-Pipeline-Delivery schafft Vorbild-Pattern fuer andere Module.
- **Lexware NAVI-Narrative gegenkontern**: Cosmi-AI-Pipeline ist Open-Source-pfadbar (Kolibri On-Premise) + auditierbar + im Self-Host-Mode komplett ohne US-Hyperscaler-Beruehrung — das kann Lexware nicht sagen.

**Sprint-Anker (konkret, 6-8 Wochen, parallel zu Empfehlung 1)**:
1. **Woche 1**: Multi-Provider-Router-Skeleton (`backend/internal/ai/providers/router/`) mit Haiku-Adapter + Mistral-Adapter + Interface-Abstraktion (4 PT)
2. **Woche 2**: AI-Disclosure-Layer-Package (`backend/internal/compliance/ai_disclosure/`) mit Machine-Readable-Marking + Audit-Log + Human-Review-Guard (5 PT)
3. **Woche 2 parallel**: Wave-7C Meeting-AI-Summary Retrofit mit Disclosure-Layer (3 PT)
4. **Woche 3-4**: Buchhaltungs-AI-Extraction (`backend/internal/biz/einvoice/ai_extraction/mistral_adapter.go` + `haiku_adapter.go` + `ocr_result.go` + Routing-Policy) (8 PT)
5. **Woche 4**: `ocr_correction_history`-Migration 0326+ (1 PT)
6. **Woche 5**: Frontend-Dialog `IncomingInvoiceAIExtractionDialog.tsx` + Disclosure-Badge-Component + Human-Review-Workflow-Integration (5 PT)
7. **Woche 6**: Konto-Vorschlag-Mapping (Mistral-OCR-Output → SKR03/SKR04-Konto-Suggestion via Rule-Base + Haiku-Fallback bei unklaren Faellen) (3 PT)
8. **Woche 7-8**: Testing + E2E-Hardening + Rollout-Feature-Flag `features.ai_ocr_extraction` (3 PT)

**Kosten-/Wert-Schaetzung**: 32-35 PT Backend + 5 PT Frontend = **6-8 Wochen total mit 2 Senior + 1 Mid**. Recurring-Kosten: ~$0.04-$2.00 pro Tenant-Monat je nach Beleg-Volumen (Haiku-Primary) + Mistral-Fallback optional. **ROI**: 
- Compliance-Pflicht-Stake bis 2026-12-02 fuer Art. 50 Disclosure
- Erste AI-Feature im reifsten Cosmi-Modul (Delivery-Momentum)
- Pricing-Argument-Verteidigung gegen Lexware NAVI
- Pattern-Vorbild fuer naechste AI-Features (helpdesk-Draft, vertraege-Klausel-Extract)
- Narrative-Grundlage fuer "Cosmi EU-Sovereign-AI-Pipeline mit Open-Source-On-Premise-Option"

**Owner-Vorschlag**: AI-Lead (Router + Disclosure-Layer), Buchhaltungs-Senior (AI-Extraction-Adapter), PM (Rollout-Plan).

**Deadline-Rahmen**: 
- Multi-Provider-Router + Disclosure-Layer live bis **2026-11-30** (vor Art-50-Grace-Period-Ende)
- Wave-7C Meeting-AI-Summary Retrofit bis **2026-11-30**
- Buchhaltungs-AI-Extraction MVP bis **2026-12-15** (Soft-Launch)
- GA bis **2027-01-15** (nach PEPPOL-Compliance-Welle)

### Empfehlung 3 (P1, 10-Wochen-Keeper-Rueckstand): Cosmi-MCP-Server mit Buchhaltungs-Scope-Phase-1

**Was**:
1. `backend/internal/core/mcp-server/` als Core-Service mit MCP-Spec-Implementation (Resource/Tool/Prompt-Primitives)
2. **Buchhaltungs-Phase-1-Scope** als erste 5 produktive MCP-Tools:
   - `invoice_read(invoice_id)` — Read-Only Single-Invoice
   - `invoice_list_by_contact(contact_id, status_filter)` — Read-Only List
   - `ledger_query_summary(from_date, to_date, account_filter)` — Read-Only Summary-Aggregation
   - `dashboard_summary(tenant_id)` — Read-Only Dashboard-Snapshot
   - `incoming_invoice_list(status_filter)` — Read-Only Eingangsrechnung-Liste
3. **Cross-Modul-Query-Tool als USP-Realizer**: `cross_module_customer_context(contact_id)` — Combined-View ueber CRM-Contact + Open-Invoices + Dunning-Status + Vertraege + Rapporte-Hours (nutzt bestehende contact_id-FK aus Migration 141 + helpdesk_ticket_contact_org aus Migration 267 + vertraege-entity-links)
4. OAuth-Scopes pro Tool (`mcp.buchhaltung.read` + `mcp.cross_module.read`)
5. Rate-Limiting pro MCP-Client-Verbindung
6. Audit-Log fuer alle MCP-Tool-Calls

**Warum jetzt P1 (nach #1 und #2)**:
- **W33-Keeper `backend/internal/core/mcp-server/`** 10 Wochen ueberfaellig
- **HubSpot MCP live seit W40, Twenty MCP seit W41** — DACH-KMU-Prospects fragen nach MCP-Zugang in Pitches
- **Cross-Modul-Query ist Cosmi-USP** gegen Lexware/sevDesk/Bexio (die haben kein CRM-/Rapporte-/Verträge-Modul mit tiefer Integration)
- **Phase-1-Scope-Minimal (5 Tools)** ist 3-5 Tage Backend-Aufwand, weil `biz/invoice/service.go` + `biz/dashboard/service.go` + `biz/einvoice/service.go` die Business-Logik bereits bereitstellen
- **MCP ohne AI-Disclosure-Compliance = Rechtsrisiko** — deshalb nach Empfehlung 2 (AI-Compliance-Foundation)

**Sprint-Anker (konkret, 1-2 Wochen Backend)**:
1. `backend/internal/core/mcp-server/server.go` — MCP-Spec-Server-Implementation (3-4 PT)
2. `backend/internal/core/mcp-server/tools/invoice_tools.go` — 3 Invoice-Tools (2 PT)
3. `backend/internal/core/mcp-server/tools/ledger_tools.go` — 2 Ledger-Tools (2 PT)
4. `backend/internal/core/mcp-server/tools/cross_module.go` — Cross-Modul-Customer-Context (3 PT, nutzt bestehende Links)
5. OAuth-Scopes + Rate-Limiting + Audit-Log (2 PT)
6. Integration-Tests + MCP-Spec-Compliance-Tests (3 PT)
7. Marketing-Content: "Cosmi-MCP-Server fuer Claude/ChatGPT/Gemini — Cross-Modul-Buchhaltung-Query ohne Lock-in" als Blog-Post + Demo-Video

**Kosten-/Wert-Schaetzung**: 15-18 PT Backend = **~2 Wochen mit 1 Senior**. Recurring-Kosten: minimal (Rate-Limiting-Overhead). **ROI**: 
- W33-Keeper-Schluss nach 10 Wochen Rueckstand
- Agent-Platform-Positionierung (HubSpot + Twenty-Antwort)
- Cross-Modul-USP-Realization (Marketing-Narrative)
- Lovable-Substitutions-Antwort (W33-Keeper): Cosmi als Business-Logic-Backend fuer Lovable-built UIs

**Owner-Vorschlag**: Backend-Senior (MCP-Core + Cross-Modul-Tool), Marketing (Blog + Demo-Video).

**Deadline-Rahmen**: Phase-1-MCP live bis **2026-12-20** (parallel zu AI-Compliance-Foundation-Finish).

### Sekundaere Empfehlungen (nicht Top-3, aber dokumentiert)

- **S2 Produktions-Audit auf Quote-Conversion-Race-Window**: SQL-Query auf `finance_invoices` nach Duplikat-source_quote_id-Rows (W27-W28, 6-Wochen-Fenster vor Migration 324). Owner: DBA, 1 PT. **Pflicht-Aktion**.
- **S2 PostgreSQL-14-EOL-Audit**: Welche Prod-Instanzen laufen auf Postgres 14? Upgrade-Plan auf 16/17 vor 2026-11-12. Owner: Platform-Lead, 2-3 PT Audit + 1-2 Wochen Upgrade. **31 Tage Deadline**.
- **S3 Expense-Receipt-Document-Storage**: Document-Attachment statt Filename-String fuer GoBD-konformes Belegarchiv. Nutze bestehende `gobdarchive`-Infrastruktur. Owner: Buchhaltungs-Mid, 3-4 PT. **Vor Modul-GA Pflicht**.
- **S3 sources/buchhaltung.yaml alternative URL-Varianten**: sevDesk + Bexio Feed-Blackout-Fallback via G2-Scrape + alternative TLD-Varianten. Owner: Intel-System-Maintainer, 2 PT.
- **S3 Standalone-Buchhaltungs-Preis-Entscheidung**: Welcher EUR-Monatspreis fuer Cosmi-Buchhaltung als Standalone-SKU? Vorschlag: 8 EUR/User/Monat (unter Lexware M-Tier 12.90, unter sevDesk-Rechnung 9.90, als EU-Sovereign-Positioning) + +2 EUR/User/Monat Cross-Modul-Bundle-Rabatt bei CRM+Buchhaltung-Kombination. Owner: Product, 1-2 Wochen Entscheidungs-Prozess.
- **S4 Steuerberater-Partner-Programm-Draft**: Cosmi-DATEV-Berater-Zugang + Elektronische-Pendelakte-Analog + Multiplier-Channel-Content. Nutze Lexware-Positioning-Vorlage (W41-Skill-Stack-Enabler-Analyse). Owner: Marketing + Sales, 4-6 Wochen Draft + Pilot.
- **S4 CH-Markt-Positionierung-Entscheidung**: Mit Bexio-Welle-3b Mirror jetzt live — Cosmi hat strukturellen Partner-Vorteil fuer CH-KMU-Prospects, aber kein CH-QR-Rechnung-Backend. Entscheidung: Bexio als CH-Buchhaltungs-Vorlieferant positionieren + Cosmi-CRM+Helpdesk+Rapporte als Erweiterungs-Package? Owner: Product + CH-Country-Lead, 2 Wochen.
- **S5 AI-Buchhaltungs-Copilot im UI (Phase 2 nach Empfehlung 2)**: Konversationaler Assistant auf Buchhaltungs-RPCs (Read-Only MVP) via Haiku 5.5 + Mistral Large 4 Tool-Calling. 10-15 PT, nach Q1 2027. **Phase 2**, nicht Phase 1.
- **S5 Bank-Feed-finAPI-Live-Polling (Phase 5)**: PSD2/finAPI-Adapter in `banking/` einbauen — der banking/-Sub-Paket-Code ist schon strukturiert vorbereitet (ConnectAccount-Methode mit explizitem "lean marker"). ~8-10 PT, nach Q1 2027.

---

## Quellen

**Markt-Recherche**:
- `pricing_snapshots/lexoffice.md` (2026-10-12) — Lexware-Office-Preis-Umbau S/M/L/XL + 50%-Promo
- `pricing_snapshots/sevdesk.md` (403 Blackout seit W29)
- `pricing_snapshots/bexio.md` (404 Blackout seit W27)
- `pricing_snapshots/weclapp.md` (stabil per 2026-10-12)
- `pricing_snapshots/odoo.md` (403 Blackout)
- `keepers/e-rechnungspflicht-2027-74-nicht-bereit-easybillyo-cross-w23.md` — easybill YouGov-Studie
- `keepers/eu-sovereignty-kipppunkt-5-signale-an-einem-tag-9--cross-w20.md` — W41-Eskalation
- `weekly/2026-W29.md`, `2026-W30.md`, `2026-W31.md`, `2026-W40.md`, `2026-W41.md` — Lexware NAVI-Positionierung, EU-Sovereign-AI-Triade, HubSpot UNBOUND MCP, Twenty v2.45 MCP
- `daily/2026-10-06-evening.md` — Mistral Large 4 Release
- `daily/2026-10-08-evening.md` — Kolibri 78B Benchmarks + Haiku 5.5 Release
- `daily/2026-10-07-evening.md` — OpenAI Decisions API Public Beta
- `daily/*-regulation.md` 2026-07-04 bis 2026-10-10 — EU AI Act Art. 50 Grace-Period, DSGVO-Enforcement (CNIL EXTIA, Google €403M, Uber €824M)

**Cosmi-Code-Stand-Recherche**:
- `backend/internal/biz/` — alle 17 Sub-Pakete gelesen, LOC-Zaehlung, Service-Methoden-Enumeration
- `backend/internal/biz/einvoice/generator_ubl.go:32` — PEPPOL-ProfileID hardcoded
- `backend/internal/biz/banking/service_accounts.go:131-138` — "lean: a flag, not a connection"-Kommentar
- `backend/internal/featureflag/registry.go:67-68` — modules.buchhaltung Flag-State
- Git-Log fuer buchhaltung-relevante Commits seit 2026-06-29 (ca. 60+ relevante Commits analysiert)
- Migrationen 000220-000325 (106 Migrationen, 6 buchhaltung-relevant)
- `desktop/src/renderer/src/modules/finanzen/` — 32 TSX/TS-Files inventarisiert, Delta zu W27 dokumentiert
- `KMU-Hub/.knowledge/pricing.md` — Buchhaltung "in Vorbereitung", kein Standalone-Preis
- `KMU-Hub/.knowledge/integrationen.md` — Bexio-Welle-3b-Deployment-Timeline, Lexware-Dunning-Email-Delivery
- `KMU-Hub/.knowledge/milestones.md` — Launch-Target 2026-09-01 (revidiert von 2026-07-01)

**Kontext aus laufenden Intel-Berichten**:
- `monthly/2026-06-29-deepdive-buchhaltung.md` — W27-Baseline (dieser Delta-Report)
- `monthly/2026-10-05-deepdive-vertraege.md` — W41-Delta-Pattern mit 3/12-Delivery-Rate
- `monthly/2026-09-28-deepdive-formulare.md` — W40 mit Backend-Hygiene-schnell + AI-Compliance-langsam Pattern
- `monthly/2026-09-21-deepdive-helpdesk.md` — W39 AI-Compliance-Foundation-Sprint-Konzept-Original
- `monthly/2026-09-14-deepdive-wiki.md` — W38 AI-Act-Art-50-Grace-Period-Erstbeobachtung
- `MEMORY.md` keepers_summary — W33-Keeper mcp-server + ai-provider-router Doppel-Eskalation

**Nicht in Deepdive-Scope** (fuer kuenftige Berichte):
- G2/Capterra-Review-Scrape fuer sevDesk + Bexio (manuelle Beobachtung bei Feed-Blackout)
- DATEV-DCO-API-Rate-Limits (fuer Phase-2-Sprint relevant)
- CH-ESR-Spec-Dokumente (fuer CH-QR-Rechnung-Backend relevant)
- Pliant-Partner-API-Dokumente (Phase-2 nach S4)

---

## Picks (vorgeschlagen)

[ ] 🟢 **P0 PEPPOL-Sende-Pfad-MVP + DATEV-PEPPOL-AP-Fallback (Empfehlung 1)** — 2-3 Wochen Backend + 1 Woche Frontend, Pagero-TSP + DATEV-via-Berater, Content-Asset-Marketing-Sprint parallel. **Stake**: 81 Tage bis DE-B2B-Sende-Pflicht 01.01.2027 fuer >800k-EUR-Umsatz-Unternehmen, 74% DACH-KMU-Markt-Fenster offen.

[ ] 🟢 **P0 AI-Compliance-Foundation-Sprint Cosmi-weit + Buchhaltungs-AI-Extraction (Empfehlung 2)** — 6-8 Wochen mit 2 Senior + 1 Mid, Haiku 5.5 Primary + Mistral Large 4 EU-Fallback + Disclosure-Layer-Package + Wave-7C-Retrofit + Buchhaltungs-OCR als erste produktive AI-Feature. **Stake**: 51 Tage bis Art-50-Grace-Period-Ende 2026-12-02, 10+ Wochen Keeper-Rueckstand, EU-Sovereign-Triade-Window gerade offen.

[ ] 🟢 **P1 Cosmi-MCP-Server mit Buchhaltungs-Scope-Phase-1 + Cross-Modul-Query (Empfehlung 3)** — ~2 Wochen Backend, 5 MCP-Tools (invoice-read, list-by-contact, ledger-summary, dashboard, incoming-list) + Cross-Modul-Customer-Context-Tool als USP-Realizer. **Stake**: W33-Keeper 10 Wochen ueberfaellig, HubSpot + Twenty MCP live, Lovable-Substitutions-Antwort.

[ ] 🟡 **S2 Produktions-Audit auf Quote-Conversion-Race-Duplikate** (SQL-Query auf finance_invoices WHERE source_quote_id duplikat vor Mig 324) — 1 PT DBA, Pflicht-Aktion.

[ ] 🟡 **S2 PostgreSQL-14-EOL-Audit + Upgrade-Plan** — 31 Tage Deadline 2026-11-12, CVE-2026-2006-Risk.

[ ] 🟡 **S3 Expense-Receipt-Document-Storage** — nutze bestehende gobdarchive-Infrastruktur, 3-4 PT, GoBD-Compliance vor Modul-GA.

[ ] 🟡 **S3 sources/buchhaltung.yaml Feed-Blackout-Fallback** — sevDesk/Bexio alternative URL-Varianten + G2-Scrape-Backup, 2 PT.

[ ] 🟡 **S3 Standalone-Buchhaltungs-Preis-Entscheidung** — Vorschlag 8 EUR/User/Monat + Cross-Modul-Bundle-Rabatt, 1-2 Wochen Product-Entscheidung.

[ ] 🟡 **S4 Steuerberater-Partner-Programm-Draft** — Cosmi-DATEV-Berater-Zugang + Elektronische-Pendelakte-Analog + Multiplier-Channel-Content, 4-6 Wochen.

[ ] 🔵 **S4 CH-Markt-Positionierung-Entscheidung** — Bexio-als-CH-Buchhaltungs-Vorlieferant + Cosmi-als-Erweiterungs-Package positionieren, 2 Wochen Product+CH-Country-Lead.

[ ] 🔵 **S5 AI-Buchhaltungs-Copilot im UI (Phase 2 Q1 2027 nach Empfehlung 2)** — konversationaler Assistant auf Buchhaltungs-RPCs via Haiku 5.5 + Mistral Large 4 Tool-Calling, 10-15 PT.

[ ] 🔵 **S5 Bank-Feed-finAPI-Live-Polling (Phase 5)** — PSD2/finAPI-Adapter in bestehender banking/-Struktur einbauen, 8-10 PT.

---

## Meta-Lesson W42

**Pattern bestaetigt seit Zyklus 2 Beginn (W35-W41 jetzt plus W42)**: Backend-Infrastruktur wird in jedem Modul schnell geliefert, strategische Markt-Luecken (AI + Compliance + Cross-Modul-Context + MCP) werden langsam oder gar nicht geliefert. **Buchhaltung ist das reifste Beispiel** — 7 Grossdeliveries nicht in W27 prognostiziert (Welle 3b, banking/, dashboard/, expense/, recurring/, quote/, GoBD-Lock-Barrier-All-Transitions), Prod-LOC +78%, Test-LOC +250%, Test-Ratio 141%, 106 Migrationen in 15 Wochen. **Gleichzeitig** sind alle drei W27-Pflicht-Picks null bis minimal geliefert (OCR 0%, PEPPOL 20% partial, Bank-Feed 40% strukturell deferred).

**Hypothese**: Backend-Team hat Dependency-Dichte als Delivery-Pfad gewaehlt (Idempotenz, GoBD-Lock, Race-Fix, Test-Coverage) weil das intern bewertbar + testbar + sicher-rueckbaubar ist. AI/PEPPOL/MCP sind extern-abhaengig (Provider-Verfuegbarkeit, Marktzeitpunkt, regulatorische Deadlines) + nicht idempotent testbar + schlechter rueckbaubar. **Konsequenz**: Deepdive-Report-Empfehlungen muessen in Zyklus 3 (W50-W64) **mit expliziter extern-vs-intern-Dependency-Markierung** geliefert werden, damit Backend-Team Risk-Appetite-Entscheidungen frueher trifft.

**Zweite Meta-Lesson**: Produktions-Audit-Pflicht-Items (wie Quote-Race-Window-SQL-Audit, PostgreSQL-14-EOL-Audit) muessen in Deepdive-Reports als **DBA-Owner-Items** mit expliziter 1-PT-Owner-Zuordnung aufgenommen werden, nicht nur im Report-Text versteckt. Verlorene Daten (Doppel-Invoices in Prod-DB) sind weder von Dev-Team noch von Deepdive-Autor wiederhergestellt. Sprint-Pflicht fuer Analyst: Produktions-Audit-Section in jedem Zyklus-2-Deepdive explizit als separates To-Do.

**Dritte Meta-Lesson**: **Feed-Blackout bei zwei groessten Konkurrenten (sevDesk + Bexio) ueber 7 Wochen** ist strukturelles Beobachtungs-Problem, nicht nur taktisches Feed-Mapping. Pipeline-Pflicht: alternative URL-Varianten + G2-Scrape-Fallback + LinkedIn-Signal + Trustpilot-Scrape pro Konkurrent als rotatives Fallback-Set in sources/*.yaml.

**Vierte Meta-Lesson**: EU-Sovereign-AI-Triade (Mistral Large 4 + Kolibri 78B + Haiku 5.5) materialisiert in 48 Stunden am 6.-8. Oktober. Das ist ein **einmaliges Positionierungs-Window** fuer Cosmi — in 3-6 Monaten sind diese Modelle Standard, in 12 Monaten sind sie oder ihre Nachfolger allgegenwaertig. **Entscheidungs-Dringlichkeit** fuer Multi-Provider-Router-Delivery ist jetzt max.

Picks bereit zum Push in `#trends` wenn `DISCORD_WEBHOOK_TRENDS` gesetzt — Deepdive-Header + Top-3-Empfehlungen als Embed-Buttons.
