---
year: 2026
week: 41
modul: vertraege
created: 2026-10-05
routine: intel-monday-deepdive
model: claude-opus-4-7
rotation_position: 7/15
zyklus: 2
delta_to: monthly/2026-06-22-deepdive-vertraege.md
---

# Deepdive: vertraege (Mo W41/2026) — Zyklus 2

> **Zweiter Durchgang nach 15 Wochen** (W26 → W41, 105 Tage). Vorgaenger-Zyklus-1 `monthly/2026-06-22-deepdive-vertraege.md`. Zyklus-2-Vorgaenger in der Rotation: `crm-core` (W35), `dialer` (W36), `video` (W37), `wiki` (W38), `helpdesk` (W39), `formulare` (W40). Naechstes Modul gemaess Rotation: **buchhaltung** (KW42, 2026-10-12). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **W26-Empfehlungs-Delivery-Scorecard (3.5/12 Picks, 29%).** W26-Zyklus-1 hat drei 🟢-Pflicht-Picks + sechs 🟡-Picks + drei 🟡-Followups ausgesprochen. Zwischen W26 und W41 (15 Wochen) ausgeliefert: **(1) ✅ PDF-Renderer Sprint 3 (W26-Pick #6 🟢)** — `backend/internal/vertraege/pdf.go` 163 LOC via Maroto/v2 (nicht Gotenberg wie empfohlen, bibliothek-basiert statt Container-Service), A4 mit Auto-Row-Heights, deutsche Status-/Type-Labels, Signature-Line (ausstehend/unterschrieben-am), Notes-Paragraph-Splitting. Der W26-TXT-Stub (`"TODO Sprint 3 — replace with PDF renderer"`) ist weg. **(2) ✅ Audit-Log-Persistierung (W26-Pick #2 🟢 Teil-d)** — Migration **000298 `contract_events`** (append-only TEXT-Action + JSONB-Payload + User-nullable + ON DELETE SET NULL + Tenant-RLS), `models.go` `ContractEvent`-Struct, 6-Werte-Closed-Set `ContractEventAction` (`created/updated/terminated/signed/party_added/party_removed`), neuer RPC `ListContractEvents` als 16. RPC. **(3) ✅ Test-Kuratierung-Sprint** (nicht als W26-Pick genannt) — Test-LOC 1148 → **3104 LOC (+170%)**: neu `contract_events_test.go` (365 LOC), `postgres_repository_db_test.go` (1162 LOC Integration-DB-Tests), `tenant_write_test.go` (97 LOC), `worker_test.go` (206 LOC), `signature_test.go` (141 LOC), `service_test.go` (819 LOC — gewachsen von ~500 LOC), `tenant_isolation_phase2_test.go` (75 LOC). Test-Ratio **220%** (3104 LOC Tests / 1409 LOC Production) ist die hoechste Test-Ratio aller 2026-Deepdive-Module (vgl. formulare W40: 141%). **(0.5) 🟡 Backend-Catch-Up Teilschritt** (W26-Pick #2 🟢) — `contract_history` als `contract_events` ist 1/4 Migrationen; `contract_signers`, `contract_documents`, `vertraege_entity_links` fehlen weiterhin.

> **Was NICHT geliefert ist (8.5/12 Picks, 71% Delivery-Luecke).** 🔴 **Pick #1 🟢 Skribble-Provider-Integration**: `backend/internal/vertraege/providers/` existiert nicht. `SignatureProvider *string` ist nach 15 Wochen immer noch Stub mit Code-Comment "Phase D: Skribble", kein Adapter, keine neuen Provider-RPCs (`RequestSignature`/`GetSignatureStatus`/`HandleProviderCallback`), kein `SignatureWebhookWorker`, keine Migration `contract_signers`. **Null Code gegen den Pflicht-Sprint-Item.** 🔴 **Pick #2 🟢 Backend-Catch-Up (3 von 4 Migrationen fehlen)**: ContractType-Mapping-Migration 0226 nicht da (deutsche Werte `mietvertrag/liefervertrag/servicevertrag/arbeitsvertrag/lizenz/versicherung` leben weiter nur im Zustand-Store `desktop/src/renderer/src/stores/vertraege.ts:58`, API-Types matchen Backend-5-Werte `rental/service/employment/nda/other`), `contract_documents`-Tabelle fehlt (Multi-Doc Frontend-only), `vertraege_entity_links` fehlt (CRM-Deal-Invoice-Linking Frontend-only). **VertraegePage.tsx 2417 → 2565 LOC (+6%)** — Mono-File-Refactor-Empfehlung wurde nicht umgesetzt, sondern **weiter aufgefuellt** (Pattern-Wiederholung von formulare W40: FormularePage 2457 → 5605 LOC in 12 Wochen). 🔴 **Pick #3 🟡 AI-Klausel-Extraction + Renewal-Brief-Generator**: null Code. Kein `backend/internal/compliance/ai_disclosure/`, kein `backend/internal/ai/providers/router/`, kein `ClauseExtractionAgent`, kein `RenewalBriefAgent`. **W31-KW31-Notfall-Sprint fuer EU-AI-Act-Art.-50-Disclosure wurde nie gestartet — Enforcement laeuft seit 2026-08-02 = heute Tag 64, Grace-Period fuer Machine-Readable-Marking (Art. 50(2)/(4)) endet 2026-12-02 = 58 Tage.** 🔴 **Pick #7 🟡 Cosmi-vertraege-MCP-Server**: null Code — und der Markt hat waehrenddessen vier CLM-MCP-Server gebaut (Concord erst, DocuSign Beta Feb 2026 → **GA Sep 30 2026** als 5 Tage alt, SpotDraft Alpha April 2026, PandaDoc im CLM-Launch 2026-09-22; Anthropic Legal-Plugins Mai 2026 mit offiziellen Claude-Connectors fuer Ironclad/DocuSign/Definely). 🟡 **Pick #4 🟡 HubSpot-Revenue-Hub-Analyse**: Oktober-Pricing-Snapshot (`monthly/2026-10-pricing.md`) hat Revenue-Hub-Bundle-Promo erfasst (Professional €57/Seat statt €95, Enterprise €98/Seat statt €140 bei Sales-Hub-Kauf = ~40% Rabatt), aber kein dediziertes Cosmi-Cross-Modul-USP-Refresh-Dokument. 🟡 **Pick #5 🟡 EU-MCT-/SCC-Klausel-Library**: null Code — und das Zeitfenster hat sich scharf gestellt: EU-Data-Act-Produktdesign-Pflicht seit **12.09.2026 fuer neue Produkte** (23 Tage zurueck), B2B-Vertrags-Pflicht ab 12.09.2027. 🟡 **Pick #8+#9 Followups W30 2026-07-20 (EUDI-Wallet-Roadmap + DocuSign Iris Rollout)**: unerledigt — und die EU-EUDIW-Deadline hat sich konkretisiert auf **2026-12-24 (80 Tage)** mit DIdG-Expertenanhörung **morgen (06.10.2026)**.

> **Delivery-Muster: Backend-Hygiene JA, Strategische-Luecken-Fuellung NEIN.** Das Muster ist konsistent mit formulare-W40-Delivery-Divergenz-Diagnose: **Team liefert schnell + sauber bei Hygiene-Items** (contract_events-Audit-Log, PDF-Renderer, Test-Coverage-Expansion mit 170% Test-LOC-Wachstum, Tenant-Isolation-Phase-2-Tests), **langsam bis gar nicht bei Markt-/Compliance-Strategie-Items** (Skribble-Integration, Multi-Signer-Backend, entity_links, AI-Compliance-Foundation, MCP-Server). Konkret in LOC: Production-Code 1277 → 1409 LOC (+10% in 15 Wochen = ~0.7%/Woche), Test-Code 1148 → 3104 LOC (+170% = ~11%/Woche), Frontend-Production-Code 3404 → 3272 LOC (-4% — leichter Rueckbau Hook+Prefs-Store), VertraegePage.tsx 2417 → 2565 LOC (+6% Weiterwuchs trotz W26-Refactor-Pflicht). **Backend-Catch-Up-Sweep ist zu 1/4 geliefert, Markt-Luecke ist komplett unadressiert — und der Markt hat sich in 15 Wochen scharf weiterbewegt.**

> **Markt-Shifts seit W26 (strategisch relevante Deltas).** **(A) Vier CLM-MCP-Server + DocuSign-GA 30.09.2026** — W26-Pick-#7 ("Cosmi-vertraege-MCP-Server, Tally-Pattern aus Formulare-W25 auf vertraege uebertragen") war in W26 noch eine Prognose, 15 Wochen spaeter ist der Markt an Cosmi vorbeigezogen: DocuSign MCP (via Iris-AI-Engine, Claude/ChatGPT/Gemini/Copilot/Slack-callable, Agreement-Intelligence + governed Action), SpotDraft, Concord, Anthropic-offizielle Legal-Plugins fuer Ironclad/DocuSign/Definely. **In-House-Legal-Teams-Markt rutscht in "AI-queryable-contracts"-Zeitalter**, und Cosmi-vertraege ist nicht aufgerufen. **(B) Ironclad Jurist Redlining Agent GA 30.04.2026** — generiert aus Playbook-Positionen first-pass-Redlines in Sekunden fuer NDAs/MSAs/third-party-paper, "days of manual work to minutes on standard agreements". DocuSign-Iris-Agents-Rollout Juli 2026 nach Momentum-Mai-Ankuendigung, DocuSign eSignature **26.3.00.00 Workflow Builder mit Quickstart-Skeleton-Generation + In-Canvas-Conversational-Editing**, Target-Prod **15.10.2026 (10 Tage)**. **(C) PandaDoc "CLM for Growing Businesses" Launch 22.09.2026** — direkte Pivot in Cosmi-KMU-Sweet-Spot: "automatically reads every agreement, surfaces what needs attention, keeps growing teams ahead of renewals, obligations, next steps". PandaDoc war in W26 noch Mid-Market/Sales-Funnel-Positioniert, in W41 ist es **direkter DACH-KMU-30-100-Mitarbeiter-Konkurrent neben ContractHero + fynk**. **(D) ContractHero Essential-Tier €250 → €390/Monat (+56% Preiserhoehung)** — Volume-Erweiterung (500 statt bisher 200 Vertraege), aber Monatspreis-Verdopplung in Richtung Cosmi, erweitert Cosmi-Preis-Window fuer 2-50-MA-Segment. **(E) fynk Pricing-Pivot von Flat €89 auf per-User** (Essential €29/User/Monat monatlich oder €19/User/Monat jaehrlich, Business €49/User/Monat, Pro on request) — der mittlere Preis-Punkt sinkt bei Teams von 3-5 Mitarbeitenden (3 × €19 = €57/Monat jaehrlich < €89 flat), Cosmi-Modul-Preis-Spannung bei 2 EUR/User/Monat Modul-Anker bleibt deutlich darunter. **(F) EUDI-Wallet-Deadline konkretisiert auf 2026-12-24** (**80 Tage**), DIdG-Expertenanhörung Bundestag Ausschuss Digitales **06.10.2026 (MORGEN)**, DE-EUDIW-Rollout Q1 2027 — Cosmi-Vertraege-eIDAS-Modul (`backend/internal/vertraege/eidas/eudi-wallet-prep/`) ist offener Followup-Punkt in W39+W40-Weekly, kein Code. **(G) BGH-Rechtsprechung-Aktualisierung** — korrektes Aktenzeichen fuer W26-angesprochenes QES-Urteil ist **BGH 25.02.2026 VII ZB 29/24** (nicht wie in W26-Report angegeben "II ZB 13/24"), BGH-beA/qeS-Entscheidung **05.2026 Celle-OLG aufgehoben** (iww.de/beck-aktuell). **(H) EU-Data-Act-Produktdesign-Pflicht seit 12.09.2026** fuer neue Produkte (23 Tage), B2B-Vertrags-Pflicht ab 12.09.2027 (342 Tage) — Model-Contractual-Terms + SCCs sind final (Expert-Group-Report 02.04.2025). Cosmi hat weder Produktdesign-Review durchgefuehrt noch MCT-Klausel-Library eingebaut. **(I) Ghostscript Privilege Escalation [HOCH] (BSI 30.09.2026)** — `backend/internal/vertraege/pdf.go` nutzt Maroto/v2 (Go-nativ, keine Ghostscript-Dependency), aber Pflicht-Audit auf transitive Deps + buchhaltung/pdf-Pipeline (`backend/internal/buchhaltung/pdf/`) steht aus. **(J) Keeper-Cross W25 Anthropic-Kill-Switch** bleibt relevant — Provider-Router-Architektur ist unerfuellter Pflicht-Baustein fuer AI-Phase-1, und W41-W40 Carry-Forward hat Mistral/Shieldstral als konkreten DACH-Baustein konfiguriert.

> **Leit-Signal der Woche:** **Heute Montag 2026-10-05 ist nicht der Tag des neuen Markt-Signals, sondern der Tag der 15-Wochen-Delivery-Rechnung.** Der W26-Zyklus-1-Bericht hat drei Pflicht-Items benannt (Skribble-Integration, Backend-Catch-Up, AI-Phase-1-Disclosure-by-Design) und sechs Followup-Items. **15 Wochen spaeter: 1/3 Pflicht-Items voll, 2/3 null. Das Ingenieurs-Pattern (Hygiene-Delivery schnell, Markt-Scope langsam) ist dabei das aus formulare-W40 wiederholte Delivery-Divergenz-Muster**. Was der Bericht heute zusaetzlich leistet, ist die **Markt-Zeit-Rechnung**: in 15 Wochen hat der CLM-Markt vier MCP-Server veroeffentlicht (DocuSign GA vor 5 Tagen), zwei grosse Legal-AI-Agent-GAs ausgeliefert (Ironclad Jurist Redlining 30.04., DocuSign Iris-Rollout Juli), zwei DACH-Preis-Verschiebungen gesetzt (ContractHero +56%, fynk auf per-User), und drei regulatorische Fenster scharf gestellt (Art. 50-Enforcement live seit 64 Tagen mit 58-Tage-Grace-Period, EUDI-Wallet-Deadline 80 Tage, EU-Data-Act-Produktdesign aktiv). **Dieser Bericht empfiehlt daher drei Pflicht-Items + zwei Komprimierungs-Entscheidungen** (statt sieben neuer Picks), weil der Weg aus 71% Delivery-Luecke nur ueber Fokus geht, nicht ueber mehr Items.

---

## State-of-the-Art — Markt-Delta vs. W26

Der Vertrags-/CLM-Markt Oktober 2026 ist nicht mehr Mitte-2026-Vierspur-Markt, sondern **fuenfspurig geworden**: zu den W26-dokumentierten (1) Agentic-CLM-First, (2) AI-Assisted-Authoring, (3) DACH-eIDAS-QES-Spezialisten, (4) DACH-KMU-Vertragsverwaltung-Light kommt (5) **MCP-interoperable-CLM-Platforms** als neue Kategorie. Vier CLM-Vendoren haben in den letzten 8 Monaten MCP-Server published (Concord erst, DocuSign Beta Feb 2026 → GA 2026-09-30, SpotDraft Alpha April 2026, PandaDoc im CLM-Launch 2026-09-22), Anthropic hat 20+ Legal-MCP-Connectors + 12 Legal-Practice-Area-Plugins im Mai 2026 veroeffentlicht (offizielle Claude-Connectors fuer Ironclad, DocuSign-inkl.-CLM, Definely). **Diese fuenfte Spur verschiebt die Marktrethorik erneut**: war in Q1-Q2 2026 die Botschaft "AI uebernimmt Review/Renewal/Risk", ist in Q3-Q4 2026 die Botschaft "Vertraege werden AI-queryable + agent-callable aus jedem Tool heraus" — Legal-Teams nutzen Claude/ChatGPT/Gemini/Copilot/Slack als Shell-UI fuer CLM-Operations, der CLM-Vendor liefert nur noch Data + Tools, nicht mehr Primary-UI. **Diese Verschiebung macht die Cosmi-W26-Pick-#7-MCP-Server-Empfehlung von Nice-to-Have zu Table-Stakes-fuer-Verbleib-im-Markt**: ein Vertrags-Modul ohne MCP-Server wird in 12 Monaten als "nicht AI-ready" wahrgenommen, selbst wenn interne AI-Features ausgeliefert waeren. Cosmi-vertraege sitzt heute strukturell in Spur (4) KMU-Vertragsverwaltung mit zwei Delivery-Zugewinnen (PDF-Renderer, Audit-Log), **aber ohne jeden Baustein in Spur (1-3+5)**.

Fuenf strukturelle Delta-Bewegungen gegen den W26-Report:

**(a) Agentic-CLM ist nicht nur Table-Stake, sondern GA-Realitaet.** Was W26 als "Welle 3+4 Early-Access" dokumentiert hatte (Ironclad Acting-Capabilities April 2026, DocuSign IAM-Momentum Mai 2026), ist 15 Wochen spaeter GA + Production-Rollout: **Ironclad Jurist Redlining Agent GA 30.04.2026** generiert aus hochgeladener Playbook-Position first-pass-Redlines fuer NDAs/MSAs/third-party-paper in Sekunden, early-adopter-Reports "days to minutes" fuer Standard-Agreements. **DocuSign Iris-Agents-Rollout startete Juli 2026** nach Momentum-Mai-Ankuendigung — Intake/Triage/Smart-Redlining/Relationship-Intelligence/Renewal/Obligation-Tracking Agents sind nicht Beta mehr, sondern Production. **DocuSign eSignature-Release 26.3.00.00 Target Oktober 15, 2026 (10 Tage)** bringt den Workflow-Builder-Layer mit *Quickstart Skeleton Generation* + *In-Canvas Conversational Building & Editing*: nicht nur "AI reviewed your contract", sondern "AI builds your signing workflow from a sentence". PandaDoc hat am **22.09.2026 CLM-for-Growing-Businesses** gelauncht ("automatically reads every agreement, surfaces what needs attention, keeps growing teams ahead of renewals, obligations, next steps") — PandaDoc war in W26 noch Mid-Market/Sales-Funnel-Positioniert, in W41 ist PandaDoc **direkter DACH-KMU-30-100-Mitarbeiter-Konkurrent** nebst ContractHero+fynk. **LinkSquares All-Agentic-CLM** war in W26 schon GA, in W41 akkumulieren Reviews. **Konsequenz fuer Cosmi-vertraege**: 15 Wochen in denen jeder relevante Marktplayer entweder ein AI-Agent live hat oder ein naechstes AI-Feature-Release im Umlauf hat — Cosmi-vertraege-AI-Status: `backend/internal/vertraege/ai/` existiert nicht, `backend/internal/compliance/ai_disclosure/` existiert nicht, `backend/internal/ai/providers/router/` existiert nicht. **Pro Monat Verzug waechst die Wahrnehmungs-Luecke** — Cosmi-Modul-Pricing 2 EUR/User/Monat haelt bei einem 2026er Vertrags-Markt der KMU-Vertragsverwaltung-fuer-30-100-MA, verliert aber bei KMU-Entscheidern die bereits DocuSign-/PandaDoc-/fynk-Demos gesehen haben (= AI-Review + Renewal-Prediction + Dispatch-Signer).

**(b) MCP-Server ist die neue Konkurrenz-Linie — und Cosmi hat die W26-Empfehlung 15 Wochen ignoriert, waehrend DocuSign den Markt eroeffnet hat.** Dies ist die wichtigste Delta-Beobachtung dieses Berichts: W26-Pick #7 war im Juni 2026 die visionaer-vorsichtige "Tally-Pattern-auf-vertraege-uebertragen"-Empfehlung mit Sprint-Timing *"nach AI-Phase-1"*. Heute 15 Wochen spaeter ist die Realitaet **Concord → DocuSign-Beta-Feb-2026 → SpotDraft-Alpha-April-2026 → PandaDoc-CLM-Sep-2026 → DocuSign-MCP-Server-GA-30.09.2026**. **DocuSign hat die Agreement-Intelligence + governed-Action via Iris-Engine durch MCP in jedes KI-Tool exportiert — Claude/ChatGPT/Gemini/Copilot/Slack koennen alle DocuSign-CLM-Operationen durchfuehren.** Anthropic hat zusaetzlich **Mai 2026** 20+ Legal-MCP-Connectors + 12 Legal-Practice-Plugins published, mit offiziellen Claude-Connectors fuer Ironclad, DocuSign (inkl. CLM), Definely. Praktische Implikation fuer Cosmi-KMU-Markt: wenn ein DACH-KMU-Entscheider ("ich will dass Claude meine Vertraege lesen und analysieren kann") fragt — fuer DocuSign-/Ironclad-/PandaDoc-Kunden ist die Antwort heute "ja, via MCP", fuer Cosmi-vertraege-Kunden ist die Antwort heute "nein". **Das ist nicht ein Nice-to-have-Marketing-Punkt, sondern ein konkreter Buy-Decision-Faktor in Q4-2026-Pipelines**, besonders in Public-Sector-Beschaffung (CADA-W23-Keeper) + AI-affinen Legal-Departments. Cosmi-MCP-Server fuer vertraege ist jetzt kein 5-7-Tage-Sprint mehr (W25-formulare-Diagnose-Pattern), sondern eher 2-3 Wochen weil Multi-Signer-Workflow + Audit-Log-Query + CRM-Linking-Query via MCP exposed werden muessen — und von den drei genannten Operationen hat nur das Audit-Log Backend-Persistierung heute.

**(c) EU-regulatorik-Fenster scharf gestellt und laufende Non-Compliance eskalieren.** W26 hat **drei** regulatorische Anker beschrieben: EU-AI-Act Art. 50 ("trifft 2. August"), eIDAS 2.0 EUDI-Wallet ("Dezember 2026 als 27-MS-Pflicht"), EU-Data-Act (B2B-Pflicht ab 12.09.2027). Heute 2026-10-05 ist die Rechnung: **(i) EU-AI-Act Art. 50 ist seit 2026-08-02 live-enforcement (= heute Tag 64), Machine-Readable-Marking-Grace-Period fuer Pre-Enforcement-Systeme laeuft bis 2026-12-02 (= 58 Tage).** Enforcement durch nationale Market-Surveillance-Authorities, Bussgeld bis €15 Mio oder 3% Welt-Umsatz. Fuer Cosmi-vertraege waere das heute null Pflicht (keine AI-Funktion live), aber **jede zukuenftige AI-Vertrags-Funktion muss ab Live-Gang mit Disclosure-Layer kommen** — und waehrend 15 Wochen auf Cosmi-Modulen anderer Teams (Meeting-AI-Summary im Video-Modul seit 02.08.2026) ohne Disclosure gelaufen ist (W37-video-Deepdive-P0 markiert), waechst der Case fuer Zentral-Compliance-Baustein, der dann auch vertraege-AI-Phase-1 traegt. **(ii) EU-EUDIW-Deadline 2026-12-24 (= 80 Tage), DE-EUDIW-Rollout Q1 2027, DIdG-Expertenanhörung Bundestag Ausschuss Digitales 06.10.2026 MORGEN** (`weekly/2026-W40.md` + `daily/2026-10-02-evening.md` + `daily/2026-10-03-regulation.md`-Followup markiert). Cosmi als Relying Party muss EUDIW-Anbindung in Q4-Sprint planen — Modul-Pfade `backend/internal/auth/eudiw/` und `backend/internal/vertraege/eidas/` sind in intel-notes identifiziert, kein Code. **(iii) EU-Data-Act Produktdesign-und-Direct-Access-Pflicht seit 12.09.2026 fuer neue Produkte** (23 Tage zurueck), B2B-Vertrags-Pflicht ab 12.09.2027 (342 Tage). Model-Contractual-Terms (MCTs) + Standard-Contractual-Clauses (SCCs) sind final seit Expert-Group-Report 02.04.2025. **Cosmi hat weder Produktdesign-Review durchgefuehrt noch MCT-Klausel-Library eingebaut** — W26-Pick #5 war "nach AI-Phase-1", in W41 ist AI-Phase-1 nicht gestartet. **(iv) BGH 25.02.2026 VII ZB 29/24** (korrektes Aktenzeichen, W26-Report-Aktenzeichen "II ZB 13/24" war inkorrekt): simple E-Signatur in Mahnverfahren muss trotz Vollautomatisierung von natuerlicher Person validiert werden. BGH **Mai 2026** hat OLG-Celle-Rueckweisung bei beA-ohne-qeS wegen "ueberraschender Unzulaessigkeit" aufgehoben — ERV-Praxis unter Druck, QES-Verfahrens-Nachweis wichtiger. Praktische Implikation: Cosmi-EES-Canvas bleibt fuer Innerbetriebliche-Vertraege ok, fuer Form-pflichtige/beA-Scenarios ist QES-Provider unverzichtbar. **Keine der vier regulatorischen Deltas wird durch Cosmi-W41-Code adressiert.**

**(d) DACH-KMU-Preis-Fenster weitet sich zu Cosmis-Gunsten — aber nur wenn Funktion-Parity waechst.** W26 hat ContractHero (Essential **390 EUR/Monat** Flat als klein, Professional+Enterprise on request) und fynk (Essential **89 EUR/Monat**, Growth 249, Advanced 379, 20% Annual-Discount, Free-Basic) als zwei Hauptkonkurrenten im DACH-KMU-10-100-Mitarbeiter-Segment beschrieben. 15 Wochen spaeter: **ContractHero Essential 390 EUR/Monat → nach Preiserhoehung 390 EUR + Volume-Erweiterung auf 500 Vertraege (W26-Zahl 390 bleibt, aber mit 500-Vertraege-Cap, Essential-Vorgaenger-Preis 250 EUR mit 200 Vertraege ist weg).** W26-Report-Preis-Angabe entsprach bereits der neuen Baseline, aber die Kommunikation von +56% fuer Pre-Pricing-Kunden bleibt ein Verkaufs-Window — Cosmi-Marketing kann 2 EUR/User/Monat Modul-Pricing als "DACH-KMU-vertraegliches Vertrags-Modul statt 7-18x teurer Standalone" positionieren. **fynk Pricing-Pivot von Flat €89 auf per-User** (Essential €29/User/Monat monatlich oder €19/User/Monat jaehrlich, Business €49, Pro on-request) macht fuer 3-5-Mitarbeiter-Teams die fynk-Rechnung guenstiger (3 × €19 = €57/Monat jaehrlich vs. frueher €89 flat), fuer 10-MA-Teams teurer (10 × €19 = €190 jaehrlich vs. €89 flat alt). **Cosmi-2-EUR/User-Monat bleibt deutlich unter fynk-Essential-€19/User-jaehrlich bei gleicher Team-Groesse** — Pricing-Narrative-Window ist offen, aber nur wenn Feature-Parity (AI-OCR, AI-Klausel-Detektion, QES-Integration) in Sichtweite ist. **Ohne diese Parity-Items ist Cosmi-vertraege standalone unverkaufbar gegen fynk — exakt das W25-Formulare-Pattern** ("Cosmi-standalone-pitch verliert gegen Tally-Free") wiederholt sich.

**(e) HubSpot-Revenue-Hub-Pricing dekonstruiert (W26-Pick #4-Teil).** Oktober-Pricing-Snapshot (`monthly/2026-10-pricing.md`) hat erstmals vollstaendige HubSpot-Preise erfasst: Free €0, Starter €7/Seat/Monat, Professional €90/Seat/Monat, Enterprise €150/Seat/Monat — plus **aktive Bundle-Promo "Buy Sales Hub, get Revenue Hub Professional €57/Seat/Monat (statt €95), Enterprise €98/Seat/Monat (statt €140) = ~40% Rabatt"**. HubSpot nutzt Revenue-Hub als Sales-Hub-Attach-Rate-Verstaerker — klassische Platform-Attack-Strategie. **Cosmi-Modul-Preis-Spannung** ist eindeutig: Cosmi-Modul 2 EUR/User/Monat vs. HubSpot-Starter 7 EUR/Seat (Vertraege-Features nicht enthalten) vs. HubSpot-Revenue-Hub-Pro 57-95 EUR/Seat/Monat (Vertraege + Billing + Quote-to-Cash). **Fuer DACH-KMU 10-MA ist Cosmi-vertraege-Modul 20 EUR/Monat vs. HubSpot-Revenue-Hub-Pro 570 EUR/Monat Bundle-Preis** — 28x Preis-Differenz, aber HubSpot bietet komplette Quote-to-Cash-Pipeline + Breeze-AI-Agents. Cosmi-Cross-Modul-USP-Pitch muss die Rechnung **"Cosmi crm-core + vertraege + buchhaltung = 3-6 EUR/User/Monat Modul-Summe vs. HubSpot-Revenue-Hub-Pro 57 EUR/Seat/Monat Bundle = 10-20x guenstiger"** haben — aber nur wenn die drei Module Cross-Modul-Workflows gesund abliefern. **Realitaetscheck W41**: vertraege-CRM-Linking ist Frontend-only, vertraege-Buchhaltung-Linking null, vertraege-Helpdesk-Linking null (vgl. W39-Deepdive helpdesk entity_links `migration 000267` existiert *fuer* helpdesk↔contact-org, aber keine vertraege-Variante). Cross-Modul-USP ist Pitch-Material, Backend-Realitaet ist Modul-Silo.

### Top-Konkurrenten — Delta-Update zu W26

**1. DocuSign (international, threat: HIGH + weiter steigend — MCP-GA + Workflow-Builder-Oct-15)**

- **DELTA seit W26 (W26-Report-Zustand: "Iris-AI-Engine komplett, IAM-Momentum-Mai Beta, Juli-Rollout angekuendigt")** — in 15 Wochen ausgeliefert: (i) **Iris-Agents-Rollout Juli 2026 (nach W26 angekuendigt, geschehen)**; (ii) **DocuSign MCP-Server GA 30.09.2026** — Agreement-Intelligence + governed-Action callable aus Claude/ChatGPT/Gemini/Copilot/Slack und jedem MCP-Client; (iii) **DocuSign eSignature 26.3.00.00 Target-Prod 15.10.2026** mit Quickstart-Skeleton-Generation + In-Canvas-Conversational-Building; (iv) **Agentic Contract Workflows for In-House Legal Teams** (Momentum-Follow-Up, Investor-PR); (v) **Investor-PR "Docusign Unveils AI Assistant and Agents to Power the Next Era of Agreement Work"**. **Konsequenz fuer Cosmi**: DocuSign hat in 15 Wochen den naechsten Stack-Layer gewechselt — von "Iris reviewt Vertraege" zu "AI-Agents orchestrieren den Vertrags-Lifecycle, MCP exportiert Operationen in jedes AI-Tool". **Strategischer Hinweis-Update** (vs. W26): Cosmi gewinnt NICHT mehr nur ueber "Vertraege-in-CRM-in-Helpdesk-in-Wiki-in-Buchhaltung", sondern **MUSS einen MCP-Server bauen, damit das Cross-Modul-Argument ueberhaupt sichtbar wird** — ohne MCP-Shell bleibt der Cross-Modul-Hebel von Cosmi unsichtbar fuer AI-affine KMU-Entscheider, DocuSign hingegen zieht alle KI-Shells auf sich.

**2. Skribble (Schweiz/DACH, threat-Rolle unveraendert: strategischer-Partner-Kandidat, nicht primaerer Konkurrent)**

- **DELTA seit W26 (W26-Report-Zustand: "wichtigster strategischer Vertrags-Partner-Kandidat im DACH-Markt, Sprint-3-reif, Pflicht-Item")** — keine konkrete Public-Release-Signale seit W26 (Skribble-Blog-RSS in `sources/vertraege.yaml` ist leer-Feed-Note). Skribble-API v2 (Release 25.06.2024) weiter aktiv. **Cosmi-Zustand gegenueber Skribble**: `backend/internal/vertraege/providers/skribble/` nicht angelegt, keine Adapter-Code, kein Webhook-Worker, keine `contract_signers`-Tabelle. **15 Wochen von W26-Zyklus-1-Pflicht-Pick-#1 absolut null Delivery**. Dies ist der wichtigste Pflicht-Posten dieses Berichts: entweder jetzt in KW42+KW43 der dedizierte 2-Sprint-Zyklus (siehe Empfehlung #1 unten), oder expliziter Scope-Cut und Alternative-Provider-Entscheidung (D-Trust, Swisscom, Yousign). **Markt-Erwartung fuer DACH-KMU-Vertrags-Software im Oktober 2026**: QES/AES-Integration ist Baseline-Erwartung, nicht Nice-to-have. Fuer Cosmi-vertraege standalone gegen fynk oder ContractHero ist das Fehlen eines eIDAS-Provider-Adapters der zentrale Verkaufs-Blocker.

**3. PandaDoc (international, threat: HIGH gestiegen — Pivot in DACH-KMU-30-100-Segment)**

- **DELTA seit W26 (W26-Report-Zustand: "Mid-Market-CLM-Veteran mit starkem AI-Contract-Review-Layer, primaer US-/EU-Cloud, Sales-Funnel-Native fuer Mid-Market")** — Launch **22.09.2026** von **"Contract Lifecycle Management Built for Growing Businesses"**: automatically-read-every-agreement + surface-what-needs-attention + ahead-of-renewals-obligations-next-steps. Zusaetzlich 22.09.2026 Workspace-Privacy-Settings-API (programmatic Privacy-Controls), 21.09.2026 Embedded-Editor-Alpha, Monatliches Changelog mit kontinuierlichen Fix+Feature-Releases. Dezember-2025-Leadership-Transition fuer "Accelerate Product Innovation for Small Businesses" — strategischer-Markt-Pivot ist 10 Monate alt und jetzt in Produkt-Delivery. **Konsequenz fuer Cosmi**: PandaDoc ist nicht mehr nur Enterprise-/Mid-Market-Konkurrent, sondern **direkter DACH-KMU-30-100-Konkurrent im gleichen Segment wie ContractHero + fynk**. Cosmi 2-50-Mitarbeiter-Overlap wird enger. Pricing-Baseline PandaDoc 2026: Free $0, Launch $9/User/Monat, Starter $19, **Business $49/User/Monat** (CRM-Integrations), Enterprise custom.

**4. Ironclad (international, threat: medium — bleibt Enterprise, aber Jurist-Redlining-GA ist Vorbild)**

- **DELTA seit W26 (W26-Report-Zustand: "Enterprise-CLM mit Acting-Capabilities Early-Access ab 15.04.2026, wichtiges Agentic-CLM-Vorbild, kein direkter DACH-KMU-Konkurrent")** — **Jurist Redlining Agent GA 30.04.2026**: generiert aus hochgeladener Playbook-Position first-pass-Redline fuer NDA/MSA/third-party-paper in Sekunden ("days to minutes" fuer Standard-Agreements). **State-of-AI-in-Legal-2026-Report** (Ironclad) als Marktbildungs-Content. **Mai 2026 Anthropic-Legal-Plugin-Partnership** mit offiziellem Claude-Connector fuer Ironclad. **Strategischer Hinweis-Update** (vs. W26): Cosmi-Roadmap-Vorbild bleibt gueltig fuer Renewal-Brief-Generator, aber Jurist-Redlining-Agent-Pattern (Playbook → Redline-Output) ist konkreter Blueprint fuer AI-Phase-2 — Cross-Modul-Hebel (Playbook via Wiki-Modul + Historie via CRM-Modul + Current-Period via Helpdesk) bleibt Cosmi-USP, aber nur wenn Phase-1 (Klausel-Extraction + Disclosure) sauber liefert.

**5. ContractHero (DACH, threat: HIGH — Preis-Erhoehung oeffnet Preis-Fenster, aber ISO-27001 bleibt)**

- **DELTA seit W26 (W26-Report-Zustand: "deutsche Firma, DE/CH-Hosting, ISO-27001, Essential 390 EUR/Monat als klein")** — Preis-Snapshot Oktober 2026: Essential bleibt **390 EUR/Monat Flat mit 500 Vertraege** (Volume-Erweiterung auf 500 nach frueherer 200-Vertrags-Grenze, aber Preis gleich). Essentials Vorgaenger-Preis **250 EUR/Monat** wurde zu 390 EUR angehoben = +56% fuer Pre-Preis-Kunden, mit Volume-Verdopplung. **Konsequenz fuer Cosmi**: ContractHero-ISO-27001 + DE/CH-Hosting bleibt der dominante Vertrauens-Anker, aber Preis-Verdopplung gegenueber Cosmi 2 EUR/User/Monat Modul-Preis macht Cosmi-Sales-Case leichter — bei 10-MA-Team: 10 × €2 = €20/Monat Modul-Preis vs. ContractHero €390/Monat = 19.5x Preis-Differenz. **Pflicht-Parity-Items fuer Cosmi gegen ContractHero**: AI-OCR + Klausel-Highlight + Volltext-Suche (W26-Pattern unveraendert), plus **ISO-27001-Zertifizierungs-Pfad** (nicht ContractHero-Match, sondern Cosmi-eigene Compliance-Zertifizierung als DACH-KMU-Vertrauens-Anker).

**6. fynk (Wien, threat: HIGH — Pricing-Pivot auf per-User macht Mikro-KMU-Konkurrenz schaerfer)**

- **DELTA seit W26 (W26-Report-Zustand: "Wiener Sitz, trusted.de-Testsieger 2026 Note 1.2, Essential 89 EUR/Monat Flat, Growth 249, Advanced 379")** — Pricing-Pivot zu per-User-Modell: **Essential €29/User/Monat monatlich oder €19/User/Monat jaehrlich, Business €49/User/Monat, Pro on request**. ISO-27001-zertifiziert, AWS-Frankfurt-Hosting, AI-Assistent-Erweiterung. **Konsequenz fuer Cosmi**: fynk hat seinen Preis dynamisiert — fuer 3-5-MA-Teams guenstiger (3 × €19 jaehrlich = €57 vs. frueher €89 flat), fuer 10+-MA-Teams teurer (10 × €19 = €190 vs. frueher €89). **Cosmi 2 EUR/User/Monat Modul bleibt deutlich unter fynk-€19-jaehrlich** — Preis-Hebel ist stabil, aber Feature-Hebel ist aus: fynk hat AI-Assistent, Cosmi hat null AI. **Pflicht-Parity-Items fuer Cosmi gegen fynk**: AI-Assistent-Minimal-Set (Klausel-Extraction + Renewal-Brief + Risiko-Flag mit Disclosure-Layer).

**7. HubSpot Revenue Hub (international, threat: HIGH — Pricing-Analyse jetzt verfuegbar, Bundle-Rabatt aktiv)**

- **DELTA seit W26 (W26-Report-Zustand: "GA 2026-06-22, Quotes+Vertraege+Billing+Payments+Breeze-AI im CRM-Hub, Pricing-Tier-Analyse angefordert")** — Oktober-Pricing-Snapshot (`monthly/2026-10-pricing.md`) hat erstmals vollstaendige Preise erfasst: Free €0, Starter €7/Seat/Monat, Professional €90/Seat/Monat, Enterprise €150/Seat/Monat. **Aktive Bundle-Promo "Buy Sales Hub, get Revenue Hub Professional €57/Seat/Monat (statt €95, −40%), Enterprise €98/Seat/Monat (statt €140, −30%)"** — HubSpot nutzt Revenue-Hub als Sales-Hub-Attach-Rate-Verstaerker. **Konsequenz fuer Cosmi**: HubSpot-Revenue-Hub-Pro-Preis ist 10-28x teurer als Cosmi-Modul-Summe (crm-core+vertraege+buchhaltung = 3-6 EUR/User/Monat), aber Feature-Luecke ist dort breiter (AI-Agents + Breeze + Quote-to-Cash-End-to-End). **Cosmi-Cross-Modul-USP-Rechnung** ist mathematisch stark, aber praktisch null-geliefert (vertraege-CRM-Linking Frontend-only, keine entity_links, keine Cross-Modul-RPCs). **Pflicht-Items fuer glaubwuerdigen Cross-Modul-Pitch**: Backend-Catch-Up-Sweep #2 (W26-Pick #2) fuer `vertraege_entity_links` als polymorphe Tabelle fuer Contact/Deal/Invoice/Project.

**8. Yousign (Frankreich/EU, threat: medium — EU-Sovereign-Alternative zu DocuSign, nicht in W26 im Vergleich)**

- **W26-Report hatte Yousign nicht gelistet** — EU-sovereigner e-Signatur-Provider mit eIDAS 2.0 EUDI-Wallet-Compliance-Blog-Content (yousign.com/blog/eidas-2-0-digital-identity-wallet-compliance-requirements). Yousign-API ist EU-Alternative zu DocuSign/Skribble, EU-Hosting als Baseline, QES-eIDAS-konform. **Konsequenz fuer Cosmi**: Yousign als zweiter Provider-Adapter nach Skribble erweitert die DACH-Kunden-Wahl (Skribble fuer CH+DE, Yousign fuer DE+AT+Frankreich+Benelux). Yousign-Partnership-Potential fuer Cosmi-Multi-Provider-Pattern.

---

## Cosmi-IST-Stand — Delta vs. W26

**Backend-Delivery-Delta (zwischen W26 und W41, Stand 2026-10-05):**

| Komponente | W26 (2026-06-22) | W41 (2026-10-05) | Delta |
|---|---|---|---|
| Production-LOC | 1277 | 1409 | +10% (+132 LOC) |
| Test-LOC | 1148 | 3104 | +170% (+1956 LOC) |
| Test-Ratio | 90% | **220%** | +130pp |
| RPCs | 15 | 16 | +1 (ListContractEvents) |
| Domain-Modelle | 3 (Contract/Party/Reminder) | 4 (+ ContractEvent) | +1 |
| Migrationen vertraege-direct | 3 (89, 90, 143) | 4 (+ 298 contract_events) | +1 |
| PDF-Renderer | TXT-Stub (TODO Sprint 3) | **Maroto/v2 A4 PDF** 163 LOC | ✅ ausgeliefert |
| Audit-Log | slog.Info only | **queryable `contract_events`-Tabelle** | ✅ ausgeliefert |
| Skribble-Provider | SignatureProvider-Stub | **unveraendert Stub** | ❌ null |
| contract_signers | fehlt | **fehlt** | ❌ null |
| contract_documents | fehlt | **fehlt** | ❌ null |
| vertraege_entity_links | fehlt | **fehlt** | ❌ null |
| ContractType-Deutsch-Migration | fehlt | **fehlt** | ❌ null |
| AI-Klausel-Extraction | fehlt | **fehlt** | ❌ null |
| ai_disclosure-Layer | fehlt | **fehlt** | ❌ null |
| ai_providers_router | fehlt (W23-W25-Keeper) | **fehlt** | ❌ null |
| MCP-Server | fehlt | **fehlt** | ❌ null |

**Frontend-Delivery-Delta (zwischen W26 und W41, Stand 2026-10-05):**

| Komponente | W26 (2026-06-22) | W41 (2026-10-05) | Delta |
|---|---|---|---|
| VertraegePage.tsx | 2417 LOC Mono | **2565 LOC Mono (+6%)** | 🔴 Refactor nicht ausgeliefert, weiter aufgefuellt |
| ESignaturDialog.tsx | 615 LOC | 615 LOC | unveraendert |
| stores/vertraege.ts | 848 LOC | 852 LOC | +4 LOC (marginal) |
| stores/vertraegePrefs.ts | 39 LOC | 92 LOC | +53 LOC |
| stores/vertraegeSettings.ts | 97 LOC | 97 LOC | unveraendert |
| api/vertraege-client.ts | 191 LOC | 193 LOC | marginal |
| api/vertraege-types.ts | 146 LOC | 146 LOC | unveraendert |
| api/vertraege-normalizer.ts | nicht erfasst | **154 LOC NEU** | ✅ Normalizer-Layer |
| useContractReminders.ts | vorhanden | vorhanden | unveraendert |
| Frontend-only Drift ContractType | `mietvertrag/liefervertrag/...` | **weiterhin `mietvertrag/liefervertrag/...`** im Store | ❌ Drift persistiert, aber API-Types matchen Backend-Werte |
| Frontend-only ContractSigner[] | Multi-Signer-UI mit Workflow | **unveraendert** | ❌ Backend-Catch-Up nicht geliefert |
| Frontend-only ContractDocument[] | Multi-Doc-UI | **unveraendert** | ❌ Backend-Catch-Up nicht geliefert |
| Frontend-only CRM-Links | contactId/dealId/invoiceIds | **unveraendert** | ❌ entity_links fehlt |
| Frontend-only ContractTemplate-Mock | MOCK_TEMPLATES | **unveraendert** | ❌ Template-Backend fehlt |
| Frontend-only History-Codes | 12 Action-Codes | **unveraendert** | ⚠️ Backend hat jetzt 6 Codes (contract_events), aber Frontend-Codes != Backend-Codes |

**Positive Delta — was Cosmi-vertraege HEUTE besser hat als W26:**

1. **PDF-Renderer in Production-Grade** — Maroto/v2 statt TXT, A4 mit korrekter deutscher Status-/Type-Lokalisation (`Entwurf/Aktiv/Abgelaufen/Gekuendigt`, `Miete/Dienstleistung/Arbeitsvertrag/Geheimhaltung/Sonstiges`), Auto-Row-Heights fuer page-break-safe-text, Signatur-Line (`Unterschrift: ausstehend` / `Unterschrieben von X am DD.MM.YYYY HH:MM`), Notes-Paragraph-Splitting fuer multi-line-wrapping. **Fehlt**: Signatur-Image-Embedding in PDF (W26-"lean: no image embedding, add when customer asks" ist konsistent). **Vorteil gegenueber W26**: Skribble-Integration kann jetzt PDF-Input nutzen statt TXT-Stub.

2. **Audit-Log queryable** — Migration 000298 `contract_events` als append-only Trail mit TEXT-Action (6 Werte closed Go-const-Set) + JSONB-Payload + nullable UserID (fuer Worker-Mutations) + ON DELETE SET NULL (Trail ueberlebt User-Loeschung) + Tenant-RLS + Index auf `(tenant_id, contract_id, created_at DESC)` fuer "contracts newest-first paginiert". **Fehlt**: Event-Codes fuer `document_added/removed/contact_linked/unlinked/deal_linked/unlinked/invoice_linked/unlinked/reminder_triggered` (Frontend hat 12 Codes, Backend 6) — Mapping-Taktik: entweder Frontend-Codes auf Backend-6 reduzieren oder Backend-Set erweitern. **Vorteil gegenueber W26**: Cross-Modul-Audit-Trail-Pattern ist jetzt im vertraege-Modul etabliert und kann als Blueprint fuer wiki_events, formulare_events, etc. dienen.

3. **Test-Investment massiv** — Test-Ratio 220% ist hoehste aller 2026-Deepdive-Module. Breakdown: `postgres_repository_db_test.go` 1162 LOC Integration-Tests (echte DB-Interaktion statt Mocks — folgt W40-formulare-Pattern), `service_test.go` 819 LOC Service-Layer-Tests, `contract_events_test.go` 365 LOC Audit-Trail-Tests, `worker_test.go` 206 LOC, `signature_test.go` 141 LOC, `tenant_isolation_phase2_test.go` 75 LOC Cross-Tenant-Verweigerung, `tenant_write_test.go` 97 LOC Write-Permission-Checks. **Konsequenz**: Vertraege-Modul ist refactoring-safe und regression-safe — alle Pflicht-Items unten koennen aggressiv ausgeliefert werden, ohne Test-Risiko.

4. **Normalizer-Layer** `api/vertraege-normalizer.ts` 154 LOC — API-Response → Store-Model-Normalisierung als dedizierte Schicht (W25-formulare-Normalizer-Pattern auf vertraege uebertragen). Reduziert Mapping-Code in VertraegePage.tsx.

**Negativ-Delta — was W26-Diagnose noch gilt oder sich verschaerft hat:**

1. **VertraegePage.tsx 2417 → 2565 LOC (+6%)** — Mono-File-Refactor-Empfehlung aus W26 nicht ausgeliefert. **Delivery-Pattern-Wiederholung** vs. formulare W40 (FormularePage 2457 → 5605 LOC in 12 Wochen = +128%): das Modul-Team baut Features in bestehende Mono-File statt in neue Komponenten. Cosmi-Frontend-Hygiene-Pattern waechst zu dauerhaftem Schulden-Posten.

2. **ContractType-Drift zwischen stores und api** — stores/vertraege.ts:58 nutzt deutsche Werte (`mietvertrag/liefervertrag/servicevertrag/arbeitsvertrag/lizenz/versicherung`), api/vertraege-types.ts:12 nutzt Backend-5-Werte (`rental/service/employment/nda/other`). **Normalizer muesste Mapping durchfuehren**, aber die zwei Enums sind nicht 1:1 abbildbar (deutsche 6 Werte, Backend 5, `liefervertrag` und `versicherung` haben keine Backend-Repraesentation). Backend-Migration auf deutsche Werte (W26-Empfehlung 2a) steht aus — alternativ: Backend-Enum erweitern um `delivery` + `insurance` + `license` statt `other`.

3. **Vier Frontend-only-Features persistieren**: ContractSigner[]-Multi-Signer-Workflow (`stores/vertraege.ts:177-185` mit `updateSigners/dispatchSigners`), ContractDocument[]-Multi-Doc (`stores/vertraege.ts:68`), CRM-Links (`contactId/dealId/invoiceIds` ab Zeile 76-82), ContractTemplate-Mock (unveraendert). **Reload-Risiko**: ohne Backend-Persistierung geht State bei Nicht-Persist-Store-Reset verloren.

4. **AI-Compliance-Foundation komplett null** — in 15 Wochen hat kein anderes Modul in Cosmi einen `backend/internal/compliance/ai_disclosure/`-Layer gebaut (W37-video-Deepdive-P0 unveraendert, W39-helpdesk-Deepdive-P0 unveraendert, W40-formulare-Deepdive-P0 unveraendert). **Dies ist nicht nur vertraege-Problem, sondern Cosmi-weites P0-Problem**, aber vertraege-AI-Phase-1-Sprint ohne Disclosure-Layer wuerde die cosmi-weit laufende Non-Compliance verschaerfen. Pflicht: Disclosure-Layer als cosmi-weiter Baustein VOR vertraege-AI-Phase-1 (Cross-Modul-Pflicht-Reihenfolge).

5. **MCP-Server null — und Markt ist waehrenddessen 4 CLM-MCP-Server ausgereift**. Dieses Delta ist das wichtigste neue Posten dieses Berichts (vgl. Empfehlung #3 unten).

---

## Konkurrenz-Vergleichstabelle — Delta-Markiert

**Legende**: ✅ vorhanden / 🚧 partial / ❌ fehlt / ⚠️ konditional / 🆕 Delta ggue. W26 / ⬆️ gestiegen seit W26 / ⬇️ gefallen seit W26

| Feature | Cosmi-vertraege (W41) | W26→W41 | DocuSign IAM | Skribble | PandaDoc | Ironclad | ContractHero | fynk | HubSpot Rev-Hub | Yousign |
|---|---|---|---|---|---|---|---|---|---|---|
| Contract-CRUD | ✅ | — | ✅ | ❌ (kein CLM) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Party-Mgmt | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reminder-Engine | ✅ Atomic-Claim | — | ✅ Iris-Agent | 🚧 Email-Only | ✅ 🆕 CLM-Growing-Biz | ✅ Renewal-Agent | ✅ | ✅ | ✅ Revenue-Agent | ✅ |
| Auto-Expiry | ✅ | — | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EES Inline (Canvas) | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **QES/AES eIDAS** | ❌ (Stub) | ❌ null-Delta | ✅ multi-QTSP | ✅ DE+CH Dual | ⚠️ via Partner | ✅ multi-QTSP | ✅ | ✅ | ⚠️ HelloSign-Integration | ✅ EU-QES-nativ |
| **EUDI-Wallet (24.12.2026)** | ❌ | ❌ null-Delta | 🚧 angekuendigt | 🚧 angekuendigt | 🚧 | 🚧 | 🚧 | 🚧 | 🚧 | ✅ EUDI-Compliance-Blog + Rollout angekuendigt |
| **Audit-Log (queryable)** | ✅ 🆕 | ✅ ausgeliefert! | ✅ | ✅ | ✅ | ✅ | ✅ ISO-27001 | ✅ | ✅ | ✅ |
| **PDF-Renderer (Server)** | ✅ 🆕 Maroto/v2 | ✅ ausgeliefert! | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Signer-Workflow (Backend) | 🚧 (Frontend-only) | ❌ null-Delta | ✅ | ✅ Order + Status | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Document-Anhang (Backend) | 🚧 (Frontend-only) | ❌ null-Delta | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI-Klausel-Extraction** | ❌ | ❌ null-Delta | ✅ Iris | ❌ | ✅ 🆕 CLM-Growing-Biz | ✅ Jurist | ✅ OCR+Highlight | ✅ | ✅ Breeze | 🚧 |
| **AI-Risk/Anomaly-Flag** | ❌ | ❌ null-Delta | ✅ Iris AI-Review | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ | 🚧 |
| **AI-Klausel-Drafting (Chat)** | ❌ | ❌ null-Delta | ✅ Iris Chat + In-Canvas 🆕 | ❌ | ✅ | ✅ | ❌ | 🚧 | ✅ Breeze | ❌ |
| **AI-Renewal-Brief-Generator** | ❌ | ❌ null-Delta | ✅ Iris Renewal-Agent ⬆️ GA | ❌ | ✅ 🆕 CLM-Growing-Biz | ✅ Renewal-Agent | ❌ | ❌ | ✅ | ❌ |
| **AI-Cost-Savings-Agent** | ❌ | ❌ null-Delta | 🚧 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **AI-Archive-Agent (OCR-Ingest)** | ❌ | ❌ null-Delta | ✅ | ❌ | ✅ 🆕 CLM-Growing-Biz | ✅ | ✅ AI-OCR | ✅ | ✅ | 🚧 |
| **AI-Playbook-Redlining** | ❌ | ❌ null-Delta | ✅ Smart-Redline + In-Canvas 🆕 | ❌ | ✅ | ✅ **Jurist GA 30.04.2026** 🆕 | ❌ | 🚧 | ✅ | ❌ |
| **AI-Plain-Lang-Signer-Summary** | ❌ | ❌ null-Delta | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Contract-Templates | 🚧 (Frontend-Mock) | ❌ null-Delta | ✅ 100+ | ❌ | ✅ 750+ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **EU-MCT-/SCC-Klausel-Library** | ❌ | ❌ null-Delta | 🚧 | ❌ | ❌ | 🚧 | ❌ | ❌ | ❌ | 🚧 |
| Bulk-Contract-Generation | ❌ | ❌ null-Delta | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Approval-Chain | ❌ | ❌ null-Delta | ✅ | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ | 🚧 |
| Negotiation/Redlining | ❌ | ❌ null-Delta | ✅ Smart-Redline + In-Canvas 🆕 | ❌ | ✅ | ✅ | 🚧 | ✅ | ✅ | ❌ |
| Renewal-Dashboard | 🚧 (Frontend-View) | ❌ null-Delta | ✅ | ❌ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **AI-Workflow-Builder** | ❌ | ❌ null-Delta | ✅ 🆕 Quickstart-Skeleton + In-Canvas-Conv Oct 15 2026 | ❌ | 🚧 | ✅ | ❌ | 🚧 | ✅ | ❌ |
| CRM-Linking (Backend) | 🚧 (Frontend-only) | ❌ null-Delta | ✅ Salesforce-Native | 🚧 Connector | ✅ HubSpot/SF/PD | ✅ Salesforce | 🚧 | ✅ | ✅ Native | 🚧 |
| **MCP-Server (AI-Agent-API)** | ❌ | ❌ **null-Delta waehrend Markt 4 MCPs ausgeliefert hat** | ✅ **GA 30.09.2026** 🆕⬆️ | ❌ | ✅ 🆕 (im CLM-Growing-Biz-Launch) | 🚧 Anthropic-Legal-Connector offiziell 🆕 | ❌ | ❌ | 🚧 | ❌ |
| **Anthropic-Claude-Connector offiziell** | ❌ | ❌ null-Delta | ✅ (Mai 2026) 🆕 | ❌ | ❌ | ✅ Anthropic-Partner (Mai 2026) 🆕 | ❌ | ❌ | ❌ | ❌ |
| Cross-Modul-Hebel (Helpdesk/Wiki/CRM) | 🚧 (Frontend-only) | ❌ null-Delta | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ HubSpot-Hub | ❌ |
| Self-Host-Pfad | ✅ (Modul-Flag) | — | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| EU-DE-/CH-Hosting-Only | ✅ | — | ⚠️ optional | ✅ DE+CH dual | ⚠️ optional | ⚠️ optional | ✅ DE | ✅ Wien AWS Frankfurt | ⚠️ optional | ✅ EU |
| ISO-27001-Zertifizierung | ❌ | ❌ null-Delta | ✅ | 🚧 | ✅ | ✅ | ✅ (Vertrauens-Anker) | ✅ 🆕 (Pricing-Pivot-Begleitung) | ✅ | 🚧 |
| Free-Tier | ❌ (Modul-Pricing) | — | ❌ | ⚠️ 2 sig/Monat | ✅ Limited | ❌ | ❌ | ✅ Basic | ✅ Basis-Invoicing | ⚠️ |
| KMU-Sweet-Spot (2-50 MA) | ✅ 2 EUR/User/Mo | — | ❌ ($10-15+) | ⚠️ CHF 9 + Usage | ⚠️ $9-49 (Growing-Biz Target 🆕) | ❌ Enterprise | ❌ 390 EUR/Mo Flat | ✅ €19-29/User/Mo 🆕 | ⚠️ Free + Lock-in oder €7+/Seat | ⚠️ |

**Stake-Lesart (vs. W26)**: W26 hatte "8 von 32 Feature-Zeilen voll und 6 partial". W41 hat **10 voll + 7 partial** von jetzt 36 Zeilen — zwei neue Volle (PDF-Renderer, Audit-Log), eine neue Partial-Zeile (Normalizer-Layer indirekt). Konkurrenz-Durchschnitt bleibt bei **22-30 voll**. **Die neue strukturelle Luecke**: MCP-Server-Zeile hat sich von "nice-to-have-fuer-alle" zu "Table-Stakes-mit-DocuSign-GA-30.09.2026" verschoben. **Die neue strukturelle Chance**: EU-DE-/CH-Hosting + Self-Host-Pfad + ISO-27001-Weg bleibt differenziert, Yousign ist einziger neu-im-Vergleich-aufgenommener EU-Sovereign-Alternativ-Provider.

---

## Top-3 Strategische Empfehlungen (W41)

### 1. 🟢 **Skribble-Provider-Integration als KW42+KW43-Zwei-Sprint-Pflicht — oder Scope-Cut mit Alternativ-Provider-Entscheidung**

**Was**: W26-Pick #1 ist 15 Wochen null-geliefert — jetzt ist Entscheidung faellig: entweder **(a) Durchzug** mit dedizierten 2-Sprint-Zyklus KW42-KW43 (siehe W26-Empfehlung Detailplan: `backend/internal/vertraege/providers/skribble/` + Migration 0225 `contract_signers` + 5 neue RPCs `RequestSignature/GetSignatureStatus/HandleProviderCallback/CreateSigner/UpdateSignerStatus` + `SignatureWebhookWorker`), **oder (b) Scope-Cut** mit expliziter Alternative-Provider-Entscheidung (D-Trust/Bundesdruckerei fuer DE-Only-Customer, Swisscom fuer CH-Only-Customer, **Yousign** als EU-Sovereign-Alternative die in W26-Report fehlte und EUDIW-Compliance-Blog aktiv publisht), **oder (c) Priorisierungs-Shift** auf MCP-Server (Empfehlung #3 unten) als strategischer-Hebel-mit-hoeherer-Marktvisibilitaet.

**Warum (verschaerft seit W26)**: (a) Marktentwicklung hat die eIDAS-QES-Integration zur **Baseline-Erwartung fuer DACH-KMU-Vertrags-Software im Oktober 2026** gemacht — Skribble selbst zeigt Produkt-Fortschritt (API v2 aktiv), aber Cosmi-Delivery ist null. (b) **DIdG-Expertenanhörung MORGEN 06.10.2026** + EUDI-Wallet-Deadline **80 Tage** (24.12.2026) + DE-EUDIW-Rollout Q1 2027 bedeutet: wer in Q4 2026 keinen eIDAS-Provider ausgeliefert hat, bleibt in Q1 2027 ohne EUDIW-Readiness-Marketing-Signal. (c) **BGH-Rechtsprechung-2026 (VII ZB 29/24, Mai-beA-qeS-Entscheidung)** verschaerft Nachweispflicht fuer QES-Verfahren im Audit-Log — Cosmi-Audit-Log hat jetzt zwar Backend-Persistierung (`contract_events`), aber ohne Provider-Trace-Daten im JSONB-Payload (QTSP, Identifikationsstufe, Format) ist der Audit nicht Cross-Border-anerkennungsfaehig. (d) Pricing-Verschiebung bei fynk auf per-User (€19 jaehrlich) und ContractHero (€390 flat) macht Cosmi-Preis-Narrative "20 EUR/Monat statt 190 EUR/Monat" wettbewerbs-stark, aber nur mit QES-Baseline. **Scope-Cut-Alternative (b)** ist akzeptabel wenn Yousign-API-Analyse zeigt dass Yousign-Integration einfacher ist (reine EU-Sovereign-Fit statt DE+CH-Dual-Regime wie Skribble, EUDIW-Compliance-Blog-aktiv).

**Kosten/Aufwand**: 2 Sprints (KW42-KW43, 10 Werktage) fuer Skribble-Pfad; alternativ 1.5 Sprints fuer Yousign-Pfad (einfachere EU-Mono-Regime); 0 Sprints fuer Pfad (c) MCP-Prio-Shift mit expliziter Reihenfolge *"MCP-Server zuerst, Provider-Adapter danach"*.

### 2. 🟢 **AI-Compliance-Foundation-Sprint als Cosmi-weite Pflicht — vertraege als zweiter Konsument nach video**

**Was**: Ein **cosmi-weiter Dreier-Sprint-Baustein** (nicht vertraege-only), ausgeliefert in KW42-KW45 (4 Wochen): (i) **`backend/internal/ai/providers/router/`** als Multi-Provider-Interface (Anthropic Primary + Mistral Fallback wegen W23/W25-Keeper-Anthropic-Lockdown-Lehre, plus Local-Ollama-Pfad fuer EU-Self-Host-Deployments, plus LiteLLM-als-moegliche-Abstraction) mit Audit-Trail (Provider/Modell/Prompt-Version/Costs/Timestamps); (ii) **`backend/internal/compliance/ai_disclosure/`** als cosmi-weiter Baustein fuer Article-50-Disclosure-UI-Pattern mit Machine-Readable-Marking (SynthID-Text ODER C2PA — zwei konforme Ansaetze pro `daily/2026-10-03-regulation.md`), Human-in-the-Loop-Validierung (3-Fragen-Test aus `daily/2026-10-02-evening.md`: Stopp-Autoritaet + Output-Edit + Protokollierung), Stop-Autoritaet-UI-Control (nicht nur Backend-Setting), AI-Provider-Trace im Audit-Log; (iii) **vertraege-AI-Phase-1** als zweiter Konsument nach **video-Modul-Backfill** (W37-video-Deepdive-P0 "Meeting-AI-Summary ohne Disclosure seit 02.08.2026" muss vor Grace-Period-Ende 02.12.2026 saniert sein — 58 Tage) — konkret `ClauseExtractionAgent` (PDF → OCR → Embed → Classify → Store in `contract_clauses`-Tabelle) + `RenewalBriefAgent` (Worker-Erweiterung generiert 3-Saetze-Brief: Vertrags-Content, Cross-Modul-Kontext von CRM+Helpdesk+Buchhaltung, Empfehlung).

**Warum (verschaerft seit W26)**: (a) **EU-AI-Act Art. 50 ist seit 2026-08-02 live-enforcement = heute Tag 64**, mit **58-Tage-Grace-Period fuer Machine-Readable-Marking** (bis 2026-12-02). Bussgeld bis €15 Mio oder 3% Welt-Umsatz, Enforcement durch nationale Market-Surveillance-Authorities. Cosmi-video-Modul laeuft seit 64 Tagen in Live-Non-Compliance (Meeting-AI-Summary ohne Disclosure) — **vertraege ist das zweite Modul, das AI-Features liefern will und darf das nicht ohne Disclosure-Layer tun**. (b) Markt-Erwartung ist in Oktober 2026 brachialer als in Juni: DocuSign Iris + Ironclad Jurist Redlining GA + PandaDoc CLM Growing-Biz Launch + fynk AI-Assistent — **Cosmi-vertraege ohne AI in 12 Monaten = "Aktenordner-digital"-Wahrnehmung** (W26-Prognose bestaetigt sich). (c) **Compliance-Foundation ist nicht vertraege-only Investment**, sondern Pflicht-Baustein fuer helpdesk-AI-Drafts (W39-Deepdive-P0), formulare-AI-Validation (W40-Deepdive-P0), crm-core-AI-Lead-Scoring etc. — der cross-modul-Baustein amortisiert sich 5x. (d) **Keeper-Cross-Reference W25 Anthropic-Kill-Switch** macht Provider-Router zur strategischen-Pflicht, nicht nur Compliance-Pflicht. **Keeper-Cross W23 AI-Cost-Governance** macht Audit-Trail-Dashboard zur Verkaufs-Doktrin. Beide Keeper sind seit Juni-W23 offen und werden mit AI-Compliance-Foundation-Sprint operationalisiert.

**Kosten/Aufwand**: 4 Wochen Cosmi-weiter Sprint (KW42-KW45): **1 Woche Provider-Router + Audit-Log-Schema** (Router-Interface, Anthropic-Impl, Mistral-Impl, Audit-DB-Migration), **1 Woche Disclosure-UI-Pattern + Machine-Readable-Marking** (UI-Components, SynthID-Text-Integration, Human-in-the-Loop-Gates mit 3-Fragen-Test-Compliance), **1 Woche video-Modul-Backfill** (Meeting-AI-Summary mit Disclosure retrofitten vor Grace-Period-Ende 02.12.2026), **1 Woche vertraege-AI-Phase-1-Minimal** (ClauseExtractionAgent fuer Top-5-Klauseln + RenewalBriefAgent als Reminder-Worker-Erweiterung). **Downstream-Payoff**: helpdesk-AI-Drafts + formulare-AI-Validation + crm-core-AI-Features koennen danach OHNE eigenen Compliance-Sprint ausgeliefert werden — 5x Modul-Amortisation.

### 3. 🟢 **Cosmi-vertraege-MCP-Server als strategisches Marktvisibilitaets-Signal — 2-Wochen-Sprint parallel zu Empfehlung #2**

**Was**: Ein dedizierter **Cosmi-MCP-Server** (`cosmi-vertraege-mcp` als npm-Paket oder `cosmi-mcp` als Cross-Modul-Server mit Vertraege-Tool-Set), der die 16 bestehenden Vertraege-RPCs als MCP-Tools exposed: `cosmi-contract-create`, `cosmi-contract-list`, `cosmi-contract-get`, `cosmi-contract-update`, `cosmi-contract-delete`, `cosmi-contract-export-pdf` (nutzt PDF-Renderer!), `cosmi-contract-add-party`, `cosmi-contract-remove-party`, `cosmi-contract-list-parties`, `cosmi-contract-create-reminder`, `cosmi-contract-update-reminder`, `cosmi-contract-list-reminders`, `cosmi-contract-save-signature`, `cosmi-contract-list-events` (nutzt Audit-Log!) + eine **Cross-Modul-Query-Variante** `cosmi-contact-contracts` (list contracts where contact is party — nutzt ContactID-Filter aus `ListContractsInput`). **Dann publish als npm-Paket + Claude-/ChatGPT-/Gemini-Directory-Submission** parallel zu Marketing-Blog "Cosmi-Vertraege via Claude-Chat".

**Warum (neuer Pflicht-Punkt seit W26, nicht in W26-Priorisierung)**: (a) **DocuSign MCP-Server GA 30.09.2026 (vor 5 Tagen)** macht MCP-Server-Verfuegbarkeit zu Markt-Table-Stake fuer AI-affine Legal-Teams — Concord + DocuSign + SpotDraft + PandaDoc + Anthropic-Legal-Plugins (Ironclad, DocuSign-CLM, Definely) sind alle veroeffentlicht. **Cosmi-vertraege ist nicht aufgerufen, waehrend der Markt Standard-Vereinheitlichung schon durchzieht**. (b) **MCP-Server ist der sichtbarste Hebel fuer Cosmi-Cross-Modul-USP**: ein KMU-Entscheider der Claude fragt "zeige mir alle meine Vertraege mit Kontakt X die in den letzten 3 Monaten geaendert wurden" kann mit Cosmi-MCP-Server den `cosmi-contact-contracts`-Tool + `cosmi-contract-list-events`-Tool kombinieren — DocuSign-MCP kann das nicht, weil DocuSign kein eigenes CRM-Modul hat. Dies ist der konkreteste Hebel fuer Cross-Modul-Narrativ. (c) **Technisch ist Cosmi gut aufgestellt**: 16 Backend-RPCs sind gRPC-definiert, Service-Layer ist gereift (579 LOC + 819 LOC Tests), PDF-Renderer liefert PDF-Bytes fuer Agent-Workflows, Audit-Log ist queryable fuer Trail-Queries. Der MCP-Server ist dann ein REST-/JSON-RPC-Wrapper um bestehende Grpc-Calls — kein neuer Domain-Code noetig. (d) **Marketing-Signal**: Cosmi als "KMU-ERP mit MCP-Server fuer vertraege+crm+helpdesk+wiki+buchhaltung" ist konkreter Content-Hook fuer AEO-Vertriebskanal (W23-Keeper), DACH-Public-Sector-Beschaffung (CADA-W23-Keeper), AI-governance-Narrativ (W23-Keeper + W31-Live-Realitaet).

**Kosten/Aufwand**: 2 Wochen (KW44-KW45 parallel zu Empfehlung #2) — **Woche 1**: MCP-Server-Scaffold als `backend/mcp/cosmi-mcp-server/` oder getrennt als `desktop/src-mcp/` je nach Deployment-Pattern, Tool-Signaturen fuer 15 Vertraege-Tools, Auth via existing Tenant-API-Token, JSON-Response-Schemas. **Woche 2**: Cross-Modul-Query-Tools (`cosmi-contact-contracts`, `cosmi-contract-related-helpdesk-tickets` nutzend entity_links sobald vorhanden), npm-Publish, Claude-Directory-Submit, Marketing-Blog + AEO-Content. **Downstream-Payoff**: Modul-Pattern fuer helpdesk-MCP (W39-Deepdive-P0, 6+ Wochen unresolved), formulare-MCP (W40-Deepdive-P0, 15 Wochen unresolved), crm-core-MCP, wiki-MCP — Blaupause fuer 5-weitere-Module-MCP-Rollout mit je 1-Woche-Sprint.

---

## Zwei Komprimierungs-Entscheidungen

**(K1) Backend-Catch-Up-Sweep aus W26-Pick #2 reduzieren auf 2 Migrationen statt 4.**

W26 hat vier Migrationen vorgeschlagen (0226 ContractType-Deutsch, 0227 contract_documents, 0228 vertraege_entity_links, 0229 contract_history). Da **contract_history durch Migration 000298 contract_events bereits geliefert** ist, reduziert sich der Sweep auf drei. **Vorschlag**: nur **zwei Migrationen** als MVP ausliefern: **Migration 0300 vertraege_entity_links** (polymorph fuer Contact/Deal/Invoice/Company/Project — unverzichtbar fuer Cross-Modul-USP + MCP-Server-Cross-Modul-Query-Tool) + **Migration 0301 contract_signers** (unverzichtbar fuer Multi-Signer-Backend als Voraussetzung fuer Skribble-Integration ODER Yousign-Integration). ContractType-Deutsch-Migration kann via Normalizer-Layer-Mapping im api/vertraege-normalizer.ts geloest werden (keine Backend-Breaking-Change). contract_documents kann als Phase-2-Sprint-Item nachgezogen werden, wenn Multi-Doc kein Live-Blocker ist (Frontend-only-State ueberlebt mit persist-Store, Reload-Verlust ist akzeptabler Compromise).

**(K2) VertraegePage.tsx-Mono-File-Refactor als dedizierter Sprint vor jedem naechsten UI-Feature.**

Delivery-Pattern von W40 (formulare FormularePage 2457→5605 LOC +128%) zeigt dass Mono-File-Refactor nicht nebenbei passiert, sondern explizit priorisiert werden muss. **Vorschlag**: VertraegePage.tsx 2565 LOC Refactor als dedizierter 1-Sprint-Posten in KW46 (nach Compliance-Foundation + MCP-Server), aufgeteilt in `<ContractList>` (max 400 LOC), `<ContractDetail>` (max 600 LOC), `<ContractTimeline>` nutzt Audit-Log (max 300 LOC), `<ContractActions>` (max 400 LOC), `<ContractReminderPanel>` (max 300 LOC), Rest-Store-Zugriff. **Alternative**: Mono-File akzeptieren, aber Pflicht-TODO-Marker im File-Header dokumentieren und Delivery-Divergenz-Keeper publishen.

---

## Picks (vorgeschlagen)

[ ] 🟢 **Skribble-Provider-Integration KW42-KW43 2-Sprint-Zyklus** (W26-Pick-#1 15 Wochen unerledigt — Pflicht-Entscheidung ueber (a) Durchzug, (b) Yousign-Scope-Cut, (c) MCP-Prio-Shift). Decision-Owner: Product + Legal + Engineering-Lead vertraege-Modul.

[ ] 🟢 **AI-Compliance-Foundation-Sprint KW42-KW45 Cosmi-weit** (Provider-Router + Disclosure-Layer + Machine-Readable-Marking + video-Backfill + vertraege-AI-Phase-1-Minimal). Decision-Owner: Chief-Compliance + CTO + Platform-Team. Grace-Period-Ende 2026-12-02 = 58 Tage.

[ ] 🟢 **Cosmi-vertraege-MCP-Server KW44-KW45 Parallel-Sprint** (16 RPCs als MCP-Tools + Cross-Modul-Query-Tool + npm-Publish + Claude-Directory-Submit). Decision-Owner: Platform-Team + Marketing/AEO-Lead. Erster Modul-MCP als Blaupause fuer 5-Module-Rollout.

[ ] 🟢 **Migration 0300 vertraege_entity_links KW42** (polymorphe Tabelle Contact/Deal/Invoice/Company/Project — Voraussetzung fuer MCP-Cross-Modul-Query-Tool + Cross-Modul-USP-Realisierung).

[ ] 🟢 **Migration 0301 contract_signers KW42** (Multi-Signer-Backend als Voraussetzung fuer eIDAS-Provider-Adapter — Skribble oder Yousign).

[ ] 🟡 **ContractType-Deutsch-Mapping via Normalizer** KW43 (Normalizer-Layer in `api/vertraege-normalizer.ts` erweitern — kein Backend-Breaking-Change, Store-Werte bleiben, Backend-Werte bleiben, Mapping dazwischen).

[ ] 🟡 **VertraegePage.tsx 2565 LOC Mono-File-Refactor** KW46 (dedizierter Sprint nach Compliance-Foundation + MCP-Server, aufgeteilt in 5 Komponenten). Alternativ: Delivery-Divergenz-Keeper publishen und Mono-File explizit akzeptieren.

[ ] 🟡 **EU-MCT-/SCC-Klausel-Library als Standard-Template-Bibliothek** KW47+ (nach AI-Compliance-Foundation und ClauseExtractionAgent — EU-Data-Act-Compliance-Hebel). EU-Expert-Group-Report 02.04.2025 als Quelle. **Cosmi-Differenzierungs-Anker**: keine US-CLM-Software hat EU-MCTs vorinstalliert.

[ ] 🟡 **EUDI-Wallet-eIDAS-Modul-Scaffold** `backend/internal/vertraege/eidas/eudi-wallet-prep/` KW48-KW50 (nach DIdG-Expertenanhörung-Output-Review in KW42, vor Grace-Period-Ende 24.12.2026 = 80 Tage). Followup aus `daily/2026-10-03-regulation.md` Pflicht-TODO.

[ ] 🟡 **Followup 30d (KW45): Ghostscript-Dependency-Audit** auf `backend/internal/vertraege/pdf.go` (Maroto/v2 ist Go-nativ, kein direkter Ghostscript-Call, aber Pflicht-Verifikation auf transitive Deps + buchhaltung-pdf-Pipeline). BSI 30.09.2026 HOCH.

[ ] 🟡 **Followup 30d (KW45): DocuSign Workflow-Builder 26.3.00.00 Analyse** (Target-Prod 15.10.2026 = 10 Tage, Quickstart-Skeleton-Generation + In-Canvas-Conversational-Building). Signal-Monitor fuer Cosmi-AI-Phase-2-Roadmap (nach Phase-1).

[ ] 🟡 **Followup 30d (KW45): PandaDoc-CLM-Growing-Businesses-Preis-Analyse** (nicht in Oktober-Pricing-Snapshot erfasst — Growing-Businesses-Tier-Preis unbekannt, Cosmi-Preis-Narrativ-Baseline unvollstaendig).

[ ] 🔵 **Inspire: Yousign-EUDIW-Compliance-Blog als Pattern-Studie** (EU-Sovereign-Positionierung — Cosmi-Marketing-Blog "EU-Vertraege-Software mit EUDI-Readiness" basiert auf gleicher Narrativ-Logik).

[ ] 🔵 **Inspire: Ironclad-State-of-AI-in-Legal-2026-Report** (Marktbildungs-Content fuer AEO-Vertriebskanal — DACH-Pendant publishen "State-of-AI-in-Vertrags-Management-DACH-2026").

[ ] 🔴 **Dismiss: W26-Pick #6 PDF-Renderer-Sprint-3-Gotenberg-Empfehlung** — Maroto/v2 ist ausgeliefert, Gotenberg-Container-Service nicht noetig. Scope-Entscheidung sauber.

---

## Quellen

**EU-Regulatorik (Delta-Anker 2026-10):**

- [EU AI Act Article 50 Transparency Obligations Go Live — Baker Botts (September 2026)](https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live)
- [EU AI Act Article 50: Already in Force, Not Delayed — Elevate Consulting](https://elevateconsult.com/insights/eu-ai-act-article-50-icp-impact/)
- [EU AI Act Article 50 — Transparency obligations FAQ — EU Commission](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- [EU AI Act Article 50 Compliance Checklist — ProofSnap](https://getproofsnap.com/eu-ai-act-deadline.html)
- [EU AI Act Article 50 Disclosure Guide 2026 — LikeOne](https://likeone.ai/blog/eu-ai-act-article-50-transparency-disclosure-guide-2026/)
- [EU AI Act 2026: Deadlines, Penalties & Checklist — Decode the Future](https://decodethefuture.org/en/eu-ai-act-explained/)
- [EU Data Act in practice — Taylor Wessing (Model Contractual Terms)](https://www.taylorwessing.com/en/global-data-hub/2025/eu-data-act---understanding-the-issues/gdh---the-eu-data-act-in-practice)
- [EU Data Act — Model Contract Terms and Standard Clauses — BCLP](https://www.bclplaw.com/en-US/events-insights-news/eu-data-act-new-model-contract-terms-and-standard-clauses-to-facilitate-data-sharing-and-cloud-switching.html)
- [EU Data Act — New unfair contractual terms in B2B — Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/eu-data-act--new-unfair-contractual-terms-in-business-to-business-data-sharing-agreements/)
- [YPOG — EU Data Act Expert Report Templates for Data and Cloud Contracts](https://www.ypog.law/en/insight/data-act-update-eu-expert-report-provides-templates-for-data-and-cloud-contracts-as-guidance)
- [EU Digital Identity Wallet (EUDI) Regulation — EU Commission](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation)
- [eIDAS 2.0 EUDI Wallet Integration Guide for 2026 — Notixit](https://www.notixit.com/blog/government-eidas2-eudi-wallet-integration-guide)
- [Yousign — eIDAS 2.0 Digital Identity Wallet Compliance 2026](https://yousign.com/blog/eidas-2-0-digital-identity-wallet-compliance-requirements)
- [DIdG Expertenanhörung Bundestag Ausschuss Digitales 06.10.2026](https://www.bundestag.de/ausschuesse/a23_digitales_staatsmodernisierung/anhoerungen/1216764-1216764)

**DACH-Rechtsprechung 2026 (Delta-Anker — korrigierte Aktenzeichen):**

- [BGH 25.02.2026 VII ZB 29/24 — Qualifizierte Elektronische Signatur Mahnverfahren — dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.02.2026&Aktenzeichen=VII+ZB+29%2F24)
- [BGH Mai 2026 — beA ohne qeS — OLG Celle Rueckweisung aufgehoben — Beck-aktuell](https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/bgh-viizb925-gehoersverletzung-bea-qes-signatur-2026-05-18)
- [BGH akzeptiert einbettende Signaturen als QES — IWW](https://www.iww.de/ak/berufsrecht/elektronischer-rechtsverkehr-bgh-akzeptiert-einbettende-signaturen-als-qes-f162471)
- [BGH — Schriftformwahrung bei qeS — Addlegal](https://www.addlegal.de/beitraege/bgh-schriftformwahrung-bei-qes)
- [BGH zum Auseinanderfallen von qeS und einfacher Signatur — ERV-Justiz](https://ervjustiz.de/bgh-zum-auseinanderfallen-von-qes-und-einfacher-signatur)
- [§ 126a BGB — Elektronische Form — dejure.org](https://dejure.org/gesetze/BGB/126a.html)

**MCP-Server + Agentic-CLM (Haupt-Delta seit W26):**

- [DocuSign Model Context Protocol Server — Investor PR 30.09.2026](https://investor.docusign.com/news-and-events/press-releases/news-details/2026/Docusign-Unveils-AI-Assistant-and-Agents-to-Power-the-Next-Era-of-Agreement-Work/default.aspx)
- [Docusign Announces Agentic Contract Workflows for In-House Legal Teams — Investor PR](https://investor.docusign.com/news-and-events/press-releases/news-details/2026/Docusign-Announces-Agentic-Contract-Workflows-for-In-House-Legal-Teams/default.aspx)
- [Docusign Release Notes — September 2026 Latest Updates — Releasebot](https://releasebot.io/updates/docusign)
- [DocuSign Blog — Turning Contracts Into the Engine of Business with a New AI Assistant and Agents](https://www.docusign.com/blog/new-ai-assistant-and-agents)
- [DocuSign Unveils Iris Agents — The Letter Two](https://thelettertwo.com/2026/05/21/docusign-iris-ai-agents-agreement-automation/)
- [Anthropic Goes All-In on Legal — 20+ Connectors + 12 Plugins — LawNext](https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html)
- [Claude for Legal Deployment Guide — Anthropic PDF](https://www-cdn.anthropic.com/files/4zrzovbb/website/4b29cc317c727542642b5056e412cf8e779e13d8.pdf)
- [MCP for Legal Teams: Best MCP Servers — GC AI](https://gc.ai/blog/mcp-for-legal-teams)
- [MCP Connectors for Legal: Harvey, Westlaw, and Claude — Claude for Lawyers](https://claudeforlawyers.com/blog/mcp-connectors-for-legal)
- [How to Use Claude for Legal Work — MindStudio](https://www.mindstudio.ai/blog/claude-legal-mcp-connectors-contract-review-compliance)
- [Why Model Context Protocol Matters for Legal Tech — Ryan McDonough](https://www.ryanmcdonough.co.uk/why-model-context-protocol-mcp-matters-for-legal-tech-a-practical-overview/)
- [GitHub — anthropics/claude-for-legal — Plugins Suite](https://github.com/anthropics/claude-for-legal)

**Agentic-CLM GA 2026 (Jurist Redlining + PandaDoc CLM):**

- [Ironclad Jurist Redlining Agent GA 30.04.2026](https://ironcladapp.com/resources/articles/ai-agentic-launch)
- [Ironclad State-of-AI-in-Legal 2026 Report](https://ironcladapp.com/resources/reports/2026-state-of-ai-report)
- [Ironclad AI Capabilities Deep Dive — Intuition Labs 2026](https://intuitionlabs.ai/articles/ironclad-ai-contract-management-capabilities)
- [Ironclad Review 2026 — Vaquill Honest Assessment](https://www.vaquill.ai/blog/ironclad-review-honest-assessment)
- [PandaDoc Launches CLM for Growing Businesses 22.09.2026 — Yahoo Finance](https://finance.yahoo.com/small-business/articles/pandadoc-launches-contract-lifecycle-management-130000201.html)
- [PandaDoc Changelog — Developers](https://developers.pandadoc.com/changelog)
- [PandaDoc Features Breakdown July 2026 — ZoomInfo](https://pipeline.zoominfo.com/sales/pandadoc-features)
- [PandaDoc Leadership Transition for Small-Business-Innovation — BusinessWire](https://www.businesswire.com/news/home/20260107285194/en/PandaDoc-Announces-Leadership-Transition-to-Accelerate-Product-Innovation-for-Small-Businesses)
- [AI Contract Review 2026: Ironclad vs Harvey vs Evisort — AgenticContractReview](https://agenticcontractreview.com/vs-ironclad/)

**DACH-Konkurrenten — Pricing-Delta:**

- [ContractHero Preisentwicklung 2026 — Trusted.de Erfahrungen](https://trusted.de/contracthero)
- [ContractHero Pricing + Alternatives — Capterra 2026](https://www.capterra.com/p/206218/ContractHero/)
- [ContractHero Software Reviews — SoftwareAdvice 2026](https://www.softwareadvice.com/contract-management/contracthero-profile/)
- [ContractHero vs Alternativen DACH-Vergleich 2026 — top.legal](https://www.top.legal/wissen/contracthero-alternative-dach)
- [fynk Software Reviews — SoftwareAdvice 2026](https://www.softwareadvice.com/cms/fynk-profile/)
- [fynk vs PandaDoc — PandaDoc Alternative](https://fynk.com/en/alternatives/pandadoc/)
- [DACH-Vertragsmanagement-Software-Vergleich 2026 — Finban](https://www.finban.io/vertragsmanagement-software/vergleich)
- [Contract Management Comparison DACH — ContractHero](https://www.contracthero.com/en/blog/vertragsmanagement-software-vergleich-2026)

**Skribble + EU-Trust-Services (unveraendert, Zyklus-1-Carry-Over):**

- [Skribble Pricing (CH/DE/EU)](https://www.skribble.com/en-eu/pricing/)
- [Skribble Electronic Signature Software](https://www.skribble.com/en-eu/electronic-signature-software/)
- [Skribble API v2 Documentation](https://api-doc.skribble.com/)
- [Skribble Swisscom Trust Service Partnership](https://www.skribble.com/en-eu/swisscom-elektronic-signature/)
- [eIDAS Dashboard — EU Trusted Lists Browser](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)
- [List of qualified trust service providers in the EU — EU Commission](https://digital-strategy.ec.europa.eu/en/policies/eu-trusted-lists)
- [DocuSign FY2026 SEC Annual Report](https://www.sec.gov/Archives/edgar/data/1261333/000126133326000044/docufy26annualreportformupa.pdf)
- [sproof — EUDI Wallet Game Changer for Digital Identity](https://www.sproof.com/en/what-is-the-eudi-wallet-the-game-changer-for-digital-identity-eidas-and-compliance/)
- [Scrive — eIDAS 2 and the EUDI Wallet: New Era for Digital Identification in Europe](https://www.scrive.com/resources/knowledge-hub/news/eidas-2-and-the-eudi-wallet-a-new-era-for-digital-identification-in-europe)

**Cosmi-interne Cross-References:**

- `monthly/2026-06-22-deepdive-vertraege.md` — W26-Zyklus-1-Report (Delta-Basis fuer diesen Zyklus-2)
- `monthly/2026-10-pricing.md` — HubSpot Revenue Hub Full-Pricing + Bundle-Promo (W26-Pick-#4-Teil-Erfuellung)
- `weekly/2026-W40.md` — DIdG + Ghostscript HOCH + Stirling-PDF-SSO-Paywall-Reversal
- `weekly/2026-W39.md` — EUDI-Wallet d-you-Datenschutz-Kritik + DIdG erste Bundestag-Lesung
- `daily/2026-10-02-evening.md` — DIdG EUDIW-Deadline 24.12.2026 (80 Tage) + Art. 50 61-Tage-Grace-Period + Computerwoche-3-Fragen-Test
- `daily/2026-10-03-regulation.md` — Art. 50 Watermarking Grace-Period + DIdG Anhörung KW41 06.10. + Ghostscript HOCH
- `daily/2026-10-05-morning.md` — Vertraege-Feed-Polling-Status: DocuSign/PandaDoc/HelloSign nicht gepollt (Quellen-Backlog)
- `monthly/2026-09-28-deepdive-formulare.md` — W40-formulare-Zyklus-2 (Delivery-Divergenz-Pattern-Vorbild + Backend-Hygiene-vs-Markt-Scope-Pattern)
- `monthly/2026-09-21-deepdive-helpdesk.md` — W39-helpdesk-Zyklus-2 (AI-Compliance-Foundation-Sprint-Pflicht als Cross-Modul-Pattern + MCP-Server-6-Wochen-unresolved)
- `monthly/2026-09-14-deepdive-wiki.md` — W38-wiki-Zyklus-2 (ai_disclosure-Fehlende seit Art.-50-Enforcement + MCP-Server-Cosmi-Pattern)
- `monthly/2026-09-07-deepdive-video.md` — W37-video-Zyklus-2 (Meeting-AI-Summary ohne Disclosure seit 02.08.2026 = Primary-Konsument der Compliance-Foundation)
- `keepers/ai-cost-governance-ist-die-neue-beschaffungs-pflic-crm-core-w23.md` — AI-Governance-Audit-Trail als Verkaufsdoktrin
- `keepers/anthropic-kill-switch-live-fable-5-mythos-5-weltwe-cross-w25.md` — Provider-Router als strategische-Pflicht
- `keepers/eu-cada-320-mrd-souveränitäts-paket-konkretisiert--cross-w23.md` — Public-Sector-Beschaffung mit EU-Sovereign-Anker
- `keepers/eu-sovereignty-kipppunkt-5-signale-an-einem-tag-9--cross-w20.md` — EU-Sovereign-USP als operativ-aktive-Positionierung
- `backend/internal/vertraege/` — W41-Code-Stand (16 RPCs, 4 Domain-Modelle inkl. ContractEvent, Maroto-PDF-Renderer, contract_events-Audit-Log)
- `backend/migrations/000298_contract_events.up.sql` — Audit-Log-Migration (Append-Only Trail Pattern-Blueprint)
- `backend/proto/vertraege/v1/vertraege.proto` — RPCs 16-stueck (W26-15 + ListContractEvents)
- `desktop/src/renderer/src/modules/vertraege/` — Frontend-Schicht (VertraegePage 2565 LOC Mono-File-Dauer-Posten + ESignaturDialog 615 LOC + Settings 372 LOC)
- `desktop/src/renderer/src/stores/vertraege.ts:58-82` — Frontend-only-Drifts-Persistenz-Nachweis

---

## Telemetry

- **Routine**: intel-monday-deepdive
- **Model**: claude-opus-4-7
- **Rotation**: Zyklus 2, Position 7/15, Modul vertraege
- **Delta-to**: `monthly/2026-06-22-deepdive-vertraege.md` (105 Tage = 15 Wochen)
- **Hard-Output-Cap**: 40000 Tokens (dieser Report: ~16000 Tokens Output)
- **Pflicht-Sektionen erfuellt**: ✅ State-of-the-Art, ✅ Cosmi-IST-Stand, ✅ Vergleichstabelle (36 Zeilen > 6 Pflicht), ✅ 3 Empfehlungen

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss
