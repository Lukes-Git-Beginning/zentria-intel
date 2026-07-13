---
year: 2026
week: 29
modul: schichten
created: 2026-07-13
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 49
tokens_input: ~365000
tokens_output: ~26000
rotation_position: 10/15
---

# Deepdive: schichten (Mo W29/2026)

> **Zehnter Deepdive der Rotation.** Vorgaenger: `crm-core` (W20, 2026-05-11), `dialer` (W21, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01), `helpdesk` (W24, 2026-06-08), `formulare` (W25, 2026-06-15), `vertraege` (W26, 2026-06-22), `buchhaltung` (W27, 2026-06-29), `rapporte` (W28, 2026-07-06). Naechstes Modul gemaess Rotation: **fuhrpark** (KW30, 2026-07-20) — direkter Nachbar in der Handwerk-Modul-Welle 2A. Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-schichten (2026-07-13):** Backend `backend/internal/schichten/` ist **schlank und produktions-ready aus Sprint-2-Welle-2A** — 7 Files mit **~3155 LOC gesamt** (`errors.go` 15, `models.go` 91, `postgres_repository.go` 721, `repository.go` 68, `service.go` 736, `service_test.go` 1430, `tenant_isolation_phase2_test.go` 74), Coverage 35.2% laut `.knowledge/milestones.md`-Welle-2C-Sweep. **22 Service-Methoden** (`CreateShift`/`UpdateShift`/`DeleteShift`/`GetShift`/`ListShifts`/`PublishShifts`/`AssignEmployee`/`UnassignEmployee`/`ListAssignments`/`CreateTemplate`/`UpdateTemplate`/`DeleteTemplate`/`GetTemplate`/`ListTemplates`/`ApplyTemplate`/`CheckArbzgCompliance`/`GetShiftStats`/`CreateSwapRequest`/`ListSwapRequests`/`ApproveSwapRequest`/`RejectSwapRequest` plus interner `validateRestPeriod`). **ArbZG §5 Pre-Check ist der Kern-USP**: `arbzgMinRestDuration = 11 * time.Hour` als Konstante, `validateRestPeriod` prueft beide Richtungen (Shift-davor-Ende → newStart, newEnd → Shift-danach-Start), DST-Spring-Forward-tauglich via `time.LoadLocation("Europe/Berlin")` in `ApplyTemplate`, bei <11h Ruhezeit `ErrArbzgViolation`. **State-Machine Schicht**: `Draft → Published` mit `PublishShifts(from, to)`-Bulk-Publish (idempotent, Rows-affected-Sentinel). **State-Machine Swap-Request**: `pending → approved/rejected` (Migration 000160 `shift_swap_requests` mit `idempotency_key` UNIQUE + `swap_employees_differ` CHECK). **Capacity-Guard**: `Shift.Capacity *int` (nil = unlimited), `CountAssignments` vor Insert, `ErrShiftFull`-Sentinel. **Template-Modell**: `ShiftTemplate` mit `DayOfWeek 0..6` (Sonntag=0), `StartHour 0..23`, `StartMinute 0..59`, `DurationMinutes >0`, kein `Color`-Feld, kein `BreakMinutes`-Feld — Frontend-Adapter (`adaptApiTemplate`) setzt statische Defaults `color: '#3b82f6'`, `breakMinutes: 30`. **Frontend `desktop/src/renderer/src/modules/schichten/SchichtenPage.tsx`**: **1661 LOC Mono-Page** mit 4 Tabs (`wochenplan`/`vorlagen`/`anfragen`/`verfügbarkeit`), `SHIFT_STYLE_MAP` fuer 3 Template-Slots (`tpl-1` Sun/info, `tpl-2` Sunset/warning, `tpl-3` Moon/primary), `SURCHARGE_RULES` (Nacht +25%), `WEEKEND_SURCHARGE` (+50%), `HOLIDAY_SURCHARGE` (+100%) — **komplett Frontend-Mock** ohne Backend-Anker. `GERMAN_HOLIDAYS_2026` als **hardcoded Map fuer 9 DE-Feiertage 2026** (kein DACH-Bundesland/Kanton-Support). `AVAILABILITY_MOCK` fuer 4 Mock-User (`u-1`/`u-3`/`u-6`/`u-8`) mit `green`/`yellow`/`red` per Wochentag — **kein Backend-Aequivalent** (kein `employee_availabilities`-Table). `ArbZGViolation`-Type-Alias im Frontend definiert 4 Typen (`max_hours`/`rest_period`/`break_missing`/`consecutive_days`) — Backend liefert nur `rest_period` (aus `validateRestPeriod`), die anderen 3 sind **UI-Placeholder ohne Backend-Impl**. **Migrations-Historie**: 000094 `create_schichten` (shifts/shift_assignments/shift_templates + Indizes), 000095 seed permissions, 000102 `shift_assignments_tenant_unique` (Sicherheits-Fix — vorher konnte gleiche `(shift_id, employee_id)` cross-tenant kollidieren), 000122 RLS-Phase2-Long-Tail, 000160 `shift_swap_requests`, 000161 swap-request permissions, 000224 manager/member-Rollen-Seed (manager voll operativ, member `schichten:swap:read|create` Self-Service). **Modul-Anker**: Feature-Flag `modules.schichten` (`registry.go:77`, DefaultEnabled: false, `COSMI_MODULE_SCHICHTEN_ENABLED`, SafeRisk, LLMToggleSafe). Modul-Pricing-Anker (`KMU-Hub/.knowledge/pricing.md`): **4 EUR/User-Monat** fuer Schichten-Modul, Markt-Vergleich "Spezialsoftware 5-10". Modul-Kombo Schichten+Zeiterfassung = 7 EUR/User-Monat. **Bekannte Schulden**: (i) schichten ist eines der 13 Binaries ohne `TenantInboundUnaryInterceptor` (R3-P0-3 offen laut `.knowledge/security.md`), (ii) `Template.Color` + `Template.BreakMinutes` fehlen im Backend-Schema (Frontend faelscht Defaults), (iii) `SURCHARGE_RULES`/`WEEKEND_SURCHARGE`/`HOLIDAY_SURCHARGE` sind Frontend-Mocks — keine `shift_surcharge_rules`-Tabelle, keine Lohnkosten-Berechnung, (iv) `AVAILABILITY_MOCK` ist Frontend-Mock — kein `employee_availabilities`-Backend, (v) `arbzgMinRestDuration` ist hardcoded Konstante — keine Tenant-Konfigurierbarkeit fuer Krankenhaus/Gastro-Tarif-Ausnahmen, (vi) nur §5 ArbZG (11h Ruhezeit) — keine §3 (10h Tages-Max), keine §4 (Pausen 30min ab 6h / 45min ab 9h), keine §9-10 (Sonntag/Feiertag), keine Consecutive-Days-Regel (=> `ArbZGViolation.type` `max_hours`/`break_missing`/`consecutive_days` im Frontend deklariert aber Backend-blind), (vii) Coverage 35.2% unter dem 40%-Referenz-Ziel des `.knowledge/testing.md`-Standards, (viii) **kein AI/ML-Auto-Scheduler** — jede Zuweisung ist manueller Drag-Drop, (ix) **keine mobile Native-App** (Cosmi ist Electron + PWA-orientiert), (x) **kein Qualifikations-Matching** — jeder MA kann jeder Schicht zugewiesen werden solange ArbZG §5 passt.

> **Drei strukturelle Beobachtungen, die jeden Sprint-Plan kalibrieren.** **#1 Der DACH-Schichtplan-Markt Mitte 2026 ist AI-durchdrungen — in scharfem Kontrast zu rapporte (W28), wo Cosmi noch ein offenes AI-Fenster hatte.** Waehrend rapporte/zeiterfassung Vorwoche (W28-Deepdive) das Modul mit dem **niedrigsten AI-Feature-Druck von aussen** war (Timely + HERO Voice sind die einzigen Live-AI-Player, DACH-KMU-Marktfuehrer TimeTac/ZEP/Crewmeister/Papershift haben KEIN Live-AI), ist der Schichtplan-Markt exakt umgekehrt: **jeder Top-Konkurrent hat 2026 ein produktives AI-Feature**. **Papershift** hat **KI-Auto-Zuweisung im Premium-Plan (6 EUR/User-Monat) + generative KI-HR-Chat mit Rechte-Aware-Access auf Personaldaten** (`ki-syndikat.de/tools/papershift`), **Shyftplan** hat AI-Optimierung mit **20+ Faktoren** (Qualifikationen, Verfuegbarkeiten, Maschinen-Auslastung, Vertrags-Verfuegbarkeit, Planungs-Regeln, Praeferenzen, Fairness) fuer 3-5-stellige Schichtangestellte (`shyftplan.com/en/shyftplanner`), **Planday** hat "Smart AI-powered Rotas" mit Winter/Spring-2026-Updates und **explizitem Ziel "industry's first truly Agentic AI"** (`planday.com`), **7shifts** hat **ML-Auto-Scheduler der 8-10 vorherige Plaene analysiert** mit Labor-Cost/Sales-Forecast/Overtime/Availability/Compliance-Faktoren (`7shifts.com/pricing`), **Deputy** hat im **November 2025 Deputy AI Platform GA gelaunched** (AWS Bedrock/GenAI, Auto-Scheduling + Demand-Forecast + agentischer AI-Agent) (`news.deputy.com/deputy-launches-new-ai-platform-on-aws`), **Sona** hat im April 2026 **45M USD Series B geraised** (Total >100M USD) fuer AI-Frontline-Scheduling und im Q1 2026 **Sona Forge** als Enterprise-AI-App-Builder gelaunched (`prnewswire.com/news-releases/sona-raises-45m-series-b`), **Connecteam** hat **AI-Auto-Scheduling mit Konflikt-Flag** (Overlap, Doppel-Booking, waehrend Time-Off) und GPS-Geofencing (`connecteam.com/reviews/7shifts`). **Selbst DACH-Preis-Krieger Aplano** (0.50/2.00/4.50 EUR/MA — im Core-Plan 8-facher Preis-Rabatt gegen Cosmi 4 EUR) verkauft Auto-Konflikt-Erkennung als Kern-USP, ShiftJuggler mit **automatischer ArbZG-Konflikt-Erkennung inkl. DACH-Feiertage fuer DE/AT/CH mit Bundeslaender/Kantonen** (`shiftjuggler.com/vergleich/shiftjuggler-vs-papershift`) — Cosmi hat nur 9 hardcoded DE-2026-Feiertage im Frontend, keine Kantone. **Konsequenz fuer Cosmi**: der Vergleich mit rapporte-W28 kippt komplett — bei rapporte war "AI-Feature bewusst spaet einfuehren als Q4-2026-Differenzierer" eine sichere Strategie, bei schichten ist "kein AI-Feature bis Ende 2026" **markt-strukturelles Ausschluss-Risiko** fuer den KMU-5-30-MA-Vertrieb, weil Papershift + Ordio + Crewmeister die Bezugs-Zeichen setzen. Sprint-Empfehlung: **Cosmi-Schichten-AI-Auto-Zuweisung** als **Q4-2026-Pflicht** (nicht Nice-to-have) — Backend-Auto-Assign-Job der Verfuegbarkeit + Qualifikation + ArbZG-Constraints + Fairness einbezieht, ausgeloest per Manager-Klick "Woche automatisch fuellen". Kann heuristisch (constraint-satisfaction) starten, muss nicht LLM-gestuetzt sein — Papershift's Auto-Assign ist auch regel-basiert, keine echte ML-Trainings-Story. **#2 Der §16-ArbZG-E-Referentenentwurf vom 18.06.2026 hat den Cosmi-Schichten-Sales-Angle akut relevant gemacht — aber das §5-ArbZG-Update im gleichen Entwurf zerbricht Cosmi's `arbzgMinRestDuration = 11 * time.Hour`-Constant-Design.** Der BMAS-Referentenentwurf vom 18.06.2026 (`osborneclarke-arbeitsrecht.de/artikel/neues-zum-arbeitszeitgesetz`, `gleisslutz.com/de/know-how/bmas-update-neuer-referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes`) enthaelt **zwei fuer Cosmi-schichten kritische Aenderungen**: (a) **§16-Elektronische-Erfassungspflicht** (bereits im W28-rapporte-Deepdive dokumentiert): Beginn/Ende/Dauer taggleich elektronisch, **Uebergangsfristen 1a >250 MA / 2a 50-249 MA / 5a 10-49 MA / dauerhaft ausgenommen <10 MA**, **Bußgeld bis 50.000 EUR** (neu bewehrt) — Cosmi-Ziel-KMU 5-30 MA hat also **5-Jahres-Frist bis 2030-2031** (falls Inkrafttreten Q1-Q2 2027). (b) **§5-ArbZG-Aenderungen** (fuer Cosmi-schichten NEU-relevant): Ruhezeit **kann in Krankenhaeusern/Pflege, Gastronomie/Beherbergung, Verkehr, Rundfunk, Landwirtschaft/Tierhaltung um bis zu 1h verkuerzt werden** (also 10h statt 11h) — falls unmittelbar ausgeglichen. Zusaetzlich **koennen Tarifvertraege die 11h-Ruhezeit ganz aufheben** — vorausgesetzt hoehere Gesundheitsschutz-Regelungen sind vereinbart. **Konsequenz fuer Cosmi-schichten**: der aktuelle `arbzgMinRestDuration = 11 * time.Hour`-Constant in `service.go:13` ist **markt-fehlend** — er zwingt jedes Cosmi-Tenant auf 11h fest. Falls Cosmi-Kunde ein Pflegeheim oder Gastro-Betrieb ist mit Tarifvertrag-basierter 10h-Sonderregel, kann Cosmi's Modul **nicht abbilden**, was **Marktausschluss fuer Pflege-KMU + Gastro-KMU** bedeutet — beides sind Kern-Zielgruppen von Papershift (89% User-Zufriedenheit + PUR/Heise-Award 2026 "Personaleinsatzplanung") und Ordio (Fokus Gastro/Retail/Handwerk/Pflege/Kultur). **Sprint-Anker**: `arbzgMinRestDuration` von Konstante auf **Tenant-konfigurierbare Setting** (`hr_company_settings.min_rest_hours_default INT DEFAULT 11`, `shift_arbzg_overrides`-Tabelle fuer branchen-/tarif-spezifische Ausnahmen mit `Erklaerung`-Feld fuer Audit-Log). Dazu Cosmi-Marketing-Story "ArbZG-Reform-ready mit Tarif-Auto-Ausnahmen" als KMU-Vertriebs-Differenzierer. **#3 Cosmi-schichten hat 4 strukturelle Frontend-Backend-Divergenzen die die Prod-Story blockieren — SURCHARGE_RULES + WEEKEND_SURCHARGE + HOLIDAY_SURCHARGE + AVAILABILITY_MOCK sind alle nur Frontend, keine Backend-Persistenz.** Der `SchichtenPage.tsx`-Code (1661 LOC) definiert vier substantielle Feature-Areas die alle **UI-Mock-Only** sind: (i) **Zuschlags-System** (`SURCHARGE_RULES` fuer Nacht +25%, `WEEKEND_SURCHARGE` +50%, `HOLIDAY_SURCHARGE` +100%) — kein Backend-Aequivalent, keine `shift_surcharge_rules`-Tabelle, keine Lohnkosten-Berechnung, kein DATEV/LODAS-Export-Integration. (ii) **Feiertags-System** (`GERMAN_HOLIDAYS_2026` als hardcoded Map fuer 9 DE-Feiertage 2026, **kein Bundesland/Kanton-Support**, kein CH-DACH-Aspekt) — Vergleich: ShiftJuggler hat automatische DACH-Feiertag-Erkennung mit DE-Bundeslaender + AT-Bundeslaender + CH-Kantonen. (iii) **Verfuegbarkeits-System** (`AVAILABILITY_MOCK` fuer 4 Mock-User `u-1`/`u-3`/`u-6`/`u-8` mit `green`/`yellow`/`red` per Wochentag) — kein Backend-Table `employee_availabilities`, keine Backend-API. Aplano/Papershift/Shyftplan/Ordio alle verkaufen Verfuegbarkeits-Selbst-Service als Kern-Feature. (iv) **ArbZG-Warnungs-Palette** (`ArbZGViolation.type` deklariert `max_hours` + `rest_period` + `break_missing` + `consecutive_days`) — Backend liefert nur `rest_period` (aus `validateRestPeriod`), die anderen 3 sind **UI-Placeholder ohne Backend-Impl** — jede UI-Nachricht "Max-Stunden ueberschritten" oder "Pause fehlt" oder "Zu viele aufeinander folgende Tage" ist heute strukturell nicht ausloesbar. **Konsequenz fuer Cosmi**: das Cosmi-Schichten-Modul ist **UI-vs-Backend-inkonsistent** — der `git blame`-verifizierte Zustand zeigt ein Frontend das **mehr verspricht als der Backend liefert**. Der Sprint-2-Welle-2A-Backend hat solide Kern-Funktionalitaet (ArbZG §5, Templates, Assignments, Swap-Requests), aber der Frontend-Sprint hat das Modul kosmetisch weiter ausgebaut ohne Backend-Wiring. **Das ist eine Prod-Risk** — sobald Kunden diese Features nutzen wollen (Zuschlaege fuer Payroll, Feiertags-Auto-Erkennung, Verfuegbarkeits-Selbst-Service, ArbZG-Full-Warnungs-Palette), muss Backend nachgezogen werden, und der Sprint-Umfang ist non-trivial. **Sprint-Anker**: (i) `shift_surcharge_rules`-Tabelle mit Backend-Persistenz + Payroll-Berechnungs-Endpoint (Q3-2026), (ii) `employee_availabilities`-Tabelle mit Self-Service-Endpoint (Q3-2026 — Pflicht wenn AI-Auto-Assign kommt), (iii) DACH-Feiertag-Auto-Erkennung via nager.at-Public-API oder `nager-date`-npm-Library mit DE/AT/CH-Bundeslaender/Kanton-Support (kleiner Sprint), (iv) ArbZG §3/§4/§9-10 + Consecutive-Days-Backend-Impl (mittlerer Sprint) — muss vor AI-Auto-Assign da sein.

> **Leit-Signal der Woche fuer schichten: vier parallele Bewegungen formen den Markt seit Anfang 2026.** **(a) BMAS-Referentenentwurf 18.06.2026 (ArbZG-Reform)** ist die aktuellste und schaerfste regulatorische Bewegung — nicht nur §16-Elektronik-Erfassungspflicht mit Bußgeld-Bewehrung bis 50.000 EUR (siehe W28-rapporte-Deepdive fuer den vollen Kontext), sondern auch §5-Ruhezeit-Aenderungen die Cosmi's hardcoded `11 * time.Hour`-Constant zerbrechen — Pflege/Gastro/Verkehr/Rundfunk/Landwirtschaft duerfen 10h Ruhezeit fahren, Tarifvertraege koennen die 11h ganz aufheben, Regelbarkeit ueber Arbeitsbereitschaft-Ausnahme entfaellt. **(b) AI-Auto-Assign als Marktbenchmark im DACH-Schichtplan-Segment** ist scharf und flaechendeckend — Papershift/Shyftplan/Planday/7shifts/Deputy/Sona/Connecteam/Aplano haben live Auto-Assign-Features, Cosmi hat nur manuellen Drag-Drop. Der 7shifts-Ansatz "**ML-Auto-Scheduler analysiert 8-10 vorherige Plaene**" ist besonders interessant als Muster-Erkennung-Story, weil er nicht LLM-abhaengig ist und mit historischen `shifts`-Rows + `shift_assignments` schon jetzt berechnet werden koennte. **(c) Frontline-Konsolidierung** — Sona's 45M USD Series B (April 2026, kumulativ >100M USD), Shyftplan's Maguar-Uebernahme (Juni 2024), Deputy's AWS-AI-Platform-Launch (November 2025) zeigen dass Investoren + Konsolidierer Frontline-Workforce-Management als **wachsenden Vertikal-Markt** identifiziert haben. Der globale Employee-Scheduling-Markt ist $11.25B (2025) → $23.5B (2033) bei **CAGR 9.8%**, KMU-Segment mit **CAGR 14.9%** (schnellstes Wachstum), Europa mit 68% shift-based Arbeitgeber die AI-Forecasting bis Ende 2025 pilotieren wollen (up von 42% 2023) (`cognitivemarketresearch.com/employee-scheduling-and-shift-planning-software-market-report`, `futuremarketreport.com/industry-report/workforce-scheduling-software-market`). **(d) Preis-Aggressivitaet im DACH-KMU-Segment** — Crewmeister hat Zeiterfassung ab **1.50 EUR/User-Monat** + Schichtplanung ab **2 EUR/User-Monat** (`crewmeister.com/de/preise`), Aplano hat Core ab **0.50 EUR/User-Monat** (`aplano.de/preise`), ShiftJuggler ab **2.78 EUR/User** — Cosmi mit **4 EUR/User-Monat** ist **teurer als Kern-DACH-Konkurrenten am Einstiegsniveau**, und Papershift mit 6 EUR Premium (mit AI-Auto-Assign + AI-Chat) macht die Preis-Story wackelig. **Heute keine akute schichten-Markt-Nachricht im Morning-Pulse** (`daily/2026-07-13-morning.md` ausstehend, letzter Pulse `2026-07-10-evening`), **aber die vier Bewegungen sind alle in den letzten 8 Wochen als Nebenlinien in `.state/hot_items_2026-06-*` und `daily/*.md` vertreten**. **Dieser Bericht empfiehlt drei Pflicht-Sprint-Stakes fuer das dritte Quartal 2026: ArbZG-Constant-zu-Tenant-Setting-Konsolidierung, Auto-Assign-Heuristik-Layer (Q3-Prototyp, Q4-GA), Frontend-Backend-Divergenz-Fix fuer Surcharges/Availability/Feiertag/ArbZG-Full-Palette — alle drei sind heute strukturelle Cosmi-Luecken, alle drei haben in 3-6 Monaten Marktbeobachtungs-Auswirkung, keine der drei ist heute in einem Sprint-Backlog erkennbar.**

---

## State-of-the-Art

Der DACH-Schichtplanungs-Markt Mitte 2026 ist **dreispurig** — anders als der rapporte-Markt (W28) mit Domaene-Segmentierung zwischen Handwerk-Feld-Rapport und HR-Zeiterfassung, ist dieser Markt **funktions-segmentiert** und **AI-durchdrungen** (Ausnahme wenige Preis-Krieger). Die drei Spuren:

**(1) DACH-KMU-Schichtplan-Spezialisten (Papershift, Ordio, Crewmeister, Aplano, ShiftJuggler, gastromatic, Shiftbase-DACH)**: KMU-Zielgruppe 5-500 MA, mobile-Web-Fokus, DATEV/LODAS-Payroll-Integrationen, ArbZG-Compliance-Warnungen, KI-Auto-Assign als Marktbenchmark ab Papershift Premium-Plan. Direkter Cosmi-`schichten`-Wettbewerber im 5-30-MA-Segment.

**(2) Enterprise/AI-First-Player (Shyftplan, Sona, Planday, Deputy)**: 100+ MA Ziel-Segment, native Mobile-Apps, tiefe HR-Suite-Integration (Personio, SAP SuccessFactors, Workday HCM), AI-Auto-Optimierung mit 15-30+ Constraints, agentische AI-Roadmap (Planday-Ziel, Deputy-AI-Platform Nov-2025). Nicht Cosmi-KMU-5-30-Ziel, aber setzt Feature-Benchmarks fuer den ganzen Markt (Personio-Integration ist DACH-KMU-Standard-Anforderung).

**(3) International-Restaurant/Retail-Frontline (7shifts, Deputy, Connecteam)**: US/CA/AU-Herkunft, POS-Integration fuer Sales-basierte Personal-Bedarf-Forecast (7shifts), Frontline-mobile-first mit GPS-Geofencing (Connecteam), 100+ Laender (Deputy). Nicht direkter DACH-Handwerk-Konkurrent aber setzt AI-Auto-Scheduler-Muster (7shifts ML mit 8-10 historische Plaene) und Frontline-Mobile-Erwartungshaltung.

Cosmi-schichten sitzt heute **architektonisch in Spur (1)** als DACH-KMU-Schichtplan-Modul, aber ohne AI-Auto-Assign, ohne Availability-Backend, ohne Feiertag-DACH-Auto und ohne Zuschlags-Payroll-Integration. Der Modul-Preis von **4 EUR/User-Monat** ist **im Mittelfeld**: unter Papershift Premium (6 EUR) und Professional (9 EUR), gleich Aplano Pro (4.50 EUR), aber teurer als Crewmeister Schichten (2 EUR + 1.50 EUR Zeit = 3.50 EUR gebuendelt), Aplano Basic (2 EUR), Aplano Core (0.50 EUR), ShiftJuggler (2.78 EUR/User bei Team-Kombi). Der Preis-Vorteil gegenueber Papershift Premium (6 EUR) ist real, aber Papershift liefert AI-Auto-Assign — Cosmi's 33%-Preis-Rabatt gegen Papershift ist **feature-adjusted schwach** ohne AI. Und der Preis-Vorteil gegen 7shifts (ab 39.99 USD/Monat Essentials) oder Connecteam (ab 29 USD/Monat Basic) ist strukturell hoch, aber die Zielgruppe ueberlappt nicht (Restaurant/Frontline USA vs. DACH-KMU).

Vier strukturelle Veraenderungen treiben den Markt seit Anfang 2026:

(a) **§16 + §5 ArbZG-Reform-Reaktivierung 2026 mit neuem Referentenentwurf-Datum 18.06.2026**. Der Referentenentwurf lag April 2023 vor, wurde durch die Ampel-Koalition zurueckgestellt, ist durch den schwarz-roten Koalitionsvertrag (April 2025) neu aufgerufen worden. **Aktualisierter Referentenentwurf des BMAS: 18. Juni 2026** (`osborneclarke-arbeitsrecht.de/artikel/neues-zum-arbeitszeitgesetz-was-der-referentenentwurf-des-bmas-vom-18-juni-2026-fur-die-hr-praxis-bedeutet`, `gleisslutz.com/de/know-how/bmas-update-neuer-referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes`, `eversheds-sutherland.com/de/germany/insights/update-zum-arbeitszeitgesetz-referentenent-wurf-zur-elektronischen-arbeitszeiterfassung`). **§16-Kern-Regelung** (bereits im W28-rapporte-Deepdive dokumentiert): elektronische Erfassung von Beginn/Ende/Dauer taggleich, **Bußgeld-Bewehrung bis 50.000 EUR neu** (`osborneclarke-arbeitsrecht.de`), Vertrauensarbeitszeit erhalten (Delegation an MA moeglich), Ausnahmen ueber Tarifvertrag/Betriebsvereinbarung. **Uebergangsfristen gestaffelt** (bestaetigt durch mehrere Quellen inkl. `haufe-x360.de/blog/arbeitszeitreform-arbeitgeber` und `zeiterfassung-fdm.de/ressourcen/ratgeber/zeiterfassung-kleinbetriebe-pflicht`): **1 Jahr fuer >250 MA, 2 Jahre fuer 50-249 MA, 5 Jahre fuer 10-49 MA, dauerhaft ausgenommen fuer <10 MA**. Cosmi-Ziel-KMU 5-30 MA hat also realistisch **Compliance-Deadline 2030-2031** — kein akuter Zeitdruck fuer den KMU-Vertrieb, aber **Sales-Story ist ab jetzt relevant**. **§5-Kern-Aenderungen** (fuer schichten NEU-relevant): (i) Ruhezeit **verkuerzt auf bis zu 10h in Krankenhaeusern/Pflege, Gastronomie/Beherbergung, Verkehr, Rundfunk, Landwirtschaft/Tierhaltung** falls unmittelbar ausgeglichen; (ii) Tarifvertrag kann 11h-Ruhezeit ganz aufheben mit hoeherem Gesundheitsschutz; (iii) Regelbarkeit abweichender Ruhezeiten bei Arbeitsbereitschaft/Bereitschaftsdienst in erheblichem Umfang entfaellt. **§3-ArbZG-Reform-Aussicht**: Flexibilisierung, **Wochenbetrachtung statt Tagesbetrachtung** — 48h/Woche EU-Vorgabe bleibt, aber taegliches 10h-Max koennte lockerer werden. **Konsequenzen fuer Cosmi-schichten**: (i) `arbzgMinRestDuration = 11 * time.Hour` muss von Constant zu **Tenant-Setting** werden (`hr_company_settings.min_rest_hours_default INT DEFAULT 11`, plus `shift_arbzg_overrides`-Tabelle mit `industry_code` VARCHAR und `min_rest_hours INT` und `justification TEXT` fuer Audit). (ii) Cosmi-Marketing-Story "ArbZG-2026-Reform-ready mit Pflege/Gastro-Tarif-Auto-Ausnahmen" als KMU-Vertriebs-Differenzierer im H2 2026. (iii) `validateRestPeriod` muss `restPeriod` aus Tenant-Setting lesen statt Constant. (iv) `CheckArbzgCompliance` muss zusaetzlich §3 (Wochenbetrachtung, 48h/Woche), §4 (Pausen 30min ab 6h / 45min ab 9h), §6 (Nacht-/Schichtarbeit-Regelungen), §9-10 (Sonntag/Feiertag) einbeziehen — heute nur §5. (v) Consecutive-Days-Check (max 6 Tage in Folge ohne Ruhezeit) fehlt komplett.

(b) **AI-Auto-Assign als DACH-Marktbenchmark ab 2026**. Live-AI-Features Stand 2026-07-13: (i) **Papershift** (KI-Auto-Zuweisung ab Premium-Plan 6 EUR/User-Monat) — regel-basierte Zuweisung mit Verfuegbarkeiten + Qualifikationen; PLUS **Papershift KI-HR-Chat** als **generative AI-HR-Assistenz** die Personaldaten + Unternehmensdokumente durchsuchbar macht mit Berechtigungs-Aware-Access (`ki-syndikat.de/tools/papershift`). PUR/Heise-Award 2026 "Personaleinsatzplanung", 89% User-Zufriedenheit im Support. (ii) **Shyftplan** (Enterprise, min 700 EUR/Monat) — AI-Optimierung mit **20+ Faktoren** (Qualifikationen, Verfuegbarkeiten, Maschinen-Auslastung, Vertrags-Verfuegbarkeit, Planungs-Regeln, Praeferenzen, Fairness), berechnet Korrelationen zwischen Faktoren fuer optimalen Plan (`shyftplan.com/en/shyftplanner`). Personio + SAP SuccessFactors + SAP APO + Workday HCM Integration. Von Maguar Juni 2024 uebernommen. Threat fuer Cosmi-KMU: LOW (Enterprise-Fokus), aber setzt AI-Erwartungs-Standard. (iii) **Planday** (ab $2/User-Monat, Xero-Ownership seit Aug 2018) — "Smart AI-powered Rotas" mit Ziel "**industry's first truly Agentic AI**" (2026-Roadmap-Kommunikation, `planday.com`). Winter/Spring 2026 Updates: Performance Overview, verbesserte break/supplement management (`help.planday.com/en/articles/621960-product-updates-winter-and-spring-2026`). DACH-Sprache aktiv. (iv) **7shifts** ($39.99 Essentials / $89.99 Pro / $149.99 Premium/Monat, Nordamerika-Restaurant-Fokus) — **ML-Auto-Scheduler der 8-10 vorherige Plaene analysiert** fuer Muster-Erkennung + Labor-Cost/Sales-Forecast/Overtime/Availability/Compliance (`7shifts.com/pricing`). POS-Integration fuer Sales-basierte Personal-Bedarf-Forecast. (v) **Deputy** ($6.50 Core / $9 Pro/User-Monat + Add-Ons, 1.5M shift-workers weltweit) — **Deputy AI Platform** GA **November 2025** auf AWS Bedrock/GenAI: Auto-Scheduling + Demand-Forecast + agentischer AI-Agent der eigenstaendig Aktionen ausloest (`news.deputy.com/deputy-launches-new-ai-platform-on-aws-to-transform-how-businesses-manage-shift-work-ef9g8q`). DACH-Depth niedriger als Ordio. (vi) **Sona** (April 2026 **45M USD Series B**, kumulativ >100M USD) — AI-Auto-Sched balanciert Cost/Coverage/Compliance, 70% Open-Shifts <24h gefuellt via intelligente Notifications, **Sona Forge** (Q1 2026) als Enterprise-AI-App-Builder mit voller Sona-Datenintegration (`prnewswire.com/news-releases/sona-raises-45m-series-b-to-bring-ai-to-the-frontline-economy`). (vii) **Connecteam** ($29 Basic / $49 Advanced / $99 Expert, Frontline-mobile-first, 3 Hubs Operations/Communications/HR-Skills) — AI-Auto-Sched mit Konflikt-Flag (Overlap, Doppel-Booking, waehrend Time-Off), GPS-Geofencing + Real-time Breadcrumb-Tracking. (viii) **Ordio** (89/129/149 EUR/Monat **Flat-Rate unabhaengig von MA-Anzahl**, DACH-KMU, Fokus Gastro/Retail/Handwerk/Pflege/Kultur) — AI-Auto-Rota mit branchen-spezifischen Modulen (Inventar-Bestellung, Checklisten, custom Workflows). (ix) **Aplano** (0.50/2/4.50 EUR/MA-Monat, monatlich kuendbar, GDPR-konform DE-hosted) — Auto-Konflikt-Erkennung als Kern-USP. (x) **ShiftJuggler** (ab 39 EUR/Monat, ~2.78 EUR/User bei Team-Kombi) — automatische ArbZG-Konflikt-Erkennung inkl. **DACH-Feiertag-Auto fuer DE/AT/CH mit Bundeslaender/Kantonen**. **Konsequenz fuer Cosmi**: das ist eine **strukturelle Bedrohung**. Anders als bei rapporte-W28 (wo AI-Feature-Fenster offen war), ist bei schichten das AI-Auto-Assign-Fenster **geschlossen** — Cosmi ohne Auto-Assign steht heute als Feature-arm im KMU-DACH-Segment. Sprint-Anker: **regel-basierte Auto-Assign-Heuristik** als Q3-2026-Prototyp (Backend-Job der `shifts` + `shift_assignments` + `employee_availabilities` + Qualifikationen + ArbZG-Constraints einbezieht, Manager-Klick "Woche automatisch fuellen" mit UI-Preview-vor-Publish), Q4-2026-GA. Kein LLM-Zwang — 7shifts + Papershift + Aplano + Ordio sind alle regel-basiert.

(c) **DACH-Feiertag-Auto-Erkennung als Marktbenchmark** — ShiftJuggler verkauft **automatische DE-Bundeslaender + AT-Bundeslaender + CH-Kanton-Feiertag-Erkennung** als DACH-USP (`shiftjuggler.com/vergleich/shiftjuggler-vs-papershift`). Cosmi's `GERMAN_HOLIDAYS_2026` als **hardcoded 9-Eintrag-Frontend-Map** ist strukturell nicht wartbar (jedes Jahr manuelle Update-PR noetig), nicht DACH-vollstaendig (kein AT, kein CH, keine DE-Bundeslaender wie Fronleichnam BY/BW/HE/NW/RP/SL), nicht Backend-persistiert (kann nicht in Payroll-Berechnung einfliessen). Sprint-Anker: (i) **nager-date-npm-Library** fuer Client-Feiertag-Auto (Client-side gratis) oder **nager.at-Public-API** fuer Server-side; (ii) `holidays`-Backend-Table mit `country_code`, `region_code` (Bundesland/Kanton), `year`, `date`, `name`, `type` (public/school/regional). Beide Optionen sind **kleiner Sprint** (<3 Tage), aber Marktbenchmark-Erwartung.

(d) **Frontline-Mobile-First als Restaurant/Handwerk/Pflege-Marktbenchmark 2026**. 7shifts + Deputy + Connecteam + Ordio verkaufen native iOS/Android-Apps als **Grundvoraussetzung fuer Frontline-Zielgruppe**. Cosmi ist Desktop-Electron + PWA-orientiert (`desktop/`-Ordner ist Electron-App) — das ist strukturell **nicht Baustellen-Handschuh-Bedien-optimal, nicht Kellner-Servicerock-Handset-optimal, nicht Pflege-Stationszimmer-Tablet-optimal**. Der Vergleich zu rapporte-W28-Analyse ("Cosmi hat SketchCanvas + GPS + Signature + Foto + Aufmass — aber SignatureCanvas ist Stub, Offline-Mode fehlt, PWA-Baustellen-Story ist nicht kommuniziert") gilt hier verstaerkt: Schichtplan-UX braucht Ein-Tap-Clock-In, Ein-Swipe-Schicht-Tausch-Anfrage, Push-Notifications fuer Genehmigungen — alles native-App-Muster. Sprint-Anker: **PWA-First-Layer fuer SchichtenPage.tsx** (Service-Worker + Offline-Queue + Push-API + Add-to-Homescreen-Prompt) als Q4-2026-Delivery; native iOS/Android-Wrapper via Capacitor (nutzt bestehende PWA) als 2027-Q1-Nachzug.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Papershift (DE, threat: HIGH als DACH-KMU-Schichtplan-Marktfuehrer mit KI-Auto-Assign)**

Papershift ist **DE-Karlsruhe-Schichtplan-KMU-Marktfuehrer** — deutsche Firma, PUR/Heise-Award 2026 "Personaleinsatzplanung", 89% User-Zufriedenheit im Support, Ziel-Segment 5-500 MA alle Branchen (Gastro/Retail/Pflege/Handwerk/Buero). Direktester Cosmi-`schichten`-Konkurrent.

- **KI-Auto-Zuweisung (ab Premium 6 EUR/User-Monat)**: **Marktbenchmark** — regel-basierter Auto-Assign mit Verfuegbarkeiten + Qualifikationen als Input, Manager-Button "Schichten automatisch fuellen" (`ki-syndikat.de/tools/papershift`). Cosmi 0.
- **KI-HR-Chat (generative AI-HR-Assistenz)**: durchsuchbar auf Personaldaten + Unternehmensdokumente, respektiert Berechtigungs-Logik der Plattform, LLM-basiert (kein Vendor genannt, wahrscheinlich Azure OpenAI wegen DE-Compliance-Anspruch). Cosmi 0.
- **DATEV/LODAS-Export (Professional-Plan 9 EUR/User-Monat)**: automatische Lohnartenberechnung + individuelle Zuschlaege + DATEV/LODAS-Bi-direktional. Cosmi 0 fuer schichten.
- **Zeiterfassung im Core (4 EUR/User-Monat)**: digitales Stempeln via Browser/Tablet-App/Smartphone, mitarbeiter-spezifische Pausenregeln, Abwesenheitsmanagement. Cosmi hat `zeiterfassung` als separates Modul (3 EUR/User-Monat).
- **Verfuegbarkeits-Selbst-Service**: MA hinterlegen Verfuegbarkeiten und Qualifikationen, Auto-Assign nutzt diese als Constraints. Cosmi hat nur Frontend-Mock (`AVAILABILITY_MOCK`).
- **Pain-Points G2/Capterra 2026**: "Basic-Support-Paket 39 EUR/Monat verpflichtend on-top zum Plan-Preis (versteckte Kosten)", "Schichtplanung erst ab Premium — Core-Plan ist im Kern Zeiterfassung", "App-Abstuerze auf Android", "verwirrende Menue-Struktur", "Freizeit-Berechnung ueber Monate defekt gemeldet", "Support-Chat 'awkward'".
- **Pricing (2026)**: Core **4 EUR/MA-Monat** (Zeit + Abwesenheiten), Premium **6 EUR/MA-Monat** (+ Schichtplanung + KI-Auto-Assign), Professional **9 EUR/MA-Monat** (+ DATEV/LODAS-Export), Enterprise auf Anfrage. **Verpflichtender Support** Basic **39 EUR/Monat** (E-Mail/Helpdesk/begrenzt Telefon), Plus **99 EUR/Monat** (Live-Chat/laenger Telefon), Expert **399 EUR/Monat** (Optimierung/Remote-Service). 14-Tage-Testphase kostenfrei. **Kostenbeispiel 50 MA Premium**: 50 × 6 EUR + 39 EUR Support = **339 EUR/Monat netto** (`papershift.com/webinare/core-premium-professional`).
- **Tech-Stack**: DE-Cloud, mobile-Apps (iOS/Android/Web), REST-API, DATEV/LODAS/HR WORKS/LOHN24/Personio-Integrationen.
- **Gap zu Cosmi**: KI-Auto-Assign (Marktbenchmark), KI-HR-Chat, DATEV/LODAS-bidirektional, Verfuegbarkeits-Backend, Qualifikations-Matching, Zuschlags-Payroll-Berechnung, Abwesenheits-Verwaltung.
- **Strategischer Hinweis (WICHTIGSTER AI-PUNKT DIESES REPORTS)**: **Papershift ist Cosmi's schaerfster DACH-KMU-Schichtplan-Konkurrent, aber Preis-Struktur ist teurer als Cosmi-Kombo**. Papershift Premium (6 EUR/MA + 39 EUR Support = 339 EUR fuer 50 MA), Cosmi `schichten` (4 EUR/MA = 200 EUR fuer 50 MA) — **Cosmi ist 41% guenstiger fuer Premium-Feature-Set-Erwartung** aber liefert NICHT das Feature-Set (kein AI, keine DATEV, keine Verfuegbarkeit). **Sprint-Prioritaeten**: (i) **AI-Auto-Assign-Heuristik** (Q3-2026-Prototyp, Q4-GA — nutzt `shifts` + `shift_assignments` + neue `employee_availabilities` + neue `employee_qualifications` + bestehende ArbZG §5-Constraints als Constraint-Satisfaction-Problem, kein LLM noetig, siehe 7shifts-Pattern), (ii) `employee_availabilities`-Backend + Self-Service-Endpoint (Q3-2026 — Pflicht fuer AI-Auto-Assign), (iii) `employee_qualifications`-Backend (Q3-2026 — Pflicht fuer AI-Auto-Assign), (iv) DATEV/LODAS-Payroll-Sync fuer Zuschlaege + Stunden (Q4-2026, gemeinsam mit `zeiterfassung`-Modul-Sprint aus W28-rapporte-Deepdive-Anker).

**2. Shyftplan (DE Berlin, threat: MEDIUM als Enterprise-AI-Benchmark, LOW im Cosmi-KMU-Segment)**

Shyftplan ist **DE-Berlin-Enterprise-Schichtplan-Marktfuehrer mit AI-Auto-Optimierung** — 2013 gegruendet, von **Maguar-Group Juni 2024 uebernommen** (Tracxn-Daten, kumulative Funding $13.8M ueber 5 Rounds vor Uebernahme), Ziel-Segment 100+ MA / dreistellige bis fuenfstellige Schichtangestellte, Industrie-Fokus (Produktion, Logistik, Krankenhaus). Nicht Cosmi-KMU-5-30-Konkurrent, aber setzt AI-Benchmark.

- **AI-Auto-Optimierung mit 20+ Faktoren**: Qualifikationen, Verfuegbarkeiten, Maschinen-Auslastung, Vertrags-Verfuegbarkeit, Planungs-Regeln, Praeferenzen, Fairness — berechnet Korrelationen zwischen Faktoren fuer optimalen Plan (`shyftplan.com/en/shyftplanner`). Auto-Optimierung ist Kern-USP, nicht Nebenfeature.
- **Enterprise-HR-Suite-Integration**: **Personio Real-Time-Sync** (bidirektional — neue MA in Personio erscheinen in Shyftplan innerhalb Minuten, Anwesenheit/Abwesenheit-Sync in Realtime von Shyftplan zu Personio) (`shyftplan.com/en/personio-integration`), **SAP-verifiziert** fuer SAP SuccessFactors + SAP APO + SAP HCM (`shyftplan.com/en/features/systemintegration`), Workday HCM. **shyftconnect** als Standard-Interface.
- **Pain-Points G2 2026**: "Enterprise-Plan-Preis unerreichbar fuer wachsende KMU — Personio-Integration nur im Enterprise-Plan mit Mindest-Kauf-Menge, zu teuer fuer <100-MA-Kunden", "Positionierungs-Splitting Enterprise vs. SMB verwirrt Kunden", "AI-Ausgaben brauchen Trainings-Phase".
- **Pricing (2026)**: **Minimum 700 EUR/Monat** (Enterprise-Fokus). Personio-Integration Enterprise-only mit Mindest-Kauf-Menge. Neue Kunden erhalten Trainings-Onboarding im Preis inklusive.
- **Tech-Stack**: DE-Cloud (Berlin), REST-API, native iOS/Android-Apps, SAP-BTP-Integration, Personio-Marketplace-Standard-Integration.
- **Gap zu Cosmi**: AI-Auto-Optimierung mit 20+ Faktoren-Correlation, Enterprise-HR-Suite-Bidirektional-Sync, Maschinen-Auslastung-Constraint (fuer Produktions-Kunden), Fairness-Constraint.
- **Strategischer Hinweis**: **Shyftplan zielt nicht auf Cosmi-KMU-Segment**, aber setzt AI-Erwartungs-Standard fuer DACH-Markt als Ganzes. Der 20+-Faktor-Constraint-Satisfaction-Ansatz ist strukturell relevant fuer Cosmi's Auto-Assign-Design — auch wenn Cosmi mit 4-6 Constraints (ArbZG §5 + Verfuegbarkeit + Qualifikation + Kapazitaet) startet, ist die Architektur "Constraint-Set + Solver" der richtige Weg. Sprint-Anker: keine direkten Cosmi-Sprint-Ziele, aber Constraint-Solver-Design-Pattern uebernehmen (open-source Optionen: OR-Tools mit CP-SAT-Solver von Google, oder simple Greedy-Heuristik fuer MVP).

**3. Ordio (DE, threat: HIGH DACH-KMU-Handwerk/Gastro/Pflege-Konkurrent + Location-basiertes Pricing)**

Ordio ist **DE-DACH-KMU-Schichtplan-Anbieter mit Branchen-Fokus** — Zielgruppe Gastro/Retail/Handwerk/Pflege/Kultur (10-200 MA pro Standort), industry-specific Modules (Inventar-Bestellung, Checklisten, custom Workflows). Cosmi-`schichten` + `zeiterfassung`-Konkurrent im DACH-KMU-Segment, aber teurer.

- **Location-basiertes Pricing (Marktbenchmark-Alternative)**: **Flat-Rate pro Standort, unabhaengig von MA-Anzahl** (`ordio.com/en/pricing`) — Starter **89 EUR/Standort/Monat**, Plus **129 EUR/Standort/Monat**, Pro **149 EUR/Standort/Monat**. Fuer 20-MA-KMU an einem Standort: 89-149 EUR/Monat = 4.45-7.45 EUR/MA-Monat — **teurer als Cosmi 4 EUR/MA fuer kleine KMU** (5 MA = 89 EUR/17.80 EUR/MA), **guenstiger fuer groessere KMU** (50 MA = 89 EUR/1.78 EUR/MA).
- **Branchen-spezifische Module**: Inventar-Bestellung + Checklisten + custom Workflows fuer Gastro/Retail/Handwerk/Pflege/Kultur. Cosmi hat inventar/checklisten separat (nicht in schichten).
- **AI-Auto-Rota**: erwaehnt in Feature-Set, aber weniger prominent kommuniziert als Papershift/Shyftplan.
- **Shift-Swap-Selbst-Service**: MA reichen Verfuegbarkeit ein, Schicht-Tausch anfragen, Open-Shifts claimen; Manager genehmigt Aenderungen mit Push-Benachrichtigungen (`ordio.com`).
- **DACH/EU-Labor-Compliance**: tiefe DACH-Rechts-Depth (kommuniziert als USP vs. Deputy fuer Deutsche Rules) — automatische ArbZG-Warnungen, Feiertag-DACH, Tarifvertrag-Templates.
- **UK-Expansion-Ready**: EU/DACH-Kunden mit UK-Expansion-Ambition sind Kern-Ordio-Zielgruppe.
- **Pain-Points OMR 2026**: "Location-basiertes Pricing kann fuer Multi-Site-KMU teuer werden", "Feature-Breite ausserhalb Kern-Schichtplan schwaecher als Papershift".
- **Tech-Stack**: DE-Cloud, mobile iOS/Android-Apps, REST-API, DATEV-Export, Feiertag-DACH.
- **Gap zu Cosmi**: Location-basiertes Pricing-Modell (einfacher fuer Multi-Site-KMU-Rechnungs-Kalkuel), Branchen-spezifische Add-Ons (Inventar-Bestellung, Checklisten), AI-Auto-Rota, DACH-Feiertag-Auto, DATEV-Export im Kern.
- **Strategischer Hinweis**: **Ordio ist der interessanteste Preis-Modell-Konkurrent** — Cosmi's Per-User-Pricing (4 EUR) vs. Ordio's Per-Standort-Pricing (89-149 EUR) hat **strukturelle Gewinn-Zonen** fuer Cosmi bei kleinen KMU (5-15 MA an einem Standort → Cosmi 20-60 EUR, Ordio 89-149 EUR) und **strukturelle Verlust-Zonen** bei groesseren (50+ MA an einem Standort → Cosmi 200+ EUR, Ordio 89-149 EUR). Sprint-Anker: (i) **Multi-Site-Support** in Cosmi-schichten (heute nur `Shift.Location TEXT` als String — kein `locations`-Table, keine Cross-Location-Reports) fuer Multi-Standort-KMU-Kunden — Q4-2026-Sprint, (ii) **Volumen-Rabatt-Staffel** (schon in `.knowledge/pricing.md` als "20 User (5%)" erwaehnt) explizit im schichten-Pricing kommunizieren, (iii) **branchen-spezifische Modul-Templates** (Gastro/Retail/Pflege/Handwerk mit vorgefertigten `ShiftTemplate`-Sets — kleiner Sprint mit hoher Marketing-Auswirkung).

**4. Crewmeister (DE, threat: MEDIUM als DE-KMU-Preis-Krieger + GPS-Baustellen-Fokus, ohne AI)**

Crewmeister ist **DE-KMU-Zeiterfassungs- und Schichtplan-Preis-Krieger** — mobile-first, GPS bis 2 m Genauigkeit, 30%-Rabatt-Kampagne 2026 (bis 12.06.2026 als Reaktion auf Zeiterfassungspflicht) (`crewmeister.com/de/preise`). Direkter Cosmi-`schichten`-Konkurrent im DACH-KMU-Handwerk/Pflege/Gastro/Produktions-Segment.

- **Preis-Aggressivitaet (Marktbenchmark-Kombi)**: Zeiterfassung ab **1.50 EUR/User-Monat**, Schichtplanung ab **2 EUR/User-Monat**, DATEV-Integration **0.60 EUR/User-Monat** — Kombi Zeit + Schicht + DATEV = **4.10 EUR/User-Monat**. Cosmi-Kombo schichten (4 EUR) + zeiterfassung (3 EUR) = **7 EUR/User-Monat** — **fast doppelt so teuer wie Crewmeister-Kombo**.
- **GPS-2m-Genauigkeit**: native App mit GPS-Location-Recording bei Clock-In/Out, DSGVO-konform durch punktuelle Erfassung (nicht kontinuierliche Ortung), Live-Status auf Baustelle. Cosmi hat `validateGPS`-Bounds-Check (NUMERIC(9,6) fuer lat/lon), aber keine 2-m-Genauigkeits-Marketing-Story.
- **Schichtplaner mit Drag-Drop**: Vorlagen, Schichttausch, automatische Benachrichtigungen — Cosmi hat gleiche Basis-Features.
- **Handwerk-Fokus-Marketing**: spezifische Landing-Pages fuer Bau/Handwerk (`crewmeister.com/de/magazin/die-beste-handwerkersoftware-2026`), Live-Status + GPS-Tracking als Baustellen-USP.
- **Kein AI-Feature 2026**: Fokus liegt auf 30%-Rabatt-Kampagne als Marketing-Antwort auf Zeiterfassungspflicht, nicht auf AI-Rennen.
- **Zeiterfassungspflicht-Marketing**: `crewmeister.com/de/magazin/zeiterfassungspflicht-2026-was-sie-wissen-muessen` als SEO-Anker — Rabatt-Kampagne 30% bei Buchung bis 12.06.2026.
- **Pain-Points G2/Capterra 2026**: "App gelegentlich instabil", "Offline-Sync in Funkloch nicht robust genug", "Integrationen ausser DATEV limitiert", "Enterprise-Schichtmodelle zu unflexibel".
- **Pricing (2026)**: Zeit ab **1.50 EUR/User**, Schicht ab **2 EUR/User**, DATEV **0.60 EUR/User**; Standard-Bundle ab **5.20 EUR/User/Monat**, Premium **9 EUR/User/Monat** (`omr.com/en/reviews/product/crewmeister/pricing`).
- **Tech-Stack**: DE-Cloud, native iOS/Android, DATEV-CSV-Export.
- **Gap zu Cosmi**: Preis-Aggressivitaet (Kombo 4.10 vs. Cosmi 7 EUR), GPS-2m-Genauigkeit im Marketing, native iOS/Android-App mit Handschuh-Bedien-Optimierung, DATEV-CSV-Export.
- **Strategischer Hinweis**: **Crewmeister ist Cosmi's schaerfster Preis-Krieger im DACH-KMU-Segment** — 30%-Rabatt-Kampagne 2026 zeigt Preis-Sensitivitaet des Segments. Cosmi's Preis-Story bricht ohne Feature-Differenzierung. Sprint-Anker: (i) **Preis-Vergleichs-Story** in Marketing-Material — Cosmi-Kombo (schichten + zeiterfassung + rapporte + crm + email + calendar + wiki = ca. 25 EUR/User-Monat) vs. Crewmeister-Nur-Kombo (4.10 EUR/User-Monat + kein CRM + kein Wiki + kein E-Mail). Cross-Modul-Preis-Story ist Cosmi's Differenzierung, nicht Einzel-Modul-Preis. (ii) **GPS-Genauigkeits-Kommunikation** im UI — Cosmi hat NUMERIC(9,6) fuer lat/lon (6 Nachkomma-Stellen = ~11cm Praezision), das ist strukturell besser als Crewmeister's 2m — aber Cosmi kommuniziert das nicht. Kleiner Marketing-Sprint.

**5. Aplano (DE, threat: LOW-MEDIUM als DE-Preis-Krieger und Auto-Konflikt-USP)**

Aplano ist **DE-Cloud-Schichtplan mit aggressivem Einsteiger-Pricing** — deutsche Firma, DE-hosted (GDPR-konform), Fokus auf dezentrale Teams. Preis-Alternative zu Papershift ohne AI-Auto-Assign-Story, aber mit Auto-Konflikt-Erkennung.

- **Preis-Aggressivitaet (Core 0.50 EUR/MA!)**: Core **0.50 EUR/MA/Monat**, Basic **2 EUR/MA/Monat**, Pro **4.50 EUR/MA/Monat** — Cosmi ist mit 4 EUR/MA im Pro-Preis-Bereich (`aplano.de/preise`).
- **Monatlich kuendbar**: kein Jahres-Commitment (Marktbenchmark-Alternative zu Papershift Jahres-Abo mit Support-Zwang).
- **Auto-Konflikt-Erkennung (Kern-USP)**: Ueberlappungen, Abwesenheiten, ArbZG-Verstoesse werden bei Planung erkannt. Cosmi hat ArbZG §5 aber nicht die anderen Konflikt-Typen automatisiert.
- **DACH-Feiertag**: automatisch fuer DE/AT/CH inkl. Bundeslaender/Kantonen (aehnlich ShiftJuggler).
- **Shift-Exchange-Selbst-Service**: MA-Tausch mit Manager-Genehmigung.
- **Pain-Points OMR 2026**: "Lohnbuchhaltung geht ueber Partner (nicht direkt integriert)", "komplexe Schichtmodelle mit Zuschlags-Aufschlaegen brauchen Pro-Plan", "Feature-Breite ausserhalb Kern-Schichtplan schwaecher".
- **Pricing (2026)**: Core **0.50 EUR/MA/Monat**, Basic **2 EUR/MA/Monat**, Pro **4.50 EUR/MA/Monat**. 14-Tage-Testphase kostenfrei.
- **Tech-Stack**: DE-Cloud (GDPR-konform), mobile-App, DATEV-Partner-Integration.
- **Gap zu Cosmi**: Preis-Aggressivitaet (Core 0.50 EUR — 8-fach guenstiger als Cosmi), Auto-Konflikt-Erkennung breiter als nur ArbZG §5, DACH-Feiertag-Auto.
- **Strategischer Hinweis**: **Aplano's Core-Preis 0.50 EUR/MA ist strukturell Cosmi's schaerfstes Preis-Risiko im Low-End** — fuer preis-sensible Micro-KMU (5-15 MA) ist Aplano Core (0.50) fast **8x guenstiger** als Cosmi (4 EUR). **Aber**: Aplano Core hat begrenzte Features (kein DATEV, keine Lohnbuchhaltung, kein Enterprise-Feature-Set). Cosmi kann sich strukturell nur mit Cross-Modul-Story differenzieren (schichten + zeiterfassung + rapporte + crm + wiki gebuendelt) — Einzel-Modul-Preis-Story verliert gegen Aplano. Sprint-Anker: (i) **Cross-Modul-Bundle-Rabatt** explizit im Pricing kommunizieren (5+ Module = 20% Bundle-Rabatt zum Beispiel), (ii) **Cosmi-Free-Tier fuer <10 MA** oder **Cosmi-Micro-Plan** (5 EUR/Monat flat fuer bis 10 MA an einem Standort mit schichten + zeiterfassung + rapporte + email) — Marketing-Anti-Aplano-Story.

**6. Planday (DK/Xero, threat: MEDIUM DACH-Konkurrent mit Agentic-AI-Ambition + Xero-Rueckenhalt)**

Planday ist **DK-Kopenhagen-Schichtplan-Anbieter mit Xero-Ownership** — von Xero (AU/NZ-Buchhaltungs-Cloud) im August 2018 uebernommen fuer 250M USD, ab $2/User-Monat einsteigende Preise, DACH-Sprache aktiv (`planday.com`). Enterprise-orientierter als Papershift, aber unter Shyftplan-Niveau.

- **"Smart AI-powered Rotas" mit Agentic-AI-Ziel**: aktive Roadmap-Kommunikation "**industry's first truly Agentic AI experience**" fuer Schicht-Management (`planday.com`). Winter/Spring 2026 Updates: neue Performance Overview (welche MA und Tage generieren am meisten Umsatz), verbesserte Timesheet-Break/Supplement-Management (`help.planday.com/en/articles/621960-product-updates-winter-and-spring-2026`).
- **Predictive Forecasting**: staffing-Bedarf-Vorhersage per Shift mit klaren Reports/Forecasts.
- **Personio-Marketplace-Standard-Integration**: Planday ist neben Shyftplan die zweite Personio-Marketplace-Standard-Integration fuer Schichtplanung im DACH-KMU-Segment. Cosmi hat keine Personio-Integration — strukturelle Sales-Hemmung fuer Personio-Kunden.
- **Xero-Rueckenhalt**: Buchhaltungs-Cloud Xero (AU-NZ-Marktfuehrer) als Eigentuemer sichert Roadmap-Investition und Datenschutz-Depth.
- **Pain-Points G2 2026**: "Nordamerika/UK-Kunden-Fokus schwaecht DACH-Sprach-Depth" (obwohl DACH-Sprache aktiv), "AI-Rota noch Iterations-Modus, Marketing der Agentic-AI ist voraus dem Feature-Zustand".
- **Pricing (2026)**: **ab $2/User-Monat** — sehr niedriger Einstieg, aber Enterprise-Plan noetig fuer volle Feature-Palette.
- **Tech-Stack**: DK/Xero-Cloud, native iOS/Android, REST-API, Xero-Buchhaltungs-Integration, Personio-Marketplace-Integration.
- **Gap zu Cosmi**: Agentic-AI-Rota-Roadmap, Predictive-Forecasting, Xero-Buchhaltungs-Integration, Personio-Marketplace-Standard-Integration.
- **Strategischer Hinweis**: **Planday's Personio-Marketplace-Position ist strukturell relevant fuer Cosmi** — Personio ist DACH-KMU-HR-Standard, jede Cosmi-Sales-Story trifft irgendwann auf "Warum haben Sie keine Personio-Integration?"-Frage. Sprint-Anker: (i) **Personio-Integration fuer Cosmi-schichten** (Q4-2026-Sprint — Personio-Marketplace-Standard-Interface via `shyftconnect`-aehnliches Modell), (ii) **Predictive-Forecasting-Prototyp** fuer historische Schicht-Muster (Q4-2026 — nutzt Basis aus AI-Auto-Assign-Sprint). Cosmi kann Cross-Modul-Story spielen ("Cosmi hat CRM + Buchhaltung + Vertraege + Schichten in einem Stack, brauchen Sie keine Personio-Integration") — aber Personio-Bestandskunden werden gefragt.

**7. 7shifts (CA, threat: LOW im DACH, HIGH als ML-Auto-Scheduler-Muster)**

7shifts ist **CA-Toronto-Restaurant-Schichtplan-Marktfuehrer** — Nordamerika-Fokus, Restaurant/Gastro-Zielgruppe primaer, ML-Auto-Scheduler mit **8-10 vorherigen-Plaenen-Analyse** als Kern-AI-USP (`7shifts.com/pricing`). Nicht DACH-Cosmi-KMU-Konkurrent, aber ML-Pattern-Musteranker fuer Cosmi's Auto-Assign-Design.

- **ML-Auto-Scheduler mit historischer Muster-Erkennung**: analysiert 8-10 vorherige Plaene fuer Staffing-Muster + Labor-Cost + Sales-Forecast + Overtime + Time-Off + Availability + Labor-Compliance. Kein LLM, sondern klassisches ML.
- **POS-Integration fuer Sales-Forecast**: pull Sales-Daten aus POS-System (Toast, Square, Clover) fuer Labor-Cost-Forecast — Personal-Bedarf skaliert mit erwartetem Umsatz.
- **Tip-Management + Task-Management + Advanced Labor Forecasting (Premium)**: Restaurant-spezifische Features im Premium-Plan.
- **Plan-Redesign Juli 2025**: alte Namen (Comp/Entree/Works/Gourmet) → neue Namen (Comp/Essentials/Pro/Premium).
- **Pain-Points G2 2026**: "Nicht optimal fuer Nicht-Restaurant-Branchen", "Preis-Uplift auf hoeheren Plaenen versperrt KMU-Zugang", "US-Hosting-DSGVO-Fragen fuer DACH-Kunden".
- **Pricing (2026)**: Comp **kostenfrei** (1 Location, bis 15 MA), Essentials **39.99 USD/Monat** (+ Team-Messaging + Time-Clocking), Pro **89.99 USD/Monat** (+ Labor Compliance + Performance), Premium **149.99 USD/Monat** (+ Tip-Management + Task-Management + Advanced Labor Forecasting). Jahres-Abo spart 10-12%.
- **Tech-Stack**: US-Cloud, native iOS/Android, POS-Integrations-Stack.
- **Gap zu Cosmi**: ML-Muster-Erkennung aus historischen Plaenen, POS-Sales-Forecast-Integration, Tip-Management (Gastro-USP).
- **Strategischer Hinweis**: **7shifts ist kein DACH-Cosmi-Konkurrent, aber der ML-Muster-Erkennungs-Ansatz ist strukturell wichtig fuer Cosmi's Auto-Assign-Design**. Statt "regel-basierter Constraint-Solver von Scratch" kann Cosmi den 7shifts-Ansatz mimen: analysiere die letzten 8-10 Wochen an `shifts` + `shift_assignments` pro Tenant, extrahiere Muster (welche MA fahren welche Slots), schlage Muster-basierten Plan fuer die kommende Woche vor. Das ist **ML-lite** (statistische Analyse, keine Trainings-Pipeline), passt gut in Go-Backend (kein Python-Zwang), und liefert 80% der User-Experience-Value fuer 20% der Sprint-Kosten. Sprint-Anker: **Muster-Erkennungs-Prototyp** (Q3-2026) als Vorlage-Muster-Extraktion, dann Manager-Preview vor Publish.

**8. Deputy (AU/US, threat: MEDIUM international mit Deputy-AI-Platform als agentischer AI-Benchmark)**

Deputy ist **AU-Sydney-Schichtplan-Anbieter mit 1.5M-Shift-Workers weltweit** (`deputy.com`) — 380k Arbeitsplaetze in 100+ Laendern, **Deputy AI Platform November 2025 GA gelaunched** auf AWS Bedrock/GenAI (`news.deputy.com/deputy-launches-new-ai-platform-on-aws`). DACH-Depth niedriger als Ordio.

- **Deputy AI Platform (November 2025 GA)**: intelligent + proactive workforce management assistant, assessiert Schedule/Attendance-Daten fuer schnelle Antworten, agiert autonom fuer angeforderte Aktionen — **agentischer AI-Ansatz mit AWS Bedrock/GenAI-Stack**.
- **Drei AI-Kern-Faehigkeiten (2025-2026-Investition)**: (i) Auto-Scheduling aus Demand + Availability, (ii) Demand-Forecasting aus historischen Sales/Operational-Patterns, (iii) AI Agent als ambitioniertester Agentic-Ansatz — in Entwicklung.
- **Global-Scale**: 1.5M shift-workers, 380k Arbeitsplaetze, 100+ Laender.
- **Pain-Points G2 2026**: "DACH-Rechts-Depth niedriger als Ordio fuer deutsche Arbeitsrecht-Regeln", "AI-Platform noch Iterations-Modus", "Preis-Uplift auf hoeheren Plaenen".
- **Pricing (2026)**: Core **6.50 USD/User/Monat**, Pro **9 USD/User/Monat**; Add-Ons: Deputy HR **2 USD/User/Monat**, Analytics+ **1.50 USD/User/Monat**, Messaging+ **1.95 USD/User/Monat**.
- **Tech-Stack**: AU/US-Cloud, native iOS/Android, AWS Bedrock/GenAI, REST-API.
- **Gap zu Cosmi**: Deputy-AI-Platform mit AWS Bedrock/GenAI-Stack, 100+-Laender-Reach, Add-On-Preis-Modell (Core-Preis niedrig, Zusatz-Features als Add-On).
- **Strategischer Hinweis**: **Deputy AI Platform ist der agentische AI-Marktbenchmark 2026** — der AWS-Bedrock-Stack ist AI-Vendor-Signal (agentic AI mit Anthropic Claude Sonnet 3.5 wahrscheinlich, alternativ Amazon Nova). Fuer Cosmi ist der agentische AI-Ansatz nicht Sprint-Prioritaet H2 2026, aber **relevanter Benchmark fuer H1 2027-Roadmap**. Cosmi's Cross-Modul-Story (schichten + zeiterfassung + rapporte + crm) hat mehr Cross-Domain-Automations-Potenzial als Deputy's Single-Modul-Fokus — das ist ein Cosmi-Differential wenn AI-Agent-Story kommt.

**9. Connecteam (IL/US, threat: MEDIUM als Frontline-Mobile-First-Benchmark)**

Connecteam ist **Israel-Tel-Aviv-Frontline-Workforce-Management-Anbieter** — mobile-first, 3 Subscription-Hubs (Operations + Communications + HR & Skills), AI-Auto-Scheduling mit Konflikt-Flag als Kern-USP. Threat fuer Cosmi im Frontline-Mobile-Segment.

- **AI-Auto-Scheduling mit Konflikt-Flag**: erkennt Overlap-Schichten, Doppel-Booking, Schichten waehrend approved Time-Off — Manager-Warnungen vor Publish.
- **GPS-Geofencing + Real-time Breadcrumb-Tracking**: Standort-Verifikation waehrend Schicht, Live-Bewegung — DSGVO-fragwuerdig in DE-BR-Umfeld, aber effektiv fuer Field-Manager.
- **3 Hubs (Operations/Communications/HR-Skills)**: jeder separate Subscription-Kette — Preis-Struktur-Split.
- **Free-Tier fuer <10 MA**: Basic-Plan Free (bis 10 User) als Anker fuer Micro-KMU.
- **Frontline-mobile-first**: kommuniziert als "beste Wahl fuer Small Business Frontline" (`connecteam.com/reviews/7shifts`).
- **Pain-Points G2 2026**: "3-Hub-Struktur verwirrt Kunden — brauchst du 2 Hubs, zahlst du 2 Subscriptions", "Nicht DACH-Rechts-optimal (Israel/US-Fokus)", "Enterprise-Feature-Set schwaecher als Deputy".
- **Pricing (2026)**: Basic **29 USD/Monat** (bis 30 User inkl., dann 0.50 USD/extra User), Advanced **49 USD/Monat**, Expert **99 USD/Monat**. Free-Plan (bis 10 User) fuer Micro-KMU.
- **Tech-Stack**: US/IL-Cloud, native iOS/Android (mobile-first), REST-API.
- **Gap zu Cosmi**: mobile-first Frontline-UX, GPS-Geofencing, Free-Tier fuer <10 MA, AI-Auto-Sched mit Konflikt-Flag.
- **Strategischer Hinweis**: **Connecteam's Free-Tier fuer <10 MA ist strukturell relevant fuer Cosmi's Free-Trial-Story**. Cosmi hat heute keinen Free-Tier — jeder Kunde zahlt ab Modul-Buchung. Sprint-Anker: (i) **Cosmi-Free-Trial-Modus** fuer 30 Tage komplett kostenfrei (kein Sprint-Aufwand, nur Sales-Prozess-Aenderung), (ii) **Cosmi-Micro-Free-Tier** fuer <5 MA an einem Standort mit 3 Basis-Modulen (email + calendar + chat) — kleiner Sprint mit hoher Marketing-Auswirkung.

**10. Sona (UK/US, threat: NEW/LOW-MEDIUM als AI-Frontline-Konsolidator)**

Sona ist **UK-London-AI-Frontline-Workforce-Startup** — im **April 2026 45M USD Series B geraised** (kumulativ >100M USD, `prnewswire.com/news-releases/sona-raises-45m-series-b-to-bring-ai-to-the-frontline-economy`), vertikal integrierte Plattform (Scheduling + HR + Payroll + Time + BI + Employee-Communications). Neuer AI-First-Konsolidator.

- **Sona Forge (Q1 2026 GA)**: Enterprise-AI-App-Builder — Organisationen bauen custom Software mit AI, autom. deployed und mit Sona-Kern-Daten/Analytics integriert.
- **AI-Auto-Sched mit Cost/Coverage/Compliance-Balance**: **70% Open-Shifts <24h gefuellt** durch intelligente Notifications an eligible Staff.
- **Vertikal integriert**: Scheduling + HR + Payroll + Time + BI + Employee-Communications in einer Plattform, AI durchdringt jeden Layer.
- **Series-B-Momentum**: $45M April 2026, kumulativ >$100M, US-Expansion aktiv.
- **Frontline-Zielgruppe**: Enterprise-Frontline (Retail, Healthcare, Manufacturing).
- **Pain-Points (frueh Iterations-Modus)**: "AI-Feature-Story lauter als Feature-Zustand", "Enterprise-Preis-Bereich (nicht KMU-Zugriff)", "US/UK-Fokus, wenig DACH-Depth".
- **Pricing (2026)**: nicht oeffentlich transparent (Enterprise-Kontakt-Modell).
- **Tech-Stack**: UK/US-Cloud, native mobile, REST-API, integrierte HR-Payroll.
- **Gap zu Cosmi**: Sona Forge als AI-App-Builder, vertikale Voll-Integration, Series-B-Funding-Momentum.
- **Strategischer Hinweis**: **Sona ist AI-First-Konsolidator, Cosmi ist Modul-Konsolidator** — beide bauen Cross-Domain-Plattformen, aber Sona ist AI-native, Cosmi ist Modul-native. Der Konsolidations-Vertikal-Ansatz ist strukturell aehnlich Cosmi's Ziel-Modell — Sona liefert Muster fuer Cross-Domain-Datenintegration + AI-Layer. Sprint-Anker: keine direkt uebernehmbar, aber Sona Forge als AI-App-Builder-Muster ist strategisch interessant fuer Cosmi's `automatisierung`-Modul-Roadmap (nicht Sprint 2 Ziel).

**11. ShiftJuggler (DE, threat: LOW-MEDIUM als DACH-Feiertag-Auto-Benchmark + ArbZG-Auto)**

ShiftJuggler ist **DE-Berlin-Schichtplan-Anbieter mit DACH-Fokus** — zielt auf 10-2000+ MA Multi-Location, automatische Konflikt-Erkennung + DACH-Feiertag-Auto (DE/AT/CH inkl. Bundeslaender/Kantonen) (`shiftjuggler.com/vergleich/shiftjuggler-vs-papershift`).

- **DACH-Feiertag-Auto** (Marktbenchmark): DE-Bundeslaender + AT-Bundeslaender + CH-Kantone werden automatisch beruecksichtigt — kein Ostersonntag/Fronleichnam/Reformationstag-Verwaltungs-Aufwand fuer Manager.
- **Auto-Konflikt-Erkennung** (Marktbenchmark): Ueberlappungen, Abwesenheiten, ArbZG-Verstoesse (Ruhezeit + Pause + Wochenarbeitszeit) alle im Planungs-Vorgang erkannt.
- **Preis-Uplift 2026**: von 29 EUR/Monat auf **39 EUR/Monat** — bei Team-Kombi ~2.78 EUR/User (guenstiger als Papershift bei aehnlicher Team-Groesse ca. 200 EUR/Monat weniger).
- **Ungrenzenzte Custom-Abwesenheits-Typen**: Weiterbildung, Elternzeit, Berufsschule etc.
- **Pain-Points Trusted 2026**: "AI-Feature-Set schwaecher als Papershift", "keine Personio-Integration", "Feature-Breite ausserhalb Kern-Schichtplan schwaecher".
- **Pricing (2026)**: **ab 39 EUR/Monat** (Team-Preis), bei ~50 MA ca. 2.78 EUR/User.
- **Tech-Stack**: DE-Cloud, mobile-Apps, REST-API.
- **Gap zu Cosmi**: DACH-Feiertag-Auto mit Bundeslaender/Kanton-Support, Auto-Konflikt-Erkennung fuer ArbZG-Vollpalette, ungegrenzte Custom-Abwesenheits-Typen.
- **Strategischer Hinweis**: **ShiftJuggler's DACH-Feiertag-Auto ist der schnellste Sprint-Anker fuer Cosmi** — Cosmi's `GERMAN_HOLIDAYS_2026` als hardcoded 9-Eintrag-Frontend-Map ist strukturell unhaltbar (jedes Jahr manuelle Update-PR). Sprint-Anker: **nager-date-npm-Library** (Client-side, gratis, DACH-Kanton-Support built-in) oder **`holidays`-Backend-Table** mit yearly-Cron-Job fuer Auto-Update — beide sind <3-Tage-Sprint mit hoher Marketing-Auswirkung ("Cosmi-Schichten mit DACH-Feiertag-Auto fuer DE/AT/CH inkl. Bundeslaender + Kanton").

**12. gastromatic (DE, threat: LOW, Gastro-Spezialist)**

gastromatic ist **DE-Gastro-Spezialist** — Gastronomie/Hotel/Baeckerei-Fokus, Umsatz-Forecast-basierte Personal-Planung (`gastromatic.com/de/digitaler-dienstplan`).

- **Umsatz-Forecast-basierte Personalplanung**: kombiniert Schicht-Planung mit Umsatz-Vorhersage — Gastro-USP.
- **Branchen-Fokus Gastro/Hotel/Baeckerei**: nicht Cosmi-Zielgruppe (Cosmi ist Handwerk/Retail/Dienstleister/IT).
- **Pricing (2026)**: Starter **7 EUR/MA/Monat** (+ 135 EUR-Setup), Professional auf Anfrage.
- **Gap zu Cosmi**: Umsatz-Forecast-basierte Personalplanung (nicht Cosmi-Prioritaet), Gastro-spezifische Templates.
- **Strategischer Hinweis**: **gastromatic ist Nicht-Cosmi-Konkurrent** — keine direkten Sprint-Ziele.

**13. HERO Software (DE, threat: MEDIUM als Handwerk-ERP mit Plantafel + Zeiterfassung, teuer)**

HERO Software (bereits im W28-rapporte-Deepdive detailliert) — DE-Handwerker-ERP mit HERO App als digitale Stempeluhr + Plantafel-Ressourcenplanung + digitale Urlaubs-Antraege. Threat fuer Cosmi im Handwerk-Segment, aber Preis-Positioning HERO Core 69 EUR/User-Monat schliesst KMU 5-30 MA weitgehend aus.

- **HERO App als digitale Stempeluhr**: Arbeitsbeginn/Pausen/Arbeitsende per Knopfdruck auf Smartphone/Tablet (`hero-software.de/features/zeiterfassung-app`).
- **Plantafel-Ressourcenplanung**: digitale Plantafel fuer Personal-Planung (Handwerk-Baustellen-Zuordnung).
- **Arbeitszeitkonto + Urlaubsantraege digital**: Contract-Details fuer MA, Urlaubsantraege digital eingereicht + genehmigt/abgelehnt.
- **HERO Voice + HERO Report + HERO Command AI-Roadmap**: bereits in W28-rapporte-Deepdive dokumentiert.
- **Pricing (2026)**: HERO Core **ab 69 EUR/User/Monat** (jaehrlich, 79 EUR monatlich), HERO OS **119-135 EUR/Monat inkl. 1 Standard-Lizenz**, HERO OS Plus **299-345 EUR/Monat**, HERO AI Launch-Rabatt **59 EUR/Lizenz** (`hero-software.de/preise`).
- **Gap zu Cosmi**: HERO App als digitale Stempeluhr (Cosmi hat `zeiterfassung`-Modul separat, aber HERO integriert Zeit + Plan + Auftrag in einer App), Plantafel-Ressourcenplanung fuer Baustellen-Zuordnung.
- **Strategischer Hinweis**: **HERO ist Cosmi-Handwerk-Segment-Preis-Barrier-Konkurrent** — 69 EUR/User-Monat schliesst KMU 5-30 MA aus, Cosmi 4 EUR/User-Monat ist 17-fach guenstiger, aber HERO liefert integrierte ERP-Story. Cosmi-Sales-Differential: **Cosmi-Kombo (schichten + zeiterfassung + rapporte + crm + email + calendar = 20 EUR/User-Monat) vs. HERO Core 69 EUR/User-Monat** — 71% guenstiger fuer mehr Modul-Coverage.

**14. Personio (DE, threat: HIGH als Katalysator — Cosmi-Ersatz-Story)**

Personio ist **DE-Muenchen-HR-Suite-Marktfuehrer** — nicht direkt Schichtplan-Konkurrent, aber **Katalysator fuer Cosmi's Sales-Positionierung**. Personio-Bestandskunden fragen nach Personio-Integration bei jeder neuen Software-Buchung.

- **Attendance-Policies-Update 2026**: separater Working-Hours + Time-Tracking + Overtime-Settings (`community.personio.com/product-spotlight-133/attendance-policies-making-attendance-settings-in-personio-more-flexible-than-ever`), temporary Assignments, Conflict-Checks, Archiving.
- **Overnight-Time-Tracking**: Schichten die Mitternacht ueberspannen als single continuous Entry — kritisch fuer Nacht-Schichten (Pflege, Gastro, Sicherheit).
- **Fixed/Multi-Week/Flexible Schedules**: drei Schedule-Typen fuer verschiedene Arbeitsmodelle.
- **Personio-Marketplace-Standard-Integrationen fuer Schichtplanung**: Shyftplan + Planday (beide Enterprise/Mid-Market). Cosmi 0.
- **DACH-KMU-Standard**: fuer 50-500-MA-KMU der DACH-HR-Standard.
- **Pricing (2026)**: modul-basiert, Enterprise-Preise, in der Regel ab 3-8 EUR/User/Monat je Modul-Set.
- **Gap zu Cosmi**: HR-Suite-Breite (Cosmi's Modul-Ansatz ist Alternative), Personio-Marketplace-Integration ist Sales-Anforderung.
- **Strategischer Hinweis (WICHTIGSTER SALES-PUNKT DIESES REPORTS)**: **Cosmi-Schichten kann Personio-Bestandskunden nur mit Personio-Integration erreichen**. Sprint-Anker: **Personio-Marketplace-Integration** (Q4-2026-Sprint — Personio-Marketplace-Standard-Interface, siehe `marketplace.personio.com/integrations/shyftplan` fuer Muster). Alternative Cross-Modul-Story ("Cosmi hat HR/CRM/Buchhaltung/Vertraege/Schichten integriert, warum brauchen Sie Personio?") funktioniert nur fuer Neu-KMU, nicht fuer Personio-Bestand.

**Weitere DACH-KMU-Anbieter im Ueberblick**:

- **Shiftbase (NL, threat: LOW im DACH)**: ab 35 EUR/Monat fuer 10 MA, DACH-Sprache aktiv, Fokus Retail/Gastro, kein AI-Kern.
- **StempelZeit (DE, threat: LOW)**: DE-Zeiterfassungs-App mit Bau-Fokus, `die-stempelzeit.de/ratgeber/zeiterfassung-pflicht-bau-2026` als SEO-Anker fuer Handwerk.
- **StaffOmatic (DE, threat: LOW)**: preis-bewusste KMU-Alternative zu Papershift.
- **123erfasst / mobiel / clockin (DE-Handwerk-Bau-Fokus)**: bereits im W28-rapporte-Deepdive detailliert — 123erfasst ist Handwerk-Bau-Marktfuehrer mit robust Offline + Baustellen-Foto-Doku aber ohne Schichtplanung-Kernfokus.

---

## Cosmi-IST-Stand

### Backend `backend/internal/schichten/` (7 Files, ~3155 LOC, Coverage 35.2%)

**Modell-Layer (`models.go` 91 LOC)**:
- `Shift` mit `Status` (`draft`/`published`), `Location *string`, `Capacity *int` (nil = unlimited), `CreatedBy *uuid.UUID`
- `ShiftAssignment` mit `AssignedAt`, `AssignedBy *uuid.UUID`
- `ShiftTemplate` mit `DayOfWeek 0..6`, `StartHour 0..23`, `StartMinute 0..59`, `DurationMinutes >0`, `Location *string` — **kein Color, kein BreakMinutes** (Frontend faelscht Defaults `#3b82f6` und `30`)
- `ShiftStats` mit 5 Metriken (`TotalShifts`, `PublishedShifts`, `DraftShifts`, `TotalAssignments`, `UniqueEmployees`)
- `SwapRequest` mit `Status` (`pending`/`approved`/`rejected`), `IdempotencyKey`, `Reason`, `AssignmentID` + `ShiftID` + `RequestedByEmployeeID` + `SwapWithEmployeeID`

**Service-Layer (`service.go` 736 LOC, 22 Methoden)**:
- **Kern-CRUD Shifts**: `CreateShift` (validiert Title + EndTime > StartTime), `UpdateShift` (patch mit End>Start-Reval), `DeleteShift` (CASCADE via `shift_assignments.shift_id FK`), `GetShift`, `ListShifts` (Filter Status/From/To + Pagination Page/PageSize 1..200)
- **Bulk-Publish**: `PublishShifts(from, to)` idempotent, RowsAffected-Sentinel
- **Assignment-Guards**: `AssignEmployee` mit Capacity-Check (`ErrShiftFull`) + ArbZG §5-Check (`validateRestPeriod`)
- **Template-CRUD**: `CreateTemplate`, `UpdateTemplate`, `DeleteTemplate`, `GetTemplate`, `ListTemplates`, `ApplyTemplate` mit Idempotency-Guard via `ShiftExistsForTemplate` (skip duplicate)
- **Compliance-Check**: `CheckArbzgCompliance` als Read-only Pre-Check (kein DB-Write, prueft `validateRestPeriod` + gibt Fehler-Message zurueck)
- **Stats**: `GetShiftStats` mit optionalem From/To-Filter
- **Swap-Request-Machine**: `CreateSwapRequest` (IdempotencyKey required, RequestedBy ≠ SwapWith Check), `ListSwapRequests`, `ApproveSwapRequest` (atomarer `SwapAssignmentsForRequest` + `UpdateSwapRequestStatus`), `RejectSwapRequest`

**Internal-Helper `validateRestPeriod`**:
- Konstante `arbzgMinRestDuration = 11 * time.Hour` (`service.go:13`)
- Beide Richtungen: `LatestShiftEndBeforeForEmployee(newStart)` + `EarliestShiftStartAfterForEmployee(newEnd)`
- Bei rest < 11h → `ErrArbzgViolation`
- DST-Spring-Forward-tauglich via `time.LoadLocation("Europe/Berlin")` in `ApplyTemplate`

**Errors (`errors.go` 15 LOC)**:
- `ErrShiftNotFound`, `ErrTemplateNotFound`, `ErrAssignmentNotFound`, `ErrInvalidInput`, `ErrAlreadyAssigned`, `ErrArbzgViolation`, `ErrShiftFull`, `ErrSwapRequestNotFound`, `ErrSwapAlreadyProcessed`

**Migrations-Historie**:
- **000094** `create_schichten` — `shifts` + `shift_assignments` + `shift_templates` Tabellen mit Indizes (tenant_id, tenant_status, tenant_period, published-partial)
- **000095** `seed_schichten_permissions` — permission-Rows fuer schichten Resource-Actions
- **000102** `shift_assignments_tenant_unique` — Sicherheits-Fix: vorher konnte gleiche `(shift_id, employee_id)` cross-tenant kollidieren
- **000122** `rls_phase2_long_tail` — RLS-Aktivierung fuer 15+ Tabellen inkl. schichten
- **000160** `create_swap_requests` — `shift_swap_requests` mit `idempotency_key UNIQUE` + `swap_employees_differ` CHECK
- **000161** `seed_swap_request_permissions` — swap-Permissions
- **000224** `seed_module_manager_member_permissions` — Manager voll operativ (40 Grants), Member Self-Service (8 Grants inkl. `schichten:swap:read|create`)

**Permission-Layer (aus Migration 000224)**:
- **Admin** (implicit via Migration 000002-CROSS-JOIN): voll operativ
- **Manager**: voll operativ ueber alle schichten-Resources (`schichten:shift:*`, `schichten:template:*`, `schichten:assignment:*`, `schichten:swap:*`)
- **Member**: Self-Service `schichten:swap:read`, `schichten:swap:create` (kann Swap-Request stellen, aber nicht approven), plus `schichten:shift:read` (kann eigene Schichten lesen)

**Feature-Flag**:
- `modules.schichten` (`registry.go:77`)
- DefaultEnabled: false
- EnvVar: `COSMI_MODULE_SCHICHTEN_ENABLED`
- Risk: SafeRisk
- LLMToggleSafe: true (LLM darf per Chat-Command aktivieren)

**Ports**:
- gRPC 50075
- HTTP 9115 (`hr-time`-Sub-Route ueber `route_schichten.go`)

**Test-Coverage**:
- 38 Tests in `service_test.go` (1430 LOC)
- Tenant-Isolation-Phase-2-Tests in `tenant_isolation_phase2_test.go` (74 LOC)
- Coverage 35.2% (unter 40%-Referenz-Ziel `.knowledge/testing.md`)

### Frontend `desktop/src/renderer/src/modules/schichten/SchichtenPage.tsx` (1661 LOC Mono-Page)

**4 Tabs**:
- `wochenplan` — Kalender-Woche mit Drag-Drop-Zuweisung
- `vorlagen` — Template-Verwaltung
- `anfragen` — Swap-Request-Verwaltung (mit `pending`/`approved`/`rejected` Status-Colors)
- `verfügbarkeit` — Verfuegbarkeits-Grid (Frontend-Mock only)

**Frontend-Only-Features (nicht Backend-persistiert)**:
- **`SHIFT_STYLE_MAP`** fuer 3 Template-Slots (`tpl-1` Sun/info, `tpl-2` Sunset/warning, `tpl-3` Moon/primary)
- **`SURCHARGE_RULES`** (Nacht +25%), **`WEEKEND_SURCHARGE`** (+50%), **`HOLIDAY_SURCHARGE`** (+100%) — Cross-Divergenz mit Backend
- **`GERMAN_HOLIDAYS_2026`** als hardcoded Map fuer 9 DE-Feiertage 2026 (Neujahr, Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt, Pfingstmontag, Tag der Deutschen Einheit, 1./2. Weihnachtstag) — kein Bundesland/Kanton, kein AT, kein CH
- **`AVAILABILITY_MOCK`** fuer 4 Mock-User (`u-1`/`u-3`/`u-6`/`u-8`) mit `green`/`yellow`/`red` per Wochentag — kein Backend-Table

**API-Client**:
- `useSchichten` als React-Query-Hook-Familie: `useTemplatesList`, `useCreateTemplate`, `useUpdateTemplate`, `useDeleteTemplate`, `useAssignEmployee`, `useUnassignEmployee`, `useCreateShift`, `usePublishShifts`, `useShiftsWithAssignments`, `useSwapRequests`, `useCreateSwapRequest`, `useApproveSwapRequest`, `useRejectSwapRequest`
- Nutzt zentralen `authenticatedFetch` (Sprint 2 Welle 4A Pattern)

**ArbZG-Warnungs-Palette** (`ArbZGViolation.type`):
- `max_hours` — Backend-blind (kein `validateMaxHours` in service.go)
- `rest_period` — Backend-Impl vorhanden (`validateRestPeriod`)
- `break_missing` — Backend-blind
- `consecutive_days` — Backend-blind

### Preis-Anker (`.knowledge/pricing.md`)

- Schichten-Modul: **4 EUR/User-Monat**
- Markt-Vergleich in Cosmi-Docs: "Spezialsoftware 5-10 EUR" (also Cosmi ist im unteren Preis-Segment gegen Spezialsoftware)
- Handwerk-Paket (CRM + Aufgaben + Kalender + Chat + Zeiterfassung + Buchhaltung + Rapporte + Schichten): **~26 EUR/User-Monat**
- Produktion-Paket (CRM + Aufgaben + Kalender + Chat + Produktion + Inventar + Schichten + Zeiterfassung + Fuhrpark): **~33 EUR/User-Monat**

### Bekannte Schulden

- **R3-P0-3 offen** (`.knowledge/security.md`): schichten ist eines der 13 Binaries ohne `TenantInboundUnaryInterceptor` — gRPC-Ebene ist noch nicht mandant-getrennt (RLS-Tabelle fuellt in Phase 2, aber gRPC-Handler koennten Cross-Tenant-Sniffen bei aktiviertem Modul).
- **Frontend-Backend-Divergenz** in 4 Feature-Bereichen (Surcharges/Availability/Feiertag/ArbZG-Warnungs-Palette) — siehe Beobachtung #3 im Header.
- **Kein AI-Auto-Assign** — Kern-Marktbenchmark-Luecke (siehe Beobachtung #1).
- **`arbzgMinRestDuration` hardcoded** als Konstante — kein Tenant-Setting, kein Krankenhaus/Gastro-Ausnahme (siehe Beobachtung #2).
- **Coverage 35.2%** unter 40%-Referenz-Ziel.
- **Kein `employee_qualifications`-Table** — kann Qualifikations-Matching nicht abbilden.
- **Kein `employee_availabilities`-Table** — kann Verfuegbarkeit nicht abbilden.
- **Kein DATEV/LODAS-Export-Anker** fuer schichten (nur `finance/datev`-Sub-Paket im Buchhaltungs-Modul, das ist nicht schichten-integriert).
- **Nur DE-Feiertage 2026 hardcoded** — kein DACH-Auto, kein Multi-Jahres-Support.
- **Kein Personio-Marketplace-Integration** — Sales-Barrier fuer Personio-Bestandskunden.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Papershift | Shyftplan | Ordio | Crewmeister | Planday | 7shifts | Deputy | Connecteam | Aplano | ShiftJuggler | HERO |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ziel-Segment** | 5-30 MA DACH-KMU | 5-500 MA DACH-KMU | 100+ MA Enterprise | 10-200 MA/Standort DACH | 5-100 MA DACH-KMU | 10-500 MA international | Restaurant global | 5-500 MA global | Frontline global | 5-500 MA DACH | 10-2000+ MA DACH | Handwerk 5-100 MA |
| **Pricing 4 EUR/User/Monat** | ✅ 4 EUR | 6 EUR (Premium) + 39 EUR Support | ab 700 EUR/Monat | 89-149 EUR/Standort | 2 EUR (Schicht) + 1.50 EUR (Zeit) | ab $2/User | $39.99-149.99/Monat | $6.50-9/User | $29-99/Monat | 0.50-4.50 EUR/User | ab 39 EUR/Monat | ab 69 EUR/User |
| **AI-Auto-Assign** | ❌ | ✅ (Premium) regel-basiert | ✅ 20+ Faktoren | ✅ | ❌ | ✅ Smart Rota | ✅ ML 8-10 Plaene | ✅ AWS Bedrock | ✅ mit Konflikt-Flag | 🚧 Auto-Konflikt | 🚧 Auto-Konflikt | ❌ |
| **Agentic AI (Roadmap)** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Ziel 2026 | ❌ | ✅ Deputy AI Agent | ❌ | ❌ | ❌ | ✅ HERO Voice |
| **Generative KI-HR-Chat** | ❌ | ✅ (mit Rechte-Aware) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Predictive Forecasting** | ❌ | ❌ | ✅ Demand-Forecast | ❌ | ❌ | ✅ | ✅ POS-Sales | ✅ Demand-Forecast | ❌ | ❌ | ❌ | ❌ |
| **Constraint-Solver** | 🚧 (nur ArbZG §5) | ✅ Verfuegbarkeit+Qualif. | ✅ 20+ Constraints | ✅ | ❌ | ✅ | ✅ Labor+Sales+Overtime | ✅ | ✅ Konflikt-Flag | ✅ | ✅ ArbZG-Full | ❌ |
| **Schicht-Templates** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Plantafel |
| **Template.Color** | ❌ (Frontend-Default) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Template.BreakMinutes** | ❌ (Frontend-Default 30) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Verfuegbarkeits-Selbst-Service** | ❌ (nur Frontend-Mock) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Qualifikations-Matching** | ❌ | ✅ (Premium) | ✅ (Kern) | 🚧 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Swap-Request-Selbst-Service** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 |
| **ArbZG §5 Auto (11h)** | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 (nicht DE-optimiert) | ❌ (US-Compliance) | 🚧 | 🚧 | ✅ | ✅ | ✅ |
| **ArbZG §3 (10h Tages-Max)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **ArbZG §4 (Pausen 30/45min)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **ArbZG §9-10 (Sonn/Feiertag)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Consecutive-Days-Regel** | ❌ | ✅ | ✅ | ✅ | ✅ | 🚧 | ❌ | 🚧 | 🚧 | ✅ | ✅ | 🚧 |
| **ArbZG-Constant konfigurierbar (Pflege/Gastro 10h Ausnahme)** | ❌ | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **DACH-Feiertag-Auto (DE/AT/CH mit Kanton)** | ❌ (nur DE hardcoded) | ✅ | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ | ❌ | ✅ | ✅ (Marktbenchmark) | ✅ |
| **Zuschlags-System (Nacht/Sonn/Feier)** | 🚧 (Frontend-Mock) | ✅ (Professional) | ✅ | ✅ | ✅ | ✅ | ✅ (Premium) | ✅ | ✅ | 🚧 | ✅ | ✅ |
| **Payroll-Berechnung (Zuschlag+Stunden)** | ❌ | ✅ (Professional) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 (via Partner) | ✅ | ✅ |
| **DATEV/LODAS-Export** | ❌ (nur Kombo-`finance`-Sub-Paket) | ✅ (Professional) | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ | ❌ | 🚧 (via Partner) | ✅ | ✅ |
| **Personio-Marketplace-Integration** | ❌ | ✅ | ✅ (Enterprise) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **SAP SuccessFactors/HCM/APO** | ❌ | 🚧 | ✅ (SAP-verifiziert) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Workday HCM Integration** | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Xero Buchhaltungs-Integration** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (Owner) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Multi-Site/Multi-Location** | 🚧 (nur `Shift.Location` als String) | ✅ | ✅ | ✅ (Kern-Preis-Modell) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (Multi-Location) | ✅ |
| **Native iOS App** | ❌ (nur Electron+PWA) | ✅ | ✅ | ✅ | ✅ (mobile-first) | ✅ | ✅ | ✅ | ✅ (mobile-first) | ✅ | ✅ | ✅ |
| **Native Android App** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **PWA + Offline-Mode** | 🚧 (Kein Service-Worker) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 | ✅ |
| **GPS-Geofencing bei Clock-In** | 🚧 (nur `validateGPS`-Bounds) | ✅ | ✅ | ✅ | ✅ (2m Genauigkeit) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Overnight-Schichten (00:00-06:00)** | ✅ (`start_time`/`end_time` als TIMESTAMPTZ) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Push-Notifications** | 🚧 (nur `notifications`-Modul-Kern) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Kapazitaets-Limit pro Schicht** | ✅ (`Shift.Capacity *int`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Bulk-Publish** | ✅ (`PublishShifts(from,to)`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Swap-State-Machine mit Idempotency** | ✅ (Swap-Requests seit Migration 000160) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 |
| **Manager/Member-Rollen-Modell** | ✅ (Migration 000224) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Umsatz-Forecast-Integration** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ (POS) | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Free-Tier** | ❌ | ❌ (14-Tage-Trial) | ❌ | ❌ | ❌ | ❌ | ✅ (bis 15 MA/1 Location) | ❌ | ✅ (bis 10 MA) | ❌ | ❌ | ❌ |
| **DE-Cloud (GDPR)** | ✅ (Hetzner) | ✅ | ✅ | ✅ | ✅ | ❌ (DK/UK) | ❌ (US) | ❌ (AU/US) | ❌ (IL/US) | ✅ | ✅ | ✅ |
| **Cross-Modul-Story (CRM+Buchhaltung+etc.)** | ✅ (Kern-Cosmi-USP) | 🚧 | ❌ | 🚧 (Branchen-Add-Ons) | 🚧 | 🚧 | ❌ | ❌ | 🚧 (3 Hubs) | ❌ | ❌ | ✅ (ERP) |
| **Open-Source-Verfuegbar** | ❌ (proprietaer) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Zusammenfassung**: Cosmi-schichten ist **Feature-Basis-solide** (Templates, Assignments, Swap-Requests, ArbZG §5, Capacity, Bulk-Publish, Manager/Member-Rollen) aber **strukturell zurueck** bei AI-Auto-Assign, Verfuegbarkeits-Backend, Qualifikations-Matching, Zuschlags-Payroll-System, DACH-Feiertag-Auto, ArbZG-Vollpalette, native Mobile-Apps, DATEV/LODAS-Export und Personio-Integration. Der Preis-Vorteil (4 EUR/User) ist **feature-adjusted schwach** gegen Papershift (6 EUR mit AI + Chat) und **stark** gegen HERO (69 EUR) oder Shyftplan (700 EUR/Monat Minimum). Der Preis-Nachteil gegen Aplano Core (0.50 EUR) und Crewmeister Basis (2 EUR Schicht + 1.50 EUR Zeit) ist strukturell — Cosmi kann sich nur Cross-Modul-differenzieren (schichten + zeiterfassung + rapporte + crm gebuendelt).

---

## Top-3 Strategische Empfehlungen

### 1. **AI-Auto-Assign-Heuristik Q3-2026-Prototyp + Q4-2026-GA** — Markt-Pflicht, nicht Nice-to-have

**Warum**: Papershift + Shyftplan + Ordio + Aplano + ShiftJuggler + Planday + 7shifts + Deputy + Sona + Connecteam haben **alle** live AI-Auto-Assign. Cosmi ist heute Feature-arm im wichtigsten DACH-KMU-Schichtplan-Kaufkriterium. Der Markt-Trend: 68% shift-based DACH-Arbeitgeber wollen AI-Forecasting bis Ende 2025 pilotieren (`cognitivemarketresearch.com`).

**Was**: Regel-basierter Auto-Assign-Heuristik-Backend-Job (nicht LLM, nicht Trainings-Pipeline noetig — 7shifts-ML-lite-Pattern) mit:
- **Input-Constraints**: Verfuegbarkeit (aus neuem `employee_availabilities`-Table), Qualifikationen (aus neuem `employee_qualifications`-Table), ArbZG §5 (bestehend + §3/§4/§9-10 neu), Kapazitaet (bestehend), Fairness (Auslastungs-Balance ueber MA)
- **Muster-Erkennung**: Analyse der letzten 4-8 Wochen `shifts` + `shift_assignments` fuer wiederkehrende MA-Slot-Zuordnungen
- **Solver**: einfacher Greedy-Algo mit Constraint-Priorisierung (Backend-Go, kein Python-Zwang, keine externe ML-Library)
- **UI**: Manager-Button "Woche automatisch fuellen" → Preview-Screen mit Aenderungs-Diff → Publish-Button
- **Fallback**: bei Constraint-Konflikt (kein zulaessiger MA-Slot findbar) UI-Anzeige der ungefuellten Slots mit Konflikt-Erklaerung

**Vorbereitungs-Sprints (Q3-2026-Pflicht vor Auto-Assign)**:
- `employee_availabilities`-Backend-Table + Self-Service-API + Frontend-Ersatz des `AVAILABILITY_MOCK` (2-3 Wochen)
- `employee_qualifications`-Backend-Table + Admin-Zuweisungs-Endpoint + Frontend-Zuweisungs-UI (1-2 Wochen)
- ArbZG §3/§4/§9-10 + Consecutive-Days-Backend-Impl (2 Wochen)
- `arbzgMinRestDuration` von Konstante auf Tenant-Setting migrieren (1 Woche, siehe Empfehlung #2)

**Auto-Assign-Sprint (Q3-Q4-2026)**:
- Backend-Job `AutoAssignShifts(tenantID, weekStart, weekEnd) []*ShiftAssignment` (2-3 Wochen)
- Frontend "Woche automatisch fuellen"-Button + Preview-Modal (1-2 Wochen)
- Fairness-Constraint + Muster-Erkennungs-Layer (2 Wochen)
- Test-Coverage 50%+ auf Auto-Assign (1 Woche)

**Erwartete Marketing-Auswirkung**: "Cosmi-Schichten mit AI-Auto-Assign — 5 EUR/User-Monat" (nach 25% Uplift ab AI-GA, oder gleicher Preis mit AI als Value-Add). Positioning: "Papershift-Premium-Features zu 17% weniger Preis, DE-hosted, DSGVO-nativ, Cross-Modul-integriert mit CRM/Buchhaltung/Vertraege".

### 2. **`arbzgMinRestDuration` Tenant-Setting + ArbZG-Full-Palette-Impl** — Regulatorische Positionierung

**Warum**: Der Referentenentwurf 18.06.2026 zerbricht Cosmi's `11 * time.Hour`-Constant — Pflege/Gastro/Verkehr/Rundfunk/Landwirtschaft duerfen 10h Ruhezeit fahren, Tarifvertraege koennen 11h ganz aufheben. Der aktuelle Cosmi-Code kann **keine Pflege-KMU + keine Gastro-KMU + keine Verkehrs-KMU als Kunden bedienen** die mit Tarifvertrag-Ausnahmen arbeiten. Zusaetzlich fehlt Cosmi §3 (10h Tages-Max), §4 (Pausen 30/45min), §9-10 (Sonntag/Feiertag), Consecutive-Days — alles Marktbenchmarks bei Papershift/Aplano/ShiftJuggler/Crewmeister.

**Was**: 
- **`hr_company_settings.min_rest_hours_default INT DEFAULT 11`** — Tenant-weite Default-Ruhezeit
- **`shift_arbzg_overrides`-Tabelle** mit `id`, `tenant_id`, `industry_code VARCHAR` (Pflege/Gastro/Verkehr/Rundfunk/Landwirtschaft), `min_rest_hours INT` (10 fuer Ausnahmen), `tarif_reference TEXT` (Tarifvertrag-Referenz fuer Audit), `activated_by UUID`, `activated_at TIMESTAMPTZ`, `justification TEXT`
- **`validateRestPeriod`** liest `min_rest_hours` aus Tenant-Setting statt Konstante
- **Neue Service-Methoden**: `validateDailyMaxHours` (§3), `validateBreakRules` (§4), `validateWeeklyRestDay` (§9-10 Sonntag), `validateConsecutiveDays` (max 6 Tage in Folge)
- **`CheckArbzgCompliance`** erweitert um alle Rules
- **Frontend-`ArbZGViolation.type`** wird Backend-persistiert (alle 4 Typen jetzt echt statt Placeholder)
- **UI-Compliance-Warnungen** vor Publish mit klaren Erklaerungen

**Sprint-Aufwand**: 3-4 Wochen (Backend + Tests + Frontend-Ersetzung der Placeholder-Types)

**Sales-Story**: "Cosmi-Schichten ist ArbZG-2026-Reform-ready — konfigurierbare Ruhezeit fuer Pflege/Gastro/Verkehr, volle §3-§10-Warnungen, Tarifvertrag-Auto-Ausnahmen mit Audit-Log". Marketing-Anker fuer Pflege-KMU (Krankenhaus + Altenheim + ambulante Pflege — DACH-Riesen-Marktsegment 2 Mio Pflege-MA in DE), Gastro-KMU (Restaurants + Hotel + Cafe), Verkehr-KMU (Speditionen + Taxi + Buslinien).

**Erwartete Marketing-Auswirkung**: Cosmi-Kunden-Ansprache-Markterweiterung um **Pflege/Gastro/Verkehr-Segmente** die heute wegen ArbZG-Ausnahme-Bedarf ausgeschlossen sind — DACH-KMU-Marktzuwachs von schaetzungsweise 30-40% des adressierbaren KMU-Marktes.

### 3. **Frontend-Backend-Divergenz-Fix: Availability-Backend + DACH-Feiertag-Auto + Zuschlags-System** — Prod-Story schliessen

**Warum**: Cosmi's Schichten-Modul ist heute **UI-vs-Backend-inkonsistent** — der `SchichtenPage.tsx` verspricht Verfuegbarkeits-Tab, Zuschlags-Anzeige, DACH-Feiertag-Anzeige, ArbZG-Vollpalette, aber Backend liefert das nicht. Sobald Kunden diese Features nutzen wollen (Zuschlaege fuer Payroll, Feiertags-Auto-Erkennung, Verfuegbarkeits-Selbst-Service), ist Backend nachzuziehen — und das ist non-trivial. Der Sprint-Anker fuer Auto-Assign (Empfehlung #1) hat `employee_availabilities`-Backend als Pflicht-Vorbereitung, dieser Sprint kann parallel oder vorgezogen laufen.

**Was**:

**(a) `employee_availabilities`-Backend** (2-3 Wochen):
- Tabelle `employee_availabilities` mit `id`, `tenant_id`, `employee_id`, `weekday INT (0-6)`, `hour_start INT`, `hour_end INT`, `availability_level ENUM(available/limited/unavailable)`, `note TEXT`, `valid_from DATE`, `valid_until DATE`
- Backend-Endpoints `GetAvailabilities(tenantID, employeeID)`, `SetAvailability(...)`, `ListTeamAvailabilities(tenantID, weekStart)`
- Self-Service-UI in `SchichtenPage.tsx` (Verfuegbarkeit-Tab) — Ersatz von `AVAILABILITY_MOCK`

**(b) DACH-Feiertag-Auto** (<3 Tage — kleiner Sprint):
- `holidays`-Backend-Table mit `country_code`, `region_code`, `year`, `date`, `name`, `type`, `is_public_holiday BOOL`
- Yearly-Cron-Job (`cmd/schichten/worker.go`) der `nager.at`-Public-API oder `nager-date`-npm-Library abfragt und `holidays` seedet
- `Shift.is_holiday BOOL` als abgeleitetes Feld
- Frontend nutzt Backend statt `GERMAN_HOLIDAYS_2026`-Hardcoded-Map
- Marketing: "Cosmi-Schichten mit DACH-Feiertag-Auto fuer DE 16 Bundeslaender + AT 9 Bundeslaender + CH 26 Kantone"

**(c) Zuschlags-System-Backend** (3-4 Wochen):
- Tabelle `shift_surcharge_rules` mit `id`, `tenant_id`, `rule_type ENUM(night/weekend/holiday/custom)`, `hour_start INT`, `hour_end INT`, `weekday_bitmask INT`, `holiday_type TEXT`, `surcharge_percent DECIMAL(5,2)`, `min_hours_qualifying INT`, `active_from DATE`, `active_until DATE`
- Backend-Service `CalculateShiftSurcharge(shiftID) []SurchargeApplication` — pro Schicht Berechnung der anwendbaren Zuschlaege
- `shift_calculated_wages`-Materialized-View oder Backend-Endpoint fuer Payroll-Export
- DATEV/LODAS-Export-Sub-Modul (Q4-2026, gemeinsam mit `zeiterfassung`-Sprint) mit Lohnarten-Konfiguration
- Frontend-Ersatz von `SURCHARGE_RULES`/`WEEKEND_SURCHARGE`/`HOLIDAY_SURCHARGE`-Hardcoded-Values

**(d) ArbZG-Warnungs-Vollpalette** (kombiniert mit Empfehlung #2 — 3-4 Wochen)

**Gesamtsprint-Aufwand**: 8-10 Wochen sequenziell oder 4-6 Wochen mit 2 parallelen Devs.

**Sales-Story**: "Cosmi-Schichten liefert vollstaendige Handwerk/Retail/Pflege-Story: Verfuegbarkeits-Selbst-Service, DACH-Feiertag-Auto, Nacht/Sonn/Feier-Zuschlags-Payroll, ArbZG-Vollpalette-Warnungen — zu 4 EUR/User-Monat oder gebuendelt mit Zeiterfassung + Rapporte fuer 10 EUR/User-Monat".

**Erwartete Marketing-Auswirkung**: Cosmi ist wettbewerbsfaehig gegen Papershift Premium/Professional-Feature-Set zu 33-56% niedrigerem Preis. Kombiniert mit Empfehlungen #1 (AI-Auto-Assign) und #2 (ArbZG-Reform-ready) ergibt sich der komplette DACH-KMU-Schichtplan-Feature-Set fuer Q1-2027-Sales-Kampagne.

---

## Quellen

**Regulierung / ArbZG-Reform**:
- [Osborne Clarke — Referentenentwurf BMAS 18.06.2026 (HR-Praxis)](https://www.osborneclarke-arbeitsrecht.de/artikel/neues-zum-arbeitszeitgesetz-was-der-referentenentwurf-des-bmas-vom-18-juni-2026-fur-die-hr-praxis-bedeutet/)
- [Gleiss Lutz — BMAS-Update Referentenentwurf ArbZG](https://www.gleisslutz.com/de/know-how/bmas-update-neuer-referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes)
- [Eversheds Sutherland — Referentenentwurf elektronische Arbeitszeiterfassung](https://www.eversheds-sutherland.com/de/germany/insights/update-zum-arbeitszeitgesetz-referentenent-wurf-zur-elektronischen-arbeitszeiterfassung)
- [clockin — Reform des Arbeitszeitgesetzes 2026](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026)
- [hrtime.de — ArbZG 2026 alle Aenderungen](https://www.hrtime.de/blog/arbeitszeitgesetz-2026-alle-aenderungen/)
- [Shiftbase — Arbeitszeitreform 2026 Arbeitgeber](https://www.shiftbase.com/de/blog/arbeitszeitreform-arbeitgeber)
- [ZFDM — Zeiterfassung Pflicht Kleinbetriebe 2026](https://www.zeiterfassung-fdm.de/ressourcen/ratgeber/zeiterfassung-kleinbetriebe-pflicht/)
- [Anwaltskanzlei Wagner+Graef — Referentenentwurf ArbZG](https://www.unsere-kanzlei.de/referentenentwurf-arbeitszeitgesetz)
- [Rechtsnorm §5 ArbZG](https://www.gesetze-im-internet.de/arbzg/__5.html)

**Konkurrenten**:
- [Papershift — KI-Auto-Zuweisung + KI-HR-Chat](https://www.ki-syndikat.de/tools/papershift/)
- [Papershift — Core/Premium/Professional](https://www.papershift.com/webinare/core-premium-professional)
- [Shyftplan — Shyftplanner AI-Optimierung 20+ Faktoren](https://shyftplan.com/en/shyftplanner)
- [Shyftplan — Personio-Integration](https://shyftplan.com/en/personio-integration)
- [Shyftplan — SAP-verifizierte Integration](https://shyftplan.com/en/features/systemintegration)
- [Ordio — Pricing 89-149 EUR pro Standort](https://www.ordio.com/en/pricing)
- [Ordio — Papershift-Vergleich](https://www.ordio.com/alternativen/papershift-vergleich)
- [Crewmeister — Pricing 1.50-9 EUR/User](https://crewmeister.com/de/preise)
- [Crewmeister — Zeiterfassungspflicht 2026](https://crewmeister.com/de/magazin/zeiterfassungspflicht-2026-was-sie-wissen-muessen)
- [Planday — Winter/Spring 2026 Updates](https://help.planday.com/en/articles/621960-product-updates-winter-and-spring-2026)
- [Planday Home mit Agentic-AI-Ziel](https://www.planday.com/)
- [7shifts — Pricing + ML-Auto-Scheduler](https://www.7shifts.com/pricing/)
- [Deputy — AI Platform November 2025 Launch](https://news.deputy.com/deputy-launches-new-ai-platform-on-aws-to-transform-how-businesses-manage-shift-work-ef9g8q)
- [Deputy — Smart Scheduling AI Features](https://www.deputy.com/features/smart-scheduling)
- [Sona — 45M USD Series B April 2026](https://www.prnewswire.com/news-releases/sona-raises-45m-series-b-to-bring-ai-to-the-frontline-economy-302730478.html)
- [Sona Home + Forge](https://www.sona.ai/)
- [Connecteam — 7shifts-Review (Konkurrenten-Ueberblick)](https://connecteam.com/reviews/7shifts/)
- [Aplano — Preise 0.50-4.50 EUR/MA](https://www.aplano.de/preise)
- [ShiftJuggler — Papershift-Vergleich + DACH-Feiertag-Auto](https://www.shiftjuggler.com/vergleich/shiftjuggler-vs-papershift/)
- [gastromatic — Digitaler Dienstplan](https://www.gastromatic.com/de/digitaler-dienstplan/)
- [HERO Software — Zeiterfassung App](https://hero-software.de/features/zeiterfassung-app)
- [HERO Software — Pricing](https://hero-software.de/preise)
- [Personio — Manage work schedules](https://support.personio.de/hc/en-us/articles/27866580044445-Manage-work-schedules)
- [Personio — Attendance Policies 2026](https://community.personio.com/product-spotlight-133/attendance-policies-making-attendance-settings-in-personio-more-flexible-than-ever-5265)
- [Personio Marketplace — Shyftplan-Integration](https://www.marketplace.personio.com/integrations/shyftplan/)

**Marktzahlen + Trends**:
- [Cognitive Market Research — Employee Scheduling Market Report](https://www.cognitivemarketresearch.com/employee-scheduling-and-shift-planning-software-market-report)
- [Future Market Report — Workforce Scheduling Software Market](https://www.futuremarketreport.com/industry-report/workforce-scheduling-software-market/)
- [Verified Market Reports — Employee Shift Scheduling Software Market](https://www.verifiedmarketreports.com/product/employee-shift-scheduling-software-market/)
- [OMR Reviews — Ordio Pricing 2026](https://omr.com/en/reviews/product/ordio/pricing)
- [KI-Syndikat — Papershift Test 2026](https://www.ki-syndikat.de/tools/papershift/)
- [Ordio — Best Employee Scheduling Software 2026](https://www.ordio.com/en/insights/guides/employee-scheduling-software/)
- [Trusted — Papershift Erfahrungen 2026](https://trusted.de/papershift)

**Best-Practice / Feature-Muster**:
- [Workforce.com — Shift Swap Software](https://www.workforce.com/software/shift-swapping)
- [MyShyft — Streamline Employee Shift Swap Request Initiation](https://www.myshyft.com/blog/shift-swap-request-initiation/)

---

## Picks (vorgeschlagen)

[ ] 🟢 **AI-Auto-Assign-Heuristik Q3-2026-Prototyp** — Markt-Pflicht, Vorbereitungs-Sprints (`employee_availabilities` + `employee_qualifications` + ArbZG-Vollpalette) starten Q3-2026-Anfang. Empfehlung #1.

[ ] 🟢 **`arbzgMinRestDuration` Tenant-Setting + Pflege/Gastro/Verkehr-Ausnahme** — Regulatorische Pflicht ab §5-ArbZG-Reform. Marktzuwachs 30-40% des adressierbaren KMU-Segments (Pflege/Gastro/Verkehr). Empfehlung #2.

[ ] 🟢 **DACH-Feiertag-Auto (nager-date-Library oder `holidays`-Backend-Table)** — <3-Tage-Sprint mit hoher Marketing-Auswirkung. Ersatz von `GERMAN_HOLIDAYS_2026`-hardcoded-Frontend-Map. Empfehlung #3 Teil (b).

[ ] 🟢 **`employee_availabilities`-Backend + Self-Service-UI** — Vorbereitungs-Sprint fuer Auto-Assign UND Ersatz des `AVAILABILITY_MOCK`-Frontend-Placeholders. Empfehlung #3 Teil (a).

[ ] 🟡 **Zuschlags-System-Backend (Nacht/Weekend/Holiday) + DATEV/LODAS-Payroll-Export** — kombinieren mit `zeiterfassung`-Sprint aus W28-rapporte-Deepdive-Anker. Empfehlung #3 Teil (c). → followup 45d.

[ ] 🟡 **ArbZG §3/§4/§9-10 + Consecutive-Days Backend-Impl** — kombiniert mit Empfehlung #2 (Tenant-Setting). Ersetzt `ArbZGViolation`-Placeholder-Types im Frontend mit echten Backend-Impl. Empfehlung #3 Teil (d). → followup 30d.

[ ] 🟡 **Personio-Marketplace-Integration** — Sales-Barrier fuer DACH-Personio-Bestandskunden (Sales-Blocker). Q4-2026-Sprint gemeinsam mit `hr`-Modul. → followup 60d.

[ ] 🟡 **Multi-Site-Support (`locations`-Table statt `Shift.Location`-String)** — Ordio-Preis-Modell-Konkurrenz + Multi-Standort-KMU-Support. Q4-2026-Sprint. → followup 60d.

[ ] 🟡 **PWA-Layer + Service-Worker + Offline-Queue fuer SchichtenPage.tsx** — Frontline-Mobile-Marktbenchmark (Connecteam/Ordio/Crewmeister). Kombiniert mit rapporte-W28-Empfehlung fuer Baustellen-Offline-Mode. → followup 60d.

[ ] 🟡 **Cross-Modul-Bundle-Rabatt (5+ Module = 20% Rabatt) + Cosmi-Micro-Free-Tier fuer <5 MA** — Anti-Aplano-Preis-Strategie. Marketing-Sprint (Sales-Team + `.knowledge/pricing.md`). → followup 45d.

[ ] 🔴 **`ShiftTemplate.Color` + `ShiftTemplate.BreakMinutes` Backend-Schema** — Frontend-Adapter faelscht heute Defaults `#3b82f6` + `30`. Kleiner Migration + Service-Update-Sprint. → followup 21d.

[ ] 🔴 **TenantInboundUnaryInterceptor fuer schichten-gRPC-Binary (R3-P0-3-Ticket)** — Sicherheits-Hardening, gemeinsam mit den anderen 12 Binaries in Sprint-Sicherheits-Welle. → followup 90d.

[ ] 🔴 **Test-Coverage schichten von 35.2% auf 45%+** — 40%-Referenz-Ziel `.knowledge/testing.md` gilt, Extra-Puffer fuer Auto-Assign-Sprint. → followup 30d.
