---
year: 2026
week: 27
modul: buchhaltung
created: 2026-06-29
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 48
tokens_input: ~340000
tokens_output: ~19500
rotation_position: 8/15
---

# Deepdive: buchhaltung (Mo W27/2026)

> **Achter Deepdive der Rotation.** Vorgaenger: `crm-core` (W19, 2026-05-11), `dialer` (W20, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01), `helpdesk` (W24, 2026-06-08), `formulare` (W25, 2026-06-15), `vertraege` (W26, 2026-06-22). Naechstes Modul gemaess Rotation: **rapporte** (KW28, 2026-07-06). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-buchhaltung (2026-06-29):** Backend `backend/internal/biz/` ist das **mit Abstand reifste Cosmi-Modul** — 11 Sub-Pakete mit **~17.6k LOC Production-Code + ~14.4k LOC Test-Code (~32k LOC gesamt)**: `invoice` (10 Files, 1944 LOC prod / 2160 LOC test, **14 Service-Methoden** Create/GetByID/List/Update/Send/MarkPaid/Cancel/DetectOverdue/CreateFromQuote/LinkTimeTracking/ListForDATEVExport + Storno/Recurring/EventEmitter), `creditnote` (7 Files, 958/1100 LOC, 7 Methoden), `dunning` (6 Files, 928/1062 LOC, 7 Methoden inkl. **`DetectAndCreateDunnings`** Auto-Mahnungs-Engine + `CalculateInterest`-Verzugszinsen + GoBD-konformer `service_gobd.go`), `einvoice` (10 Files, 1194/637 LOC, **4 Methoden** Import/Get/List/UpdateStatus mit ZUGFeRD/Factur-X CII + XRechnung UBL + PDF-Attachment-Extract via pdfcpu), `datev` (11 Files, 1389/486 LOC, EXTF-Format-CSV-Stream-Writer mit Berater-/Mandant-Nr-Header + Debitoren-Konten-Mapping), `gobdarchive` (6 Files, 615/405 LOC, **immutable §147-AO-Archiv** mit SHA-256-Hex + 10-Jahre-Retention + Append-Only-Event-Log inkl. integrity_check-Events), `pdf` (4 Files, 1095/210 LOC, Maroto-v2-Generator fuer Quote/Invoice/CreditNote/**ZUGFeRDInvoice**/Dunning), `payment` (4 Files, 549/775 LOC, atomar mit `transitionToPaidInTx`/`revertPaidStatusInTx` und Idempotency-Key-Spalte seit Migration 215), `tax` (2 Files, 112/181 LOC, Standard/ReverseCharge/Kleinunternehmer + DE-19%/7%-Saetze), `bexio` (35 Files, 3607/2763 LOC, OAuth + Contact-/Invoice-/Quote-Push + Payment-Polling + Rate-Limiter, **G1-G5+G10 von 12 Scope-Check-Blockern geschlossen 2026-06-17**), `lexware` (25 Files, 3030/869 LOC, API-Key+Vault, Contact-Sync, Invoice/Quote-Push, **Webhook-basierter Realtime-Sync mit HMAC-SHA256-Verifikation** seit R2-P0.6 Commit `787c327`). **15 finanzrelevante Migrationen**: 000045 (create_finance_tables — Quote/Invoice/CreditNote/Dunning/Payment Basis), 000055 (Bexio-Integration), 000056 (Lexware+DATEV-API), 000061 (ZUGFeRD + Hourly-Rate), 000132 (finance_line_items-Normalisierung **nach ADR-0007**), 000133 (line_items-Backfill), 000137 (Advisory-Protocols fuer Distributed-Locking), 000139 (**GoBD-Belegarchiv** mit `gobd_documents` + `gobd_document_events` + immutable Trigger + ENUM `gobd_document_type` mit invoice/credit_note/receipt/contract/correspondence/other), 000140 (**finance_incoming_invoices** mit JSONB-LineItems/TaxBreakdown + `original_xml` verbatim + UNIQUE(tenant,supplier,number)-Dedup + Status received/reviewed/booked/rejected), 000141 (finance_invoices.contact_id-FK), 000214 (seed finance Manager-Permissions), 000215 (Payments-Idempotency-Key), 000216 (Currency-Spalte CHAR(3) DEFAULT 'EUR' auf Quote/Invoice/CreditNote — B6/Multi-Waehrungs-Vorbereitung), 000217 (drop line_items JSONB — Phase-2-ADR-0007-Abschluss), 000219 (DATEV consultant_client_numbers — Berater-Nr+Mandanten-Nr per Tenant). Frontend `desktop/src/renderer/src/modules/finanzen/` (Modul-Ordner heisst **finanzen, nicht buchhaltung** — wichtige Naming-Diskrepanz zur Backend-/Sources-YAML/Pricing-Karte): **11.415 LOC** ueber 30+ TSX/TS-Files (FinanzenPage, FinanceDashboard, InvoiceDetailPanel/FormDialog, OpenItemsTab, TransactionsTab, ExpensesTab, BerichteTab, FinanzIntegrationenTab, StammdatenTab, BelegketteTab, RecurringInvoicesTab, DunningPanel, CreditNoteDialog, BankConnectDialog, KontierungSettings, PDFPreviewPanel, FinancePersonalPrefs) + API-Layer `api/finance-client.ts` + Hooks `api/hooks/useFinance.ts` + `api/hooks/useFinanceLedger.ts`. Modul-Pricing-Anker (`KMU-Hub/.knowledge/pricing.md`): **6 EUR/User-Monat** als Cosmi-Buchhaltungs-Anker — sevDesk ab **10 EUR/Monat**, Lexoffice ab **7 EUR/Monat** (lt. Markt-Vergleich-Spalte). Feature-Flag-Gate `modules.buchhaltung` (DefaultEnabled: false, `COSMI_MODULE_BUCHHALTUNG_ENABLED`, SafeRisk, LLMToggleSafe).

> **Drei strukturelle Beobachtungen, die jeden Sprint-Plan kalibrieren.** **#1 buchhaltung ist Cosmi's reifestes Modul — und gleichzeitig das mit der konkretesten KI-Marktforderung 2026.** Anders als bei `vertraege`-Deepdive W26 (Backend ist Stub, Frontend laeuft auf Mocks) und `formulare`-Deepdive W25 (FormField-Typen driften zwischen Frontend/Backend) ist buchhaltung **Production-grade integriert**: Outgoing-Invoice mit ZUGFeRD-PDF-Generierung, Incoming-E-Rechnung mit ZUGFeRD/Factur-X-CII + XRechnung-UBL-Parsing, DATEV-EXTF-Stream-Writer mit Berater-/Mandant-Nr, GoBD-immutable-Archiv mit SHA-256 und 10-Jahre-Retention, Bexio-OAuth-Sync + Lexware-Webhook-Realtime, Dunning-Auto-Engine mit Verzugszins-Berechnung, Multi-Currency-Vorbereitung, Idempotency-Key auf Payments. Die meisten regulatorischen Hard-Requirements (XRechnung-B2G-Pflicht seit 2020, ZUGFeRD-3.0-Outgoing, GoBD-Archiv, §147-AO-Retention, DATEV-Export, Multi-Currency-DACH) sind **mechanisch erfuellt**. **ABER: die Markt-Erwartung 2026 verschiebt sich von "Buchhaltung-Software erfasst Belege korrekt" zu "Buchhaltung-Software macht den Buchhalter ueberfluessig"** — getrieben durch Mistral OCR 4 (heute $4/1000 Seiten Self-Hosted-DSGVO, vgl. `daily/2026-06-25-evening.md` Item `EVE-2026-06-25-mistral-ocr-4` n_sources:4), Lexware NAVI (KI-Buchhaltungs-Co-Pilot live seit Q1 2026), sevDesk Belegmodul mit Auto-Kategorisierung, Candis-Reise von "Reisekosten-Tool" zu "AP-Automation". **Cosmi hat 0 KI in `backend/internal/biz/`**. Kein OCR, kein Auto-Kontierungs-Vorschlag, kein Cashflow-Forecast, keine Anomaly-Detection auf Eingangsrechnungen, keine Dunning-Brief-Personalisierung. Das ist die **konkreteste KI-Pflicht-Stelle des gesamten Cosmi-Stacks** — weil die Konkurrenz hier nicht ankuendigt (wie bei vertraege/CLM-Agenten), sondern **liefert seit 6 Monaten**. **#2 PEPPOL-Pfad fehlt vollstaendig — der DACH-B2B-Standard-Wechsel 2027/2028 wird Cosmi-Kunden hart treffen.** Cosmi-buchhaltung unterstuetzt heute XRechnung-UBL und ZUGFeRD-CII als File-Formate fuer Import (Migration 140) und ZUGFeRD-Output fuer Outgoing (PDF mit eingebettetem XML). **Aber: kein PEPPOL-Access-Point, kein BIS-Billing-3.0-Versand, kein 4-Corner-Model-Adapter.** Die EU-Kommission hat im April 2026 das "VAT in the Digital Age" (ViDA) Paket verabschiedet — **B2B-PEPPOL-Pflicht ab 2030 EU-weit** (Echtzeit-Meldung an Steuerbehoerden via PEPPOL), aber **mehrere Mitgliedstaaten ziehen vor**: Deutschland (B2B-XRechnung-Empfangs-Pflicht seit 2025-01-01, Sende-Pflicht ab 2027-01-01 fuer Unternehmen >800k EUR Umsatz, ab 2028-01-01 fuer alle), Frankreich (Factur-X-Pflicht Plattform-basiert ab 2026-09-01 fuer grosse + 2027-09-01 fuer alle), Spanien (Verifactu/SII bereits live), Italien (SdI-Plattform bereits live seit 2019). **Cosmi-Kunden mit DE-Sitz und >800k EUR Umsatz haben ab 01.01.2027 (6 Monate) PEPPOL-Versand-Pflicht** — Cosmi unterstuetzt das nicht. **Sprint-Anker**: PEPPOL-Access-Point-Integration via Trusted-Service-Provider (Pagero, Crossinx, B2Brouter) oder Self-Hosted (ph-peppol-server, Mustang-Project), `peppol_messages`-Tabelle als Audit-Log, neue `SendInvoiceViaPeppol`-RPC. **#3 Cosmi-buchhaltung hat keinen Bank-Feed-Layer — der weicheste Punkt im UI-Vergleich gegen sevDesk/Lexoffice/BuchhaltungsButler.** Frontend hat einen `BankConnectDialog.tsx` und einen `TransactionsTab.tsx`, aber Backend hat keinen PSD2/FinTS-Adapter, keinen HBCI-Provider, keine Reconciliation-Engine zwischen Bank-Transaktionen und Open-Items. **Auch hier**: sevDesk, Lexoffice, BuchhaltungsButler, Candis, Pliant haben native Bank-Feeds (figo/finAPI/Bankin/Tink/Klarna-Open-Banking) seit Jahren, mit Auto-Matching von Eingangsbuchungen auf Open-Items. Cosmi-Kunden buchen heute manuell aus CSV-Export oder via DATEV-CSV-Reimport — das ist die **groesste KMU-UX-Luecke des gesamten Cosmi-Stacks** (Cosmi-CRM-Pipeline ist gut, Cosmi-Helpdesk ist gut, Cosmi-Buchhaltung ohne Bank-Feed wirkt wie "Excel-Plus"). **Sprint-Anker**: `backend/internal/biz/bankfeed/` mit figo/finAPI-Adapter (DACH-PSD2-Bevorzugung), `bank_accounts`-Tabelle, `bank_transactions`-Tabelle mit Auto-Matching-Score, `MatchTransactionToInvoice`-RPC, `BankFeedSyncWorker`-Cron.

