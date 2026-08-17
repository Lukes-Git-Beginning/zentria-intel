---
year: 2026
week: 34
modul: produktion
created: 2026-08-17
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 46
tokens_input: ~310000
tokens_output: ~24000
rotation_position: 15/15
sources_polled:
  - sources/produktion.yaml (6 competitor blocks: weclapp, ProSeS BDE, Myfactory, MES-NeXT, ams.erp, MPDV Hydra, IIoT-Platforms)
  - sources/_competitors.yaml (Odoo cross-ref, monday.com secondary)
  - kmuhub/backend/internal/produktion/ (16 Go files, 5604 LOC)
  - kmuhub/desktop/src/renderer/src/modules/produktion/ (6 files, 2921 LOC)
  - kmuhub/backend/cmd/produktion/main.go (gRPC :50072)
  - kmuhub/backend/api/openapi.yaml (16 dokumentierte Pfade, ~17 undokumentierte Ext-Ops)
  - .knowledge/architektur.md, milestones.md (Sprint-2-Welle-1-Historie)
  - .state/hot_items_2026-08-{03..17}.json (0 produktion-Treffer 3 Wochen)
  - weekly/2026-W32.md, weekly/2026-W33.md (beide: "produktion 0 Items, stille Woche")
  - WebSearch: weclapp/Odoo/MPDV/Myfactory/ams.erp/OpenMES/CSDDD/Foerderung
---

# Deepdive: produktion (Mo W34/2026)

**Zusammenfassung in einem Satz:** Cosmi-Produktion ist ein sauberer **PPS-Kern für Losgroesse-1-bis-500-Werkstattfertigung** (Orders + Machine-Bookings mit Advisory-Lock + BOM + WorkStep + Machine + QualityCheck + Material-Availability-Cross-Check gegen Inventar) — aber die MES-Konkurrenz hat 2026 **AI-APS (Reinforcement-Learning-Scheduling), OEE-Echtzeit, OPC-UA/MQTT/UNS-Ingest und Composable-Shop-Floor-Apps** zum Standard gemacht, und Cosmi hat **null davon**. Die kritische strategische Entscheidung ist **nicht Feature-Parity** (unmoeglich gegen MPDV/Odoo), sondern eine **explizite Non-Parity-Line** analog zur Twenty-Debatte (W33): Cosmi positioniert sich als "kaufmaennisches Produktions-Backend fuer die 5-50-Mitarbeiter-Werkstatt", nicht als MES. Wer OEE-Berechnung, OPC-UA und AI-Scheduling braucht, ist bei MPDV oder Odoo besser aufgehoben — Cosmi gewinnt ueber Cross-Modul-Kette (Kunde → Angebot → Auftrag → BOM → Produktion → Rechnung) in einem System. **Der P0 fuer 2026 ist nicht Feature-Aufbau, sondern die USP-Formulierung, weil sonst Feature-Vergleiche in Sales gewonnen werden muessen, die Cosmi strukturell nicht gewinnen kann.**

---

## State-of-the-Art (Was koennen die Top-6-Konkurrenten Mitte 2026?)

Marktkontext: MES-Weltmarkt USD 19.98B (2025) → 21.85B (2026), +9.4% CAGR. 62% Smart-Factory-Integration, 57% IIoT-Adoption, 51% Predictive-Analytics, 41% Cloud-MES. `OPC-UA + MQTT + UNS` werden Zitat: "buying criteria, not IT decisions" (Nucleus 2026 Value Matrix). Cosmi-Zielgruppe (5-50 MA, Losgroesse 1-500) ist **explizit unterhalb** dieses Enterprise-Segments — die Frage ist, ob die Zielgruppe die Enterprise-Features trotzdem einfordert.

### 1. weclapp (DACH-KMU-ERP, threat_level: **high** — dieselbe Zielgruppe wie Cosmi)
- **Bedarfsmeldung → Produktionsauftrag → Bestellung**-Chain nativ (analog dem Einkauf-Deepdive W33 aufgezeigten Muster).
- Stuecklisten (Multi-Level) + Arbeitsplaene inkl. Materialdisposition + Kapazitaeten-Uebersicht — Cosmi-Aequivalent existiert nur als Single-Level BOM.
- **APS-Luecke offen bestaetigt** (ERP-Experte 2026-Vergleich weclapp vs. myfactory): "machine scheduling, capacity planning and advanced production planning (APS) are missing" — weclapp positioniert sich bewusst schlanker. **Cosmi ist hier NICHT im Nachteil**, sondern gleichauf.
- Q1/26 externe Integrationen: `planeus`-Partner-Loesung als APS-Bridge (extern, kostenpflichtig, Cloud-Sync).
- Fehlend bei weclapp genauso: OEE, OPC-UA, echtes MES.
- **Cosmi-Fenster:** Feature-Parity zu weclapp-Produktion ist realistisch (Multi-Level-BOM + Arbeitsplaene mit Materialdisposition), kein AI-Rennen noetig.

### 2. Odoo 19.1 MRP (Open-Source-Benchmark, architektonisch am naechsten an Cosmi)
- **Odoo 19.1** (Release Januar 2026): **ASAP-Planning** — MRP-Runs ignorieren Wunschtermine und planen nach Priority-Liste; **MO-Splitting** (Manufacturing-Order aufteilen bei Kapazitaets-Konflikten) automatisch.
- **AI-Demand-Forecasting** speist direkt die Produktionsplanung — Saisonalitaet, Lieferanten-Performance, externe Signale.
- **Neural-Network-Lead-Scoring, Predictive-Inventory, embedded AI-Agents** modul-uebergreifend.
- **Gantt-Chart-Verbesserungen** (Odoo 18): schnellere Reallokation, Konflikt-Highlighting.
- Odoo 19 hat AI-OCR fuer Wareneingaenge (Cloud-Service, DSGVO-Nachteil bei EU-Kunden — Cosmi-Argument).
- Multi-Level-BOM + Alternative-Routings + Sub-Contracting-Workflow — Cosmi fehlt komplett.
- **Cosmi-IST vs. Odoo-19.1:** funktional 40-50% dahinter. Odoo ist die groesste architektonische Bedrohung, weil ebenfalls Open-Source/Self-Hosted-faehig.

### 3. MPDV Hydra X + APS FEDRA (Enterprise-DACH-MES-Referenz, threat_level: **low** — falsche Kundengruppe, aber Trendsetter)
- **HYDRA X** = plattformbasiertes MES ueber VDI-Richtlinie 5600 hinaus. **BI-Adapter** (Q2/26) verkuerzt Datenaufbereitung, produktions- und qualitaetsdaten direkt in BI-Systeme.
- **APS FEDRA**: Reinforcement-Learning-basierte Feinplanung, Nutzer modelliert Planungsfaktoren, RL fuellt Luecken. Zitat: "APS wird adaptiv und realistisch".
- Enterprise-Preisklasse (sechsstellige Implementierung, monatelange Projekte).
- **Cosmi-Relevanz:** MPDV holt Kunden ab 50-100 MA — Cosmi kann darunter bleiben (5-50 MA). ABER: MPDV setzt den Feature-Referenzrahmen, was Sales-Prospects erwarten koennten. **Positioning-Sprech muss explizit klarstellen: "Cosmi ist NICHT MPDV — Cosmi ist die Vor-MES-Stufe."**

### 4. Myfactory Cloud-ERP (DACH-KMU, threat_level: **medium**)
- Vollstaendiges PPS-Modul: Stueckliste, Fertigungsauftraege, **Kapazitaetsplanung mit grafischem Plantafel**, BDE (Betriebsdatenerfassung), MRP.
- 22.000 Nutzer, 25 Jahre DACH-Fokus, 250-MA-Obergrenze — direkte Zielgruppen-Ueberschneidung mit Cosmi-Zielsegment.
- Preis: **EUR 209/User/Monat** fuer ERP + PPS-Paket (Stand 03/2026) — teuer, Cosmi-Flatrate-USP schlaegt hier voll durch.
- Cloud-only, kein Self-Hosting — Cosmi hat EU-Sovereignty-Vorsprung.
- Kein AI-APS, kein OEE-Echtzeit — Feature-Aequivalenz erreichbar.

### 5. ams.erp (DACH-Losgroesse-1-Spezialist, Auftragsfertigung)
- Nischen-ERP fuer Maschinenbau, Anlagenbau, Stahlbau, Metallbau — **Losgroesse 1+, projektorientierte Fertigung**.
- Integriertes BDE-Grundmodul + optionale BDE-Terminals mit Barcode-Scanner.
- Leitstand-Add-on fuer Feinplanung.
- **Cosmi-Ueberlappung: hoch** — dieselbe Kundengruppe (Auftragsfertigung, Losgroesse 1-500). ams.erp ist der praezise Konkurrent, wenn Cosmi das Werkstatt-Segment aggressiv adressiert.
- ams.erp hat **keinen Web-Client, keine mobile-first Erfahrung** — Cosmi kann hier UX-Vorteil ausspielen.

