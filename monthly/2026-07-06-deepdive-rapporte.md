---
year: 2026
week: 28
modul: rapporte
created: 2026-07-06
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 51
tokens_input: ~355000
tokens_output: ~23000
rotation_position: 9/15
---

# Deepdive: rapporte (Mo W28/2026)

> **Neunter Deepdive der Rotation.** Vorgaenger: `crm-core` (W20, 2026-05-11), `dialer` (W21, 2026-05-18), `video` (W22, 2026-05-25), `wiki` (W23, 2026-06-01), `helpdesk` (W24, 2026-06-08), `formulare` (W25, 2026-06-15), `vertraege` (W26, 2026-06-22), `buchhaltung` (W27, 2026-06-29). Naechstes Modul gemaess Rotation: **schichten** (KW29, 2026-07-13) — direkt angrenzend an rapporte via HR-Domaene. Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-rapporte (2026-07-06):** Backend `backend/internal/rapporte/` ist **schlank und produktions-ready aus Sprint-2-Welle-2A** — 8 Files mit **~2998 LOC gesamt** (`errors.go` 16, `models.go` 140, `postgres_repository.go` 938, `repository.go` 73, `service.go` 636, `service_test.go` 961, `signature_test.go` 165, `tenant_isolation_phase2_test.go` 69), Coverage 33.9-35.6% laut `.knowledge/milestones.md` Welle-2C-Sweep. **21 Service-Methoden** (`CreateReport`/`UpdateReport`/`DeleteReport`/`GetReport`/`ListReports`/`SubmitReport`/`ApproveReport`/`RejectReport`/`AddLine`/`UpdateLine`/`DeleteLine`/`ListLines`/`UploadAttachment`/`ListAttachments`/`DeleteAttachment`/`GetReportStats`/`ListPendingApprovals`/`SaveSignature`/`ExportPDF` plus `validateGPS` und `NewService`). Approval-State-Machine ist sauber: `Draft → Submitted → Approved/Rejected` mit `ErrAlreadyApproved`-Sentinel gegen Rueckwaerts-Transitions. GPS-Tag via `lat`/`lon`-NUMERIC(9,6)-Spalten mit `validateGPS`-Bounds-Check (-90..90 / -180..180). Signature-Support seit Migration 000143 (`signature_data` + `signed_at` + `signed_by`) — dedizierter `signature_test.go`-Test-Pfad. Extended Field-Report-Spalten seit Migration 000162 (`weather`, `temperature`, `work_start`/`end`, `break_minutes`, `project_name`) + `report_workers`-Tabelle (Multi-Worker pro Rapport mit `name`/`role`/`hours`) + `report_lines.category`/`.article` fuer Kategorisierung. Separate `:approve`-Permission seit Migration 000100 (admin-only, Sweep 2026-06 durch Welle-2C-Sicherheits-Fix). MinIO-Attachment-Layer mit ObjectKey-Tenant-Prefix-Validierung (Welle-2C-Sicherheits-Fix). **Frontend `desktop/src/renderer/src/modules/rapporte/`**: `RapportePage.tsx` mit **1869 LOC** (Mono-Root-Page mit 3 Tabs: `tagesberichte`/`aufmass`/`vorlagen`), `SketchCanvas.tsx` mit **732 LOC** (Aufmass-Zeichnen fuer Handwerk), `SignatureCanvas.tsx` mit **nur 3 LOC** (auffaellig — Stub/Placeholder statt echter Canvas-Signatur-Erfassung, das ist eine strukturelle Frontend-Luecke). Volumen gesamt Frontend rapporte: **2604 LOC**. **Parallel-Modul `zeiterfassung`** (nicht rapporte): `desktop/src/renderer/src/modules/zeiterfassung/` mit `ZeiterfassungPage.tsx` (35 LOC Mono-Root, verweist auf Components) + Components `AuswertungenView.tsx` (200), `ExportDialog.tsx` (151), `ManualEntryDialog.tsx` (200), `StundenkontoBadge.tsx` (38), `TeamView.tsx` (132), `WeekSubmitBanner.tsx` (48), `weekUtils.ts` + `ZeiterfassungSettingsPanel.tsx` (205) — Volumen gesamt Frontend zeiterfassung: **~1000 LOC**. **Zeiterfassung-Backend** ist NICHT in `backend/internal/rapporte/`, sondern in `hr_work_time_entries`-Tabelle mit Migrationen 000030 (create_time_entries), 000046 (create_hr_tables), 000178 (hr_time_categories), 000179 (hr_time_templates), 000180 (hr_week_approvals mit `open`/`submitted`/`approved`/`rejected` + UNIQUE(tenant,employee,week_start)), 000181 (hr_time_projects), 000182 (extend mit `category_id`/`location_lat`/`location_lng`/`location_address`/`deleted_at`), 000212 (project_id-FK), 000213 (hr_company_settings work_hours_per_day/max_daily_hours/break_after_hours). **Modul-Anker**: Feature-Flag `modules.rapporte` (`registry.go:74`, DefaultEnabled: false, `COSMI_MODULE_RAPPORTE_ENABLED`, SafeRisk, LLMToggleSafe). Modul-Pricing-Anker (`KMU-Hub/.knowledge/pricing.md`): **3 EUR/User-Monat** fuer Rapporte-Modul, Markt-Vergleich "In Proj.tools ab 24 EUR" — Cosmi-Rapporte ist **9-facher Preis-Rabatt** gegen Bau-ERP-Rapport-Module wie 123erfasst Standard (30 EUR/User-Monat) oder HERO Core (69 EUR/User-Monat). **Zeiterfassung** wird separat abgerechnet: **3 EUR/User-Monat** (`.knowledge/pricing.md` Zeile 53, Markt-Vergleich "Clockify/Harvest ab 5"). Modul-Kombo Rapporte+Zeiterfassung = 6 EUR/User-Monat. **Bekannte Schulden**: (i) rapporte ist eines der 13 Binaries ohne `TenantInboundUnaryInterceptor` (R3-P0-3 offen laut `.knowledge/security.md`), (ii) `SignatureCanvas.tsx` ist Placeholder-Stub — muss ausgebaut werden fuer echte Vor-Ort-Signatur-Workflow, (iii) rapporte-Backend `Test-Coverage 33.9%` unter dem 40%-Referenz-Ziel des `.knowledge/testing.md`-Standards.

> **Drei strukturelle Beobachtungen, die jeden Sprint-Plan kalibrieren.** **#1 rapporte + zeiterfassung sind zwei parallele Module ohne gemeinsame Domain-Schicht — die architektonische Auftrennung ist historisch, nicht domain-getrieben, und blockiert die Q3-2026-Zeiterfassungspflicht-Story.** Cosmi hat heute **zwei getrennte Datenmodelle** fuer Arbeitszeit: (i) `work_reports` (`backend/internal/rapporte/`, Migration 000092+000162) als Field-Rapport mit `work_start`/`work_end`/`break_minutes`/`workers[]` — **Ziel: Handwerk-Baustelle mit Foto + Aufmass + Signatur**, (ii) `hr_work_time_entries` (Migration 000030 + 000046 + 000182 + 000212, im `hr`-Backend-Paket) als HR-Zeiterfassung mit `category_id`/`project_id`/`location_lat/lng` und Wochen-Approval via `hr_week_approvals` — **Ziel: Office-KMU mit Kategorien + Projekten + Woche-Freigabe**. Beide Modelle haben **eigene Approval-State-Machines** (rapporte: draft/submitted/approved/rejected; hr_week_approvals: open/submitted/approved/rejected), **eigene GPS-Erfassung** (rapporte: `lat/lon` auf Rapport-Ebene; hr_work_time_entries: `location_lat/lng` auf Entry-Ebene seit Migration 000182), **eigene Frontend-Pages** (RapportePage 1869 LOC vs ZeiterfassungPage + 7 Components ~1000 LOC), **eigene API-Client-Familien** (`useRapporte`/`api/rapporte-adapter.ts` vs `api/hooks/useZeiterfassung`). **Das ist keine sinnvolle Cosmi-Modul-Architektur** — es ist zwei Module fuer die gleiche Domain (Zeit + Arbeit + Freigabe). Anders als bei `buchhaltung` W27 (drei Sub-Pakete `invoice`+`incoming`+`dunning` als bewusste Vertikal-Trennung im gleichen Modul) oder `vertraege` W26 (ein Modul, ein State-Machine-Layer) ist rapporte↔zeiterfassung eine **Namens-Verwaltungs-Splittung**. Der Markt sieht das nicht so: TimeTac, ZEP, Crewmeister, Papershift, Clockify, Harvest verkaufen alle **ein** Zeiterfassungs-Produkt mit Feld-/Projekt-/Handwerk-Modi als **Konfigurations-Optionen**, nicht als getrennte Produkte. **Der neue §16 ArbZG-Referentenentwurf (Juni 2026, mit Koalitionsausschuss-Beratung 01.07.2026 laut hrtime.de) macht diese Splittung strategisch teuer**: die Zeiterfassungspflicht schreibt **elektronische Erfassung von Beginn/Ende/Dauer der taeglichen Arbeitszeit** vor (§16 Abs. 2 + Abs. 7, ArbZG-E) — mit 5-Jahres-Uebergangsfrist fuer <50-MA-Betriebe (Cosmi-Ziel-KMU-Segment, realistisch **Compliance-Deadline 2030-2031**). Cosmi kann diese Pflicht heute mit `hr_work_time_entries` und `hr_week_approvals` erfuellen — **aber nur wenn Cosmi-Kunde das `zeiterfassung`-Modul bucht**, was heute optional ist. Wenn Cosmi-Kunde `rapporte` bucht (Handwerk-Fokus), erfasst er `work_start`/`work_end`/`break_minutes` in `work_reports` — **das ist ArbZG-konform als Erfassung, aber Woche-Aggregation fehlt** (kein `hr_week_approvals`-Aequivalent). **Sprint-Anker**: rapporte und zeiterfassung zu **einem Cosmi-Modul `zeiten`** konsolidieren (oder: rapporte behaelt Field-Rapport-Fokus, zeiterfassung wird zur Basis-Pflicht) — Domain-Design-Entscheidung fuer Q3-2026-Milestone. **#2 Der DACH-Zeiterfassungs-KI-Markt ist ein offenes Fenster — Cosmi kann jetzt eine differenzierende Position einnehmen, weil die grossen DACH-Marktfuehrer noch KEIN live AI-Feature haben.** Der Kontrast zu buchhaltung W27 (wo Lexware NAVI + sevDesk-Beleg-AI + BuchhaltungsButler-Bank-AI seit 6 Monaten live sind und Cosmi hinterher rennen muss) ist hier **umgekehrt**: TimeTac hat **kein Live-AI-Auto-Kategorisierungs- oder AI-Timesheet-Draft-Feature** (Stand Juli 2026 laut Vendor-Docs), ZEP **kein AI-Feature-Set 2026** (Roadmap kommuniziert Reisekosten + UX-Renewals, kein AI), Crewmeister **keine AI** (Fokus auf 30%-Rabatt-Kampagne als Reaktion auf Zeiterfassungspflicht), Papershift **keine AI**, 123erfasst **kein oeffentlich verkuendetes AI-Feature 2026**, Toggl **kein AI-GA-Feature** (nur Preis-Uplift), Clockify **kein AI-Feature**. **Live-AI im Segment**: nur (i) **Timely** (Memory-Autosheet mit Auto-Kategorisierung + Reduktion manueller Korrekturen bis 90% laut Vendor), (ii) **HERO Software 2026** (HERO Voice als KI-Telefonassistent GA 2026, HERO Report angekuendigt fuer Bautagebuch per Voice-Input) — aber HERO ist mit 69 EUR/User-Monat KEIN KMU-Standard-Preis. **Konsequenz fuer Cosmi**: eine **AI-Rapport-Auto-Kategorisierung** oder eine **AI-Timesheet-Kategorisierung** waere im DACH-KMU-Segment ein klarer Differenzierer, weil TimeTac/ZEP/Crewmeister/Papershift/Clockify die Erwartungshaltung **nicht gesetzt haben**. Anders als bei helpdesk (AI-Drafts als Tabellenstake seit Zendesk-2025-Herbst), formulare (AI-Form-Generation als Tabellenstake), vertraege (AI-Klausel-Extraction als Tabellenstake), buchhaltung (AI-OCR-Beleg als Tabellenstake). Rapporte/Zeiterfassung ist heute noch das Modul mit dem **niedrigsten AI-Feature-Druck** von aussen — aber es ist ein zeitlich enger werdendes Fenster, weil Timely-AI Fokus auf DACH-Vermarktung 2026 legt und HERO Voice die Handwerk-Zielgruppe direkt adressiert. Sprint-Empfehlung: **AI-Auto-Kategorisierung von Rapport-Positionen** (nicht Timesheet-Draft) als Q4-2026-Cosmi-USP. **#3 Cosmi hat mit rapporte einen echten Handwerk-Baustellen-Vorteil (SketchCanvas + GPS + Signature + Foto + Aufmass + Vorlagen) — aber SignatureCanvas ist Stub, Offline-Mode fehlt, PWA-Baustellen-Story ist nicht kommuniziert.** RapportePage 1869 LOC zeigt eine **breite Feature-Palette**: `weatherIcons` Map (Sun/Cloud/CloudRain/Snowflake), `Camera` Icon fuer Attachment-Upload, `Users` fuer report_workers-Multi-Worker, `HardHat` als Handwerk-Icon, `Ruler` fuer Aufmass-Tab, `Send`/`ShieldCheck` fuer Signature-Flow, `Package` fuer Materialien, `ClipboardCheck` fuer Approval, `Thermometer`/`Wind`/`Droplets` fuer erweiterte Wetter-Erfassung. Das Frontend-Feature-Set ist **konkurrenzfaehig gegen 123erfasst und HERO Software** — beide sind DACH-Handwerk-Fokus, beide mit Foto + Signature + Baustellen-UX. **Aber drei strukturelle Baustellen-Luecken**: (i) **SignatureCanvas.tsx ist 3-LOC-Stub** — kein produktions-tauglicher Canvas-Signatur-Erfasser, das ist der `git blame`-verifizierte Frontend-Zustand. Der Backend-Weg (`SaveSignature`-RPC + `signature_data`/`signed_at`/`signed_by`) ist funktional, aber das Frontend liefert die Signatur nicht ein. **Sprint-Pflicht**: SignatureCanvas mit `react-signature-canvas` oder `signature_pad`-npm-Library nachziehen, base64-PNG-Serialisierung an `SaveSignature`-Endpoint. (ii) **Kein Offline-Mode** — `authenticatedFetch.ts` hat `OfflineError`-Guard fuer Mutations (`api/utils/authenticatedFetch.ts`), aber **kein Queue-Persistenz-Layer** fuer Rapport-Erstellung ohne Netz. Der Kern-Handwerk-Use-Case (Baustelle ohne LTE/5G) ist heute nicht abgedeckt. **123erfasst und HERO Software haben robusten Offline-Mode als Marktbenchmark** (123erfasst als Bau-Marktfuehrer mit Foto-Doku mit automatischer GPS + Datum + Uhrzeit + Bautagebuch offline). (iii) **Cosmi ist Desktop-Electron + PWA-orientiert** (kein natives iOS/Android) — der `desktop/`-Ordner ist Electron-App, das ist strukturell **nicht Baustellen-Handschuh-Bedien-optimal**. TimeTac/Crewmeister/123erfasst/HERO haben alle native iOS/Android-Apps mit Ein-Tap-Stempel + Handschuh-taugliche Touch-Bereiche. **Sprint-Anker**: (i) SignatureCanvas ausbauen (kleiner Sprint), (ii) Offline-Queue fuer rapporte + zeiterfassung (mittlerer Sprint mit IndexedDB + Service-Worker + Sync-on-Reconnect), (iii) PWA-Manifest + Baustellen-optimierte-Mobile-UX fuer RapportePage (mittlerer Sprint).