> **Leit-Signal der Woche fuer buchhaltung: drei parallele Bewegungen formen den Markt seit Januar 2026.** **(a) KI-OCR-Commodity-Welle**: Mistral OCR 4 (Paris, EU-Hosting, Apache-2.0-Open-Weight, **170 Sprachen**, **$4/1000 Seiten**, 72%-Win-Rate gegen Google Document AI in Benchmarks, RAG-ready Semantic-Chunking nach Paragraphen statt Seiten) hat seit W25 (Heise/Mistral-Blog/HN/TechCrunch n_sources:4) das KI-OCR-Tabellenstake fuer EU-DSGVO-DACH-KMU gesetzt. Davor war OCR-fuer-Buchhaltung **DACH-strukturell Google-Document-AI-blocked** (US-Cloud-Vendor-Bedenken). Jetzt: Mistral OCR 4 macht Self-Hosted-DACH-KMU-OCR **technisch und finanziell trivial** — 50-200 Eingangsrechnungen/Monat = 4-16 EUR Cosmi-Tenant-Kosten (oder gar 0 bei Self-Host). **Konsequenz fuer Cosmi**: jeder Konkurrent ohne KI-OCR in 6 Monaten wirkt 2010-veraltet. Cosmi-buchhaltung hat **alle Voraussetzungen** (gobd_documents Archiv, finance_incoming_invoices Status-Lifecycle received→reviewed→booked, pdfcpu PDF-Attachment-Extract, MinIO-Document-Storage), **fehlt nur**: ein `backend/internal/biz/einvoice/ai_extraction/` Pfad zwischen PDF-Upload und ParsedInvoice — Mistral-OCR-4 oder Mistral-OCR-3-Base (Free) als Adapter. **(b) e-Rechnung-Pflicht-Welle**: Deutschland (B2B-Pflicht-Stufenplan 2025-2028), Frankreich (Plattform-basiert mit Y-Modell seit 2026-09-01 fuer grosse), Polen (KSeF seit 2026-02-01), Belgien (B2B-Pflicht ab 2026-01-01), Daenemark (B2B-Pflicht ab 2026-01-01). Plus EU-ViDA-Paket (April 2026) als 2030-Backstop fuer alle EU-Laender. **Konsequenz fuer Cosmi**: ZUGFeRD/XRechnung-Empfang ist erfuellt (das ist gut), **aber PEPPOL-Versand ist offen** — Sprint-Pflicht fuer Q4 2026 spaetestens. **(c) Bank-Feed-Konsolidierung**: figo-Mutter (FinTecSystems) wurde 2024 von Tink uebernommen, Tink wiederum 2022 von Visa gekauft — der DACH-Standard-Bank-Feed-Anbieter ist jetzt **US-Visa-owned**, was fuer Cosmi-EU-Sovereign-Story Frage stellt. Alternativen: **finAPI** (Deutschland, FinTech-Group/SCHUFA-owned), **Bankin/Bridge by Bankin** (Frankreich, oekosystem-EU), **Salt Edge** (Estland/EU-only, FRX). Cosmi-Bank-Feed-Adapter sollte multi-provider, default finAPI/Salt-Edge. **Heute kein neuer buchhaltung-Markt-Schock im Morning-Pulse** (`daily/2026-06-29-morning.md` zeigt buchhaltung als "stilles Modul" — keine Lexoffice/Easybill-Items vor Watermark, Akaunting kein Zugang), **aber zwei indirekte Signals**: PostgreSQL-CVE BSI [hoch] (kritisch fuer Cosmi-Buchhaltungs-DB-Patch-Status, action: noch heute pruefen) + KI-Haftungsgesetz DE in Sicht (relevant fuer kuenftige Cosmi-AI-Buchhaltungs-Funktionen — Disclosure-by-Design-Pflicht). **Dieser Bericht empfiehlt drei Pflicht-Sprint-Stakes fuer das zweite Halbjahr 2026 (Q3+Q4): KI-OCR-Layer auf einkommende Belege, PEPPOL-Access-Point-Anbindung, Bank-Feed-Adapter — alle drei sind heute komplette Backend-Greenfields, alle drei haben in 6-12 Monaten Marktbeobachtungs-Auswirkung.**

---

## State-of-the-Art

Der DACH-Buchhaltungs-Markt Mitte 2026 ist nicht mehr "sevDesk vs Lexoffice vs DATEV" — er ist **vierspurig**: (1) **KI-First-Cloud-Buchhaltung** (Lexware Office mit Lexware NAVI seit Q1 2026, sevDesk mit Beleg-Auto-Kategorisierung + AI-Anomaly-Detection, Candis vom Spesen-Tool zur AP-Automation mit AI-Workflow, Pliant Corporate-Cards mit Auto-Buchung), (2) **PEPPOL-Compliance-Pflicht-Spur** (B2Brouter, Crossinx/Comarch, Pagero/Tradeshift, Basware fuer Enterprise — alle bieten "Access-Point + 4-Corner-Model + UBL/CII-Conversion"), (3) **DACH-KMU-Plus-Buchhaltung** (Lexoffice/sevDesk/BuchhaltungsButler/easybill als 5-15-EUR/Monat-Tier, klassisch ohne AI bis vor 6 Monaten, jetzt unter AI-Modernisierungs-Druck), (4) **Branchen-/Enterprise-Buchhaltung** (DATEV Unternehmen Online fuer Steuerberater-Workflow, Bexio fuer CH-KMU-Komplettloesung mit CRM-Integration, weclapp als ERP-Light-Player, Odoo Accounting als Open-Source-Modular). Cosmi-buchhaltung sitzt heute **architektonisch in Spur (4)** als KMU-Komplettloesung im Cosmi-Modul-System, **mit Spur-2-Lueckeninhalt** (PEPPOL fehlt) und **ohne Spur-1-Layer** (kein KI). Das ist eine **definierte, klare, schliessbare Luecke** — anders als bei vertraege W26, wo gleich 4 strukturelle Diskrepanzen (ContractType-Drift, Multi-Signer, Multi-Document, CRM-Linking) Backend-Catch-Up brauchten.

Drei strukturelle Veraenderungen treiben den Buchhaltungs-Markt seit Januar 2026:

(a) **Lexware NAVI (Q1 2026 GA) hat das KI-Tabellenstake fuer DACH-KMU-Buchhaltung gesetzt — sevDesk + BuchhaltungsButler + Candis ziehen nach.** Lexware NAVI (frueher als "Lexware AI-Assistent" gepitcht, im Januar 2026 als markenname "NAVI" gelauncht): Konversationaler Buchhaltungs-Copilot direkt in Lexware Office, der Belege automatisch zuordnet ("Diese Tank-Rechnung wird auf Konto 4520 Kfz-Betriebsstoffe gebucht"), Fragen beantwortet ("Wie viele Umsatzsteuer habe ich diesen Monat gezahlt?"), Anomalien flaggt ("Diese Rechnung von XY ist 40% hoeher als der 6-Monats-Schnitt"). Hauptnutzungs-Pattern: **Beleg fotografieren mit Smartphone → NAVI extrahiert + kategorisiert + bucht vor → User bestaetigt mit Wisch**. sevDesk hat zur DMEXCO 2025 KI-Belegerfassung mit Vendor-Erkennung + Konto-Vorschlag + Steuersatz-Erkennung gelauncht (heute fuer alle Tarife verfuegbar, frueher Pro-only). BuchhaltungsButler hat im Maerz 2026 AI-Powered-Buchungsvorschlaege fuer Bank-Transaktionen erweitert (Auto-Matching auf Open-Items mit Confidence-Score). Candis (urspruenglich Spesen-Belege/Reisekosten) hat 2026 die volle AP-Automation-Suite gestartet: Eingangsrechnung → AI-OCR → AI-Validierung gegen Bestellung → AI-Workflow-Approval → Auto-Zahlungsfreigabe → Buchungsvorschlag fuer DATEV/Lexware/sevDesk. Pliant Corporate-Cards machen Auto-Buchung jede Kartentransaktion direkt in die Buchhaltung. **Konsequenz fuer Cosmi-buchhaltung**: das 6-EUR/User/Monat-Pricing (gegen sevDesk ab 10, Lexoffice ab 7) ist heute attraktiv **fuer den feature-paritaeten Vergleich von 2024**. **Aber**: die Konkurrenz hat seit 6 Monaten die KI-Layer addiert, ohne dafuer den Preis anzuheben (Lexware NAVI ist im Standard-Plan enthalten, sevDesk hat Auto-Beleg-Kategorisierung von Pro auf alle Plaene runtergeschoben). Cosmi-Kunden, die 2026 evaluieren, sehen 6 EUR/User-Monat fuer "Buchhaltung ohne KI" gegen 7 EUR/Monat fuer "Lexoffice mit NAVI" — die Pricing-Differenz schmilzt, das KI-Feature-Differential waechst. **Pflicht-Antwort**: KI-OCR-Layer als Sprint-Anker im naechsten Modul-Zyklus.

(b) **PEPPOL ist nicht mehr "irgendwann EU-Pflicht 2030", sondern "DE-Pflicht-Stufenplan 2027/2028 + 5 weitere EU-Pflicht-Programme bereits live".** Stand 2026-06-29: **Deutschland**: B2B-XRechnung-Empfangs-Pflicht seit 2025-01-01 (alle Unternehmen muessen XRechnung empfangen koennen), **Sende-Pflicht ab 2027-01-01 fuer Unternehmen >800k EUR Umsatz**, **Sende-Pflicht ab 2028-01-01 fuer alle Unternehmen**. Mindestformate: XRechnung-UBL oder ZUGFeRD-CII (PDF/A-3 + EN 16931-konformes XML). PEPPOL-Versand ist heute optional, wird in ViDA-Phase 2 (2030+) verpflichtend. **Frankreich**: Plattform-basiertes Y-Modell (PPF = Plateforme Publique de Facturation, ergaenzt durch private PDP = Plateformes de Dematerialisation Partenaires). Stufenplan 2026-09-01 fuer >5000-Mitarbeiter-Unternehmen, **2027-09-01 fuer alle Unternehmen** (B2B-Empfangs- und Sende-Pflicht zugleich). Format: Factur-X oder UBL via PEPPOL-PDP. **Polen**: KSeF (Krajowy System e-Faktur) seit 2026-02-01 verpflichtend fuer alle Unternehmen >200 Mio PLN Umsatz, ab 2026-04-01 fuer alle. Format: FA(2)-XML via API. **Belgien**: B2B-PEPPOL-Pflicht seit 2026-01-01 fuer alle BTW-pflichtigen Unternehmen. **Daenemark**: NemHandel-Plattform (PEPPOL-Access-Point) B2B-Pflicht seit 2026-01-01. **Spanien**: Verifactu + SII (Suministro Inmediato de Informacion) live seit 2026, mit FACE-Plattform fuer B2G. **EU-ViDA-Paket (April 2026 verabschiedet)**: digitale Meldepflicht fuer grenzueberschreitende B2B-Transaktionen ab 2030, basierend auf PEPPOL BIS Billing 3.0 als technisches Format, einheitlicher EU-Standard fuer e-Invoicing-Meldung an Steuerbehoerden. **Konsequenz fuer Cosmi**: alle Cosmi-DACH-Kunden mit grenzueberschreitendem B2B (DE-FR, DE-PL, DE-BE, CH-DE, AT-DE) brauchen ab 2027 PEPPOL-Versand. Cosmi-Kunden mit DE-Sitz und >800k EUR Umsatz brauchen ab 01.01.2027 die DE-B2B-Sende-Pflicht. **Cosmi-Sprint-Anker**: PEPPOL-Access-Point-Integration ist Q4-2026-Pflicht-Stake. Drei Wege: (i) **PEPPOL-as-a-Service** ueber TSP wie Pagero/Crossinx/B2Brouter/Tradeshift/Basware — schneller Time-to-Market (4-6 Wochen Integration), laufende Per-Document-Kosten (0.10-0.50 EUR pro PEPPOL-Versand), keine eigene PKI-Wartung. (ii) **Self-Hosted PEPPOL-Access-Point** via Open-Source-Tools (ph-peppol-server, Mustang-Project, OpenPEPPOL-AP) — hoeher Aufwand (3-4 PT Integration + PKI-Pflege), keine Per-Document-Kosten, volle EU-Sovereign-Kontrolle. (iii) **Hybrid**: Self-Hosted-AP fuer DACH, TSP fuer exotische Laender. Empfehlung fuer Cosmi: **Self-Hosted-AP fuer DACH-Volumen + Pagero-/B2Brouter-Fallback fuer Long-Tail** — passt zur Cosmi-EU-Sovereign-Story und vermeidet Pro-Document-Skalierungs-Kosten.

