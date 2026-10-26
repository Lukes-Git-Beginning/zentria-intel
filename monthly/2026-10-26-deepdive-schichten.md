---
year: 2026
week: 44
modul: schichten
created: 2026-10-26
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 56
tokens_input: ~410000
tokens_output: ~34000
rotation_position: 10/15
zyklus: 2
delta_to: monthly/2026-07-13-deepdive-schichten.md
---

# Deepdive: schichten (Mo W44/2026, Zyklus 2)

> **Zweiter schichten-Deepdive** (Vorgaenger W29/2026-07-13, 15 Wochen Delta). Zyklus-2-Rotation Position 10/15 nach rapporte-W43 (2026-10-19), Nachfolger: fuhrpark (W45/2026-11-02). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Delivery-Score W29→W44: 1/13-🟢-Picks komplett geliefert, 1/13-🔴-Picks delivered (TenantInboundUnaryInterceptor), 11/13 nicht geliefert — aber 5 grosse Bonus-Deliveries nicht in W29-Picks prognostiziert.** Konkret delivered: **(a) 🔴 TenantInboundUnaryInterceptor** auf `backend/cmd/schichten/main.go:56` (schichten-Binary jetzt tenant-ready, einer von 13 ehemaligen R3-P0-3-Debt-Binaries ausgeraeumt). **Nicht delivered aus 4 🟢-Picks**: #1 AI-Auto-Assign-Heuristik (null Code, kein `backend/internal/schichten/auto_assign/`-Sub-Package, keine neuen Methoden), #2 `arbzgMinRestDuration` Tenant-Setting (bleibt Konstante `11 * time.Hour` auf `service.go:14`, kein `hr_company_settings.min_rest_hours_default`, kein `shift_arbzg_overrides`), #3 DACH-Feiertag-Auto (frontend `GERMAN_HOLIDAYS_2026`-Hardcoded-Map weiter in `desktop/src/renderer/src/modules/schichten/schichten-shared.ts:42-52` mit 9 DE-2026-Eintraegen, kein Backend-Table, keine `nager.at`-Integration), #4 `employee_availabilities`-Backend (frontend `AVAILABILITY_MOCK` weiter als `useState(AVAILABILITY_MOCK)` auf `SchichtenPage.tsx:413` mit 4 Mock-Usern). **Nicht delivered aus 5 🟡-Picks**: Zuschlags-System-Backend (`SURCHARGE_RULES`/`WEEKEND_SURCHARGE`/`HOLIDAY_SURCHARGE` weiter in `schichten-shared.ts:34-39`), ArbZG §3/§4/§9-10 Backend (`validateDailyMaxHours`/`validateBreakRules`/`validateWeeklyRestDay`/`validateConsecutiveDays` existieren null), Personio-Marketplace-Integration (null `personio`-Match im Repo), Multi-Site-Support (`Shift.Location` weiter TEXT-String, kein `locations`-Table), PWA-Layer (globaler `offline-queue.ts` existiert seit rapporte-W43, aber schichten-Mutations enqueuen nicht). **Nicht delivered aus 3 🔴-Picks**: ShiftTemplate.Color + BreakMinutes Backend-Schema (Frontend-Adapter faelscht weiter `#3b82f6` + 30), Test-Coverage auf 45%+ offen (siehe unten — delivered via Test-LOC +100%). **5 Bonus-Deliveries NICHT in W29 prognostiziert**: (A) **JArbSchG-Jugendarbeitsschutz-Compliance** als neue Service-Methoden `validateMinorProtection` (service.go:816-837) + `checkMinorShiftLimits` (service.go:839-876) + 3 Error-Sentinels `ErrJArbSchGNightWork`/`ErrJArbSchGDailyHours`/`ErrJArbSchGWeekend` (errors.go:19-21) + Migration 000299 `hr_employee_profiles.is_minor BOOLEAN` + Index `idx_hr_employee_profiles_tenant_minor` (commit 7493cf0f 2026-08-08) — enforced §8 (max 8h), §14 (keine Arbeit 20:00-06:00), §16/§17 (keine Sa/So-Arbeit). **Das ist die wichtigste Delivery der 15 Wochen und keine der 13 W29-Picks hat sie prognostiziert**. (B) **Shift-Swap-Stabilisierungs-Trio** — 3 Bugfixes auf `shift_swap_requests`-State-Machine: `f379b30a` 2026-08-29 "make shift swaps land instead of failing or no-op'ing", `4b3f6bb2` 2026-10-20 "bind swap requests to the caller's own assignment", `fe9eb5c4` 2026-10-25 "answer a second assignment of the same employee with 409 instead of 500" (HTTP-Status-Hygiene). (C) **Concurrency-Safety-Delivery** via Assignment-Lock-Pattern — commit `1d24373b` 2026-09-10 "serialise shift assignments under a shift and employee lock" + `assignment_lock_test.go` 787 LOC Dual-Assignment-Race-Coverage. (D) **RLS-Phase-2-Audit** — commit `2055c475` 2026-07-19 "R-3 batch 4 enforcement" (Capability-Catalog-Wiring fuer schichten-Permissions, scope-own-Filter fuer Swaps) + `tenant_isolation_phase2_test.go` 288 LOC + `own_scope_list_test.go` 665 LOC. (E) **Test-Investment-Welle 2× W29** — Test-LOC 2913→5826 (+100%, nur produkt-code waechst 25%), 5 neue Test-Files, Test-Ratio 48%→60% (W29-Pick #R2 "40% Referenz-Ziel" uebertroffen). **Zusaetzlich 4 Frontend-Deliveries**: `ShiftDetailModal.tsx` NEU 268 LOC (commit 9cb06ab7 2026-07-19), `schichten-export.ts` NEU 208 LOC (PDF/CSV-Builder), `schichten-shared.ts` NEU 92 LOC (SURCHARGE_RULES/WEEKEND_SURCHARGE/HOLIDAY_SURCHARGE/GERMAN_HOLIDAYS_2026 aus Mono-Page extrahiert — aber WEITER frontend-only), `SchichtenSettingsPanel.tsx` NEU 135 LOC (module-settings-registry-Integration). SchichtenPage.tsx bleibt Mono-Page 1661→2002 LOC (+21%, aehnlich rapporte-W43-Pattern "additiv waechst statt refactored"). **Delivery-Pattern-Bestaetigung (W39/W40/W41/W42/W43/W44 = 6 in Folge)**: Backend-Hygiene (Shift-Swap-Fixes + Concurrency-Lock + JArbSchG + RLS-Audit + Test-Investment) wird schnell geliefert, strategische Markt-Luecken (AI-Auto-Assign + Availability-Backend + Zuschlags-System + ArbZG-Full + DACH-Feiertag + Personio + MCP) null geliefert. **ERSTMALS positive Delivery-Signal in Zyklus-2 bei schichten**: TenantInboundUnaryInterceptor als 1-von-13-R3-P0-3-Binaries abgeschlossen (W29 war das letzte offene P0-Sicherheits-Thema).

> **Drei strukturelle Beobachtungen, die jeden Sprint-Plan W44 kalibrieren.** **#1 Der DACH-Schichtplan-Markt hat am 2026-10-22 die MCP-Agentic-Grenze ueberschritten — Planday ist First-in-Workforce mit verifizierten Dual-Connectors (ChatGPT + Claude), 216+ Early-Access-Kunden in <48h, deutsche Fach-Presse hat sofort aufgegriffen.** Am Mittwoch 2026-10-22 hat Planday (DK, Xero-Portfolio) als **erste** Workforce-Management-Plattform **verifizierte Connectors in beiden Haupt-LLM-Marketplaces** gelauncht — OpenAI ChatGPT Apps/Connectors + Anthropic Claude Marketplace Connectors (`thehotelmagazine.co.uk/planday-brings-context-aware-workforce-scheduling-to-chatgpt-and-claude`, `claude.com/marketplace/connectors/planday`, `help.planday.com/en/articles/776982-how-to-connect-planday-to-claude`). **216+ Kunden haben in Early-Access-Phase ihre Planday-Accounts verbunden** (Stand Launch-Day). Beispiel-Use-Case: Gastro-Manager fragt im Chat "Wie beeinflussen Buchungen + Wetter die Schichtdeckung?" — der Connector kombiniert Planday-Rota mit externem Kontext und liefert direkte Rekommendationen. Bank-/Payroll-/NI-Daten explizit ausgeschlossen, existing RBAC gilt, Early-Access global kostenfrei. **DACH-Impakt sofort**: `ad-hoc-news.de/wissenschaft/planday-chatgpt-und-claude-entwerfen-schichtplaene-fuer-gastronomie-und-hotels/70404162` hat am 2026-10-22 auf Deutsch berichtet mit Gastro/Hotel-Fokus — DACH-KMU-Buyer diskutieren jetzt "KI entwirft Schichtplaene" als Standard-Erwartungshaltung. **Vergleich zum DACH-Konkurrenten-Rest**: Papershift hat KI-HR-Chat (statisch, kein Connector), Shyftplan hat kein MCP (nutzt SAP-BTP-Flow), Ordio hat Nano-AI-Agent (Chat-Live-Daten, keine Marketplace-Connectors), Crewmeister/Aplano/ShiftJuggler haben null AI, Deputy hat Zapier-hosted-MCP (nicht offiziell), **UKG hat am 2026-10-20 Beta-Claude-Integration gelauncht** (`natlawreview.com/press-releases/ukg-claude-makes-ai-work-beyond-chat` — Enterprise-WFM, parallel-Benchmark). **Konsequenz fuer Cosmi**: Das Zeitfenster "MCP-Server als DACH-KMU-Erstbesetzer" ist zu, aber Zeitfenster "MCP-Server als DACH-Open-Source-ERP-Erstbesetzer" ist noch offen. Papershift/Shyftplan/Ordio/Crewmeister/Shiftbase/Sona haben alle noch keinen offiziellen Vendor-MCP-Server. Cosmi's Entscheidung W44: **(a) MCP-Server fuer schichten + rapporte + helpdesk + crm Read-Ops** als Cosmi-weiter Sprint W45-W47 (W33-Keeper 20 Wochen ueberfaellig, in buchhaltung-W42 + helpdesk-W39 + formulare-W40 + vertraege-W41 + rapporte-W43 immer wieder gelistet), **(b)** Agentic-Positioning in Marketing-Material ("Cosmi orchestriert Agenten ueber alle Module hinweg, Papershift's Chat kann nur innerhalb Schichten antworten") als erste Reaktion. Der MCP-Spec-Update 2026-07-28 (stateless, multi-round-trip, authorization-hardening, extensions-framework, `blog.modelcontextprotocol.io/posts/2026-07-28`) macht Cloudflare-Worker-Edge-Hosting trivial — der Sprint ist nicht mehr Monate, sondern 1-2 Wochen pro Modul. **Fuer schichten konkret**: ein MCP-Server mit 3 Read-Tools (`list_shifts`, `check_arbzg_compliance`, `list_swap_requests`) + 2 Write-Tools (`create_shift`, `assign_employee` mit human-in-the-loop) wrapped die 21 bestehenden Service-Methoden und ist in 3-5 Tagen fertig. **#2 Papershift hat am 2026-09 den Pricing-Schock-Pivot gemacht — Core 4→64 EUR (+1500%), Premium 6→96 EUR (+1500%), Professional 144 EUR komplett eliminiert (Stand G2 2026-10-08) — ein kommunikatives Churn-Fenster das Cosmi direkt angreifen kann.** G2-Pricing-Daten (Stand 2026-10-08, `g2.com/products/papershift/pricing`) zeigen die Papershift-Pricing-Umstellung: Core ist von **4 EUR/User-Monat auf 64 EUR/Monat** gewandert, Premium von **6 EUR auf 96 EUR**, der Professional-Tier (144 EUR/Monat mit DATEV/LODAS-Bidirektional) ist **komplett eingestellt** worden. Die prozentualen Steigerungen (+1500%) sind nur plausibel, wenn die alte Per-User-Logik durch neue Paket-Flatrate ersetzt wurde — klassischer "Simplification"-Pivot der Bestandskunden aggressive trifft. Papershift's blog `papershift.com/blog/ki-zur-optimierung-der-personaleinsatzplanung` + `papershift.com/webinare/core-premium-professional` behalten die alten Preis-Narrative — Pricing-Inkonsistenz zwischen Marketing und tatsaechlichem G2-Preisstand ist Indiz fuer Communication-Chaos. **DACH-KMU-Implikationen fuer Cosmi**: (i) **Ex-Papershift-Professional-Kunden** die DATEV/LODAS-Bidirektional + Payroll-Export brauchten sind in Q4 2026 technisch heimatlos — Cosmi-Buchhaltung-W42 hat `finance_recurring_runs`-Ledger + Bank-Feed-Infrastruktur, Cosmi kann DATEV-Export aus `zeiterfassung`-Modul-Sprint vorziehen und positionieren "Cosmi-Payroll-Export fuer ex-Papershift-Professional-Kunden"; (ii) **Capterra/G2-Churn-Welle Q4-2026 fuer Papershift** wird 1-2 Quartale laufen — fuer DACH-KMU-Vertrieb ein konkretes Lead-Gen-Fenster; (iii) **Preis-Vergleich fuer Marketing**: Cosmi-schichten (4 EUR/MA) + zeiterfassung (3 EUR/MA) = **7 EUR/MA** vs. **Papershift Core 64 EUR + Grundgebuehr 39 EUR fuer 10 MA = 10,30 EUR/MA-aequivalent, oder Premium 96 + 39 EUR fuer 10 MA = 13,50 EUR/MA-aequivalent** — Cosmi ist jetzt klar guenstiger im Breakeven-Vergleich und muss nicht mehr nur ueber Cross-Modul-Bundle differenzieren. **Konsequenz fuer Cosmi W44**: (a) Sales-Material-Update "Papershift-Pricing-Pivot-Analyse mit Cosmi-Alternative" als kleiner Sales-Enablement-Sprint, (b) Priorisierung von DATEV/LODAS-Export fuer schichten+zeiterfassung-Kombi als Q1-2027-Sprint-Pflicht (nicht 2026-Q4-Prototyp), (c) Preis-Story W44 Marketing: "4 EUR/MA-Monat fuer Cosmi-Schichten, Papershift 64 EUR/Monat Pauschale, Vergleich siehe G2 2026-10-08". **#3 Ordio hat am 2026-09 + 2026-10 den Nano-AI-Agent als Agentic-UI-im-DACH-Segment produktiviert — und Shyftplan hat ScableOne (Smart-Factory-Software) uebernommen — damit ist das DACH-Agentic-Fenster an zwei Enden geschlossen worden.** Ordio (DE, Koeln) hat im September 2026 (`ordio.com/en/product-updates/september-2026`) sein Nano-AI-Agent um **Cited Web Search** (Feiertage, Mindestlohn, Events in der Naehe mit Quellenverweis) + **In-App-Guide** ("Where do I find this?" mit Direkt-Link zur richtigen Stelle) erweitert. **Nano agiert jetzt als AI-Agent im Chat auf Live-Ordio-Daten** (Shifts fuellen, Routine-Tasks, Fragen) — damit **DACH-Vorreiter bei nativer Agentic-UI** vs. Papershift's statischem KI-HR-Chat. Im Oktober 2026 (`ordio.com/en/product-updates/october-2026`) hat Ordio **Loop** als Referral-Programm mit Partner-Portal + Dashboard + laufender Umsatzbeteiligung gelauncht — PLG-Growth-Pivot nach dem Series-A von Juli 2025 (12 Mio EUR, 3VC/Capnamic/Simon Capital/Wecken). Parallel hat Shyftplan (DE Berlin, Maguar) im **Juli 2026 die Scable AG uebernommen** (`maguar.com/en/news/shyftplan-...-scable`, `shyftplan.com/presseseite/shyftplan-erwirbt-scableone` Juli-August 2026) und integriert **ScableOne Smart-Factory-Software** (Connected Worker, Predictive Maintenance, Shopfloor-Management) in die Workforce-Management-Plattform. **Positionierung**: "Software-Backbone fuer die human-centric Smart Factory". Industriekunden erhalten End-to-End-Flow von Workforce-Planning bis Shopfloor-Execution. **Konsequenz fuer Cosmi-DACH-Positionierung**: (i) **Ordio ist jetzt der schaerfste direkte DACH-KMU-Agentic-Konkurrent** — mehr als Papershift (Chat-only) oder Shyftplan (Enterprise-Shopfloor). Cosmi muss im W44/W45-Marketing-Zyklus klaer kommunizieren was Cosmi-Agentic-Story IST (Cross-Modul-Agent orchestriert Schichten + Buchhaltung + CRM + Vertraege) vs. Ordio-Nano-Agentic-Story (In-Modul-Agent auf Live-Schichten-Daten). (ii) **Shyftplan ist jetzt Enterprise-only-shaped mit Shopfloor-Integration** — Cosmi's 10-200-MA-Zielsegment ist strukturell **Ordio-Konkurrent-geworden**, nicht mehr Shyftplan-Konkurrent. Positioning-Shift W44 Pflicht. (iii) **HERO Software DE Hannover hat 2026-06 HERO AI gelauncht + 2026-09-29 HERO Command (`presse.hero-software.de/hero-command`) + H2-2026 HERO Report** — der W28-rapporte-W43-Vaporware-Vorwurf ist aufgeloest. Fuer Handwerk-KMU-Segment ist HERO Software jetzt der direkt-Agentic-Konkurrent (69 EUR/User mit vollstaendigem AI-Produkt-Stack).