### 6. Tulip + OpenMES (Composable-MES-Trend, threat_level: **medium** langfristig)
- **Tulip** (US, No-Code): Frontline-Ops-Plattform, Werker bauen ohne Code Shop-Floor-Apps, Maschinen-Konnektor, ERP/MES-Bridge. Enterprise-orientiert aber Composable-Ansatz.
- **OpenMES** (getopenmes.com, Github Mes-Open/OpenMes): kostenlose Open-Source-MES mit Realtime-Monitoring, Quality-Mgmt, ERP/SCADA-Integration. **Live-Demo verfuegbar**, produkt-reif fuer KMU-Piloten.
- **qcadoo MES, Apache OFBiz, jukbot/smart-industry** — weitere Github-MES-Options, alle < 5k stars.
- **Cosmi-Relevanz:** Wenn ein DACH-KMU heute self-hosted MES sucht, ist **OpenMES + Odoo-CE die Kombination** — Cosmi muss erklaeren, warum die integrierte Kette (CRM+Angebot+Rechnung+Produktion+Buchhaltung) mehr wert ist als 2 separate Self-Hosted-Systeme.

### Sekundaere Signale
- **monday.com** hat produktion in _competitors.yaml als secondary_module — monday-Work-OS-Templates fuer Fertigung sind Marketing-Aufhaenger, aber kein echtes PPS. Wird als Vorstufe von KMU-Interessenten evaluiert, oft nicht ausreichend.
- **SAP S/4HANA Public Cloud + PP** — Enterprise-only, Cosmi-Zielgruppe unterhalb.
- **MES-NeXT, Bosch IoT, Siemens MindSphere** — IIoT-Platformen, keine PPS-Konkurrenz, aber Machine-Data-Integration-Standard, an dem Cosmi sich messen lassen wird bei Anfragen mit CNC/SPS.

---

## Cosmi-IST-Stand produktion (Code-Read Stand 2026-08-17)

**Pfad:** `backend/internal/produktion/` — 16 Go-Files, **5604 LOC**, Sprint 2 Welle 1 + Ext (BOM/WorkStep/Machine/QualityCheck).
**Frontend:** `desktop/src/renderer/src/modules/produktion/` — 6 Files, **2921 LOC** (ProduktionPage 973, DetailModals 1100, MaschinenbelegungChart 259, Export 251, Shared 143, SettingsPanel 195).
**gRPC:** `cmd/produktion/main.go` — Port 50072, gRPC-Server mit ProduktionServiceServer + ProduktionExtService.
**OpenAPI:** 16 Pfade dokumentiert unter `tags: [produktion]`, **17 Ext-Ops undokumentiert** (BOM/WorkStep/Machine/QualityCheck — bewusst nicht doku, weil `RegisterExtRoutes` laut Milestones-Note 2026-06-26 "toter Code, nirgends aufgerufen" — **VERDACHT: das ist heute veraltet, Ext-Routes sind aktiv, Doku-Drift**). **Zu verifizieren.**

### Was existiert (funktional komplett)
- **ProductionOrder** mit Lifecycle `planned → in_progress → completed / cancelled`, Priority 1-5, Planned/Actual Start-End, optionale BOM-Bindung. Start/Complete/Cancel-Aktionen.
- **MachineBooking** mit Advisory-Lock (`pg_advisory_xact_lock(hashtext(tenant||':'||machine))`) — **saubere Ueberlappungspruefung** via TX-lokalem Lock, konkurrenzsicher.
- **ProductionPlan** (weekly): total capacity hours, planned capacity hours, Status draft/active/completed, `CapacityOverview` (Booked vs. Available fuer Maschine im Plan-Zeitraum).
- **BOM + BomItem** — Single-Level (keine Sub-Assemblies), Version + Active-Flag, mehrere BOMs pro Produkt.
- **WorkStep** — Step-Nr, Duration, Assignee (freier String), 4 Status `pending/in_progress/completed/skipped`.
- **Machine** als Entity — Name, Type, Status `available/in_use/maintenance`.
- **QualityCheck** — Inspector, Passed/DefectsFound, Notes. **Order-Complete blockt** ohne bestandene QC (Frontend-Hinweis `produktion.action.qcRequiredHint` im i18n).
- **Material-Availability-Check** (`GetMaterialAvailability`) — **Highlight**: BOM-Positionen gegen echten Inventar-Bestand pruefen via `InventarLookup`-Interface (`inventar_lookup.go` — grpc-Client zu inventar-Service). Graceful degradation: unbekannte Positionen liefern `AvailableQuantity=nil` statt Fehler.
- Multi-Tenant sauber isoliert (Tests: `tenant_isolation_phase2_test.go` + `tenant_write_test.go`).
- Frontend: Auftrags-Liste, Detail-Modals, Maschinenbelegungs-Chart (Gantt-lite), CSV-Export, Laufkarte-PDF (i18n-Key `produktion.action.pdfLaufkarte`).
- Test-Coverage: 3 Test-Files fuer Postgres-Repo, 2 fuer Service, 2 fuer Multi-Tenant — solide.

