---
year: 2026
week: 43
modul: rapporte
created: 2026-10-19
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 54
tokens_input: ~372000
tokens_output: ~27500
rotation_position: 9/15
zyklus: 2
delta_to: monthly/2026-07-06-deepdive-rapporte.md
---

# Deepdive: rapporte (Mo W43/2026, Zyklus 2)

> **Vierter Zyklus-2-Deepdive mit vollstaendiger W28-Delta-Rechnung.** Vorgaenger-Zyklus 2: `crm-core` (W35), `dialer` (W36), `video` (W37), `wiki` (W38), `helpdesk` (W39), `formulare` (W40), `vertraege` (W41), `buchhaltung` (W42). **Zyklus 1-Vorgaenger fuer rapporte: W28/2026-07-06** — dieser Report rechnet strikt gegen die W28-Picks ab (3 🟢 + 10 🟡/🔵) und faehrt die W29-Schichten-Nachbarschaft nicht nach (W44 ist `schichten` an der Reihe, Modul-Rotation `settings.yaml` `intel-monday-deepdive.rotation_modules`). **Zweiter Rapporte-Deepdive insgesamt**, erster strukturierter Delta-Vergleich mit messbarem Code-Volumen-Shift.

> **Stand Cosmi-rapporte (2026-10-19) vs. W28 (2026-07-06):** Backend `backend/internal/rapporte/` ist in 15 Wochen **von ~2998 LOC auf 4371 LOC gewachsen (+46%)** — nicht durch Feature-Breite, sondern durch (i) **neue `pdf.go` mit maroto/v2** (156 LOC, Commit `7a01590f` 2026-08-02, "feat(rapporte): render real PDF for work report export"), (ii) **tenant_write_test.go** (125 LOC, Commit `a133ebd2` 2026-07-28), (iii) **own_scope_list_test.go** (93 LOC), (iv) **postgres_repository_test.go** komplett neu (898 LOC, Commit `f33da131` 2026-08-11 "cover postgres_repository update/delete/get/list and atomic transitions"). `service.go` 636→646 LOC (nur +10), `postgres_repository.go` 938→952 LOC (+14), `models.go` unveraendert 140 LOC. **8→12 Backend-Files, Test-LOC 1195→2317 (+94%)**, Prod-LOC 1803→2054 (+14%) — klarer **Test-Investment-Sprint**, kein Feature-Sprint. Frontend: `RapportePage.tsx` **1869→1641 LOC (−228, −12%)** (W28-Anti-Pattern "Mono-File waechst statt Refactor" **gebrochen**), **neue `ReportDetailModal.tsx` 500 LOC** (Commit `23c39644` 2026-07-15 "demo-depth - real pdf export, detail modal, settings"), `SketchCanvas.tsx` 732 LOC unveraendert, `SignatureCanvas.tsx` 3 LOC **ist jetzt ein 3-Zeilen-Re-Export** auf `@/components/signature/SignatureCanvas` (215 LOC, geteilt mit vertraege/vermietung) — **W28-P0-#2a geliefert**, nicht als Stub-Fix sondern als Shared-Component mit nativer Canvas-API (DPR-Scaling, Touch+Mouse, Clear-Button, Base64-PNG-Serialisierung, i18n-Keys `rapporte.signature.*`). **IndexedDB-Offline-Queue** als `desktop/src/renderer/src/api/offline-queue.ts` (**247 LOC NEU**) mit Idempotency-Key-Header-Auto-Gen, Exponential-Backoff 1s→16s mit MAX_RETRIES=5, Dead-Letter-Store, Batched-Parallel-Replay MAX_PARALLEL=5 — **W28-P0-#2b strukturell geliefert**, aber **ohne PWA-Service-Worker-Manifest** (W28-P0-#2c nicht geliefert, auch kein `handshoe-mode`-CSS). **Parallel-Modul `zeiterfassung`-Frontend** 1000→978 LOC (praktisch unveraendert), aber **HR-Backend hat 10 Zyklus-2-Deliveries** die W28-Konsolidierungs-Diskussion verschieben: Migration **000248 work_time_superseded_status** (2026-08-ish, "stop approved time corrections from counting twice" aus Commit `b871bbba` 2026-07-26), Commit **`7d612aa3` 2026-07-26 "enforce week approval locks and add the reopen transition"** (Multi-Stage-Freigabe-adjacent auf HR-Seite), Commit **`5f442703` 2026-08-22 "prevent double invoice creation from the same time entries"** (**Rapport→Rechnung-Bridge findet via `hr_work_time_entries` statt, nicht via `rapporte`**), Commit **`23ceede6` 2026-08-03 feat(hr): employee offboarding**, Commits **`9f2045c9`/`d78f9176` 2026-07-27** (tenant-isolation-refactor fuer hr_work_time_entries + break-entries), Commits **`121ea866` 2026-08-08** (week-approval repo + state machine gap coverage), **`6ea944c3`/`28a5d652`/`1e6691f1` 2026-08-26** (manual-entry-idempotency + HR-Approval-Balances + Analytics-Gateway-Coverage). **Migrations zwischen W28 und W43** fuer rapporte-Scope: keine (die naechste rapporte-direkte Migration ist 000164 aus W24-Welle, W28-Baseline). HR-Scope: **000248 superseded status** (einziger harter Impact). Fuer Umgebungs-Reports: Migration **000245 report_documents** + **000252 report_share_tokens** sind **`berichte`-Modul (Dashboard-Reports mit TipTap-Bloecken), NICHT `rapporte`-Modul** — Namenskollision, nicht Delivery. **Bekannte Schulden Zyklus-2-Stand**: (i) **AI-Auto-Kategorisierung null geliefert** (W28-P1 #3a) — kein `backend/internal/rapporte/ai_categorization/`-Pfad, kein Mistral-Adapter, kein `ai_categorization_corrections`-Table trotz 15 Wochen Fenster; (ii) **Voice-Input null geliefert** (W28-P1 #3b) — kein `useSpeechRecognition`-Hook, kein `SpeechRecognition`-Call anywhere in Repo; (iii) **GPS-Consent-Flow null geliefert** (W28-🟡 Pick) — keine `GPSConsentBanner`-Komponente, keine `report_gps_consent_events`-Migration, `validateGPS` prueft weiter nur Bounds, kein tenant-Opt-out, kein Audit-Log; (iv) **DWD-Wetter-API null geliefert** (W28-🟡 Pick) — Zero Matches auf `DWD|wetter.*api` im Backend, `weather`/`temperature` bleiben manuell; (v) **Multi-Stage-Freigabe fuer `rapporte` null geliefert** (W28-🟡 Pick) — State-Machine linear Draft→Submitted→Approved/Rejected unveraendert, einziger `reviewer_id`-Field, aber `hr_week_approvals` hat **reopen-Transition** bekommen am 2026-07-26 (asymmetrische Entwicklung HR vs. rapporte); (vi) **DATEV-Realtime-Sync fuer hr_work_time_entries null geliefert** (W28-🟡 Pick); (vii) **native iOS/Android null**, **Bautagebuch-Chronologie null**, **Datanorm/IDS-Connect null**, **Terminal-Integration null** — alle 🔵 Picks unangetastet; (viii) **ADR-0009 "rapporte+zeiterfassung Domain-Konsolidierung" nicht geschrieben** (W28-P0 #1) — Modul-Katalog `backend/internal/modules/catalog.go:64` listet weiter `rapporte` als eigenes Modul mit `modules.rapporte`-Flag, Feature-Flag `modules.zeiterfassung` existiert gar nicht (zeiterfassung ist Teil des HR-Pakets), aber `5f442703 "prevent double invoice creation from the same time entries"` **implementiert faktisch die W28-Option-B-Bridge-Richtung via Invoice-Linking**, nicht via Event-Emitter aus `rapporte.SubmitReport`.