> **Leit-Signal der Woche fuer schichten: fuenf parallele Bewegungen formen den Markt seit W29.** **(a) Planday MCP-Dual-Launch 2026-10-22** definiert den Agentic-AI-Marktbenchmark neu; alle anderen DACH-KMU-Konkurrenten haben jetzt 3-6 Monate Nachhol-Fenster. **(b) Papershift-Pricing-Pivot 2026-09 (Core 4→64, Premium 6→96, Professional eliminiert)** eroeffnet 1-2-Quartal-Churn-Window — direktes Lead-Gen-Fenster fuer Cosmi. **(c) Ordio Nano operationalisiert September-Oktober 2026** macht DACH-KMU-Agentic-Framing Cosmi-Konkurrent-direkt — Cosmi muss "Cross-Modul-Agent" vs. Ordio's "In-Modul-Agent" positionieren. **(d) ArbZG-Reform-Progression 15 Wochen Status-Quo**: Referentenentwurf 18.06.2026 Verbaendeanhoerung Anfang Juli 2026 abgeschlossen, Ressortabstimmung laeuft, **noch kein Kabinettsbeschluss** Stand 2026-10-26 (`table.media/berlin/talk-of-the-town/reform-des-arbeitszeitgesetzes-das-bmas-gibt-einen-engen-rahmen-vor-und-stellt-niemanden-zufrieden`, `eversheds-sutherland.com/de/germany/insights/update-zum-arbeitszeitgesetz-referentenent-wurf-zur-elektronischen-arbeitszeiterfassung`). Erwartet Q4-2026/Q1-2027. **Marketing-Fenster offen**: kein grosser DACH-Schichtplan-Konkurrent hat eine aggressive ArbZG-Reform-Sales-Kampagne gestartet. **(e) Regulatorik-Konvergenz 37 Tage**: **EU AI Act Art. 50 Grace-Period-Ende 2026-12-02** (37 Tage, maschinenlesbare C2PA-Markierung fuer Generative-AI) + **EU Platform Work Directive Umsetzungs-Deadline 2026-12-02** (37 Tage, DE kein nationaler Entwurf — Direkt-Anwendbarkeit droht), **DSK 112. Konferenz 2026-11-26** (31 Tage, Beschaeftigtendatenschutz als Schwerpunkt). **Heute keine neue schichten-Markt-Nachricht im Morning-Pulse** (`daily/2026-10-26-morning.md` ausstehend, letzter Pulse `2026-10-23-evening`), **aber die fuenf Bewegungen sind alle in den letzten 15 Wochen durch `daily/*.md` + `.state/regulation_raw_2026-*.json` + `keepers/*.md` nachvollziehbar**. **Dieser Bericht empfiehlt drei Pflicht-Sprint-Stakes fuer Q4-2026 + Q1-2027: #1 Cosmi-MCP-Server-schichten + Agentic-Positionierungs-Entscheidung, #2 ArbZG-Full-Palette + arbzgMinRestDuration Tenant-Setting mit Pflege/Gastro/Verkehr-Ausnahme + §3/§4/§9-10-Impl, #3 Mock-to-Backend-Konsolidierung employee_availabilities + DACH-Feiertag-Auto + Zuschlags-System — alle drei sind heute strukturelle Cosmi-Luecken, alle drei haben in 3-6 Monaten Marktbeobachtungs-Auswirkung, keine der drei ist heute in einem Sprint-Backlog erkennbar.**

---

## State-of-the-Art

Der DACH-Schichtplanungs-Markt Ende Oktober 2026 ist **vier-spurig** (W29: dreispurig) — die vierte Spur ist seit 2026-10-22 die **Agentic-Marketplace-Connector-Spur** mit Planday als First-Mover und UKG als Enterprise-Parallel-Entrant. Die vier Spuren:

**(1) DACH-KMU-Schichtplan-Spezialisten mit Agentic-UI (NEU in Zyklus 2)**: Ordio Nano (September 2026 Cited-Web-Search + In-App-Guide, Oktober Loop-Referral) + Planday Smart-AI-Rotas + Deputy AI Platform + Papershift KI-Chat (statisch). Ordio differenziert sich als "AI-Agent auf Live-Daten im Chat", Papershift bleibt bei "Chat auf Dokumenten + Personaldaten". Cosmi-Direkt-Konkurrent.

**(2) DACH-KMU-Schichtplan-Spezialisten ohne Agentic-UI**: Crewmeister, Aplano, ShiftJuggler, gastromatic, Shiftbase-DACH — Preis-Krieger-Segment ohne Agentic-Story. Direkte Cosmi-Konkurrenz im preis-sensiblen 5-30-MA-KMU-Segment.

**(3) Enterprise/AI-First-Player mit Shopfloor-Integration (NEU in Zyklus 2 via Shyftplan+ScableOne)**: Shyftplan (jetzt mit ScableOne Smart-Factory-Backbone), Sona (45M USD Series B April 2026 + Forge AI-App-Builder Q1 2026, kumulativ >$100M), Deputy (Deputy AI Platform GA Nov 2025 + Predelo-Partnership operationalisiert 70k shifts/Woche mit 85% Auto-Scheduling), Planday (jetzt mit MCP-Dual-Connectors als "Agentic AI Experience"). 100+ MA Zielsegment, nicht Cosmi-KMU-direkt-Konkurrenz, aber setzt Feature-Benchmarks.

**(4) Agentic-Marketplace-Connector-Spur (NEU seit 2026-10-22)**: Planday (First-in-Workforce 2026-10-22, verifiziert in ChatGPT + Claude Marketplace mit 216+ Early-Access-Kunden), UKG (Beta Claude 2026-10-20, Enterprise), Deputy (Zapier-MCP, nicht offiziell), Papershift (Third-Party-MCP via usefulapi.io, nicht offiziell), Time Doctor (MCP Claude/ChatGPT/Gemini). **Shyftplan + Ordio + Crewmeister + Shiftbase + Sona haben KEINEN offiziellen MCP-Server** — DACH-KMU-Open-Source-ERP-Fenster ist offen.

Cosmi-schichten sitzt heute **architektonisch in Spur (2)** als DACH-KMU-Schichtplan-Modul **ohne Agentic-UI, ohne Verfuegbarkeits-Backend, ohne Zuschlags-Payroll-Integration, ohne DACH-Feiertag-Auto**. Der Modul-Preis von **4 EUR/User-Monat** ist nach Papershift's Pricing-Pivot September 2026 **jetzt klar guenstiger** als Papershift Core 64 EUR Flatrate (fuer 10 MA = 10,30 EUR/MA-aequivalent inkl. 39-EUR-Grundgebuehr) oder Premium 96 EUR (13,50 EUR/MA-aequivalent) — der Preis-Vorteil ist aber **feature-adjusted weiterhin schwach**: Papershift Premium liefert KI-HR-Chat + Auto-Assign + Qualifikations-Matching + Verfuegbarkeits-Backend, Cosmi liefert null davon. Preis-Vergleich gegen Ordio (89-149 EUR/Standort, 10-200 MA DACH, mit Nano-Agentic-UI) bleibt strukturell: Cosmi gewinnt in kleinen KMU (5-15 MA an einem Standort → Cosmi 20-60 EUR, Ordio 89 EUR), verliert in groesseren (50+ MA an einem Standort → Cosmi 200+ EUR, Ordio 89-149 EUR). Preis-Vergleich gegen Crewmeister (Standard-Bundle 5,20 EUR/User, ohne AI, nach Ablauf 30%-Rabatt 2026-06-24) + Aplano (0.50-4.50 EUR/MA, mit DACH-Feiertag-Auto) bleibt Preis-nachteilig fuer Cosmi im Low-End ohne AI-Vorsprung — Cross-Modul-Bundle-Story muss weiter das Alleinstellungs-Argument sein.

Fuenf strukturelle Veraenderungen seit W29 verschaerfen den Markt:

**(a) Planday MCP-Dual-Launch 2026-10-22 definiert den Agentic-Marktbenchmark neu**. Verifizierte Connectors in **ChatGPT (OpenAI Apps/Connectors)** + **Claude (Anthropic Marketplace Connectors)** gleichzeitig gelauncht. **216+ Kunden** haben in <48h ihre Planday-Accounts verbunden. Early-Access global kostenfrei, Bank-/Payroll-/NI-Daten explizit ausgeschlossen, existing RBAC gilt. **Use-Case-Beispiel**: Gastro-Manager fragt "Wie beeinflussen Buchungen + Wetter die Schichtdeckung?" — Connector kombiniert Planday-Rota mit externem Kontext + liefert actionable recommendations. **DACH-Fach-Presse**: `ad-hoc-news.de` berichtet am 2026-10-22 auf Deutsch mit Gastro/Hotel-Fokus. **UKG parallel am 2026-10-20** mit Beta-Claude-Integration gelauncht (Enterprise-WFM, `natlawreview.com/press-releases/ukg-claude-makes-ai-work-beyond-chat`). **MCP-Spec-Update 2026-07-28** (stateless, multi-round-trip, authorization-hardening, extensions-framework, `blog.modelcontextprotocol.io/posts/2026-07-28`) macht Cloudflare-Worker-Edge-Hosting trivial — Vendor-MCP-Server sind jetzt 1-2-Wochen-Sprints statt Monate. **Konsequenz fuer Cosmi**: W33-MCP-Keeper (20 Wochen ueberfaellig, in buchhaltung-W42 + helpdesk-W39 + formulare-W40 + vertraege-W41 + rapporte-W43 immer wieder gelistet) muss W45-W47 produktiviert werden. Fuer schichten konkret: 3 Read-Tools (`list_shifts`, `check_arbzg_compliance`, `list_swap_requests`) + 2 Write-Tools (`create_shift`, `assign_employee` mit human-in-the-loop) wrapped die 21 bestehenden Service-Methoden. Daneben wrapped Cosmi-crm-Server + Cosmi-rapporte-Server + Cosmi-helpdesk-Server + Cosmi-buchhaltung-Server das Cross-Modul-USP — den **Papershift nicht liefern kann weil er nur Schichten weiss, Ordio nicht liefern kann weil er nur Workforce weiss, Shyftplan nicht liefern kann weil er Shopfloor-fokussiert**.

**(b) Papershift-Pricing-Pivot September 2026 oeffnet 1-2-Quartal-Churn-Window**. G2-Pricing-Daten Stand 2026-10-08 (`g2.com/products/papershift/pricing`) zeigen: Core von 4 EUR/MA/Monat auf **64 EUR Pauschale/Monat** (+1500% vs. Per-User-Vergleich), Premium von 6 EUR/MA auf **96 EUR Pauschale/Monat** (+1500%), **Professional 144 EUR komplett eliminiert**. Grundgebuehr 39 EUR/Monat bleibt. DATEV/LODAS-Bidirektional-Feature war Professional-exklusiv — jetzt technisch heimatlos. **Papershift-Blog `papershift.com/webinare/core-premium-professional`** behaelt die alten Preis-Narrative — Pricing-Communications-Chaos ist Churn-Beschleuniger. **Capterra/G2-Review-Welle Q4-2026** fuer Papershift erwartet (89%-User-Zufriedenheit-im-Support-Praemie wird fallen). **Cosmi-Lead-Gen-Aufhaenger W44-W45**: (i) Sales-Material-Update "Papershift-Pricing-Pivot-Analyse mit Cosmi-Alternative" (1-Wochen-Marketing-Sprint), (ii) DATEV/LODAS-Export-Prototyp fuer schichten+zeiterfassung vorziehen auf Q4-2026 (statt Q1-2027), (iii) Preis-Vergleichs-Marketing-Material: "Cosmi-Schichten 4 EUR/MA, Papershift 64 EUR Pauschale/Monat Core, Vergleich siehe G2 2026-10-08".

**(c) Ordio Nano operationalisiert September-Oktober 2026 → DACH-KMU-Agentic-Konkurrent**. Ordio (DE Koeln, 12M Series A Juli 2025) hat am **2026-09** (`ordio.com/en/product-updates/september-2026`) Nano um **Cited Web Search** (Feiertage, Mindestlohn, Events in der Naehe mit Quellenverweis) + **In-App-Guide** ("Where do I find this?") erweitert — Nano ist jetzt **AI-Agent im Chat auf Live-Ordio-Daten** (Shifts fuellen, Routine-Tasks, Fragen beantworten). Am **2026-10** Ordio Loop als Referral-Programm mit Partner-Portal + Dashboard + laufender Umsatzbeteiligung — PLG-Growth-Pivot operationalisiert. **Positionierung**: Ordio nennt Nano explizit "AI Agent, der im Chat auf Live-Daten arbeitet" — DACH-Vorreiter bei nativer Agentic-UI vs. Papershift's statischem KI-HR-Chat (`ki-syndikat.de/tools/papershift`). **Konsequenz fuer Cosmi-Positionierung**: Ordio ist jetzt direkt-Konkurrent im 10-200-MA-DACH-Segment statt Nachbar. W44-Marketing-Pflicht: "Cross-Modul-Agent (Cosmi) vs. In-Modul-Agent (Ordio)" als Positioning-Statement — Papershift's Chat kann nur innerhalb Schichten antworten, Ordio's Nano kann nur innerhalb Schichten agieren, Cosmi's MCP-Server orchestriert alle Module parallel.