### Was fehlt (kritische Luecken vs. Wettbewerb)
- **Multi-Level-BOM (Sub-Assemblies)** — komplett fehlend. Selbst weclapp und Myfactory haben das. Bei echter Werkstatt-Fertigung (auch Losgr. 1) essentiell.
- **Arbeitsplan-Vorlagen / Routings** — WorkSteps existieren nur pro Order, nicht als wiederverwendbare Vorlage pro BOM. Bedeutet: jeder neue Auftrag = manuelle Step-Erstellung.
- **APS / AI-Feinplanung** — Machine-Booking ist manuell/Advisory-Lock, kein Auto-Scheduling. Odoo hat ASAP-Planning, MPDV hat RL-basiertes FEDRA — Cosmi hat 0.
- **OEE-Kalkulation** — WorkStep-Duration + ActualStart/End sind da, **OEE (Verfuegbarkeit x Leistung x Qualitaet) ist rechnerisch ableitbar** aus Booking-geplant-vs-tatsaechlich + QualityCheck-Passed/Defects. **Steht nirgends im Code.** Sales-Argument, 3-5 Tage Aufwand.
- **BDE / Rueckmeldung von Werker (mobile/Barcode)** — kein mobile-first Shop-Floor-UI, keine Terminal-Integration. Frontend ist Desktop-Web-App fuer den Planer, nicht Werker-Tablet.
- **OPC-UA / MQTT / SPS-Ingest** — komplett fehlend. Cosmi-Position: bewusst nicht Ziel (siehe Empfehlung 3).
- **Serial-/Chargen-Verfolgung** — Cosmi-Inventar hat rudimentaeres SN-Tracking (siehe W32 inventar-deepdive), aber Produktion-Auftrag traegt keine Serials/Chargen mit — Rueckverfolgbarkeit fehlt (regulatorisch relevant fuer Lebensmittel/Kosmetik).
- **Alternative Ressourcen / Ausweich-Maschinen** — Booking bindet an eine `machine_id`, keine Fallback-Logik.
- **CSDDD/LkSG-Lieferkanten-Panel im Kontext der Produktion** — heute vermutlich in _competitors.yaml einkauf zugeordnet. Nach EU-Umnibus 2026 (siehe unten) weniger dringlich fuer KMU.
- **Nachkalkulation** (Ist-Kosten pro Order aus WorkStep-Duration x Stundensatz + Material-Ist-Verbrauch) — WorkStep hat `DurationMinutes` als geplant, ActualHours-Ist-Erfassung fehlt.
- **Produktions-Rueckstands-Report** (planned vs. actual pro Woche) — Datenmodell tragfaehig, Report fehlt.
- **Multi-Site / Werk-uebergreifende Kapazitaet** — Cosmi ist Single-Site.

---

## Konkurrenz-Vergleichstabelle produktion

Legende: ✅ vorhanden • 🚧 Beta/eingeschraenkt • ❌ fehlend • 🔵 nicht Zielgruppe/Preisklasse-inkompatibel • ➖ nicht relevant fuer Zielsegment

