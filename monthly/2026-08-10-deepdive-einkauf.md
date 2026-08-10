---
year: 2026
week: 33
modul: einkauf
created: 2026-08-10
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 48
tokens_input: ~340000
tokens_output: ~28000
rotation_position: 14/15
sources_polled:
  - sources/einkauf.yaml (6 competitor blogs)
  - sources/_competitors.yaml (Odoo, weclapp, Myfactory cross-refs)
  - kmuhub/backend/internal/einkauf/ (14 Go files, 4829 LOC)
  - kmuhub/backend/internal/biz/einvoice/, biz/pdf/zugferd.go (Ausgangs-Seite)
  - .knowledge/api.md, milestones.md
  - keepers/e-rechnungspflicht-2027, eu-cada-320-mrd, ai-cost-governance
  - .state/hot_items_2026-08-{03..10}.json (0 einkauf-Treffer)
---

# Deepdive: einkauf (Mo W33/2026)

**Zusammenfassung in einem Satz:** Cosmi-Einkauf ist ein solides Sprint-2-Fundament (Supplier-CRUD, PO-Lifecycle, Framework-Contracts, Rating, Inventar-Wiring) — aber der Markt hat 2026 auf **E-Rechnungs-Eingang, AI-OCR, 3-Way-Match, PEPPOL und Autonomous-Procurement-Agents** verschoben, und Cosmi hat **keins davon**. Die wichtigste Luecke ist regulatorisch, nicht kompetitiv: **XRechnung-Eingang** ist seit 01.01.2025 gesetzliche Empfangspflicht — und wird ab 01.01.2027 auch fuer den Rechnungs-Versand Pflicht. Bis dahin muss Einkauf das Eingangs-Parsing beherrschen, sonst blockiert es die Buchhaltungs-GA (keeper `e-rechnungspflicht-2027`).

---

## State-of-the-Art (Was koennen die Top-6-Konkurrenten Mitte 2026?)

### 1. Coupa (Enterprise-Benchmark, US, threat_level fuer Cosmi: low — falsche Kundengruppe, aber Feature-Trendsetter)
- **Coupa Navi** GenAI-Copilot (Q4/25 GA): Natural-Language-Buchung "Bestell 200 Stueck A4-Papier bei bestem Lieferanten mit Lieferung bis Freitag" → wird zu PO + Approval-Chain.
- **Coupa Agents** (H1/26): autonome Ausschreibungs-Agents, verhandeln mit Lieferanten via E-Mail, generieren RfQ-Vergleichs-Tabelle.
- **Community.ai** Spend-Intelligence: aggregiert anonymisiert Preise ueber 3000+ Kunden → Benchmark-Preis pro SKU/Region.
- **Scope-3-CO2-Tracking** pro PO — CSRD-driven.
- **Multi-Tier-Supply-Chain-Visibility**: LkSG/CSDDD-Compliance-Panel, Lieferanten-N+2 Mapping.

### 2. weclapp (DACH-ERP, threat_level: high — dieselbe Zielgruppe)
- **Bedarfsmeldung → Anfrage → Angebot → Bestellung**-Chain nativ. Cosmi hat nur PO ohne vorgelagerte RfQ.
- **Multi-Lieferanten-Angebots-Vergleich** in Matrix-View.
- **E-Rechnung Empfang (XRechnung + ZUGFeRD)**: seit Q1/26 mit Auto-Buchungsvorschlag (kein AI, regelbasiert). Beleg-Erkennung ueber SDK-Partner (Zervant / candis).
- **KI-Rechnungsauslese**: **immer noch nicht Q2/26 GA** (Roadmap-Stand aus keeper `w30 weclapp-ai-status` — Cosmi-Fenster ist noch offen, aber schrumpft).
- Native Anbindung: **DATEV, Bexio, LexOffice**, keine Cosmi-Anbindung (Cosmi kann selbst Buchhaltung, insofern egal).

### 3. Odoo (Open-Source-Benchmark, architektonisch am naechsten an Cosmi)
- **Odoo 18** (2025-10): AI-OCR fuer Lieferantenrechnungen und Lieferscheine inklusive Zeilenposten-Extraktion (via `iap.odoo.com` Cloud-Service — datenschutz-fragwuerdig fuer DACH).
- **Purchase Agreements** (Framework/Blanket) — Cosmi hat das seit Welle 2 auch, funktional gleichauf.
- **Requests for Quotation** (RfQ) mit Vendor-Comparison-Report — Cosmi fehlt.
- **Purchase Approval-Workflows** ueber `hr.employee`-Managerkette — Cosmi fehlt.
- **Reordering-Rules** (Bestellpunkt-Verfahren) — Cosmi fehlt (Inventar hat `min_quantity`-Warnings, aber kein Auto-PO-Vorschlag).
- **Odoo Studio**: No-Code-Approval-Chain-Bau.

### 4. Tradeshift (EU-founded DK, IBM-Aquisition 2025)
- **PEPPOL Access Point** nativ — grosser DACH-Vorteil fuer B2B-Rechnungs-Empfang aus EU.
- **Supplier-Netzwerk** 1.5M+ Firmen, Instant-Onboarding.
- **IBM-Post-Merger Umbenennung** zu "IBM Business Network for Procurement" H2/26 geplant — **Souveraenitaets-Positionierung geschwaecht**, Cosmi-Chance fuer EU-Sovereignty-Kunden (siehe keeper `eu-sovereignty-kipppunkt` W20).

### 5. Onventis (Deutscher Mid-Market Procurement, Hannover)
- **Katalog-Aggregation** aus 200+ Lieferanten-Katalogen (Mercateo-Unite-Konkurrent).
- **Ausschreibungs-Modul** (Tender-Management) mit BAFO-Runden (Best-and-Final-Offer).
- **Compliance-Modul LkSG**: automatisierte Lieferanten-Fragebogen + Score.
- **SAP-Ariba-Ablose**-Positionierung im deutschen Mid-Market ist deren primaerer Sales-Move.

### 6. Mercateo Unite / Xeebra (DACH-B2B-Marktplatz)
- **Instant-Bestellung** aus aggregiertem Katalog von 30M+ SKUs.
- **Punchout-Integration** (OCI/cXML) — Buyer springt aus ERP in Katalog, kommt mit Warenkorb zurueck.
- **Ist Katalog+Marktplatz, nicht Procurement-Suite** — Integration statt Konkurrenz. Cosmi sollte OCI-Client bauen, nicht selbst Katalog werden.

### Sekundaere DACH-Player (kurz)
- **sevDesk Einkauf**: Beleg-erfassung mit OCR (getsby-Card + candis-Integration), **kein PO-Lifecycle**. Ergaenzung zur Buchhaltung, kein Procurement-System.
- **Myfactory / ProSeS BDE**: klassisches DE-ERP, Bedarfsermittlung MRP-basiert, keine GenAI, aber Produktions-Anbindung stark.
- **Pickware**: Shopware-Plugin, E-Commerce-Einkauf (Reorder-Rules fuer Retail), nicht KMU-Business-Procurement.

---

## Cosmi-IST-Stand einkauf (Code-Read Stand 2026-08-10)

**Pfad:** `backend/internal/einkauf/` — 14 Files, 4829 LOC, Sprint 2 Welle 1 + Welle 2 (Framework Contracts).

### Was existiert
- `models.go` — `Supplier`, `PurchaseOrder`, `POLine`, `POStatus` (draft/submitted/sent/partially_received/received/closed/cancelled) — sauberer Lifecycle.
- `models_extended.go` — `CatalogItem`, `SupplierRating` (1–5 in 3 Kategorien: quality/delivery/price), `FrameworkContract` mit `FrameworkContractItem` und `FrameworkContractCall` (Abrufe).
- `service.go` (777 LOC) — CRUD-Services fuer Supplier, PO, POLine; PO-Lifecycle-Transitions mit Validation.
- `service_extended.go` (690 LOC) — Catalog-CRUD, Rating-CRUD, FrameworkContract-Lifecycle mit `UsedValue`-Tracking.
- `inventar_adjuster.go` — `InventarAdjuster`-Interface, wired `ReceiveGoods` → `AdjustStockBySKU` (soft-fail wenn SKU im Inventar unbekannt — architektur-rule 8 graceful-degradation).
- **Test-Coverage**: `service_test.go` (984 LOC) + `service_extended_test.go` (562 LOC) + Tenant-Isolation-Tests (`tenant_isolation_phase2_test.go`, `tenant_write_test.go`) → **Coverage-Kategorie: ordentlich fuer Sprint-2.**
- **API-Endpunkte**: ~18 (aus `.knowledge/api.md`): `/api/v1/einkauf/suppliers`, `/purchase-orders`, `/po-lines`, `/receive`.
- **Frontend**: EinkaufPage mit `showWareneingangDialog` — Wareneingangs-UX existiert (aus milestones-Log W2D-Batch), Null-Guards seit `.knowledge/milestones.md` Sprint-2-Fixes bereinigt.

### Was FEHLT (kritisch — sortiert nach Business-Impact)

| # | Fehlend | Wer hat es | Regulatorisch? | Impact |
|---|---------|-----------|---------------|--------|
| 1 | **E-Rechnungs-EINGANG parsen** (XRechnung XML + ZUGFeRD-PDF-Extraktion → PO-Match → Buchungsvorschlag) | weclapp, Odoo, sevDesk | **JA — §14 UStG seit 01.01.2025 Empfangs-Pflicht** | 🔴 P0 |
| 2 | **AI-OCR fuer Papier-Lieferschein/Rechnung** | Odoo 18, Coupa, weclapp (via Partner) | nein | 🔴 P0 |
| 3 | **3-Way-Match** (PO ↔ Lieferschein ↔ Rechnung Auto-Reconciliation) | Coupa, Odoo, Onventis | nein | 🟠 P1 |
| 4 | **RfQ / Anfrage-an-mehrere-Lieferanten mit Vergleichs-Matrix** | weclapp, Odoo, Onventis | nein | 🟠 P1 |
| 5 | **PO-Approval-Workflow** (Threshold-based, Managerkette) | Coupa, Odoo, weclapp | nein (interne Compliance) | 🟠 P1 |
| 6 | **PEPPOL Access Point** (EU-B2B-Empfang standardisiert) | Tradeshift, weclapp-via-Partner | ab 2027 EU-weit Standard | 🟡 P2 |
| 7 | **LkSG/CSDDD-Lieferanten-Risiko-Fragebogen** | Onventis, Coupa Community | **JA — LkSG seit 2024 alle Firmen >1000 MA, CSDDD 2027 auch >500 MA** | 🟡 P2 |
| 8 | **Reordering-Rules** (Auto-PO-Vorschlag bei Bestellpunkt) | Odoo, Myfactory | nein | 🟡 P2 |
| 9 | **Punchout / OCI-Client** (Mercateo, Unite, andere Kataloge) | weclapp, Onventis | nein | 🟢 P3 |
| 10 | **CO2/Scope-3-Tracking pro PO** | Coupa | **JA fuer CSRD-berichtspflichtige Kunden (>250 MA ab GJ 2025)** | 🟡 P2 |
| 11 | **SupplierRating aus Signalen auto-berechnet** (Delivery-Time aus PO-Historie, Quality aus Helpdesk-Reklamationen) | Coupa | nein | 🟢 P3 |
| 12 | **Autonomous-Procurement-Agent** (GenAI-Copilot fuer PO-Anlage aus NL) | Coupa Navi/Agents | nein | 🟢 P3 (Hype > Ertrag 2026) |

### Cross-Modul-Wiring-Status
- **Inventar**: ✅ wired via `InventarAdjuster` (soft-fail).
- **Buchhaltung**: ❌ Kein Auto-Buchungsvorschlag aus Wareneingang. `biz/einvoice/` ist AUSGANGS-Seite (Cosmi als Rechnungs-Sender). Fuer Einkauf brauchen wir Einlese-Seite.
- **Vertraege**: ❌ `FrameworkContract` in einkauf ist ISOLIERT vom `vertraege`-Modul. Doppelte Vertrags-Semantik = Tech-Debt-Bombe.
- **CRM**: ✅ `Supplier.ContactID *uuid.UUID` verweist auf CRM-Contact — sauber.
- **Helpdesk**: ❌ Reklamationen aus Helpdesk fliessen nicht in `SupplierRating.quality` zurueck. Manuell blieben Ratings fast leer (typisches KMU-Muster).

---

## Konkurrenz-Vergleichstabelle (12 Zeilen)