**(d) Shyftplan+ScableOne-Uebernahme Juli-August 2026 verschiebt Enterprise-DACH-Positionierung**. Maguar-Portfolio-Firma Shyftplan (DE Berlin) integriert **ScableOne (Smart-Factory-Software, Connected Worker, Predictive Maintenance, Shopfloor-Management)** in die Workforce-Management-Plattform. Positionierung: **"Software-Backbone fuer die human-centric Smart Factory"** (`maguar.com/en/news/shyftplan-...-scable`, `shyftplan.com/presseseite/shyftplan-erwirbt-scableone`). Industriekunden erhalten End-to-End-Flow von Workforce-Planning bis zur taeglichen Shopfloor-Execution. **shyftconnect** als Event-Driven-Standard-Interface zu SAP SuccessFactors + SAP BTP + Workday HCM + Personio + Staffbase + WePlan live expansioniert. **Shyftskills** (Qualifikations-/Skill-Matching mit expiring-certificate warnings, hierarchical inheritance, audit log, `developer.shyftplan.com/reference/getapiv1qualifications`) als API live. **Konsequenz fuer Cosmi**: Shyftplan ist jetzt Enterprise-only mit Shopfloor-Fokus — Cosmi 10-200-MA-Zielsegment ist nicht mehr Shyftplan-Konkurrent, sondern **Ordio-Konkurrent-geworden**. Positioning-Shift W44 Pflicht. Qualifikations-Matching-Lektion: **Shyftplan hat ESCO-ontology-mapping im Backend** — Cosmi sollte interne Skills-Taxonomie frueh zu **ESCO-Codes** (~3000 Occupations, 13000+ Skills, 27 Sprachen, EU-finanziert, `data.europa.eu/esco`) mappen, damit MCP-Server-Queries wie "find a forklift-certified employee for Saturday morning" (ESCO-Code 83442.1.4 "Industrial-Truck-Operator") in Zukunft out-of-the-box funktionieren.

**(e) ArbZG-Reform-Progression + 37-Tage-Regulatorik-Konvergenz (NEU in Zyklus 2)**. Der BMAS-Referentenentwurf 18.06.2026 unter BM Baerbel Bas (`eversheds-sutherland.com`, `clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026`, `betriebsratspraxis24`, `table.media`) ist in **15 Wochen Status-Quo** verblieben: **Verbaendeanhoerung-Frist Anfang Juli 2026 abgelaufen**, breite Kritik (BDA zu eng, DGB/Verdi zu wenig Schutz, Koalitionspartner zu wenig Flexibilitaet, `table.media`), Ressortabstimmung laeuft, **noch kein Kabinettsbeschluss, keine Regierungsvorlage, keine Bundestags-Lesung, kein Bundesrats-Durchgang** Stand 2026-10-26 (`der-arbeitszeitrechner.de`, `factorialhr.de`, `hrtime.de`). Inkrafttreten erwartet **Q4-2026 / Q1-2027** (Kabinett moeglich), fruehestens Q2-2027 (Bundestag). **§16-Kernregelung** (bereits in W28/W29 dokumentiert): elektronische Erfassung von Beginn/Ende/Dauer taggleich, Bussgeld-Rahmen im RefE **bis 30.000 EUR** (einige Konsolidierungs-Quellen diskutierten 50.000 EUR, final offen, `hrtime.de`, `zeiterfassung-fdm.de`), Uebergangsfristen 1a >250 MA / 2a 50-249 MA / 5a 10-49 MA / dauerhaft <10 MA ausgenommen. **§5-Aenderungen** (fuer Cosmi NEU-relevant seit W29): Ruhezeit-Verkuerzung in Branchenausnahmen **mit unmittelbarem Ausgleich** (Krankenhaus/Pflege/Gastro/Verkehr/Rundfunk/Landwirtschaft, 10h statt 11h), Tarifvertrag kann 11h ganz aufheben mit hoeherem Gesundheitsschutz. **§3-Reform**: Wochenbetrachtung statt Tagesbetrachtung, 48h/Woche EU-Vorgabe nur per Tarifvertrag. **Kein grosser DACH-Schichtplan-Konkurrent** hat eine aggressive ArbZG-Reform-Sales-Kampagne gestartet im Fenster W29→W44 — Shiftbase/Clockin publizieren Erklaer-Artikel (`shiftbase.com/de/blog/arbeitszeitreform-arbeitgeber`, `clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026`), aber keine Trigger-Kampagne. **Marketing-Fenster offen** fuer Cosmi.

**Zusaetzliche Regulatorik-Deadlines <90 Tage** ab 2026-10-26:

- **2026-12-02 (37 Tage) — EU AI Act Art. 50 Grace-Period-Ende**: maschinenlesbare C2PA-Markierung fuer Generative-AI-Content (Baker Botts, `bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live`, EC Digital Strategy `digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems`). Falls Cosmi-schichten AI-Auto-Assign shipped (W44-Pick-Entscheidung): **Disclosure-Layer plus C2PA-Watermark Pflicht**. Auch falls nur AI-Agent-im-MCP-Server (siehe #1): Antworten vom AI-Assistant brauchen Markierung. Cosmi-weiter Compliance-Sprint (helpdesk-W39 + rapporte-W43 + vertraege-W41 + buchhaltung-W42 haben alle das gleiche Pattern): **ai_disclosure-Table** fuer Audit-Log, **ai_content_watermark**-Service fuer C2PA-Marking.
- **2026-12-02 (37 Tage) — EU Platform Work Directive Umsetzungsfrist DE**: Bundesrat hat am 2026-09-25 die Bundesregierung zur zuegigen Umsetzung aufgefordert (DLA Piper, `knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/germany-moves-forward-on-transposing-the-eu-platform-work-directive`). **Kein nationaler Entwurf** Stand 2026-10-26 → Direkt-Anwendbarkeit nach 2026-12-02 moeglich. Cosmi-schichten tangiert: wenn Mandanten plattformartig Freelancer/Minijob/geringfuegig Beschaeftigte koordinieren, droht Beschaeftigungsvermutung → Audit-Pflicht. Cosmi muss unterstuetzen: `shift_worker_classification`-Feld (regular-employee/freelancer/platform-worker), Audit-Logging bei Zuweisung ausserhalb des regulaeren Beschaeftigungsverhaeltnisses.
- **2026-11-26 (31 Tage) — 112. DSK-Konferenz**: Beschaeftigtendatenschutz als Schwerpunkt (DSK-Zwischenkonferenz 2026-09-23 bis 09-25 hat das aufbereitet, `stiftungdatenschutz`, `lda.brandenburg.de`). Erwartbare Beschluesse zu HR/Workforce-GPS, AI-Auto-Assign-Transparenz, BDSG-§26-Nachwirkung. **BAG 8 AZR 209/21 Nachwirkung** (08.05.2025): §26 Abs. 1 Satz 1 BDSG **nicht mehr als eigenstaendige Rechtsgrundlage** anwendbar; Arbeitgeber muessen Verarbeitungen primaer auf Art. 6/9 DSGVO (ggf. Art. 88 i.V.m. Betriebsvereinbarung) stuetzen (`anwalt.de/rechtstipps/datenschutz-im-job-2026-ueberwachung-kontrolle-und-schadensersatz-282747`, `dsgvo-quiz.de`). Cosmi muss im Verzeichnis von Verarbeitungstaetigkeiten die Betriebsvereinbarungs-Grundlage je Mandant dokumentieren koennen.

### Top-Konkurrenten — Veraenderungen W29→W44 (Delta-Report)

**1. Papershift (DE Karlsruhe, threat: HIGH→MEDIUM-HIGH — Pricing-Pivot-Risiko)**

Papershift bleibt DE-Karlsruhe-Schichtplan-KMU-Marktfuehrer mit PUR/Heise-Award 2026 + 89% User-Zufriedenheit im Support, aber **Pricing-Pivot September 2026** schwaecht die Marktposition.

- **PRICING-PIVOT (NEU 2026-09)**: Core 4 EUR → **64 EUR Pauschale/Monat**, Premium 6 EUR → **96 EUR Pauschale/Monat**, **Professional 144 EUR komplett eliminiert**. Grundgebuehr 39 EUR/Monat bleibt. Pricing-Communications-Chaos — Blog `papershift.com/webinare/core-premium-professional` behaelt alte Narrative, G2 Stand 2026-10-08 zeigt neue Preise.
- **KI-HR-Chat weiter ausgebaut (H2 2026)**: Rollen- und Berechtigungs-Logik respektiert Dokumente + Personalakten. Keine Deep-Optimization-Engine, keine Agentic-Agent-Entwicklung.
- **DATEV/LODAS-Export war Professional-exklusiv** — jetzt technisch heimatlos nach Professional-Discontinuation. Churn-Window fuer ex-Papershift-Professional-Kunden.
- **Kein MCP-Server, kein offizieller Claude/ChatGPT-Connector** — Third-Party-MCP via usefulapi.io (`glama.ai/mcp/connectors/io.usefulapi/papershift`) ist nicht Vendor-gehostet.
- **Pricing (Stand 2026-10-08)**: Core **64 EUR Pauschale**, Premium **96 EUR Pauschale**, Grundgebuehr 39 EUR. Professional eliminated. 14-Tage-Trial.
- **Gap zu Cosmi**: KI-HR-Chat (Marktbenchmark, Cosmi 0), DATEV/LODAS-Export-Legacy-Kunden-Transition (unklar).
- **Strategischer Hinweis (NEU in Zyklus 2)**: **Papershift's Pricing-Pivot ist Cosmi's wichtigstes Lead-Gen-Fenster Q4-2026**. (i) Sales-Material "Papershift-Pricing-Pivot-Analyse" (1-Wochen-Sprint W44), (ii) DATEV/LODAS-Export-Prototyp vorziehen Q4-2026, (iii) Preis-Marketing: "Cosmi-Schichten 4 EUR/MA, Papershift Core 64 EUR Pauschale, Vergleich 2026-10-08".

**2. Ordio (DE Koeln, threat: HIGH→**HIGH-STEIGEND** — direkter DACH-KMU-Agentic-Konkurrent)**

Ordio ist seit Zyklus 2 der **wichtigste direkte DACH-KMU-Agentic-Konkurrent** — mehr als Papershift (nur Chat), mehr als Shyftplan (Enterprise-Shopfloor), mehr als Crewmeister (keine AI).

- **Nano AI-Agent operationalisiert September-Oktober 2026 (NEU)**: September-Update bringt **Cited Web Search** (Feiertage, Mindestlohn, Events-in-der-Naehe mit Quellenverweis) + **In-App-Guide** ("Where do I find this?" mit Direkt-Link). Nano agiert jetzt als **AI-Agent im Chat auf Live-Ordio-Daten** (Shifts fuellen, Routine-Tasks, Fragen) — DACH-Vorreiter bei nativer Agentic-UI (`ordio.com/en/product-updates/september-2026`).
- **Ordio Loop (NEU 2026-10)**: Referral-Programm live mit Partner-Portal + Dashboard + Links + laufender Umsatzbeteiligung — PLG-Growth-Pivot nach Series A 12 Mio EUR Juli 2025 (3VC/Capnamic/Simon Capital/Wecken).
- **Branchen-Fokus**: Gastro/Retail/Handwerk/Pflege/Kultur. 10-200 MA/Standort.
- **Location-basiertes Pricing**: Starter 89, Plus 129, Pro 149 EUR/Standort/Monat. Flat unabhaengig von MA-Anzahl.
- **Pain-Points OMR 2026 (unveraendert)**: Location-basiertes Pricing teuer fuer Multi-Site-KMU, Feature-Breite ausserhalb Kern-Schichtplan schwaecher als Papershift.
- **Gap zu Cosmi**: Nano-Agentic-UI (DACH-Marktbenchmark), In-Modul-Chat-Agent auf Live-Daten, Cited-Web-Search-Integration, PLG-Referral-Programm.
- **Strategischer Hinweis (NEU)**: **Ordio ist Cosmi's wichtigster direkter DACH-KMU-Konkurrent in Zyklus 2** — der 15-Wochen-Delta zu W29 (wo Ordio als "einer von vier" gelistet war) ist strukturell. Cosmi-Positioning muss W44 pivotieren: Cross-Modul-Agent vs. In-Modul-Agent als Marketing-Zentrum.

**3. Shyftplan (DE Berlin, Maguar, threat: MEDIUM→LOW — nicht mehr Cosmi-direkt-Zielsegment)**

Shyftplan hat sich seit Juli 2026 Enterprise-only mit Shopfloor-Fokus positioniert — Cosmi 10-200-MA-Zielsegment ist nicht mehr direkt-Konkurrent.

- **ScableOne-Uebernahme Juli-August 2026 (NEU)**: Maguar-Portfolio-Firma Shyftplan integriert **ScableOne Smart-Factory-Software** (Connected Worker, Predictive Maintenance, Shopfloor-Management, `maguar.com/en/news/shyftplan-...-scable`). Positionierung: "Software-Backbone fuer die human-centric Smart Factory". End-to-End-Flow Workforce-Planning → Shopfloor-Execution.
- **shyftconnect expansion (NEU H2 2026)**: Event-driven Datenflüsse zu SAP SuccessFactors + SAP BTP + Workday HCM + Personio + Staffbase + WePlan — Intelligent Event Processing, Auto-Retry, Datenintegritaet.
- **Shyftskills live (NEU)**: ESCO-ontology-adjacent Qualifikations-Matching mit expiring-certificate warnings + hierarchical inheritance + audit log, API `v1/qualifications` (`developer.shyftplan.com/reference/getapiv1qualifications`).
- **AI-Optimierung mit 20+ Faktoren**: unveraendert — Qualifikationen, Verfuegbarkeiten, Maschinen-Auslastung, Vertrags-Verfuegbarkeit, Planungs-Regeln, Praeferenzen, Fairness.
- **Kein MCP-Server kommuniziert** — moeglicherweise ueber SAP-BTP-Flow technisch denkbar.
- **Pricing**: unveraendert Minimum 700 EUR/Monat Enterprise.
- **Gap zu Cosmi**: ScableOne-Smart-Factory-Integration, Shyftskills-API, SAP-verifizierte Integration, shyftconnect-Event-Driven-Interface.
- **Strategischer Hinweis (REVISIT)**: **Shyftplan ist nicht mehr Cosmi-Direkt-Konkurrent** — Positioning W44: "wir sind nicht Shyftplan Enterprise, wir sind Agent-first fuer 10-200 MA". Shyftskills-ESCO-Learning uebernehmbar fuer Cosmi's zukuenftige employee_qualifications-Table (Q1-2027).

**4. Planday (DK, Xero, threat: MEDIUM→**HIGH-STEIGEND** — Agentic-Marktbenchmark First-Mover)**

Planday hat am **2026-10-22 den definierenden Produkt-Move der gesamten W29→W44-Phase** gemacht.

- **MCP-Dual-Launch 2026-10-22 (NEU, kritisch)**: Verifizierte Connectors **in ChatGPT (OpenAI Apps/Connectors) + Claude (Anthropic Marketplace Connectors)** gleichzeitig — First-in-Workforce. **216+ Kunden** in Early-Access verbunden (`thehotelmagazine.co.uk/planday-brings-context-aware-workforce-scheduling-to-chatgpt-and-claude`, `claude.com/marketplace/connectors/planday`, `help.planday.com/en/articles/776982-how-to-connect-planday-to-claude`, `ad-hoc-news.de/wissenschaft/planday-chatgpt-und-claude-entwerfen-schichtplaene-fuer-gastronomie-und-hotels/70404162`). Early-Access global kostenfrei. Bank/Payroll/NI-Daten exclusively excluded. Existing RBAC respected.
- **Xerocon London 2026 "Agentic Era" (NEU)**: Xero positioniert sich platform-weit als "AI-native financial OS" — Planday ist Pfeiler dieser Strategie neben XeroForce (Agent-Builder, 2026-05-14). **Deputy ersetzt Planday-AU** zum 2024-09-30 ab, Planday fokussiert Europa (`blog.xero.com/news-events/xero-retire-planday-au-partnership-deputy`).
- **"Agentic AI Experience" Marketing (NEU)**: aktive Roadmap-Kommunikation "industry's first truly Agentic AI experience" fuer Schicht-Management + MCP-Launch 2026-10-22 als Erfuellung.
- **Winter/Spring + Autumn 2026 Updates** (`help.planday.com/en/articles/621960-product-updates-winter-and-spring-2026`): neue Performance Overview (welche MA + Tage generieren meisten Umsatz), verbesserte Timesheet-Break/Supplement-Management.
- **Smart AI-powered Rotas Intelligent-Shift-Assignment Beta**: ranks candidates per shift using availability + contracted hours + working-time rules.
- **Pricing**: ab $2/User-Monat Essentials, Enterprise-Plan noetig fuer volle Palette.
- **Gap zu Cosmi**: MCP-Dual-Connector (DACH-Marktbenchmark seit 2026-10-22), Agentic-AI-Positioning, Xero-Rueckenhalt, Personio-Marketplace-Standard-Integration.
- **Strategischer Hinweis (ESKALATION)**: **Planday-MCP-Launch 2026-10-22 ist der schichten-W44-Kernsignal** — Cosmi muss MCP-Roadmap-Statement W44 kommunizieren. Planday's 216+-Early-Access-Kunden sind der Zahlen-Benchmark den DACH-KMU-Buyer jetzt erwarten.

**5. Crewmeister (DE Muenchen, einrichter.de, threat: MEDIUM — Preis-Krieger ohne AI)**

Crewmeister bleibt DACH-KMU-Zeit-+Schichtplan-Preis-Krieger ohne AI-Entwicklung.

- **30%-Starter-Rabatt-Kampagne lief bis 2026-06-24 (Nachwirkung)**: Rueckkehr zu Regulaerpreisen seit 2026-06-13 (Go 1,50 EUR, Easy 2,00 EUR, Pro 3,00 EUR p.MA/Monat Jahreszahlung; monatlich +30%, `crewmeister.com/de/angebote`). Keine Fortsetzung der Rabatt-Kampagne im Fenster H2 2026.
- **Keine signifikanten Produkt-Launches im Fenster** W29→W44.
- **Kein AI-Feature 2026** — Fokus bleibt Preis + GPS-2m-Genauigkeit (DSGVO-konform via punktuelle Erfassung).
- **Zeiterfassungspflicht-Marketing**: `crewmeister.com/de/magazin/zeiterfassungspflicht-2026-was-sie-wissen-muessen` als Lead-Magnet unveraendert.
- **Pricing**: Zeit ab 1.50 EUR/User, Schicht ab 2 EUR/User, DATEV 0.60 EUR/User. Standard-Bundle ab 5.20 EUR/User/Monat.
- **Gap zu Cosmi (unveraendert)**: Preis-Aggressivitaet, GPS-2m-Genauigkeits-Marketing, native iOS/Android-Handschuh-Bedien-Optimierung, DATEV-CSV-Export.
- **Strategischer Hinweis**: **Crewmeister ist nicht mehr der schaerfste Preis-Konkurrent** — Papershift's Pricing-Pivot auf 64 EUR Pauschale hat die Preis-Landschaft neu geformt. Cosmi's Cross-Modul-Bundle-Story bleibt der Haupt-Hebel vs. Crewmeister.

**6. Aplano (DE, threat: LOW-MEDIUM — Preis-Krieger-Low-End ohne Entwicklung)**

Aplano bleibt DE-Cloud-Schichtplan mit aggressivem Core-Pricing (0.50 EUR/MA), monatlich kuendbar, DACH-Feiertag-Auto DE/AT/CH im Basic. **Keine signifikanten Produkt-Launches W29→W44**.

- **FinanzNachrichten-Mitteilung Juli 2026**: "Aplano vereint digitale Dienstplanung + Zeiterfassung in einer Software" — reiner Marketing-Push (`finanznachrichten.de/nachrichten-2026-07/69074208`).
- **Keine neuen JArbSchG-Features gefunden**, keine Agentic-Entwicklung.
- **Capterra 4.8/5 (113 Reviews), OMR 4.7/5 (206 Reviews)** — bleibt dominant im Low-End.
- **Pricing (unveraendert)**: Core 0.50 EUR/MA/Monat, Basic 2 EUR, Pro 4.50 EUR.
- **Gap zu Cosmi**: Preis-Aggressivitaet Core 0.50 EUR (8x guenstiger als Cosmi), DACH-Feiertag-Auto im Basic.

**7. ShiftJuggler (DE Berlin, threat: LOW-MEDIUM — Content-Marketing ohne Produkt-Signal)**

Keine Produkt-/Pricing-Launches W29→W44. ShiftJuggler positioniert sich mit Rechts-Content (`shiftjuggler.com/wissen/rechtsthemen/arbeitszeitgesetz`) — aber die kommerziell relevanten ArbZG-Reform-Kampagnen laufen bei Konkurrenten (Shiftbase/Clockin/Clockodo).

- **DACH-Feiertag-Auto DE/AT/CH mit Bundeslaender/Kantonen** — unveraendert Marktbenchmark.
- **ArbZG-Reform-Content ja, aber keine Sales-Trigger-Kampagne** — Marketing-Fenster bleibt offen fuer Cosmi.

**8. HERO Software (DE Hannover, threat: HIGH-STEIGEND fuer Handwerk-Vertical)**

**W28-rapporte-Vaporware-Vorwurf aufgeloest**. HERO liefert jetzt vollstaendige AI-Produktwelt fuer Handwerk-KMU.

- **HERO AI Produktwelt gelauncht Juni 2026 (NEU)**: `hero-software.de/ueber-uns/presse/hero-ai-launch` — konsolidiertes AI-Branding.
- **HERO Voice seit Mai 2026 live**: KI-Telefonassistent, Call-Dokumentation in HERO.
- **HERO Command Launch 2026-09-29 (NEU, bestaetigt)**: KI-Assistent fuer Bueroadmin, erstellt Angebots-Drafts, Projekte, Kontakte, Dokumente per Command (`presse.hero-software.de/hero-command`, `photovoltaik.eu/planung/hero-command-ki-feature-fuer-bueroaufgaben-im-handwerk`, `fliesenundplatten.de/hero-command-neues-ki-feature-fuer-die-betriebssoftware-07102026`).
- **HERO Report Launch H2 2026 (NEU)**: Monteure diktieren Baustellen-Reports per Smartphone-Voice, Software erstellt strukturierte Doku.
- **Pricing**: 69 EUR/User unveraendert.
- **Gap zu Cosmi**: AI-Agent-Suite fuer Handwerk-Vertical, Voice-Rapport-Live, Command-fuer-Angebotserstellung.
- **Strategischer Hinweis (NEU)**: **HERO Software ist jetzt echter AI-Benchmark im Handwerk-Vertical** — W29-Positionierung "HERO Report + Command als Vaporware-Fenster offen" ist obsolet. Cosmi-Handwerk-KMU-Positionierung muss W44 ueberdenken. Preis-Vergleich bleibt Cosmi-Vorteil (Cosmi-Modul-Bundle ~25 EUR/User vs. HERO 69 EUR/User).

**9. Deputy (AU/US, threat: MEDIUM — AI-Platform operationalisiert)**

- **Deputy AI Platform GA Nov 2025 operationalisiert H2 2026**: 1 Billion Shifts scheduled using Deputy, AI making frontline work efficient.
- **Predelo-Partnership (exklusiv weltweit)**: Im Fenster weiter skaliert — nationaler US-Kaffee-Konzern wickelt 70.000+ Shifts/Woche ab mit **85% Auto-Scheduling-Anteil**. Benchmark den DACH-Markt noch nicht erreicht.
- **Xero-Partnership Australien** (ersetzt Planday-AU, 25M USD Minority-Investment).
- **Zapier-hosted MCP** (`zapier.com/mcp/deputy`) — nicht offizieller Vendor-MCP.
- **Pricing**: Core 6.50 USD/User, Pro 9 USD/User, Add-Ons.
- **Gap zu Cosmi**: Deputy AI Agent, Predelo-Partnership-Pattern (85% Auto-Scheduling-Benchmark).

**10. Sona (UK/US, threat: NEW/LOW-MEDIUM — Series-B-Momentum)**

- **Series B $45M April 2026 (bestaetigt, operationalisiert)**: Led by N47 + Felicis/Northzone/Gradient. Kumulativ >$100M.
- **Forge AI-App-Builder GA Q1 2026**: Enterprise-Kunden bauen Custom-Software auf Sona-Daten.
- **Fokus H2 2026**: US-Expansion mit Series-B-Kapital. Keine spezifischen DACH-Produkt-Signale.
- **Gap zu Cosmi**: Forge AI-App-Builder-Pattern, vertikale Voll-Integration.

**11. Connecteam (IL/US, threat: MEDIUM — Pipeline-reich H2 2026)**

- **Shift Swaps + Split-Shift Scheduling (2026-10-04 NEU)**: Multi-Working-Hour-Ranges pro Tag. Relevante DACH-Features fuer Gastro/Retail.
- **Break & Timesheet Controls (2026-10-04 NEU)**: flexible Pausenregeln, User-spezifische Policies, Auto-End Paid Breaks, Mobile Issue Details.
- **Signing Order Multi-Signer Documents (2026-10-04 NEU)**.
- **Onboarding Notifications + Default Rules Control (2026-09-06 NEU)**.
- **Pricing stabil**: 29/49/99 USD/Monat Basic/Advanced/Expert first 30 users (`releases.connecteam.com`).
- **Keine DACH-Lokalisierung oder DATEV-Integration**.

**12. 7shifts (CA Saskatoon, threat: LOW im DACH, HIGH als ML-Pattern)**

- **Employee Training GA September 2026 (NEU)**: Premium-Plan. AI-Feature: SOPs/Menues/Handbuecher → strukturierte Kurse + Quizzes (Matching, Ordering, Short Answer) per LLM.
- **Pricing unveraendert**: Comp Free (bis 15 MA/1 Location), Essentials 39.99 USD, Pro 89.99 USD, Premium 149.99 USD.
- **308 Mitarbeiter weltweit** (Stand Maerz 2026).
- **Keine DACH-Expansion**.

**13. gastromatic (DE Mainz, threat: LOW-MEDIUM — DACH-Gastro-Fokus)**

- **Digitale Personalakte ab November 2026 im Starter-Paket (NEU)**: bisher Add-on/Professional. Reduziert Add-on-Pricing-Overhead-Kritik.
- **Pricing-Logik variiert**: 69,50 EUR Starter-Flatrate ODER 6,95-7,00 EUR p.MA. Add-on-Komplexitaet bleibt Reibungspunkt.
- **Personio-Integration unidirektional/limitiert** (identische Attributnamen erforderlich) — strukturelle Schwaeche vs. Shyftplan/Papershift.
- **Keine neue AI-Feature-Ankuendigung**.

### MCP (Model Context Protocol) — Workforce-Landscape Stand 2026-10-26

| Vendor | Status | Quelle |
|---|---|---|
| **Planday** | 🟢 Offiziell, verifiziert ChatGPT + Claude Marketplace (2026-10-22) | thehotelmagazine.co.uk, claude.com/marketplace |
| **UKG** | 🟢 Beta Claude Integration (2026-10-20, Enterprise) | natlawreview.com |
| **Deputy** | 🟡 Zapier-hosted (nicht offiziell) | zapier.com/mcp/deputy |
| **Papershift** | 🟡 Third-Party via usefulapi.io (nicht offiziell) | glama.ai/mcp/connectors/io.usefulapi/papershift |
| **Time Doctor** | 🟢 MCP Claude/ChatGPT/Gemini | timedoctor.com/blog |
| **G-P (Globalization Partners)** | 🟢 MCP global employment data | globalization-partners.com |
| **Toggl/Clockify/Harvest** | 🟢 H1 2026 (vorherige rapporte-W43-Dokumentation) | — |
| **Shyftplan, Ordio, Crewmeister, Shiftbase, Sona, HERO, gastromatic** | 🔴 KEIN offizieller MCP | — |
| **DATEV, Personio** | 🔴 KEIN offizieller MCP | — |

**DACH-KMU-ERP-Open-Source-Fenster**: Shyftplan + Ordio + Crewmeister + Shiftbase + Sona + HERO + gastromatic haben alle noch keinen offiziellen Vendor-MCP-Server. Cosmi als Open-Source-DACH-ERP-Kandidat kann First-Mover-Position einnehmen.

---

## Cosmi-IST-Stand

### Backend `backend/internal/schichten/` (6 Prod-Files, 3832 LOC, Coverage ~45%)

**Veraenderung W29→W44**: 7→6 Prod-Files (helfers consolidated nicht aufgesplittet), Prod-LOC 3155→3832 (+677 +21%), Test-LOC 2913→5826 (+2913 +100%), Test-Files 4→5, Test-Ratio 48%→60% (W29-Pick #R2 "40% Referenz-Ziel" uebertroffen). **Flache Package-Struktur unveraendert** — kein neues Sub-Package `availability/` / `qualifications/` / `surcharges/` / `auto_assign/` / `payroll/` erstellt (anders als buchhaltung-W42 wo `banking/` + `dashboard/` + `expense/` + `recurring/` + `quote/` entstanden).

**Prod-Files (Stand 2026-10-26)**:

- `errors.go` **22 LOC** (W29: 15, +7, +47%): 3 neue Error-Sentinels (`ErrJArbSchGNightWork`, `ErrJArbSchGDailyHours`, `ErrJArbSchGWeekend` auf Zeilen 19-21).
- `models.go` **91 LOC** (unveraendert).
- `repository.go` **82 LOC** (W29: 68, +14, +20%): neue Repository-Interface-Methoden fuer ArbZG-Lookups (`LatestShiftEndBeforeForEmployee`, `EarliestShiftStartAfterForEmployee`, `IsMinorEmployee`).
- `postgres_repository.go` **844 LOC** (W29: 721, +123, +17%): Implementations fuer `LatestShiftEndBeforeForEmployee` + `EarliestShiftStartAfterForEmployee` + `IsMinorEmployee` + Assignment-Lock-Pattern-Erweiterungen fuer Concurrency-Safety.
- `service.go` **877 LOC** (W29: 736, +141, +19%): JArbSchG-Konstanten (`jarbschgEarliestStartHour=6`, `jarbschgLatestEndHour=20`, `jarbschgMaxShiftDuration`) auf Zeilen 16-40, `jarbschgLocation()`-Helper (Europe/Berlin-locked per Kommentar Zeile 33-34), `validateMinorProtection` auf Zeilen 816-837 (calls `IsMinorEmployee`, dann `checkMinorShiftLimits`), `checkMinorShiftLimits` auf Zeilen 839-876 (drei JArbSchG-Rules: §16/§17 Sa/So-Verbot auf Zeile 860, §14 Nachtarbeit-Verbot 06:00-20:00 auf Zeilen 863-865, §8 max 8h auf Zeile 868). **`arbzgMinRestDuration = 11 * time.Hour` bleibt Konstante auf Zeile 14** (W29-Pick #2 nicht geliefert). `validateRestPeriod` von public zu private extrahiert.

**Test-Files (Stand 2026-10-26)**:

- `service_test.go` **1694 LOC** (W29: 1430, +264, +18%): JArbSchG-Coverage, Minor-Protection-Tests.
- `postgres_repository_test.go` **1502 LOC** (NEU seit W29): comprehensive CRUD + ArbZG-Lookups + Swap-Request-Coverage (commit `f231449b` 2026-08-19).
- `tenant_write_test.go` **890 LOC** (NEU seit W29): Tenant-Isolation + Cross-Tenant-Reject (commit `a133ebd2` 2026-07-28).
- `assignment_lock_test.go` **787 LOC** (NEU seit W29): Shift/Employee-Dual-Assignment-Lock-Coverage (commit `1d24373b` + `e00fc946` 2026-09-10).
- `own_scope_list_test.go` **665 LOC** (NEU seit W29): Swap-Request-Scope-Own-Filter-Coverage.
- `tenant_isolation_phase2_test.go` **288 LOC** (W29: 74, +214, +289%): RLS-Phase-2-Edge-Cases.

**21 Service-Methoden (Delta W29: 22)**: `CreateShift`, `UpdateShift`, `DeleteShift`, `GetShift`, `ListShifts`, `PublishShifts`, `AssignEmployee`, `UnassignEmployee`, `ListAssignments`, `CreateTemplate`, `UpdateTemplate`, `DeleteTemplate`, `GetTemplate`, `ListTemplates`, `ApplyTemplate`, `CheckArbzgCompliance`, `GetShiftStats`, `CreateSwapRequest`, `ListSwapRequests`, `ApproveSwapRequest`, `RejectSwapRequest`. **Delta: `validateRestPeriod` extrahiert zu private func** (W29 war public). **NET keine neuen Methoden**, aber `CheckArbzgCompliance` erweitert um `validateMinorProtection`-Branch.

**Welle-2A-Features (unveraendert aus W29)**: ArbZG §5 Pre-Check mit `arbzgMinRestDuration` + `validateRestPeriod` bidirektional + DST-Spring-Forward-tauglich, State-Machine Schicht (Draft→Published mit Bulk-Publish `PublishShifts(from,to)`), State-Machine Swap-Request (pending→approved/rejected mit `shift_swap_requests.idempotency_key UNIQUE` + `swap_employees_differ CHECK`), Capacity-Guard (`Shift.Capacity *int` nil=unlimited, `CountAssignments` + `ErrShiftFull`), Template-Modell (`ShiftTemplate` mit `DayOfWeek 0..6`, `StartHour/Minute`, `DurationMinutes`).

**NEU in Zyklus 2 — JArbSchG-Jugendarbeitsschutz-Features (Commit `7493cf0f` 2026-08-08)**:
- Migration **000299 `hr_employee_profiles.is_minor BOOLEAN DEFAULT FALSE`** + Index `idx_hr_employee_profiles_tenant_minor`.
- `IsMinorEmployee(tenantID, employeeID)` auf `postgres_repository.go` liest `is_minor`-Flag.
- `validateMinorProtection` + `checkMinorShiftLimits` auf `service.go` enforce §16/§17 (keine Sa/So-Arbeit, Zeile 860) + §14 (keine Arbeit ausserhalb 06:00-20:00, Zeilen 863-865) + §8 (max 8h pro Schicht, Zeile 868). `jarbschgLocation()`-Helper fuer Europe/Berlin.
- Call aus `CheckArbzgCompliance` erweitert.
- 162 LOC `service_test.go`-Coverage.

**NEU in Zyklus 2 — Concurrency-Safety-Delivery (Commit `1d24373b` 2026-09-10)**:
- Dual-Assignment-Race-Fix: Shift/Employee-Lock-Pattern verhindert dass gleiche Employee zweimal in gleicher Shift gelandet werden kann.
- `assignment_lock_test.go` 787 LOC-Coverage.
- Zusaetzliche Fixes: `fe9eb5c4` 2026-10-25 (HTTP-Status-Hygiene: Second-Assignment-of-Same-Employee → 409 Conflict statt 500 Internal Server Error).

**NEU in Zyklus 2 — Shift-Swap-Stabilisierungs-Trio**:
- `f379b30a` 2026-08-29 "make shift swaps land instead of failing or no-op'ing" — State-Machine wird reliable.
- `126c40f6` 2026-08-09 "add own-scope filter to ListSwapRequests" — Badge-Count respektiert Requester/Counterpart-Filter.
- `4b3f6bb2` 2026-10-20 "bind swap requests to the caller's own assignment" — Swap-Request muss zum eigenen Assignment des Requesters passen.

**NEU in Zyklus 2 — RLS-Phase-2-Audit (Commit `2055c475` 2026-07-19)**:
- "R-3 batch 4 enforcement": Capability-Catalog-Wiring fuer schichten-Permissions, scope-own-Filter fuer Swaps.
- Test-Coverage: `tenant_isolation_phase2_test.go` 288 LOC + `own_scope_list_test.go` 665 LOC.

**NEU in Zyklus 2 — TenantInboundUnaryInterceptor (W29-🔴-Pick #R1 delivered)**:
- `backend/cmd/schichten/main.go:56` registriert `middleware.TenantInboundUnaryInterceptor()` als gRPC-Server-Middleware.
- Schichten-Binary jetzt tenant-ready. **Einer von 13 ehemaligen R3-P0-3-Debt-Binaries ausgeraeumt** (`.knowledge/security.md`-Status).

### Frontend `desktop/src/renderer/src/modules/schichten/` (Stand 2026-10-26)

**Modul-Verzeichnis-Erweiterung (NEU in Zyklus 2)**:
- **SchichtenPage.tsx**: 1661→**2002 LOC** (+341, +21%) — Mono-Page weiter waechst additiv statt refactored, aehnlich rapporte-W43-Pattern. 4 Tabs unveraendert.
- **ShiftDetailModal.tsx**: **NEU 268 LOC** (Commit `9cb06ab7` 2026-07-19 "demo-depth - shift detail modal, real exports, settings") — Modal-Komponente geoeffnet auf Grid-Cell-Click.
- **schichten-export.ts**: **NEU 208 LOC** — PDF/CSV-Export-Builder (dedupe mit maroto/v2 statt pdfKit).
- **schichten-shared.ts**: **NEU 92 LOC** — Konstanten aus Mono-Page extrahiert: `SHIFT_STYLE_MAP`, `SURCHARGE_RULES` auf Zeilen 34-36 (nur `tpl-3` Nacht-Zuschlag), `WEEKEND_SURCHARGE` auf Zeile 38, `HOLIDAY_SURCHARGE` auf Zeile 39, `GERMAN_HOLIDAYS_2026` auf Zeilen 42-52 (9 DE-2026-Eintraege, keine DACH-Bundeslaender/Kantone), Helper-Funktionen. **Alle 4 Mock-Features weiter frontend-only ohne Backend-Wiring** — W29-Pick #3 nicht geliefert.
- **settings/SchichtenSettingsPanel.tsx**: **NEU 135 LOC** — module-settings-registry-Integration (`module-settings-registry.tsx`).

**Mock-Status (Stand 2026-10-26)**:

| Feature | Status | Code-Location |
|---|---|---|
| `AVAILABILITY_MOCK` | 🔴 Weiter hardcoded | SchichtenPage.tsx:151-410 (4 Mock-User), useState(AVAILABILITY_MOCK) Zeile 413 |
| `SURCHARGE_RULES` | 🔴 Weiter frontend | schichten-shared.ts:34-36 |
| `WEEKEND_SURCHARGE` | 🔴 Weiter frontend | schichten-shared.ts:38 |
| `HOLIDAY_SURCHARGE` | 🔴 Weiter frontend | schichten-shared.ts:39 |
| `GERMAN_HOLIDAYS_2026` | 🔴 Weiter hardcoded | schichten-shared.ts:42-52 (9 DE holidays, kein DACH) |
| `ShiftTemplate.Color` | 🔴 Adapter-Default | Frontend faelscht `#3b82f6` weiter |
| `ShiftTemplate.BreakMinutes` | 🔴 Adapter-Default | Frontend nutzt Store-Tenant-Default statt Backend-Field |

Alle 4 Mock-Features weiter **frontend-only** — keine API-Calls, keine Backend-Persistenz. Store-Backing via `schichtenTenant.ts` + `schichtenPrefs.ts` (Zustand-based).

**PWA/Offline (Stand 2026-10-26)**:
- `desktop/src/renderer/src/api/offline-queue.ts` EXISTIERT (seit rapporte-W43 commit, 247 LOC, IndexedDB-Queue + Idempotency-Key + Exponential-Backoff 1s-16s + Dead-Letter-Store + Batched-Parallel-Replay MAX_PARALLEL=5).
- **`desktop/src/renderer/src/modules/schichten/*` nutzt KEINE offline-queue-Imports**.
- Schichten-Mutations (`CreateShift`, `AssignEmployee`, `CreateSwapRequest`, etc.) **enqueuen nicht** — Online-only.
- Kein Service-Worker in `renderer/src/` gefunden (W29-Pick #PWA-Layer nicht geliefert).

### Preis-Anker (`KMU-Hub/.knowledge/pricing.md`, Stand 2026-08-17)

- Line 65: `| Schichten | 4 | buchbar |` — **unveraendert 4 EUR/User-Monat**.
- Pricing-Doc updated 2026-08-17, aber keine Preis-Delta zu W29.
- **Marktbenchmark-Vergleich (NEU in Zyklus 2)**:
  - Papershift Core nach Pricing-Pivot: 64 EUR Pauschale + 39 EUR Grundgebuehr = fuer 10 MA 10,30 EUR/MA-aequivalent (W29: 4 EUR/MA + 39 EUR Support = fuer 10 MA 7,90 EUR/MA-aequivalent). **Cosmi ist jetzt klar guenstiger.**
  - Ordio Pro: 149 EUR/Standort unveraendert. **Cosmi gewinnt in 5-15-MA-Zone, verliert in 50+-MA-Zone pro Standort.**
  - Crewmeister Standard-Bundle: 5,20 EUR/User (nach Ablauf 30%-Rabatt). **Cosmi guenstiger.**
  - Aplano Core 0,50 EUR/MA unveraendert. **Cosmi 8x teurer im Low-End.**

### Bekannte Schulden (Stand 2026-10-26)

- **R3-P0-3 schichten-Teil delivered** (`.knowledge/security.md`): `TenantInboundUnaryInterceptor` auf `cmd/schichten/main.go:56` — **einer von 13 Binaries ausgeraeumt**. 12 Binaries verbleiben in R3-P0-3-Debt.
- **`ShiftTemplate.Color` + `ShiftTemplate.BreakMinutes` fehlen weiter im Backend-Schema** — Frontend-Adapter (`adaptApiTemplate`) faelscht Defaults.
- **`SURCHARGE_RULES`/`WEEKEND_SURCHARGE`/`HOLIDAY_SURCHARGE` sind weiter Frontend-Mocks** — keine `shift_surcharge_rules`-Tabelle, keine Lohnkosten-Berechnung.
- **`AVAILABILITY_MOCK` ist weiter Frontend-Mock** — kein `employee_availabilities`-Backend-Table.
- **`arbzgMinRestDuration = 11 * time.Hour` ist weiter hardcoded Konstante** — keine Tenant-Konfigurierbarkeit fuer Pflege/Gastro/Verkehr-Ausnahmen trotz 15-Wochen-W29-Pick.
- **ArbZG-Nur-§5-Impl** — §3 (10h Tages-Max), §4 (Pausen 30/45min), §9-10 (Sonntag/Feiertag), Consecutive-Days-Regel weiter nicht geliefert. **JArbSchG wurde geliefert als Zyklus-2-Bonus**, aber generelle Erwachsenen-ArbZG-Palette fehlt.
- **Coverage** von 35,2% auf ~45% gestiegen (Test-LOC +100%) — W29-🔴-Pick #R2 "45%+ Ziel" delivered via Test-Investment.
- **Kein AI/ML-Auto-Scheduler** — jede Zuweisung bleibt manueller Drag-Drop.
- **Keine mobile Native-App** (Cosmi bleibt Electron + PWA-orientiert ohne Service-Worker-Wiring).
- **Kein Qualifikations-Matching** — jeder MA kann jeder Schicht zugewiesen werden solange ArbZG §5 passt.
- **Kein Personio-Integration-Code** — `grep personio` null Hits im Repo.
- **Kein MCP-Server fuer schichten** — kein `cmd/schichten-mcp/` oder `backend/internal/schichten/mcp/`.
- **Kein DATEV/LODAS-Export** aus schichten (buchhaltung hat DATEV OAuth seit buchhaltung-W42 commit 3b63d2c1 2026-08-22, aber kein schichten-Payroll-Export-Pfad).

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Papershift | Shyftplan | Ordio | Crewmeister | Planday | 7shifts | Deputy | Connecteam | Aplano | ShiftJuggler | HERO |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ziel-Segment** | 5-30 MA DACH-KMU | 5-500 MA DACH-KMU | 100+ MA + Shopfloor | 10-200 MA/Standort DACH | 5-100 MA DACH-KMU | 10-500 MA international | Restaurant global | 5-500 MA global | Frontline global | 5-500 MA DACH | 10-2000+ MA DACH | Handwerk 5-100 MA |
| **Pricing 4 EUR/User/Monat** | ✅ 4 EUR | ❌ Core 64 EUR Flatrate + 39 EUR Grundgeb. | ab 700 EUR/Monat | 89-149 EUR/Standort | 2 EUR (Schicht) + 1.50 EUR (Zeit) | ab $2/User | $39.99-149.99/Monat | $6.50-9/User | $29-99/Monat | 0.50-4.50 EUR/User | ab 39 EUR/Monat | ab 69 EUR/User |
| **AI-Auto-Assign** | ❌ | ✅ (ex-Premium) regel-basiert | ✅ 20+ Faktoren | ✅ (Nano-Agentic) | ❌ | ✅ Smart Rota + Intel-Shift Beta | ✅ ML 8-10 Plaene | ✅ AWS Bedrock + Predelo (85% Auto-Scheduling) | ✅ mit Konflikt-Flag + Split-Shift | 🚧 Auto-Konflikt | 🚧 Auto-Konflikt | ❌ |
| **Agentic AI (Live-Daten-Agent)** | ❌ | ❌ (Chat-only) | ❌ | ✅ **Nano NEU 2026-09** | ❌ | ✅ **"Agentic AI Experience"** | ❌ | ✅ Deputy AI Platform GA | ❌ | ❌ | ❌ | ✅ HERO Command + Report + Voice |
| **MCP-Dual-Connector (ChatGPT + Claude)** | ❌ | ❌ (3rd party) | ❌ | ❌ | ❌ | ✅ **FIRST-IN-WORKFORCE 2026-10-22** | ❌ | 🚧 Zapier | ❌ | ❌ | ❌ | ❌ |
| **Generative KI-HR-Chat** | ❌ | ✅ (mit Rechte-Aware) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Predictive Forecasting** | ❌ | ❌ | ✅ Demand-Forecast | ❌ | ❌ | ✅ | ✅ POS-Sales | ✅ Demand-Forecast + Predelo | ❌ | ❌ | ❌ | ❌ |
| **Constraint-Solver** | 🚧 (nur ArbZG §5 + JArbSchG) | ✅ Verfuegbarkeit+Qualif. | ✅ 20+ Constraints | ✅ (Nano) | ❌ | ✅ CP-SAT-adjacent | ✅ Labor+Sales+Overtime | ✅ | ✅ Konflikt-Flag | ✅ | ✅ ArbZG-Full | ❌ |
| **Schicht-Templates** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Plantafel |
| **Template.Color** | ❌ (Frontend-Default #3b82f6) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Template.BreakMinutes** | ❌ (Store-Default) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Verfuegbarkeits-Selbst-Service** | ❌ (nur Frontend-Mock) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Qualifikations-Matching (ESCO-mappable)** | ❌ | ✅ (ex-Premium) | ✅ (**Shyftskills NEU**) | 🚧 | ❌ | ✅ (**Intel-Shift ranks on contracted hours**) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Swap-Request-Selbst-Service** | ✅ **STABIL** nach W44 (3 Fixes) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Split-Shift NEU | ✅ | ✅ | 🚧 |
| **ArbZG §5 Auto (11h)** | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 (nicht DE-optimiert) | ❌ (US-Compliance) | 🚧 | 🚧 | ✅ | ✅ | ✅ |
| **ArbZG §3 (10h Tages-Max)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **ArbZG §4 (Pausen 30/45min)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ **NEU Break-Controls** | ✅ | ✅ | ✅ |
| **ArbZG §9-10 (Sonn/Feiertag)** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Consecutive-Days-Regel** | ❌ | ✅ | ✅ | ✅ | ✅ | 🚧 | ❌ | 🚧 | 🚧 | ✅ | ✅ | 🚧 |
| **JArbSchG-Jugendarbeitsschutz** | ✅ **NEU in Zyklus 2** (§8+§14+§16/17) | 🚧 | 🚧 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **ArbZG-Constant konfigurierbar (Pflege/Gastro 10h)** | ❌ | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **DACH-Feiertag-Auto (DE/AT/CH mit Kanton)** | ❌ (nur 9 DE hardcoded) | ✅ | ✅ | ✅ **+Nano Cited Web Search** | ✅ | 🚧 | ❌ | ❌ | ❌ | ✅ (DE/AT/CH im Basic) | ✅ (Marktbenchmark) | ✅ |
| **Zuschlags-System (Nacht/Sonn/Feier)** | 🚧 (Frontend-Mock) | ✅ (ex-Professional) | ✅ | ✅ | ✅ | ✅ | ✅ (Premium) | ✅ | ✅ **NEU Break-Controls** | 🚧 | ✅ | ✅ |
| **Payroll-Berechnung (Zuschlag+Stunden)** | ❌ | 🚧 (post-Pivot unklar) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 (via Partner) | ✅ | ✅ |
| **DATEV/LODAS-Export** | ❌ (buchhaltung-Teil, nicht schichten) | 🚧 (post-Professional-Discontinuation) | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ | ❌ | 🚧 (via Partner) | ✅ | ✅ |
| **Personio-Marketplace-Integration** | ❌ | ✅ | ✅ (Enterprise + shyftconnect) | ✅ | ✅ | ✅ (Standard) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **SAP SuccessFactors/HCM/APO** | ❌ | 🚧 | ✅ **shyftconnect NEU** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Workday HCM Integration** | ❌ | ❌ | ✅ **shyftconnect NEU** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Xero Buchhaltungs-Integration** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (Xero-Owner) | ❌ | ✅ (AU-Partnership) | ❌ | ❌ | ❌ | ❌ |
| **Smart-Factory-Integration (Shopfloor)** | ❌ | ❌ | ✅ **ScableOne NEU 2026-07/08** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Multi-Site/Multi-Location** | 🚧 (nur `Shift.Location` als String) | ✅ | ✅ | ✅ (Kern-Preis-Modell) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (Multi-Location) | ✅ |
| **Native iOS App** | ❌ (nur Electron+PWA) | ✅ | ✅ | ✅ | ✅ (mobile-first) | ✅ | ✅ | ✅ | ✅ (mobile-first) | ✅ | ✅ | ✅ |
| **Native Android App** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **PWA + Offline-Mode** | 🚧 (offline-queue.ts exists aus W43, aber schichten nicht wired) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 | ✅ |
| **GPS-Geofencing bei Clock-In** | 🚧 (nur `validateGPS`-Bounds) | ✅ | ✅ | ✅ | ✅ (2m Genauigkeit) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Overnight-Schichten (00:00-06:00)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Push-Notifications** | 🚧 (nur `notifications`-Modul-Kern) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Kapazitaets-Limit pro Schicht** | ✅ (`Shift.Capacity *int`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Bulk-Publish** | ✅ (`PublishShifts(from,to)`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Swap-State-Machine Idempotency** | ✅ (Mig 000160 + 3 Fixes W29→W44 stabilisiert) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 |
| **Concurrency-Safety (Shift+Employee Lock)** | ✅ **NEU in Zyklus 2** (1d24373b 2026-09-10) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Manager/Member-Rollen-Modell** | ✅ (Migration 000224) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **TenantInboundUnaryInterceptor (gRPC-Tenant)** | ✅ **NEU in Zyklus 2** (cmd/schichten/main.go:56) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| **Umsatz-Forecast-Integration** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ (POS) | ✅ Predelo | ❌ | ❌ | ❌ | ❌ |
| **Free-Tier** | ❌ | ❌ (14-Tage-Trial) | ❌ | ❌ | ❌ | ❌ | ✅ (bis 15 MA/1 Location) | ❌ | ✅ (bis 10 MA) | ❌ | ❌ | ❌ |
| **DE-Cloud (DSGVO)** | ✅ (Hetzner) | ✅ | ✅ | ✅ | ✅ | ❌ (DK/UK) | ❌ (US) | ❌ (AU/US) | ❌ (IL/US) | ✅ | ✅ | ✅ |
| **Cross-Modul-Story (CRM+Buchhaltung+etc.)** | ✅ (Kern-Cosmi-USP) | 🚧 | ❌ | 🚧 (Branchen-Add-Ons) | 🚧 | 🚧 (Xero) | ❌ | ❌ | 🚧 (3 Hubs) | ❌ | ❌ | ✅ (ERP) |
| **Open-Source-Verfuegbar** | ❌ (proprietaer) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Series-Funding seit 2026** | n/a (bootstrapped) | n/a | Maguar Portfolio | 12M EUR Serie A 2025 | n/a | Xero Owner | n/a | n/a | n/a | n/a | n/a | n/a |

**Zusammenfassung Zyklus 2 (W44 2026-10-26)**: Cosmi-schichten hat **1 of 13 W29-Picks gruen delivered** (TenantInterceptor) + 5 **nicht-prognostizierte Bonus-Deliveries** (JArbSchG, Concurrency-Lock, Shift-Swap-Fixes-Trio, RLS-Audit, Test-Investment-Welle). Das ist **mittelmaessige strategische Delivery** aber **starke Backend-Hygiene-Delivery**. Der Preis-Vorteil ist nach Papershift's Pricing-Pivot **strukturell staerker** geworden (Cosmi 4 EUR/MA vs. Papershift Core 64 EUR Flatrate = fuer 10 MA 10,30 EUR/MA-aequivalent), aber **feature-adjusted weiterhin schwach** gegenueber Papershift-KI-HR-Chat + Ordio-Nano-Agentic-UI + Planday-MCP-Dual-Connectors. **Zyklus-2-Positionings-Shift Pflicht**: Shyftplan ist nicht mehr Direkt-Konkurrent (Enterprise-Shopfloor-pivot), **Ordio ist der schaerfste DACH-KMU-Direkt-Konkurrent** (Nano-Agentic-UI operationalisiert September-Oktober 2026). HERO Software liefert jetzt echten Handwerk-AI-Benchmark (HERO AI + Voice + Command + Report). Der schichten-Delivery-Score bleibt mittelmaessig im Zyklus-2-Vergleich: 1/13 Green-Picks delivered vs. vertraege-W41 3.5/12 Picks delivered (29%), rapporte-W43 2/4 P0-Picks delivered (50%), buchhaltung-W42 0.6/3 Green-Picks delivered (20%).

---

## Top-3 Strategische Empfehlungen

### 1. **Cosmi-MCP-Server fuer schichten (+ cross-Modul-Scope) + Agentic-Positioning-Entscheidung W44** — Markt-Pflicht nach Planday-Launch 2026-10-22

**Warum**: Planday hat am 2026-10-22 als **erste** Workforce-Management-Plattform verifizierte Dual-Connectors (ChatGPT + Claude) gelauncht mit **216+ Early-Access-Kunden**, deutsche Fach-Presse hat sofort aufgegriffen. UKG hat parallel 2026-10-20 Beta-Claude-Integration gelauncht. Shyftplan/Ordio/Crewmeister/Shiftbase/Sona/HERO/gastromatic/Papershift haben **keinen offiziellen Vendor-MCP-Server** — DACH-KMU-Open-Source-ERP-Erstbesetzer-Fenster ist offen. **W33-MCP-Keeper 20 Wochen ueberfaellig** (in buchhaltung-W42 + helpdesk-W39 + formulare-W40 + vertraege-W41 + rapporte-W43 immer wieder gelistet) — Zyklus-2-Pflicht. MCP-Spec-Update 2026-07-28 (stateless, multi-round-trip, Cloudflare-Worker-Edge-Hosting trivial) macht Sprint 1-2 Wochen statt Monate.

**Was**:

**(a) Cosmi-schichten-MCP-Server MVP (W45-W46, 1.5-2 Wochen)**:
- Neues Sub-Package `backend/internal/schichten/mcp/` mit `server.go` (MCP-Server-Implementation), `tools.go` (Tool-Registrations), `auth.go` (API-Key + RBAC-Check).
- **Read-Tools** (5): `list_shifts(tenant_id, from, to, employee_id?, status?)`, `get_shift(shift_id)`, `list_assignments(tenant_id, shift_id)`, `check_arbzg_compliance(tenant_id, employee_id, start_time, end_time)`, `list_swap_requests(tenant_id, employee_id?, status?)`.
- **Write-Tools mit Human-in-the-Loop** (2): `create_shift(tenant_id, start_time, end_time, template_id?, capacity?)` (dry-run default, requires confirm-token), `assign_employee(shift_id, employee_id)` (dry-run default, requires confirm-token).
- Alle Tools respektieren bestehende RBAC (Capability-Catalog), schreiben Audit-Log in `ai_disclosure`-Table (siehe Empfehlung #2), bedienen EU AI Act Art. 50 Transparenzpflicht via maschinenlesbare Antwort-Signatur.
- Cloudflare-Worker-Edge-Hosting ODER Server-Side-SSE-Endpoint auf cosmi.app-Domain.

**(b) Cross-Modul-MCP-Scope-Erweiterung (W45-W47, parallel 3-4 Wochen)**:
- `cosmi-crm-mcp` (list_opportunities, list_contacts, create_lead, dry-run default).
- `cosmi-rapporte-mcp` (list_rapporte, get_rapport, flag_rapport_review).
- `cosmi-helpdesk-mcp` (list_tickets, get_ticket, create_ticket_reply dry-run).
- `cosmi-buchhaltung-mcp` (list_invoices, get_invoice, list_contacts).
- `cosmi-vertraege-mcp` (list_contracts, get_contract, list_signers).
- **Cross-Modul-Query-Tool (USP-Realizer)**: `query_across_modules(tenant_id, question_text)` — nutzt Cosmi's `automatisierung`-Modul-Infrastruktur um ueber mehrere Module zu antworten (z.B. "Welche Rechnungen sind an Kunde X offen fuer Baustelle Y wo Monteur Z arbeitet?" → kombiniert crm + buchhaltung + schichten + rapporte).

**(c) Agentic-Positioning-Statement W44 (3-Tage-Marketing-Sprint)**:
- Blog-Post "Cosmi orchestriert Agenten ueber alle Module hinweg" mit Vergleich: Papershift Chat (nur Schichten), Ordio Nano (nur Schichten + Cited-Web-Search), Planday Dual-Connector (nur Schichten + externe-Daten), Cosmi MCP-Server-Suite (schichten + crm + rapporte + helpdesk + buchhaltung + vertraege + Cross-Modul-Query).
- Marketing-Material-Update auf `cosmi.app/schichten` mit Agentic-AI-Story.
- Discord-#trends-Push mit MCP-Launch-Timing-Prognose.

**(d) EU AI Act Art. 50 Compliance (Deadline 2026-12-02, 37 Tage, Pflicht fuer MCP-Server)**:
- Migration **000330 `ai_disclosure(id UUID PK, tenant_id UUID FK, module TEXT, model_id TEXT, prompt_hash TEXT, response_hash TEXT, created_at TIMESTAMPTZ, consumer_type TEXT CHECK ('mcp-tool','auto-assign','chat'))`** — Audit-Log fuer jede AI-Operation.
- `ai_content_watermark` Service in `backend/internal/common/ai_disclosure/` — C2PA-Markierung-Service fuer Generative-AI-Output. Signiert MCP-Server-Antworten mit maschinenlesbarer Markierung (C2PA Content Credentials, `c2pa.org`).
- Cosmi-weiter Compliance-Package: schichten + rapporte + helpdesk + vertraege + buchhaltung alle muessen vor 2026-12-02 ai_disclosure-schreibend sein.

**Sprint-Aufwand**: 4-6 Wochen bei 1 Dev (schichten-MCP + cross-Modul-MCP parallel), 2-3 Wochen bei 2 Devs.

**Erwartete Marketing-Auswirkung**: Cosmi positioniert sich **als erster Open-Source-DACH-ERP mit offiziellem MCP-Server-Portfolio** — vor Papershift, Ordio, Shyftplan, Crewmeister, Shiftbase, Sona, HERO, gastromatic. Direkt-Kontra zum Planday-MCP-Launch-Marketing. **Lead-Gen-Window**: DACH-KMU-Buyer die seit 2026-10-22 "KI entwirft Schichtplaene" via `ad-hoc-news.de` + Fach-Presse diskutieren.

**Risiko-Faktor**: Papershift ODER Ordio koennten in Q1-2027 nachlegen (beide haben AI-Teams). First-Mover-Fenster ist 2-4 Monate — W44-Entscheidung ist strukturell.

### 2. **ArbZG-Full-Palette + `arbzgMinRestDuration` Tenant-Setting + Pflege/Gastro/Verkehr-Ausnahmen** — Regulatorische Positionierung + Delivery-Momentum nutzen

**Warum**: 15 Wochen W29-Pick #2 "Tenant-Setting" null geliefert, aber **JArbSchG-Delivery** (Commit 7493cf0f 2026-08-08) beweist dass das Team ArbZG-Delta liefern kann. Der Referentenentwurf 18.06.2026 ist weiterhin in Verbaendeanhoerung-Nachlauf / Ressortabstimmung (`table.media`, `eversheds-sutherland.com`), **noch kein Kabinettsbeschluss** Stand 2026-10-26 — Marketing-Fenster offen (kein DACH-Konkurrent hat eine aggressive ArbZG-Reform-Kampagne gestartet). §5-Aenderungen (10h Ruhezeit mit unmittelbarem Ausgleich fuer Pflege/Gastro/Verkehr/Rundfunk/Landwirtschaft, Tarifvertrag kann 11h ganz aufheben) **brechen weiter Cosmi's `arbzgMinRestDuration = 11 * time.Hour`-Konstante** auf `service.go:14`. Zusaetzlich fehlt §3 (10h Tages-Max), §4 (Pausen 30/45min), §9-10 (Sonntag/Feiertag), Consecutive-Days — alles Marktbenchmarks bei Papershift/Aplano/ShiftJuggler/Crewmeister. **Nach JArbSchG-Delivery ist das Team ArbZG-Delivery-ready.**

**Was**:

**(a) `arbzgMinRestDuration` von Konstante zu Tenant-Setting (1-2 Wochen)**:
- Migration **000331 `hr_company_settings`-Table** (falls nicht schon vorhanden) mit `min_rest_hours_default INT DEFAULT 11, max_daily_hours_default INT DEFAULT 10, break_30min_threshold_hours INT DEFAULT 6, break_45min_threshold_hours INT DEFAULT 9, max_consecutive_days INT DEFAULT 6, max_weekly_hours INT DEFAULT 48` — Tenant-weite Defaults.
- Migration **000332 `shift_arbzg_overrides(id UUID PK, tenant_id UUID FK, industry_code TEXT, min_rest_hours INT, immediate_compensation_required BOOLEAN, tarif_reference TEXT, activated_by UUID, activated_at TIMESTAMPTZ, justification TEXT)`** — branchen-/tarif-spezifische Ausnahmen mit Audit-Trail.
- `validateRestPeriod` liest `min_rest_hours` aus Tenant-Setting oder Override statt Konstante.

**(b) ArbZG §3/§4/§9-10 + Consecutive-Days Backend-Impl (2-3 Wochen)**:
- Neue Service-Methoden auf `service.go`:
  - `validateDailyMaxHours(shift, employee)` — pruft §3 (10h Tages-Max, abhaengig von `max_daily_hours_default`).
  - `validateBreakRules(shift, employee)` — pruft §4 (30min ab 6h, 45min ab 9h). Erfordert `shift_breaks`-Sub-Entity.
  - `validateWeeklyRestDay(shift, employee)` — pruft §9-10 (Sonntag/Feiertag-Verbot, mit Branchen-Ausnahme-Table).
  - `validateConsecutiveDays(shift, employee)` — max 6 Tage in Folge (abhaengig von `max_consecutive_days`).
- `CheckArbzgCompliance` erweitert um alle 4 Rules + bestehende §5-Rule + JArbSchG-Branch.
- Frontend `ArbZGViolation.type` wird jetzt Backend-persistiert (alle 4 Typen `max_hours` + `rest_period` + `break_missing` + `consecutive_days` jetzt echt statt Placeholder — W29-Pick #R-Placeholder-Replacement delivered).

**(c) UI-Compliance-Warnungen vor Publish (1 Woche)**:
- `SchichtenPage.tsx` Preview-Modal zeigt bei `PublishShifts` alle Violations gruppiert nach Type mit klaren Erklaerungen (z.B. "Mitarbeiter M. Schmidt: Ruhezeit zwischen 2026-11-10 22:00 und 2026-11-11 05:00 ist 7h, erforderlich 11h — ArbZG §5. Branchen-Ausnahme fuer Pflege (10h) ist moeglich via Tarif-Konfiguration").

**(d) Marketing-Story W44-W47 (parallel 2 Wochen)**:
- Blog-Post "Cosmi-Schichten ist ArbZG-2026-Reform-ready mit JArbSchG + Pflege/Gastro/Verkehr-Tarif-Auto-Ausnahmen".
- Sales-Deck fuer DACH-Pflege-KMU-Segment (Krankenhaus + Altenheim + ambulante Pflege = 2 Mio Pflege-MA in DE), Gastro-KMU (Restaurants + Hotel + Cafe), Verkehr-KMU (Speditionen + Taxi + Buslinien).
- Marktzuwachs-Projektion: 30-40% des adressierbaren DACH-KMU-Marktes (W29-Projektion bestaetigt).

**Sprint-Aufwand**: 4-5 Wochen (Backend + Tests + Frontend-Replacement der Placeholder-Types + Marketing).

**Erwartete Marketing-Auswirkung**: Cosmi-Kunden-Ansprache-Markterweiterung um **Pflege/Gastro/Verkehr-Segmente** die heute wegen ArbZG-Ausnahme-Bedarf ausgeschlossen sind. DACH-KMU-Marktzuwachs 30-40%. **Compliance-Pakage mit JArbSchG als Zusatz-Vorsprung**: kein DACH-Konkurrent hat JArbSchG-Jugendarbeitsschutz-Automatisierung mit `is_minor`-Flag + 3 Rules. **Deadline-Marketing**: Cosmi positioniert sich als "ArbZG-2026-Reform-ready + Platform Work Directive-ready + EU AI Act Art. 50-ready" vor Kabinettsbeschluss — Marketing-Fenster von W44 bis ca. Q1-2027.

### 3. **Mock-to-Backend-Konsolidierung: `employee_availabilities` + DACH-Feiertag-Auto + `shift_surcharge_rules`** — Pflicht-Vorbereitung fuer Auto-Assign + Prod-Risk-Fix

**Warum**: Alle 4 W29-Mocks (`AVAILABILITY_MOCK`, `SURCHARGE_RULES`, `GERMAN_HOLIDAYS_2026`, `ArbZGViolation.type`-Placeholder) sind nach 15 Wochen **immer noch Mocks** — die 2 ersten explizit in `schichten-shared.ts:34-52` extrahiert aber **nicht** zu Backend verdrahtet. Das ist **Prod-Risk** — sobald Kunden diese Features nutzen wollen (Zuschlaege fuer Payroll, Feiertags-Auto-Erkennung, Verfuegbarkeits-Selbst-Service), muss Backend nachgezogen werden. Dieser Sprint ist **Pflicht-Vorbereitung fuer AI-Auto-Assign** (W29-Pick #1, 15 Wochen null-geliefert — eventuell fuer Q1-2027-Delivery vorbereiten).

**Was**:

**(a) `employee_availabilities`-Backend (2-3 Wochen, Pflicht-Vorbereitung fuer Auto-Assign)**:
- Migration **000333 `employee_availabilities(id UUID PK, tenant_id UUID FK, employee_id UUID FK, weekday INT 0..6, hour_start INT 0..23, hour_end INT 0..23, availability_level TEXT CHECK ('available','limited','unavailable'), note TEXT, valid_from DATE, valid_until DATE, created_at TIMESTAMPTZ, updated_at TIMESTAMPTZ)`**.
- Backend-Endpoints auf `backend/internal/schichten/service.go`:
  - `GetAvailabilities(tenantID, employeeID, from, to)` — eigene + Team-Vorgesetzter.
  - `SetAvailability(tenantID, employeeID, weekday, hour_start, hour_end, level, note, valid_from, valid_until)`.
  - `ListTeamAvailabilities(tenantID, weekStart)` — Manager-View.
  - `DeleteAvailability(tenantID, availabilityID)` — scope-own-Check.
- Self-Service-UI in `SchichtenPage.tsx` Verfuegbarkeit-Tab — **Ersatz von `AVAILABILITY_MOCK`**. Mitarbeiter kann eigene Verfuegbarkeit per Wochentag + Stunden-Fenster setzen.
- Manager-UI zeigt Team-Verfuegbarkeits-Heatmap fuer Woche.

**(b) DACH-Feiertag-Auto (3 Tage, kleiner Sprint mit hoher Marketing-Auswirkung)**:
- Migration **000334 `public_holidays(id UUID PK, country_code TEXT CHECK ('DE','AT','CH'), region_code TEXT NULLABLE, year INT, date DATE, name TEXT, holiday_type TEXT CHECK ('public','school','regional'), is_public_holiday BOOLEAN, created_at TIMESTAMPTZ, UNIQUE(country_code, region_code, date))`**.
- Yearly-Cron-Job (`cmd/schichten-cron/worker.go`) der **`dach-holidays`-npm-Library** (DE + AT + CH, Kanton/Bundesland-granular, aktiver MIT-Lizenz) **ODER `nager.at`-Public-API** (100+ countries, free, no auth, no rate limit per `freeapihub.com` 2026, `date.nager.at`) abfragt und `public_holidays` seedet. Primaer: `dach-holidays` (Kanton-granular), Sekundaer: `nager.at` als Verifikations-Cache.
- `Shift.is_holiday BOOLEAN` als abgeleitetes Feld bei Insert (JOIN auf `public_holidays`).
- Frontend liest Backend statt `GERMAN_HOLIDAYS_2026`-Hardcoded-Map. `schichten-shared.ts:42-52` entfernt.
- **Marketing**: "Cosmi-Schichten mit DACH-Feiertag-Auto fuer DE 16 Bundeslaender + AT 9 Bundeslaender + CH 26 Kantone — Nacht/Sonn/Feiertag-Zuschlags-Berechnung by Jurisdiction automatisch korrekt".

**(c) `shift_surcharge_rules`-Backend (3-4 Wochen, Prod-Risk-Fix)**:
- Migration **000335 `shift_surcharge_rules(id UUID PK, tenant_id UUID FK, rule_type TEXT CHECK ('night','weekend','holiday','custom'), hour_start INT 0..23, hour_end INT 0..23, weekday_bitmask INT, holiday_type TEXT, surcharge_percent DECIMAL(5,2), min_hours_qualifying INT DEFAULT 0, active_from DATE, active_until DATE)`**.
- Backend-Service `CalculateShiftSurcharge(shiftID) []SurchargeApplication` — pro Schicht Berechnung der anwendbaren Zuschlaege (Nacht + Weekend + Holiday additiv). Konstante im Postgres statt als Frontend-Hardcoded-Map.
- `shift_calculated_wages`-Materialized-View oder Backend-Endpoint `GetShiftWages(shiftID)` fuer Payroll-Export.
- Frontend-Ersatz von `SURCHARGE_RULES`/`WEEKEND_SURCHARGE`/`HOLIDAY_SURCHARGE`-Hardcoded-Values in `schichten-shared.ts:34-39`.

**(d) Vorbereitung fuer AI-Auto-Assign-Prototyp (Q1-2027, nicht W44-Sprint)**:
- Nachdem (a) + (b) + (c) delivered sind: **`employee_qualifications`-Backend** mit ESCO-Code-Mapping (Shyftskills-Pattern uebernehmen, `developer.shyftplan.com/reference/getapiv1qualifications`).
- **CP-SAT-basierter Constraint-Solver**: Backend-Go-Package `backend/internal/schichten/auto_assign/` mit Go-OR-Tools-Binding (oder einfacher Greedy-Heuristik fuer MVP). Constraint-Set: ArbZG §3/§4/§5/§9-10 + Consecutive-Days + JArbSchG + Verfuegbarkeit + Qualifikation + Kapazitaet + Fairness.
- Manager-Button "Woche automatisch fuellen" mit Preview-Screen + Publish-Workflow + EU AI Act Art. 50 Disclosure-Markierung (via `ai_disclosure`-Table aus Empfehlung #1).

**Sprint-Aufwand**: 5-6 Wochen sequenziell (a + b + c), 3-4 Wochen mit 2 parallelen Devs. (d) als Q1-2027-Prototyp-Sprint 4-6 Wochen.

**Erwartete Marketing-Auswirkung**: Cosmi liefert vollstaendige **DACH-KMU-Schichtplan-Prod-Story**: Verfuegbarkeits-Selbst-Service + DACH-Feiertag-Auto + Nacht/Sonn/Feier-Zuschlags-Payroll + ArbZG-Vollpalette-Warnungen (aus Empfehlung #2) + JArbSchG-Compliance + TenantInterceptor-Security. Kombiniert mit Empfehlung #1 (MCP-Server) und #2 (ArbZG-Reform-ready) ergibt sich der **komplette DACH-KMU-Schichtplan-Feature-Set fuer Q2-2027-Sales-Kampagne mit AI-Auto-Assign-Add-On**.

---

## Quellen

**Planday MCP-Dual-Launch 2026-10-22 (W44-Kern-Signal)**:
- [Hotel Magazine — Planday brings context-aware workforce scheduling to ChatGPT and Claude](https://thehotelmagazine.co.uk/planday-brings-context-aware-workforce-scheduling-to-chatgpt-and-claude/)
- [Claude Marketplace — Planday Connector](https://claude.com/marketplace/connectors/planday)
- [Planday Help — How to connect Planday to Claude](https://help.planday.com/en/articles/776982-how-to-connect-planday-to-claude)
- [ad-hoc-news.de — ChatGPT und Claude entwerfen Schichtplaene fuer Gastronomie und Hotels](https://ad-hoc-news.de/wissenschaft/planday-chatgpt-und-claude-entwerfen-schichtplaene-fuer-gastronomie-und-hotels/70404162)
- [bar Magazine — Planday brings context-aware workforce scheduling](https://barmagazine.co.uk/planday-brings-context-aware-workforce-scheduling-to-chatgpt-and-claude/)
- [UKG + Claude Beta Launch 2026-10-20](https://natlawreview.com/press-releases/ukg-claude-makes-ai-work-beyond-chat)
- [MCP Spec Update 2026-07-28 — stateless + multi-round-trip + authorization-hardening](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**Papershift Pricing-Pivot September 2026**:
- [G2 — Papershift Pricing Snapshot Stand 2026-10-08](https://www.g2.com/products/papershift/pricing)
- [Papershift Blog — Core Premium Professional (alte Preis-Narrative)](https://www.papershift.com/webinare/core-premium-professional)
- [Papershift Blog — KI zur Optimierung der Personaleinsatzplanung](https://www.papershift.com/blog/ki-zur-optimierung-der-personaleinsatzplanung)
- [KI-Syndikat — Papershift KI-Auto-Zuweisung + KI-HR-Chat Test 2026](https://www.ki-syndikat.de/tools/papershift/)

**Ordio Nano Operationalisierung September-Oktober 2026**:
- [Ordio Product Updates September 2026 — Nano Cited Web Search + In-App Guide](https://www.ordio.com/en/product-updates/september-2026)
- [Ordio Product Updates October 2026 — Loop Referral-Programm](https://www.ordio.com/en/product-updates/october-2026)
- [Ordio Pricing 89-149 EUR pro Standort](https://www.ordio.com/en/pricing)

**Shyftplan + ScableOne-Uebernahme Juli-August 2026**:
- [Maguar News — Shyftplan expands AI-supported workforce mgmt platform into shopfloor execution through Scable acquisition](https://maguar.com/en/news/shyftplan-a-maguar-portfolio-company-expands-its-ai-supported-workforce-mgmt-platform-into-shopfloor-execution-through-the-acquisition-of-scable-a-leading-provider-of-smart-factory-software/)
- [Shyftplan Presseseite — Shyftplan erwirbt ScableOne](https://shyftplan.com/presseseite/shyftplan-erwirbt-scableone)
- [Shyftplan Shyftskills Qualifikations-API](https://developer.shyftplan.com/reference/getapiv1qualifications)
- [Shyftplan Personio-Integration](https://shyftplan.com/en/personio-integration)
- [Shyftplan SAP-verifizierte Integration](https://shyftplan.com/en/features/systemintegration)

**ArbZG-Reform-Progression 15 Wochen Status-Quo**:
- [Eversheds Sutherland — Referentenentwurf elektronische Arbeitszeiterfassung](https://www.eversheds-sutherland.com/de/germany/insights/update-zum-arbeitszeitgesetz-referentenent-wurf-zur-elektronischen-arbeitszeiterfassung)
- [clockin — Reform des Arbeitszeitgesetzes 2026](https://www.clockin.de/blog/reform-des-arbeitszeitgesetzes---pflicht-zur-arbeitseiterfassung-in-2026)
- [Table.media — Reform des ArbZG: BMAS enger Rahmen](https://table.media/berlin/talk-of-the-town/reform-des-arbeitszeitgesetzes-das-bmas-gibt-einen-engen-rahmen-vor-und-stellt-niemanden-zufrieden)
- [IHK Regensburg — Arbeitgeber muessen Arbeitszeit erfassen](https://www.ihk.de/regensburg/fachthemen/recht/arbeitsrecht/arbeitsvertrag-und-beschaeftigungsverhaeltnisse/arbeitnehmer-muessen-arbeitszeit-erfassen-5629408)
- [Bundestag Textarchiv kw42 2026 — Anhoerung Modernisierung Arbeitsfoerderung](https://www.bundestag.de/dokumente/textarchiv/2026/kw42-pa-arbeit-1221706)
- [Gleiss Lutz — BMAS-Update RefE ArbZG](https://www.gleisslutz.com/de/know-how/bmas-update-neuer-referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes)

**EU AI Act Art. 50 + Platform Work Directive + DSK 2026**:
- [Baker Botts — EU AI Act Article 50 Transparency Obligations Go Live (2026-08-02)](https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live)
- [EC Digital Strategy — Quick Facts Transparency rules for AI systems](https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems)
- [Gibson Dunn — EU AI Act Omnibus postponed High-Risk Deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [DLA Piper GENIE — Germany moves forward on transposing EU Platform Work Directive](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/germany-moves-forward-on-transposing-the-eu-platform-work-directive)
- [DLA Piper GENIE — Digital AI Omnibus deferral of high-risk AI obligations](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [LDA Brandenburg — DSK-Entschliessungen](https://www.lda.brandenburg.de/lda/de/datenschutz/institutionen-und-dokumente/dsk-entschliessungen/)
- [anwalt.de — Datenschutz im Job 2026 nach BAG 8 AZR 209/21](https://www.anwalt.de/rechtstipps/datenschutz-im-job-2026-ueberwachung-kontrolle-und-schadensersatz-282747.html)

**Konkurrenten W29→W44 Delta**:
- [HERO Software Presse — HERO AI Launch Juni 2026](https://hero-software.de/ueber-uns/presse/hero-ai-launch)
- [HERO Presse — HERO Command Launch 2026-09-29](https://presse.hero-software.de/hero-command)
- [photovoltaik.eu — HERO Command KI-Feature fuer Bueroaufgaben](https://www.photovoltaik.eu/planung/hero-command-ki-feature-fuer-bueroaufgaben-im-handwerk)
- [fliesenundplatten.de — HERO Command neues KI-Feature 2026-10-07](https://www.fliesenundplatten.de/hero-command-neues-ki-feature-fuer-die-betriebssoftware-07102026)
- [Deputy News — AI Platform GA + Predelo Partnership](https://news.deputy.com/deputy-ai-is-the-intelligent-trusted-teammate-for-managing-shift-based-businesses-dvzl7c)
- [Deputy News — Predelo exclusive global partnership](https://news.deputy.com/deputy-announces-exclusive-global-partnership-with-predelo-to-bring-ai-to-shift-based-businesses-s3v2hv)
- [Sona Series B 45M USD April 2026 (pymnts.com)](https://www.pymnts.com/news/investment-tracker/2026/sona-raises-45-million-to-expand-ai-platform-for-frontline-businesses/)
- [Connecteam Releases Shift Swaps + Split-Shift + Break Controls 2026-10-04](https://releases.connecteam.com/)
- [Crewmeister Starter-Angebot (Rabatt-Kampagne lief bis 2026-06-24)](https://crewmeister.com/de/angebote)
- [Aplano Preise 0.50-4.50 EUR/MA](https://www.aplano.de/preise)
- [ShiftJuggler Wissen — Rechtsthemen ArbZG](https://www.shiftjuggler.com/wissen/rechtsthemen/arbeitszeitgesetz)
- [7shifts — What's New September 2026 (Training GA + AI-Content-Gen)](https://kb.7shifts.com/hc/en-us/articles/55110421916179-Whats-New-September-2026)
- [Xero Blog — Retire Planday AU Partnership Deputy](https://blog.xero.com/news-events/xero-retire-planday-au-partnership-deputy)
- [Papershift Third-Party MCP via usefulapi.io (glama.ai)](https://glama.ai/mcp/connectors/io.usefulapi/papershift)
- [Deputy Zapier MCP](https://zapier.com/mcp/deputy)

**AI-Scheduling + MCP + PWA Best-Practice 2026**:
- [CP-SAT nurse-scheduling benchmark paper arxiv 2608.30419 (Aug 2026)](https://arxiv.org/html/2608.30419v1)
- [LLM-powered MILP engine for workforce scheduling arxiv 2511.02364 (Nov 2026)](https://arxiv.org/abs/2511.02364)
- [SCHEDBench — LLM constraint faithfulness benchmark arxiv 2608.00991](https://arxiv.org/pdf/2608.00991)
- [Deputy AI Product Page](https://www.deputy.com/ai)
- [Planday Winter/Spring 2026 Updates incl. Intelligent Shift Assignment Beta](https://help.planday.com/en/articles/621960-product-updates-winter-and-spring-2026)
- [Dexie 4.4 + Dexie Cloud 3.0 Release Post (March 2026)](https://dexie.org/blog/dexie-44-dexie-cloud-server-30-the-big-one)
- [PWA & Offline-First Sync Engines 2026 Deep Dive (2026-05-16)](https://www.youngju.dev/blog/culture/2026-05-16-pwa-offline-first-sync-2026-workbox-replicache-rxdb-yjs-automerge-livestore-electric-zero-ground-deep-dive.en)
- [Nager.Date API — No rate limit 2026](https://date.nager.at/api)
- [NPM dach-holidays Package](https://www.npmjs.com/package/dach-holidays)
- [NPM german-holidays (mulkatz)](https://github.com/mulkatz/german-holidays/)
- [Everything your team needs to know about MCP in 2026 (WorkOS)](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026)
- [ChatGPT App Directory State 2026 Mid-Year](https://chatgptappsrank.com/state-of-chatgpt-apps-2026)
- [ESCO Occupations + Skills Taxonomy EU](https://data.europa.eu/esco)

**Personio + DATEV LODAS Ecosystem 2026**:
- [Personio Press — Profitability + aurio acquisition April 2026](https://www.personio.com/about-personio/press/personio-profitability-acquisition-aurio/)
- [Personio acquires Circula October 2026 (eu-startups)](https://www.eu-startups.com/2026/10/german-unicorn-personio-acquires-spend-management-platform-circula/)
- [Personio Developer Changelog — Webhook Events API Breaking Change 2026-07-15](https://developer.personio.de/changelog/webhooks-events-api)
- [DATEV LODAS Infoservice Dezember 2025 PDF (2026-Version)](https://www.datev.de/content/dam/markenassets/themen-und-produktgruppen/service/pdf/Infoservice%20LODAS%20Dezember%202025.pdf)
- [DATEV Lohnauswertungsdatenservice API Docs](https://wissensplattform.apps.datev.de/help/document/1019845)

**Markt-Zahlen 2026**:
- [Cognitive Market Research — Employee Scheduling Market Report](https://www.cognitivemarketresearch.com/employee-scheduling-and-shift-planning-software-market-report)
- [DataIntelo — Employee Scheduling Software Market CAGR 11.2%](https://dataintelo.com/report/employee-scheduling-software-market)
- [Verified Market Reports — Employee Shift Scheduling Software Market](https://www.verifiedmarketreports.com/product/employee-shift-scheduling-software-market/)
- [Fortino Capital — Shiftbase Partnership April 2026](https://www.fortino.capital/portfolio/shiftbase)
- [IDA Ireland — Rippling Dublin EU-HQ Expansion May 2026](https://www.idaireland.com/latest-news/press-release/workforce-management-platform-rippling-announces-eu-hq-in-dublin)

---

## Picks (vorgeschlagen)

[ ] 🟢 **Cosmi-schichten-MCP-Server MVP (W45-W46)** — 5 Read-Tools + 2 Write-Tools mit Human-in-the-Loop, wrapped 21 bestehende Service-Methoden, Cloudflare-Worker-Edge-Hosting. First-DACH-Open-Source-ERP-Erstbesetzer-Fenster offen bis Q1-2027. Empfehlung #1(a).

[ ] 🟢 **Cross-Modul-MCP-Scope-Erweiterung (W45-W47 parallel)** — cosmi-crm-mcp + cosmi-rapporte-mcp + cosmi-helpdesk-mcp + cosmi-buchhaltung-mcp + cosmi-vertraege-mcp + Cross-Modul-Query-Tool als USP-Realizer. W33-MCP-Keeper 20 Wochen ueberfaellig. Empfehlung #1(b).

[ ] 🟢 **EU AI Act Art. 50 ai_disclosure + C2PA-Watermark-Service (Deadline 2026-12-02, 37 Tage)** — Migration 000330 + ai_content_watermark-Service in `backend/internal/common/ai_disclosure/`. Pflicht fuer MCP-Server-Antworten + fuer alle zukuenftigen AI-Features. Cosmi-weiter Compliance-Package. Empfehlung #1(d).

[ ] 🟢 **`arbzgMinRestDuration` Tenant-Setting + `shift_arbzg_overrides`-Table (Pflege/Gastro/Verkehr-Ausnahmen)** — Migration 000331 `hr_company_settings` + 000332 `shift_arbzg_overrides`. 15-Wochen-W29-Pick #2 pflicht-zu-liefern. §5-ArbZG-Reform-Marketing-Fenster offen vor Kabinettsbeschluss. Empfehlung #2(a).

[ ] 🟢 **ArbZG §3 + §4 + §9-10 + Consecutive-Days Backend-Impl** — `validateDailyMaxHours` + `validateBreakRules` + `validateWeeklyRestDay` + `validateConsecutiveDays` + CheckArbzgCompliance erweitert. Ersetzt ArbZGViolation-Placeholder-Types im Frontend. 15-Wochen-W29-Pick nach JArbSchG-Delivery-Momentum. Empfehlung #2(b).

[ ] 🟢 **`employee_availabilities`-Backend + Self-Service-UI** — Migration 000333 + GetAvailabilities/SetAvailability/ListTeamAvailabilities Endpoints. Pflicht-Vorbereitung fuer AI-Auto-Assign Q1-2027. Ersatz von AVAILABILITY_MOCK (SchichtenPage.tsx:151-410). 15-Wochen-W29-Pick #3a. Empfehlung #3(a).

[ ] 🟢 **DACH-Feiertag-Auto via dach-holidays-npm oder nager.at-API** — Migration 000334 `public_holidays` + Yearly-Cron-Job. 3-Tage-Sprint mit hoher Marketing-Auswirkung. Ersatz von GERMAN_HOLIDAYS_2026-Hardcoded-Map (schichten-shared.ts:42-52). 15-Wochen-W29-Pick #3b. Empfehlung #3(b).

[ ] 🟡 **`shift_surcharge_rules`-Backend + Payroll-Berechnung + DATEV/LODAS-Export vorziehen** — Migration 000335 + `CalculateShiftSurcharge`. Ersatz von SURCHARGE_RULES/WEEKEND_SURCHARGE/HOLIDAY_SURCHARGE (schichten-shared.ts:34-39). Papershift-Pricing-Pivot oeffnet DATEV-Lead-Gen-Fenster. Empfehlung #3(c). → followup 45d.

[ ] 🟡 **Papershift-Pricing-Pivot-Sales-Enablement-Sprint (W44 1-Wochen-Marketing)** — Vergleichs-Material "Cosmi-Schichten 4 EUR/MA vs. Papershift Core 64 EUR Pauschale (G2 Stand 2026-10-08)". Blog-Post + Sales-Deck + Discord-#trends-Push. Lead-Gen-Fenster Q4-2026. → followup 14d.

[ ] 🟡 **Agentic-Positioning-Statement W44 "Cross-Modul-Agent (Cosmi) vs. In-Modul-Agent (Ordio/Papershift/Planday)"** — Blog-Post + Marketing-Material-Update auf cosmi.app/schichten + Discord-#trends-Push. Direkt-Kontra zum Planday-MCP-Launch 2026-10-22. Empfehlung #1(c). → followup 7d.

[ ] 🟡 **Personio-Marketplace-Integration + Technology-Partner-Program-Application** — Sales-Barrier fuer DACH-Personio-Bestandskunden (Sales-Blocker). Breaking API Change 2026-07-15 (Webhook-Allowlist) ist Lead-Gen-Opportunity. Zero-Cost Partner-Program. → followup 60d.

[ ] 🟡 **Multi-Site-Support (`locations`-Table statt `Shift.Location`-String)** — Ordio-Preis-Modell-Konkurrenz + Multi-Standort-KMU-Support + nationale Pflege/Gastro-Ketten. 15-Wochen-W29-Pick. → followup 60d.

[ ] 🟡 **PWA-Layer fuer SchichtenPage.tsx mit offline-queue-Integration** — existing `offline-queue.ts` seit rapporte-W43 verfuegbar, schichten-Mutations enqueuen aktuell nicht. 15-Wochen-W29-Pick #PWA-Layer. Capacitor-Wrapper fuer iOS-Business-App-Distribution Q2-2027. → followup 60d.

[ ] 🟡 **Cross-Modul-Bundle-Rabatt-Marketing + Cosmi-Micro-Free-Tier fuer <5 MA** — Anti-Aplano-Preis-Strategie (0.50 EUR Core 8x guenstiger). Marketing-Sprint + `.knowledge/pricing.md`-Update. 15-Wochen-W29-Pick. → followup 45d.

[ ] 🟡 **`employee_qualifications`-Backend mit ESCO-Code-Mapping (Q1-2027)** — Shyftskills-Pattern uebernehmen, Pflicht-Vorbereitung fuer AI-Auto-Assign. ESCO-ontology-adjacent (~3000 Occupations, 13000+ Skills). → followup 90d.

[ ] 🟡 **AI-Auto-Assign-Prototyp CP-SAT-based (Q1-2027)** — Backend-Go-Package `backend/internal/schichten/auto_assign/` nach (a)+(b)+(c) delivered. Constraint-Satisfaction mit ArbZG-Full + Verfuegbarkeit + Qualifikation + Kapazitaet + Fairness. 15-Wochen-W29-Pick #1. 68% DACH-Buyer-Erwartung laut W29-Markt-Report. → followup 90d.

[ ] 🔴 **`ShiftTemplate.Color` + `ShiftTemplate.BreakMinutes` Backend-Schema** — Frontend-Adapter faelscht heute weiter Defaults `#3b82f6` + Store-BreakMinutes. Kleiner Migration + Service-Update-Sprint. 15-Wochen-W29-Pick #R-Schema-Fix. → followup 21d.

[ ] 🔴 **Platform Work Directive-Compliance-Vorbereitung (Deadline 2026-12-02, 37 Tage)** — `shift_worker_classification`-Feld (regular-employee/freelancer/platform-worker) + Audit-Logging bei Zuweisung ausserhalb regulaerem Beschaeftigungsverhaeltnis. Bundesrat 2026-09-25-Push + DE kein nationaler Entwurf. → followup 30d.

[ ] 🔴 **MinorProtection-UI im SchichtenPage.tsx** — Backend JArbSchG-Delivery seit 2026-08-08 vorhanden, Frontend zeigt noch keine Minor-Specific-Warnings. UI-Preview-Modal fuer `ErrJArbSchGNightWork`/`ErrJArbSchGDailyHours`/`ErrJArbSchGWeekend`. → followup 21d.

[ ] 🔴 **Test-Coverage-Konsolidierung schichten auf 60%+** — Jetzt ~45%-60% nach Zyklus-2-Test-Investment-Welle, Ziel >60% weiter raising. Fokus: Auto-Assign-Vorbereitungs-Code. → followup 60d.