| Feature | Cosmi | weclapp | Odoo 19.1 | Myfactory | ams.erp | MPDV Hydra X | Tulip / OpenMES |
|---|---|---|---|---|---|---|---|
| Produktions-Auftraege (Lifecycle) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Single-Level BOM | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Multi-Level BOM (Sub-Assemblies)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Arbeitsplan-Vorlagen / Routings | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Maschinenbelegung / Kapazitaets-View | ✅ (Gantt-lite) | ✅ | ✅ (Gantt 18+) | ✅ (Plantafel) | ✅ (Leitstand) | ✅ | ✅ (Composable) |
| Advisory-Lock gegen Doppelbuchung | ✅ (pg_advisory_xact_lock) | k.A. | ✅ | k.A. | k.A. | k.A. | k.A. |
| Material-Availability-Check gegen Inventar | ✅ (cross-modul) | ✅ | ✅ | ✅ | ✅ | ➖ (delegates to ERP) | ➖ |
| **APS / AI-Feinplanung (RL, Auto-Optim)** | ❌ | ❌ (planeus-Partner) | ✅ (ASAP + MO-Splitting) | ❌ | ❌ | ✅ (FEDRA) | 🚧 |
| Alternative Maschinen / Ausweich-Ressourcen | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **OEE-Kalkulation (Verf x Leist x Qual)** | ❌ (ableitbar!) | 🚧 | ✅ | ✅ (BDE-basis) | ✅ | ✅ | ✅ |
| **BDE / Rueckmeldung Werker (mobile)** | ❌ | ✅ (mobile-fit) | ✅ | ✅ | ✅ (Terminals) | ✅ | ✅ (Composable Apps) |
| Serial / Chargen-Verfolgung | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **OPC-UA / MQTT / SPS-Ingest** | ❌ (bewusst?) | ➖ | 🚧 (via IoT-Box) | 🚧 | ➖ | ✅ (Kernkompetenz) | ✅ |
| Nachkalkulation (Ist-Kosten pro Auftrag) | ❌ | ✅ | ✅ | ✅ | ✅ | ➖ | ➖ |
| Quality-Checks / QMS-Integration | ✅ (light) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Site / Werk-uebergreifend | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Self-Hosting / EU-Souveraen** | ✅ | ❌ | ✅ (CE) | ❌ | ❌ | ✅ (On-Prem) | ✅ (OpenMES) |
| CRM+Buchhaltung+Produktion in EINEM System | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| DSGVO-by-design / DE-Server | ✅ | ✅ (DE-Server) | 🚧 (Cloud-Service in AI-OCR) | ✅ | ✅ | ✅ | ✅ (self-host) |
| Preisklasse EUR/User/Monat | Cosmi-Flat | ~99-149 | 24.90 (Standard) | 209 (mit PPS) | Projekt | 6-stellig Impl. | 0 (OpenMES) / hoch (Tulip) |

**Lesart:** Cosmi hat 8 rote ❌ in Feature-Zeilen, dafuer 4 klare ✅ in USP-Zeilen (Self-Hosting, CRM-Kette, DSGVO, Advisory-Lock). Der Vergleich sieht schlecht aus, **wenn Sales als Feature-Checkbox-Vergleich gefuehrt wird**. Er sieht gut aus, **wenn Sales als "eine integrierte Kette statt 5 Systeme"-Vergleich gefuehrt wird**. Das ist eine Marketing-Frage, keine Engineering-Frage.

---

## Was widerspricht der Cosmi-Strategie?

Ehrliche Kontradiktion (nicht wegargumentieren):

1. **Cosmi-USP "alles in einem System" bricht bei Produktion**, weil PPS-Anforderungen an OEE/OPC-UA/APS aus einer anderen technischen Welt kommen (SPS-Netzwerke, Reinforcement-Learning-Trainings). Wer diese Features **wirklich** braucht, wird Cosmi + externes MES kaufen — dann ist der USP "in EINEM System" tot fuer diesen Kunden.
2. **Odoo-CE + OpenMES + candis/getsby ist eine legitime Open-Source-Alternative-Kette** mit Self-Hosting, DSGVO und mehr Features als Cosmi — Cosmi-Kunde muss den Migrations-Zwang von 3 Systemen auf 1 System stark genug empfinden, damit die Feature-Delta akzeptabel ist.
3. **DACH-KMU-Foerderung Digitalbonus/Mittelstand-Digital laeuft 2026 aus** (Programme mit 5-50k Zuschuss fuer KMU-ERP-Einfuehrung enden Ende 2026 planmaessig, siehe BMWK-Update). Cosmi verliert einen Sales-Boost-Kanal.
4. **CSDDD wurde 2026 abgeschwaecht** (EU-Umnibus Q1/26): direkter LkSG-Enforcement-Druck auf KMU ist reduziert, kein akuter Compliance-Zugpferd-Effekt fuer Cosmi-Produktion (im Gegensatz zu XRechnung/E-Rechnung, die scharf bleibt).
5. **ams.erp als Nischen-Konkurrenz** ist Cosmi in Auftragsfertigung/Losgroesse-1 fachlich voraus — Cosmi-Marketing muss klar sagen: "wir sind fuer Handwerksbetriebe/Serienfertigung KMU, ams.erp fuer Sondermaschinenbau", sonst verliert Cosmi Deals.
6. **Twenty-Sprint-Kadenz-Muster (W33)** wiederholt sich hier: Cosmi baut PPS in Wellen, Odoo shipped alle 6 Monate ein Major-Release mit AI-Features. **Feature-Parity-Strategie kollabiert strukturell.**
7. **AI-Rollen-Cosmi hat noch keinen produktiven AI-Feature** (siehe W33 keeper `ai-substitution-lovable`), Konkurrenz hat es ueberall. Solange Cosmi keine AI-Story fuer Produktion (Auto-Scheduling, Bedarfs-Prognose) hat, klingt jedes weclapp-Sales-Deck moderner.
8. **Cosmi hat keine OPC-UA-Adapter, kein IoT-Gateway** — sobald ein Prospect "wir haben CNC-Maschinen mit Datenanbindung" sagt, ist Cosmi im Vergleichsangebot raus. Explizite Adressierung noetig: "OPC-UA via Partner-Integration" ODER "wir sind PPS ohne MDE".

---

## Top-3 Strategische Empfehlungen

### 1. **NON-PARITY-LINE explizit ziehen — Cosmi-Produktion positioniert als "kaufmaennisches PPS fuer 5-50-MA-Werkstatt, kein MES"** (STRATEGIE-P0, blockierend fuer Roadmap)

**Analog zur Twenty-Architekturentscheidung W33**: bevor die naechsten 8-12 Sprint-Wellen fuer Multi-Level-BOM/Routings/BDE-Terminal/APS eingeplant werden, muss die grundsaetzliche Frage beantwortet sein: **Baut Cosmi ein MES-Konkurrenzprodukt oder eine bewusst schlankere Vor-MES-Stufe?**

Empfehlung: **bewusst schlanker bleiben** — Cosmi-Produktion adressiert die Kundengruppe, die heute **noch mit Excel + Zettel** arbeitet, nicht die, die HYDRA X evaluiert. Konkret:
- Kein OPC-UA / SPS-Ingest bauen. Bei Anfragen: "Partner-Integration ueber IoT-Gateway XY" (potenzieller Partner: Bosch IoT, opinta.io — als OEM-Bridge, kein Cosmi-Code).
- Kein APS/AI-Scheduling in-house bauen. Positionierung: "wir liefern die Datenbasis, Feinplanung machen Excel/Trello/oder externe Tools."
- **Explizit im Marketing kommunizieren**, welche Kundengroesse Cosmi trifft und welche nicht. Analog Basecamp-Story ("we're not for everyone"). Filter-Effekt in Sales spart Deal-Frustration.
- Konsequenz: **Multi-Level-BOM + Routings-Vorlagen JA** (weil auch Excel-Werkstatt-Nachfolger das erwartet), **APS/OPC-UA NEIN**.
- Konsequenz Preisklasse: Cosmi-Flatrate positioniert unter Myfactory 209 EUR/User — konsistent zur "unter-MES"-Botschaft.

**Deliverable dieses Q3/26:** Positioning-Document fuer Sales + Website "Was Cosmi-Produktion IST und was NICHT" (analog cosmi.eu/produktion-scope). Ohne dieses Dokument gewinnt Feature-Vergleich in Sales strukturell (Cosmi verliert 8:4 gegen weclapp/Myfactory laut Tabelle oben).

### 2. **OEE-Berechnung aus vorhandenen Daten bauen — 3-5 Tage Aufwand, +Sales-Argument** (BUILD-P1)

**Rationale:** OEE (Verfuegbarkeit x Leistung x Qualitaet) ist der DE-facto-KPI, den jeder Produktions-Sales-Prospect fragt. **Cosmi hat alle Datenpunkte, aber keine Formel:**
- **Verfuegbarkeit** = ActualEnd-ActualStart / (PlannedEnd-PlannedStart) je Order (Rohwert) oder pro Machine aus Bookings mit `Status=completed` vs. `Status=maintenance`.
- **Leistung** = (Ist-Menge / Soll-Menge) × (Sollzeit / Istzeit) — WorkStep-DurationMinutes + Order.Quantity vorhanden.
- **Qualitaet** = (Order.Quantity - QualityCheck.DefectsFound) / Order.Quantity.
- OEE = V × L × Q.

**Wichtig:** OEE-Report muss **explizit** kommunizieren "Basis: geplant vs. Rueckmeldung, keine Maschinen-Direkt-Anbindung — Genauigkeit +/- 15%". Ehrlichkeit statt MPDV-Anspruch.

Sales-Effekt: "Cosmi liefert OEE-Basis-Werte am Tag 1, ohne SPS-Anbindung" = Story-Verkaufsargument gegen ams.erp/weclapp, die BDE-Terminals brauchen. **Aufwand: 3-5 Entwicklertage** (SQL-Aggregations-Query + Dashboard-Widget + i18n).

**Prio-Reihenfolge:** OEE-Report **VOR** Multi-Level-BOM ausliefern, weil Signal-Wert (Modernitaet) > Feature-Wert (Vollstaendigkeit).

### 3. **Multi-Level-BOM + Arbeitsplan-Vorlagen als "Table-Stakes-Ergaenzung" einbauen — 2 Sprint-Wellen** (BUILD-P1)