> **Vier strukturelle Beobachtungen, die den Sprint-Plan W43 kalibrieren.** **#1 Das Delivery-Muster "Backend-Hygiene + Frontend-Refactor-RICHTIG, strategische Luecken null" aus Zyklus-2-W39/W40/W41/W42 bestaetigt sich fuer rapporte ein fuenftes Mal in Folge — mit einer kritischen Nuance.** Nach helpdesk-W39 (5/10 W24-Picks delivered, aber P0-AI-Compliance-Foundation null), formulare-W40 (3.5/7 W25-Picks delivered 50%, aber P0-AI-Foundation + MCP null), vertraege-W41 (3.5/12 W26-Picks delivered 29%, P0-Skribble + Multi-Signer + AI null), buchhaltung-W42 (0.6/3 W27-Green-Picks delivered 20%, aber 7 Grossdeliveries NICHT prognostiziert) liefert rapporte-W43 jetzt: **2/4 W28-P0-Picks delivered (50%)** — Baustellen-Offline-Mode `desktop/src/renderer/src/api/offline-queue.ts` (247 LOC, Idempotency-Key + Dead-Letter + Exponential-Backoff als Marktbenchmark-fester Code, siehe `offline-queue.ts:11-61` fuer Replay-Pfad) und SignatureCanvas-Ausbau als Shared-Component `desktop/src/renderer/src/components/signature/SignatureCanvas.tsx` (215 LOC, native Canvas + Touch-Events, nicht `react-signature-canvas` wie W28-empfohlen — aber funktional aequivalent + ohne npm-Dependency); **0/3 W28-P1-Picks delivered (0%)** — AI-Auto-Kategorisierung + Voice-Input + ADR-0009 null; **4 nicht-prognostizierte Bonus-Deliveries**: (a) real-PDF-Export via maroto/v2 (`pdf.go` 156 LOC — W28 behauptete "ExportPDF-RPC existiert", in Wahrheit war's ein Stub bis 2026-08-02), (b) ReportDetailModal-Extraction aus RapportePage (500 LOC neu, −228 LOC in RapportePage — struktureller Refactor), (c) tenant_write_test.go + own_scope_list_test.go + postgres_repository_test.go-Komplett-Neufassung (+1116 Test-LOC), (d) RBAC-R-3-Batch-4-Enforcement fuer rapporte (`2055c475` 2026-07-19 "scope-own for edit/delete") plus `cefb5419` "require review_note on RejectReport" + `9db416e3` "reject measurement positions for foreign measurements" + `152fa892` "default empty template lines to [] instead of NULL" (vier atomare Hardenings statt grosser Features). **Die kritische Nuance**: Zyklus-2-W43 ist das **erste Modul mit vollstaendigem P0-Pflicht-Lift** (Baustellen-Offline + SignatureCanvas-Produktion) — Backend-Hygiene UND Frontend-Refactor UND Test-Investment UND einer der zwei P0-Markt-Luecken-Deliveries alles in einem Zyklus. Verglichen mit buchhaltung-W42 (riesiges Backend-Volumen, aber PEPPOL + AI-OCR + Bank-Feed-Live null), vertraege-W41 (Skribble null trotz 15 Wochen), formulare-W40 (Anti-Spam-Trias null), helpdesk-W39 (AI-Drafts null) — **rapporte ist 2026-Q3-Q4 das Modul mit dem besten W28→W43-Delivery-Score auf P0-Pflicht-Picks**. Das aendert die Zyklus-3-Pick-Logik: statt neue grosse Picks ist der 2 noch offene W28-Hebel (AI-Auto-Kategorisierung) jetzt die **Fokus-Luecke**, nicht ein Nach-Deepdive-Priorisierungs-Thema. **#2 Die rapporte↔zeiterfassung-Domain-Splittung ist in 15 Wochen *schlimmer* geworden, nicht besser — HR-Seite hat 10 Deliveries bekommen, rapporte-Seite 11, und beide Seiten haben *orthogonal* geliefert, nicht konvergent.** HR-Deliveries 2026-07-26 bis 2026-08-26: **Week-Approval-Locks + Reopen-Transition** (`7d612aa3` 2026-07-26 "enforce week approval locks and add the reopen transition" — das ist die Multi-Stage-adjacent-Erweiterung die W28 fuer `rapporte` empfohlen hat, nur auf der falschen Modul-Seite geliefert), **Superseded-Status** (`b871bbba` 2026-07-26 + Migration 000248 — hr_work_time_entries bekommt 5. State fuer Correction-Replace, das ist korrektheits-kritisch), **Tenant-Hardening** (`9f2045c9`+`d78f9176` 2026-07-27 — scope every work_time query + break entries), **Employee-Offboarding** (`23ceede6` 2026-08-03 — HR-Lifecycle), **Double-Invoice-Prevention** (`5f442703` 2026-08-22 — faktische Rapport→Rechnung-Bridge via time-entries), **Manual-Entry-Idempotency-Dedup** (`6ea944c3` 2026-08-26 — Gateway-Chain-Hardening). rapporte-Deliveries parallel: PDF, Detail-Modal, Scope-Own-RBAC, Review-Note-Pflicht, Measurement-Tenant-Fix, Template-Lines-Default. **Die beiden Modul-Zustaende**: HR-side hat State-Machine evolviert (von 4 States auf 5 States, mit Lock/Reopen-Edges), rapporte-side hat State-Machine *nicht* evolviert (bleibt 4 States ohne Lock/Reopen). HR-side hat jetzt Idempotency-Dedup, rapporte-side setzt auf Offline-Queue-Idempotency-Keys (anderer Mechanismus). HR-side hat `superseded`-Audit-Trail fuer Corrections, rapporte-side hat keine Correction-Semantik ueberhaupt. **Das ist jetzt ein Produkt-Risiko**: Cosmi-Handwerk-Kunde erfasst Baustellen-Rapporte mit `work_start`/`work_end`/`break_minutes`, aber die Wochen-Aggregation fuer §16 ArbZG-Reform-Readiness laeuft gegen `hr_work_time_entries` (Lock/Reopen/Supersede), nicht gegen `work_reports` — zwei Datenwelten mit zwei State-Machinen und *keiner* Bridge. **W28-P0 #1 ADR-0009 nicht geschrieben = 15-Wochen-Opportunitaet verpasst**: die Zeit zwischen den beiden Modulen die Bridge zu schlagen, haette genau in diesen 15 Wochen stattfinden muessen, weil beide Seiten Delivery-Momentum hatten. W43-Pflicht: **ADR-0009 schreiben MIT Entscheidung Option-B-Hybrid, Event-Emitter aus `rapporte.SubmitReport` → `hr_work_time_entries.CreateFromRapport`-RPC implementieren, Wochen-Aggregation gemeinsam-sichtbar machen** — 3-4 PT-Schaetzung aus W28 bleibt gueltig, aber jetzt mit konkretem Trigger (**§16 ArbZG-Referentenentwurf 18.06.2026 bleibt in Verbaendeanhoerung, Inkrafttreten 2027-Q1 noch moeglich, Uebergangsfrist 5 Jahre fuer <50MA = 2029-Compliance-Horizont** — Sales-Story-Compliance-Dringlichkeit sinkt, aber ADR-Konsolidierung bleibt sprint-oekonomisch zwingend). **#3 Der AI-Markt-Druck im DACH-Zeiterfassungs-Segment hat sich in 15 Wochen signifikant veraendert — Cosmis W28-"offenes Fenster"-These ist nicht mehr frei, aber auch nicht geschlossen.** W28-Behauptung: TimeTac/ZEP/Crewmeister/Papershift/123erfasst/Clockify/Toggl haben KEIN Live-AI-Feature, nur Timely (Enterprise) + HERO Software (69 EUR Premium) adressieren. **W43-Delta**: (a) **ZEP Release 8.0 September 2026 mit "ZEP Assistant"** — In-App-GenAI fuer Buchung/Antrag/Belege via Natural Language, Confirmation-Card-Pattern + Audit-Log fuer AI-Aktionen (`zep.de/en/roadmap`). **Erster deutscher PSA-Player mit GenAI-Produkt-Launch**, scoped auf Buchungs-UX (nicht auf Rapport-Erzeugung) — Cosmi-rapporte direkt nicht konkurriert, Cosmi-zeiterfassung-Konsulting-Overlap-Zone aber betroffen. (b) **clockin.de** hat seit 2026 "AI-Video-Dokumentation" und "AI-Gespraechsnotizen" als Baustellen-Dokumentations-Features (`trusted.de/clockin`), AI-Telefon-Assistent angekuendigt — **das ist clockins Bewegung in Cosmis AI-Rapport-Zone** (Video + Voice als Baustellen-Doku), mit Preis-Positionierung Basic 3.19 EUR / Projekt 6-7 EUR / Full-Suite 8-10 EUR — **direkt im Cosmi-3-EUR-Preis-Cluster**. clockin ist 2026-Q4 der konkreteste neue Konkurrenz-Signal. (c) **noovi (CH)** positioniert sich 2026 explizit als **"AI-Sprachaufnahme → strukturierter deutscher Rapport"** (`noovi.ch/funktionen/rapporte`), Offline-faehig, Werkzeug-/Lager-Modul, Bautagebuch — Pro-Paket CHF ~195/5 User, Einstieg CHF 19/User. **Das ist der direkteste Cosmi-rapporte-CH-Konkurrent** und validiert die W28-Voice-Rapport-Hypothese *kompetitiv* (nicht mehr nur HERO-Vaporware-Schatten, sondern lebendes CH-Produkt). (d) **HERO Report** (Bautagebuch-Voice, W28-Benchmark-Zitat) ist in 15 Wochen **weiterhin Vaporware** — `hero-software.de/features` listet nur HERO Voice als live, HERO Report + HERO Command bleiben "folgt in Kuerze". Fenster fuer Cosmi Voice-Rapport bleibt offen bis mindestens Q1/2027. (e) **Toggl Track** hat Beta "Toggl AI" Chat-Panel + MCP-Server fuer AI-Assistenten (`checkthat.ai/brands/toggl/pricing`) — **MCP-Server-Signal: Zeiterfassungs-Vendor machen Daten fuer AI-Agenten adressierbar**, Cosmi-MCP-Server (W33-Keeper 10 Wochen ueberfaellig, in buchhaltung-W42-Pflicht-Empfehlung erneut gelistet) bekommt neue Rechtfertigungs-Dringlichkeit. (f) **Clockify** hat Freemium-Entluftung April 2026 (Free-Tier auf 5 User gekappt, zuvor unbegrenzt; AI-Forecasting + Kiosk-Photo-Capture in Pro-Tarif gezogen) — der Clockify-Freemium-Churn-Pipeline begunstigt bezahlte Mitbewerber in KMU-Konvertierung, inkl. Cosmi. (g) **Timely/Memory.ai Oslo** rebrandete im April 2026 zurueck auf "Timely" (`timely.com/company-news/2026-04-15`); **die oft gesehene "Upstage acquires Timely Juni 2026"-Headline betrifft eine koreanische AI-Agenten-Firma, NICHT das Oslo-Zeiterfassungs-Produkt**. Keine M&A fuer AI-Zeiterfassungs-Marktfuehrer. (h) **TimeTac + Crewmeister + Papershift + 123erfasst**: alle vier zeigen **keine materiellen 2026-H2-Produkt- oder Pricing-News** — Markt-Snapshot stabil fuer vier der sechs W28-Haupt-Benchmarks. **Kombinierte Konsequenz fuer Cosmi**: das Fenster "DACH-KMU-AI-differenzierter-Zeiterfassungs-Player unter 10 EUR/User-Monat" ist **nicht geschlossen** (HERO Report Vaporware, ZEP-Assistant nicht Rapport-fokussiert, Timely-Enterprise-Pricing), **aber enger** (clockin AI-Video + AI-Gespraechsnotizen im 3-EUR-Preis-Cluster, noovi AI-Voice-Rapport in CH-Markt). W43-Pflicht: **AI-Rapport-Auto-Kategorisierung Sprint-Start jetzt**, nicht Q4-2026-Plan — 15 Wochen Verzug ist Cosmi-Standard, 20 Wochen Verzug mit clockin+noovi im gleichen Preis-Cluster wird Cosmi-strategisch teuer. **#4 Die Regulatorik-Fakten-Lage hat sich seit W28 drei-mal verschoben, und zwei davon reduzieren Cosmis Marketing-Argumente, waehrend eine das Produkt-Risiko unmittelbar erhoeht.** (a) **§16 ArbZG-Reform**: Referentenentwurf 18.06.2026 ist seit W28 **weiter in Verbaendeanhoerung**, kein Kabinettsbeschluss im Delta-Zeitraum, Inkrafttreten 2027-Q1 noch moeglich, aber Uebergangsfristen gestaffelt (2 Jahre <250MA, **5 Jahre <50MA = Cosmi-Ziel-KMU-Compliance-Deadline realistisch 2029-2032**) — W28-Marketing-Pitch "jetzt kaufen wegen Pflicht" wird schwaecher, **Cosmi-Narrative muss von Compliance-Angst auf Rapport-Produktivitaet umschwenken**. (b) **CSRD-Omnibus-I-Richtlinie** EU 2026/470 in Kraft Maerz 2026 — CSRD-Scope um ~90% reduziert, nur noch Unternehmen >1000 MA UND >450M EUR Umsatz berichtspflichtig, boersennotierte KMU raus, CSDDD nur noch >5000 MA + >1.5 Mrd EUR Umsatz (`industrieblatt.de/csrd-omnibus-berichtspflicht-aenderungen-2026`). **Konsequenz fuer Cosmi**: "ESG-Zeiterfassung" als KMU-Up-Sell-Hebel ist **effektiv erloschen**, Mitarbeiter-ESG-Reporting-Features fuer KMU-Segment nicht mehr sales-tragfaehig. (c) **EU AI Act Article 50**: Grace-Period fuer maschinenlesbare Markierung von AI-Content laeuft **02.12.2026 aus** (Legacy-Systeme vor 02.08.2026 placed-on-market, danach alle Art.-50-Pflichten enforceable). Fuer Cosmi: **wenn AI-Rapport-Auto-Kategorisierung + Voice-Input nach 02.12.2026 live gehen, zaehlt AI-generierter Rapport-Text als "synthetic text" → maschinenlesbare Markierung Pflicht** (C2PA Content Credentials als empfohlener Standard). Zusaetzlich Chatbot-Disclosure wenn User mit AI "spricht" (CSA-Research-Note Art. 50 Watermarking + Paul-Weiss-Transparency-Rules). Cosmi-W28-Backlog muss **C2PA-Marker + "AI-generated"-Flag im Rapport-Modell** ergaenzen — **44 Tage bis Deadline**. (d) **EU AI Act Annex III HR-High-Risk**: Digital Omnibus on AI (in Kraft 27.07.2026) hat Compliance-Deadline fuer standalone High-Risk-Systeme von 02.08.2026 auf **02.12.2027 verschoben** (knowlee.ai + teamazing.com AI-Act-Analysen). HR-Worker-Evaluation / Task-Allocation bleibt Annex-III. **Konsequenz fuer Cosmi**: Entspannung bis Ende 2027, **aber jede AI-Feature die Performance scored, Produktivitaet rankt, Task-Allocation vorschlaegt (Cosmi AI-Rapport-Analytics betroffen) braucht spaetestens 02.12.2027 High-Risk-Compliance**. Produkt-Architektur-Guard-Rail: **"nur Erfassung, kein Ranking"** als AI-Act-Pfad oder High-Risk-Compliance einplanen. (e) **GPS/DSGVO-Rechtsprechung**: BAG-Urteil **8 AZR 209/21 vom 08.05.2025** wirkt nach — § 26 Abs. 1 BDSG allein reicht NICHT als Rechtsgrundlage fuer GPS-Tracking, Betriebsvereinbarung ODER Art. 6 DSGVO notwendig (`activemind.legal/de/guides/urteil-gps-daten`). **2026 haben deutsche Landesdatenschutzbehoerden GPS-Ortung Beschaeftigter als Pruefschwerpunkt definiert**, Beschwerden und Bussgelder steigen (`geotapp.com/blog/de/2026/06/15`). Konsequenz: **Cosmi-W28-Pick "GPS-Consent-Flow + Audit-Log" bleibt 🟡-Pflicht, 15 Wochen null geliefert = Produkt-Risiko fuer Cosmi-Kunden mit Betriebsrat** — DSGVO-Pruefschwerpunkt macht `GPSConsentBanner` + `report_gps_consent_events`-Tabelle jetzt sales-notwendig (nicht nur compliance-ready). (f) **MiLoG §17**: Mindestlohn 2026 = 13.90 EUR/h, §17 technisch angepasst (Art. 8 Abs. 3 G. v. 12.05.2026, BGBl. 2026 I Nr. 137), keine strukturelle Verschaerfung der Doku-Pflicht, Bussgeld bis 30.000 EUR unveraendert — Cosmi-Marketing-Punkt bleibt gleich. (g) **CH ArG Art. 46**: Keine Reformen im Delta auffindbar — CH-Markt stabil, kein Compliance-Katalysator. **Zusammengefasste W43-Regulatorik-Konsequenz**: ArbZG-Reform-Dringlichkeit sinkt (realistisch 2029-Horizont fuer <50MA), ESG-Up-Sell-Hebel erloschen, AI-Act-Art.50-Watermarking in 44 Tagen Pflicht, AI-Act-Annex-III-HR-High-Risk auf 2027-Q4 verschoben, GPS-DSGVO-Pruefschwerpunkt verstaerkt — **drei Produkt-Code-Konsequenzen**: (i) ADR-0009 beschleunigen (schwaecherer ArbZG-Druck heisst nicht weniger-Konsolidierung, nur weniger-Dringlichkeit, aber Produkt-Risiko aus HR↔rapporte-Divergenz ist jetzt groesser), (ii) C2PA-Watermark-Flag ins AI-Feature-Sprint eintakten (02.12.2026-Hard-Deadline), (iii) GPSConsentBanner + Audit-Log liefern (W28-🟡 wird de-facto-🟢).

> **Leit-Signal der Woche fuer rapporte: drei Zyklus-2-Beobachtungen aus den vier Vorgaenger-Deepdives bestaetigen sich bei rapporte, mit einer markanten Ausnahme beim Delivery-Score.** Zyklus-2-Pattern (helpdesk-W39/formulare-W40/vertraege-W41/buchhaltung-W42) sagte: **Backend-Hygiene + Idempotenz + Race-Fix + Test-Coverage schnell geliefert; strategische Markt-Luecken AI + MCP + Integrations-Partner null bis minimal; Frontend-Refactor-W24/W25-Empfehlungen rueckwaerts-geliefert (RapportePage, FormularePage, VertraegePage, Mono-File-waechst-statt-Refactor)**. Rapporte-W43 bestaetigt das Pattern mit **einer kritischen Ausnahme**: der Frontend-Refactor-W28-Empfehlung ist diesmal **vorwaerts-geliefert** — RapportePage ist 1869→1641 LOC (−228 LOC, −12%), die 500 LOC ReportDetailModal.tsx-Extraktion ist das erste Zyklus-2-Modul mit *abnehmendem* Mono-File-LOC-Zaehler. Verglichen mit formulare-W40 (FormularePage 2457→5605 LOC +128%), vertraege-W41 (VertraegePage 2417→2565 LOC +6%), helpdesk-W39 (Frontend 2043→3197 LOC +57%), buchhaltung-W42 (Prod-LOC +78%) ist **rapporte-W43 das erste Zyklus-2-Modul mit nachhaltigem Frontend-Refactor**. Backend-Volumen-Explosion-Pattern bleibt sichtbar aber kleiner (+46% Backend, +94% Test-LOC) — rapporte ist nicht das groesste Backend-Delivery-Modul (das bleibt buchhaltung-W42 mit +78% Prod-LOC), aber das disziplinierteste Modul im Test-Investment-pro-Prod-LOC. AI-Compliance-Foundation-Null-Delivery bestaetigt sich zum 5. Mal in Folge (W39→W43) — rapporte liefert **wie formulare + vertraege + buchhaltung** null AI-Code, obwohl AI-Compliance-Foundation seit W39 als P0 markiert ist und EU AI Act Art.50-Grace-Period in 44 Tagen auslaeuft. **Dieser Bericht empfiehlt drei Pflicht-Empfehlungen fuer die W43-W45-Zyklus-3-Vorbereitung** (statt breitem 15-Picks-Katalog): **(1) ADR-0009 Domain-Konsolidierung JETZT schreiben + Option-B-Hybrid-Bridge (`rapporte.SubmitReport` → `hr_work_time_entries.CreateFromRapport`-Event-Emitter) implementieren, 3-4 PT** — HR-Seite hat 10 Zyklus-2-Deliveries, rapporte-Seite hat 11, Bridge-Luecke ist Produkt-Risiko. **(2) AI-Rapport-Auto-Kategorisierung + C2PA-Watermark-Marker als 1-Sprint-Paket, 6-8 PT, Deadline 2026-12-02 fuer Art.50-Compliance** — Mistral-Adapter-Reuse aus buchhaltung-W27-W42-AI-OCR-Sprint-Plan (der auch null geliefert ist), AI-generated-Flag im `work_report`-Modell, 15-Wochen-Fenster-Verzug jetzt im clockin+noovi-Preis-Cluster. **(3) GPSConsentBanner + `report_gps_consent_events`-Tabelle + Audit-Log als 2-PT-Compliance-Sprint, Deadline 2027-Q1-Betriebsrats-Verhandlungs-Season** — DSGVO-Pruefschwerpunkt-Signal 2026 macht W28-🟡-Pick de-facto-🟢-Pflicht, Produkt-Risiko fuer Cosmi-Kunden mit Betriebsrat jetzt sales-blocker.