| Feature | Cosmi | Odoo | weclapp | Coupa | sevDesk | Onventis | Tradeshift |
|---|---|---|---|---|---|---|---|
| Supplier-CRUD + Katalog | ✅ | ✅ | ✅ | ✅ | 🟡 basic | ✅ | ✅ |
| PO-Lifecycle (draft→closed) | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Framework-Vertraege (Blanket-PO) | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| SupplierRating (Q/D/P) | ✅ manuell | ✅ manuell | ✅ manuell | ✅ **auto** | ❌ | ✅ **auto (Score)** | ✅ Netzwerk-Score |
| Wareneingangs-Buchung → Inventar | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| **E-Rechnungs-Empfang XRechnung** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (PEPPOL) |
| **AI-OCR Papier-Rechnung/Lieferschein** | ❌ | ✅ Odoo 18 | 🟡 Partner | ✅ | ✅ candis | ✅ | ✅ |
| **3-Way-Match Auto** | ❌ | ✅ | 🟡 semi | ✅ | ❌ | ✅ | ✅ |
| **RfQ + Angebots-Vergleich** | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ (BAFO) | ✅ |
| **Approval-Workflows** | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **PEPPOL Access Point** | ❌ | 🟡 Plugin | 🟡 Partner | ❌ | 🟡 Partner | 🟡 | ✅ **nativ** |
| **LkSG/CSDDD-Fragebogen** | ❌ | ❌ | ❌ | ✅ Community | ❌ | ✅ **nativ** | 🟡 |
| GenAI-Copilot | ❌ | 🟡 Beta | ❌ | ✅ Navi/Agents | ❌ | ❌ | 🟡 Agent-Preview |
| CO2/Scope-3-per-PO | ❌ | ❌ | ❌ | ✅ | ❌ | 🟡 Beta | 🟡 |
| Preis/User/Monat (KMU-Package) | tbd | 25€ | 39€ | Enterprise 60€+ | 20€ | 45€+ | Enterprise |
| **Self-hosted-Option** | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **EU-Data-Residency garantiert** | ✅ | 🟡 Enterprise | ✅ | ❌ | ✅ | ✅ | 🟡 nach IBM-Deal |

---

## Was widerspricht der Cosmi-Strategie?

Zwei ehrliche Selbst-Kritiken (keeper-alignment-check):

1. **Framework-Contracts in einkauf vs. `vertraege`-Modul** — Cosmi hat sich strategisch positioniert als "cross-module context". Aber `einkauf.FrameworkContract` und `vertraege.Contract` sind heute **zwei getrennte Domain-Modelle mit ueberlappender Semantik**. Das ist genau die Fragmentierung, die Cosmi bei Konkurrenten kritisiert. **Empfehlung:** `einkauf.FrameworkContract` als View/Facade auf `vertraege.Contract` mit `type=framework_purchase` refactorn — spaeter, wenn Vertraege-Modul stabilisiert ist. Bis dahin: Migrations-Deprecation-Notice in `models_extended.go` dokumentieren.

2. **"EU-souveraen" ohne PEPPOL ist ein widerspruechliches Verkaufsversprechen** — PEPPOL ist die einzige EU-standardisierte B2B-Rechnungs-Infrastruktur. Wer nicht PEPPOL-empfangen kann, ist nicht "EU-ready". Tradeshifts IBM-Verlust hier ist eine seltene Cosmi-Chance — wenn wir schnell sind. Aber wir sind es nicht (P2 in obiger Liste). **Ehrlicher Umgang**: Positionierung "EU-Sovereignty" bewusst NICHT fuer PEPPOL-Enterprise-Cases pitchen bis Access-Point live. Sonst produziert Sales Discovery-Call-Enttaeuschungen.

---

## Top-3 Strategische Empfehlungen

### 1. 🔴 **P0: XRechnung-Eingang bauen — VOR Buchhaltungs-GA, NICHT danach**
**Warum jetzt:** Der keeper `e-rechnungspflicht-2027` sagt: 74% der DE-Firmen sind auf 2027-Rechnungs-Versand nicht vorbereitet. Was er nicht laut sagt: die **Empfangs-Pflicht existiert seit 01.01.2025**. Jede DACH-KMU MUSS heute XRechnung akzeptieren koennen. Cosmi verkauft sich als All-in-One, aber Einkauf kann Rechnungen nicht einlesen — das ist eine Discovery-Call-Bombe.

**Konkret:**
- Neues Package `backend/internal/einkauf/einvoice/` mit XRechnung-XML-Parser (UBL 2.1 / CII) und ZUGFeRD-PDF-Extraktor (nutzt bestehenden `biz/pdf/zugferd.go` als Vorbild, aber reverse — extract statt embed).
- Neue Route `POST /api/v1/einkauf/invoices/parse` — nimmt PDF oder XML entgegen, liefert strukturiertes `IncomingInvoice`-Draft + PO-Match-Kandidaten via `SupplierID + PO-Number + Betrag ± 2%`.
- UI: neuer Tab "Rechnungs-Eingang" in EinkaufPage, Drag-Drop-Zone, Vorschlags-Matching, One-Click-Buchung.
- Deadline: **Sprint 3 Welle 1** (spaetestens 2026-Q4), sonst blockt es Buchhaltungs-Pilot.