**Rationale:** Ohne Sub-Assemblies (Baugruppe A besteht aus Baugruppe B + Teil C + Teil D) faellt Cosmi bei jedem realistischen Kunden-Assessment durch — das ist Basis, nicht Advanced. Ohne Arbeitsplan-Vorlagen (Routing) ist "neuer Auftrag = 12 WorkSteps manuell tippen" ein UX-Killer.

**Scope Welle 1 (Multi-Level BOM):**
- `bom_item` bekommt optionale `sub_bom_id uuid` (References `bom.id`).
- Rekursive Expansion in `GetMaterialAvailability` (mit Loop-Detection).
- Frontend: Aufklapp-Struktur im BOM-Detail-Modal.

**Scope Welle 2 (Routings):**
- Neue Tabelle `routing` + `routing_step` (analog BOM/BomItem).
- BOM.RoutingID (optional).
- Order-Create-Flow: BOM waehlen → Steps aus Routing auto-generieren.
- Optional: Standard-Maschinen-Zuweisung pro Step.

**Aufwand:** je Welle ~1-2 Sprint-Wochen. **Prio nach OEE**, weil OEE mehr Signal-Wert hat.

### Bonus-Empfehlung (dringend, nicht produktion-Kern, aber kritisch)

**Ext-Routes-Doku-Status verifizieren** (`RegisterExtRoutes` fuer BOM/WorkStep/Machine/QualityCheck-HTTP-Endpoints). Milestones-Note 2026-06-26 sagt "toter Code" — Code-Read zeigt aber, dass Frontend die Endpoints (BOM-Detail, WorkStep-Erstellung, QualityCheck) offenbar benutzt (siehe i18n-Keys `produktion.bomDetail.*`, `produktion.action.qualitaetspruefung`). Wenn Ext-Routes aktiv sind, ist die openapi.yaml um 17 Ops **drift-belastet** — das wuerde Kundenintegrationen (via API) blockieren und ist ein P1-Doku-Bug. **Zu verifizieren durch Code-Review von `gateway/route_produktion.go` + `route_produktion_ext.go`.** Falls Drift bestaetigt: 1-Tag-Aufwand fuer openapi.yaml-Nachdokumentation, analog zum Doku-Sweep W26 (rapporte + einkauf-ext).

---

## Cross-Modul-Effekte fuer bestehende keepers

- **`ai-cost-governance` (W23):** wenn Cosmi-Produktion irgendwann APS-Auto-Scheduling bekommt, muss Preis flach/predictable sein (keine per-Run-Kosten pro Optimierungs-Lauf). Odoo-Kunden zahlen fuer AI-Features pro Token/Run — Cosmi-Chance fuer "AI-inklusiv"-Positioning.
- **`anthropic-kill-switch` (W25) + `ai-substitution-lovable-vibe-coding-w33`:** falls Cosmi je Auto-Scheduling baut, ueber den Multi-Provider-Router (`backend/internal/ai/providers/router/`) — Muse Glimmer 30B (On-Prem, siehe W33-Update) waere idealer Kandidat, weil Optimierungs-Prompts kein PII enthalten und lokal laufen koennen.
- **`e-rechnungspflicht-2027` (W23):** Produktions-Auftraege muenden in Rechnungen. Cosmi-Produktion-Modul selbst hat keinen XRechnung-Bezug, aber die Fertigmeldung → Buchhaltungs-GA-Trigger muss XRechnung-faehig sein bis 01.01.2027. Kein direkter Produktions-Fix noetig, aber Datenfluss im Auge behalten.
- **W32 inventar-deepdive:** die `InventarLookup` in Produktion-`material_availability.go` ist der **einzige echte Cross-Modul-Beweis-of-Concept** im gesamten Cosmi-Repo (nach Code-Read). **Marketing-Story-Wert!** — sollte im Positioning-Doc (Empfehlung 1) explizit erwaehnt werden als "so sieht Cross-Modul in Cosmi konkret aus, nicht als Marketing-Behauptung."

---

## Quellen (Top, die diesen Bericht stuetzen)