---

## State-of-the-Art

Der DACH-Zeiterfassungs- und Field-Rapport-Markt Mitte-2026 bis Herbst-2026 ist **vierspurig unveraendert** gegenueber W28, aber in zwei Spuren mit neuen AI-Launches und einer regulatorischen Nachlassbewegung. Die Spur-Zuordnung aus W28:

**(1) Handwerk-Baustellen-Feld-Rapport-Spezialisten**: 123erfasst (DE Bau-Marktfuehrer), HERO Software (DE Handwerker-ERP), mobiel (DACH Niche), **noovi (CH, 2026 neu-positioniert mit "AI-Sprachaufnahme → strukturierter deutscher Rapport")**, clockin (DE, **seit 2026 "AI-Video-Dokumentation" + "AI-Gespraechsnotizen"**). **Spur-1-Delta**: noovi und clockin bewegen sich 2026-H2 explizit in AI-Rapport-Zone, 123erfasst/HERO bleiben Vaporware-fuer-AI (HERO Report "folgt in Kuerze" bleibt).

**(2) HR-Zeiterfassungs-Klassiker (DACH)**: TimeTac, **ZEP (September 2026 Release 8.0 mit "ZEP Assistant")**, Crewmeister, Papershift. **Spur-2-Delta**: ZEP ist erster DACH-PSA-Player mit GenAI-Produkt-Launch — scoped auf Buchungs-UX, nicht auf Rapport-Erzeugung, aber Markt-Signal fuer AI-Erwartungshaltung im Zeiterfassungs-Mainstream.

**(3) International-Freelancer-Time-Tracker**: Toggl Track (**MCP-Server + Toggl-AI-Chat-Panel-Beta**), Harvest (**Pricing-Hike auf $9/Seat teams + $14/Enterprise jaehrlich**, two-layer Billing), **Clockify (April 2026 Free-Tier auf 5 User gekappt, AI-Forecasting + Kiosk-Photo-Capture in Pro-Tarif)**, Timely (Oslo, keine M&A, DACH-Fokus-Vermarktung unveraendert aktiv).

**(4) Consulting-PSA / IT-Service-KMU-Time-Tracker**: ZEP Compact/Professional (mit neuem AI-Assistant), Kimai (Open-Source v2.69.0 ohne AI), TimeChimp (NL, Pricing stabil 9-13 EUR + Base, AI-Timesheet-Suggestions). **Spur-4-Delta**: TimeChimp-Pricing stabil, Kimai weiter AI-leer.

Cosmi-rapporte sitzt weiter architektonisch in Spur (1), Cosmi-`zeiterfassung`/HR-Modul in Spur (2) + (4). Der Modul-Preis bleibt **3 EUR/User-Monat pro Modul** (rapporte + zeiterfassung-als-Teil-von-HR). Preis-Vorteil gegen clockin Basic (3.19 EUR) jetzt enger, aber Full-Suite-Vergleich noch Cosmi-Vorteil (6 EUR Rapport+Zeit vs. clockin 8-10 EUR Full-Suite, 123erfasst 30-50, HERO 69-345, TimeTac Essential 3+19.50 Basis).

**Drei strukturelle Veraenderungen seit W28** (statt vier W28-Veraenderungen):

(a) **§16 ArbZG-Reform-Status Oktober 2026 — Verbaendeanhoerung weiter aktiv, Kabinettsbeschluss ausstehend**. Referentenentwurf 18.06.2026 (BMAS, Bas) weiter in Verbaendeanhoerung Stand 2026-10-19 (`clockin.de/blog/reform-des-arbeitszeitgesetzes`, `factorialhr.de/blog/arbeitszeitgesetz-reform`, `energieundrecht.com`). Kein Kabinettsbeschluss im Delta-Zeitraum W28→W43 (15 Wochen). Inkrafttreten-Ziel: 2027-Q1, aber mit Uebergangsfristen **2 Jahre fuer <250 MA, 5 Jahre fuer <50 MA** (Cosmi-Ziel-KMU). Realistische Compliance-Deadline fuer Cosmi-Kunden mit <50 MA: **2029-Q1 bis 2032-Q1**. **W43-Marketing-Konsequenz**: W28-Pitch "Cosmi-Zeiterfassung ist ArbZG-2026-Reform-ready" bleibt sachlich korrekt, aber Verkaufs-Dringlichkeit "jetzt kaufen weil Pflicht" ist dreifach entlastet (keine Verabschiedung + 5-Jahres-Uebergang + Entwurf-Diskussion offen). **Cosmi-Narrative muss W43+ von Compliance-Angst auf Rapport-Produktivitaet umschwenken** — "Baustellen-Dokumentation ohne Dachpappe-Zettel-Chaos" ist der neue USP-Anker, nicht "Pflicht erfuellen". **Delivery-Konsequenz**: `hr_work_time_entries` + `hr_week_approvals`-Fundament bleibt ArbZG-Reform-ready (W28-Baseline-Validitaet unveraendert), die am 2026-07-26 nachgezogene `hr_week_approvals.reopen`-Transition (Commit `7d612aa3`) + superseded-State (Migration 000248) *verstaerken* ArbZG-Readiness auf HR-Seite — aber nicht auf rapporte-Seite (dort State-Machine linear ohne Reopen). ADR-0009-Luecke bleibt bestehen.

(b) **GPS/DSGVO-Verschaerfung durch Landesdatenschutzbehoerden-Pruefschwerpunkt 2026 + BAG 8 AZR 209/21 Nachwirkung**. Zwei Delta-Fakten gegenueber W28: (i) **BAG-Urteil 8 AZR 209/21 vom 08.05.2025**: § 26 Abs. 1 BDSG alleine reicht NICHT als Rechtsgrundlage fuer GPS-Tracking von Beschaeftigten, Betriebsvereinbarung ODER explizite Art.-6-DSGVO-Rechtsgrundlage notwendig (`activemind.legal/de/guides/urteil-gps-daten`, `energieundrecht.com/blog-arbeitsrecht-zivilrecht/gps-ueberwachung-mitarbeiter-firmenfahrzeuge-arbeitgeber-2026`). Das war in W28 unterrepraesentiert — W28 zitierte nur BDSG + DSB-AT-Nov-2025, nicht BAG-DE 05/2025. (ii) **2026 haben deutsche Landesdatenschutzbehoerden GPS-Ortung Beschaeftigter als Pruefschwerpunkt definiert**, Beschwerden und Bussgelder steigen (`geotapp.com/blog/de/2026/06/15/gps-ortung-mitarbeiter-dsgvo-regeln-2026`). **W43-Konsequenz fuer Cosmi**: W28-🟡-Pick "GPS-Consent-Flow + Audit-Log" ist 15 Wochen null geliefert, aber die Compliance-Rechtfertigung ist seit 2026-H1 verstaerkt — Betriebsrats-Mitbestimmungs-Workflow nach §87 Abs. 1 Nr. 6 BetrVG ist zwingend, Cosmi-Produkt-UI muss transparente Dokumentation welche Position wann erfasst wird liefern, `report_gps_consent_events`-Tabelle mit event_type (rapport_create/clock_in/clock_out) + consent_at + consent_source (tenant_setting/user_toggle) ist DSGVO-Beweislast-fest. **Delivery-Konsequenz**: W28-🟡 wird W43-de-facto-🟢-Pflicht, 2-PT-Sprint.

(c) **AI-Act Article 50 Grace-Period-Ende 2026-12-02 + Annex-III-High-Risk-HR-Verschiebung auf 2027-12-02**. (i) **Art. 50**: Grace-Period fuer **maschinenlesbare Markierung** von AI-Content laeuft **02.12.2026** aus — fuer Legacy-Systeme (vor 02.08.2026 placed-on-market); alle anderen Art.-50-Pflichten (Chatbot-Disclosure, Deepfake-Label, Emotion-Recognition-Notice) sind seit 02.08.2026 bereits enforceable (CSA Research Note Art. 50 Watermarking, Paul Weiss Transparency Rules, `praxikon.com/en/ai-act/artikel/50`). **44 Tage bis Deadline Stand 2026-10-19**. Fuer Cosmi: wenn AI-Rapport-Auto-Kategorisierung + Voice-Input nach 02.12.2026 live gehen, zaehlt AI-generierter Rapport-Text als "synthetic text" → maschinenlesbare Markierung Pflicht (**C2PA Content Credentials** als empfohlener Standard, [c2pa.org](https://c2pa.org) fuer Tech-Dokumentation). Zusaetzlich Chatbot-Disclosure wenn User mit AI "spricht" (Voice-Input-Scenario). (ii) **Annex III**: Digital Omnibus on AI (in Kraft 27.07.2026) hat Compliance-Deadline fuer standalone High-Risk-Systeme von 02.08.2026 auf **02.12.2027 verschoben** (`knowlee.ai/blog/ai-act-annex-iii-hr-employment`, `teamazing.com/blog/ai-act-annex-iii-hr-high-risk`, `technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus`). HR-Worker-Evaluation / Task-Allocation / Performance-Scoring bleibt Annex-III-Kategorie. **W43-Konsequenz fuer Cosmi**: Entspannung bis Ende 2027, **aber Cosmi AI-Rapport-Analytics (wenn geliefert) betroffen**, Guard-Rail "nur Erfassung, kein Ranking" oder High-Risk-Compliance (Risk-Mgmt, Datenqualitaet, Human Oversight, Logging, Transparenz) planen. (iii) **CSRD-Omnibus**: EU 2026/470 Maerz 2026 — CSRD-Scope um 90% reduziert, "ESG-Zeiterfassung" als Cosmi-KMU-Up-Sell-Hebel ist erloschen. **Delivery-Konsequenz**: Zwei neue Code-Pflichten — `work_reports.ai_generated_fields` TEXT[]-Spalte + C2PA-Marker-Serialisierer fuer AI-generated-Rapport-Felder; `ai_disclosure`-Tabelle (schon in W39-helpdesk-W40-formulare-W41-vertraege-W42-buchhaltung-als-P0 markiert, immer noch null geliefert — jetzt mit Deadline 02.12.2026).

### Top-Konkurrenten — W28→W43-Delta und was Cosmi jetzt nicht hat

**1. 123erfasst (DE, threat: HIGH, Delta: UI-Redesign vollendet, keine neue AI-Welle)**

W28-Snapshot: Bau-Marktfuehrer Nevaris/bps software, UI-Redesign Fruehjahr 2026 kommuniziert, Offline-Mode Marktbenchmark, Pricing 30-50 EUR/User-Monat.

- **digitalBAU 2026 (24.-26. Maerz)**: Kalkulations-Modul fuer durchgaengige Angebots/Rechnungs-Prozesse praesentiert (`bvbs.de/2026/04/16/digitalbau-2026-nevaris-setzt-digitalisierungsimpulse`).
- **Offline-Mode + Bautagebuch**: unveraendert Kernfeatures (`bpz-online.de`).
- **Keine neuen 2026-H2-Pricing- oder AI-Produkt-Signale**.
- **Keine M&A-Aktivitaet Nevaris/123erfasst/bps** im Delta auffindbar.
- **Cosmi-W43-Delta-Konsequenz**: 123erfasst-Vorsprung bei Baustellen-Offline + nativer App bleibt, aber Cosmi hat durch `offline-queue.ts`-Delivery die groesste W28-Luecke geschlossen. Preis-Differential Cosmi 3 EUR vs. 123erfasst 30 EUR unveraendert = 10x Preis-Rabatt, aber Native-App + Handschuh-UI-Luecken bleiben. Sprint-Pflicht unveraendert aus W28: PWA-Manifest + Handschuh-Bedien-UI, native iOS/Android-App ueber Capacitor-Wrapper als mittelfristig.

**2. HERO Software (DE, threat: HIGH, Delta: Vaporware-Status fuer HERO Report + HERO Command bleibt, HERO Voice live)**

W28-Snapshot: HERO Voice GA 2026, HERO Report + HERO Command angekuendigt, 69-345 EUR/User-Monat Premium-Pricing.

- **HERO Voice (KI-Telefonassistent)**: live, bestaetigt ueber `hero-software.de/features`.
- **HERO Report (Bautagebuch-Voice)**: **weiter als "folgt in Kuerze" markiert, kein GA-Datum verifizierbar in 15 Wochen Delta** (`handwerksblatt.de/betriebsfuehrung/ki-soll-den-bueroalltag-im-handwerk-erleichtern`, `hero-software.de/ueber-uns/presse`).
- **HERO Command (KI-Angebots-Assistent)**: ebenfalls weiter Vaporware.
- **HERO Insights+-Studie "Handwerk digital" August 2026**: Marketing-Material statt Produkt-GA (`hero-software.de/ueber-uns/presse`).
- **Finanzmanagement-Integration Mai 2026** (`sbz-online.de`): produktseitig neu, aber nicht AI-fokussiert.
- **Keine neue Funding-Runde** seit Series B 07/2024 ($51.8M total) auffindbar (`tracxn.com/d/companies/hero`).
- **Cosmi-W43-Delta-Konsequenz**: **Zeitfenster fuer Cosmi Voice-Rapport bleibt offen bis mindestens Q1/2027** — HERO Report-Vaporware ist 15-Wochen-Lackmustest fuer HERO-AI-Produkt-Roadmap-Realitaet. Cosmi kann mit Voice-Input-Layer + AI-Auto-Kategorisierung in 6-8 Wochen *vor* HERO Report live sein, im 3-EUR-Preis-Cluster vs. HERO 69-EUR. Priorisierungs-Verschiebung von Q4-2026-Plan auf **W43-Sprint-Start Pflicht**.

**3. TimeTac (AT/DE, threat: HIGH, Delta: keine materiellen Produkt- oder Pricing-News)**

W28-Snapshot: AT/DE-HR-Zeiterfassungs-Marktfuehrer, DATEV-Lodas + Lohn&Gehalt bidirektional 2025-Refresh, keine Live-AI.

- **Capterra-Snapshot Januar 2026**: unveraendert — Basisgebuhr 19.50 EUR/Monat, Zeiterfassung 5.20 EUR/User, Projektzeit 9.00 EUR/User (`capterra.com/p/127555/TimeTac`).
- **DATEV-LODAS-Integration**: unveraendert dokumentiert (`timetac.com/en/integration-api/datev-lodas`).
- **TimeTac-Blog 07-10/2026**: kein spezifisches neues Produkt-Signal auffindbar — **Gap-Markierung**, Follow-up-Direkt-Scrape im naechsten Zyklus empfehlenswert.
- **Cosmi-W43-Delta-Konsequenz**: TimeTac-Preis-Struktur + Feature-Set stabil, Cosmi-Preis-Differential 3 EUR OHNE Basisgebuhr vs. TimeTac Essential 3 EUR + 19.50 EUR Basis = Cosmi weiter 5-User-Cluster 85% guenstiger (15 EUR vs. 45.50 EUR). DATEV-Realtime-Sync fuer `hr_work_time_entries` bleibt W28-🟡-Pick, 15 Wochen null geliefert.

**4. ZEP (DE, threat: MEDIUM→HIGH, Delta: ERSTER DACH-PSA-Player mit GenAI-Launch September 2026)**

W28-Snapshot: PSA-Fokus Consulting/IT-KMU, Reisekosten-Modul v2.14.0, keine AI-Features, Pricing 2-18 EUR.

- **Release 8.0 September 2026 mit "ZEP Assistant"**: In-App-GenAI, Buchen/Antrag/Belege via Natural Language, Confirmation-Card-Pattern (User-Bestaetigung vor AI-Aktion), Audit-Log fuer AI-Aktionen (`zep.de/en/roadmap`). **Erster deutscher PSA-Player mit konkretem GenAI-Produkt-Launch im Delta**.
- **Pricing-Stack**: stabil (Clock 2, Compact 7, Professional 18 EUR).
- **Cosmi-W43-Delta-Konsequenz**: ZEP Assistant ist **auf Buchungs-UX scoped (nicht Rapport-Erzeugung)** — Cosmi-rapporte direkt nicht konkurriert, aber Cosmi-zeiterfassung-Consulting-Overlap-Zone (IT/Beratungs-KMU) betroffen. ZEP-Confirmation-Card-Pattern + Audit-Log fuer AI-Aktionen ist **genau das Pattern das Cosmi fuer AI-Act-Art.-50-Compliance brauchen wird** — ZEP liefert strukturellen Blueprint. Cosmi-Sprint-Anker: wenn AI-Rapport-Auto-Kategorisierung gebaut wird, Confirmation-Card-Pattern + per-Tenant-Audit-Log von Anfang an einbauen.

**5. Crewmeister (DE, threat: MEDIUM, Delta: keine 2026-H2-Preisaenderung, GPS-Positionierung bleibt)**

W28-Snapshot: 30%-Rabatt-Kampagne bis 12.06.2026, GPS-2m-Genauigkeit, 2-9 EUR Pricing.

- **Nach Rabatt-Ende**: aktuelle Tarife bestaetigt — Go 1.50 EUR / Easy 2.00 EUR / Pro 3.00 EUR (jaehrlich, ab ~50 MA, `crewmeister.com/de/fakten`).
- **GPS-Standort in Go-Paket**: bereits Einstieg (`crewmeister.com/de/magazin/zeiterfassung-software-vergleich-2026-die-7-besten-losungen`).
- **Keine neuen AI-Features 2026-H2**.
- **Cosmi-W43-Delta-Konsequenz**: Crewmeister jetzt Preis-Druck 1.50-3.00 EUR Cosmi 3 EUR — **Crewmeister-Go-Pricing 1.50 EUR ist 50% guenstiger als Cosmi-rapporte 3 EUR**. Cosmi-Differential bleibt Rapport+Aufmass+SketchCanvas (Crewmeister hat nicht) + Full-Cross-Modul-Story (Crewmeister ist Zeiterfassung-only). GPS-Consent-Flow + 2m-Genauigkeits-Story im Cosmi-UI bleibt Sprint-Luecke.

**6. clockin.de (DE Baustellen, threat: NEU HIGH, Delta: AI-Video-Doku + AI-Gespraechsnotizen seit 2026, direkter Cosmi-Preis-Cluster)**

W28-Snapshot: Baustellen-Fokus, keine konkrete AI-Positionierung erwaehnt.

- **AI-Video-Dokumentation + AI-Gespraechsnotizen** seit 2026 als neue Features (`trusted.de/clockin`, `softwareabc24.de/zeiterfassung-software/clockin`).
- **AI-Telefon-Assistent** angekuendigt (nicht GA verifizierbar).
- **Pricing 2026**: Basic 3.19 EUR / Projektzeit 6-7 EUR / Full-Suite 8-10 EUR, **DATEV/Lexoffice/Sevdesk-Integrationen**.
- **Cosmi-W43-Delta-Konsequenz**: **clockin ist 2026-Q4 der konkreteste neue Konkurrenz-Signal im Cosmi-rapporte-Preis-Cluster** — Basic 3.19 EUR vs. Cosmi-rapporte 3 EUR + Full-Suite 8-10 EUR vs. Cosmi 6 EUR (rapporte+zeit) = clockin positioniert *leicht teurer* bei bereits-live-AI, Cosmi positioniert *leicht guenstiger* bei fehlender AI. **Das ist das Preis-AI-Delta das in 6-12 Monaten entscheidend wird** fuer DACH-KMU-Handwerk-Betriebe die AI-Video-Doku als Standard-Erwartung internalisieren. Cosmi-Sprint-Pflicht: AI-Rapport-Auto-Kategorisierung + Voice-Input priorisieren.

**7. noovi (CH, threat: MEDIUM→HIGH, Delta: 2026 "AI-Sprachaufnahme → strukturierter Rapport")**

W28-Snapshot: CH-Niche-Handwerk-Feldrapport, aehnlich Cosmi, 15-30 CHF Marktumfeld.

- **2026 explizite Positionierung "AI-Sprachaufnahme → strukturierter deutscher Rapport"** (`noovi.ch/funktionen/rapporte`).
- **Offline-faehig, Werkzeug-/Lager-Modul, Bautagebuch** als Marktbenchmark fuer CH-Handwerk.
- **Pro-Paket CHF ~195/5 User** (ca. 39 CHF/User), Einstieg CHF 19/User (`noovi.ch/vergleich/handwerkersoftware-schweiz`).
- **60-Tage-Maengelruegefrist CH ab 2026-01-01** erhoeht Dokumentationsdruck → Abnahmeprotokoll-Nachfrage steigt (`noovi.ch/ratgeber/maengelruege`).
- **Cosmi-W43-Delta-Konsequenz**: **noovi ist jetzt der direkteste Cosmi-rapporte-CH-Konkurrent** und validiert die W28-Voice-Rapport-Hypothese kompetitiv (nicht mehr nur HERO-Vaporware-Schatten). CH-Markt-Zahlen 19-39 CHF/User vs. Cosmi 3 EUR = Cosmi deutlich guenstiger, aber ohne AI-Voice-Rapport. **CH-Spezifika: Cosmi-Bexio-Partnerschaft (buchhaltung-W27-W42-Analyse) + Cosmi-rapporte-AI-Voice koennte Cosmi im CH-KMU-Handwerk-Segment positionieren als "Deutscher Rapport mit Schweizer Bexio-Buchhaltungs-Bridge zu halbem noovi-Preis"**.

**8. Toggl Track (EE, threat: MEDIUM, Delta: MCP-Server + Toggl-AI-Chat-Beta)**

W28-Snapshot: Freelancer/Agentur-Marktfuehrer, Pricing-Uplift ohne AI-GA.

- **Neue Pricing-Struktur 2026**: Free-Tier bis 3 User (zuvor 5), Starter $9, Premium $16-18 (`checkthat.ai/brands/toggl/pricing`, `aiproductivity.ai/pricing/toggl-track`).
- **Beta "Toggl AI" Chat-Panel** + **MCP-Server fuer AI-Assistenten**.
- **Capacity Management + Time Off** als paid Add-ons.
- **Cosmi-W43-Delta-Konsequenz**: **MCP-Server-Signal: Zeiterfassungs-Vendor machen Daten fuer AI-Agenten adressierbar** — Cosmi-MCP-Server (W33-Keeper 10 Wochen ueberfaellig, in buchhaltung-W42-#3-Pflicht + helpdesk-W39 + formulare-W40 + vertraege-W41 immer wieder gelistet, immer noch null geliefert) bekommt neue Rechtfertigungs-Dringlichkeit auf Modul-Ebene (jetzt mit konkretem Zeiterfassungs-Konkurrenz-Signal, nicht nur CLM/Wiki/Formulare).

**9. Harvest (US / Bending Spoons, threat: LOW fuer DACH, Delta: Pricing-Hike + Legacy-Churn)**

W28-Snapshot: Bending-Spoons-Uebernahme, Preis-Kritik.

- **Pricing-Hike auf $9/Seat teams + $14/Enterprise jaehrlich** (`operating.app/blog-posts/harvest-2026-price-increase`, `tillage.ai/blog/harvest-price-increase-2026`, `timecamp.com/blog/harvest-pricing`).
- **Two-layer Billing** (Seat + Usage) seit 2026, Legacy-Kunden mit 10-15x hoeheren Rechnungen.
- **Cosmi-W43-Delta-Konsequenz**: **Harvest-Churn liefert KMU-Agentur-Pipeline fuer europaeische Alternativen** (TimeTac, ZEP, awork — und Cosmi falls PSA-Edge ausgebaut). Cosmi-zeiterfassung + Cosmi-crm + Cosmi-vertraege Full-Cross-Modul-Story als Agentur-Pitch waehrend Harvest-Pricing-Protest-Welle laeuft.

**10. Clockify (US, threat: LOW, Delta: Freemium-Entluftung April 2026)**

W28-Snapshot: Free-Tier unlimited, US-Hosting-DSGVO-Problem.

- **Ab April 2026 Free-Tier auf 5 User gekappt** (zuvor unbegrenzt), Kiosk-Mode, Billable Hours, CSV/Excel-Export, Shared Reports, Projekt-Estimates in Basic+ gezogen (`xpay.sh/saas-pricing/clockify`, `costbench.com/software/time-tracking/clockify`).
- **Pro-Plan ($7.99)**: AI-Forecasting + Kiosk Photo Capture.
- **Cosmi-W43-Delta-Konsequenz**: **Clockify-Freemium-Gravitation schwaecht sich ab — begunstigt bezahlte Mitbewerber in KMU-Konvertierung**, inkl. Cosmi fuer DSGVO-sensible DACH-KMU.

**11. Timely / Memory.ai Oslo (threat: HIGH stabil, Delta: Rebrand, keine M&A)**

W28-Snapshot: AI-Zeiterfassungs-Marktfuehrer mit Memory-Autosheet.

- **April 2026 Rebrand zurueck auf "Timely"** nach "Memory"-Interim (`timely.com/company-news/2026-04-15`).
- **Keine Memory.ai-Akquisition im Delta**: Juni-2026-"Upstage acquires Timely"-Headline betrifft **gleichnamige koreanische AI-Agenten-Firma, NICHT das Oslo-Timely** (`en.sedaily.com/technology/2026/06/09/upstage-acquires-ai-agent-platform-timely-to-diversify-ai`). **W28-Risiko-Annahme "Timely-DACH-Fokus 2026" bleibt gueltig**, keine M&A-Beschleunigung.
- **Cosmi-W43-Delta-Konsequenz**: Timely-Enterprise-Pricing ($11-$28/User) + GPS-Hintergrund-Erfassung bleibt DSGVO-Angriffsflaeche, Cosmi-Chance-"AI-Rapport-Auto-Kategorisierung ohne kontinuierliche Ortung" unveraendert.

**12. Papershift + TimeChimp + Kimai + Factorial HR**: alle vier zeigen **keine materiellen 2026-H2-Produkt- oder Pricing-News** (Papershift-Shiftbase-Fortino-Kapital-Investment April 2026 fuer Shiftbase-EU-Expansion verschaerft DACH-Schicht-Markt-Druck, aber nicht direkt rapporte).

**13. Workyard (US Bau, threat: LOW DACH, Delta: September 2026 customizable Overtime + Time-Assistant)**

Workyard-Release September 2026 — customizable Overtime-Regeln + erweiterter "Time Assistant"-Zugang fuer Manager (`makerstack.co/reviews/workyard-review`). Keine EU-Expansion-Signale.

**14. mobiel, Buildertrend, Procore, Rhumbix**: **keine neuen DACH-Launches**, mobiel-Signal weiter abwesend (Vendor moeglicherweise ruhend).

### Zusammenfassende Konkurrenz-Delta-Tabelle (nur Items die W28-W43 geaendert haben)

| Konkurrent | W28-Position | W43-Delta | Cosmi-strategische-Konsequenz |
|---|---|---|---|
| **ZEP** | 2-18 EUR, keine AI | **Release 8.0 Sept 2026 "ZEP Assistant"**, GenAI Buchung + Confirmation-Card + Audit-Log | ZEP-Pattern als Blueprint fuer Cosmi-AI-Compliance-Confirmation-Flow |
| **clockin.de** | Nicht in W28 benannt | **AI-Video-Doku + AI-Gespraechsnotizen seit 2026** im 3-EUR-Preis-Cluster | **Konkretester neuer Konkurrent im Cosmi-Preis-Segment**, Sprint-Pflicht AI-Auto |
| **noovi** | CH-Niche-Rapport | **"AI-Sprachaufnahme → strukturierter Rapport" 2026** | Validiert Voice-Rapport-Hypothese; Cosmi-CH-Strategie mit Bexio-Bridge |
| **HERO Report** | Angekuendigt 2026 | **Weiter Vaporware 15 Wochen** | **Fenster bleibt offen** fuer Cosmi Voice-Rapport bis mindestens Q1/2027 |
| **Toggl Track** | Freelancer, kein AI | **MCP-Server + Toggl-AI-Chat-Beta** | MCP-Server-Signal verschaerft Cosmi-MCP-Server-Prioritaet (W33-Keeper) |
| **Harvest** | Preis-Kritik | **Pricing-Hike $9-$14/jaehrlich + two-layer Billing** | Churn-Pipeline fuer EU-Alternativen inkl. Cosmi fuer Agentur-Pitches |
| **Clockify** | Free unlimited | **April 2026 Free-Tier auf 5 User gekappt** | Freemium-Gravitation entluftet, bezahlte DSGVO-Alternativen bevorzugt |
| **Timely Oslo** | AI-Marktfuehrer | **Rebrand zurueck zu "Timely" April 2026, keine M&A** | Risiko-Annahme stabil, kein Akquisitions-Beschleuniger |
| **123erfasst** | Bau-Marktfuehrer | **digitalBAU 2026 Kalkulations-Modul, keine AI** | Vorsprung stabil, Cosmi-Offline-Queue schliesst Hauptluecke |
| **TimeTac** | HR-Marktfuehrer | **Keine materiellen News 15 Wochen** | Markt-Snapshot stabil, DATEV-Realtime-Sync-Luecke bleibt |

---

## Cosmi-IST-Stand

**rapporte ist das Zyklus-2-Modul mit dem besten W28→W43-Delivery-Score auf P0-Pflicht-Picks** — zwei von vier P0-Picks geliefert (Baustellen-Offline-Mode + SignatureCanvas-Ausbau), vier Bonus-Deliveries nicht in W28 prognostiziert (real-PDF-Export via maroto/v2, ReportDetailModal-Extraction, Test-Investment-Komplett-Sprint, RBAC-R-3-Batch-4-Enforcement), drei P0-Picks weiter null (ADR-0009-Domain-Konsolidierung, AI-Rapport-Auto-Kategorisierung, PWA-Handschuh-UI). Parallel-Modul `zeiterfassung`/HR-Backend hat 10 Zyklus-2-Deliveries bekommen (Week-Approval-Locks + Reopen, Superseded-State, Tenant-Hardening, Offboarding, Double-Invoice-Prevention, Manual-Entry-Idempotency, Analytics-Coverage).

### Backend `backend/internal/rapporte/` — W28→W43-Delta

| File | W28 LOC | W43 LOC | Delta | Rolle |
|---|---|---|---|---|
| `errors.go` | 16 | 16 | 0 | Domain-Sentinels unveraendert |
| `models.go` | 140 | 140 | 0 | WorkReport + ReportLine + Worker + Measurement + ReportTemplate — unveraendert |
| `postgres_repository.go` | 938 | 952 | +14 | CRUD + Tenant-Isolation (minimale Erweiterung) |
| `repository.go` | 73 | 75 | +2 | Interface-Minor-Erweiterung |
| `service.go` | 636 | 646 | +10 | 21 Service-Methoden + validateGPS (minimale Erweiterung) |
| `pdf.go` | — | 156 | **+156 NEU** | **maroto/v2-basierter PDF-Renderer (Commit `7a01590f` 2026-08-02)** |
| `service_test.go` | 961 | 1036 | +75 | Reject-Reason + State-Guards |
| `postgres_repository_test.go` | — | 898 | **+898 NEU** | **CRUD + atomic transitions (Commit `f33da131` 2026-08-11)** |
| `tenant_write_test.go` | — | 125 | **+125 NEU** | **real-repo tenant write tests (Commit `a133ebd2` 2026-07-28)** |
| `own_scope_list_test.go` | — | 93 | **+93 NEU** | **RBAC scope-own tests** |
| `signature_test.go` | 165 | 165 | 0 | Signature-Persistenz unveraendert |
| `tenant_isolation_phase2_test.go` | 69 | 69 | 0 | Cross-Tenant unveraendert |
| **TOTAL** | **2998** | **4371** | **+1373 (+46%)** | **8→12 Files, Prod-LOC +180 (+9.8%), Test-LOC +1191 (+99%)** |

### Rapporte Git-Log (W28→W43, 15 Wochen)

| Commit | Datum | Titel | W28-Delta-Konsequenz |
|---|---|---|---|
| `23c39644` | 2026-07-15 | feat(rapporte): demo-depth - real pdf export, detail modal, settings | **W28-Mono-File-Refactor-Vorbereitung** (ReportDetailModal 500 LOC Extraktion aus RapportePage) |
| `2055c475` | 2026-07-19 | feat(rbac): R-3 batch 4 enforcement - schichten, fuhrpark, vermietung, rapporte, dialer | scope-own filtering fuer edit/delete + reviewer-role fuer approve |
| `a133ebd2` | 2026-07-28 | test(schichten,rapporte,vertraege): add real-repo tenant write tests | +125 LOC Test |
| `7a01590f` | 2026-08-02 | feat(rapporte): render real PDF for work report export | **NEU `pdf.go` 156 LOC via maroto/v2** — W28 behauptete ExportPDF-RPC existiere, bis dato Stub |
| `cefb5419` | 2026-08-10 | fix(rapporte): require a reason when rejecting a report | review_note auf RejectReport Pflicht |
| `f33da131` | 2026-08-11 | test(rapporte): cover postgres_repository update/delete/get/list and atomic transitions | **NEU `postgres_repository_test.go` 898 LOC** |
| `152fa892` | 2026-08-11 | fix(rapporte): default empty template lines to [] instead of NULL | Template-Lines-Default-Fix |
| `3f151a26` | 2026-08-26 | test(gateway): cover rapporte measurement handlers and add-position tenant gap | Measurement-Tenant-Gap-Coverage |
| `94076a6d` | 2026-08-26 | test(gateway): cover rapporte line/attachment/signature/template handlers | Gateway-Full-Chain-Coverage |
| `9db416e3` | 2026-08-27 | fix(rapporte): reject measurement positions for foreign measurements | Measurement-Cross-Tenant-Reject |

### HR-Timetracking Git-Log (W28→W43) — Parallel-Modul-Deliveries

| Commit | Datum | Titel | Cosmi-Delta-Konsequenz |
|---|---|---|---|
| `b871bbba` | 2026-07-26 | fix(hr): stop approved time corrections from counting twice | **Migration 000248 superseded status** — Correctness-Fix |
| `7d612aa3` | 2026-07-26 | feat(hr): enforce week approval locks and add the reopen transition | **W28-Multi-Stage-Freigabe-adjacent AUF HR-SEITE geliefert** |
| `9f2045c9` | 2026-07-27 | refactor(hr): scope every work time query to its tenant | Tenant-Isolation-Hardening |
| `d78f9176` | 2026-07-27 | fix(hr): write the tenant on break entries and scope every break query | Break-Entries-Tenant-Fix |
| `23ceede6` | 2026-08-03 | feat(hr): add employee offboarding | **Neue Lifecycle-Feature** (HR-Scope, nicht rapporte) |
| `121ea866` | 2026-08-08 | test(biz): cover hr timetracking week-approval repo and state machine gaps | Week-Approval-State-Machine-Coverage |
| `5f442703` | 2026-08-22 | fix(biz): prevent double invoice creation from the same time entries | **Faktische Rapport→Rechnung-Bridge via time entries** — W28-Option-B-adjacent |
| `6ea944c3` | 2026-08-26 | test(hr): prove manual-entry idempotency dedup through gateway chain | Idempotency-Dedup |
| `28a5d652` | 2026-08-26 | test(gateway): cover HR time-tracking approvals, balances, and catalogues | Full-HR-Gateway-Coverage |
| `1e6691f1` | 2026-08-26 | test(gateway): cover HR time analytics and settings handlers | HR-Analytics-Coverage |

### Migrationen W28→W43 (rapporte + zeiterfassung-relevant)

| Migration | Datum (est.) | Inhalt | Strategischer Anker |
|---|---|---|---|
| 000248 | 2026-07-26-ish | **work_time_superseded_status** | 5. State fuer hr_work_time_entries, Correction-Replace-Audit-Trail, Backfill-Query gegen double-counting |

Nur **eine** Migration mit direktem Zeiterfassungs-Impact in 15 Wochen (Migration 000248). Migrations 000245 `report_documents` + 000252 `report_share_tokens` sind **`berichte`-Modul (Dashboard-Reports mit TipTap-Bloecken), NICHT `rapporte`-Modul** — Namenskollision wie in W35-crm-core Delta zu beachten. Migration 000195 `create_gps_positions` ist **fuhrpark-Vehicle-GPS**, nicht rapporte.

### Frontend `desktop/src/renderer/src/modules/rapporte/` — W28→W43-Delta

| File | W28 LOC | W43 LOC | Delta | Rolle |
|---|---|---|---|---|
| `RapportePage.tsx` | 1869 | 1641 | **-228 (-12%)** | **Mono-File SHRINKS** — ReportDetailModal-Extraction |
| `SketchCanvas.tsx` | 732 | 732 | 0 | Aufmass-Canvas unveraendert |
| `SignatureCanvas.tsx` | 3 | 3 | 0 | **Jetzt 3-Zeilen-Re-Export** auf `@/components/signature/SignatureCanvas` |
| `ReportDetailModal.tsx` | — | 500 | **+500 NEU** | **Extraction aus RapportePage (Commit `23c39644`)** |
| **TOTAL rapporte-Modul** | **2604** | **2876** | **+272 (+10.4%)** | **4 Files, Mono-File-Anti-Pattern GEBROCHEN** |

### Shared Signature-Component — NEU in Zyklus 2

- **`desktop/src/renderer/src/components/signature/SignatureCanvas.tsx` 215 LOC** — native HTML5-Canvas mit DPR-Scaling, Mouse+Touch-Events, Clear-Button + Save-Button, i18n-Keys `rapporte.signature.*` (default), initialData-base64-PNG-Load, lineCap='round', lineWidth=2. **Geteilt mit vertraege/vermietung Modulen** (W41-vertraege-Delta-Analyse hat Signature-Backend als unverbunden markiert — jetzt Frontend-Shared-Component ist das Bindeglied, aber vertraege-Pick-#1-Skribble-Integration ist davon unabhaengig und null geliefert).
- **Keine `react-signature-canvas` oder `signature_pad` npm-Dependency** — Cosmi hat Custom-Canvas implementiert statt W28-Empfehlung zu folgen. Funktional aequivalent, 0 npm-Supply-Chain-Risiko, 0 bundle-size-Zuwachs.

### Offline-Queue — NEU in Zyklus 2

- **`desktop/src/renderer/src/api/offline-queue.ts` 247 LOC** mit:
  - IndexedDB-Storage-Keys: `cosmi-mutation-queue`, `cosmi-mutation-dead-letter`
  - Idempotency-Key-Header Auto-Generation via `generateIdempotencyKey()`
  - Exponential-Backoff: 1s → 2s → 4s → 8s → 16s (MAX_RETRIES=5)
  - Batched-Parallel-Replay MAX_PARALLEL=5
  - Dead-Letter-Store fuer Items > MAX_RETRIES
  - Response-Handling: 2xx idempotent, 4xx (ausser 409/429) non-retryable, 5xx retryable
  - Public API: `enqueue(method, path, body, headers?, idempotencyKey?)`, `drain(baseUrl, getAccessToken)`, `peek()`, `getDeadLetter()`, `retryDeadLetter(idempotencyKey)`, `clear()`
- **Test**: `desktop/src/renderer/src/api/__tests__/offline-queue.test.ts`
- **Keine `sync_pending`-Felder in Migrationen** — Queue persistiert in IndexedDB unabhaengig vom DB-Schema (Cosmi-Design-Entscheidung: Client-side-Queue, nicht Server-side-State-Tag). Das ist pragmatisch und entkoppelt Rapport-Modell von Offline-Mechanik.

### Parallel-Modul-Frontend `desktop/src/renderer/src/modules/zeiterfassung/` (unveraendert ~978 LOC)

- **ZeiterfassungPage.tsx** 35 LOC, **AuswertungenView** 204, **TeamView** 132, **ManualEntryDialog** 200, **ExportDialog** 151, **StundenkontoBadge** 38, **WeekSubmitBanner** 48, **ZeiterfassungSettingsPanel** 205 — **praktisch unveraendert** gegenueber W28.
- **Frontend-Delta Zyklus-2**: Backend-HR-Timetracking hat 10 Deliveries bekommen, Frontend hat null — klassisches Zyklus-2-Backend-vorne-Frontend-hinterher-Pattern (anders als rapporte, wo Frontend diesmal mit refactor-Delivery dabei ist).

### Was Cosmi-rapporte W43 KANN (vs. W28 Delta)

| Feature | W28-Status | W43-Status | Zyklus-2-Delivery |
|---|---|---|---|
| ✅ 21 Service-Methoden | ✅ | ✅ | unveraendert |
| ✅ Approval-State-Machine (draft/submitted/approved/rejected) | ✅ | ✅ + review_note-Pflicht bei Reject | `cefb5419` |
| ✅ GPS-Tag + validateGPS-Bounds | ✅ | ✅ | unveraendert |
| ✅ Signature-Backend | ✅ | ✅ | unveraendert |
| ✅ Extended Field-Report (weather/temp/work_start/end/break_minutes/project_name) | ✅ | ✅ | unveraendert |
| ✅ Aufmass-Canvas SketchCanvas | ✅ | ✅ | unveraendert |
| ✅ MinIO-Attachments + Tenant-Prefix-Validierung | ✅ | ✅ | unveraendert |
| ✅ Separate `:approve`-Permission (admin-only) | ✅ | ✅ | unveraendert |
| ✅ Tenant-Isolation | ✅ | ✅ + measurement-position-cross-tenant-reject | `9db416e3` |
| ⚠️ ExportPDF-RPC (W28 behauptete existent, war Stub) | ⚠️ | **✅ real PDF via maroto/v2** | **`7a01590f` NEU 156 LOC `pdf.go`** |
| ✅ Report-Templates mit default_lines_json | ✅ | ✅ + default [] statt NULL | `152fa892` |
| ✅ Multi-Worker pro Rapport (report_workers) | ✅ | ✅ | unveraendert |
| ✅ Aufmass-Positionen (Measurement + MeasurementPosition) | ✅ | ✅ | unveraendert |
| ✅ Feature-Flag modules.rapporte | ✅ | ✅ | unveraendert (`backend/internal/modules/catalog.go:64`) |
| ❌ Baustellen-Offline-Mode | ❌ | **✅ offline-queue.ts 247 LOC** | **W28-P0-#2b DELIVERED** |
| ❌ SignatureCanvas-Frontend (3-LOC-Stub) | ❌ | **✅ Shared-Component 215 LOC** | **W28-P0-#2a DELIVERED** |
| ❌ ReportDetailModal | ❌ | **✅ Extraction 500 LOC** | **Bonus (`23c39644`)** |
| ❌ RapportePage-Refactor | ❌ | **✅ -228 LOC** | **Bonus (`23c39644`)** |
| ❌ rapporte Test-Coverage (33.9%) | ❌ | **✅ Test-LOC +99%** (postgres_repo + tenant_write + own_scope) | **Bonus** |
| ❌ scope-own RBAC filtering | ❌ | **✅ R-3 batch 4** | **Bonus (`2055c475`)** |

### Was Cosmi-rapporte W43 WEITER NICHT KANN (unveraenderte strategische Luecken, 15 Wochen null geliefert)

| Feature | W28-Status | W43-Status | Luecken-Alter |
|---|---|---|---|
| ❌ **ADR-0009 Domain-Konsolidierung** | ❌ | ❌ | **15 Wochen** (W28-P0 #1) |
| ❌ **Event-Emitter rapporte.SubmitReport → hr_work_time_entries** | ❌ | ❌ | **15 Wochen** (W28-Option-B-Hybrid) |
| ❌ **AI-Rapport-Auto-Kategorisierung** (`ai_categorization/`-Pfad) | ❌ | ❌ | **15 Wochen** (W28-P1 #3a) |
| ❌ **Voice-Input (`useSpeechRecognition`-Hook)** | ❌ | ❌ | **15 Wochen** (W28-P1 #3b) |
| ❌ **PWA-Manifest + Handschuh-Bedien-UI** | ❌ | ❌ | **15 Wochen** (W28-P0 #2c) |
| ❌ **GPS-Consent-Flow (`GPSConsentBanner` + Audit-Log)** | ❌ | ❌ | **15 Wochen** (W28-🟡) |
| ❌ **DATEV-Realtime-Sync fuer hr_work_time_entries** | ❌ | ❌ | **15 Wochen** (W28-🟡) |
| ❌ **DWD-Wetter-API-Auto-Erfassung** | ❌ | ❌ | **15 Wochen** (W28-🟡) |
| ❌ **Multi-Stage-Freigabe fuer rapporte** (linear bleibt) | ❌ | ❌ | **15 Wochen** (aber HR-Seite hat week_approvals.reopen bekommen) |
| ❌ **native iOS/Android-App via Capacitor** | ❌ | ❌ | **15 Wochen** (W28-🔵) |
| ❌ **Bautagebuch-Chronologie mit Foto-Zeitlinie** | ❌ | ❌ | **15 Wochen** (W28-🔵) |
| ❌ **Datanorm/IDS-Connect Handwerk-Material-Katalog** | ❌ | ❌ | **15 Wochen** (W28-🔵) |
| ❌ **Terminal-Integration (Empfangs-Buero-Hardware)** | ❌ | ❌ | **15 Wochen** (W28-🔵) |
| ❌ **GPS-Genauigkeits-Story im UI** | ❌ | ❌ | **15 Wochen** (W28-🟡) |
| ❌ **Rapport→Rechnung Cross-Modul-Frontend-UX** | ⚠️ (LinkTimeTracking-Backend-RPC existiert) | ⚠️ (Backend-Hardening + Double-Create-Prevention, Frontend-UX weiter null) | **15 Wochen** |

### Was Cosmi-zeiterfassung HR-Seite W43 KANN (vs. W28 Delta)

| Feature | W28-Status | W43-Status | Zyklus-2-Delivery |
|---|---|---|---|
| ✅ HR-Zeit-Erfassung (hr_work_time_entries) | ✅ | ✅ + **superseded-State** | Migration 000248 |
| ✅ Wochen-Freigabe (hr_week_approvals) | ✅ open/submitted/approved/rejected | ✅ + **Locks + Reopen-Transition** | `7d612aa3` |
| ✅ Zeit-Kategorien + Projekte | ✅ | ✅ | unveraendert |
| ✅ Company-Settings (work_hours_per_day, max_daily_hours, break_after_hours) | ✅ | ✅ | unveraendert |
| ✅ Tenant-Isolation | ✅ | ✅ + **break-entries-tenant-scope-fix** | `9f2045c9`/`d78f9176` |
| ✅ Manual-Entry-Idempotency-Dedup | ⚠️ | ✅ | `6ea944c3` |
| ✅ Employee-Offboarding | ❌ | **✅ feat NEU** | `23ceede6` |
| ✅ Prevent-Double-Invoice-from-Time-Entries | ❌ | **✅ fix NEU** | `5f442703` |
| ✅ Analytics + Balances + Approvals Gateway-Coverage | ⚠️ | ✅ Full | `28a5d652`/`1e6691f1` |

---

## Konkurrenz-Vergleichstabelle (W43-Delta zur W28-Tabelle)

Pflichtsektion mit >6 Zeilen; W28-Tabelle hatte 11 Konkurrenten + 36 Features. Hier **Delta-Tabelle** mit nur Items die W28→W43 geaendert haben + 3 neue Features (AI-Kategorisierung, Voice-Rapport-Input, MCP-Server-Readiness):

| Feature | Cosmi W28 | Cosmi W43 | 123erfasst | HERO | TimeTac | ZEP | clockin | noovi | Toggl | Timely |
|---|---|---|---|---|---|---|---|---|---|---|
| **Signatur-Frontend-Canvas** | ❌ 3-LOC-Stub | **✅ Shared 215 LOC** | ✅ | ✅ | ➖ | ➖ | ✅ | ✅ | ➖ | ➖ |
| **Baustellen-Offline-Mode** | ❌ | **✅ 247 LOC Queue+IDB** | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ |
| **Real PDF Export** | ⚠️ Stub | **✅ maroto/v2 156 LOC** | ✅ | ✅ | ⚠️ CSV | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| **PWA-Manifest + Handschuh-UI** | ❌ | ❌ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ✅ | ❌ | ⚠️ |
| **AI-Auto-Kategorisierung Rapport** | ❌ | ❌ | ❌ | ⚠️ Vaporware HERO Report | ❌ | ❌ (ZEP Assistant scoped auf Buchung) | ⚠️ AI-Gespraechsnotizen 2026 | ✅ 2026 Voice→Rapport | ❌ | ✅ Memory-Autosheet |
| **AI-Voice-Input Rapport** | ❌ | ❌ | ❌ | ⚠️ Vaporware HERO Report | ❌ | ❌ | ⚠️ AI-Gespraechsnotizen 2026 | **✅ 2026 AI-Sprachaufnahme** | ❌ | ❌ |
| **AI-Telefon-Assistent** | ❌ | ❌ | ❌ | ✅ HERO Voice GA 2026 | ❌ | ⚠️ ZEP Assistant 2026 | ⚠️ Angekuendigt | ❌ | ❌ | ❌ |
| **MCP-Server fuer AI-Agenten** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **✅ Toggl 2026** | ❌ |
| **C2PA-Watermark fuer AI-Content** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ (ZEP Assistant hat Audit-Log, nicht C2PA) | ❌ | ❌ | ❌ | ❌ |
| **GPS-Consent-Flow (DSGVO)** | ❌ | ❌ **15 Wochen null** | ✅ | ✅ | ✅ | ➖ | ✅ | ✅ | ➖ | ⚠️ DSGVO-fraglich |
| **Multi-Stage-Freigabe rapporte** | ❌ linear | ❌ linear | ✅ | ✅ | ⚠️ Task-Ebene | ⚠️ | ✅ | ✅ | ❌ | ❌ |
| **Multi-Stage-Freigabe HR-Woche** | ⚠️ submit/approve/reject | **✅ + Locks + Reopen** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ⚠️ |
| **ReportDetailModal (UX-Refactor)** | ❌ | **✅ 500 LOC NEU** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Test-Coverage (Produktions-Code)** | 33.9% | **~45%+ geschaetzt** | — | — | — | — | — | — | — | — |
| **Rapport→Rechnung Cross-Modul** | ⚠️ LinkTimeTracking-RPC | ⚠️ + **Double-Invoice-Prevention** | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **CSRD-ESG-Zeiterfassung-Up-Sell** | ⚠️ KMU-Scope | ❌ **Omnibus-I macht KMU-Scope obsolet** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **§16 ArbZG-Reform-ready (elektronisch)** | ✅ hr_work_time_entries | ✅ + **superseded + Locks + Reopen** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| **Pricing (EUR/User/Monat Baseline)** | **3 rapporte + 3 zeit** | **unveraendert** | 30-50 | 69-345 | 3-9 + 19.50 Basis | 2-18 | **3.19-10** | **~19-39 CHF** | $9-$18 | $11-$28 |

Legende: ✅ Full implementiert, ⚠️ Eingeschraenkt/Partial, ➖ N/A fuer Tool-Kategorie, ❌ Fehlt vollstaendig

**Lesart der Delta-Tabelle**:
- **Cosmi-Delivery-Fortschritte Zyklus 2** (6 Stellen aus ❌ auf ✅): Signatur-Frontend-Canvas (W28-P0 #2a geliefert), Baustellen-Offline-Mode (W28-P0 #2b geliefert), Real-PDF-Export (W28-Behauptung-nachgezogen), Multi-Stage-HR-Woche-Approval (nicht W28-vorgesehen, aber HR-Seite als Zyklus-2-Bonus geliefert), ReportDetailModal-Extraktion (Bonus-Delivery), Test-Coverage (Investment-Sprint).
- **Cosmi-Static-Luecken Zyklus 2** (6 Stellen weiter ❌): PWA-Manifest + Handschuh-UI, AI-Auto-Kategorisierung, AI-Voice-Input, GPS-Consent-Flow, Multi-Stage-Freigabe-rapporte, MCP-Server. Alle 6 Stellen sind in Zyklus 1 bereits markiert, 15-Wochen-null-Delivery-Fenster.
- **Cosmi-Negativ-Delta Zyklus 2**: CSRD-ESG-Zeiterfassung-Up-Sell (W28 schon markiert als KMU-Scope, Omnibus-I macht KMU-Scope obsolet — ein W28-Nebenargument faellt weg).
- **Konkurrenz-Positiv-Delta Zyklus 2** (3 Stellen): ZEP Assistant (Buchungs-UX GenAI), clockin AI-Video + AI-Gespraechsnotizen (im Cosmi-Preis-Cluster), noovi AI-Sprachaufnahme → strukturierter Rapport (direktester CH-rapporte-Konkurrent). HERO Report + HERO Command bleiben Vaporware (Cosmi-Fenster bleibt offen).
- **Pricing-Delta**: Cosmi-rapporte-3-EUR-Preis **unveraendert**, aber clockin-Basic-3.19-EUR + Crewmeister-Go-1.50-EUR Druck jetzt im Cluster. Cosmi-Full-Suite-6-EUR (rapporte+zeit) + 20-EUR-Full-Cross-Modul-Story bleibt vorteilhaft gegen 123erfasst-30-EUR + HERO-69-EUR + Timely-$11-$28.

---

## Top-3 Strategische Pflicht-Empfehlungen (statt breitem 15-Picks-Katalog)

Wegen 50% W28-P0-Pflicht-Delivery-Score (2/4 geliefert) **drei Pflicht-Empfehlungen W43** statt 7+-Picks-Katalog. Jede Empfehlung schliesst eine konkrete W28-Luecke mit konkretem W43-Trigger:

### Empfehlung 1: ADR-0009 Domain-Konsolidierung SOFORT schreiben + Option-B-Hybrid-Bridge implementieren (P0, 3-4 PT, KW43-KW44)

**Was**: ADR-0009 "Rapporte + Zeiterfassung Domain-Konsolidierung" schreiben mit **festgelegter Entscheidung Option-B-Hybrid** (nicht Option A full merge). Event-Emitter-Pfad implementieren: `rapporte.SubmitReport` → `hr_work_time_entries.CreateFromRapport`-RPC fuer AuthorID + report_workers. Frontend `RapportePage` zeigt Rapport-Woche im `ZeiterfassungsBadge` inline. Rapport-`work_start`/`work_end`/`break_minutes` werden automatisch als `hr_work_time_entries` fuer AuthorID gebucht; `hr_week_approvals` nutzt dieselben Zeit-Entries fuer Wochen-Lock + Reopen (die Zyklus-2-neu-gebauten HR-Seite-Transitions).

**Warum jetzt P0**:
- **15 Wochen null geliefert, HR-Seite hat 10 Deliveries parallel ohne Bridge** — Produkt-Risiko aus HR↔rapporte-Divergenz ist jetzt groesser als W28-Baseline. HR-Seite hat Lock/Reopen/Supersede/Offboarding/Double-Invoice-Prevention; rapporte-Seite hat Linear-State-Machine ohne Correction-Semantik. Zwei Datenwelten, zwei State-Machinen, keine Bridge.
- **ArbZG-Reform-Dringlichkeit sinkt zwar** (Uebergangsfrist 5 Jahre fuer <50MA = 2029-2032-Horizont), **aber Produkt-Risiko aus HR↔rapporte-Divergenz steigt** (Cosmi-Handwerk-Kunde bucht Rapporte, aber Wochen-Aggregation laeuft gegen hr_work_time_entries ohne Bridge — Sales-Blocker fuer Kunden mit >10 MA die ArbZG-ready sein wollen).
- **W28-Option-B 3-4-PT-Schaetzung bleibt gueltig** — Event-Emitter-Pfad mit `biz/hr/leave/event_emitter.go` als Precedent (schon fuer leave-Modul implementiert, Pattern-Reuse).
- **`5f442703` 2026-08-22 "prevent double invoice creation from the same time entries" liefert faktisch Option-B-Bridge-Richtung schon** — Rapport→Rechnung-Bridge findet via time entries statt, Cross-Modul-Logik existiert, Event-Emitter-Fehlen ist die letzte Lucke.

**Wie**: (i) ADR-0009 `.planning/adr/0009-rapporte-zeiterfassung-domain-consolidation.md` schreiben mit festgelegter Option-B-Hybrid-Entscheidung. (ii) Neuer `backend/internal/rapporte/events.go` mit `OnReportSubmitted`-Hook, abonniert von `backend/internal/biz/hr/timetracking/service.go`-`CreateFromRapport`-RPC. (iii) Migration `000325_rapporte_work_time_link.up.sql` fuer `hr_work_time_entries.source_rapport_id`-FK (nullable, kein Breaking-Change). (iv) Frontend-`ZeiterfassungsBadge` in RapportePage.tsx neu einbauen (eine der 1641 LOC-Stellen).

**Schaetzung**: 3-4 PT (unveraendert aus W28). **W43-Trigger**: KW43 ADR-schreiben + KW44 Code-Implementierung.

**Anti-Muster vermeiden**: Nicht "nur ADR schreiben ohne Code" — W28-Entscheidung ist 15 Wochen alt, es braucht atomare Delivery (ADR + Event-Emitter + Migration + Frontend-Badge als 1 Sprint-Paket).

### Empfehlung 2: AI-Rapport-Auto-Kategorisierung + C2PA-Watermark-Marker + ai_disclosure-Table als 1-Sprint-Paket (P0, 6-8 PT, KW44-KW47)

**Was**: Drei zusammenhaengende AI-Compliance-Deliveries als EIN-Sprint-Paket:

(i) **AI-Rapport-Auto-Kategorisierung**: neuer Pfad `backend/internal/rapporte/ai_categorization/service.go` mit **Mistral-Adapter oder Haiku-5.5-Adapter** (Haiku-5.5 ist 90%-Preis-reduziert laut buchhaltung-W42-Analyse, $0.10/$0.50 pro-Million-Tokens, HubSpot-CRM-Benchmark 92.8% — passt zur Cosmi-Multi-Provider-Router-Vision). Input: Rapport-Description + report_lines + report_attachments-Metadata + report_workers. Output: Kategorie-Vorschlag pro Line + Artikel-Zuordnung fuer `report_lines.category`/`.article` mit Confidence-Score. Lern-Schleife via `ai_categorization_corrections`-Tabelle (Migration 000326+).

(ii) **C2PA-Watermark-Marker**: Migration 000327+ `work_reports.ai_generated_fields` TEXT[]-Spalte, Set bei AI-Auto-Fuellung, C2PA-Content-Credentials-Serializer in PDF-Export (nutzt `pdf.go`-maroto/v2-Pfad, embeddet C2PA-Manifest-JSON als PDF-Attachment nach [c2pa.org Spec](https://c2pa.org/specifications/specifications/1.3/specs/C2PA_Specification.html)).

(iii) **ai_disclosure-Table + Confirmation-Card-Pattern**: zentrale `ai_disclosure`-Tabelle fuer tenant-weite Disclosure-Config (seit W39-helpdesk + W40-formulare + W41-vertraege + W42-buchhaltung immer wieder gefordert, immer null geliefert — jetzt mit konkretem Deadline-Trigger). Frontend-ConfirmationCard-Pattern (uebernommen von ZEP-Assistant-Blueprint): User sieht AI-Vorschlag + Confidence + Confirm/Reject-Buttons vor Save.

**Warum jetzt P0**:
- **EU AI Act Art. 50 Grace-Period-Ende 2026-12-02 = 44 Tage** fuer maschinenlesbare Markierung von AI-Content. Cosmi-video-Modul (Wave-7C Meeting-AI-Summary seit 2026-08-02 live) ist seit 78 Tagen Non-Compliant; rapporte-AI haette diesen Compliance-Fehler jetzt vermeidbar.
- **AI-Markt-Fenster schmaler**: clockin (AI-Gespraechsnotizen im 3-EUR-Preis-Cluster) + noovi (AI-Sprachaufnahme CH) sind in 15 Wochen live gegangen, HERO Report bleibt Vaporware. Cosmi-20-Wochen-Verzug wird teuer.
- **Mistral-Adapter oder Haiku-5.5-Adapter kostet Cosmi minimal** (Setup-PT ~2-3 nach W42-buchhaltung-Analyse der Multi-Provider-Router-Vision).
- **Rapport-Content ist strukturell AI-geeignet**: Freitext-Description + Foto-Metadata + report_workers-Pattern → Kategorie-Zuordnung ist niedrig-Risiko-High-Value-AI-Case (nicht Performance-Scoring, nicht Task-Allocation → NICHT Annex-III-High-Risk).

**Wie**: (i) `backend/internal/rapporte/ai_categorization/service.go` mit LLM-Adapter-Interface (`CategorizeLine(ctx, input) → (CategoryProposal, error)`). (ii) Migration 000326 `ai_categorization_corrections` (tenant_id, report_id, report_line_id, proposed_category, accepted_category, confidence, model_name, created_at). (iii) Migration 000327 `work_reports.ai_generated_fields` TEXT[] + `work_report_lines.ai_generated_fields` TEXT[]. (iv) C2PA-Serializer in `pdf.go` als embedded JSON-Attachment. (v) Zentrale `ai_disclosure`-Tabelle (Migration 000328, tenant_id, module, feature_key, is_enabled, disclosed_at, provider_name, model_name). (vi) Frontend `ConfirmationCard`-Komponent in `RapportePage.tsx` + `ReportDetailModal.tsx`.

**Schaetzung**: 6-8 PT (AI-Service 3 PT + Migrations 1 PT + C2PA-Serializer 1 PT + ai_disclosure 1 PT + Frontend-Confirmation-Card 2 PT).

**Deadline**: 2026-12-02 fuer Art.-50-Watermark-Pflicht. 44 Tage ab 2026-10-19 = **KW47-Fenster-schluss**.

**Cosmi-Differential**: **erster AI-differenzierender DACH-KMU-Zeiterfassungs-Player unter 10 EUR/User-Monat MIT C2PA-Compliance von Anfang an**. Story: "Cosmi-rapporte mit KI-Kategorisierung + maschinenlesbare EU-AI-Act-Markierung fuer 3 EUR/User-Monat — HERO Report ist 2026 noch nicht live, clockin AI-Gespraechsnotizen hat keinen C2PA-Marker, noovi AI-Sprachaufnahme CH-only."

**Anti-Muster vermeiden**: Nicht "AI-Timesheet-Draft bauen" (Timely-USP mit 90%-Korrektur-Reduktion und ausgereiften Kalender-/App-Ingestion-Pipelines, nicht kopieren). Cosmi-Chance ist angrenzende Rapport-Kategorisierung + Voice-Input, nicht Timesheet-Draft-Kopie.

### Empfehlung 3: GPSConsentBanner + report_gps_consent_events-Tabelle + Audit-Log als 2-PT-Compliance-Sprint (P1, KW45)

**Was**: Drei zusammenhaengende Compliance-Deliveries:

(i) **GPSConsentBanner-Komponente** in `RapportePage.tsx` + `SettingsPanel.tsx` — DSGVO-konformer transparenter Banner "Standort bei Rapport-Erstellung erfassen (DSGVO Art. 6 Abs. 1 lit. c ArbZG-Erfassung) — ja/nein". Tenant-weiter Opt-out via `SettingsPanel.tsx`.

(ii) **report_gps_consent_events-Tabelle** (Migration 000329+) mit `event_type` (rapport_create/clock_in/clock_out), `consent_at`-Timestamp, `consent_source` (tenant_setting/user_toggle), `report_id`-FK, `user_id`-FK, `tenant_id`-FK. DSGVO-Beweislast-fest.

(iii) **GPS-Erfassung nur bei aktivem User-Action-Event** (nicht kontinuierliche Ortung) — Code-Audit der RapportePage.tsx `useGeolocation`-Pfad, assertion: GPS-API-Call nur bei Submit-Button-Press, nicht im Hintergrund.

**Warum jetzt P1**:
- **GPS/DSGVO-Pruefschwerpunkt 2026** bei DE-Landesdatenschutzbehoerden, Bussgelder steigen (`geotapp.com/blog/de/2026/06/15`).
- **BAG 8 AZR 209/21 vom 08.05.2025 Nachwirkung**: § 26 Abs. 1 BDSG allein reicht nicht, BV ODER Art. 6 DSGVO notwendig. Cosmi-UI heute liefert weder Consent-Flow noch Audit-Log — Beweislast-Problem fuer Cosmi-Kunden mit Betriebsrat.
- **Zyklus-3-Sales-Blocker-Prevention**: ohne GPS-Consent-Flow kann Cosmi-Sales keine DE-KMU mit Betriebsrat gewinnen (Verweigerung an Datenschutz-Pruefstelle). W28-🟡-Pick wird de-facto-🟢-Pflicht.
- **Niedrige Komplexitaet**: 2 PT, Component + Migration + 3 Backend-Hooks + Settings-Panel-Toggle.

**Wie**: (i) `desktop/src/renderer/src/modules/rapporte/GPSConsentBanner.tsx` NEU (~100 LOC). (ii) `backend/internal/rapporte/postgres_repository.go`-Erweiterung fuer `InsertGPSConsentEvent`-RPC. (iii) Migration 000329 `report_gps_consent_events`. (iv) Settings-Panel-Toggle `rapporte.gps.enabled` (tenant_setting). (v) `useGeolocation`-Hook-Audit (ggf. umbauen).

**Schaetzung**: 2 PT.

**Cosmi-Differential**: **DSGVO-Pruefschwerpunkt-robust mit transparentem Consent-Flow** — gegen Timely (Hintergrund-GPS, DSGVO-fraglich) + Clockify (US-Hosting, DSGVO-fraglich) differenzierend positioniert. Cosmi-EU-Sovereign-Story bekommt konkretes Produkt-Feature.

**Anti-Muster vermeiden**: Nicht "nur Settings-Panel-Toggle ohne Audit-Log" — Beweislast-Pflicht nach Art. 7 DSGVO (Consent-Dokumentation) braucht Timestamp + Source, nicht nur Boolean-Flag.

---

## Quellen

Diese W43-Empfehlungen stuetzen sich auf Delta-Live-Recherche (W28 → W43, 15 Wochen) und die 2026-H2-DACH-KMU-Zeiterfassungs-/Rapport-Marktbeobachtungen:

**Konkurrenz-Produkt-Updates 2026-H2**:
- ZEP Release 8.0 Assistant Roadmap — [zep.de/en/roadmap](https://www.zep.de/en/roadmap)
- clockin AI-Features — [trusted.de/clockin](https://trusted.de/clockin), [softwareabc24.de/zeiterfassung-software/clockin](https://www.softwareabc24.de/zeiterfassung-software/clockin), [clockin.de/blog/reform-des-arbeitszeitgesetzes](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026)
- noovi 2026 AI-Voice-Rapport — [noovi.ch/funktionen/rapporte](https://noovi.ch/funktionen/rapporte/), [noovi.ch/vergleich/handwerkersoftware-schweiz](https://noovi.ch/vergleich/handwerkersoftware-schweiz/), [noovi.ch/ratgeber/maengelruege](https://noovi.ch/ratgeber/maengelruege/)
- HERO Software Features-Snapshot 2026 — [hero-software.de/features](https://hero-software.de/features), [hero-software.de/ueber-uns/presse](https://hero-software.de/ueber-uns/presse), [handwerksblatt.de](https://www.handwerksblatt.de/betriebsfuehrung/ki-soll-den-bueroalltag-im-handwerk-erleichtern), [sbz-online.de](https://www.sbz-online.de/meldungen/handwerkersoftware-hero-software-integriert-digitales-finanzmanagement)
- 123erfasst + Nevaris digitalBAU 2026 — [bvbs.de/2026/04/16/digitalbau-2026-nevaris](https://www.bvbs.de/2026/04/16/digitalbau-2026-nevaris-setzt-digitalisierungsimpulse-fr-die-baubranche/), [bpz-online.de](https://www.bpz-online.de/Baustelle-und-Baubuero/IT-am-Bau/NEVARIS-Bausoftware-GmbH-Digitalisierung-ohne-Brueche-mit-Nevaris-und-123erfasst)
- Toggl Pricing 2026 + Toggl AI MCP — [checkthat.ai/brands/toggl/pricing](https://checkthat.ai/brands/toggl/pricing), [aiproductivity.ai/pricing/toggl-track](https://aiproductivity.ai/pricing/toggl-track/)
- Harvest Pricing Hike 2026 — [operating.app/blog-posts/harvest-2026-price-increase](https://www.operating.app/blog-posts/harvest-2026-price-increase), [tillage.ai/blog/harvest-price-increase-2026](https://tillage.ai/blog/harvest-price-increase-2026), [timecamp.com/blog/harvest-pricing](https://www.timecamp.com/blog/harvest-pricing/)
- Clockify Freemium April 2026 — [xpay.sh/saas-pricing/clockify](https://www.xpay.sh/saas-pricing/clockify/), [costbench.com/software/time-tracking/clockify](https://costbench.com/software/time-tracking/clockify/)
- Timely Rebrand April 2026 — [timely.com/company-news/2026-04-15-we-re-timely-again](https://www.timely.com/company-news/2026-04-15-we-re-timely-again/), [en.sedaily.com/technology/2026/06/09](https://en.sedaily.com/technology/2026/06/09/upstage-acquires-ai-agent-platform-timely-to-diversify-ai) (Upstage-Timely ist nicht Oslo-Timely)
- Crewmeister 2026 Tarif-Snapshot — [crewmeister.com/de/fakten](https://crewmeister.com/de/fakten), [crewmeister.com/de/magazin/zeiterfassung-software-vergleich-2026](https://crewmeister.com/de/magazin/zeiterfassung-software-vergleich-2026-die-7-besten-losungen)
- TimeTac Capterra-Snapshot Januar 2026 — [capterra.com/p/127555/TimeTac](https://www.capterra.com/p/127555/TimeTac/), [timetac.com/en/integration-api/datev-lodas](https://www.timetac.com/en/integration-api/datev-lodas/)
- Workyard September 2026 Release — [makerstack.co/reviews/workyard-review](https://makerstack.co/reviews/workyard-review/)
- TimeChimp Pricing 2026 — [timechimp.com/en/pricing](https://www.timechimp.com/en/pricing)
- Kimai 2.69.0 Release Notes — [github.com/kimai/kimai/releases/tag/2.69.0](https://github.com/kimai/kimai/releases/tag/2.69.0)
- Factorial HR Zeiterfassung — [factorialhr.de/arbeitszeiterfassung-app](https://factorialhr.de/arbeitszeiterfassung-app)
- Shiftbase Fortino-Kapital April 2026 — [fortino.capital/portfolio/shiftbase](https://www.fortino.capital/portfolio/shiftbase)

**Regulatorik-Delta 2026-H2**:
- §16 ArbZG-Reform Status — [clockin.de/blog/reform](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026), [factorialhr.de/blog/arbeitszeitgesetz-reform](https://factorialhr.de/blog/arbeitszeitgesetz-reform/), [energieundrecht.com/blog-arbeitsrecht-zivilrecht/arbeitszeitgesetz-reform-2026-referentenentwurf](https://www.energieundrecht.com/blog-arbeitsrecht-zivilrecht/arbeitszeitgesetz-reform-2026-referentenentwurf)
- GPS-DSGVO BAG 8 AZR 209/21 — [activemind.legal/de/guides/urteil-gps-daten](https://www.activemind.legal/de/guides/urteil-gps-daten/), [energieundrecht.com/blog-arbeitsrecht-zivilrecht/gps-ueberwachung-mitarbeiter-firmenfahrzeuge-arbeitgeber-2026](https://www.energieundrecht.com/blog-arbeitsrecht-zivilrecht/gps-ueberwachung-mitarbeiter-firmenfahrzeuge-arbeitgeber-2026)
- GPS-Pruefschwerpunkt Landes-DSB 2026 — [geotapp.com/blog/de/2026/06/15](https://geotapp.com/blog/de/2026/06/15/gps-ortung-mitarbeiter-dsgvo-regeln-2026/)
- EU AI Act Art. 50 Watermarking 2026-12-02 Deadline — [labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article50-watermarking-deadline](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article50-watermarking-deadline/), [paulweiss.com/insights/client-memos/eu-finalises-transparency-rules-for-ai-generated-content](https://www.paulweiss.com/insights/client-memos/eu-finalises-transparency-rules-for-ai-generated-content), [praxikon.com/en/ai-act/artikel/50](https://www.praxikon.com/en/ai-act/artikel/50)
- EU AI Act Annex III HR Verschiebung 2027-12-02 (Digital Omnibus) — [knowlee.ai/blog/ai-act-annex-iii-hr-employment](https://www.knowlee.ai/blog/ai-act-annex-iii-hr-employment), [teamazing.com/blog/ai-act-annex-iii-hr-high-risk](https://www.teamazing.com/blog/ai-act-annex-iii-hr-high-risk), [technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus](https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/)
- CSRD/CSDDD Omnibus-I 2026/470 — [deutsches-nachhaltigkeitsinstitut.de/2026/csrd-und-csddd-nach-omnibus-was-sich-fuer-unternehmen-ab-2026-aendert](https://deutsches-nachhaltigkeitsinstitut.de/2026/csrd-und-csddd-nach-omnibus-was-sich-fuer-unternehmen-ab-2026-aendert/), [industrieblatt.de/csrd-omnibus-berichtspflicht-aenderungen-2026](https://industrieblatt.de/csrd-omnibus-berichtspflicht-aenderungen-2026)
- Schweiz SECO ArG Art. 46 2026 — [seco.admin.ch/dam/de/sd-web/HgQABCOvNmQV/ArGV-1-2-SECO-AB-2026-DE.pdf](https://www.seco.admin.ch/dam/de/sd-web/HgQABCOvNmQV/ArGV-1-2-SECO-AB-2026-DE.pdf), [seco.admin.ch/seco/de/home/Arbeit/Arbeitsbedingungen/Arbeitnehmerschutz/Arbeits-und-Ruhezeiten/Arbeitszeiterfassung](https://www.seco.admin.ch/seco/de/home/Arbeit/Arbeitsbedingungen/Arbeitnehmerschutz/Arbeits-und-Ruhezeiten/Arbeitszeiterfassung.html)
- MiLoG §17 2026 Anpassung — [buzer.de/17_MiLoG](https://www.buzer.de/17_MiLoG.htm), [lohndialog.de](https://www.lohndialog.de/die-mindestlohn-dokumentationspflicht-das-muessen-sie-beachten/)
- C2PA Content Credentials Spec — [c2pa.org](https://c2pa.org)

**Cosmi-interne Quellen (W28-Baseline + W43-Delta)**:
- W28-Baseline — `monthly/2026-07-06-deepdive-rapporte.md`
- `backend/internal/rapporte/` (12 Files, 4371 LOC, W28→W43 Delta +1373 LOC)
- `backend/internal/rapporte/pdf.go` (NEU 156 LOC, Commit `7a01590f` 2026-08-02 via maroto/v2)
- `backend/internal/rapporte/postgres_repository_test.go` (NEU 898 LOC, Commit `f33da131` 2026-08-11)
- `backend/internal/rapporte/tenant_write_test.go` (NEU 125 LOC, Commit `a133ebd2` 2026-07-28)
- `backend/internal/rapporte/own_scope_list_test.go` (NEU 93 LOC)
- `backend/internal/rapporte/service.go` (646 LOC + review_note-Pflicht via `cefb5419`)
- `backend/internal/rapporte/models.go` (140 LOC unveraendert — kein ai_generated_fields, keine Correction-Semantik)
- `backend/internal/biz/hr/timetracking/` (10 Zyklus-2-Commits inkl. `7d612aa3` week-approval locks + reopen, `b871bbba` superseded-status, `5f442703` prevent-double-invoice)
- `backend/internal/biz/hr/leave/event_emitter.go` (Precedent fuer Event-Emitter-Pattern — Reuse fuer rapporte.SubmitReport-Bridge)
- `backend/migrations/000248_work_time_superseded_status.up.sql` (einzige rapporte+zeit-relevante Migration in 15 Wochen Delta)
- `backend/internal/modules/catalog.go:64` (`{ID: "rapporte", Group: GroupTools, FlagKey: "modules.rapporte"}` — Modul-Katalog weiter mit rapporte als eigenes Modul)
- `backend/internal/featureflag/registry.go:74` (`modules.rapporte` DefaultEnabled:false SafeRisk LLMToggleSafe)
- `desktop/src/renderer/src/modules/rapporte/RapportePage.tsx` (1641 LOC, −228 LOC durch ReportDetailModal-Extraction)
- `desktop/src/renderer/src/modules/rapporte/ReportDetailModal.tsx` (NEU 500 LOC, Commit `23c39644` 2026-07-15)
- `desktop/src/renderer/src/modules/rapporte/SketchCanvas.tsx` (732 LOC unveraendert)
- `desktop/src/renderer/src/modules/rapporte/SignatureCanvas.tsx` (3-Zeilen-Re-Export auf shared Component)
- `desktop/src/renderer/src/components/signature/SignatureCanvas.tsx` (NEU 215 LOC Shared-Component, native Canvas + DPR-Scaling + Touch+Mouse)
- `desktop/src/renderer/src/api/offline-queue.ts` (NEU 247 LOC IndexedDB-Queue + Idempotency-Key + Exponential-Backoff + Dead-Letter)
- `desktop/src/renderer/src/api/__tests__/offline-queue.test.ts` (Test fuer Offline-Queue)
- `desktop/src/renderer/src/modules/zeiterfassung/` (978 LOC Frontend unveraendert vs. W28 ~1000)
- `monthly/2026-09-21-deepdive-helpdesk.md` W39 (AI-Compliance-Foundation-Sprint-P0 — 5. Mal in Folge Null-Delivery-Status)
- `monthly/2026-09-28-deepdive-formulare.md` W40 (AI-Compliance-Foundation-Sprint-P0 unveraendert)
- `monthly/2026-10-05-deepdive-vertraege.md` W41 (AI-Compliance-Foundation KW42-KW45 Pflicht-Sprint cosmi-weit)
- `monthly/2026-10-12-deepdive-buchhaltung.md` W42 (AI-Compliance-Foundation 6-8 Wochen Pflicht-Sprint, Haiku 5.5 Primary + Mistral Large 4 EU-Fallback)

---

## Picks (vorgeschlagen)

[ ] 🟢 **ADR-0009 Domain-Konsolidierung + Option-B-Hybrid-Bridge** (KW43 ADR + KW44 Code: Event-Emitter + Migration 000325 + Frontend-Badge, 3-4 PT, 15-Wochen-W28-P0-Luecke)
[ ] 🟢 **AI-Rapport-Auto-Kategorisierung + C2PA-Watermark + ai_disclosure-Table** (KW44-KW47 vor Art.-50-Deadline 2026-12-02, 6-8 PT, Haiku-5.5 oder Mistral-Large-4-Adapter, Migrations 000326/327/328, Confirmation-Card-Pattern aus ZEP-Assistant-Blueprint)
[ ] 🟢 **GPSConsentBanner + report_gps_consent_events + Audit-Log** (KW45, 2 PT, W28-🟡-Pick wird de-facto-🟢 wegen 2026-DSB-Pruefschwerpunkt + BAG 8 AZR 209/21-Nachwirkung, Migration 000329)
[ ] 🟡 **Voice-Input via Web-Speech-API** (Client-side, DSGVO-freundlich, 3-4 PT, nach AI-Auto-Kategorisierung priorisiert, HERO Report bleibt Vaporware, Fenster offen bis mindestens Q1/2027, → followup 30d)
[ ] 🟡 **PWA-Manifest + Handschuh-Bedien-UI** (Tenant-Setting, vergroesserte Touch-Bereiche, 2-3 PT, W28-P0-#2c 15 Wochen null geliefert aber niedrigere Dringlichkeit nach Offline-Queue-Delivery, → followup 30d)
[ ] 🟡 **DATEV-Realtime-Sync fuer hr_work_time_entries** (bexio-Webhook-Pattern-Reuse, 4-5 PT, TimeTac-Marktbenchmark-Parity, → followup 60d)
[ ] 🟡 **DWD-Wetter-API-Auto-Erfassung** (fuer Rapport-weather/temperature, 2 PT, 123erfasst-Marktbenchmark-Parity, → followup 30d)
[ ] 🟡 **Multi-Stage-Freigabe-Workflow fuer rapporte** (State-Machine-Erweiterung analog HR-Seite-Lock+Reopen, 4-5 PT, → followup 60d)
[ ] 🟡 **Cosmi-MCP-Server fuer rapporte + zeiterfassung** (Phase-1 mit SubmitReport/ApproveReport/ListReports als MCP-Tools, Toggl-MCP-Marktbenchmark-Signal, 2-3 PT nach W42-buchhaltung-Phase-1-Pattern, → followup 30d)
[ ] 🔵 **native iOS/Android-App via Capacitor-Wrapper** (langfristig, 15-20 PT, Q2-2027)
[ ] 🔵 **Bautagebuch-Chronologie mit Foto-Zeitlinie** (123erfasst-Marktbenchmark-Parity, 6-8 PT, Q1-2027)
[ ] 🔵 **Datanorm/IDS-Connect Handwerk-Material-Katalog** (HERO-Marktbenchmark-Parity, 10-15 PT, Q2-2027)
[ ] 🔵 **Terminal-Integration fuer Empfangs-Buero-Zeit-Erfassung** (TimeTac-Marktbenchmark-Parity, 8-10 PT, Q2-2027)
[ ] 🔵 **GPS-Genauigkeits-Story im UI** (Crewmeister-"2m"-Vermarktung-Parity, 1 PT, Q1-2027)
[ ] 🔵 **Rapport→Rechnung Cross-Modul-Frontend-UX** (LinkTimeTracking-Backend-RPC existiert, Double-Create-Prevention aus `5f442703` wirkt, Frontend-Button + Modal, 3-4 PT, Q1-2027)