> **Leit-Signal der Woche fuer rapporte: drei parallele Bewegungen formen den Markt seit Anfang 2026.** **(a) Zeiterfassungspflicht-Reform (Referentenentwurf Juni 2026, Koalitionsausschuss-Beratung 01.07.2026)**: nach EuGH-CCOO-Urteil (14.05.2019, C-55/18) und BAG-Beschluss 1 ABR 22/21 (13.09.2022, "objektive, verlaessliche und zugaengliche Arbeitszeiterfassung ist Pflicht") legt der schwarz-rote Koalitionsvertrag "Verantwortung fuer Deutschland" (April 2025) das Vorhaben neu auf — Referentenentwurf lag Juni 2026 aktualisiert vor, Koalitionsausschuss beriet offene Punkte am 01.07.2026 (laut `hrtime.de/blog/arbeitszeitgesetz-2026-alle-aenderungen` und `cmshs-bloggt.de/arbeitsrecht/referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes-liegt-endlich-vor`). Kern-§16-ArbZG-E-Regelung: **elektronische Erfassung von Beginn, Ende, Dauer der taeglichen Arbeitszeit am Tag der Arbeitsleistung** (Abs. 2 + Abs. 7); Ausnahmen ueber Tarif-/Betriebsvereinbarung. **Uebergangsfristen gestaffelt**: 1 Jahr fuer >250 MA, 2 Jahre fuer <250 MA, **5 Jahre fuer <50 MA** (Cosmi-Ziel-KMU), <10 MA ausgenommen. Fuer Cosmi-Ziel-KMU also **Compliance-Deadline realistisch 2030-2031** — kein akuter Zeitdruck, aber **Zertifizierungs-Fit-Story** fuer Sales-Pitch ist ab jetzt relevant ("Cosmi-Zeiterfassung ist ArbZG-2026-Reform-ready"). Der Entwurf sieht ausserdem Flexibilisierung der taeglichen Hoechstarbeitszeit zugunsten **woechentlicher Betrachtung** vor — Software muss `hr_week_approvals`-Wochen-Aggregation weiterfuehren, `hr_company_settings.max_daily_hours` (Migration 000213) muss **konfigurierbar per Tenant** bleiben (nicht hardcoded 10h). **(b) DSGVO-GPS-Strengung**: die oesterreichische DSB stoppte im **November 2025** GPS-Tracker in Dienstfahrzeugen mangels Erforderlichkeit (laut `dataprotect.at/2025/11/27/gps-tracking-in-dienstfahrzeugen-dsb-stoppt-einsatz-von-gps-tracker-mangels-erforderlichkeit`), und DE-Betriebsrat-Mitbestimmungspflicht nach §87 Abs. 1 Nr. 6 BetrVG ist zwingend. **Konsequenz fuer Cosmi**: **kontinuierliche GPS-Ortung ist nicht defensiv-korrekt** — der einzige zulaessige Weg ist **punktuelle GPS-Erfassung nur beim Clock-In/Out und beim Rapport-Absetzen**, mit klarem Consent-Flow im UI und `location_lat/lng`-Erfassung nur bei aktivem User-Action-Event. Cosmi-heute: `validateGPS` prueft nur Bounds, aber **kein Consent-Flow im RapportePage.tsx** — Nutzer sieht nicht, dass GPS erfasst wird. Sprint-Anker: `GPSConsentToggle`-Komponent in `SettingsPanel.tsx`, tenant-weite Aktivierungs-Option, Audit-Log via `report_gps_consent_events`-Tabelle. **(c) Handwerk-Baustellen-Standard 2026**: 123erfasst hat im Fruehjahr 2026 neue Benutzeroberflaeche gelauncht (laut `buildingnet.de/digitalisierung/123erfasst-mit-neuer-benutzeroberflaeche.htm`), HERO Software hat Recap-2025-Feature-Sweep mit HERO Voice GA gemacht (`hero-software.de/features/recap-2025`), mobiel/noovi.ch adressieren dezidiert CH-KMU-Handwerk-Segment mit digitalen Rapporten inkl. Vor-Ort-Unterschrift. **Konsequenz fuer Cosmi**: der Baustellen-Handwerk-Feature-Standard heisst **Foto-mit-GPS-Georeferenz + eIDAS-Signatur + Multi-Stage-Freigabe + Offline-Mode + Handschuh-taugliches UI**. Cosmi hat 3 von 5 (Foto, GPS-Tag, Signatur-Backend), fehlt 2 von 5 (Offline-Mode, mehrstufige Freigabe — die aktuelle State-Machine hat nur 1 Reviewer-Stufe), plus SignatureCanvas-Stub-Bug im Frontend. **Heute keine akute rapporte-Markt-Nachricht im Morning-Pulse** (`daily/2026-07-06-morning.md` noch ausstehend, letzter Pulse `2026-07-02-friday`), **aber die drei Bewegungen sind alle in `.state/hot_items_2026-06-*`-Feeds als Nebenlinien vertreten**. **Dieser Bericht empfiehlt drei Pflicht-Sprint-Stakes fuer das dritte Quartal 2026: rapporte↔zeiterfassung-Domain-Konsolidierung, Baustellen-Offline-Mode + Signature-Canvas-Ausbau, AI-Rapport-Auto-Kategorisierung — alle drei sind heute strukturelle Cosmi-Luecken, alle drei haben in 6-12 Monaten Marktbeobachtungs-Auswirkung, keine der drei ist heute in einem Sprint-Backlog erkennbar.**

---

## State-of-the-Art

Der DACH-Zeiterfassungs- und Field-Rapport-Markt Mitte 2026 ist **vierspurig** — anders als der buchhaltung-Markt (W27) mit klarer AI-First-Dominanz oder der vertraege-Markt (W26) mit CLM-Agenten-Diskussion, ist dieser Markt **domaenen-segmentiert** und **AI-Feature-arm** (Ausnahme Timely + HERO). Die vier Spuren:

**(1) Handwerk-Baustellen-Feld-Rapport-Spezialisten**: 123erfasst (DE, Nevaris/bps software, Bau-Marktfuehrer, Foto-Doku-Benchmark mit automatischer GPS+Datum+Uhrzeit, offline Bautagebuch, neue UI 2026), HERO Software (DE, Handwerker-ERP mit HERO Voice AI + HERO Report angekuendigt), mobiel (DACH, Nischen-Handwerk-Feldrapport), noovi (CH, digitale Rapporte + Vor-Ort-Unterschrift), clockin (DE, Baustellen-Fokus). Diese Spur ist **Cosmi-rapporte-direkte-Konkurrenz** — dieselbe Zielgruppe (Handwerks-KMU 5-30 MA), dieselben Features (Foto, GPS, Signatur, Aufmass, Wetter).

**(2) HR-Zeiterfassungs-Klassiker (DACH)**: TimeTac (AT, TimeTac Classic + Next mit Geofencing/Approvals, DATEV Lodas/Lohn&Gehalt-Sync 2025), ZEP (DE, PSA-Fokus fuer Consulting/IT-KMU, Reisekosten-Modul 2026), Crewmeister (DE, mobile-first, GPS bis 2 m Genauigkeit, 30%-Rabatt-Kampagne 2026 bis 12. Juni als Reaktion auf Zeiterfassungspflicht), Papershift (DE, Schicht-Primary mit Zeiterfassung angrenzend, DATEV/LODAS-Payroll). Diese Spur ist **Cosmi-zeiterfassung-direkte-Konkurrenz** — dieselbe Zielgruppe (Office/Retail-KMU), dieselben Features (Web/Mobile-Erfassung, Kategorien, Projekt-Tracking, DATEV-Export).

**(3) International-Freelancer-Time-Tracker**: Toggl Track (Estonia, Freelancer/Agentur-Fokus, Preis-Uplift 2026 ohne AI-GA-Feature), Harvest (US, Bending-Spoons-Uebernahme 2025 mit Preis-Kritik in G2-Reviews, Blog-Content ueber AI aber kein GA-Feature), Clockify (US, Free-Tier-Krieger, GPS/Geofencing ab Pro $7.99, US-Hosting = DSGVO-Fragen), Timely (Norwegen, Memory-Autosheet AI-Marktfuehrer mit angeblich 90% Korrektur-Reduktion). Diese Spur ist **Cosmi-DACH-KMU-Segment-Rand** — internationale KMU/Freelancer verwenden diese Tools, DACH-KMU-Handwerk selten. Threat-Level medium bis low.

**(4) Consulting-PSA / IT-Service-KMU-Time-Tracker**: ZEP Compact/Professional, Kimai (Open-Source), Toggl Track Premium — mit Fokus auf Projekt-Zeit-Erfassung fuer abrechenbare Kundenprojekte. Diese Spur ueberlappt sich mit Cosmi-`zeiterfassung`-Modul, wenn Cosmi-KMU-Kunde Consulting-Betrieb ist (10-50 Mitarbeitende IT/Beratung).

Cosmi-rapporte sitzt heute **architektonisch in Spur (1)** als Handwerk-Feld-Rapport-Modul, Cosmi-`zeiterfassung` sitzt in Spur (2). Der Modul-Preis von 3 EUR/User-Monat pro Modul ist **konsistent unter allen DACH-Konkurrenten** (TimeTac Essential 3 EUR/User + Basisgebuhr 19.50, ZEP Clock 2 EUR/User + Compact 7, Crewmeister Standard 5.20 EUR/User, 123erfasst Standard ab 30 EUR/User, HERO Core ab 69 EUR/User). Der Preis-Vorteil ist echt, aber das Feature-Gap gegen 123erfasst/HERO im Handwerk und gegen TimeTac/ZEP/Crewmeister im HR-Zeiterfassung ist auch echt.

Drei strukturelle Veraenderungen treiben den Markt seit Anfang 2026:

(a) **§16 ArbZG-Reform-Reaktivierung Q2 2026 + Uebergangsfristen-Landscape**. Der Referentenentwurf lag April 2023 vor, wurde durch die Ampel-Koalition zurueckgestellt, ist durch den schwarz-roten Koalitionsvertrag (April 2025) neu aufgerufen worden. **Aktualisierter Referentenentwurf: Juni 2026**, Koalitionsausschuss-Beratung offener Punkte: **01. Juli 2026** (5 Tage vor diesem Bericht). Kern-§16-ArbZG-E-Bestimmungen: (i) **elektronische Erfassung von Beginn, Ende, Dauer der taeglichen Arbeitszeit** am Tag der Arbeitsleistung — vorher hatten nur Ueberstunden dokumentiert werden muessen. (ii) Ausnahmen nur ueber Tarifvertrag oder Betriebsvereinbarung; Verzicht auf tagesscharfe elektronische Erfassung nicht mehr moeglich fuer KMU ohne Betriebsrat. (iii) Flexibilisierung der taeglichen Hoechstarbeitszeit von aktuell 10 Stunden auf woechentliche Betrachtung (48-Stunden-Wochen-Grenze bleibt EU-rechtlich vorgegeben) — Cosmi muss `hr_week_approvals`-Wochen-Aggregation weiterfuehren, Wochen-Uebersicht-View im Frontend liefern. (iv) **Uebergangsfristen**: 1 Jahr fuer >250 MA, 2 Jahre fuer <250 MA, **5 Jahre fuer <50 MA**, <10 MA ausgenommen. **Cosmi-Ziel-KMU** (5-50 MA laut `.knowledge/pricing.md`) hat also realistisch **Compliance-Deadline 2030-2031** nach Inkrafttreten (frueheste Bundesrat-Verabschiedung Q4 2026, Inkrafttreten dann Q1-Q2 2027). **Kein akuter Zeitdruck fuer Cosmi-Kunden**, aber Sales-Story ist ab jetzt relevant: "Cosmi-Zeiterfassung ist ArbZG-2026-Reform-ready" — konkret erfuellt Cosmi das Basis-Requirement (elektronische Erfassung von Beginn/Ende/Dauer via `hr_work_time_entries`), muss aber die Wochen-Aggregation robust vorzeigen (`hr_week_approvals` seit Migration 000180 mit UNIQUE(tenant,employee,week_start) und State `open`/`submitted`/`approved`/`rejected` — das ist schon vorhanden). **Konsequenz fuer Cosmi**: (i) Zertifizierungs-Marker "Cosmi-ArbZG-Reform-ready" im Marketing-Material bis Q4 2026, (ii) `hr_company_settings.max_daily_hours` bleibt konfigurierbar pro Tenant, (iii) rapporte-`work_start`/`work_end`/`break_minutes` sind ArbZG-konform als Erfassungs-Layer, aber Woche-Aggregation muss gegen `hr_week_approvals` ausgerichtet werden (heute nicht verbunden — strukturelle Domain-Konsolidierungs-Pflicht).

(b) **DSGVO-GPS-Strengung durch Herbst-2025-DSB-AT-Entscheid + BAG-Rechtsprechungs-Kontinuitaet 2025**. Die oesterreichische Datenschutzbehoerde hat im **November 2025** GPS-Tracker in Dienstfahrzeugen mangels Erforderlichkeit gestoppt (`dataprotect.at/2025/11/27`) — Analogie zu Cosmi-rapporte-GPS-Erfassung: **kontinuierliche Ortung ist unzulaessig, punktuelle Ereignis-basierte Erfassung ist zulaessig**, wenn (i) Zweck klar dokumentiert, (ii) Erforderlichkeit gegen mildere Mittel nachgewiesen, (iii) Verhaeltnismaessigkeit gewahrt. DE-BDSG §26 Abs. 2 und Art. 6 Abs. 1 DSGVO: **Einwilligung im Beschaeftigungsverhaeltnis regelmaessig unwirksam** wegen fehlender Freiwilligkeit (`dr-datenschutz.de/gps-ueberwachung-am-arbeitsplatz-und-der-datenschutz`) — Cosmi-Kunden koennen sich also **nicht auf Consent-Popup verlassen**, sondern muessen Erforderlichkeits-Argumentation liefern. Zulaessige Rechtsgrundlagen: Art. 6 Abs. 1 lit. b (Vertrag: GPS zur Arbeitsleistungs-Nachweisung), lit. c (gesetzliche Pflicht: ArbZG-Erfassung), lit. f (berechtigte Interessen: Diebstahlschutz Dienstfahrzeug). **Betriebsrat-Mitbestimmung** nach §87 Abs. 1 Nr. 6 BetrVG ist zwingend fuer alle GPS-Tracking-Software-Einfuehrungen. **Konsequenz fuer Cosmi-rapporte**: (i) GPS-Erfassung im Rapport ist **defensiv-korrekt nur beim Clock-In/Out und beim Rapport-Absetzen** (aktuelles Cosmi-Modell), nicht kontinuierlich — passt. (ii) UI muss **transparent kommunizieren**, welche Position wann erfasst wird — heute liefert `RapportePage.tsx` das nicht, `lat`/`lon`-Erfassung ist im Hintergrund. Sprint-Anker: `GPSConsentBanner`-Komponent + `SettingsPanel.tsx`-Toggle "Standort bei Rapport-Erstellung erfassen (ArbZG-konform)". (iii) Tenant-weite Opt-out-Option + Betriebsrats-Aktivierungs-Workflow fuer Kunden mit Betriebsrat. (iv) Audit-Log `report_gps_events`-Tabelle mit `event_type` (rapport_create/clock_in/clock_out) + `consent_at`-Timestamp + `consent_source` (tenant_setting/user_toggle) — DSGVO-Beweislast-fest.