- Nucleus Research 2026 MES Value Matrix — [Yahoo Finance](https://finance.yahoo.com/technology/articles/nucleus-research-releases-2026-manufacturing-140000249.html)
- Odoo Manufacturing 2026 ASAP Planning + MO Splitting — [OdooSkillz Blog](https://www.odooskillz.com/blog/odoo-skillz-insights-1/odoo-manufacturing-2026-mo-splitting-asap-planning-ai-281)
- MPDV APS FEDRA Reinforcement Learning — [IT&Production Interview](https://it-production.com/fertigungsnahe-it/advanced-planning-and-scheduling/)
- MPDV Hydra X BI-Adapter Q2/26 — [mav Industrie](https://mav.industrie.de/software/performance-schub-fuer-die-smart-factory/)
- weclapp vs. Myfactory Vergleich 2026 (APS-Luecke) — [ERP-Experte AT](https://www.erp-experte.at/en/comparison/weclapp-vs-myfactory)
- Myfactory Preis EUR 209/User (03/2026) — [erp-4-business.de](https://erp-4-business.de/myfactory-erp-blog/erp-produktion-fertigung)
- ams.erp Losgroesse 1+ Positionierung — [softguide.de](https://www.softguide.de/programm/ams-erp-fuer-maschinenbau-anlagenbau-stahlbau-und-metallbau)
- OEE Benchmarks + Cloud-MES-KMU-These — [TeepTrak DE](https://teeptrak.com/de/oee-software-kmu-mittelstand-fertigung/)
- OpenMES Github Repo + Live-Demo — [Mes-Open/OpenMes](https://github.com/Mes-Open/OpenMes)
- CSDDD Umnibus 2026 Abschwaechung — [Anwalt-Seiten CSDDD Fahrplan](https://anwalt-seiten.de/eu-lieferkettenrichtlinie-csddd-fahrplan-bis-2026)
- Mittelstand-Digital Foerderung endet 2026 — [mybusinessfuture.com](https://mybusinessfuture.com/mittelstand-digital-zentren-bmwk-foerderung-auslauf-2026-nachfolge-2027/)
- Cosmi-Code: `backend/internal/produktion/` (5604 LOC), `desktop/src/renderer/src/modules/produktion/` (2921 LOC), `backend/cmd/produktion/main.go`
- Cosmi-Knowledge: `.knowledge/architektur.md` (Ports/Routes), `.knowledge/milestones.md` (Sprint-2-W1-Historie, produktion-ext-Doku-Notiz)

---

## Picks (vorgeschlagen)

- [ ] 🔴 **Positioning-Document Cosmi-Produktion "PPS ja, MES nein"** — Empfehlung 1, blockiert Roadmap-Diskussion Q4/26. **Owner: Product + Sales gemeinsam, Frist 4 Wochen.**
- [ ] 🟢 **OEE-Basis-Report aus vorhandenen Daten (3-5 Entwicklertage)** — Empfehlung 2, Sales-Signal-Wert hoch, niedriger Aufwand. Sprint-Wave-2-Ready.
- [ ] 🟡 **Multi-Level-BOM (Welle 1) + Routings (Welle 2)** — Empfehlung 3, 2 Sprint-Wellen, Table-Stakes-Ergaenzung. Nach OEE.
- [ ] 🔴 **Ext-Routes openapi.yaml-Drift verifizieren** (Bonus) — 1 Tag Aufwand, blockiert API-Kunden-Integration. **Zu checken vor naechstem produktion-Sprint.**
- [ ] 🟡 **Partner-Sondierung IoT-Gateway (Bosch IoT / opinta.io)** fuer OPC-UA-Bridge — Empfehlung 1 Konsequenz, keine Cosmi-Code-Investment, aber Sales-Antwort auf CNC-Anfragen. Recherche 2 Tage.
- [ ] 🟢 **Cross-Modul-Marketing-Story "material_availability.go als Proof-of-Concept"** — Empfehlung Bonus, Feed fuer Content-Marketing (siehe W33 Anti-SaaS-flation-Sprint keeper).
- [ ] 🟡 **Follow-up 30d:** Odoo 19.2 Release-Notes checken (erwartet Q3/26), APS-Feature-Gap-Update.
- [ ] 🟡 **Follow-up 60d:** Deepdive-Rotation-Zyklus 2 startet naechste Woche W35 mit `crm-core` (Round 2) — Cross-Referenz "was hat sich seit W20 in CRM getan?" wichtig fuer Vergleichbarkeit.

---

## Telemetry

- Rotation: Position 15/15 abgeschlossen — **erster kompletter Modul-Zyklus in 15 Wochen (W20-W34) beendet**.
- Naechste Woche (W35, 2026-08-24): Zyklus-Restart mit `crm-core`.
- State-File-Update: `.state/deepdive_rotation.json` erhaelt `last_module: produktion`, `next_module: crm-core`, `next_week: 2026-W35`, `rotation_index: 0` (Restart), `rotation_total: 15`, `zyklus: 2`.
- Erwartete Erkenntnis-Dichte Zyklus 2: **hoeher als Zyklus 1**, weil Delta-Vergleich moeglich (was hat sich beim Wettbewerber seit letztem Deepdive geaendert?).