(c) **EU-AI-Act Article 50 (02.08.2026, exakt 5 Wochen weg) + EU-Data-Act + DSGVO-Buchhaltungs-Form-Anker treffen jetzt zusammen.** **EU-AI-Act Article 50 trifft am 2. August 2026**: jede KI-Funktion in Buchhaltungs-Software (AI-OCR-Beleg-Extraction, AI-Kontierungs-Vorschlag, AI-Dunning-Brief-Personalisierung, AI-Anomaly-Flag, AI-Cashflow-Forecast, AI-Buchungs-Co-Pilot) faellt unter Transparenz-Pflicht — User muss informiert werden, dass AI im Spiel ist, Disclosure-Pattern wie "Buchungsvorschlag von AI generiert" oder "Powered by AI", Bussgeld bis 15 Mio EUR oder 3% Welt-Umsatz. Plus: AI-Output bei Hoch-Risiko-Anwendungen (Buchhaltung faellt darunter, da finanzielle Konsequenzen) braucht Audit-Log-Pflicht + Human-Review-Option. **EU-AI-Omnibus** (Provisional-Agreement 16.06.2026, Rats-Annahme erwartet Juli 2026, OJ-Publikation **vermutlich vor 02.08.2026**) verschiebt Hochrisiko-AI-Standalone von 02.08.2026 auf **02.12.2027** und Annex-I-AI von 02.08.2026 auf **02.08.2028**. Aber: GPAI + verbotene Praktiken bleiben unveraendert, Transparenz-Pflicht (Article 50) bleibt unveraendert. **EU-Data-Act greift seit 12. September 2025 fuer alle NEUEN B2B-Daten-Sharing-Vertraege** mit FRAND-Pflicht — relevant fuer Cosmi-Buchhaltungs-Daten-Sharing mit Bexio/Lexware/DATEV-Schnittstellen. **DSGVO-Buchhaltungs-Form-Anker**: BGH 11.03.2026 I ZR 202/25 bestaetigt Textform durch Email-Austausch (relevant fuer Dunning-Brief-Email-Versand). **Konsequenz fuer Cosmi-buchhaltung**: jede AI-Funktion ab heute MUSS mit Disclosure-Schicht ausgeliefert werden. Cosmi hat **strukturellen Vorteil**, weil noch keine AI-Funktion existiert: **Disclosure-by-Design** kann jetzt eingebaut werden, bevor die erste AI-Phase live geht. Konkurrenten (Lexware NAVI, sevDesk-Belege-AI, Candis) muessen rueckwirkend ihre Q1/Q2-2026-AI-Releases auditieren — Lexware NAVI-FAQ verweist auf "Lexware-AI-Datenschutz-Hinweise", aber das Pattern ist nicht konsequent ausgerollt. Cosmi kann hier **Q3-2026-Compliance-Marker** setzen: erste KI-OCR-Funktion mit klarem Disclosure-Badge + Audit-Log + Human-Review-Pflichtschritt im Workflow.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Lexware Office (DACH, threat: HIGH als DACH-KMU-Markt-#1 + NAVI-AI-Vorbild)**

Lexware Office (frueher Lexoffice) ist **das DACH-KMU-Buchhaltungs-Refernezmodell** — Lexware-Mutter Haufe-Group, deutscher Sitz, deutsche Datenhaltung, **Lexware NAVI-AI-Assistent seit Q1 2026 live**. Hauptkunde: 1-30-Mitarbeiter-DACH-KMU. Direkter Cosmi-Konkurrent im Preis-Segment.

- **Lexware NAVI (Q1 2026 GA, Lexware-Markenname fuer den KI-Layer)**: Konversationaler Co-Pilot im Lexware-Office-UI ("Wie viele Umsatzsteuer habe ich diesen Monat?"), Beleg-Auto-Kategorisierung mit Konto-Vorschlag, Anomaly-Flag auf Eingangsrechnungen (Abweichungen vs. 6-Monats-Schnitt), Auto-Buchungsvorschlag fuer Bank-Transaktionen mit Confidence-Score, AI-Dunning-Brief-Generierung mit Personalisierungs-Optionen.
- **e-Rechnung**: vollstaendige XRechnung-UBL + ZUGFeRD-CII Import und Export, native Anbindung an deutsche Behoerden via OZG-Schnittstelle, ZUGFeRD-3.0-Versand. **PEPPOL-Access-Point ist GEPLANT fuer Q4-2026** (Roadmap-Ankuendigung im Lexware-Blog Mai 2026, "wir bauen unseren eigenen PEPPOL-AP fuer alle Office-Kunden").
- **Bank-Feed**: native Anbindung an alle DACH-Banken via Lexware-eigene HBCI-Schnittstelle und PSD2/FinTS-Provider (finAPI als Primary), Auto-Matching von Bank-Transaktionen auf Open-Items, Multi-Konto-Support, Cashflow-Forecast.
- **DATEV-Schnittstelle**: bidirektional (Push und Pull), Realtime-Sync mit DATEV Unternehmen Online, Berater-Workflow-Integration.
- **G2/Capterra-Pain-Points 2026**: "Onboarding-UX gut, aber bei komplexen Faellen (Multi-Tenant, Multi-Currency) wird's umstaendlich", "Reporting-Layer schwach gegen DATEV", "Mobile-App-Belegerfassung ok, aber AI-Kategorisierung manchmal falsch", "Preis-Erhoehung 2026 unangenehm — Plus von 9.90 auf 12.90 EUR", "Bei Steuerberater-Wechsel teilweise Datenmigrations-Frust".
- **Pricing (2026)**: Buchhaltung Basis **7.90 EUR/Monat netto**, Buchhaltung Plus **12.90 EUR/Monat netto** (mit Lexware NAVI), Buchhaltung XL **24.90 EUR/Monat netto** (mit Multi-Konto + erweiterten Reports), Jahres-Discounts ueblich.
- **Tech-Stack**: Cloud-only, DE-Hosting, kein Self-Host, klassisches SaaS-Modell.
- **Gap zu Cosmi**: Lexware NAVI (KI-Co-Pilot mit allen Funktionen), native Bank-Feed-Anbindung, bidirektionaler DATEV-Sync (nicht nur Export), Realtime-PEPPOL-Roadmap, Mobile-App mit AI-Belegerfassung, deutsche Steuerberater-Workflow-Integration.
- **Strategischer Hinweis (WICHTIGSTER AI-PUNKT DIESES REPORTS)**: **Cosmi gewinnt nicht ueber "KI besser als NAVI"** — Lexware hat 6+ Monate NAVI-Vorsprung und tausende Trainings-Buchungen pro DACH-KMU-Branche. **Cosmi gewinnt ueber "Buchhaltung-in-CRM-in-Verträge-in-Helpdesk-in-Rapporte im Cosmi-Modul-Preis"**: eine Rapport-Stunde wird automatisch zur Invoice-Line, ein Vertrag triggert Recurring-Invoice, ein CRM-Deal-Won wird automatisch zum Quote→Invoice-Workflow, ein Helpdesk-Ticket mit "Rechnung falsch" zieht direkt die Invoice im Backend ueber Cross-Modul-Link. **Das ist Cosmi-USP, Lexware NAVI kann das strukturell nicht** (kein eigenes CRM, kein eigenes Helpdesk, kein eigenes Verträge-Modul, kein eigenes Rapporte-Tool). **Aber:** KI-OCR + KI-Kontierungs-Vorschlag + KI-Anomaly-Flag MUSS ab Q1 2027 verfuegbar sein — sonst greift der "Cosmi-fuehlt-sich-nicht-modern-an"-Effekt, wie schon bei Helpdesk W24 (AI-Drafts als Stake), Formulare W25 (AI-Form-Generation als Stake), Vertraege W26 (AI-Klausel-Extraction als Stake) als Pattern erkannt. Die KI-Pflicht ist hier konkreter als bei vertraege, weil sie nicht "Roadmap-Anspruch" sondern "Tabellenstake-seit-6-Monaten" ist.

**2. sevDesk (DACH, threat: HIGH als DACH-KMU-#2 + Premium-AP-Player)**

sevDesk ist Lexware's groesster DACH-Konkurrent — deutsche Firma (Offenburg), deutsche Datenhaltung, ca. 90.000+ KMU-Kunden 2026, **Beleg-Auto-Kategorisierung mit KI im Standard-Plan seit DMEXCO 2025**. Direkter Cosmi-Konkurrent.

- **KI-Belegerfassung (seit 2025)**: Foto/PDF von Beleg hochladen → KI extrahiert Lieferant + Datum + Betrag + Steuersatz + Konto-Vorschlag, User bestaetigt mit einem Klick. Aktive Lern-Schleife: Korrekturen werden Tenant-spezifisch persistiert.
- **e-Rechnung**: vollstaendige XRechnung + ZUGFeRD Import/Export, PEPPOL-Access-Point via Partner-TSP (Crossinx-Integration), DE-OZG-Schnittstelle.
- **Bank-Feed**: native PSD2/HBCI-Anbindung an alle DACH-Banken, Auto-Matching mit Confidence-Score, Multi-Konto, Cashflow-Forecast (Premium-Plan).
- **DATEV-Schnittstelle**: bidirektional, Realtime-Sync, Steuerberater-Portal "sevDesk Berater".
- **G2/Capterra-Pain-Points 2026**: "Pricing erhoeht sich 2026 nochmal — fuer kleine Selbststaendige zu teuer geworden", "Mobile-App-Buchhaltung gut, Desktop-UI altert", "Berichts-Layer eingeschraenkt gegen DATEV", "Kundenservice-Antwortzeiten variabel", "AI-Belegerfassung ok, aber bei mehrseitigen Rechnungen Quote-Fehler", "Schnittstellen zu fremden Tools (Shopware/WooCommerce/Magento) teils brueechig".
- **Pricing (2026)**: Rechnung Basis **9.90 EUR/Monat netto**, Rechnung Plus **15.90 EUR/Monat netto**, Buchhaltung Plus **29.90 EUR/Monat netto** (mit DATEV-Schnittstelle), Buchhaltung Pro **49.90 EUR/Monat netto** (mit Mehrbenutzern, erweiterten Reports, voller AI).
- **Tech-Stack**: Cloud-only, DE-Hosting, kein Self-Host.
- **Gap zu Cosmi**: KI-Belegerfassung mit aktiver Lern-Schleife, native Bank-Feed-Anbindung mit Auto-Matching, bidirektionaler DATEV-Sync, PEPPOL-Access-Point via TSP, Mobile-App mit Belegfoto-Workflow, Shop-System-Integration (Shopware/WooCommerce).
- **Strategischer Hinweis**: **sevDesk-Plus-Plan 29.90 EUR/Monat fuer DATEV-Anbindung ist das Cosmi-Preis-Vergleichs-Anker fuer Sales**. Cosmi-Buchhaltung mit Cosmi-CRM + Cosmi-Vertraege + Cosmi-Rapporte bei 6+5+5+3 = 19 EUR/User/Monat ist **billiger und cross-funktional weiter**, **wenn die KI-Luecke geschlossen ist**. Sprint-Anker: KI-Belegerfassung als Phase-1-AI-Sprint (nach Mistral-OCR-4-Adapter), Bank-Feed-Adapter als Phase-2-Sprint.

**3. DATEV Unternehmen Online (DACH, threat: MEDIUM als Steuerberater-Standard, low als KMU-Direkt-Konkurrent)**

DATEV ist **kein direkter Cosmi-Konkurrent** im KMU-Segment — DATEV verkauft an Steuerberater, die wiederum an KMU verkaufen. Aber DATEV-Schnittstelle ist **Cosmi-Pflicht-Stake** (jeder DACH-KMU-Steuerberater nutzt DATEV). DATEV Unternehmen Online (DUO) ist das KMU-Frontend fuer DATEV-Buchhaltungsdaten — Belegerfassung, Bank-Anbindung, Berater-Kommunikation.

- **DUO-Belegerfassung 2026**: KI-OCR fuer Eingangsrechnungen (DATEV-eigene OCR-Engine, kein Mistral/Google-OCR), DMS-Integration, Mandanten-spezifische Kontoplan-Vorschlaege, Buchungsstapel-Export an Steuerberater.
- **DATEV Smart Transfer / Smart Login**: PEPPOL-Access-Point seit 2025-Q4 ("DATEV als PEPPOL-AP" — alle Kunden koennen XRechnung via PEPPOL versenden und empfangen, ohne eigenen AP).
- **DATEV-Connect-Online (DCO) API**: REST-API fuer Dritt-Software-Anbindung, OAuth 2.0, eingeschraenkte Schreib-Zugriffe (vor allem Lese-Zugriff auf Buchungsdaten). Cosmi-DATEV-Schnittstelle nutzt heute den **EXTF-CSV-Export** (Migration 056 + 219), nicht die DCO-API.
- **Pain-Points 2026** (aus Steuerberater-Feedback, da DATEV nicht im KMU-G2): "API-Erweiterungen langsam, Schreib-Zugriffe limitiert", "Pricing fuer Berater hoch, KMU bekommt nur was Berater freigibt", "UX-Modernisierung schleppend (DATEV bekannt fuer schwerfaellige UI)".
- **Pricing**: DATEV Unternehmen Online wird **vom Steuerberater bezahlt** und an den KMU-Kunden weitergegeben (typisch 10-30 EUR/Monat im Berater-Vertrag).
- **Tech-Stack**: DATEV-Cloud, Nuernberg, EU-Hosting, deutsche Steuerberater-Compliance-Master.
- **Gap zu Cosmi**: PEPPOL-Access-Point seit Q4 2025 (Cosmi 0), bidirektionale DCO-API-Anbindung (Cosmi nur CSV-Export), DATEV-eigene OCR im DUO-Frontend (Cosmi 0 OCR), Buchungsstapel-Realtime-Sync (Cosmi Snapshot-Export).
- **Strategischer Hinweis (KRITISCH FUER COSMI-DATEV-SCHNITTSTELLE)**: **Cosmi-DATEV-Export-CSV ist das absolute Minimum** — DCO-API-Integration ist Mittelfrist-Ziel (Q1 2027), aber CSV-Export erfuellt 80% der Steuerberater-Use-Cases. **Aber**: Cosmi sollte **DATEV-PEPPOL-AP als optionalen PEPPOL-Channel** evaluieren — wenn Cosmi-Tenant bereits DATEV-Steuerberater hat, koennte das XRechnung-Sende-Volumen ueber den DATEV-AP laufen statt ueber einen eigenen Cosmi-PEPPOL-AP. Das vermeidet Dual-AP-Kosten und nutzt bestehende Steuerberater-Beziehung. **Sprint-Anker**: `peppol_provider`-Konfigurations-Feld pro Tenant mit Optionen `cosmi-self-hosted` | `datev-via-berater` | `pagero-tsp` | `b2brouter-tsp`.

**4. BuchhaltungsButler (DACH, threat: MEDIUM als KMU-Mittelfeld + Bank-Feed-Spezialist)**

BuchhaltungsButler ist DACH-KMU-Buchhaltungs-Spezialist mit **Schwerpunkt Bank-Feed-Automation** — deutsche Firma (Berlin), deutsche Datenhaltung, ca. 30.000+ Kunden, AI-Powered-Buchungsvorschlaege fuer Bank-Transaktionen seit Maerz 2026 erweitert.

- **Bank-Feed-Auto-Matching (Maerz-2026-Update)**: AI-Vorschlaege fuer Konto-Zuweisung pro Bank-Transaktion mit Confidence-Score, Lern-Schleife pro Tenant, automatische Belegzuordnung (Bank-Transaktion → Open-Item-Match).
- **e-Rechnung**: vollstaendige XRechnung + ZUGFeRD Import/Export, PEPPOL-AP via Partner (Crossinx).
- **Belegerfassung**: KI-OCR fuer Beleg-Foto/PDF (vergleichbar mit sevDesk-Niveau), Vendor-Erkennung, Konto-Vorschlag.
- **DATEV-Schnittstelle**: bidirektional, Realtime-Sync.
- **Pain-Points 2026**: "Pricing teurer geworden — fuer Kleinunternehmer 14.90 EUR/Monat hoch", "AI-Buchungsvorschlaege gut bei Standardlieferanten, schwach bei Erstmaligen", "Mobile-App schwach gegen sevDesk/Lexware".
- **Pricing (2026)**: Solo **14.90 EUR/Monat netto**, Smart **24.90 EUR/Monat netto**, Pro **39.90 EUR/Monat netto** (mit DATEV + erweitertem AI-Layer).
- **Tech-Stack**: Cloud-only, DE-Hosting.
- **Gap zu Cosmi**: Bank-Feed-Auto-Matching mit AI-Confidence-Score, AI-OCR-Belegerfassung, bidirektionale DATEV-Synchronisation, PEPPOL-AP via TSP.
- **Strategischer Hinweis**: **BuchhaltungsButler ist Bank-Feed-UX-Vorbild fuer Cosmi**. Cosmi-Sprint-Anker: nach KI-OCR (Phase 1) als Phase 2 ein **Bank-Feed-Adapter mit Auto-Matching-Engine** — finAPI/Salt-Edge fuer PSD2, `bank_transactions`-Tabelle, `MatchTransactionToInvoice`-RPC mit ML-Score, `MatchSuggestionConfirmAtomic` fuer User-Bestaetigung.

**5. Bexio (CH-DACH, threat: HIGH als CH-Markt-Komplettloesung + Cosmi-Existing-Integration)**

Bexio ist **CH-KMU-Komplettloesung** — Schweizer Firma (Zuerich, Swisscom-Tochter), Schweizer Datenhaltung, ca. 65.000+ KMU-Kunden, **Cosmi hat bereits OAuth-Integration** (`backend/internal/biz/bexio/`, **35 Files, 3607 LOC**, Haertungs-Sweep 2026-06-17 mit G1-G5+G10 von 12 Scope-Check-Blockern geschlossen, vgl. `.planning/bexio-scope-check.md`). Bexio ist Cosmi-Konkurrent fuer CH-Markt, **aber gleichzeitig Cosmi-Integrations-Partner** (Bexio-User koennen Cosmi-CRM/Helpdesk-Module ergaenzen, Bexio bleibt Buchhaltung).

- **Komplett-Suite (CH-Standard)**: CRM + Auftragsabwicklung + Buchhaltung + Bank-Anbindung + Lohnbuchhaltung + Projekt-/Zeit-Erfassung in einem CH-konformen System. CH-MWST-Saetze (7.7% + 2.5% + 3.7%), CH-QR-Rechnung-Standard, **CH-PEPPOL-Anbindung via Bexio-PEPPOL-AP seit Q2 2025**.
- **AI-Features 2026**: Bexio AI Assistent (seit Q1 2026, vergleichbar mit Lexware NAVI) — KI-Belegerfassung, AI-Buchungsvorschlaege, AI-Anomaly-Flag, AI-Dunning-Brief-Personalisierung.
- **Bank-Feed**: CH-Banken-Native (UBS, Credit Suisse jetzt UBS, Raiffeisen, Postfinance, ZKB), DE-Banken via finAPI, ISO-20022-XML-Native (CH-Banking-Standard).
- **CH-spezifisch**: ESR/QR-Rechnung-Generator (gesetzlicher CH-Standard fuer Rechnungen seit 2022-09-30), CH-MWST-Abrechnung mit Effektiv/Saldo/Pauschale-Methoden, ELM-Lohnmeldung-Format fuer SVA/AHV.
- **Pain-Points 2026**: "CH-Funktionen perfekt, aber AT/DE-Funktionen eingeschraenkt — fuer DACH-Cross-Border-KMU nicht erste Wahl", "Pricing teurer fuer Mehrbenutzer", "Reporting-Layer gegen DATEV-Berater eingeschraenkt".
- **Pricing (2026)**: Easy **39 CHF/Monat netto**, Pro **89 CHF/Monat netto**, Premium **159 CHF/Monat netto** (mit Multi-User + AI + Lohnbuchhaltung).
- **Tech-Stack**: Swisscom-Cloud, CH-Hosting, ISO-27001 + FINMA-konform.
- **Gap zu Cosmi**: AI-Belegerfassung, CH-PEPPOL-AP, ESR/QR-Rechnung-Generator (Cosmi muss das ergaenzen fuer CH-Kunden), ISO-20022-XML-Native-Bank-Feed, CH-MWST-Saetze + CH-Lohnbuchhaltung-Format.
- **Strategischer Hinweis (CRITICAL FUER CH-MARKT-STRATEGIE)**: **Cosmi-Bexio-Integration ist strategischer Partner, nicht Konkurrent — fuer CH-Markt**. Cosmi-Strategie sollte sein: (i) **CH-Kunden mit Bexio-Bestand**: Cosmi-Module (CRM/Helpdesk/Vertraege/Wiki) ergaenzen Bexio-Buchhaltung via OAuth-Integration — Sprint-Pflicht G2-G12 abschliessen, (ii) **CH-Kunden ohne Buchhaltungs-Vorgaben**: Cosmi-Buchhaltung mit **CH-Specifika ergaenzen** — ESR/QR-Rechnung-Generator + CH-MWST-Saetze + ISO-20022-Bank-Feed, dann Cosmi-Komplett-Loesung anbieten. Cosmi-Sprint-Anker: `backend/internal/biz/ch_specifics/` Pfad — ESR-Code-Generator (ISO 11649 + Banking-Common-Standard), QR-Code-Generator (SwissQR-Spec), CH-MWST-Modul.

**6. Odoo Accounting (international, threat: MEDIUM als Open-Source-Modular-Vorbild)**

Odoo ist **architektonisches Cosmi-Vorbild** — modulares Open-Source-ERP mit eigenem Accounting-Modul, internationaler Anbieter (Belgien). Direkter Open-Source-Vergleich mit Cosmi-Module-System. Threat-Level medium, weil Odoo enterprise-orientiert ist (Implementation-Partner-Modell), nicht DACH-KMU-Direkt-Sales.

- **Modulares Accounting**: Multi-Currency-Native (170+ Waehrungen), Multi-Tax-Regime, Localization-Module pro EU-Land (DE-XRechnung-Module, FR-Factur-X-Module, CH-QR-Rechnung-Module, alle als separate Add-ons), Bank-Feed-Anbindung via Plaid/Yodlee/Open-Banking, AI-Belegerfassung (Odoo-Studio-AI seit Odoo 17 2024).
- **PEPPOL**: vollstaendige PEPPOL-AP-Integration seit Odoo 17 (Mitte 2024), unterstuetzt alle EU-Mandate-Formate (XRechnung, Factur-X, FatturaPA, KSeF, NemHandel, etc.).
- **DATEV-Schnittstelle**: ueber Drittanbieter-Module (Open-Source Community-Modul `l10n_de_skr03`/`l10n_de_skr04`), nicht offiziell Odoo-supported.
- **Pricing**: Odoo Community **kostenfrei** (Self-Host), Odoo Enterprise ab **24.90 USD/User/Monat** (Cloud), aber Implementation-Kosten 5k-50k EUR ueblich.
- **Tech-Stack**: Python/PostgreSQL, Self-Hosted oder Odoo-Cloud, modular via Add-ons.
- **Gap zu Cosmi**: PEPPOL-AP-Native, AI-Belegerfassung (Odoo-Studio-AI), Multi-Currency-Multi-Tax-Native, Bank-Feed via Plaid/Yodlee, Localization-Module-Marketplace.
- **Strategischer Hinweis**: **Odoo ist architektonisches Vorbild fuer Cosmi-Multi-Modul-Pricing-System** — Odoo-Buchhaltungs-Modul ist im Komplett-Package, nicht standalone. Cosmi's Modul-x-User-Pricing-System (vgl. `KMU-Hub/.knowledge/pricing.md`) ist konzeptionell aehnlich, aber **klarer pro KMU positioniert** (Odoo-Implementation-Kosten sind KMU-prohibitiv). Cosmi-Differential: **6 EUR/User/Monat Buchhaltung im Modul-System ohne Implementation-Partner-Pflicht** gegen Odoo's enterprise-orientiertes Modell. Sprint-Anker: PEPPOL-AP-Native als Cosmi-USP-Differential gegen Lexware/sevDesk (die nutzen Partner-TSP).

**7. weclapp (DACH, threat: MEDIUM als ERP-Light + CRM+Accounting-Bundle)**

weclapp ist DACH-ERP-Light-Player — deutsche Firma (Marburg), CRM + Auftrag + Warenwirtschaft + Buchhaltung in einem System, ca. 4.000+ KMU-Kunden, fokussiert auf 20-200-Mitarbeiter-Mittelstand.

- **Komplett-Suite**: CRM + Lager + Einkauf + Verkauf + Buchhaltung + Projekt-/Zeit-Erfassung — direkter Cosmi-Modul-System-Konkurrent fuer Mid-Market (Cosmi ist 2-50, weclapp ist 20-200, **Overlap-Zone 20-50 Mitarbeitende**).
- **e-Rechnung**: XRechnung + ZUGFeRD Import/Export, PEPPOL-AP via Crossinx-Partner.
- **DATEV-Schnittstelle**: bidirektional, Realtime-Sync.
- **AI-Features 2026**: weclapp-AI-Assistent (Q2-2026-Launch) — Buchhaltungs-Co-Pilot, Anomaly-Flag, Cashflow-Forecast (im Premium-Plan).
- **Bank-Feed**: PSD2/HBCI-Anbindung, Multi-Konto, Auto-Matching.
- **Pricing (2026)**: Standard ab **39 EUR/User/Monat** (alles inkl.), Professional ab **59 EUR/User/Monat**, Enterprise ab **89 EUR/User/Monat**.
- **Gap zu Cosmi**: ERP-Light-Komplett-Suite (Cosmi Module-System), AI-Assistent (Cosmi 0), Premium-Cashflow-Forecast, Mid-Market-Lager-Funktionen.
- **Strategischer Hinweis**: **weclapp's 39 EUR/User-Monat ist deutlich teurer als Cosmi's Modul-System** (Cosmi-Buchhaltung 6 + CRM 6 + Einkauf 5 + Inventar 5 + Aufgaben 3 + Kalender 2 = 27 EUR/User/Monat fuer aequivalentes ERP-Light-Bundle). Cosmi-Differential ist **Pricing + Modularitaet** (weclapp ist Komplett-Bundle, Cosmi ist Pick-and-Choose). **Aber**: weclapp hat AI-Assistent + Bank-Feed + bidirektionalen DATEV-Sync — Cosmi muss diese Luecken schliessen, um den Pricing-Vorteil verteidigen zu koennen.

**8. Candis (international/DACH, threat: MEDIUM als AP-Automation-Spezialist + AI-Workflow-Vorbild)**

Candis ist **DACH-AP-Automation-Spezialist** — frueher Spesen-/Reisekosten-Tool, 2026 zur vollen AP-Automation-Suite ausgebaut, ca. 5.000+ KMU/Mittelstand-Kunden. Direkter Cosmi-Konkurrent fuer Eingangsrechnungs-Workflow.

- **AP-Automation-Workflow 2026**: Eingangsrechnung (E-Mail/PDF/XRechnung) → AI-OCR-Extraction → AI-Validierung gegen Bestellung (Order-Matching) → AI-Workflow-Approval (Multi-Stage mit Rollen-Definition) → Auto-Zahlungsfreigabe → Buchungsvorschlag fuer DATEV/Lexware/sevDesk.
- **AI-Anomaly-Detection**: Erkennt Doubletten, Abweichungen vom Bestell-Wert, ungewoehnliche Lieferanten-Patterns.
- **Integrations**: native DATEV-Anbindung, Lexware, sevDesk, BuchhaltungsButler, Microsoft 365, Slack (fuer Workflow-Approvals).
- **Pricing (2026)**: ab **199 EUR/Monat** (10 Belege/Monat), eskaliert je nach Beleg-Volumen, Enterprise on request.
- **Gap zu Cosmi**: AI-OCR mit Order-Matching, Multi-Stage-Workflow-Approval, AI-Anomaly-Detection, native DATEV-Anbindung als Workflow-Endpoint.
- **Strategischer Hinweis**: **Candis 199 EUR/Monat ist deutlich teurer als Cosmi-Buchhaltung 6 EUR/User-Monat**, weil Candis Premium-AP-Automation positioniert ist. **Cosmi sollte AP-Automation als Cosmi-Buchhaltung-Plus-Feature positionieren**, nicht als separates Modul — Workflow-Approval-Schicht im bestehenden `finance_incoming_invoices`-Lifecycle (received → reviewed → **approved** → booked → paid) als neue Status-Stages. Sprint-Anker: `IncomingInvoiceApprovalWorkflow`-RPC + `approval_stages`-JSONB-Konfiguration pro Tenant.

**9. Pliant (international/DACH, threat: low als Corporate-Card-Player + Auto-Buchung)**

Pliant ist **DACH-Corporate-Card-Spezialist mit Auto-Buchungs-Layer** — Berliner Firma, Corporate-Cards mit eingebautem Spend-Management + Buchhaltungs-Sync, ca. 3.000+ KMU/Mittelstand-Kunden. Threat-Level low, weil Pliant Spend-Management-only ist (kein Komplett-Buchhaltungs-Konkurrent), aber relevant als **Corporate-Card-Integration-Vorbild**.

- **Auto-Buchung jede Kartentransaktion**: Jede Pliant-Karten-Transaktion wird automatisch in die Buchhaltung uebertragen (Lexware/sevDesk/DATEV als Targets) mit Konto-Vorschlag + Beleg-Foto-Anhang via Mobile-App.
- **Beleg-Erinnerung**: Wenn 24h nach Transaktion kein Beleg hochgeladen, automatische Push-Notification.
- **Gap zu Cosmi**: Corporate-Cards mit Auto-Buchungs-Integration, native Spend-Management-Workflow, Mobile-App-Beleg-Workflow.
- **Strategischer Hinweis**: **Cosmi sollte Pliant als Integration-Partner-Kandidat evaluieren** (statt Eigenbau Corporate-Cards) — Pliant-API-Integration in Cosmi-Buchhaltung wuerde Cosmi-KMU-Kunden Auto-Buchung ihrer Kartentransaktionen ohne Eigenbau geben. Long-Term-Sprint-Item (Q1 2027+).

**10. Akaunting (Open-Source, threat: low als Self-Host-Vorbild)**

Akaunting ist Open-Source-Buchhaltungs-Player — PHP-Stack, Self-Hosted-First, ca. 1.000+ aktive Self-Host-Installationen DACH-weit (geschaetzt). Threat-Level low, weil Akaunting feature-arm gegen DACH-KMU-Bedarfe (kein DATEV, kein PEPPOL-DACH, kein deutsches MWST), aber relevant als **Open-Source-Self-Host-Vergleichsanker** fuer Cosmi-Orbit-Self-Host-Positionierung.

- **Open-Source-Basis**: Free-Plan mit allen Basis-Funktionen, Premium-Apps fuer DATEV (Drittanbieter-Module, ca. 50-100 EUR/Jahr), PEPPOL-Add-on (Community-Modul, kostenfrei aber wartungsschwach), Multi-Currency-Native.
- **GitHub Releases**: aktive Maintenance, ca. 2-3 Releases/Monat, **letztes Release im akaunting.atom-Feed laut sources/buchhaltung.yaml**.
- **Pricing (2026)**: Self-Host **kostenfrei**, Cloud ab **9 USD/Monat**, Premium-Apps add-on.
- **Strategischer Hinweis**: **Akaunting ist Cosmi-Orbit-Positionierungs-Anker** (Cosmi-Orbit = Self-Hosted-Variante, vgl. `KMU-Hub/.knowledge/pricing.md` "COSMI (SaaS) + ORBIT (Self-Hosted)"). Akaunting-Lessons: (i) Open-Source-Modulares-Add-on-System ist KMU-attraktiv aber Wartungs-Belastung, (ii) DATEV-Add-ons via Community sind brueechig (Cosmi sollte First-Party-DATEV-Modul liefern), (iii) PEPPOL-Add-ons brauchen aktive Maintenance.

---

## Cosmi-IST-Stand

**buchhaltung ist Cosmi's reifestes Modul** — sowohl im Backend (`backend/internal/biz/` mit 11 Sub-Paketen und ~32k LOC) als auch im Frontend (`modules/finanzen/` mit 11.4k LOC ueber 30+ Files) als auch in der Integration (Bexio + Lexware + DATEV). Die folgende IST-Tabelle dokumentiert den genauen Stand 2026-06-29.

### Backend-Sub-Pakete (`backend/internal/biz/`)

| Sub-Paket | Files | Prod LOC | Test LOC | Service-Methoden | Key-Capability |
|---|---|---|---|---|---|
| `invoice` | 10 | 1944 | 2160 | 14 | Outgoing-Invoice mit Create/Send/MarkPaid/Cancel/Storno/Recurring + DATEV-Export-List + TimeTracking-Link + Overdue-Detection + Quote→Invoice + EventEmitter |
| `creditnote` | 7 | 958 | 1100 | 7 | Storno-Rechnung (Gutschrift) mit Send-Atomic-TX, eigene Nummer-Sequenz |
| `dunning` | 6 | 928 | 1062 | 7 | **Auto-Mahnungs-Engine** mit `DetectAndCreateDunnings`, `CalculateInterest`-Verzugszinsen, GoBD-konformer `service_gobd.go`, 3 Status (draft/sent/paid) |
| `einvoice` | 10 | 1194 | 637 | 4 | **E-Rechnung Eingang** ZUGFeRD/Factur-X-CII + XRechnung-UBL Parser + PDF-Attachment-Extract via pdfcpu, Status-Lifecycle received→reviewed→booked/rejected, Tenant-Isolation-Tests |
| `datev` | 11 | 1389 | 486 | n/a | **DATEV-EXTF-Format-CSV-Stream-Writer** mit Berater-/Mandant-Nr-Header (Migration 219), Debitoren-Konten-Mapping, Belegbilder-Export, OAuth-Schicht (Sprint-3-Ready, noch nicht aktiv) |
| `gobdarchive` | 6 | 615 | 405 | 7 | **§147-AO-Immutable-Archive** mit SHA-256-Hex + 10-Jahre-Retention + Append-Only-Event-Log inkl. integrity_check-Events |
| `pdf` | 4 | 1095 | 210 | n/a | Maroto-v2-Generator fuer Quote/Invoice/CreditNote/**ZUGFeRDInvoice**/Dunning mit Company-Settings-Validation |
| `payment` | 4 | 549 | 775 | 4 | Atomic-Payment-Recording mit `transitionToPaidInTx`/`revertPaidStatusInTx` und Idempotency-Key seit Migration 215 |
| `tax` | 2 | 112 | 181 | n/a | Tax-Calculator fuer Standard/ReverseCharge/Kleinunternehmer + DE-19%/7%-Saetze, Helper-Funktionen |
| `bexio` | 35 | 3607 | 2763 | n/a | OAuth-Integration + Contact-/Invoice-/Quote-Push + Payment-Polling + Rate-Limiter, **G1-G5+G10 von 12 Scope-Check-Blockern geschlossen 2026-06-17** |
| `lexware` | 25 | 3030 | 869 | n/a | API-Key+Vault + Contact-Sync + Invoice/Quote-Push + **Webhook-basierter Realtime-Sync mit HMAC-SHA256-Verifikation** seit R2-P0.6 Commit `787c327` |
| **TOTAL** | **120** | **17.4k** | **12.6k** | **50+** | **~32k LOC** |

### Migrationen (chronologisch, finanz-relevant)

| Migration | Inhalt | Strategischer Anker |
|---|---|---|
| 000045 | create_finance_tables (Quote/Invoice/CreditNote/Dunning/Payment Basis) | Foundation Sprint-0 |
| 000055 | add_bexio_integration | CH-Integrations-Start |
| 000056 | add_lexware_datev_api | DE-Integrations-Start |
| 000061 | add_zugferd_and_hourly_rate | ZUGFeRD-Export-Vorbereitung |
| 000132 | add_finance_line_tables | **ADR-0007 Normalisierung Sprint-4** — line_items aus JSONB in eigene Tabelle |
| 000133 | backfill_finance_line_tables | line_items-Daten-Migration |
| 000137 | advisory_protocols | Distributed-Locking-Foundation |
| 000139 | **gobd_belegarchiv** | §147-AO-Compliance: immutable gobd_documents + gobd_document_events, SHA-256, 10-Jahre |
| 000140 | **finance_incoming_invoices** | E-Rechnung-Eingang: JSONB-LineItems/TaxBreakdown + original_xml + UNIQUE(tenant,supplier,number)-Dedup |
| 000141 | finance_invoices_contact_id | CRM-Linking-Foundation |
| 000214 | seed_finance_manager_permissions | RBAC fuer Manager-Rolle |
| 000215 | finance_payments_idempotency_key | Atomic-Payment-Idempotency |
| 000216 | add_currency_to_finance | **B6 / Multi-Currency-Vorbereitung** — CHAR(3) DEFAULT 'EUR' |
| 000217 | drop_line_items_jsonb | **ADR-0007 Phase-2-Abschluss** — JSONB-Spalten entfernt |
| 000219 | add_datev_consultant_client_numbers | DATEV-Berater-Nr + Mandanten-Nr per Tenant |

### Frontend (`desktop/src/renderer/src/modules/finanzen/`)

**Wichtige Naming-Diskrepanz**: Frontend-Ordner heisst **`finanzen`** (deutsch: Finanzen), Backend-Sub-Pakete heissen **`biz/invoice`/`biz/creditnote`/etc.** (englisch), Sources/YAML/Pricing-Karte heisst **`buchhaltung`**. Das ist eine **historische Schichten-Diskrepanz**, die das Modul-Mapping erschwert (Suche nach "buchhaltung" trifft Backend nicht, Suche nach "finanzen" trifft Backend nicht, Suche nach "invoice" trifft Frontend nicht direkt). Sprint-Anker (low-prio): **Modul-Naming-Konsolidierung** auf "buchhaltung" als kanonisches Modul-Token in Cosmi-Domain-Schicht.

**Frontend-Files (30+):**

- **Pages**: `FinanzenPage.tsx` (Mono-Root-Page), `FinanceDashboard.tsx` (Dashboard-View), `FinanceDetailNav.tsx` (Detail-Navigation)
- **Tabs**: `tabs/TransactionsTab.tsx`, `tabs/BerichteTab.tsx`, `tabs/FinanzIntegrationenTab.tsx`, `tabs/StammdatenTab.tsx`, `tabs/ExpensesTab.tsx` + Root-Level `OpenItemsTab.tsx`, `BelegketteTab.tsx`, `RecurringInvoicesTab.tsx`
- **Dialoge**: `InvoiceFormDialog.tsx`, `CreditNoteDialog.tsx`, `BankConnectDialog.tsx`, `KontierungSettings.tsx`
- **Panels**: `InvoiceDetailPanel.tsx`, `TransactionDetailPanel.tsx`, `PDFPreviewPanel.tsx`, `DunningPanel.tsx`
- **Prefs**: `FinancePersonalPrefs.tsx`
- **Library**: `lib/` (Helper-Funktionen)

**API-Layer**:
- `api/finance-client.ts` (REST-API-Client)
- `api/hooks/useFinance.ts` (TanStack-Query-Hooks fuer Finance-Endpoints)
- `api/hooks/useFinanceLedger.ts` (Ledger-spezifische Hooks)

**Volumen**: 11.415 LOC ueber 30+ TSX/TS-Files (vs. vertraege W26: 3404 LOC ueber 3 TSX-Files). Frontend ist **deutlich breiter ausgebaut** als vertraege, aber **als Mono-Page-Pattern aufgesplittet** (nicht Single-File-Mono wie VertraegePage 2417 LOC). Tabs-Pattern ist sauber.

### Was Cosmi-buchhaltung HEUTE kann (positive Bestandsaufnahme)

- ✅ **Outgoing-Invoice-Lifecycle**: Draft → Sent → Paid/Overdue/Cancelled, mit Recurring-Invoices, Storno-Rechnungen, TimeTracking-Link, Quote→Invoice-Conversion, atomic-Mark-Paid mit Idempotency
- ✅ **ZUGFeRD-Output**: PDF mit eingebettetem ZUGFeRD-XML (Migration 061), Maroto-v2-Generator
- ✅ **XRechnung-/ZUGFeRD-Import**: vollstaendiger Parser fuer CII + UBL + PDF-Attachment-Extract via pdfcpu (`einvoice` Sub-Paket)
- ✅ **GoBD-Compliance**: §147-AO-konformes Belegarchiv mit SHA-256-Integrity-Check + 10-Jahre-Retention + Append-Only-Event-Log
- ✅ **DATEV-Export**: EXTF-Format-CSV-Stream-Writer mit Berater-/Mandant-Nr (Migration 219), Debitoren-Konten-Mapping, **Snapshot-basiert**
- ✅ **Dunning-Engine**: Auto-Detection + Verzugszins-Berechnung + 3-Status-Lifecycle + GoBD-konformer Pfad
- ✅ **Multi-Currency-Foundation**: CHAR(3)-Currency-Spalte (Migration 216), DEFAULT 'EUR' aber pro Document waehlbar
- ✅ **Bexio-Integration**: OAuth + Contact-Sync + Invoice-Push + Quote-Push + Payment-Polling (mit Rate-Limiter), G1-G5+G10 von 12 Scope-Check-Blockern geschlossen
- ✅ **Lexware-Integration**: API-Key+Vault + Contact-Sync + Invoice-Push + Quote-Push + **Webhook-Realtime mit HMAC-SHA256-Verifikation**
- ✅ **Tax-Calculator**: Standard/ReverseCharge/Kleinunternehmer + DE-19%/7%-Saetze (Test-Coverage 161% — mehr Test-LOC als Prod-LOC, Indikator fuer kritischen Pfad)
- ✅ **Idempotency**: Payments mit Idempotency-Key (Migration 215), atomar Transitionen
- ✅ **RBAC**: Manager-Permissions geseedet (Migration 214), tenant_isolation_phase2_test + phase3_test
- ✅ **Feature-Flag**: `modules.buchhaltung` (SafeRisk, LLMToggleSafe)

### Was Cosmi-buchhaltung HEUTE NICHT kann (strategische Luecken)

- ❌ **KI-OCR auf Eingangsbelege**: kein Mistral-OCR-4-Adapter, kein Google-Document-AI-Adapter, kein Tesseract-Fallback. `finance_incoming_invoices`-Status `received` muss heute manuell via XML-Upload eskaliert werden — Beleg-Foto-Workflow (Smartphone → KI → Pre-Fill) fehlt komplett.
- ❌ **KI-Kontierungs-Vorschlag**: kein AI-Suggestion fuer Konto-Zuweisung pro Buchungssatz, kein Lern-Schleife pro Tenant.
- ❌ **KI-Anomaly-Detection**: kein automatischer Flag fuer Doubletten, Wert-Abweichungen, ungewoehnliche Lieferanten-Patterns.
- ❌ **KI-Dunning-Brief-Personalisierung**: Dunning-Briefe werden heute aus statischer Template-Schicht generiert, keine AI-Personalisierung nach Kunden-Historie + Zahlungsverhalten.
- ❌ **Cashflow-Forecast**: kein Forecast-Engine, kein ML-Modell fuer Liquiditaets-Projektion.
- ❌ **PEPPOL-Access-Point**: kein PEPPOL-AP, kein BIS-Billing-3.0-Versand, kein 4-Corner-Model-Adapter. **Pflicht-Stake fuer DE-B2B-Sende-Pflicht ab 2027-01-01.**
- ❌ **Bank-Feed**: kein PSD2/FinTS-Adapter, kein HBCI-Provider, keine Reconciliation-Engine. Frontend `BankConnectDialog.tsx` + `TransactionsTab.tsx` sind UI-Stubs ohne Backend-Anbindung.
- ❌ **DATEV-API-Realtime-Sync**: nur CSV-EXTF-Export, kein DATEV-Connect-Online-API-Adapter (bidirektional).
- ❌ **CH-QR-Rechnung**: kein QR-Code-Generator fuer SwissQR-Rechnung (CH-gesetzlicher Standard seit 2022-09-30). Cosmi-CH-Kunden koennen heute keine CH-QR-Rechnungen erstellen.
- ❌ **CH-Lohnbuchhaltung**: kein ELM-Format-Generator (SVA/AHV/UVG-Meldungen), keine CH-MWST-Saetze konfigurierbar.
- ❌ **OZG-Schnittstelle DE**: kein direkter Anschluss an deutsche Behoerden via OZG-XOEV-Standard.
- ❌ **Multi-Tax-Regime**: nur DE-Steuersaetze (19%/7%), CH-Saetze (7.7%/2.5%/3.7%) + AT-Saetze (20%/13%/10%) fehlen als konfigurable Tenant-Stammdaten.
- ❌ **Workflow-Approval-Multi-Stage**: `finance_incoming_invoices`-Status-Lifecycle ist linear received→reviewed→booked, keine Multi-Stage-Approval (z.B. Sachbearbeiter → Abteilungsleiter → CFO).
- ❌ **Corporate-Card-Integration**: keine Pliant/AmEx/Visa-Anbindung fuer Auto-Buchung.
- ❌ **Mobile-App-Beleg-Workflow**: kein nativer Mobile-Pfad fuer Beleg-Fotografie + Sofort-Upload (Cosmi ist Desktop-Electron + PWA, kein nativ Mobile).
- ❌ **Buchungs-Co-Pilot**: kein konversationaler AI-Assistent im UI ("Wie viel USt habe ich diesen Monat?"), nichts vergleichbar zu Lexware NAVI / Bexio AI Assistent.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Lexware Office | sevDesk | BuchhaltungsButler | Bexio | weclapp | Candis | Odoo Accounting |
|---|---|---|---|---|---|---|---|---|
| **Outgoing-Invoice Lifecycle** | ✅ Full | ✅ | ✅ | ✅ | ✅ | ✅ | ➖ AP-only | ✅ |
| **ZUGFeRD-Output (CII+PDF)** | ✅ Migration 061 | ✅ | ✅ | ✅ | ✅ | ✅ | ➖ | ✅ |
| **XRechnung-Import (UBL)** | ✅ einvoice | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **ZUGFeRD-Import (CII+PDF)** | ✅ einvoice + pdfcpu | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **GoBD §147-AO-Archiv** | ✅ Migration 139 (SHA-256, 10y) | ✅ | ✅ | ✅ | ✅ (CH-FINMA) | ✅ | ✅ | ⚠️ via Add-on |
| **Dunning-Auto-Engine** | ✅ Verzugszinsen + GoBD | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| **DATEV-CSV-Export** | ✅ EXTF + Berater-Nr (Migration 219) | ✅ | ✅ | ✅ | ⚠️ ueber Drittanbieter | ✅ | ✅ | ⚠️ Community-Modul |
| **DATEV-API bidirektional** | ❌ nur CSV | ✅ DCO-Sync | ✅ DCO-Sync | ✅ DCO-Sync | ❌ | ✅ DCO-Sync | ✅ DCO-Sync | ❌ |
| **KI-OCR Belege** | ❌ | ✅ NAVI | ✅ Std-Plan | ✅ | ✅ Bexio-AI | ✅ Q2 2026 | ✅ Kern-USP | ✅ Studio-AI |
| **KI-Kontierungs-Vorschlag** | ❌ | ✅ NAVI | ✅ | ✅ Maerz 2026 | ✅ | ✅ | ✅ | ✅ |
| **KI-Anomaly-Detection** | ❌ | ✅ NAVI | ⚠️ Beta | ⚠️ Beta | ✅ | ⚠️ Beta | ✅ Kern-USP | ⚠️ Add-on |
| **KI-Cashflow-Forecast** | ❌ | ✅ Plus | ✅ Premium | ⚠️ Beta | ✅ Premium | ✅ Premium | ❌ | ✅ Enterprise |
| **KI-Buchhaltungs-Copilot** | ❌ | ✅ NAVI | ⚠️ Q3 2026 | ❌ | ✅ Bexio-AI | ⚠️ Q2 2026 | ❌ | ⚠️ Studio-AI |
| **PEPPOL-AP (Versand)** | ❌ | 🚧 Q4 2026 (Roadmap) | ⚠️ via Crossinx-TSP | ⚠️ via Crossinx-TSP | ✅ CH-AP seit Q2 2025 | ⚠️ via Crossinx-TSP | ⚠️ via Partner | ✅ Native seit Odoo 17 |
| **PEPPOL-AP (Empfang)** | ❌ | 🚧 Q4 2026 | ✅ via TSP | ✅ via TSP | ✅ CH-AP | ✅ via TSP | ✅ via TSP | ✅ Native |
| **Bank-Feed PSD2/HBCI** | ❌ UI-Stub | ✅ finAPI | ✅ Native | ✅ Kern-USP | ✅ ISO-20022 + finAPI | ✅ | ➖ N/A | ✅ Plaid/Yodlee |
| **Bank-Transaktion Auto-Match** | ❌ | ✅ NAVI | ✅ | ✅ KI-Score | ✅ AI | ✅ | ➖ | ✅ |
| **CH-QR-Rechnung** | ❌ | ❌ (DE-fokussiert) | ❌ | ❌ | ✅ Kern-USP CH | ⚠️ via Drittanbieter | ❌ | ✅ via l10n_ch |
| **CH-MWST-Saetze (7.7/2.5/3.7%)** | ❌ nur DE-19/7 | ❌ | ❌ | ❌ | ✅ Kern-USP CH | ⚠️ via Drittanbieter | ❌ | ✅ via l10n_ch |
| **AT-MWST-Saetze (20/13/10%)** | ❌ | ⚠️ Limited | ⚠️ Limited | ❌ | ⚠️ Limited | ✅ | ❌ | ✅ via l10n_at |
| **Multi-Currency-Native** | ⚠️ Foundation (Mig 216) | ⚠️ EUR-fokus | ⚠️ EUR-fokus | ⚠️ EUR-fokus | ✅ CH+EUR | ✅ | ➖ | ✅ 170+ Waehrungen |
| **Mobile-App Beleg-Workflow** | ❌ | ✅ | ✅ | ⚠️ Limited | ✅ | ✅ | ✅ Kern-USP | ✅ Odoo Mobile |
| **Workflow-Approval Multi-Stage** | ❌ Linear-Status | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited | ✅ | ✅ | ✅ Kern-USP | ✅ |
| **Bexio-Integration (Cosmi=Partner)** | ✅ OAuth + Sync | n/a | n/a | n/a | self | n/a | n/a | n/a |
| **Lexware-Integration (Cosmi=Partner)** | ✅ Webhook + HMAC | self | n/a | n/a | n/a | n/a | ✅ | n/a |
| **Cross-Modul-CRM-Link** | ✅ contact_id (Mig 141) | ⚠️ HubSpot/Pipedrive-API | ⚠️ Limited | ❌ | ✅ Native CRM | ✅ Native CRM | ➖ | ✅ Native CRM |
| **Cross-Modul-Vertraege-Link** | ⚠️ vertraege-Modul, kein direkter Link | ❌ | ❌ | ❌ | ⚠️ Limited | ✅ | ❌ | ✅ Subscriptions |
| **Cross-Modul-Rapporte-Link** | ✅ LinkTimeTracking-RPC | ❌ | ⚠️ Limited | ❌ | ✅ via Bexio-Time | ✅ | ❌ | ✅ Timesheets |
| **Self-Host-Option** | ✅ Orbit-Roadmap | ❌ Cloud-only | ❌ Cloud-only | ❌ Cloud-only | ❌ Cloud-only | ❌ Cloud-only | ❌ Cloud-only | ✅ Community |
| **EU-Sovereign-Hosting** | ✅ Hetzner DE | ✅ Lexware DE | ✅ DE | ✅ DE | ✅ CH (Swisscom) | ✅ DE | ✅ DE | ⚠️ je nach Cloud |
| **Pricing Modul/User-Monat (EUR netto)** | **6** | **7.90-24.90 Flat** | **9.90-49.90 Flat** | **14.90-39.90 Flat** | **39-159 CHF Flat** | **39-89 (User)** | **199+ Flat (10 Belege)** | **24.90 USD (User)** |

Legende: ✅ Full implementiert, ⚠️ Eingeschraenkt/via Drittanbieter, 🚧 Geplant/Roadmap, ❌ Fehlt vollstaendig, ➖ N/A fuer Tool-Kategorie

**Lesart der Tabelle**:
- **Cosmi-Staerken (vergleichbar mit Markt)**: Outgoing-Invoice, ZUGFeRD-Output, XRechnung-Import, GoBD-Archiv, Dunning-Engine, DATEV-CSV-Export, Cross-Modul-CRM-Link, Self-Host-Option, EU-Sovereign-Hosting, **Bexio+Lexware-Partnerschaft** (das ist Cosmi-USP — kein Konkurrent integriert beide gleichzeitig).
- **Cosmi-Kritische-Luecken (Markt hat Pflicht-Stake)**: KI-OCR Belege, KI-Kontierungs-Vorschlag, PEPPOL-AP, Bank-Feed, Bank-Auto-Match, CH-QR-Rechnung, Mobile-App-Beleg-Workflow.
- **Cosmi-Strategische-Luecken (Markt-Standard, aber 6+ Monate Vorlauf)**: KI-Anomaly-Detection, KI-Cashflow-Forecast, KI-Buchhaltungs-Copilot, DATEV-API-bidirektional, Multi-Tax-Regime (CH/AT), Workflow-Approval-Multi-Stage.
- **Cosmi-Differential-Pricing**: 6 EUR/User-Monat ist **billiger** als alle DACH-KMU-Konkurrenten **bei vergleichbarem Basis-Feature-Set**, aber das Pricing-Argument schmilzt, wenn AI-Tabellenstakes fehlen.

---

## Top-3 Strategische Empfehlungen

### Empfehlung 1: KI-OCR-Layer auf Eingangsbelege als Q3-2026-Pflicht-Sprint (Phase B+C)

**Was**: Mistral-OCR-4-Adapter (oder Open-Source-Mistral-OCR-3-Base-Self-Host) in `backend/internal/biz/einvoice/ai_extraction/` als neuer Pfad zwischen PDF-/Foto-Upload und `ParsedInvoice`. Pre-Fill von Lieferant/Datum/Betrag/Steuersatz/Konto-Vorschlag mit Confidence-Score, User-Bestaetigung im `finance_incoming_invoices`-`reviewed`-Status. Aktive Lern-Schleife pro Tenant via Korrektur-Persistenz in neuer `ocr_correction_history`-Tabelle.

**Warum jetzt P0**:
- Lexware NAVI live seit Q1 2026, sevDesk-Beleg-AI im Std-Plan, BuchhaltungsButler Maerz-2026-Update — **Cosmi ist seit 6 Monaten hinter dem KI-Tabellenstake**.
- Mistral OCR 4 ($4/1000 Seiten, EU-Anbieter Paris, Apache-2.0-Open-Weight, **170 Sprachen**, RAG-ready Semantic-Chunking) hat die KI-OCR-Cost-Barriere fuer DACH-KMU **vor 4 Wochen** kollabiert (vgl. `daily/2026-06-25-evening.md` Item mit n_sources:4).
- Cosmi hat alle **Voraussetzungen** (gobd_documents Archiv, finance_incoming_invoices Status-Lifecycle, pdfcpu PDF-Extract, MinIO-Storage, Tenant-Isolation-Tests).
- EU-AI-Act Article 50 trifft am **02.08.2026** (5 Wochen weg) — Disclosure-by-Design kann jetzt beim Bau eingebaut werden, Konkurrenten muessen rueckwirkend auditieren.

**Sprint-Anker (konkret)**:
1. `backend/internal/biz/einvoice/ai_extraction/mistral_adapter.go` — Mistral-OCR-4-Client (HTTP-API + Optional Self-Host-Fallback)
2. `backend/internal/biz/einvoice/ai_extraction/ocr_result.go` — Mapping von Mistral-OCR-Output auf `ParsedInvoice`-Struktur, inkl. Confidence-Score pro Feld
3. Migration 0242 `create_ocr_correction_history` — Persistenz pro Tenant: original_extracted, user_corrected, confidence_score, created_at
4. RPC-Erweiterung `ExtractIncomingInvoiceFromBelegPhoto` — neue API neben bestehender XML-Import-API
5. Frontend `modules/finanzen/IncomingInvoiceAIExtractionDialog.tsx` — Drag-Drop-Pfad fuer Foto/PDF + AI-Pre-Fill-UI mit Disclosure-Badge "AI-extrahiert — bitte pruefen"
6. **Disclosure-by-Design**: jeder AI-Vorschlag mit eindeutigem AI-Badge + Audit-Log-Eintrag + Human-Review-Pflichtschritt im Workflow vor `booked`-Status (AI-Act-Art-50-konform)

**Kosten-/Wert-Schaetzung**: 8-12 PT Backend + 5-8 PT Frontend = ~2-3 Wochen Entwicklung mit 1 Senior + 1 Mid. Recurring-Kosten: 4-16 EUR/Tenant-Monat (50-200 Belege). Return-on-Investment: Cosmi-buchhaltung-Differenzierungs-Argument gegen sevDesk/Lexoffice in Sales-Pitches, plus User-Adoption-Boost (Beleg-Workflow ohne KI ist 2026-Anti-Pattern).

### Empfehlung 2: PEPPOL-Access-Point-Anbindung als Q4-2026-Pflicht-Sprint (DE-B2B-Sende-Pflicht-Vorlauf)

**Was**: PEPPOL-Access-Point-Integration in `backend/internal/biz/peppol/` mit Multi-Provider-Pattern (Self-Hosted-AP + TSP-Fallback). `peppol_messages`-Tabelle als Audit-Log mit `peppol_id`, `direction` (sent/received), `recipient_peppol_id`, `format` (UBL/CII), `status` (queued/sent/delivered/rejected), `original_xml`, `provider`. Neue RPCs `SendInvoiceViaPeppol`, `ListPeppolMessages`, `GetPeppolMessageStatus`. Frontend `FinanzIntegrationenTab.tsx` erweitert um PEPPOL-Konfigurations-Karte (Provider-Wahl, eigene PEPPOL-ID, Empfaenger-Verzeichnis-Lookup via PEPPOL-Discovery-Service SMP/SML).

**Warum jetzt P0**:
- **DE-B2B-Sende-Pflicht ab 2027-01-01 fuer Unternehmen >800k EUR Umsatz** (6 Monate Vorlauf). Cosmi-DACH-Kunden mit >800k EUR Umsatz (Mittelstand-Ziel-Segment) brauchen das.
- **DE-B2B-Sende-Pflicht ab 2028-01-01 fuer alle Unternehmen** (18 Monate Vorlauf). Alle Cosmi-Kunden mit DE-Sitz brauchen das.
- **5 EU-Laender bereits live mit B2B-Pflicht-Programmen** (BE seit 2026-01-01, DK seit 2026-01-01, FR Stufenplan ab 2026-09-01, PL KSeF seit 2026-02-01, ES Verifactu live).
- **EU-ViDA-Paket** (April 2026) als 2030-Backstop fuer alle EU-Laender — PEPPOL BIS Billing 3.0 als technisches Format.
- Lexware-Roadmap-Ankuendigung **eigener PEPPOL-AP fuer Q4 2026** — Lexware setzt das als kuenftiges Tabellenstake.

**Sprint-Anker (konkret)**:
1. **Provider-Entscheidung (1 PT Architecture Review)**: Self-Hosted-AP (ph-peppol-server / Mustang-Project / OpenPEPPOL-AP) vs. TSP-Integration (Pagero / Crossinx / B2Brouter / DATEV-AP-via-Berater). **Empfehlung**: **Self-Hosted-AP fuer DACH-Volumen + Pagero-Fallback fuer exotische Laender + DATEV-AP-via-Berater als Tenant-Option** (passt zu Cosmi-EU-Sovereign-Story, vermeidet Per-Document-Skalierungs-Kosten).
2. `backend/internal/biz/peppol/access_point/` — Self-Hosted-AP basierend auf ph-peppol-server oder Mustang-Project
3. `backend/internal/biz/peppol/tsp_adapter/` — Pagero/B2Brouter/DATEV-Adapter als Fallback
4. Migration 0243 `create_peppol_messages` + 0244 `add_peppol_config_to_tenants` (peppol_id, provider, smp_url)
5. RPCs `SendInvoiceViaPeppol`, `LookupPeppolRecipient`, `ListPeppolMessages`, `GetPeppolMessageStatus`
6. Frontend `FinanzIntegrationenTab.tsx` mit PEPPOL-Konfigurations-Section + PEPPOL-Discovery-Lookup-UI
7. **PKI-Pflege-Pipeline**: PEPPOL-Zertifikat-Bestellung bei Trust Service Provider, Auto-Renewal-Worker, Vault-Speicherung

**Kosten-/Wert-Schaetzung**: 15-20 PT Backend + 5 PT Frontend + 3 PT PKI-Setup = ~5-6 Wochen Entwicklung mit 1 Senior + 1 Mid. Recurring-Kosten: 200-500 EUR/Jahr PEPPOL-Zertifikat + 0 EUR/Document fuer Self-Hosted-AP. Return-on-Investment: **Compliance-Pflicht-Stake fuer DE-Kunden ab 2027-01-01, EU-Cross-Border-Stake** + Cosmi-EU-Sovereign-Differentiation gegen Lexware/sevDesk (die nutzen Crossinx-TSP).

### Empfehlung 3: Bank-Feed-Adapter mit Auto-Matching als Q4-2026-/Q1-2027-Sprint (UX-Stake)

**Was**: `backend/internal/biz/bankfeed/` mit Multi-Provider-Adapter (finAPI als Primary, Salt-Edge als EU-Sovereign-Alternative, optional Tink-Fallback). `bank_accounts`-Tabelle und `bank_transactions`-Tabelle. Auto-Matching-Engine `MatchTransactionToInvoice`-RPC mit Heuristic-Score (Betrag-Match + Referenz-Match + Lieferant-Match) **plus optional KI-Match-Score** (Phase 2). Frontend `BankConnectDialog.tsx` Backend-Anbindung + `TransactionsTab.tsx` mit Auto-Match-Vorschlaegen + Bulk-Confirm-UI.

**Warum jetzt P1 (nach KI-OCR Empfehlung 1)**:
- **Groesste KMU-UX-Luecke des gesamten Cosmi-Stacks** — Cosmi-CRM ist gut, Cosmi-Helpdesk ist gut, Cosmi-Buchhaltung ohne Bank-Feed wirkt wie "Excel-Plus" gegen Lexoffice/sevDesk/BuchhaltungsButler.
- BuchhaltungsButler positioniert Bank-Feed-Auto-Matching als **Kern-USP** — Cosmi muss in der Funktion mithalten, um gegen BuchhaltungsButler ueberhaupt im Vergleich genannt zu werden.
- Frontend hat bereits **UI-Stubs** (`BankConnectDialog.tsx` + `TransactionsTab.tsx`) — Cosmi-User erwarten die Funktion, sehen sie aber als nicht-implementiert.
- Cosmi-Pricing-Vorteil (6 EUR/User-Monat) wird **nur dann wahrgenommen**, wenn das Feature-Set vergleichbar ist.

**Sprint-Anker (konkret)**:
1. **Provider-Entscheidung (1 PT Architecture Review)**: finAPI (Deutschland, FinTech-Group/SCHUFA-owned) als Primary-Provider fuer DACH-Banken (umfangreichste DACH-Bank-Abdeckung). **Salt-Edge** (Estland/EU-only, FRX) als EU-Sovereign-Alternative — relevant fuer Cosmi-EU-Sovereign-Pitch, falls finAPI-SCHUFA-Mutter problematisch wird. **Tink (Visa-owned)** als Fallback fuer EU-Cross-Border.
2. `backend/internal/biz/bankfeed/finapi_adapter.go` — finAPI-Client mit OAuth + Webhook-Subscription fuer Transaktions-Updates
3. `backend/internal/biz/bankfeed/saltedge_adapter.go` — Salt-Edge-Client als Multi-Provider-Pattern
4. Migration 0245 `create_bank_accounts` + 0246 `create_bank_transactions` + 0247 `create_bank_transaction_matches` (Match-Score, User-Confirmed-At)
5. RPCs `ConnectBankAccount`, `SyncBankTransactions`, `MatchTransactionToInvoice`, `ConfirmMatch`, `ListBankTransactions`
6. Auto-Matching-Engine `bankfeed/matcher.go` mit Heuristic-Score:
   - Exact-Betrag-Match: +0.4
   - Naeher-Betrag-Match (±5%): +0.2
   - Verwendungszweck-Referenz-Match: +0.3
   - Lieferant-Name-Fuzzy-Match: +0.2
   - Datum-Naeher (±7 Tage): +0.1
   - Total > 0.7 = Auto-Match-Vorschlag (User-Confirm), > 0.95 = Auto-Match-Persistiert (User-Notify)
7. `BankFeedSyncWorker`-Cron alle 4h pro Tenant
8. Frontend `BankConnectDialog.tsx` Backend-Anbindung + `TransactionsTab.tsx` mit Match-Vorschlag-Liste + Bulk-Confirm-Button

**Kosten-/Wert-Schaetzung**: 15-20 PT Backend + 8-10 PT Frontend = ~5-7 Wochen Entwicklung. Recurring-Kosten: finAPI-Pricing tenant-volumens-abhaengig (typisch 5-15 EUR/Tenant-Monat fuer 5-20 Bank-Konten). Return-on-Investment: **KMU-Adoption-Boost** + Sales-Argument-Parity gegen DACH-Wettbewerb + Foundation fuer Phase 2 (KI-Bank-Match-Score in 2027).

### Sekundaere Empfehlungen (nicht Top-3, aber dokumentiert)

- **CH-QR-Rechnung-Generator** (S2): Pflicht-Stake fuer CH-Markt-Sales — kein CH-KMU akzeptiert Rechnung ohne SwissQR-Code seit 2022-09-30. `backend/internal/biz/ch_specifics/qr_invoice/` mit QR-Code-Generator (segno + SwissQR-Spec), Maroto-PDF-Integration. ~5 PT Aufwand.
- **CH-MWST-/AT-MWST-Saetze als Tenant-Stammdaten** (S2): `tenant_tax_rates`-Tabelle mit Multi-Land-Konfiguration, Tax-Calculator-Erweiterung. ~3 PT Aufwand.
- **DATEV-Connect-Online-API-Adapter (bidirektional)** (S3): nach DATEV-Berater-Approval (DCO-API braucht DATEV-Berater-Account fuer OAuth-Setup). `backend/internal/biz/datev/dco_api/`. ~10 PT Aufwand + 4-6 Wochen DATEV-Approval-Wartezeit.
- **Multi-Stage-Workflow-Approval fuer Eingangsrechnungen** (S3): nach KI-OCR (Empfehlung 1). `approval_stages`-JSONB-Konfiguration pro Tenant, `ApprovalStepClaim/Confirm/Reject`-RPCs. ~8 PT Aufwand.
- **KI-Buchhaltungs-Copilot im UI** (S4): nach KI-OCR (Empfehlung 1) als Phase 3, Anthropic-/Mistral-LLM mit Tool-Calling auf Cosmi-Buchhaltungs-RPCs ("Wie viel Umsatzsteuer habe ich diesen Monat?" → SQL-Query). Disclosure-by-Design + Audit-Log + Read-Only-Beschraenkung im MVP. ~15 PT Aufwand.
- **Modul-Naming-Konsolidierung** (S4, low-prio): Frontend-Ordner `modules/finanzen/` → `modules/buchhaltung/` umbenennen, oder Backend/Sources/Pricing-Karte auf "finanzen" angleichen. **Empfehlung**: kanonisches Modul-Token bleibt **buchhaltung** (matched Sources-YAML, Pricing-Karte, Feature-Flag `modules.buchhaltung`), Frontend-Ordner umbenennen. ~3 PT Aufwand + Migration-Path fuer User-Bookmarks.

---

## Quellen

**Markt-Recherche (State-of-the-Art-Sektion)**:
- Lexware NAVI: Lexware-Blog Q1-2026-Launch-Posts (kanonische Quelle), Heise-Bericht "Lexware launcht AI-Assistent" Januar 2026
- sevDesk Beleg-AI: DMEXCO 2025-Press-Release, sevDesk-Blog "AI im Standard-Plan" April 2026
- BuchhaltungsButler Maerz-2026-Update: BuchhaltungsButler-Blog "AI-Buchungsvorschlaege erweitert" Maerz 2026
- Candis AP-Automation: Candis-Blog 2026-Suite-Launch, Trustpilot/Capterra-Reviews
- Bexio AI-Assistent: Bexio-Blog Q1-2026, Swisscom-Press-Release
- DATEV PEPPOL-AP: DATEV-Press-Release Q4 2025 "DATEV als PEPPOL-AP"
- weclapp-AI-Assistent: weclapp-Press-Release Q2-2026
- Mistral OCR 4: Mistral-Blog 2026-06-24, Heise 2026-06-24 (`daily/2026-06-25-evening.md` n_sources:4)
- EU-AI-Act Article 50: Datamatters/Sidley Analyse 2026-06-22 (`daily/2026-06-27-regulation.md`)
- EU-AI-Omnibus: Parlament 16.06.2026, Rat-Annahme erwartet Juli 2026 (`daily/2026-06-27-regulation.md`)
- EU-ViDA-Paket: EU-Kommission April 2026
- DE-B2B-XRechnung-Stufenplan: Wachstumschancengesetz 2024, e-rechnung-bund.de (RSS down seit 10 Wochen, vgl. `daily/2026-06-20-regulation.md`)
- FR-Factur-X-Stufenplan: chorus-pro.gouv.fr 2026-Updates
- PL-KSeF: Ministerstwo-Finansow 2026-Updates
- BE/DK B2B-PEPPOL: noverstedu/erhvervsstyrelsen 2026-Updates

**Cosmi-Code-Stand-Recherche (Cosmi-IST-Stand-Sektion)**:
- `backend/internal/biz/invoice/service.go` — 14 Service-Methoden
- `backend/internal/biz/creditnote/service.go` — 7 Methoden
- `backend/internal/biz/dunning/service.go` + `service_gobd.go` — Auto-Engine + GoBD-Pfad
- `backend/internal/biz/einvoice/service.go` + `parser.go` + `pdf_extract.go` — ZUGFeRD/XRechnung-Stack
- `backend/internal/biz/datev/exporter.go` — EXTF-Stream-Writer
- `backend/internal/biz/gobdarchive/service.go` — §147-AO-Archiv
- `backend/internal/biz/pdf/generator.go` — Maroto-v2-Generator inkl. ZUGFeRDInvoicePDF
- `backend/internal/biz/payment/service.go` — Atomic-Payment
- `backend/internal/biz/tax/calculator.go` — Standard/ReverseCharge/Kleinunternehmer
- `backend/internal/biz/bexio/` — 35 Files, G1-G5+G10-Sweep `.planning/bexio-scope-check.md`
- `backend/internal/biz/lexware/` — 25 Files, HMAC-SHA256-Verifikation seit `787c327`
- Migrationen 000045/055/056/061/132/133/137/139/140/141/214/215/216/217/219 — finanzrelevant chronologisch
- Frontend `desktop/src/renderer/src/modules/finanzen/` — 30+ TSX/TS-Files, 11.415 LOC
- `desktop/src/renderer/src/api/finance-client.ts` + `api/hooks/useFinance.ts` + `api/hooks/useFinanceLedger.ts`
- Feature-Flag `modules.buchhaltung` in `backend/internal/featureflag/registry.go`
- `KMU-Hub/.knowledge/pricing.md` — Buchhaltung 6 EUR/User/Monat (Markt-Vergleich-Spalte)
- `KMU-Hub/.knowledge/integrationen.md` — Bexio/Lexware/DATEV-Status, Circuit-Breaker, Brevo-SMTP
- `KMU-Hub/.knowledge/milestones.md` — Sprint-Historie, ADR-0007 (line_items-Normalisierung), GoBD-Migration 139, e-Invoice-Migration 140

**Kontext aus laufenden Intel-Berichten**:
- `daily/2026-06-29-morning.md` — heute, buchhaltung als "stilles Modul", PostgreSQL-CVE BSI [hoch] kritisch
- `daily/2026-06-27-regulation.md` — KW26-Regulation-Sweep, AI-Omnibus, BCR-EDPB
- `daily/2026-06-25-evening.md` — Mistral OCR 4 (n_sources:4), GLM 5.2
- `daily/2026-06-26-evening.md` — Twenty-SDK, AI-Privacy-Play, Buchhaltungs-Reconciliation-Checks als Cross-Modul-Anker
- `daily/2026-06-22-evening.md` — HubSpot Revenue Hub GA (Quote-to-Cash, Cross-Modul-Hebel-Anker)
- `monthly/2026-06-22-deepdive-vertraege.md` — Vorgaenger-Deepdive mit Backend-Catch-Up-Pattern
- `monthly/2026-06-15-deepdive-formulare.md` — Vorgaenger, FormField-Typ-Drift-Pattern
- `monthly/2026-06-08-deepdive-helpdesk.md` — Vorgaenger, AI-Drafts-als-Stake-Pattern

---

## Picks (vorgeschlagen)

[ ] 🟢 **KI-OCR-Layer auf Eingangsbelege als Q3-2026-Pflicht-Sprint** — Mistral-OCR-4-Adapter in `backend/internal/biz/einvoice/ai_extraction/`, Disclosure-by-Design fuer AI-Act-Art-50, 8-12 PT Backend + 5-8 PT Frontend. **Stake**: hinter 6-Monats-Markt-Standard (Lexware NAVI, sevDesk-Beleg-AI, BuchhaltungsButler), groesste Cosmi-buchhaltung-Modernisierungs-Luecke.

[ ] 🟢 **PEPPOL-Access-Point-Anbindung als Q4-2026-Pflicht-Sprint** — Self-Hosted-AP (ph-peppol-server/Mustang) + TSP-Fallback (Pagero/B2Brouter) + DATEV-AP-via-Berater-Option, 15-20 PT Backend. **Stake**: DE-B2B-Sende-Pflicht ab 2027-01-01 fuer >800k-Umsatz-Unternehmen (6 Monate Vorlauf), 5 EU-Laender bereits live.

[ ] 🟢 **Bank-Feed-Adapter mit Auto-Matching als Q4-2026/Q1-2027-Sprint** — finAPI-Primary + Salt-Edge-EU-Alternative, Heuristic-Match-Engine mit Confidence-Score, 15-20 PT Backend + 8-10 PT Frontend. **Stake**: groesste UX-Luecke gegen sevDesk/Lexoffice/BuchhaltungsButler, Frontend hat bereits UI-Stubs.

[ ] 🟡 **CH-QR-Rechnung-Generator + CH-MWST-Saetze** (-> followup 30d) — Pflicht-Stake fuer CH-Markt-Sales, ~8 PT Aufwand kombiniert. Vor Bexio-CH-Markt-Push priorisieren.

[ ] 🟡 **DATEV-Connect-Online-API-Adapter bidirektional** (-> followup 60d, nach DATEV-Berater-Approval-Wartezeit) — von CSV-Export auf API-Realtime-Sync. ~10 PT Aufwand + 4-6 Wochen DATEV-Approval.

[ ] 🟡 **Modul-Naming-Konsolidierung Frontend** (-> followup 90d, low-prio) — `modules/finanzen/` → `modules/buchhaltung/` umbenennen, kanonisches Token konsolidieren. ~3 PT Aufwand + Migration-Path fuer User-Bookmarks.

[ ] 🟡 **AI-Disclosure-by-Design-Pattern dokumentieren** (-> followup 14d, Pflicht vor erstem KI-Release) — AI-Badge + Audit-Log + Human-Review-Workflow als Cosmi-Pattern dokumentieren in `docs/ai-disclosure-pattern.md`, dann auf alle Module ausrollen (helpdesk-AI, formulare-AI, vertraege-AI, buchhaltung-AI). EU-AI-Act-Art-50 trifft 02.08.2026.

[ ] 🔵 **PostgreSQL-CVE BSI [hoch] (Morning-Pulse `MOR-2026-06-29-i01`) noch heute pruefen** — Cosmi-Kerndatenbank kritisch, Patch-Status der Production-Postgres-Instance verifizieren. Reine Ops-Action, nicht buchhaltung-spezifisch aber kritisch fuer Cosmi-Buchhaltungs-Datenhaltung.

[ ] 🔵 **Multi-Stage-Workflow-Approval fuer Eingangsrechnungen** (-> sekundaere Empfehlung, nach KI-OCR) — `finance_incoming_invoices`-Status-Lifecycle um `approved`-Stage erweitern, Multi-Stage-Approval-Konfiguration pro Tenant. ~8 PT.

[ ] 🔵 **KI-Buchhaltungs-Copilot im UI** (-> Q1-2027, nach KI-OCR) — konversationaler Assistent mit Tool-Calling auf Cosmi-Buchhaltungs-RPCs, Read-Only im MVP, Disclosure-by-Design. ~15 PT.

---

## Routing-Telemetry

- **Modell**: claude-opus-4-7 (Strategie-Tiefe)
- **Input-Tokens (geschaetzt)**: ~340.000 (Cosmi-Code-Reads + Knowledge-Vault + Sources-YAMLs + Daily/Monthly-Kontext + Markt-Recherche)
- **Output-Tokens (geschaetzt)**: ~19.500 (Bericht selbst)
- **Runtime (geschaetzt)**: 48 Minuten
- **Quellen-Failures**: e-rechnung-bund.de RSS (10. Woche 404), sevDesk-Blog (404 in Morning), Reddit-Quellen muted (Responsible-Builder-Policy)
- **Cross-Modul-Anker**: vertraege W26 (Backend-Catch-Up-Pattern), helpdesk W24 (AI-Drafts-als-Stake), formulare W25 (Cross-Modul-Hebel-USP), W22 HubSpot-Revenue-Hub (Quote-to-Cash-Cross-Modul)
- **Naechste Rotation**: rapporte (KW28, 2026-07-06)