(c) **AI-Feature-Fenster im DACH-KMU-Zeiterfassungs-Segment ist offen — im scharfen Gegensatz zu buchhaltung/helpdesk/formulare/vertraege**. Live-AI-Features Stand 2026-07-06: (i) **Timely** (Norwegen, seit 2024 ausgebauter Memory-Autosheet mit AI-Kategorisierung + GPS-Erfassung im Hintergrund + Auto-Tagging von Kalender-Ereignissen und Anwendungs-Nutzung — laut Vendor bis 90% Reduktion manueller Timesheet-Korrekturen, `hubstaff.com/blog/best-ai-time-tracking-software`). Timely fokussiert 2026 auf DACH-Vermarktung (Website `timely.com/de` seit Q1 2026 aktiv). (ii) **HERO Software** (DE, Handwerker-ERP): HERO Voice als KI-Telefonassistent GA 2026 (`hero-software.de/ai/voice`), HERO Command (KI-Angebots-Assistent) und HERO Report (Bautagebuch per Voice-Input) angekuendigt fuer 2026. HERO ist mit 69 EUR/User-Monat KMU-teuer, aber die AI-Roadmap ist ambitioniert. **Nicht live (Stand Juli 2026)**: TimeTac (kein AI-Feature-Set), ZEP (kein AI, Roadmap kommuniziert Reisekosten + UX-Renewals), Crewmeister (kein AI, Fokus auf Rabatt-Kampagne), Papershift (kein AI, DATEV/LODAS-Integrations-Ausbau), 123erfasst (kein oeffentlich verkuendetes AI-Feature 2026 trotz UI-Redesign), Clockify (kein AI-GA-Feature), Toggl (kein AI-GA, nur Preis-Uplift), Harvest (Blog-Content ueber AI aber kein konkretes GA-Feature). **Konsequenz fuer Cosmi**: das ist eine **strukturelle Chance**. Anders als bei buchhaltung (wo Cosmi 6 Monate hinter Lexware NAVI + sevDesk-Beleg-AI + BuchhaltungsButler-Bank-AI ist), anders als bei helpdesk (wo Zendesk-2025-Herbst AI-Drafts als Tabellenstake gesetzt hat), anders als bei formulare (wo AI-Form-Generation Marktbenchmark ist), anders als bei vertraege (wo AI-Klausel-Extraction bei DocuSign/PandaDoc/Ironclad live ist), ist **rapporte/zeiterfassung heute noch das Modul mit dem niedrigsten AI-Feature-Druck von aussen**. Sprint-Empfehlung: **AI-Rapport-Auto-Kategorisierung** (nicht AI-Timesheet-Draft, das ist Timely's schon-gesetzter USP) als differenzierender Cosmi-USP — Rapport-Textbeschreibung + Foto → AI schlaegt Kategorie/Artikel-Zuordnung vor + LSA-Bewertung mit Confidence-Score. Nutzt bestehende `report_lines.category`/`.article` + `report_workers` + `report_attachments` als AI-Input, erweitert `finance_incoming_invoices`-AI-OCR-Sprint-Pfad aus buchhaltung-W27 fuer OCR-Reuse.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. 123erfasst (DE, threat: HIGH als DACH-Handwerk-Baustellen-Marktfuehrer + Foto-Doku-Benchmark)**

123erfasst (Nevaris-Group / bps software) ist **DE-Bau-Zeiterfassungs- und Rapport-Marktfuehrer** — deutsche Firma, deutsche Datenhaltung, mittlere/grosse Bau-Betriebe im Fokus. Direkter Cosmi-Konkurrent im Handwerk-Feld-Rapport-Segment (`rapporte`-Modul). Fruehjahr-2026-UI-Redesign.

- **Baustellen-Offline-Mode**: **Marktbenchmark** — native iOS/Android-App mit robustem Offline-Sync, offline Foto-Doku mit automatischer GPS-Koordinate + Datum + Uhrzeit + Verknuepfung ins Bautagebuch. Cosmi 0.
- **Bautagebuch-Automatisierung**: Foto-Sammlungen pro Baustelle mit chronologischer Zeitlinie, Multi-Foto-Upload pro Rapport, Wetter-Automatik-Erfassung ueber DWD-API.
- **Neue UI 2026 (Fruehjahr-Launch)**: gemaess `buildingnet.de/digitalisierung/123erfasst-mit-neuer-benutzeroberflaeche.htm` — modernisierte Handschuh-taugliche Bedien-Oberflaeche, verbesserte Navigations-Struktur.
- **DATEV/LODAS-Interface**: bidirektional fuer Personal-Kosten-Sync.
- **Pain-Points G2/OMR 2026**: "Preise fuer ganzen Bau-Betrieb schnell hoch — 30 EUR/User Standard + 50 EUR/User Pro summiert sich", "Setup komplex, braucht Consulting-Support", "UI trotz Redesign noch Bau-lastig, KMU-Handwerk empfindet's als 'over-engineered' fuer Kleinbetriebe unter 10 MA".
- **Pricing (2026)**: Qualitaets-Modul Free (1 User), Basis-Personal/Zeit-Modul kostenfrei bis 10 User, Standard ab **30 EUR/User/Monat**, Pro ab **50 EUR/User/Monat**. Modul-orientiert, aehnlich Cosmi-Ansatz.
- **Tech-Stack**: DE-Cloud (Nevaris/bps software), native iOS/Android mit robustem Offline-Sync.
- **Gap zu Cosmi**: Baustellen-Offline-Mode (Marktbenchmark), Bautagebuch-Automatisierung mit Foto-Chronologie, DWD-Wetter-Automatik-Erfassung, native iOS/Android-Apps mit Handschuh-Bedien-Optimierung, Pro-Bau-Betriebs-Zertifizierungen (VDI-Richtlinien-Konformitaet).
- **Strategischer Hinweis**: **123erfasst ist Cosmi-rapporte's schaerfster Handwerk-Konkurrent im DE-Segment, aber Preis-strukturell hoch fuer Cosmi-Ziel-KMU 5-30 MA**. Cosmi-Differential: **3 EUR/User-Monat gegen 30 EUR/User-Monat** — 10-facher Preis-Rabatt, aber Cosmi liefert nicht die 123erfasst-Baustellen-UX. Sprint-Prioritaeten: (i) Offline-Mode (Q3-2026-Pflicht), (ii) SignatureCanvas-Ausbau (Q3-2026-Sprint), (iii) DWD-Wetter-API-Auto-Erfassung (Q4-2026-Nice-to-have), (iv) PWA-Baustellen-Mobile-UX (Q4-2026-Pflicht).

**2. HERO Software (DE, threat: HIGH als DACH-Handwerker-ERP mit ambitioniertem AI-Layer)**

HERO Software ist **deutscher Handwerker-ERP mit signifikantem AI-Push 2026** — Handwerks-Zielgruppe, HERO Voice als KI-Telefonassistent GA 2026, HERO Report als Bautagebuch-Voice-Input angekuendigt. Direkter Cosmi-Konkurrent im Handwerk-Segment, aber preislich in einer anderen Kategorie.

- **HERO Voice (GA 2026)**: KI-Telefonassistent — Kundengespraeche mit AI-gestuetzter Transkription und automatischer Ticket-/Angebots-Vorbereitung, Voice-Input fuer Auftragserfassung. Kein Cosmi-Aequivalent.
- **HERO Command (angekuendigt 2026)**: KI-Angebots-Assistent — Angebotsvorlagen mit AI-gestuetzter Kalkulation.
- **HERO Report (angekuendigt 2026)**: Bautagebuch per Voice-Input — Rapport-Erstellung durch Sprach-Diktat + AI-Kategorisierung + Foto-Anhang.
- **Offline-fahige App + Digitale Unterschriften**: **produktiv** (nicht Stub wie Cosmi's SignatureCanvas.tsx) — nativ iOS/Android mit Offline-Sync.
- **Handwerker-Full-Suite**: ZUGFeRD/XRechnung + DATEV-Export + Datanorm/IDS-Connect (Handwerk-B2B-Standards fuer Material-Bestellung).
- **Pain-Points 2026** (aus SBZ-Online + Fachpresse): "Preise deutlich ueber KMU-Marktschnitt (69 EUR/User Core + 119-135 EUR HERO OS + 299-345 EUR HERO OS Plus)", "steile Lernkurve wegen Feature-Breite", "AI-Features noch 'beta-esque'".
- **Pricing (2026)**: HERO Core ab **69 EUR/User (jaehrlich) / 79 EUR monatlich**, HERO OS **119-135 EUR/Monat inkl. 1 Standard-Lizenz**, HERO OS Plus **299-345 EUR/Monat**, HERO AI Launch-Rabatt **59 EUR/Lizenz** (`hero-software.de/preise`).
- **Tech-Stack**: DE-Cloud, native App mit Offline-Modus, ZUGFeRD/XRechnung, DATEV-Export, Datanorm/IDS-Connect.
- **Gap zu Cosmi**: HERO Voice (KI-Telefon-Transkription), HERO Report (Voice-zu-Rapport), digitale Unterschriften produktiv (nicht Stub), native Offline-App, Datanorm/IDS-Connect-Handwerk-Material-Katalog-Integration.
- **Strategischer Hinweis (WICHTIGSTER AI-PUNKT DIESES REPORTS)**: **HERO Software macht die Rapport/Zeiterfassungs-AI-Story im DACH-Handwerk-Segment vor** — Voice-Input fuer Bautagebuch ist strukturell attraktiv fuer Baustellen-UX (Handschuhe an, Hand frei fuer Werkzeug, Rapport per Sprache). **Aber Preis-Positionierung 69-345 EUR/Monat schliesst KMU 5-30 MA weitgehend aus**. Cosmi-Sprint-Anker: **Voice-Input-Layer im RapportePage.tsx** als Q4-2026-Differenzierer — nutzt Web-Speech-API fuer Sprach-zu-Text (kostenfrei im Browser, DSGVO-freundlich weil Client-side), Rapport-Vorlage-Auto-Fill mit AI-Kategorisierung (Backend-side). Cosmi-Differential: **3 EUR/User-Monat mit Voice-Rapport-Input** gegen HERO 79 EUR/User-Monat — Preis-Story wird ohne Voice-Feature zu schwach fuer KMU-Handwerk-Betriebe, die Voice-Handschuh-Bedienung erwarten.

**3. TimeTac (AT/DACH, threat: HIGH als AT/DE-HR-Zeiterfassungs-Marktfuehrer + DATEV-Integration)**

TimeTac ist **AT/DE-HR-Zeiterfassungs-Marktfuehrer** — oesterreichische Firma, EU-DSGVO-Fokus, Modular-Portfolio 2025 in "TimeTac Classic" + "TimeTac Next" gesplittet, DATEV-Lodas + DATEV-Lohn&Gehalt bidirektionale Integrationen 2025 refreshed. Direkter Cosmi-`zeiterfassung`-Konkurrent.

- **Modular-Portfolio 2025-2026**: Employee Time Tracking + Leave Management + Project Time Tracking als separate buchbare Module — architektonisch aehnlich Cosmi-Modul-System.
- **Geofencing (Professional-Tarif)**: GPS + Geofences fuer Standort-basierte Clock-In-Erfassung — DSGVO-konform, aber Betriebsrats-Mitbestimmungspflicht.
- **DATEV Lodas + Lohn&Gehalt bidirektional (2025-Refresh)**: `timetac.com/en/integration-api/datev-lodas` — Realtime-Sync fuer Personal-Kosten-Buchhaltung.
- **REST-API + native iOS/Android**: `docs.timetac.com` mit vollstaendiger Dokumentation.
- **Keine live AI-Features 2026**: Regel-basierte Workflows, kein AI-Auto-Kategorisierungs- oder Timesheet-Draft-Feature.
- **Pain-Points G2/Capterra 2026**: "Reporting nur begrenzt individualisierbar", "Neuanwender brauchen viel Onboarding-Support", "TimeTac Classic vs. Next verwirrt Bestandskunden" (Positionierungs-Splitting-Problem).
- **Pricing (2026)**: modular — Essential ab **3 EUR/User + Basisgebuhr 19.50 EUR/Monat**, Professional ab **5 EUR/User** (mit Geofencing/Approvals). Employee Time Tracking **5.20 EUR/User**, Leave Management **3.40 EUR/User**, Project Time Tracking **9.00 EUR/User** (`kimai.org/en/blog/2025/price-comparison`).
- **Tech-Stack**: AT-Cloud, REST-API, native iOS/Android, EU-DSGVO-Fokus.
- **Gap zu Cosmi**: DATEV-Lodas + Lohn&Gehalt bidirektional (Cosmi hat nur DATEV-CSV-Export via `finance/datev`-Sub-Paket), Geofencing mit Standort-basierter Auto-Clock-In (Cosmi 0), native iOS/Android-Apps (Cosmi ist Desktop-Electron + PWA), Terminal-Integration (Zeit-Erfassungs-Hardware fuer Empfangs-Buero), Urlaub/Abwesenheiten-Management-Modul.
- **Strategischer Hinweis**: **TimeTac-Preis-Struktur ist Cosmi's direkter Vergleichsanker** — Essential 3 EUR/User + 19.50 EUR Basisgebuhr = ca. 22.50 EUR/Monat fuer 1 User (5.20 fuer 5 User = 45.50 EUR). Cosmi-`zeiterfassung` mit 3 EUR/User-Monat OHNE Basisgebuhr ist **guenstiger** fuer Cosmi-KMU 5-30 MA (5 User = 15 EUR/Monat gegen TimeTac 45.50 EUR/Monat). **Aber**: TimeTac hat DATEV-Realtime-Sync + Geofencing + native Apps + Terminal-Integration + Urlaub-Modul. Sprint-Anker: (i) DATEV-Realtime-Sync fuer `hr_work_time_entries` (aehnlich buchhaltung-`bexio`-Webhook-Realtime-Pattern), (ii) native iOS/Android-App via Capacitor/Cordova-Wrapper um bestehende Electron-Views, (iii) Urlaub-Abwesenheiten-Sub-Modul in `zeiterfassung`.

**4. ZEP (DE, threat: MEDIUM als IT/Consulting-KMU-Marktfuehrer + PSA-Fokus)**

ZEP ist **DE-Zeiterfassungs-Player mit PSA-Fokus (Professional Services Automation)** — deutsche Firma, IT/Consulting-KMU-Zielgruppe, Reisekosten-Modul-Ausbau 2026, ZEP-App v2.14.0 (05.12.2025) mit Business-Travel-Detection und Belegerfassung. Nicht Cosmi-Handwerk-Konkurrent, aber Cosmi-`zeiterfassung`-Konkurrent fuer IT/Consulting-KMU.

- **PSA-Fokus (Professional Services Automation)**: Projektzeit-Erfassung + Reisekosten + DATEV-Export + Rechnungsstellung ueber DATEV-Integration.
- **Business-Travel-Detection (v2.14.0)**: automatische Erkennung von Geschaeftsreisen + Belegerfassung.
- **DATEV-Export**: unidirektional CSV (nicht Realtime-Sync wie TimeTac).
- **Keine AI-Features 2026**: Roadmap kommuniziert Reisekosten-Ausbau + UX-Renewals, kein AI-Auto-Kategorisierungs- oder Draft-Feature (`zep.de/en/roadmap`).
- **Pain-Points G2/OMR 2026**: "UI wirkt bei Handwerkern sperrig — Consultant-optimiert", "kein echter Baustellen-Offline-Mode", "App-Handling ausserhalb Beratungs-Use-Cases umstaendlich".
- **Pricing (2026)**: ZEP Clock **2 EUR/User/Monat**, ZEP Compact **7 EUR/User/Monat**, ZEP Professional **18 EUR/User/Monat** (`zep.de/preise`).
- **Tech-Stack**: DE-Cloud, native iOS/Android, REST-API, DATEV-Export.
- **Gap zu Cosmi**: PSA-Reisekosten-Modul, Business-Travel-Detection, Consulting-Rechnungsstellung ueber DATEV-Integration.
- **Strategischer Hinweis**: **ZEP zielt auf Consulting/IT-KMU** — Cosmi zielt auf breiteres KMU-Spektrum inkl. Handwerk, Dienstleister, Retail. Overlap-Zone: IT/Beratungs-Cosmi-Kunden. **Cosmi-Differential fuer IT/Consulting-KMU**: Cosmi-`zeiterfassung` + Cosmi-`crm` + Cosmi-`vertraege` + Cosmi-`buchhaltung` als **Full-Cross-Modul-Story** fuer 3+6+5+6 = **20 EUR/User-Monat** gegen ZEP Compact 7 EUR/User-Monat (Zeiterfassung only). Cosmi ist teurer, aber cross-funktional. Sprint-Anker (low-prio): Reisekosten-Sub-Modul in `zeiterfassung` fuer Consulting-Cosmi-Kunden.

**5. Crewmeister (DE, threat: MEDIUM als DE-KMU-Zeiterfassung + Preis-Krieger + GPS-Feature-Vorbild)**

Crewmeister ist **DE-KMU-Zeiterfassungs-Anbieter** — mobile-first, GPS bis 2 m Genauigkeit bei Clock-In/Out, 30%-Rabatt-Kampagne 2026 (bis 12.06.2026) als Reaktion auf Zeiterfassungspflicht. Kleiner Cosmi-`zeiterfassung`-Konkurrent, aber GPS-Feature-Vorbild.

- **GPS-Location-Recording (2 m Genauigkeit)**: Standort-Erfassung bei Clock-In/Clock-Out via native App (`crewmeister.com/de/zeiterfassung/mobil`) — DSGVO-konform, weil punktuelle Erfassung (nicht kontinuierliche Ortung).
- **DATEV-CSV-Export**: unidirektional.
- **Keine AI-Features 2026**: kein AI-Auto-Kategorisierungs-Feature, Fokus auf Rabatt-Kampagne als Marketing-Antwort auf Zeiterfassungspflicht.
- **Pain-Points G2/Capterra 2026**: "App gelegentlich instabil", "Offline-Sync in Funkloch nicht robust genug", "Integrationen ausser DATEV limitiert", "Enterprise-Schichtmodelle zu unflexibel".
- **Pricing (2026)**: Einstieg ab **~2 EUR/User (Einzeltarif)**, Standard ab **5.20 EUR/User/Monat**, Premium **9 EUR/User/Monat** (`omr.com/en/reviews/product/crewmeister/pricing`).
- **Tech-Stack**: DE-Cloud, native iOS/Android, DATEV-CSV-Export.
- **Gap zu Cosmi**: GPS-Location-Recording auf Genauigkeits-Level (Cosmi hat `validateGPS`-Bounds-Check, aber keine 2-m-Genauigkeits-Marketing-Story), native iOS/Android-App mit Handschuh-Bedien-Optimierung, breitere Schichtmodelle.
- **Strategischer Hinweis**: **Crewmeister-30%-Rabatt-Kampagne 2026 zeigt Preis-Sensitivitaet des DE-KMU-Zeiterfassungs-Segments** — Cosmi's 3 EUR/User-Monat ist strukturell attraktiver als Crewmeister's 5.20 EUR/User Standard. **Aber**: Crewmeister hat GPS-2-m-Feature + native App + Offline-Sync (auch wenn "nicht robust genug"). Cosmi-Sprint-Anker: (i) GPS-Genauigkeits-Story im UI (heute nur `lat`/`lon`-NUMERIC(9,6) ohne kommunizierte Genauigkeit), (ii) Offline-Mode + PWA-Baustellen-UX (mittelfristig).

**6. Papershift (DE, threat: MEDIUM als Schicht-Primary + Zeiterfassung-Nebenmodul + DATEV/LODAS-Payroll)**

Papershift ist **DE-Schichtplanungs-Marktfuehrer mit Zeiterfassung-Nebenmodul** — Fokus Retail/Gastronomie/Pflege, DATEV/LODAS-Payroll-Integrationen 2026 ausgebaut. Wird primaer in W29-Deepdive (`schichten`-Modul) tiefer analysiert, hier nur Zeiterfassungs-Aspekt.

- **Zeiterfassung als Nebenmodul**: kein separates Field-Report-Modul; Rapporte werden ueber Standard-Reports + CSV/DATEV-Export abgebildet.
- **DATEV/LODAS-Payroll-Integrationen (Professional)**: bidirektional fuer Personal-Kosten-Sync.
- **Keine AI-Features 2026**: Fokus auf DATEV/LODAS-Integrations-Ausbau, keine AI-Auto-Kategorisierung.
- **Pain-Points Capterra 2026**: "App-Abstuerze", "verwirrende Menue-Struktur", "Freizeit-Berechnung ueber Monate defekt gemeldet", "Mobile-App unterlegen der Web-App", "Support-Chat 'awkward'".
- **Pricing (2026)**: Core **4 EUR/User/Monat**, Premium **6 EUR/User/Monat**, Professional **9 EUR/User/Monat**, Enterprise auf Anfrage; Support-Pakete separat 39/99/399 EUR/Monat.
- **Gap zu Cosmi**: DATEV/LODAS-Payroll-bidirektional (Cosmi 0 fuer HR-Zeiterfassung), Marketplace-Add-Ons + Zapier.
- **Strategischer Hinweis**: **Papershift ist Cosmi-`schichten`-Direktkonkurrent (W29-Deepdive)**, nicht Cosmi-`rapporte`. Fuer Cosmi-`zeiterfassung` ist Papershift schwacher Konkurrent, weil Zeiterfassung Nebenmodul ist. Cross-Modul-Anker: DATEV/LODAS-Payroll-Realtime als gemeinsame Sprint-Ziel fuer `zeiterfassung` + `schichten` + `buchhaltung`.

**7. Toggl Track (Estonia, threat: MEDIUM als International-Freelancer-Benchmark)**

Toggl Track ist **internationaler Freelancer/Agentur-Time-Tracking-Marktfuehrer** — Estonia-Sitz, EU-Data-Region optional, Preis-Uplift 2025-2026, kein AI-Live-Feature. Nicht DACH-KMU-Handwerk-Konkurrent, aber Referenz fuer Time-Tracking-UX.

- **Timer-basiertes Time-Tracking**: Freelancer-Fokus, Kunden-/Projekt-Tags, offene REST-API.
- **Keine AI-Live-Features 2026**: Preis-Uplift ohne AI-GA-Feature (Toggl Track $9 Starter, $18 Premium).
- **Pain-Points G2/Capterra 2026**: "Timer-Steuerung fehleranfaellig", "Preis fuer KMU zunehmend hoch empfunden", "Tarifstruktur schwer verstaendlich", "kein GPS, keine Feld-Rapporte".
- **Pricing (2026)**: Free (bis 5 User), Starter **$9/User/Monat**, Premium **$18/User/Monat**, Enterprise auf Anfrage.
- **Gap zu Cosmi**: offene REST-API mit breitem Integrations-Oekosystem, EU-Data-Region-Optional (Cosmi ist DE-Hetzner default).
- **Strategischer Hinweis**: **Toggl ist kein direkter Cosmi-Konkurrent** — Cosmi liefert Handwerk/DACH-KMU-Fokus, Toggl liefert Freelancer/Agentur-Fokus. Sprint-Anker: keine.

**8. Clockify (US, threat: LOW als Free-Tier-Krieger + US-Hosting-DSGVO-Problem)**

Clockify ist **Free-Tier-Time-Tracking-Marktfuehrer** — US-Hosting (COING Inc.), Free-Plan unlimited-Users, GPS/Geofencing ab Pro $7.99. Threat-Level low fuer Cosmi-DACH-KMU-Segment, weil US-Hosting DSGVO-Fragen aufwirft.

- **Free-Plan unlimited-Users**: Kern-USP, deutlicher Preis-Vorteil.
- **GPS + Geofencing (Pro-Tarif $7.99)**: aber "kein echtes Geofencing selbst im Enterprise" laut G2-Reviews.
- **Cross-Plattform Web/iOS/Android/Desktop**: offene REST-API.
- **Pain-Points G2/Capterra 2026**: "Bulk-Edit-Zeiten umstaendlich", "Projekt-Struktur bei vielen Kunden unuebersichtlich", "Reporting-Depth im Free-Plan zu duenn".
- **Pricing (2026)**: Basic **$3.99**, Standard **$5.49**, Pro **$7.99** (inkl. GPS), Enterprise **$11.99**.
- **Gap zu Cosmi**: Free-Plan unlimited-Users (Cosmi 3 EUR/User-Monat), offene REST-API.
- **Strategischer Hinweis**: **Clockify's US-Hosting ist DACH-KMU-strukturell-Nachteil** — Cosmi-EU-Sovereign-Story schlaegt Clockify's Preis-Vorteil im DSGVO-sensiblen Segment. Sprint-Anker: keine.

**9. Timely (Norwegen, threat: HIGH als AI-Zeiterfassungs-Marktfuehrer + DACH-Vermarktung 2026)**

Timely ist **AI-Zeiterfassungs-Marktfuehrer** — norwegische Firma, Memory-Autosheet als Kern-USP mit AI-Kategorisierung + GPS-Erfassung im Hintergrund + Auto-Tagging von Kalender-Ereignissen. DACH-Vermarktung 2026 aktiv (`timely.com/de`).

- **Memory-Autosheet (AI-Live-Feature)**: **90% Reduktion manueller Timesheet-Korrekturen** laut Vendor (`timely.com/feature/ai-timesheets`) — Kalender-Ereignisse + Anwendungs-Nutzung + Standort werden AI-kategorisiert zu automatischen Zeitbuchungen.
- **GPS-Erfassung im Hintergrund**: fuer AI-Auto-Kategorisierung — DSGVO-strukturell fraglich fuer DACH-KMU, weil kontinuierliche Ortung.
- **Cross-Plattform**: Web + native iOS/Android + Desktop.
- **Pain-Points G2 2026**: "Preis fuer KMU hoch (Enterprise-orientiert)", "AI-Kategorisierung braucht Trainings-Zeit pro Nutzer".
- **Pricing (2026)**: Starter **$11/User/Monat**, Premium **$20/User/Monat**, Unlimited **$28/User/Monat** — Enterprise-orientiert.
- **Gap zu Cosmi**: AI-Memory-Autosheet mit Kalender-/App-Auto-Kategorisierung, cross-Plattform-Timer-Sync.
- **Strategischer Hinweis (KRITISCH FUER COSMI-AI-STRATEGIE)**: **Timely ist der EINE relevante DACH-AI-Zeiterfassungs-Konkurrent** — Memory-Autosheet-Feature ist marktfeature-setzend. **Aber**: (i) Timely-GPS-Erfassung im Hintergrund ist DSGVO-Angriffsflaeche im DACH-Segment (BAG/DSB-AT-Rechtsprechung strikt gegen kontinuierliche Ortung), (ii) Enterprise-Pricing $11-$28/User schliesst Cosmi-KMU-5-30-MA-Ziel-Segment weitgehend aus. Cosmi-Chance: **AI-Rapport-Auto-Kategorisierung ohne kontinuierliche Ortung** — DSGVO-strukturell besser positioniert, Preis-strukturell besser positioniert. Sprint-Anker: `backend/internal/rapporte/ai_categorization/` als Q4-2026-Pflicht-Sprint.

**10. mobiel + noovi (DACH, threat: LOW-MEDIUM als CH-Niche-Handwerk-Feldrapport)**

mobiel (DACH, `mobiel.io`) und noovi (CH, `noovi.ch`) sind **CH/DACH-Handwerk-Feldrapport-Niche-Spezialisten** — direkte Cosmi-`rapporte`-Konkurrenten fuer CH-Handwerk-Segment.

- **Foto + Georeferenz + Vor-Ort-Unterschrift + PDF-Export**: Kern-Feature-Set beider, aehnlich Cosmi-`rapporte`.
- **CH-Markt-Fokus (noovi)**: CH-KMU-Handwerk-Zielgruppe, digitale Rapporte + Vor-Ort-Unterschrift, `noovi.ch/funktionen/rapporte`.
- **Kein oeffentliches Roadmap-Dokument (mobiel)**: Website mit gelegentlichen Service-Ausfaellen (503), unklarer Wartungs-Status.
- **Kaum G2/Capterra-Reviews**: Niche-Anbieter, geringes Ecosystem.
- **Pricing (2026)**: keine oeffentliche Preisliste; individuelle Angebote. CH-Marktumfeld vergleichbar 15-30 CHF/User/Monat (noovi + Baubit).
- **Gap zu Cosmi**: CH-Markt-Fokus + CH-Handwerker-Zertifizierungen, aktive Vor-Ort-Unterschrift-Workflow (Cosmi hat Stub).
- **Strategischer Hinweis**: **mobiel + noovi sind CH-Niche-Konkurrenten** — Cosmi-CH-Markt-Strategie ist Bexio-Partnerschaft (via `backend/internal/biz/bexio/`-OAuth-Integration aus buchhaltung-W27-Analyse). Fuer CH-Cosmi-Kunden mit Bexio-Bestand: Cosmi-`rapporte` + Bexio-Buchhaltung-Bridge = Cosmi-USP gegen mobiel/noovi (die kein CRM/Buchhaltungs-Modul haben). Sprint-Anker: CH-QR-Rechnung-Support fuer `rapporte`-basierte Rechnungsstellung (Cross-Modul mit `buchhaltung`).

---

## Cosmi-IST-Stand

**rapporte ist Cosmi's schlankstes Handwerk-Feld-Modul aus Sprint-2-Welle-2A** — Backend mit 21 Service-Methoden und klarer Approval-State-Machine, Frontend mit RapportePage-Mono-Root (1869 LOC) + SketchCanvas-Aufmass-Canvas (732 LOC) + SignatureCanvas-Stub (3 LOC). Parallel-Modul `zeiterfassung` mit HR-basiertem Modell (`hr_work_time_entries` + `hr_week_approvals` + `hr_time_categories` + `hr_time_projects`).

### Backend `backend/internal/rapporte/` — Files und LOC

| File | LOC | Rolle |
|---|---|---|
| `errors.go` | 16 | Domain-Sentinels: ErrInvalidInput, ErrNotFound, ErrAlreadyApproved, etc. |
| `models.go` | 140 | Domain-Types: WorkReport (mit ReportStatus draft/submitted/approved/rejected + Extended-Fields weather/temperature/work_start/end/break_minutes/project_name/workers), ReportLine (+ Category/Article), ReportAttachment (MinIO-Metadata), ReportStats, Worker, Measurement, MeasurementPosition, ReportTemplate |
| `postgres_repository.go` | 938 | Postgres-Repository mit Tenant-Isolation, alle CRUD-Operationen |
| `repository.go` | 73 | Repository-Interface |
| `service.go` | 636 | Business-Logic mit 21 Service-Methoden + validateGPS-Helper |
| `service_test.go` | 961 | Test-Suite (Coverage 33.9%) |
| `signature_test.go` | 165 | Signature-Persistenz-Test |
| `tenant_isolation_phase2_test.go` | 69 | Cross-Tenant-Isolation-Test |
| **TOTAL** | **2998** | **8 Files, ~2998 LOC, Test-Coverage 33.9%** |

### Backend Service-Methoden (21)

| Methode | Zweck |
|---|---|
| `CreateReport` | Draft-Rapport anlegen mit Title/Description/AuthorID/Lat/Lon/ReportDate |
| `UpdateReport` | Rapport-Felder aktualisieren (Title/Description/Lat/Lon/ReportDate), nur im Draft-Status |
| `DeleteReport` | Soft-Delete mit deleted_at |
| `GetReport` | Single-Rapport-Lookup mit Tenant-Filter |
| `ListReports` | Paginierte Liste mit Status/Author-Filter + Search |
| `SubmitReport` | Draft → Submitted (Approval-Anforderung) |
| `ApproveReport` | Submitted → Approved (Reviewer + ReviewNote) |
| `RejectReport` | Submitted → Rejected (Reviewer + ReviewNote) |
| `AddLine` / `UpdateLine` / `DeleteLine` / `ListLines` | Report-Line-CRUD |
| `UploadAttachment` / `ListAttachments` / `DeleteAttachment` | MinIO-Attachment-CRUD mit Tenant-Prefix-Path-Validierung |
| `GetReportStats` | Tenant-Level-Aggregate (Total/Draft/Submitted/Approved/Rejected-Count) |
| `ListPendingApprovals` | Approver-View der noch-nicht-approved-Rapporte |
| `SaveSignature` | Signature-Data-Speichern mit signed_at/signed_by |
| `ExportPDF` | Rapport-PDF-Export |

### Migrationen (chronologisch, rapporte + zeiterfassung-relevant)

| Migration | Inhalt | Strategischer Anker |
|---|---|---|
| 000030 | create_time_entries | Fruehere Zeiterfassungs-Basis-Tabelle |
| 000046 | create_hr_tables | HR-Employee-Profile + Foundation fuer hr_work_time_entries |
| 000069 | add_tenant_id_to_hr_employee_profiles | Tenant-Isolation-Anker |
| 000092 | **create_rapporte** | Sprint-2-Welle-2A Basis: work_reports + report_lines + report_attachments |
| 000093 | seed_rapporte_permissions | RBAC-Foundation |
| 000100 | rapporte_approve_permission | **Separate `:approve`-Berechtigung, admin-only** (Welle-2C-Sicherheits-Fix) |
| 000127 | rls_welle4_hr_role_based | HR-RLS-Wellen-4-Rollout |
| 000128 | fix_hr_document_policy_sysctx | HR-Sys-Context-Fix |
| 000143 | add_signature_to_rapporte_vermietung_vertraege | Signature-Support (signature_data/signed_at/signed_by) |
| 000162 | **full_extend_work_reports_report_lines_workers** | Extended-Feld-Report: weather/temperature/work_start/end/break_minutes/project_name + report_workers-Tabelle + report_lines.category/.article |
| 000164 | rapporte_new_permissions_seed | Permissions-Sweep |
| 000178 | **hr_time_categories** | Zeiterfassungs-Kategorien-Master |
| 000179 | hr_time_templates | Zeiterfassungs-Vorlagen |
| 000180 | **hr_week_approvals** | Wochen-Freigabe-State-Machine (open/submitted/approved/rejected) mit UNIQUE(tenant,employee,week_start) — **ArbZG-2026-Reform-relevant** |
| 000181 | hr_time_projects | Projekt-Master fuer Zeiterfassung |
| 000182 | hr_work_time_entries_extend | category_id/location_lat/lng/location_address/deleted_at |
| 000212 | hr_work_time_entries_project_id | project_id-FK |
| 000213 | **hr_company_settings_work_hours** | work_hours_per_day/max_daily_hours/break_after_hours — **konfigurierbar per Tenant** (ArbZG-Reform-Wochenbetrachtungs-Vorbereitung) |
| 000230 | rls_wiki_hr_child_tables | RLS-Rollout HR-Child-Tabellen |

### Frontend `desktop/src/renderer/src/modules/rapporte/` (2604 LOC)

- **RapportePage.tsx (1869 LOC)**: Mono-Root-Page mit 3 Tabs (`tagesberichte`/`aufmass`/`vorlagen`). Enthaelt weatherIcons-Map (Sun/Cloud/CloudRain/Snowflake/Thermometer/Wind/Droplets), Icons fuer Camera/Users/HardHat/Ruler/Package/ClipboardCheck/ShieldCheck. Types: FieldReport, ReportTemplate, WeatherType, ReportWorker, ReportActivity, ReportMaterial. Hooks: useRapporteList, useReportStats, useCreateReport, useUpdateReport, useDeleteReport, useSubmitReport. adaptWorkReport-Pattern (Backend→Frontend).
- **SketchCanvas.tsx (732 LOC)**: Aufmass-Zeichnen-Canvas fuer Handwerker — differenzierendes Feature.
- **SignatureCanvas.tsx (3 LOC)**: **Stub/Placeholder** — produktiv nicht funktionsfaehig, offene Frontend-Luecke.

### Parallel-Modul-Frontend `desktop/src/renderer/src/modules/zeiterfassung/` (~1000 LOC)

- **ZeiterfassungPage.tsx (35 LOC)**: Mono-Root-Verweis auf Components.
- **AuswertungenView.tsx (200), TeamView.tsx (132), ManualEntryDialog.tsx (200), ExportDialog.tsx (151), StundenkontoBadge.tsx (38), WeekSubmitBanner.tsx (48)**: Zeiterfassungs-Kern-Views.
- **weekUtils.ts**: Wochen-Berechnungs-Helper.
- **settings/ZeiterfassungSettingsPanel.tsx (205)**: Tenant-Settings-Panel.

### Was Cosmi-rapporte HEUTE kann (positive Bestandsaufnahme)

- ✅ **Approval-State-Machine**: draft → submitted → approved/rejected mit `ErrAlreadyApproved`-Rueckwaerts-Blocker
- ✅ **GPS-Tag**: `lat`/`lon`-Erfassung mit `validateGPS`-Bounds-Check (-90..90 / -180..180)
- ✅ **Signature-Backend**: `SaveSignature`-RPC + signature_data/signed_at/signed_by (Migration 143)
- ✅ **Extended Field-Report**: weather/temperature/work_start/end/break_minutes/project_name + report_workers (Migration 162)
- ✅ **Aufmass-Canvas**: SketchCanvas.tsx 732 LOC — differenzierendes Handwerk-Feature
- ✅ **MinIO-Attachments**: Upload/List/Delete mit Tenant-Prefix-Path-Validierung (Welle-2C-Sicherheits-Fix)
- ✅ **Separate `:approve`-Permission**: admin-only (Migration 100)
- ✅ **Tenant-Isolation**: `tenant_isolation_phase2_test.go` + Cross-Tenant-Filter in allen SELECTs
- ✅ **PDF-Export**: `ExportPDF`-RPC
- ✅ **Report-Templates**: reusable Templates mit default_lines_json
- ✅ **Rapport-Multi-Worker**: report_workers-Tabelle mit name/role/hours
- ✅ **Aufmass-Positionen**: Measurement + MeasurementPosition mit unit/quantity/unit_price
- ✅ **Feature-Flag**: `modules.rapporte` (SafeRisk, LLMToggleSafe)

### Was Cosmi-zeiterfassung HEUTE kann (parallel)

- ✅ **HR-Zeit-Erfassung**: `hr_work_time_entries` mit category_id/project_id/location_lat/lng
- ✅ **Wochen-Freigabe**: `hr_week_approvals` (open/submitted/approved/rejected) — **ArbZG-2026-Reform-relevant**
- ✅ **Zeit-Kategorien + Vorlagen**: `hr_time_categories` + `hr_time_templates`
- ✅ **Company-Settings**: `hr_company_settings.work_hours_per_day/max_daily_hours/break_after_hours` (Migration 213)
- ✅ **Export-Dialog + Team-View + Auswertungen**: Frontend-Kern-Views
- ✅ **StundenkontoBadge**: Ueberstunden-Anzeige

### Was Cosmi-rapporte HEUTE NICHT kann (strategische Luecken)

- ❌ **SignatureCanvas-Frontend**: 3-LOC-Stub, produktiv nicht funktionsfaehig. Backend-Weg funktioniert, aber Frontend-Erfassung fehlt. **Sofortiger Sprint-Fix.**
- ❌ **Offline-Mode / Baustellen-Sync**: `authenticatedFetch.ts` liefert `OfflineError` bei Mutations, aber **kein IndexedDB-Queue-Persistenz-Layer**. Baustellen-Handwerk-Use-Case ohne Netz nicht abgedeckt.
- ❌ **Multi-Stage-Freigabe-Workflow**: aktuelle State-Machine ist linear (Draft → Submitted → Approved/Rejected mit 1 Reviewer). Mehrstufige Freigabe (Team-Leiter → Projekt-Leiter → Buchhaltung) fehlt.
- ❌ **AI-Rapport-Auto-Kategorisierung**: keine AI-Integration fuer Positionsbeschreibung → Kategorie/Artikel-Vorschlag.
- ❌ **AI-Timesheet-Draft**: kein Memory-Autosheet-Aequivalent (Timely-Kern-USP).
- ❌ **Voice-Input**: kein Sprach-zu-Text-Rapport-Erfasser (HERO Report angekuendigt).
- ❌ **DWD-Wetter-API-Auto-Erfassung**: `weather`/`temperature`-Felder werden manuell befuellt, keine Auto-Erfassung ueber Wetter-API + GPS-Standort.
- ❌ **Native iOS/Android-App**: Cosmi ist Desktop-Electron + PWA — keine Handschuh-Bedien-optimierte Baustellen-Native-App.
- ❌ **Handschuh-taugliches UI-Skinning**: Standard-Cosmi-UI ist nicht Handschuh-Bedien-optimiert (grosse Touch-Bereiche, Ein-Tap-Aktionen fehlen).
- ❌ **Datanorm/IDS-Connect**: Handwerk-Material-Katalog-Integration fehlt (HERO Software liefert).
- ❌ **Terminal-Integration**: keine Empfangs-Buero-Hardware-Zeit-Erfassung (TimeTac liefert).
- ❌ **DATEV-Realtime-Sync fuer hr_work_time_entries**: `hr`-Backend hat keinen DATEV-Adapter fuer Zeit-/Lohn-Buchhaltungs-Sync (TimeTac + Papershift + Crewmeister liefern).
- ❌ **Bautagebuch-Chronologie**: Foto-Sammlungen pro Baustelle als chronologische Zeitlinie fehlen (123erfasst-Kern-USP).
- ❌ **GPS-Genauigkeits-Story**: `lat`/`lon`-NUMERIC(9,6) ist technisch praezise, aber UI kommuniziert keine Genauigkeit (Crewmeister vermarktet "2 m Genauigkeit").
- ❌ **GPS-Consent-Flow**: DSGVO-konformer Consent-Banner + tenant-Weit-Aktivierungs-Option + Audit-Log fehlt — **Compliance-Risiko fuer Cosmi-Kunden mit Betriebsrat**.
- ❌ **rapporte↔zeiterfassung Domain-Konsolidierung**: 2 parallele Datenmodelle (`work_reports` vs `hr_work_time_entries`), keine gemeinsame Woche-Aggregation zwischen Rapport-Zeiten und HR-Zeiterfassung. Strukturelle Domain-Design-Schuld.
- ❌ **Urlaub/Abwesenheiten-Modul**: TimeTac hat als drittes Modul; Cosmi hat kein `abwesenheiten`-Modul.
- ❌ **Reisekosten-Modul**: ZEP hat als Modul-Add-On; Cosmi hat kein Reisekosten-Modul.
- ❌ **Rapport → Rechnung Cross-Modul-Auto-Bridge**: `finance/invoice/LinkTimeTracking`-RPC existiert im buchhaltung-Modul, aber Frontend-UX fuer "aus Rapport Rechnung erzeugen" fehlt.
- ❌ **Frontend-Test-Coverage**: RapportePage 1869 LOC ohne dedizierten Component-Test-Pfad.
- ❌ **rapporte-Backend-Test-Coverage**: 33.9% unter dem 40%-Referenz-Ziel.
- ❌ **TenantInboundUnaryInterceptor**: rapporte ist eines der 13 Binaries ohne den Interceptor (R3-P0-3 offen).

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | 123erfasst | HERO Software | TimeTac | ZEP | Crewmeister | Papershift | Toggl | Clockify | Timely | mobiel |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Rapport-Erstellung** | ✅ 21 RPCs | ✅ Kern-USP | ✅ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ✅ Kern-USP |
| **Approval-State-Machine** | ✅ 4 States | ✅ Multi-Stage | ✅ Multi-Stage | ✅ | ✅ | ⚠️ Limited | ✅ Professional | ➖ | ⚠️ Enterprise | ➖ | ⚠️ Limited |
| **Multi-Stage-Freigabe** | ❌ Linear | ✅ Bau-Workflow | ✅ | ⚠️ Task-Ebene | ⚠️ | ❌ | ⚠️ Professional | ❌ | ❌ | ❌ | ❌ |
| **GPS-Erfassung (punktuell)** | ✅ validateGPS + Bounds | ✅ Auto beim Foto | ✅ | ✅ Geofencing (Pro) | ➖ | ✅ 2m-Genauigkeit | ➖ | ❌ | ✅ Pro-Tarif | ⚠️ Hintergrund | ✅ |
| **GPS-Genauigkeits-Story** | ⚠️ Technisch praezise, kein Marketing | ✅ Foto-GPS | ✅ | ⚠️ | ➖ | ✅ 2m vermarktet | ➖ | ❌ | ⚠️ | ⚠️ | ⚠️ |
| **GPS-Consent-Flow (DSGVO)** | ❌ Kein Consent-Banner | ✅ | ✅ | ✅ Betriebsrat-Workflow | ➖ | ✅ | ➖ | ➖ | ⚠️ US-Recht | ⚠️ DSGVO-fraglich | ⚠️ |
| **Signatur-Backend** | ✅ SaveSignature-RPC | ✅ | ✅ produktiv | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ✅ |
| **Signatur-Frontend-Canvas** | ❌ 3-LOC-Stub | ✅ | ✅ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ✅ |
| **eIDAS-Konformitaet** | ⚠️ Backend-ready, Frontend-Stub | ✅ | ✅ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ✅ |
| **Foto-Attachment mit Georeferenz** | ⚠️ MinIO-Upload, keine Auto-GPS-Verknuepfung | ✅ Marktbenchmark | ✅ | ➖ | ➖ | ⚠️ | ➖ | ➖ | ➖ | ➖ | ✅ |
| **Aufmass-Canvas (Handwerk)** | ✅ SketchCanvas 732 LOC | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Limited |
| **Wetter-Erfassung (manuell)** | ✅ weather+temp Fields | ✅ | ✅ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ⚠️ |
| **DWD-Wetter-API-Auto** | ❌ | ✅ Marktbenchmark | ⚠️ Roadmap | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| **Multi-Worker pro Rapport** | ✅ report_workers | ✅ | ✅ | ➖ | ➖ | ⚠️ | ⚠️ | ➖ | ➖ | ➖ | ✅ |
| **Report-Templates** | ✅ ReportTemplate | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| **PDF-Export** | ✅ ExportPDF | ✅ | ✅ | ⚠️ CSV | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **HR-Zeiterfassung (Wochen)** | ✅ hr_work_time_entries + hr_week_approvals | ⚠️ Add-On | ✅ | ✅ Kern-USP | ✅ Kern-USP | ✅ Kern-USP | ✅ | ⚠️ Timer-only | ✅ | ✅ Kern-USP AI | ➖ |
| **§16 ArbZG-Reform-ready** | ✅ hr_work_time_entries elektronisch | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| **Zeit-Kategorien + Projekte** | ✅ hr_time_categories/_projects | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ AI-Auto | ➖ |
| **DATEV-CSV-Export (Zeit/Lohn)** | ⚠️ Backend im biz/datev-Modul, aber nicht rapporte-Cross-Modul | ✅ Lodas | ✅ Lodas | ✅ Lodas + L&G Realtime | ✅ | ✅ | ✅ LODAS | ❌ | ❌ | ⚠️ | ⚠️ |
| **DATEV-Realtime-Sync (Zeit)** | ❌ | ⚠️ | ⚠️ | ✅ Kern-USP 2025-Refresh | ❌ CSV | ❌ CSV | ❌ CSV | ❌ | ❌ | ❌ | ❌ |
| **AI-Auto-Kategorisierung** | ❌ | ❌ | ⚠️ HERO Report Q4 2026 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Memory-Autosheet | ❌ |
| **AI-Timesheet-Draft** | ❌ | ❌ | ⚠️ HERO Report angekuendigt | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Kern-USP 90% | ❌ |
| **AI-Voice-Input Rapport** | ❌ | ❌ | ⚠️ HERO Report angekuendigt | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **AI-Telefon-Assistent** | ❌ | ❌ | ✅ HERO Voice GA 2026 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Offline-Mode Baustelle** | ❌ OfflineError-Guard, kein Queue | ✅ Marktbenchmark | ✅ produktiv | ⚠️ Partial | ⚠️ Partial | ⚠️ "nicht robust" | ❌ | ⚠️ Timer | ⚠️ Partial | ⚠️ | ⚠️ |
| **Native iOS/Android-App** | ❌ Electron + PWA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Handschuh-taugliches UI** | ❌ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ⚠️ | ❌ | ❌ | ⚠️ | ✅ |
| **Terminal-Integration** | ❌ | ⚠️ | ⚠️ | ✅ Kern-USP | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Urlaub/Abwesenheiten-Modul** | ❌ | ⚠️ | ✅ | ✅ Leave Management | ❌ | ⚠️ | ✅ | ❌ | ⚠️ | ❌ | ❌ |
| **Reisekosten-Modul** | ❌ | ❌ | ⚠️ | ❌ | ✅ Kern-USP 2026 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Rapport→Rechnung Cross-Modul** | ⚠️ LinkTimeTracking-Backend-RPC, kein Frontend | ✅ Bautagebuch→Rechnung | ✅ | ⚠️ | ⚠️ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| **Datanorm/IDS-Connect** | ❌ | ✅ | ✅ Kern-USP | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Cross-Modul-CRM-Link** | ⚠️ contact_id in finance/invoice, nicht rapporte | ⚠️ | ✅ Native CRM | ⚠️ | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ |
| **Cross-Modul-Vertraege-Link** | ❌ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Self-Host-Option** | ✅ Orbit-Roadmap | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **EU-Sovereign-Hosting** | ✅ Hetzner DE | ✅ DE | ✅ DE | ✅ AT | ✅ DE | ✅ DE | ✅ DE | ✅ Optional | ❌ US | ❌ NO | ✅ CH |
| **Pricing (EUR/User/Monat)** | **3 (rapporte) + 3 (zeit)** | **30-50** | **69-345** | **3-9 + 19.50 Basis** | **2-18** | **~2-9** | **4-9** | **$9-$18** | **$3.99-$11.99** | **$11-$28** | **~15-30 CHF** |

Legende: ✅ Full implementiert, ⚠️ Eingeschraenkt/Partial, ➖ N/A fuer Tool-Kategorie, ❌ Fehlt vollstaendig

**Lesart der Tabelle**:
- **Cosmi-Staerken (vergleichbar mit Markt)**: Rapport-Erstellung mit 21 RPCs, GPS-punktuell mit Bounds-Check, Signatur-Backend (Backend-only), Aufmass-Canvas als differenzierendes Handwerk-Feature, Multi-Worker pro Rapport, Report-Templates, HR-Wochen-Freigabe via `hr_week_approvals` (**ArbZG-2026-Reform-ready**), Self-Host-Option, EU-Sovereign-Hosting.
- **Cosmi-Kritische-Luecken (Markt hat Pflicht-Stake)**: **SignatureCanvas-Frontend-Stub** (3 LOC vs. 123erfasst/HERO-produktiv), Offline-Mode Baustelle, Native iOS/Android-App, Handschuh-taugliches UI, GPS-Consent-Flow (DSGVO), Multi-Stage-Freigabe-Workflow.
- **Cosmi-Strategische-Luecken (Markt-Standard, aber differenzierend addressierbar)**: DATEV-Realtime-Sync fuer Zeit (TimeTac 2025-Refresh), AI-Auto-Kategorisierung (Timely-Kern-USP), AI-Voice-Input-Rapport (HERO Report Q4 2026), DWD-Wetter-API-Auto (123erfasst-Marktbenchmark), Bautagebuch-Chronologie, Datanorm/IDS-Connect.
- **Cosmi-Differential-Pricing**: 3 EUR/User-Monat pro Modul (rapporte + zeiterfassung = 6 EUR/User-Monat kombiniert) ist **billiger** als alle DACH-Handwerk-Konkurrenten (123erfasst 30-50, HERO 69-345) und im Cluster mit TimeTac Essential (3 EUR + 19.50 Basisgebuhr), ZEP Clock (2), Papershift Core (4), Crewmeister Standard (5.20). **Cosmi-USP fuer Handwerk-KMU 5-30 MA**: gleicher Preis-Cluster wie TimeTac/ZEP/Crewmeister/Papershift, aber **mit Rapport + Aufmass + Signatur + Feld-Wetter** — die anderen liefern nur Zeiterfassung ohne Rapport-Feld-Story.

---

## Top-3 Strategische Empfehlungen

### Empfehlung 1: rapporte↔zeiterfassung Domain-Konsolidierung als Q3-2026-Struktur-Sprint (ADR-Pflicht)

**Was**: Design-Entscheidung zwischen zwei Optionen: (A) **Konsolidierung**: `rapporte` + `zeiterfassung` zu einem Cosmi-Modul `zeiten` verschmelzen, gemeinsame Domain-Schicht mit `work_reports` und `hr_work_time_entries` als Sub-Types eines gemeinsamen `TimeRecord`-Root-Types, gemeinsame Wochen-Aggregation via `hr_week_approvals`, gemeinsame Approval-State-Machine. (B) **Bewusste Trennung mit klarem Domain-Cut**: `rapporte` bleibt Field-Rapport-Handwerk-Fokus (Draft/Submitted/Approved/Rejected mit Signatur/Aufmass/Foto), `zeiterfassung` bleibt HR-Pflicht-Erfassung (open/submitted/approved/rejected pro Woche) — aber **Cross-Modul-Bridge**: Rapport-`work_start`/`work_end`/`break_minutes` werden automatisch als `hr_work_time_entries` fuer den `AuthorID` gebucht (via Event-Emitter aus `rapporte.SubmitReport`).

**Warum jetzt P0**:
- **§16 ArbZG-Referentenentwurf (Juni 2026) schreibt elektronische Erfassung von Beginn/Ende/Dauer der taeglichen Arbeitszeit vor** — Cosmi-Handwerk-Kunde, der nur `rapporte` bucht (nicht `zeiterfassung`), erfuellt das nicht sauber, weil `hr_week_approvals`-Wochen-Aggregation fehlt.
- **Domain-Klarheit fuer Sales-Story**: heute muss Sales erklaeren, warum `rapporte` und `zeiterfassung` beide gebraucht werden — der Markt (TimeTac/Crewmeister/ZEP) verkauft **ein** Zeiterfassungs-Produkt mit Konfigurations-Optionen.
- **Verhindert Duplikations-Sprint-Kosten**: State-Machine, GPS-Erfassung, Approval-Logic sind heute doppelt implementiert — jede Sprint-Aenderung muss zweimal gemacht werden.

**Wie**: (i) ADR-0009 (naechste ADR-Nummer nach ADR-0007-buchhaltung) mit Titel "Rapporte + Zeiterfassung Domain-Konsolidierung" schreiben, Optionen A/B/Hybrid detaillieren, Entscheidung dokumentieren. (ii) Bei Option A: neue Migration `000232_rename_rapporte_to_zeiten_module.up.sql` mit Feature-Flag-Umbenennung + Backend-Package-Move (Umbenennung von `backend/internal/rapporte/` und Zusammenfuehrung mit `hr/`-Sub-Bereich). Frontend-Merge von `RapportePage.tsx` + `ZeiterfassungPage.tsx` zu `ZeitenPage.tsx` mit Tab-Splitting. (iii) Bei Option B: Event-Emitter aus `rapporte.SubmitReport` → `hr_work_time_entries.CreateFromRapport`-RPC, Frontend `RapportePage` zeigt Rapport-Woche im ZeiterfassungsBadge inline.

**Schaetzung**: Option A: ~6-8 PT (grosser Migrations-Sprint mit Frontend-Merge). Option B: ~3-4 PT (Event-Emitter + Cross-Modul-Bridge). **Empfehlung: Option B als Q3-2026-Sprint, Option A als Q1-2027-Refactor-Kandidat**.

**Anti-Muster vermeiden**: Nicht "beide Module weiter parallel maintainen ohne Cross-Modul-Bridge" — das ist der heutige Zustand und der Kern-Problem.

### Empfehlung 2: SignatureCanvas-Ausbau + Baustellen-Offline-Mode + PWA-Handschuh-UI als Q3-2026-Handwerk-Sprint (P0)

**Was**: Drei zusammenhaengende Frontend-Sprints, die den Handwerk-Baustellen-Use-Case produktions-tauglich machen: (i) **SignatureCanvas.tsx-Ausbau** von 3-LOC-Stub auf produktions-tauglichen Canvas-Signatur-Erfasser mit `react-signature-canvas` oder `signature_pad`-npm-Library, base64-PNG-Serialisierung, Anbindung an bestehenden `SaveSignature`-Backend-RPC. (ii) **Offline-Mode fuer rapporte**: IndexedDB-Queue-Persistenz fuer Rapport-Erstellung/Update ohne Netz, Service-Worker-basiertes Background-Sync-on-Reconnect, `sync_pending`-Status-Flag im `WorkReport`-Model, konfliktbehandlungs-Strategie fuer paralleles Backend-Update. (iii) **PWA-Manifest + Handschuh-Bedien-UI** fuer RapportePage mit vergroesserten Touch-Bereichen (Ein-Tap-Aktionen fuer Draft-Anlegen + Rapport-Absenden + Signatur-Erfassen), landscape-Orientierungs-Optimierung fuer Tablet-Nutzung, Handschuh-Test-Kriterium (Test-Targets 48x48px).

**Warum jetzt P0**:
- **SignatureCanvas-Stub ist Produkt-Bug**: Backend-Weg ist funktional, aber Frontend-Erfassung fehlt — kein Cosmi-Kunde kann heute Vor-Ort-Signatur einholen. Das ist die Ein-Zeile-Diskrepanz zwischen "Cosmi-rapporte hat Signatur" (Marketing) und "Cosmi-rapporte hat keine Signatur" (Produkt).
- **Offline-Mode ist Handwerk-Baustellen-Kern-Requirement**: 123erfasst und HERO Software haben es produktiv, Cosmi 0. Cosmi-Handwerk-Kunden auf Baustellen mit Funkloch koennen heute keine Rapporte erstellen.
- **PWA-Handschuh-UI ist Baustellen-Bedien-Requirement**: Handwerker auf Baustelle nutzen Handschuhe (Sicherheit + Waerme), Standard-Cosmi-UI ist nicht Handschuh-Bedien-optimiert.
- **§16 ArbZG-Reform verstaerkt Baustellen-Erfassungs-Pflicht**: elektronische Erfassung "am Tag der Arbeitsleistung" bedeutet fuer Baustellen-Handwerk: **auf Baustelle erfassen, nicht abends am Buero-Desktop**.

**Wie**: (i) SignatureCanvas: `npm install react-signature-canvas`, Component-Refactor, Test-Add (min. 3 Test-Cases: leere Canvas, Signatur-erfasst, base64-Serialisierung). (ii) Offline-Mode: neue `desktop/src/renderer/src/api/queue/` mit IndexedDB-Queue-Persistenz, Service-Worker fuer Background-Sync (bereits PWA-Foundation vorhanden), Konflikterkennung via `updated_at`-Timestamp-Compare. (iii) PWA-Handschuh-UI: Tailwind-Custom-Klassen fuer `handshoe-mode`-Toggle (per Tenant-Setting), vergroesserte Buttons/Inputs, landscape-Auto-Rotation-Handling.

**Schaetzung**: SignatureCanvas ~1 PT, Offline-Mode ~4-5 PT, PWA-Handschuh-UI ~2-3 PT. **Gesamt ~7-9 PT, Q3-2026-Sprint-Slot.**

**Cosmi-Differential**: gegen 123erfasst-Baustellen-Benchmark (30-50 EUR/User-Monat) mit Cosmi-3-EUR-Preis + Baustellen-Offline-Story + Handschuh-UI + Signature-Canvas produktiv — **10-facher Preis-Rabatt bei erreichtem Baustellen-Feature-Parity**.

### Empfehlung 3: AI-Rapport-Auto-Kategorisierung + Voice-Input-Layer als Q4-2026-Differential-Sprint (P1)

**Was**: Zwei zusammenhaengende AI-Sprints, die Cosmi-rapporte im DACH-KMU-Segment differenzieren: (i) **AI-Rapport-Auto-Kategorisierung**: neuer `backend/internal/rapporte/ai_categorization/`-Pfad mit LLM-Adapter (Mistral-Medium oder Ollama-Local-Model fuer DSGVO-Sovereign), Input: Rapport-Description + report_lines-Description + report_attachments-Metadata + report_workers, Output: Kategorie-Vorschlag pro Line + Artikel-Zuordnung (fuer report_lines.category/.article) mit Confidence-Score, aktive Lern-Schleife via `ai_categorization_corrections`-Tabelle. (ii) **Voice-Input-Layer im RapportePage.tsx**: Web-Speech-API-basierter Sprach-zu-Text-Erfasser (Client-side, DSGVO-freundlich weil keine Server-Uebertragung), Rapport-Description und report_lines.description via Sprach-Diktat, Baustellen-Handschuh-freundlich.

**Warum jetzt P1** (nicht P0, weil kein akuter Zeitdruck):
- **AI-Feature-Fenster ist offen im DACH-KMU-Zeiterfassungs-Segment**: TimeTac, ZEP, Crewmeister, Papershift, 123erfasst, Clockify, Toggl **haben KEIN Live-AI-Feature 2026**. Nur Timely (Enterprise-Segment) + HERO Software (Handwerk-Premium-Segment 69+ EUR) haben AI live oder angekuendigt.
- **Timely-DACH-Vermarktung 2026** setzt Erwartungshaltung auf **AI-Timesheet-Draft** — Cosmi kann mit **AI-Rapport-Auto-Kategorisierung** eine differenzierende Position einnehmen (nicht kopieren, sondern angrenzend positionieren).
- **HERO Report Voice-Input angekuendigt fuer 2026** — Cosmi Voice-Input im Q4 2026 waere **vor oder mit** HERO Report live, im 3-EUR-KMU-Preis-Cluster vs. HERO 69-EUR-Preis-Cluster.
- **Web-Speech-API ist DSGVO-strukturell besser** als Server-side-STT (kein Audio-Upload zum Cosmi-Backend), passt zur Cosmi-EU-Sovereign-Story.
- **AI-Modell-Wahl: Mistral-Medium (EU-Anbieter Paris, Apache-2.0-Open-Weight fuer Self-Host)** — passt zur Mistral-OCR-4-Sprint-Empfehlung aus buchhaltung-W27 (`daily/2026-06-25-evening.md` Item mit n_sources:4). Backend-Adapter-Reuse.

**Wie**: (i) AI-Auto-Kategorisierung: neuer Pfad `backend/internal/rapporte/ai_categorization/service.go` mit Mistral-Adapter-Reuse aus geplantem einvoice-AI-Extraction-Sprint (buchhaltung-W27-Empfehlung), Prompt-Template mit Rapport-Kontext + verfuegbare Kategorien (aus `hr_time_categories` gelesen), Confidence-Threshold-Config pro Tenant. (ii) Voice-Input: `useSpeechRecognition`-Hook mit `webkitSpeechRecognition`-Fallback, DE-DE-Sprach-Locale-Default, Interim-Result-Update in RapportePage-Description-Field, Ende-erkannt-Autocomplete.

**Schaetzung**: AI-Auto-Kategorisierung ~5-6 PT (nach Mistral-Adapter aus buchhaltung-Sprint-Reuse), Voice-Input ~3-4 PT. **Gesamt ~8-10 PT, Q4-2026-Sprint-Slot.**

**Cosmi-Differential**: **erster AI-differenzierender KMU-Zeiterfassungs-Player im DACH-Segment unter 10 EUR/User-Monat**. Story: "Cosmi-rapporte mit KI-Kategorisierung + Voice-Input fuer 3 EUR/User-Monat — HERO Software liefert Aehnliches fuer 69 EUR/User-Monat, alle anderen (TimeTac/ZEP/Crewmeister/Papershift/123erfasst) haben keine live AI."

**EU-AI-Act Article 50 Disclosure-Pflicht (02.08.2026)**: jede AI-Funktion braucht Disclosure-Badge — Cosmi kann das von Anfang an einbauen (wie in buchhaltung-W27 empfohlen), Konkurrenten (Timely + HERO) muessen rueckwirkend auditieren.

**Anti-Muster vermeiden**: Nicht "AI-Timesheet-Draft" bauen (das ist Timely-USP mit 90%-Korrektur-Reduktion und ausgereiften Kalender-/App-Ingestion-Pipelines) — Cosmi's Chance ist die angrenzende Rapport-Kategorisierung + Voice-Input, nicht die Timesheet-Draft-Kopie.

---

## Quellen

Diese Empfehlungen stuetzen sich auf Live-Recherche (Juli 2026) und die zentralen DACH-KMU-Zeiterfassungs-/Rapport-Marktbeobachtungen:

**Zeiterfassungs-Reform DE**:
- BAG-Beschluss 1 ABR 22/21 (13.09.2022) — [bundesarbeitsgericht.de/entscheidung/1-abr-22-21](https://www.bundesarbeitsgericht.de/entscheidung/1-abr-22-21/)
- Referentenentwurf ArbZG-Analyse — [cmshs-bloggt.de](https://www.cmshs-bloggt.de/arbeitsrecht/referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes-liegt-endlich-vor/)
- Uebergangsfristen — [deubner-recht.de](https://www.deubner-recht.de/themen/arbeitszeit/neufassung-arbeitszeitgesetz.html)
- Reform-Zusammenfassung — [hrtime.de/blog/arbeitszeitgesetz-2026-alle-aenderungen](https://www.hrtime.de/blog/arbeitszeitgesetz-2026-alle-aenderungen/)
- IHK Rhein-Neckar Zeiterfassung 2026 — [ihk.de/rhein-neckar/recht/arbeitsrecht/arbeitszeiterfassung-5631422](https://www.ihk.de/rhein-neckar/recht/arbeitsrecht/arbeitszeiterfassung-5631422)
- clockin Baustellen-Reform-Kontext — [clockin.de/blog/reform-des-arbeitszeitgesetzes](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026)

**GPS/DSGVO-Kontext**:
- Dr. Datenschutz GPS am Arbeitsplatz — [dr-datenschutz.de/gps-ueberwachung-am-arbeitsplatz-und-der-datenschutz](https://www.dr-datenschutz.de/gps-ueberwachung-am-arbeitsplatz-und-der-datenschutz/)
- Factorial HR GPS-Urteil — [factorialhr.de/blog/gerichtsurteil-gps-ueberwachung](https://factorialhr.de/blog/gerichtsurteil-gps-ueberwachung/)
- DSB AT GPS-Tracking-Stopp Nov 2025 — [dataprotect.at/2025/11/27](https://www.dataprotect.at/2025/11/27/gps-tracking-in-dienstfahrzeugen-dsb-stoppt-einsatz-von-gps-tracker-mangels-erforderlichkeit/)
- Haufe GPS-Firmenfahrzeuge — [haufe.de/recht/arbeits-sozialrecht](https://www.haufe.de/recht/arbeits-sozialrecht/wann-ist-gps-tracking-von-firmenfahrzeugen-zulaessig_218_689606.html)

**Konkurrenz-Produkt-Docs 2026**:
- ZEP Preise + Roadmap — [zep.de/preise](https://www.zep.de/preise), [zep.de/en/roadmap](https://www.zep.de/en/roadmap)
- TimeTac API + DATEV Lodas — [docs.timetac.com](https://docs.timetac.com), [timetac.com/en/integration-api/datev-lodas](https://www.timetac.com/en/integration-api/datev-lodas/)
- Crewmeister mobil + GPS 2m — [crewmeister.com/de/zeiterfassung/mobil](https://crewmeister.com/de/zeiterfassung/mobil)
- 123erfasst Preise + neue UI 2026 — [123erfasst.de/preise](https://123erfasst.de/preise/), [buildingnet.de/digitalisierung/123erfasst-mit-neuer-benutzeroberflaeche](https://www.buildingnet.de/digitalisierung/123erfasst-mit-neuer-benutzeroberflaeche.htm), [123erfasst.de/fotodokumentation](https://123erfasst.de/fotodokumentation/)
- HERO Software Preise + AI-Roadmap — [hero-software.de/preise](https://hero-software.de/preise), [hero-software.de/ai/voice](https://hero-software.de/ai/voice), [hero-software.de/features/recap-2025](https://hero-software.de/features/recap-2025), [sbz-online.de](https://www.sbz-online.de/meldungen/digitale-tools-hero-ai-ki-fuer-effizientere-ablaeufe-im-handwerk)
- Papershift Pricing — [papershift.com/en](https://www.papershift.com/en), [anyworks.com/Papershift](https://www.anyworks.com/Papershift)
- Harvest Pricing + Bending-Spoons-Kritik — [getharvest.com/pricing](https://www.getharvest.com/pricing), [trackingtime.co](https://trackingtime.co/time-tracking-software/harvest-price-increase-agencies.html)
- Toggl Pricing — [toggl.com/track/pricing](https://toggl.com/track/pricing/)
- Clockify Pricing — [clockify.me/pricing](https://clockify.me/pricing)
- Timely AI Timesheets — [timely.com/feature/ai-timesheets](https://www.timely.com/feature/ai-timesheets/)
- noovi CH Rapporte — [noovi.ch/funktionen/rapporte](https://noovi.ch/funktionen/rapporte)
- Kimai Preisvergleich 2026 — [kimai.org/en/blog/2025/price-comparison](https://www.kimai.org/en/blog/2025/price-comparison)
- Basicthinking Projektzeiterfassung Vergleich 2026-06-15 — [basicthinking.de/blog/2026/06/15/projektzeiterfassung-im-vergleich](https://www.basicthinking.de/blog/2026/06/15/projektzeiterfassung-im-vergleich-welche-software-lohnt-sich-wirklich/)
- Hubstaff Best AI Time Tracking 2026 — [hubstaff.com/blog/best-ai-time-tracking-software](https://hubstaff.com/blog/best-ai-time-tracking-software/)

**Cosmi-interne Quellen**:
- `backend/internal/rapporte/` (8 Files, ~2998 LOC, 21 Service-Methoden)
- `backend/internal/rapporte/service.go` (636 LOC, validateGPS, State-Machine)
- `backend/internal/rapporte/models.go` (140 LOC, WorkReport/ReportLine/Worker/Measurement/ReportTemplate)
- `backend/migrations/000092_create_rapporte.up.sql` (Basis-Schema)
- `backend/migrations/000162_full_extend_work_reports_report_lines_workers.up.sql` (Extended Field-Report + report_workers)
- `backend/migrations/000143_add_signature_to_rapporte_vermietung_vertraege.up.sql` (Signatur-Basis)
- `backend/migrations/000100_rapporte_approve_permission.up.sql` (admin-only :approve)
- `backend/migrations/000178_hr_time_categories.up.sql` + `000179_hr_time_templates.up.sql` + `000180_hr_week_approvals.up.sql` + `000181_hr_time_projects.up.sql` + `000182_hr_work_time_entries_extend.up.sql` + `000212_hr_work_time_entries_project_id.up.sql` + `000213_hr_company_settings_work_hours.up.sql`
- `desktop/src/renderer/src/modules/rapporte/RapportePage.tsx` (1869 LOC), `SketchCanvas.tsx` (732 LOC), `SignatureCanvas.tsx` (3 LOC Stub)
- `desktop/src/renderer/src/modules/zeiterfassung/` (~1000 LOC gesamt)
- `desktop/src/renderer/src/api/utils/authenticatedFetch.ts` (OfflineError-Guard)
- `backend/internal/featureflag/registry.go:74` (modules.rapporte SafeRisk LLMToggleSafe)
- `.knowledge/pricing.md` (Rapporte 3 EUR + Zeiterfassung 3 EUR pro User-Monat, Handwerk-Paket ~26 EUR)
- `.knowledge/milestones.md` (Welle-2A-Sprint-2 Coverage 33.9-35.6%)
- `.knowledge/architektur.md` (Rapport-Modul :50074, Approval-State-Machine, GPS-Tag Sprint-2-Welle-2A)
- `.knowledge/security.md` (R3-P0-3 offen: 13 Binaries ohne TenantInboundUnaryInterceptor inkl. rapporte)
- `monthly/2026-06-29-deepdive-buchhaltung.md` (Mistral-OCR-4-Sprint-Empfehlung, AI-Adapter-Reuse-Muster)

---

## Picks (vorgeschlagen)

[ ] 🟢 **rapporte↔zeiterfassung Domain-Konsolidierung ADR-0009** (Q3-2026-Pflicht, Option-B-Bridge empfohlen, ~3-4 PT)
[ ] 🟢 **SignatureCanvas.tsx-Ausbau von 3-LOC-Stub auf produktions-tauglich** (react-signature-canvas, ~1 PT, sofort)
[ ] 🟢 **Baustellen-Offline-Mode fuer rapporte** (IndexedDB-Queue + Service-Worker-Sync, ~4-5 PT, Q3-2026)
[ ] 🟢 **PWA-Manifest + Handschuh-Bedien-UI** (Tenant-Setting, vergroesserte Touch-Bereiche, ~2-3 PT, Q3-2026)
[ ] 🟡 **AI-Rapport-Auto-Kategorisierung** (Mistral-Adapter-Reuse aus buchhaltung, ~5-6 PT, Q4-2026, → followup 30d)
[ ] 🟡 **Voice-Input-Layer via Web-Speech-API** (Client-side, DSGVO-freundlich, ~3-4 PT, Q4-2026, → followup 30d)
[ ] 🟡 **GPS-Consent-Flow + Audit-Log** (DSGVO-Compliance, ~2 PT, Q3-2026, → followup 14d Sales-Anfrage)
[ ] 🟡 **DATEV-Realtime-Sync fuer hr_work_time_entries** (aehnlich buchhaltung-bexio-Webhook-Pattern, ~4-5 PT, Q4-2026, → followup 60d)
[ ] 🟡 **DWD-Wetter-API-Auto-Erfassung fuer Rapport-weather/temperature** (~2 PT, Q4-2026 Nice-to-have, → followup 30d)
[ ] 🟡 **Multi-Stage-Freigabe-Workflow fuer rapporte** (State-Machine-Erweiterung, ~4-5 PT, Q1-2027, → followup 60d)
[ ] 🔵 **native iOS/Android-App via Capacitor-Wrapper** (langfristig, ~15-20 PT, Q2-2027)
[ ] 🔵 **Bautagebuch-Chronologie mit Foto-Zeitlinie** (123erfasst-Marktbenchmark-Parity, ~6-8 PT, Q1-2027)
[ ] 🔵 **Datanorm/IDS-Connect Handwerk-Material-Katalog** (HERO-Software-Marktbenchmark-Parity, ~10-15 PT, Q2-2027)
[ ] 🔵 **Terminal-Integration fuer Empfangs-Buero-Zeit-Erfassung** (TimeTac-Marktbenchmark-Parity, ~8-10 PT, Q2-2027)
[ ] 🔵 **rapporte-Test-Coverage von 33.9% auf 45%+** (Sprint-Hygiene, ~3-4 PT, laufend)
[ ] 🔵 **TenantInboundUnaryInterceptor fuer rapporte-Binary** (R3-P0-3-Offen-Fix, ~1 PT, low-prio)