**Kosten:** ~15 Personentage Backend + 8 Frontend. Kein AI-Budget (regelbasiertes Parsing reicht — AI-OCR ist Erweiterung).

**Kreuzref:** keeper `e-rechnungspflicht-2027`; API-Doc `.knowledge/api.md` §55.

---

### 2. 🟠 **P1: RfQ-Modul + PO-Approval-Chain zusammen — nicht getrennt entwickeln**
**Warum zusammen:** Beide setzen auf `PurchaseOrder` als Kern-Objekt. RfQ ist "pre-PO", Approval ist "on-PO-transition". Wenn beide in einem Sprint gebaut werden, teilen sie sich das Notification-Wiring (E-Mail an Lieferant fuer RfQ, E-Mail an Manager fuer Approval) und die neue `EinkaufWorkflow`-Engine.

**Warum jetzt:** Ohne diese beiden Features ist Cosmi-Einkauf im DACH-KMU-Sales gegen weclapp/Odoo **direkt vergleichbar unterlegen** — nicht "auch bei". Beide sind Standard-Features seit 2022. Discovery-Kill.

**Konkret:**
- `models_extended.go`: neue Typen `RfQ`, `RfQItem`, `Quote` (=Lieferanten-Angebot auf RfQ), `ApprovalRule` (Threshold + Rolle), `ApprovalRequest` (PO ↔ Approver).
- `service_extended.go`: `CreateRfQ`, `SendRfQToSuppliers`, `RecordQuote`, `CompareQuotes` (liefert Matrix), `RequestApproval`, `ApprovePO`, `RejectPO`.
- Approval-Chain-Konfiguration: neuer Settings-Bereich pro Tenant, Regeln `IF total_amount > 5000 EUR THEN require role:team_lead`, kaskadierbar.
- Deadline: **Sprint 4** (Q1/2027).

**Warnung:** Kein Workflow-Engine-Overengineering (kein Camunda-Import). Simpel: State-Machine in Go, Config-Table in Postgres, Notifications via existierendes `notification`-Package.

---

### 3. 🟡 **P2: PEPPOL-Access-Point als 2027-Kill-Feature einplanen — jetzt Feasibility, nicht Bau**
**Warum jetzt-nicht-bauen:** PEPPOL-Access-Point ist ein 4–6-Personenmonate-Bau plus Zertifizierung (OpenPEPPOL-Autoritaet, ~15k€ Setup, jaehrliche Audit-Gebuehr). Fuer KMU-Zielgruppe erst dann Payback, wenn Kunde selbst >20 Lieferanten-XRechnungen/Monat empfaengt. Das ist heute die Ausnahme, wird 2027 die Regel.

**Was jetzt tun:** Feasibility-Spike in Q4/2026:
- Optionen bewerten: (a) eigener AP-Bau, (b) White-Label ueber deutschen AP-Partner (z.B. seeburger, Basware — beide bieten Reseller), (c) neutraler AP via PEPPOL-Directory-Lookup und Sub-Delegation.
- Entscheidungsvorlage bis Ende Q4/2026, Bau-Entscheidung in Q1/2027 mit GA-Ziel Q3/2027 (rechtzeitig vor 01.01.2028-Kickstart der volumigen Nutzung).
- Ist gleichzeitig **CADA-Argument** (siehe keeper `eu-cada-320-mrd`): "Cosmi ist der PEPPOL-Access-Point fuer den deutschen Mittelstand" — public-sector-taugliche Positionierung.

**Kosten Feasibility-Spike:** 3 Personentage Product + 2 Legal-Beratung. Bau spaeter separate Entscheidung.

---

## Zweitrangige Empfehlungen (nicht in Top-3, aber notieren)

- **SupplierRating aus Helpdesk-Reklamationen automatisch fuellen**: 3-Tage-Task. Zieht ein leeres Feature ins Leben. Delivery-Time-Rating aus PO-Historie (Compare `expected_delivery_date` vs. `received_at`) — noch schneller, 1 Tag.
- **`einkauf.FrameworkContract` → `vertraege.Contract` konsolidieren**: Refactoring-Ticket in Backlog anlegen. Nicht jetzt, aber nicht vergessen.
- **CO2-Feld pro POLine als "Datensammlung" ergaenzen** (nullable, kein Blocker): Wenn CSRD-Kunden reinkommen 2027, koennen sie retroaktiv Daten anreichern. Kosten: 1 Tag Migration.
- **OCI-Punchout-Client fuer Mercateo Unite** — als optional-Modul fuer Kunden mit hohem Standardartikel-Anteil. Q2/2027-Kandidat.

---

## Quellen (Top-Belege dieses Reports)

- **Code-Stand**: `/opt/kmuhub/backend/internal/einkauf/` (models.go, models_extended.go, service.go, service_extended.go, inventar_adjuster.go — Stand 2026-08-10).
- **API-Dokumentation**: `/opt/kmuhub/.knowledge/api.md` §54–55 (Inventar + Einkauf-Endpoints, Sprint 2 Welle 1).
- **Milestones-Log**: `/opt/kmuhub/.knowledge/milestones.md` (Sprint-2-Welle-Historie, W2D-Batch, Placeholder-Tenant-ID Altlast).
- **Ausgangs-E-Rechnung Referenz**: `/opt/kmuhub/backend/internal/biz/einvoice/` und `biz/pdf/zugferd.go` — Vorbild fuer Eingangs-Parser.
- **Keeper-Chain**: `e-rechnungspflicht-2027-74-nicht-bereit-easybillyo-cross-w23.md`, `eu-cada-320-mrd-souveränitäts-paket-konkretisiert-cross-w23.md`, `eu-sovereignty-kipppunkt-5-signale-an-einem-tag-cross-w20.md`.
- **Konkurrenz-Feature-Stand**: Ableitung aus Blog-Feeds (weclapp, Tradeshift, sevDesk, Coupa, Onventis via `sources/einkauf.yaml`) — keine neuen 2026-W33-Treffer in `.state/hot_items_2026-08-*.json` (0 procurement-Hits letzte 7 Tage → Modul-Quellen sind vermutlich rueckstaendig gepflegt — siehe Followup).
- **Regulatorik**: §14 UStG (Wachstumschancengesetz 2024), LkSG 2024, CSRD/ESRS EU 2022/2464, CSDDD EU 2024/1760.

---

## Followups fuer Bot

[ ] 🟢 **AI-OCR-Eingang als Sprint-3-P0-Kandidat aufnehmen** — XRechnung-Eingang zuerst regelbasiert, AI-OCR als Erweiterung Sprint 4. (→ `followups/einkauf-einvoice-eingang.md`, 90 Tage)
[ ] 🟢 **Framework-Contract-Konsolidierung dokumentieren** — Deprecation-Notice in `einkauf/models_extended.go` fuer FrameworkContract mit Hinweis "will move to vertraege.Contract in R4". (→ Tech-Debt-Ticket, 30 Tage)
[ ] 🟡 **PEPPOL-Feasibility-Spike planen** — Product-Discovery-Session terminieren Q4/2026 (Kalender-Task). (→ 60 Tage)
[ ] 🟡 **Einkauf-Quellen-Health-Check** — 0 Hits in 7 Tagen ist verdaechtig. Coupa/Tradeshift/Onventis RSS-Feeds auf 200-Status pruefen. (→ Source-Maintenance-Run, 14 Tage)
[ ] 🟢 **SupplierRating-Auto-Fill aus Helpdesk-Reklamationen** — Quick-Win, 3 Personentage. (→ Sprint-Backlog, 30 Tage)
[ ] 🟢 **Delivery-Time-Rating aus PO-Historie berechnen** — 1-Tages-Task. (→ Sprint-Backlog, 30 Tage)

## Picks (vorgeschlagen)

[ ] 🔴 XRechnung-Eingangs-Parser als Sprint-3-Welle-1-P0 aufnehmen (blockiert Buchhaltungs-GA)
[ ] 🟠 RfQ + Approval-Chain als Sprint-4-Doppelpack einplanen (nicht getrennt)
[ ] 🟡 PEPPOL-Feasibility-Spike Q4/2026 terminieren
[ ] 🟢 Followup: Einkauf-Quellen-Health-Check (0 Hits in 7 Tagen)
[ ] 🟢 SupplierRating-Auto-Fill Quick-Wins ins Sprint-Backlog
