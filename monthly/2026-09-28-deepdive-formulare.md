---
year: 2026
week: 40
modul: formulare
created: 2026-09-28
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 42
tokens_input: ~180000
tokens_output: ~24000
rotation_position: 6/15
zyklus: 2
delta_to: monthly/2026-06-15-deepdive-formulare.md
---

# Deepdive: formulare (Mo W40/2026) — Zyklus 2 Delta

> **Zyklus 2, sechster Deepdive.** Baseline: `monthly/2026-06-15-deepdive-formulare.md` (Zyklus 1 W25, vor 15 Wochen). Vorgaenger Zyklus 2: `crm-core` (W35), `dialer` (W36), `video` (W37), `wiki` (W38), `helpdesk` (W39). Naechstes Modul gemaess Rotation: **vertraege** (KW41, 2026-10-05).

> **Delivery-Rate W25 → W40: 3.5/7 W25-Empfehlungen strukturell geliefert (50%).** Geliefert: SSRF-Schutz (via `safehttp`-Package im Worker), Public-Form-Rate-Limit (Gateway-Middleware `publicRateLimit` auf `/api/v1/public/formulare/submit/{token}`), CSV-Formula-Injection-Fix (`csvutil.NeutralizeFormulaCell` + dediziertes XLSX-Injection-Test-File), Field-Type-Union-Fix `email` (Anti-Drift-Sweep #1). Half-Delivered: Anti-Drift-Sweep (1/4 der Diskrepanzen behoben). **Null geliefert:** Honeypot, Captcha, Submission-Spam-Status, AI-Form-Generation, MCP-Server. **Regression:** FormularePage.tsx 2457 → 5605 LOC (+128%) — Refactor-Empfehlung W25 nicht ignoriert, sondern rueckwaerts-geliefert.

> **Aber (der andere Teil der Story):** Zwei grosse strukturelle Auslieferungen, die im W25-Baseline NICHT prognostiziert waren, sind jetzt live. **B6 Intake-Target-Binding** (Migration 000292): Form-Schema kann via `intake_target_id` an ein Modul-Ziel gebunden werden (heute: nur `helpdesk_ticket`). Feldern wird eine `role` zugewiesen (`subject/description/priority/category/requester_name/requester_email`), Submission dispatched direkt via `gateway/intake_helpdesk.go::createHelpdeskTicketFromIntake` einen echten Ticket ueber den Helpdesk-gRPC-Client. **B8 Public-Share-Tokens** (Migration 000293): `form_share_tokens` mit korrekter 3-Step-Sicherheits-Sequenz (Token in System-Context aufloesen → Tenant re-scopen → Tenant-scoped-Write), Klartext-Token analog zu report_share_tokens 000252 + csat + document_share_links 000266, Soft-Revoke bewahrt submission_count, MaxSubmissions optional pro Link, RedeemShareLinkTx transaktional gegen Race-Conditions. Das ist der **konkrete Cross-Modul-Beweis** den W25 als Empfehlung 2 (b) skizziert hat — geliefert als tatsaechlicher Sub-System-Wechsel, nicht als Prototyp.

> **Leit-Signal der Woche (Zyklus-2-Delta):** **Drei Zeitfenster verkleinern sich gleichzeitig.** (a) **EU-AI-Act Art. 50 live seit 2026-08-02** (57 Tage per W40). Cosmi hat weiterhin `null` `backend/internal/compliance/ai_disclosure/` und `null` `backend/internal/ai/providers/router/` (verifiziert per Directory-Check heute). Meeting-AI-Summary (video-Modul, Wave-7C) laeuft seit 2026-08-02 im Non-Compliance-Fenster — jetzt Tag 57, W39-P0 AI-Compliance-Foundation-Sprint 7 Tage weiter unadressiert. **Grace-Period bis 2026-12-02 fuer Machine-Readable-Marking (Deepfake/GPT-Content)** — das ist eine 66-Tage-Deadline, nicht mehr. (b) **Anti-Spam-Trias 15 Wochen unadressiert**. Cosmi hat heute B8-Public-Share-Tokens *live-deployt* (Public-Form-Traffic ist erlaubt), aber keinen Honeypot, kein Captcha, keinen Spam-Submission-Status. Der Gateway-Rate-Limit (`publicRateLimit`) ist der einzige Anti-Bot-Layer — er stoppt 100-req/min-Bursts, aber nicht 5-req/min-verteilte Bot-Farmen ueber 24h. **Erste oeffentliche Cosmi-Form kann jederzeit gehen** (B8 shipped, kein Feature-Flag-Gate mehr) — Anti-Spam-Trias ist ab jetzt kein "Sprint-Item vor Public-GA", sondern Live-Production-Risk. (c) **Konkurrenz-Reife**: Typeform ISO/IEC 42001 (AI-Governance-Zertifizierung, Juni 2026), Tally-MCP-Server offiziell in Claude+ChatGPT One-Click-Directory (Q3 2026), JotForm MCP paid + Claude/ChatGPT-Directory. **Cosmi hat MCP-Server-Empfehlung aus W25 (Sprint-Aufwand 5-7 Tage!) 15 Wochen ignoriert waehrend genau dieses Fenster von der Konkurrenz besetzt wurde.**

> **Interpretation der Delivery-Divergenz:** Backend-Team liefert konsequent tief in *neuen* Domaenen (Intake-Binding, Share-Token-Sec, Retention-Handler, safehttp/csvutil-Security-Sweep). **Sicherheits-Empfehlungen wurden ernst genommen** — SSRF, Formula-Injection, Rate-Limit alle delivered. Frontend-Team liefert konsequent breit an *UI-Features* (FT-2a Validierung, FT-2b Rating/Thanks-You, FO-4 Notifications, FO-6 Conditional-Eval, FD-0/1/2 Share-Distribution). **Die Verkehrsbereichs-Drift zwischen Frontend und Backend hat sich VERGROESSERT**, nicht verkleinert — 4 neue Drift-Achsen (`consent`/`rating`-Pseudo-Types, `closed`-Status, FormSchema-Extra-Fields, ShareLink-Channel/Views) sind ADDITIV zu den 3 alten (FieldOption, FormAction, per-field-Page) hinzugekommen. **Das W25-Sprint-2-Hygiene-Item ist heute ein Sprint-2+Sprint-3-Doppel-Item.**

---

## Zusammenfassung Delivery-Rate W25 → W40

| W25-Empfehlung | Status W40 | Wo im Code | Notiz |
|---|---|---|---|
| Anti-Spam Honeypot-Feldtyp | ❌ Null geliefert | `service.go:44 validFieldTypes` = 9 Typen unveraendert | 15 Wochen unadressiert |
| Anti-Spam Captcha-Slot (Turnstile/hCaptcha) | ❌ Null im Formulare-Modul | `security/captcha.go` existiert (fuer route_booking), aber `route_formulare.go` bindet ihn NICHT | CaptchaVerifier ist verfuegbare Zutat, formulare-Public-Route wurde nicht angehakt |
| Anti-Spam Rate-Limit pro IP/Form | ✅ Teil-geliefert (Gateway-Ebene) | `route_formulare.go:149-158 RegisterPublicRoutes` mit `publicRateLimit` Middleware | Fehlt: Per-Schema-Cap (1000 Submissions/Form/Tag), Per-IP-Cap-Konfigurierbarkeit |
| Anti-Spam Submission-Status `spam` | ❌ Null geliefert | `models.go:19-25` FormSubmissionStatus = new/read/archived (3 unveraendert) | Sprint-Item weiter offen |
| SSRF-Schutz auf Webhook-URLs | ✅ Geliefert | `worker.go:61` `safehttp.New(safehttp.WithTimeout(10*time.Second))` | Kommentar zeigt: "URL kommt vom Tenant, gleicher Guard wie automation http.request action" — richtig verstanden und delivered |
| CSV/XLSX-Formula-Injection-Schutz | ✅ Geliefert (NICHT in W25 prognostiziert) | `service.go:600,611` `csvutil.NeutralizeFormulaCell()` + `xlsx_formula_injection_test.go` (87 LOC) | Bonus-Delivery — war kein W25-P0 aber wichtig |
| AI-Form-Generation Cross-Modul-Architektur | ❌ Null geliefert | Keine `docs/architecture/ai-formulare-cross-modul.md`, kein `backend/internal/ai/`-Package | Alle drei Q4-2026 / Q1-2027-Empfehlungen 2 (a)–(e) offen |
| MCP-Server (`cosmi-formulare-mcp`) 5-7-Tage-Spike | ❌ Null geliefert | Kein `backend/internal/*/mcp*` Path im Repo | 15 Wochen ignoriert waehrend Tally-/JotForm-/Typeform-MCP live gingen und in Claude/ChatGPT-Directory landeten |
| Anti-Drift-Sweep #1: Field-Type-Union `email` | ✅ Geliefert | `stores/formulare.ts:17-31` FormFieldType hat `email` jetzt drin | Aber 2 neue Pseudo-Types `consent`+`rating` hinzugefuegt die Backend nicht kennt = neue Drift |
| Anti-Drift-Sweep #2: FieldOption struct | ❌ Null geliefert | Frontend `options?: string[]` (line 58), Backend `[]FieldOption{Value,Label}` (models.go:83-86) unveraendert | Round-trip-Loss von Option-Labels weiter aktiv |
| Anti-Drift-Sweep #3: FormAction backend-persistence | ❌ Null geliefert | `stores/formulare.ts:83-86` FormAction (email/task/crm_contact) mit Kommentar "not yet persisted to backend" unveraendert | Aber: `intake_target_id` (B6) ist ein *anderer* Weg — Post-Submission-Aktion wird jetzt ueber Intake-Registry statt FormAction-Pipeline geloest. Frage: FormAction ist damit toter Code oder komplementaer? |
| Anti-Drift-Sweep #4: Per-Field-Page-Assignment | ❌ Null geliefert | Frontend `page?: number` (line 74) weiter frontend-only, Backend `FormField` (models.go:68-80) hat kein Page-Feld | Bug-Latency: Multi-Page-Forms verlieren Layout beim Round-Trip |
| FormularePage.tsx Mono-File-Refactor 6-8 Sub-Components | ❌❌ Regression | `FormularePage.tsx` 2457 → 5605 LOC (+128%) | Refactor-Schuld hat sich mehr als verdoppelt |
| Cloudflare-Turnstile-Audit + Marketing-Site | Unbekannt | Nicht im Repo geprueft — DevOps-Kontext | 30-Tage-Followup war 2026-07-15 — ueber 10 Wochen ueberzogen |
| SOC-2-Type-II Roadmap-Marker | Unbekannt | Nicht in `.knowledge/security.md` erkennbar | Security-Lead-Frage |

**Netto-Lesart:** **3 volle P0-Deliveries** (SSRF + Rate-Limit-Gateway + Formula-Injection) + **1 Cross-Modul-Bonus** (Intake-Binding + Share-Tokens als reale Cross-Modul-Auslieferung). **2 P0-Non-Deliveries** (Anti-Spam-Trias komplett + AI-Compliance-Foundation komplett). **Refactor-Schuld verdoppelt.** Team-Skill-Diagnose bestaetigt W39-Muster: **schnell in Backend-Sicherheit + Cross-Modul-Domaenen-Model, langsam in Frontend-Refactor + AI-Compliance-Neuland**.

---

## Neue Sub-Systeme seit W25 (im Detail)

### B6 Intake-Target-Binding (Migration 000292, +field.Role)

Formulare-Modul spielt seit Zyklus 2 in einer **anderen Liga** als in W25 skizziert: Ein Formular ist nicht nur "Datencontainer, dessen Submission via Webhook rausgeht", sondern kann **strukturell an ein Modul-Ziel gebunden** werden.

- **Migration 000292** — additiv, kein FK: `ALTER TABLE form_schemas ADD COLUMN intake_target_id TEXT NULL`. Text-Identifier in Code-Registry, nicht DB-Reference.
- **Registry heute**: exakt **ein** Ziel — `helpdesk_ticket` — in `backend/internal/gateway/intake_helpdesk.go`. Rollen-Liste `subject/description/priority/category/requester_name/requester_email`. Priority-Coercion mit DE-/EN-Synonymen (`niedrig→low`, `hoch→high`, `dringend→urgent`, `kritisch→urgent`).
- **Field-Role-Validation** — `service.go:54-57 validIntakeRoles` als Whitelist auf Service-Ebene. Fehlerhafte Rolle = `ErrInvalidFields` beim CreateFormSchema. Symmetrisch zum Frontend-Rollen-Dropdown (`components/shared/intake/types.ts`) — Kommentar in Code: *"single flat list today because there is exactly one registered target"*.
- **Dispatch-Fluss (authenticated Submission)**: `route_formulare.go::HandleCreateSubmission` → `service.CreateSubmission` → `intake.go::dispatchIntake` → `intake_helpdesk.go::createHelpdeskTicketFromIntake` → `helpdesk`-gRPC-Client (via ServiceRegistry, richtig — nicht direkter Service-Aufruf; RLS wuerde sonst umgangen).
- **Dispatch-Fluss (public Submission via Share-Token)**: `intake_channel_external = "external"` statt `intake_channel_selfservice = "selfservice"` — RequesterIsExternal=true, kein RequesterID → Helpdesk-Ticket landet als externer Kanal, korrekt fuer Sales-/Support-Formulare mit anonymen Absendern.
- **Default-Subject** `intakeDefaultTicketSubject = "Anfrage über Formular"` — Kommentar: *"losing the submission over an empty field would be absurd"*.
- **Dispatch-Error-Handling**: Kommentar in route_formulare.go:472 sagt *"the dispatch error is logged and the submitter their answers, so the dispatch error is logged and the submitter [not blocked]"* — Submission ist eingecheckt, Intake-Fehler wird nicht bis zum Client durchgereicht (richtig: die Antworten des Users sind gerettet, nur die Post-Submission-Dispatch-Aktion faellt weg).

**Cosmi-USP-Bedeutung:** Das ist der **konkrete dritte Cross-Modul-Proof-of-Concept** im Repo, nach `material_availability.go` (produktion↔inventar, W34) und `helpdesk_ticket_contact_org` via `entity_links` (helpdesk↔CRM, W39). Der Unterschied: Intake-Binding ist der **einzige** dieser drei, der ueber eine **gemeinsame Registry-Konvention** funktioniert (`intake_target_id` als Text-Key, `intakeTarget`-Struct mit `roles map + create func` — extensible ohne Schema-Changes fuer neue Ziele). Wenn Cosmi zwei weitere Ziele registriert (`crm_deal`, `dialer_callback`), skaliert das Muster ohne SQL-Migration. Das ist ein **generisches Cross-Modul-Pattern**, nicht nur ein Ad-hoc-Wiring wie die anderen zwei.

**Sales-Marketing-Verwendung**: Diese Story ist ready-to-pitch. "Bewerbungsformular oder Kunden-Anfrage-Formular wird in einem Klick zu einem Helpdesk-Ticket mit korrekter Priority + Category + Requester-Email — ohne dass Sie ein Zapier-/Make-Konto brauchen. Cosmi-nativ, DSGVO-konform, Tenant-isoliert." Typeform/Fillout/JotForm koennen das strukturell nicht in einer Suite, muessen mit externem Helpdesk-Tool integrieren (Zendesk/Freshdesk/Zammad — jeweils separate Rechnung, separates DPA, separates Compliance-Audit).

### B8 Public-Share-Tokens (Migration 000293)

Das W25-Baseline sprach von "IsPublic-Mode aktiv (Backend Code-Pfad existiert), aber keine Anti-Spam-Schicht". Der Bericht hat sich **ein wichtiges Detail** gemerkt: der `IsPublic`-Flag wurde tatsaechlich nie als Auth-Gate ausgewertet — die gesamte `/api/v1/formulare`-Gruppe sass hinter `RequireAuthenticated`, sodass eine "public" Form ohne Login nicht submittable war. **Das war ein Blocker**, nicht ein Live-Risiko.

- **Migration 000293** — neue Tabelle `form_share_tokens` mit korrekter RLS-Pattern-Uebernahme von `report_share_tokens (252) / document_share_links (266) / csat`. 
  - `token TEXT NOT NULL UNIQUE` — 32 Bytes crypto/rand, base64url = 43 Chars, **cross-tenant-unique** (der Public-Route resolved den Tenant aus der Token-Spalte, Kollision waere Cross-Tenant-Write).
  - `expires_at TIMESTAMPTZ NULL` (NULL = never expires), `revoked_at TIMESTAMPTZ NULL` (soft-revoke), `max_submissions INTEGER NULL CHECK (>0)` (NULL = unlimited), `submission_count INTEGER NOT NULL DEFAULT 0`.
  - RLS mit `is_system_context()`-Bypass fuer die Public-Lookup-Query — sauber begruendet: *"the public lookup by token runs in the system context because the request carries no tenant yet — resolving it is the very question the token answers"*.
- **3-Step-Sicherheits-Sequenz** (`form_share.go:230-334 SubmitByShareToken`) — Kommentar zitiert: *"same shape as helpdesk.Service.SubmitCsatByToken and berichte GetSharedDocument"*:
  1. Token-Lookup in System-Context (einzige Query die RLS bewusst umgeht) — Antwort auf "welchen Tenant darf der Caller schreiben".
  2. Refuse revoked/expired/quota-erreicht — **alle drei geben `ErrShareLinkNotFound`** (nicht `ErrShareLinkExpired` / `ErrShareLinkRevoked`), Kommentar: *"the route must not report which tokens exist"*. Timing-Attack-Sicher.
  3. Re-enter Tenant-Scope mit `withTenant(ctx, link.TenantID)` → alle folgenden Reads/Writes tenant-scoped mit RLS aktiv.
- **Schema-Re-Check on redemption**: `schema.DeletedAt != nil || !schema.IsPublic || schema.Status == Archived` — alle drei → same `ErrShareLinkNotFound`. Das schliesst die Baseline-Gap "IsPublic switchen laesst tote Links leben".
- **File-Field-Refusal** (`form_share.go:284-290`) — Public-Submission mit `file`-Feld wird **outright rejected**, nicht half-supported. Kommentar: *"accepting the form anyway would store an attachment reference pointing at nothing"*. Sauber: keine Half-Baked-Uploads.
- **Race-Condition-Schutz** (`form_share.go:311-320 RedeemShareLinkTx`) — Repository wiederholt "still live, still under quota" innerhalb des Write-Trx. Kommentar: *"two visitors redeeming the last slot at once is exactly the race the check above cannot cover"*. Quota haelt.
- **maxPublicAnswersBytes = 256 KB** (`form_share.go:93`) — Service-Side-Floor, nicht nur Gateway-Body-Cap. *"the limit holds no matter who calls the RPC"*.
- **shareTokenMaxLength = 128** (`form_share.go:88`) — vermeidet DB-Query fuer offensichtliche Probes.

**Sicherheits-Interpretation**: **B8 ist Production-Grade-Security-Engineering.** Der komplette Public-Flow ist sauber begruendet, Kommentare zeigen tiefes Verstaendnis (Timing-Sicherheit, Race-Trx, System-Context-Grenzen). *Aber:* Der Flow ist heute **anti-spam-blank**. Ein Bot mit gueltigem Token kann bis zum `maxSubmissions`-Cap posten, oder — wenn `maxSubmissions=NULL` (Default) — unbegrenzt. Der einzige Bremsklotz ist der Gateway-`publicRateLimit` (Per-IP-Bucket) — ein Bot-Farm mit 100 IPs umgeht das trivial. **Anti-Spam-Trias ist ab B8-Live-Datum zwingend.**

### GDPR-Retention (Migration 000317 + FormSubmissionRetentionHandler)

- **Migration 000317** — `ALTER TABLE form_submissions ADD COLUMN anonymized_at TIMESTAMPTZ NULL`. Kommentar begruendet warum eine dedizierte Spalte statt `updated_at`: *"a second retention run does not rewrite the same rows forever"*.
- **Handler** in `internal/security/gdpr/retention_helpdesk_formulare.go` (nicht direkt gelesen in dieser Session, aber Migration-Kommentar bestaetigt Existenz).
- **Zusammen mit W38-Wiki-Deepdive** (dort auch `wiki_articles` Retention-Handler geflaggt): Cosmi hat jetzt eine querschnittliche Retention-Worker-Architektur — Formulare + Helpdesk in einem Handler-Modul, Wiki + Berichte separat. **Struktureller Fortschritt fuer DSGVO Art. 17 + Art. 5(1)(e)**.

### Sicherheits-Sweep (safehttp + csvutil.NeutralizeFormulaCell)

- **`safehttp` Package** (`internal/security/safehttp`) — wird jetzt in `worker.go:61` genutzt. Kommentar in Code: *"the same guard the automation http.request action uses applies here: without it a form webhook pointed at 169.254.169.254 or at an internal service turns this worker into a request forwarder inside our own network"*. **W25-Empfehlung 1 (d) exakt geliefert**, mit Referenz auf gleiche Klasse in `automation`-Modul (Muster-Wiederverwendung, nicht Ad-hoc).
- **`csvutil.NeutralizeFormulaCell`** (`internal/csvutil`) — wird in `service.go:600,611` fuer CSV + XLSX genutzt. Dediziertes `xlsx_formula_injection_test.go` (87 LOC) beweist Coverage. **CVE-Klasse**: CSV-Formula-Injection (CVE-2014-3524 seed, Q3-2026 immer noch aktiv exploitiert — Bewerbungsformulare mit `=cmd|'/c calc'!A0` als Antwort-Text landen als Excel-Formel im Recruiter-Download). **Konkurrenz-Kontext**: Fillout/Typeform/JotForm haben CSV-Injection-Schutz seit Jahren, war Cosmi-Gap; jetzt geschlossen. Nicht-W25-empfohlen, aber richtige Prioritaet.

### Frontend-Feature-Auslieferungen (FT/FO/FD/P-Serie)

Frontend hat 12+ benannte Feature-Marker in 15 Wochen ausgeliefert. Grobe Kategorisierung:

- **FT-1..FT-5** (Form-Tab-UX): Modal-Struktur, Detail/Eingänge/Verteilung-Tabs, Template-Modal, Grid/List-Toggle, Status-Quick-Filter.
- **FT-2a Field-Validation**: `patternType` (free/plz/phone/iban Presets), min/max Length + Value. Kommentar im Store: *"we never store a free-form regex — too error-prone for KMU users"*. Richtige KMU-Doktrin.
- **FT-2b Rating + Page-Break + Thanks-You + Redirect**: rating field mit `ratingScale` (5=Sterne, 10=NPS), page-break mit `pageTitle`, `thankYouMessage` (Post-Submit-Text), `redirectUrl` (Post-Submit-URL).
- **FO-4 Notifications**: `recipients: string[]` + `confirmToSubmitter: boolean`. Mocked SMTP im Demo, echtes Dispatch ist "Luke's lane" (Kommentar). Attached-Snapshot-Pattern (`SubmissionNotificationDispatch` gespeichert am Submission zur Zeit des Eingangs) — richtig fuer Audit-Trail.
- **FO-6 Conditional-Logic-Evaluation**: `equals/not_equals/contains` bei Render (Preview + Public). Backend hat die Struktur laengst (models.go:88-93 FieldCondition), aber die Auswertung passierte vorher clientseitig nicht — jetzt implementiert.
- **FD-0 Lifecycle `closed`-Status**: 4-Zustand-Machine `draft → active → closed → archived`. Kommentar: *"Darien decision 2026-06-20"* — historisch nachvollziehbar. **Backend hat weiterhin nur 3 Zustaende** — siehe Diskrepanz-Sektion.
- **FD-1 Share-Dialog + Channel-Wahl**: `channel: 'link'|'email'|'embed'|'qr'` — Frontend generiert Distributions-Metadata. **Backend `form_share_tokens` hat keine channel-Spalte** — Frontend-only Field-Attribute.
- **FD-2 Distribution-Overview**: Share-Links-Liste mit Toggle/Delete + Views-Counter + Submissions-Counter. **Views-Counter ist backend-lose** — Backend hat nur `submission_count`.
- **P2 Intake-Role-Dropdown**: Feld-Editor zeigt Rollen-Auswahl (subject/description/priority/category/requester_name/requester_email) wenn Draft an `helpdesk_ticket` gebunden ist. **Backend hat symmetrische Validation** (validIntakeRoles) — hier ist die Drift null, symmetrisch entwickelt.
- **Consent + Rating Pseudo-Types**: `consent` (DSGVO-Zweckbindungs-Checkbox mit privacyUrl-Link), `rating` (Sterne / NPS). **Beide Frontend-only Pseudo-Types**, Kommentar im Store: *"not in the backend proto whitelist"*. Werden beim Save gesilent verworfen? Oder werden sie als `text` erwatch neu getypt? Ungeprueft — potentieller Bug.
- **FormulareSettingsPanel.tsx** (284 LOC neu) — Modul-Praeferenzen (Default-Tab, Default-Export-Format, Default-View), Tenant-Settings-Sektion. Konsistent mit W38-Wiki-`Module-Settings-Shell`-Pattern.

**LOC-Bilanz Frontend:** FormularePage.tsx 2457→5605 (+128%) + Settings-Panel 284 (neu) + api-client 255→312 (+22%) + api-types 195→318 (+63%) + store 175→248 (+42%) = **6767 LOC gesamt** (vs W25 3082 LOC) = **+119%**. Backend-Prod-Code +25%. **Frontend liefert 4.8× schneller als Backend** — Drift-Vergroesserung ist strukturell erwartbar.

---

## Neue Struktur-Drift Backend ↔ Frontend (Zyklus 2)

Die W25-Diskrepanzen und der neue Zustand:

### Alt-Drift-Status

| W25-Diskrepanz | Status W40 | Kommentar |
|---|---|---|
| **#1 Field-Type-Union (email fehlt)** | ✅ Behoben | `email` jetzt in FormFieldType (stores/formulare.ts:20) |
| **#2 FieldOption-Struktur (string[] vs {value,label})** | ❌ Bleibt | Frontend `options?: string[]` (line 58) — Roundtrip-Label-Loss weiter aktiv |
| **#3 FormAction Frontend-only** | ⚠️ Zombie | FormAction (email/task/crm_contact) unveraendert mit gleichem Kommentar "not yet persisted to backend" — aber Cosmi hat via B6-Intake-Binding einen *anderen* Weg zur Post-Submission-Action geloest. Frage: Ist FormAction jetzt Legacy-UI-Zombie? Sollte entweder gestrichen oder als *ergaenzender* Weg zu Intake-Binding backend-persisted werden. |
| **#4 Per-Field-Page-Assignment** | ❌ Bleibt | Frontend `page?: number` (line 74) frontend-only. Backend `FormField` hat kein Page-Feld. |

### Neu-Drift W40

| Neue Diskrepanz | Frontend | Backend | Konsequenz |
|---|---|---|---|
| **#5 `consent`-Pseudo-Type** | `type: 'consent'` mit `consentText` + `privacyUrl` | `validFieldTypes` kennt nur 9 Typen, `consent` fehlt | Save-Zeit-Reject (`ErrInvalidFields`) — muss der User erst Backend-Bypass erwatch |
| **#6 `rating`-Pseudo-Type** | `type: 'rating'` mit `ratingScale: 5\|10` | dito | dito |
| **#7 `closed`-Status** | `FormSchemaStatus: 'draft'\|'active'\|'closed'\|'archived'` (4) | `FormSchemaStatus: draft/active/archived` (3) | Frontend-Setter `closed` → Backend gibt vermutlich Error zurueck (Status-Enum-Validation unbekannt) oder speichert als String. Latent-Bug. |
| **#8 FormSchema-Extra-Fields** | `notifications, closedMessage, thankYouMessage, redirectUrl` alle in FormSchema | Backend `FormSchema`-Struct hat keins davon | Frontend sendet die Felder, Backend gRPC-Wrapper ignoriert oder erroret. Nicht direkt in dieser Session validiert (waere Sprint-Item: gRPC-Proto-Read). |
| **#9 ShareLink `channel`** | `channel: 'link'\|'email'\|'embed'\|'qr'` | `form_share_tokens` hat keine channel-Spalte | Frontend zeigt Distributions-Kanal-Auswahl, Backend ignoriert — nur Token-Link ist real. |
| **#10 ShareLink `views`-Counter** | `views: number` neben `submissions: number` | Backend hat nur `submission_count` | Views ist Frontend-Analytik-Fantasie. |
| **#11 FormShareLink `url`** | `url: string` (public fill-out URL mit "placeholder host until FD-4") | Backend gibt `token` zurueck, kein url | Frontend baut URL clientseitig — akzeptabel, aber "placeholder host" ist Todo. |
| **#12 FormShareLink `status`-Derivation** | `status: 'active'\|'expired'\|'disabled'` mit Frontend-Logik | Backend `FormShareLink.Status(now)` liefert exakt dieselben 3 (form_share.go:66-77) | **Symmetrisch** — kein Drift. Beispiel wie es geht: beide Seiten haben derselben Enum + derselben Regel-Aufloesung. |

**Struktur-Interpretation:** Die Drift-Achsen 5-11 sind alle "Frontend hat FEATURE-erweitert, Backend nicht mitgezogen". Das ist **das gleiche Anti-Muster wie W25**, nur an mehr Stellen. **Sprint-2-Hygiene-Item wird zu Sprint-2+Sprint-3-Doppel-Item** — der Anti-Drift-Sweep muss jetzt 7 Diskrepanzen (4 alte + 3-5 neue je nach Zaehlung) statt der urspruenglichen 4 handhaben, plus einen FormularePage-Refactor der 2.3× so gross geworden ist.

---

## Cosmi-IST-Stand W40 (Delta zu W25)

### Backend (`backend/internal/formulare/`, 6353 LOC)

**LOC-Bilanz:**
- **Production-Code:** ~2637 LOC (W25: ~2117 LOC, **+25%**) ueber 7 Files (`errors.go` 25, `form_share.go` 357, `models.go` 137, `postgres_repository.go` 957, `repository.go` 98, `service.go` 840, `worker.go` 223).
- **Test-Code:** ~3716 LOC (W25: ~1753 LOC, **+112%**) ueber 8 Test-Files (`form_share_db_test.go` 128, `form_share_test.go` 289, `postgres_repository_db_test.go` 923, `service_test.go` 1530, `tenant_isolation_phase2_test.go` 79, `tenant_write_test.go` 120, `worker_test.go` 560, `xlsx_formula_injection_test.go` 87).
- **Test-Ratio:** Test/Production = **141%** (W25: 83%). Cosmi-Formulare ist jetzt eines der best-getesteten Module in Cosmi (Vergleich: helpdesk 39% zu W24, unbekannter Wert W40). Ein `postgres_repository_db_test.go` mit 923 LOC deutet auf echte DB-Integrations-Tests, nicht nur Mocks — richtig.

**Neue Migrationen seit W25:**
- **000292** — `form_schemas.intake_target_id TEXT NULL` (B6)
- **000293** — `form_share_tokens` Table (B8, mit RLS)
- **000317** — `form_submissions.anonymized_at TIMESTAMPTZ NULL` (Retention)

**Neue Files seit W25:**
- **`form_share.go`** (357 LOC) — Public-Share-Token-Service (CreateShareLink, ListShareLinks, RevokeShareLink, SubmitByShareToken)
- **`form_share_test.go`** (289 LOC) + `form_share_db_test.go` (128 LOC) — Share-Link-Coverage
- **`postgres_repository_db_test.go`** (923 LOC) — echte Postgres-Integrations-Tests
- **`tenant_write_test.go`** (120 LOC) — Cross-Tenant-Write-Test
- **`xlsx_formula_injection_test.go`** (87 LOC) — Formula-Injection-Test

**gRPC-Service-Wachstum:** W25 hatte 21 RPCs. W40 hat mindestens die W25-21 + Share-Link-RPCs (ListShareLinks, CreateShareLink, RevokeShareLink) sichtbar in `route_formulare.go:1001-... HandleListShareLinks/HandleCreateShareLink/HandleRevokeShareLink`. Wahrscheinliche neue Zahl: 24-26 RPCs. Nicht direkt aus proto gelesen — Sprint-Item fuer Detail-Verification.

**Sicherheits-Status W40:**
- ✅ **Tenant-Isolation Phase 2** — unveraendert.
- ✅ **HMAC-Webhook-Signing** — unveraendert.
- ✅ **SSRF-Schutz** — GELIEFERT via `safehttp.New()` in Worker.
- ✅ **CSV/XLSX-Formula-Injection-Schutz** — GELIEFERT via `csvutil.NeutralizeFormulaCell()`.
- ✅ **Public-Rate-Limit** — GELIEFERT via Gateway-Middleware.
- ✅ **Share-Token-Sicherheit** — GELIEFERT (3-Step-Lookup + Timing-safe 404 + Race-Trx + File-Refusal + Body-Cap).
- ✅ **GDPR-Retention** — GELIEFERT (Anonymization-Marker + Retention-Worker-Handler).
- ✅ **Idempotency** — via Gateway-Middleware (unveraendert seit W25).
- ⚠️ **KEIN Honeypot** — 9 Field-Types unveraendert. Empfehlung W25 offen.
- ⚠️ **KEIN Captcha** — CaptchaVerifier existiert im Repo (`security/captcha.go`), aber nicht an formulare-Public-Route gebunden. 5-Zeilen-Fix.
- ⚠️ **KEIN Submission-Spam-Status** — `new/read/archived` unveraendert.
- ⚠️ **IP-Address-DSGVO-Gate fehlt weiter** — models.go:103 Kommentar "DSGVO: nur mit Consent", Service stempelt IP unconditional (parseIPAddress liefert nil nur bei Parse-Failure).
- ⚠️ **KEIN AI-Layer** — keine ai/-, compliance/-, mcp-server/-Package im Repo.

### Frontend (`desktop/src/renderer/src/modules/formulare/` + shared)

**LOC-Bilanz:** 6767 LOC gesamt (W25: 3082 LOC, **+119%**). FormularePage.tsx 5605 LOC (W25: 2457 LOC, **+128%**) — Refactor-Regression.

**Neue Files seit W25:**
- **`settings/FormulareSettingsPanel.tsx`** (284 LOC) — Modul-Settings mit ModuleSettingsShell-Pattern.
- **`stores/formularePrefs.ts`** (nicht direkt gelesen, referenziert aus SettingsPanel) — Persoenliche Praeferenzen.
- **`stores/formulareTenant.ts`** (nicht direkt gelesen, referenziert aus SettingsPanel) — Tenant-Level-Praeferenzen.

**Wachstum-Verteilung im Frontend:**
- FormularePage.tsx +3148 LOC (+128%) — Feature-Marker FT/FO/FD/P
- api/formulare-client.ts +57 LOC (+22%) — Share-Link + Intake-RPCs
- api/formulare-types.ts +123 LOC (+63%) — FormShareLink, FormNotificationConfig, ShareChannel, ShareLinkStatus, FieldValidation, FieldPatternType, SubmissionNotificationDispatch
- stores/formulare.ts +73 LOC (+42%) — FieldValidation, FormNotificationConfig, DraftSchema-Erweiterungen

**Refactor-Notiz:** Ein 5605-LOC-Mono-File ist heute **jenseits jedes vertretbaren Wartungsschwelle**. Zum Vergleich: KMU-Hub-Guidelines (heuristisch) haben typischerweise Component-Files unter 800 LOC. FormularePage.tsx ist 7× ueber die Schwelle. Jede Bug-Fix-PR in diesem File hat exponentiell wachsende Review-Complexity + Merge-Konflikt-Risiko. **P0-Refactor** vor jedem weiteren FT/FO/FD-Sprint.

---

## Konkurrenz-Delta W25 → W40 (Zyklus 2 Markt-Update)

Der Form-Builder-Markt hat sich in 15 Wochen strukturell weiter differenziert. Nicht neu (aus W25 bestaetigt), sondern erweitert:

### Typeform — Q2/Q3-2026-Auslieferungen

Aufbauend auf W25-Baseline (AI Data Enrichment Feb 2026, Growth Flow Mai 2026, Research Flow Juni 2026):

- **Video Responses** (Q3 2026) — User-Antworten koennen jetzt als Video gegeben werden (mit AI-Analyse der Emotion/Sprache-zu-Text). Cosmi hat via `video`-Modul die Tech-Basis (LiveKit-Backend), koennte theoretisch Reversal-Story bauen — aber kein Sprint-Item.
- **Create form from HubSpot properties** (Q3 2026) — AI generiert Form-Schema aus HubSpot-Custom-Field-Liste des Kunden. **Das ist exakt das Cosmi-USP-Muster aus W25-Empfehlung 2(b)** — "GenerateFromCrmContact(contact_id)" — nur eben mit HubSpot als Datenquelle. Konkurrenz hat die Idee zuerst geliefert.
- **ISO/IEC 42001 Certification** (Juni 2026) — AI-Governance-Zertifizierung. Neuer **Compliance-Tabellenstake** fuer Q4-2026-Enterprise-Deals. Cosmi hat keine ISO-27001, keine SOC-2, keine ISO-42001 — Formbricks 4.7 SOC-2-Type-II bleibt der DACH-Open-Source-Anker (W25-Learnings unveraendert).
- **AI Info Page** (`typeform.com/ai-info`) — dedizierte Landing-Page, wie AI-Assistants (Claude/ChatGPT) mit Typeform arbeiten sollen. Das ist SEO/AI-Discoverability-Marketing — Cosmi hat kein `cosmi.app/ai-info`.

### Tally.so — MCP-Reife-Sprung

Aufbauend auf W25-Baseline (MCP-Server Beta, 20+ Tools, OAuth):

- **MCP-Server jetzt in Claude+ChatGPT One-Click-Directory** (Q3 2026) — Anwender findet Tally-MCP mit einem Klick in der Directory-Sicht. Cosmi ist nirgends indexiert.
- **21 Tools Statement** (up from 20+) — reife Werkzeug-Sammlung, kostenlos auch im Free-Tier.
- **Fetch submissions into chat + analyze responses with AI** — MCP-Server ermoeglicht "summarize NPS feedback in Slack from last week's forms" per Chat-Prompt. **Cosmi kann das kraft der Ist-Formulare-gRPC-RPCs prinzipiell auch**, aber ohne MCP-Adapter ist die Konvertierung 0→100 (nichts sichtbar, alles baubar).
- **Cursor-Support hinzugefuegt** — Tally-MCP funktioniert jetzt in Cursor-IDE zusaetzlich zu Claude+ChatGPT. Trend-Signal: Developer-Adoption jenseits der zwei grossen LLM-Chats.

### JotForm — MCP + AI-Agents Live

Aufbauend auf W25-Baseline (AI Agents seit Anfang 2025, Voice-Add-on):

- **MCP-Server offiziell im Claude+ChatGPT-Directory** (Q3 2026) — paid plans only, aber directory-listed.
- **AI Agents mit GDPR-Support** (Sep 2026-Update per Web-Search) — dedizierte "GDPR Compliance | JotForm AI Agents" Landing-Page. Antwort auf EU-AI-Act Art. 50 als Verkaufs-Story.

### Fillout — GDPR built-in + AI-Free-Tier

Aufbauend auf W25-Baseline (AI-Form-Generation aus Prompt/PDF, 40+ Question-Types):

- **1000 Responses/Monat mit Full AI Generation im Free-Tier** — aggressive KMU-Preisstrategie. Cosmi-Formulare 2-EUR-Modul-Anker ist weiter attraktiv, aber Fillout-Free-Full-AI ist noch attraktiver.
- **GDPR built in by default** — Marketing-Formulierung fuer EU-Sales.

### Formbricks — SOC-2-Type-II stabilisiert

- **SOC-2-Type-II-Certification** aus 4.7-Release ist stabil, DACH-Open-Source-Enterprise-Referenz. Weiterhin nicht direkter Cosmi-Konkurrent (Survey-only), aber Compliance-Marker-Vorbild.

### EU-AI-Act Art. 50 — Live seit 2026-08-02, W40 = Tag 57

- **Enforcement live seit 2. August 2026** (W25 hat das als Zukunft prognostiziert). Baker Botts + Cloud Security Alliance + European Commission publizieren September-2026 Praxis-Guides.
- **Grace-Period bis 2. Dezember 2026** fuer Machine-Readable-Marking (Deepfake/Synthetic-Content) — **66-Tage-Fenster ab heute (W40)** fuer Cosmi-Wave-7C-Meeting-AI-Summary Retrofit + AI-Form-Generation-Roadmap.
- **Penalty**: €15 Mio oder 3% Welt-Umsatz — unveraendert seit W25-Baseline.
- **Enforcement-Authorities**: National Competent Market Surveillance Authorities. DACH: BNetzA (DE), BAKOM (CH), RTR (AT).
- **Cosmi-Lage** (verifiziert per Directory-Check heute): kein `backend/internal/compliance/`-Package, kein `backend/internal/ai/providers/router/`-Package, kein `<AIDisclosureBanner>`-Frontend-Component (nicht separat gegrept, aber W38-Verweis auf grep-Miss in kmuhub stimmt weiter). **Wave-7C Meeting-AI-Summary im video-Modul laeuft seit 2026-08-02 im Non-Compliance-Fenster = Tag 57 per heute**.
- **Cosmi-Formulare-Bezug**: Cosmi hat heute *keine* AI-Funktion in `formulare`. Das ist paradoxerweise die **einzige Absicherung** — Art. 50 greift nicht, weil kein AI. Sobald AI-Form-Generation (W25-Empfehlung 2) startet, muss Disclosure-Layer *vorher* stehen. Chance: **Disclosure-by-Design als Sprint-0-Prep** vor jeder AI-Formulare-Auslieferung.

### Anti-Bot-Landschaft (Community-Standard-Update)

Aus den 2026-Anti-Bot-Vergleichen (Prospect Hub, Pi Stack, ALTCHA-Community):

- **Cloudflare Turnstile** bleibt DACH-KMU-Empfehlung fuer Cloud-Verifier (invisible, EU-Datenschutz-Policy, kein WebGL-Fingerprint mehr seit W23-Fix).
- **ALTCHA** (privacy-first, no-cookies, GDPR-out-of-the-box) — neue Empfehlung fuer Self-Hosted-Sensibilitaet. Cosmi-Self-Host-Kunden mit strenger DSGVO-Interpretation koennen Cloudflare vermeiden.
- **hCaptcha Privacy-Mode** — Alternative fuer Kunden mit Cloudflare-Zoegern.
- **Honeypot als Minimum-Viable-Layer** — jeder 2026-Vergleich sagt: Honeypot + Rate-Limit filtert 90% der Bot-Noise, Captcha ist die Backstop-Schicht. Cosmi hat heute nur den Rate-Limit-Layer.

**Empfehlung** (Konkretisierung W25 1a-c): Honeypot als Pflicht-Grundschicht (3 Tage), Captcha-Slot mit Turnstile-Default + ALTCHA-Self-Host-Option + hCaptcha-Alt (7 Tage), Redis-Rate-Limit-Erweiterung um Per-Schema-Cap (2 Tage) — 12 Tage Sprint statt urspruenglich 16, weil safehttp+publicRateLimit-Basis schon steht.

### MCP-Server-Marktreife (Q3-2026)

**Von Tally-Marktforschung** (`tally.so/help/best-mcp-form-builders`): Q3-2026-Ranking (Form-Builder-Kategorie):
1. **Tally** — best free, 21 tools, native OAuth, Claude+ChatGPT+Cursor-Directory
2. **JotForm** — mature paid MCP, Claude+ChatGPT-Directory
3. **Typeform** — Beta MCP, im Directory unterwegs

**Cosmi ist im 2026-MCP-Form-Builder-Ranking gar nicht gelistet, weil kein MCP-Server existiert.** Das ist ein **wachsender Kompetitiv-Nachteil** — MCP wird Q1/2027 wahrscheinlich Standard-Erwartung, wie REST-API 2018.

---

## Konkurrenz-Vergleichstabelle W40

| Feature | Cosmi-Formulare W40 | Cosmi-Formulare W25 | Typeform | Tally | Fillout | JotForm | Formbricks |
|---|---|---|---|---|---|---|---|
| **Self-Host EU** | ✅ Frankfurt | ✅ Frankfurt | ❌ | ❌ | ❌ | ❌ | ✅ Docker |
| **Field-Types-Anzahl** | 🟡 9 (Backend) + 2 Frontend-Pseudo (consent/rating) | 🟡 9 | ✅ 30+ | ✅ 20+ | ✅ 40+ | ✅ 30+ | 🟡 ~15 |
| **Conditional Logic** | 🟢 1-Cond +Frontend-Evaluation (FO-6 delivered) | 🟡 1-Cond (nicht evaluiert im Preview) | ✅ Multi-Cond+AND/OR | ✅ Multi-Cond | ✅ Multi-Cond+DB-Query | ✅ Multi-Cond | ✅ Event-based |
| **Native E-Signature** | ❌ | ❌ | ❌ | ✅ Pro | ✅ | ✅ | ❌ |
| **Native Payment (Stripe)** | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **File-Upload-Backend** | 🟡 Field-Type + share-token-refusal + no-storage-hook | 🟡 nur Field-Type | ✅ | ✅ 10MB Free | ✅ Business | ✅ | 🟡 Beta |
| **Multi-Page Forms** | 🟡 PageCount + Frontend-per-Field-Page (drift #4) | 🟡 PageCount-only | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Rating / NPS** | 🟡 Frontend-Pseudo-Type (drift #6) | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ NPS-Kern |
| **DSGVO-Consent-Field** | 🟡 Frontend-Pseudo-Type (drift #5) | ❌ | 🟡 als Text | 🟡 als Text | 🟡 als Text | ✅ dedicated | ✅ dedicated |
| **Partial Submissions** | ❌ | ❌ | ✅ | ✅ Pro | ✅ | ✅ | ✅ |
| **Hidden Fields / URL-Pre-Fill** | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Honeypot / Anti-Spam-Default** | ❌ **FEHLT** | ❌ **FEHLT** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Captcha-Slot (Turnstile/hCaptcha/ALTCHA)** | ❌ CaptchaVerifier-Klasse vorhanden, nicht gewired | ❌ FEHLT | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Rate-Limit pro Form/IP** | ✅ Gateway-Middleware (Per-IP) | ❌ FEHLT | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Public-Share-Tokens (secure)** | ✅ 3-Step-Lookup, Timing-safe 404, Race-Trx, File-Refusal | ❌ IsPublic-Flag ohne Token | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Webhook (HMAC-Signed)** | ✅ sha256 | ✅ sha256 | ✅ | 🟡 Pro | ✅ | ✅ | ✅ |
| **Webhook Exp-Backoff + Dead-Letter** | ✅ 30s/2m/10m/30m/2h, 5 attempts | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **SSRF-Schutz auf Webhook-Egress** | ✅ safehttp (RFC1918+AWS-Meta-Block) | ❌ FEHLT | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CSV/XLSX-Formula-Injection-Schutz** | ✅ csvutil.NeutralizeFormulaCell + dedicated test | ⚠️ ungeprueft | ✅ | ✅ | ✅ | ✅ | 🟡 |
| **CSV/XLSX-Export** | ✅ BOM-UTF-8 + excelize | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Submission-Anonymization (Retention)** | ✅ anonymized_at + Retention-Handler | ❌ FEHLT | 🟡 Consent-basiert | 🟡 Data-Retention Controls Business | 🟡 | ✅ GDPR-Center | ✅ |
| **Cross-Modul-Intake-Binding (form→ticket/deal/etc)** | ✅ B6: helpdesk_ticket delivered, generisches Pattern | ❌ FEHLT | ❌ | ❌ | 🟡 externe DB-Connectoren | ❌ | ❌ |
| **AI Form-Generation (Prompt/PDF)** | ❌ FEHLT | ❌ FEHLT | ✅ Q1 2026 | 🚧 via MCP | ✅ | ✅ | ❌ |
| **AI Follow-Up-Questions** | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **AI-Pre-Fill / Enrichment** | ❌ | ❌ | ✅ Data Enrichment 2026 | ❌ | ❌ | ❌ | ❌ |
| **MCP-Server (Claude/ChatGPT-Directory)** | ❌ FEHLT (Empfehlung 15 W ignoriert) | ❌ FEHLT | ✅ im Directory (Q3 2026) | ✅ Free, 21 Tools, im Directory | ❌ | ✅ Paid, im Directory | ❌ |
| **EU-AI-Act Art. 50 Disclosure** | n/a (keine AI) — vermeidet Risiko | n/a | ⚠️ retrofit | ⚠️ retrofit (MCP) | ⚠️ retrofit | ⚠️ retrofit | n/a |
| **ISO/IEC 42001 (AI-Governance)** | ❌ | ❌ | ✅ Juni 2026 | ❌ | ❌ | ❌ | ❌ |
| **SOC-2-Type-II** | ❌ | ❌ | ✅ | 🟡 Cloud | ✅ | ✅ | ✅ 4.7 2026 |
| **Submission-Spam-Status** | ❌ nur new/read/archived | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Pricing-Start (€/User-Monat)** | **2 EUR** | 2 EUR | $25 / $83 fuer 10k | $0 Free / $29 Pro | $19 Starter | $34 Bronze | $0 Self-Host |

**Delta-Lesarten:**

**Cosmi hat 5 neue ✅-Zellen seit W25:** SSRF-Schutz, CSV-Injection-Schutz, Rate-Limit (Gateway), Public-Share-Tokens (secure), Submission-Anonymization/Retention, Cross-Modul-Intake-Binding. Das sind **6 substanzielle Struktur-Auslieferungen in 15 Wochen** — signifikant, wenn man bedenkt dass ein Team parallel den gesamten Cross-Modul-B6-Layer gebaut hat.

**Cosmi hat 0 neue ❌-Zellen geschlossen bei den Kernluecken:** Honeypot, Captcha, AI-Form-Generation, MCP-Server, ISO/SOC-2 — alle unveraendert offen.

**Zwei neue Achsen wo Konkurrenz Cosmi ueberholt hat:** ISO/IEC 42001 (Typeform Juni 2026) und MCP-Server im Claude/ChatGPT-Directory (Tally+JotForm+Typeform, Q3 2026). Diese zwei Achsen waren W25-Empfehlungen mit klarem Sprint-Aufwand-Marker (SOC-2-Roadmap-Marker + 5-7-Tage-MCP-Spike) — beide unaddressiert.

---

## Top-3 Strategische Empfehlungen W40

### 1. **Anti-Spam-Trias jetzt sofort (P0, Live-Production-Risk, 12 Tage Sprint)**

**Kontext:** W25-Baseline hat das als "Pflicht-Stake VOR Public-Form-GA" formuliert. **B8-Public-Share-Tokens ist inzwischen live** (`form_share_tokens`-Migration deployt, `SubmitByShareToken` in Production, Public-Route registriert). Die Bedingung "vor GA" ist **bereits ueberschritten**. Anti-Spam-Trias ist ab jetzt kein Sprint-Item-vor-Launch, sondern **Live-Production-Absicherung**.

**Was:**

(a) **Honeypot-Field-Type** — 3 Tage. Neuer FormField-Type `honeypot` in `service.go:44 validFieldTypes`. Frontend rendert hidden Input mit `display: none + tabindex=-1 + autocomplete="off"`. Backend `service.CreateSubmission` + `service.SubmitByShareToken` rejected Submission mit nicht-leerem Honeypot (HTTP 200 an Client, `status=spam` in DB). **Sprint-Owner: 1 Backend + 1 Frontend + 0.5 Tests.**

(b) **Captcha-Slot bind an Formulare-Public-Route** — 4 Tage (nicht 7 wie W25, weil `CaptchaVerifier`-Klasse in `internal/security/captcha.go` schon existiert). Wire in `route_formulare.go RegisterPublicRoutes`: neben `publicRateLimit` einen `RequireCaptcha`-Middleware, der `siteverifyResponse` bei Turnstile/hCaptcha/ALTCHA/reCAPTCHA prueft (alle vier haben gleiche JSON-Shape, CaptchaVerifier-Klasse ist provider-agnostisch). Tenant-Settings: `formulare.captcha.provider (none/turnstile/hcaptcha/altcha)` + `formulare.captcha.site_key` + `formulare.captcha.secret`. Default DACH-KMU: `turnstile` mit fallback zu `honeypot-only` wenn kein Site-Key konfiguriert. **Sprint-Owner: 2 Backend + 1 Frontend + 1 Tests.**

(c) **Rate-Limit-Erweiterung mit Per-Schema-Cap** — 2 Tage. Redis-basiert (Cosmi hat Redis-Infrastruktur bereits — dialer/helpdesk-Modul nutzen es). Cap-Regel: 10 Submissions/IP/Minute (Gateway hat wahrscheinlich Global-Cap, muss verifiziert), plus **1000 Submissions/Schema/Tag** (neuer Layer), konfigurierbar pro Schema. **Submission-Status erweitern um `spam`** (Enum-Migration: `ALTER TYPE form_submission_status ADD VALUE 'spam'` — vorsicht, unversioned Postgres-Enum-Migration ist restart-heavy; besser: Migration mit temp-column-swap). **Sprint-Owner: 1 Backend + 0.5 Migration + 0.5 Tests.**

(d) **IP-Address-DSGVO-Gate** — 2 Tage. `models.go:103` Kommentar sagt "DSGVO: nur mit Consent", aber Service stempelt IP unconditional. Loesung: `CreateSubmissionInput.ConsentIPLogging bool` Flag; wenn false → IP nicht persistieren, wenn true → IP mit anonymize-after-N-days-Retention persistieren. Verbinden mit Consent-Field-Typ (Drift #5) — wenn Frontend `consent`-Field mit `purpose = "ip_logging"` submittet, wird `ConsentIPLogging=true` implizit. **Sprint-Owner: 1 Backend + 0.5 Frontend + 0.5 Tests.**

(e) **Feature-Flag-Gate B8** — 0.5 Tage. `modules.formulare.public_share_tokens` Feature-Flag pruefen und default zu **false** setzen bis Anti-Spam-Trias abgeschlossen. Alle bereits-mintete Tokens bleiben, aber neue MintCreateShareLink-Requests werden abgelehnt. Nach Trias-Delivery Flag auf true.

**Total-Sprint:** ~12 Tage. **Priorat: NOW.**

**Begruendung:**
- **EDPB CEF 2026 (Art. 12-14 Transparenz-Enforcement)** laeuft seit Maerz 2026 in 25 EU-DSBs — inzwischen 30 Wochen aktiv. Formulare mit IP-Logging ohne Consent-Gate ist genau die Klasse Verstoss, die CEF-2026 dokumentiert.
- **OLG-Hamm-Urteil zu AI-Vorausfuellung** (W20-Carry-Forward) — Cosmi hat noch keine AI-Vorausfuellung, aber wenn W25-Empfehlung 2 kommt, muss Consent-Field bereit sein.
- **noyb-Klagen gegen "Pay-or-Okay"-Modelle** (W23) — irrelevant fuer Cosmi-Modul-Pricing, aber DPA/Consent-Doktrin-Standard verschaerft sich weiter.
- **Cosmi-Sales-Story**: "Cosmi-Formulare ist der einzige EU-Self-Host-Form-Builder mit DSGVO-Consent-Gate fuer IP-Logging by Default" — verkaufsfaehiges Differenzierungs-Argument gegen Tally-Belgium und Formbricks-Cloud, die IP unconditional loggen.

### 2. **AI-Compliance-Foundation-Sprint mit Formulare als Retrofit-Target #2 (P0, 66-Tage-Grace-Deadline, 6-8 Wochen Sprint)**

**Kontext:** W39-helpdesk-deepdive hat AI-Compliance-Foundation-Sprint (Multi-Provider-Router + Article-50-Disclosure + AI-Draft-Endpoint als 6-8-Wochen-Sprint-Paket) als P0 identifiziert, mit Wave-7C-Meeting-AI-Summary als **Erst-Retrofit-Target**. Formulare ist heute **kein Retrofit-Target** (keine AI-Funktion existiert), aber **Formulare ist der beste Neu-Bau-Kandidat**, weil:

- AI-Form-Generation ist Konkurrenz-Tabellenstake (Typeform, Fillout, JotForm alle live).
- Cosmi hat **strukturelle Cross-Modul-Story** (W25-Empfehlung 2) die keine Konkurrenz replizieren kann.
- **Formulare hat null AI-Funktion heute** — kann Disclosure-by-Design als Blueprint einbauen, statt retrofit.
- 66-Tage-Fenster bis 2026-12-02 Grace-Period-Ende fuer Machine-Readable-Marking — Cosmi kann als **erster EU-Form-Builder** mit vollstaendiger Art. 50-Compliance-by-Design in DACH-Sales-Kaenaelen positionieren.

**Was:**

(a) **AI-Compliance-Foundation-Sprint** (6-8 Wochen, W39-P0 unveraendert):
- `backend/internal/ai/providers/router/` — Multi-Provider-Router (Anthropic-primary, Mistral-EU-fallback, Muse-Glimmer-Self-Host, Ollama-Local, DeepSeek-Non-PII-Batch, ISO-Whitelist per Tenant).
- `backend/internal/compliance/ai_disclosure/` — Article-50-Disclosure-Wrapper, Prompt-Hash-Audit-Log (3-Jahre-Retention), Human-Escalation-Trigger.
- `frontend/components/ai-disclosure/` — Persistent-Visual-Indicator ("AI Assistant" Badge), First-Message-Notice, "AI-generated, please review" pro Feld.
- **Erst-Retrofit-Target: video-Modul Wave-7C Meeting-AI-Summary** (schliesst 57-Tage-Non-Compliance-Fenster).

(b) **Formulare als Neu-Bau-AI-Layer** (nach Foundation-Sprint, Q4-2026 Sprint 1):
- `backend/internal/formulare/ai/` — Cosmi-AI-Client-Wrapper mit Provider-Router-Bindung.
- **Cross-Modul-Schema-Source-Funktionen** (W25-Empfehlung 2b):
  - `GenerateFromCrmContact(contact_id)` — Form-Schema aus CRM-Contact-Custom-Fields (P1, direkte Cross-Modul-Story mit W39-helpdesk_ticket_contact_org-Migration + W34-material_availability-Pattern).
  - `GenerateFromIntakeTarget(target_id)` — nutzt Intake-Registry aus B6, generiert Form-Schema mit korrekten Rollen-Zuweisungen fuer target-registrations (heute `helpdesk_ticket`, morgen `crm_deal`, `dialer_callback`). **Das ist die tightere Cross-Modul-Story als W25-Empfehlung 2b, weil sie an B6 anknuepft.**
  - `GenerateFromWikiArticle(article_id)` — Onboarding/Quiz-Form aus Wiki-Article-Strukturen (nach W38-P0 wiki-embedding-Aktivierung).
  - `GenerateFromPrompt(prompt)` — Generic Fallback analog Typeform/Fillout.
- **Disclosure-by-Design im Form-Builder**: AI-generierte Felder haben `ai_generated: true`-Flag im FormField-JSONB, Frontend rendert Badge, Public-Form zeigt Footer "AI-generated form template, customised by [Tenant-Name]".

(c) **MCP-Server-Adapter fuer Cosmi-Formulare** (W25-Empfehlung als Sub-Deliverable, 5-7 Tage): siehe Empfehlung 3.

**Total-Sprint:** 6-8 Wochen Foundation + 3-4 Wochen Formulare-AI-Layer. **Deadline: 2026-12-02 Grace-Period-Ende (66 Tage)** fuer Foundation-Alone; Formulare-AI-Layer kann Q1-2027 nachziehen wenn Deadline greift.

**Begruendung:**
- **Regulatorische Notwendigkeit**: 66-Tage-Fenster fuer Machine-Readable-Marking, danach €15 Mio Bussgeld-Risk fuer Wave-7C-Meeting-AI-Summary.
- **Sales-Notwendigkeit**: Q4-2026-DACH-Enterprise-RFPs werden Art. 50-Compliance-Nachweise fordern. Cosmi als "AI-Act-compliant by Design" positioniert ist Alleinstellungs-Merkmal gegen US-Cloud-Konkurrenz.
- **Cross-Modul-Marketing-Story**: B6-Intake-Binding gibt jetzt konkretes Sprint-Ready-Fundament fuer `GenerateFromIntakeTarget()` — Cosmi-USP nicht-mehr abstrakt.
- **Technische Basis vorhanden**: `internal/llm/client.go` existiert bereits (Wave-7C nutzt es), Multi-Provider-Router ist der einzige noch fehlende Kern.

### 3. **MCP-Server-Spike + FormularePage-Refactor-Bundle (P1, 3-Wochen-Sprint, hoher Sales-Signalwert)**

**Kontext:** MCP-Server-Empfehlung aus W25 (5-7 Tage) ist 15 Wochen ignoriert. Waehrend dieser 15 Wochen sind Tally + JotForm + Typeform in die Claude+ChatGPT-Directory eingezogen und werden dort als "One-Click-Connector" beworben. Cosmi ist unsichtbar in dieser Sichtbarkeits-Landschaft.

Zugleich hat FormularePage.tsx sich mehr als verdoppelt (5605 LOC). Ohne Refactor werden alle folgenden Feature-Sprints exponentiell teurer. Beide Items zusammen bilden ein 3-Wochen-Sprint-Bundle.

**Was:**

(a) **`cosmi-formulare-mcp` Server-Adapter** (5-7 Tage). Existierende ~24 gRPC-RPCs (21 aus W25 + 3-5 Share-Link + Intake) sind das Fundament. MCP-Wrapper mappt:
- `mcp:cosmi-form-create` → `CreateFormSchema`
- `mcp:cosmi-form-list` → `ListFormSchemas`
- `mcp:cosmi-form-get` → `GetFormSchema`
- `mcp:cosmi-form-update` → `UpdateFormSchema`
- `mcp:cosmi-form-stats` → `GetFormStats`
- `mcp:cosmi-form-submissions-list` → `ListSubmissions`
- `mcp:cosmi-form-share-link-create` → `CreateShareLink`
- `mcp:cosmi-form-share-link-list` → `ListShareLinks`
- `mcp:cosmi-form-share-link-revoke` → `RevokeShareLink`
- `mcp:cosmi-form-webhook-create` → `CreateWebhook`

**Safety-Guardrails** (kopieren von Tally, gutes Vorbild):
- Delete-Operations sind **default disabled**, brauchen explizite Tenant-Setting `formulare.mcp.allow_deletion = true` um freigeschaltet zu werden.
- Bulk-Operations (loesche alle Submissions eines Schemas) sind gar nicht exponiert — nur Single-Item-Operationen.
- Rate-Limit auf MCP-Aufrufe: 60 Ops/Minute/Tenant.
- OAuth-Auth mit dedizierter `formulare:mcp:access`-Permission.

**Cross-Modul-Differenzierung** (das Cosmi-USP-Element gegen Tally-MCP): der gleiche Server exponiert **auch** CRM/Helpdesk/Wiki-Tools (jeder Modul-Service registriert seine RPCs beim shared MCP-Server). Anwender sagt zu Claude "Erstell ein Bewerbungs-Formular, lege auf Submission einen CRM-Kontakt an, fuege den in den Helpdesk-Welcome-Workflow ein" — Cosmi-MCP kann via B6-Intake-Binding: Form generieren → `intakeTargetId=helpdesk_ticket` setzen → Field-Rollen mappen → fertig. Ein Prompt, ein Server, drei Module. Tally-MCP kann nur Form-Tools.

(b) **FormularePage.tsx-Split** (14-18 Tage, Sprint-Backbone-Item). 5605 LOC in 8-10 Sub-Components auftrennen:
- `FormListView.tsx` (Grid+List-View mit Status-Quick-Filter)
- `FormDetailModal.tsx` (Detail/Eingänge/Verteilung-Tabs)
- `FormBuilder/index.tsx` (Editor-Root)
- `FormBuilder/FormFieldList.tsx` (Drag-Drop-Feldliste)
- `FormBuilder/FormFieldEditor.tsx` (Single-Field-Editor mit ValidationPresets + Rating + Consent + Intake-Role)
- `FormBuilder/FormPreview.tsx` (Live-Preview mit Conditional-Logic-Eval)
- `FormBuilder/FormActionsPanel.tsx` (Post-Submission-Actions — heute Zombie, klaeren ob strichen oder als komplementaerer Weg zu B6-Intake ausbauen)
- `FormBuilder/FormWebhooksPanel.tsx` (Webhook-Config)
- `FormSubmissionsTable.tsx` (Submissions-List + Filter + Export)
- `FormDistributionPanel.tsx` (FD-2 Share-Links-Overview)
- `FormLifecycleActions.tsx` (FD-0 Close/Reopen/Archive-Confirmations)
- `FormBuilderHooks/*.ts` (Custom-Hooks fuer Draft-State, Field-Validation, etc)

**Aufwand-Reduzierer**: kein Test-Refactor noetig (nur File-Split, Interfaces bleiben), Feature-Flag-Rollback trivial, PR-Review nur "sehen die neuen Files richtig aus" — Sprint-Owner-Frontend-Lead + Junior-Support machbar.

(c) **Anti-Drift-Sweep #2 (FieldOption struct) + #5+#6 (consent/rating backend-persistence)** — 3 Tage. FieldOption-Migration wie in W25 (Frontend liest beide Formate, schreibt neues, 30-Tage-Backwards-compat). `consent` und `rating` in `validFieldTypes` aufnehmen, `FormField`-Struct um `ConsentText`, `PrivacyURL`, `RatingScale` erweitern (JSONB-additiv, keine Migration). **Neben-Effekt: Diskrepanzen #5+#6 backend-persistent** = 2 Drift-Achsen geschlossen.

**Total-Sprint:** 22-28 Tage (5-7 MCP + 14-18 Refactor + 3 Drift-Fixes). Optional: Diskrepanz #3 FormAction-Zombie klaeren (streichen oder Backend-persistieren), #4 Per-Field-Page hinzufuegen (2 Tage additiv-Migration-frei) — sprint-verlaengert um 4-5 Tage aber schliesst 3 weitere Drift-Achsen.

**Begruendung:**
- **MCP-Server-Fenster wird kleiner**: Q1-2027-Standard-Erwartung waechst. Cosmi als DACH-KMU-Erster mit MCP-Server hat 6-9-Monate-Fenster fuer Sales-Story "Cosmi ist in Claude+ChatGPT-Directory". Nach Q1-2027 ist es "endlich hat Cosmi auch MCP".
- **Cross-Modul-USP-Amplification**: MCP-Server ist der beste Sales-Demo-Kanal fuer die B6-Intake-Story. "Ich sage Claude: Erstell ein Formular, bau ein Ticket, verlinke einen Wiki-Article — ein Prompt" ist unwiderstehlicher als Slide-Deck.
- **Refactor-Blocker fuer AI-Sprint**: Wenn Empfehlung 2 (AI-Formulare-Layer) auf einem 5605-LOC-Mono-File aufsetzt, wird sie doppelt teuer. Refactor-JETZT ist ein Beschleuniger fuer alle Q4/Q1-Sprints.
- **Drift-Kompaktifizierung**: Jede weitere Frontend-Feature-Woche vergroessert Drift. Jetzt schliessen ist billiger als spaeter.

---

## Was widerspricht Cosmi-Strategie (ehrliche Team-Realitaets-Sektion)

Analog W38+W39 — Zyklus-2-Pattern.

**(a) Delivery-Divergenz Frontend vs Backend.** Frontend-Team liefert 4.8× schneller LOC-maessig als Backend-Team. Ist das ein Skill-Gap, Priorisierungs-Gap oder Kapazitaets-Gap? Wenn Frontend jede Woche 12+ Feature-Marker liefert (FT-1..FT-5, FO-4/6, FD-0/1/2, P2, B6-fe, B8-fe) und Backend im gleichen Zeitraum 4 Migrationen + Sicherheits-Sweep + Cross-Modul-Intake-Binding, dann ist das nicht "Backend liefert langsam" — das ist "Backend liefert *tief* in wenigen Punkten, Frontend liefert *breit* in vielen". Beide Muster sind valid. Das Problem ist die **Drift**, nicht die Geschwindigkeit — vier neue Drift-Achsen in 15 Wochen. Anti-Drift-Sweep-Item aus W25 ist ein Dauer-Sprint, nicht ein Einmal-Ereignis. **Frage an Sprint-Lead**: sollte ab jetzt jede Frontend-PR mit Schema-Aenderung eine Backend-PR-Referenz zwingend brauchen (PR-Gate)?

**(b) MCP-Server-Empfehlung 15 Wochen ignoriert.** W25 hat einen 5-7-Tage-Spike-Aufwand veranschlagt. Das ist ein Junior-Backend-Item. 15 Wochen × 5 Arbeitstage = 75 verfuegbare Tage. Wenn 5-7 Tage in 75 nicht passen, dann ist der Bottleneck nicht Kapazitaet, sondern **Priorisierungs-Entscheidung von jemandem**. Wer hat entschieden, dass Anti-Spam + MCP + AI-Compliance-Foundation alle drei nach hinten rutschen, waehrend FD-1 Share-Dialog + FD-2 Distribution-Overview + FT-2a Field-Validation-Presets Prioritaet bekommen? Das ist eine **Product-Owner-Entscheidungs-Prufung**, nicht Team-Kritik. Aber die Entscheidung muss sichtbar gemacht und benannt werden — sonst wiederholt sich das Muster 15 weitere Wochen.

**(c) FormularePage.tsx-Explosion ist Selbst-Bestrafung.** 5605 LOC ist nicht nur "Refactor-Schuld", sondern jede weitere PR in diesem File hat 2-3× hoehere Merge-Konflikt-Wahrscheinlichkeit mit anderer paralleler Feature-Arbeit. Wenn zwei Entwickler gleichzeitig FT-3 und FD-3 bauen wollen, kollidieren sie strukturell im gleichen File. Das ist **Team-Coordination-Kost, nicht nur Code-Aesthetik**. Refactor jetzt ist ein Team-Produktivitaets-Beschleuniger, nicht Kosmetik.

**(d) B6-Intake-Binding ist grossartig, aber unterexploitiert.** Cosmi hat gerade den **konkretesten Cross-Modul-Pattern-Beweis** im Repo gebaut (extensible Registry-Konvention, echter Cross-Service-gRPC-Dispatch, symmetrische FE/BE-Validation). Wo ist die Sales-Slide, die das feiert? Wo ist die Case-Study "Wie Cosmi-Kunde X sein Kontakt-Formular mit einem Klick zum Helpdesk-Ticket macht"? Wo ist der Marketing-Blog-Post "Warum Cosmi das einzige Suite ist, die Formulare nicht als isolierte Datencontainer, sondern als First-Class-Modul-Ziel-Bindung behandelt"? Das ist **fertig-gelieferte Feature-Story ohne PR-Amplification** — der klassische Software-Firmen-Fehler.

**(e) IsPublic-Interpretations-Falle.** Cosmi hat 15 Wochen "IsPublic-Flag existiert im Schema, aber keine Public-Route dazu" gehabt (W25-Baseline-Interpretation: "IsPublic-Mode aktiv" — falsch). Erst B8-Migration hat das aufgedeckt: **die Public-Route existierte gar nicht, `IsPublic` war ein orphaned Flag**. Solche Interpretations-Fallen zeigen: der Intel-Baseline-Report kann nicht 100% code-verlaessliche Konklusionen aus Code-Reads ziehen. Sanity-Check-Regel fuer Deepdive-Autor: bei jeder Sicherheits-Kritik im Baseline (z.B. "Public-Mode ohne Anti-Spam") pruefen, ob der kritisierte Pfad ueberhaupt kontrollflow-erreichbar ist. Sonst produziert der Report False-Positive-P0s.

---

## Quellen

**Cosmi-interne Quellen (Code + Knowledge, Stand 2026-09-28):**
- `/opt/kmuhub/backend/internal/formulare/` — 6353 LOC (Production ~2637 + Tests ~3716)
  - `models.go` (137 LOC) — FormSchema mit IntakeTargetID, FormField mit Role
  - `service.go` (840 LOC) — validIntakeRoles, CreateSubmission, ExportSubmissions mit csvutil.NeutralizeFormulaCell
  - `form_share.go` (357 LOC) — FormShareLink, SubmitByShareToken 3-Step-Sequence
  - `worker.go` (223 LOC) — WebhookWorker mit safehttp.New
  - `postgres_repository.go` (957 LOC), `repository.go` (98 LOC)
  - `errors.go` (25 LOC) — ErrShareLinkNotFound, ErrSchemaNotPublic, ErrShareLinkFileFieldUnsupported, ErrAnswersTooLarge
- `/opt/kmuhub/backend/internal/gateway/route_formulare.go` (1203 LOC) — RegisterRoutes + RegisterPublicRoutes mit publicRateLimit, Share-Link-Handlers
- `/opt/kmuhub/backend/internal/gateway/intake.go` (297 LOC) + `intake_helpdesk.go` (174 LOC) — Cross-Modul-Dispatch-Registry
- `/opt/kmuhub/backend/internal/security/captcha.go` (97 LOC) — Provider-agnostischer CaptchaVerifier (nicht an formulare gewired)
- `/opt/kmuhub/backend/migrations/000292_formulare_intake_target.up.sql` (B6)
- `/opt/kmuhub/backend/migrations/000293_form_share_tokens.up.sql` (B8)
- `/opt/kmuhub/backend/migrations/000317_form_submissions_anonymized_at.up.sql` (Retention)
- `/opt/kmuhub/desktop/src/renderer/src/modules/formulare/FormularePage.tsx` (5605 LOC — Mono-File-Regression)
- `/opt/kmuhub/desktop/src/renderer/src/modules/formulare/settings/FormulareSettingsPanel.tsx` (284 LOC — neu)
- `/opt/kmuhub/desktop/src/renderer/src/api/formulare-types.ts` (318 LOC) — TS-Mirror mit Drift-Achsen
- `/opt/kmuhub/desktop/src/renderer/src/api/formulare-client.ts` (312 LOC)
- `/opt/kmuhub/desktop/src/renderer/src/stores/formulare.ts` (248 LOC) — Zustand mit FormFieldType (+ consent + rating)
- `/opt/kmuhub/.knowledge/datenbank.md:101-102,366-372` — Formulare-Schema-Doku, Share-Token-Muster
- `/opt/kmuhub/.knowledge/security.md:32,45,62,167,255,330` — Formulare-Tenant-Isolation, DSAR-Modul-Registrierung
- `/opt/kmuhub/.knowledge/architektur.md:26,93,106,125,210,239,328` — Service-Port :50064, Route, Modul-Slug, Webhook-Trigger
- `/opt/kmuhub/.knowledge/testing.md:58` — Formulare 54% Test-Coverage-Statement (jetzt vermutlich hoeher aufgrund neuer Tests, nicht direkt verifiziert)

**Baseline-Report:**
- `/opt/zentria-intel/monthly/2026-06-15-deepdive-formulare.md` — W25/Zyklus-1-Baseline

**Zentria-Intel Cross-Reports:**
- `/opt/zentria-intel/monthly/2026-08-24-deepdive-crm-core.md` (Zyklus 2 W35)
- `/opt/zentria-intel/monthly/2026-08-31-deepdive-dialer.md` (Zyklus 2 W36)
- `/opt/zentria-intel/monthly/2026-09-07-deepdive-video.md` (Zyklus 2 W37 — Wave-7C Meeting-AI-Summary P0-Kontext)
- `/opt/zentria-intel/monthly/2026-09-14-deepdive-wiki.md` (Zyklus 2 W38 — W23-P0s 2+3 nicht ausgeliefert, gleiches Muster)
- `/opt/zentria-intel/monthly/2026-09-21-deepdive-helpdesk.md` (Zyklus 2 W39 — 5/10 W24-Deliveries + AI-Compliance-Foundation-Sprint P0)

**Externe Quellen (Stand 2026-09-28):**
- [EU AI Act Article 50 Transparency Obligations Go Live | Baker Botts September 2026](https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live)
- [EU AI Act Article 50 Transparency Obligations Take Effect | Cloud Security Alliance 2026-07-29](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/)
- [EU AI Act Article 50 in Force Since 2 August 2026 | Regulation AI](https://www.regulation-ai.eu/en/transparency-obligations/)
- [Transparency obligations under Article 50 | European Commission Digital Strategy](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- [EU AI Act Article 50 transparency rules enter force | AI News](https://www.artificialintelligence-news.com/news/eu-ai-act-article-50-transparency-rules-enter-force/)
- [Typeform News September 2026 STARTUP EDITION](https://blog.mean.ceo/typeform-news-september-2026/)
- [Typeform What's New](https://www.typeform.com/whats-new)
- [Typeform AI Info Page](https://www.typeform.com/ai-info)
- [Typeform AI Form Builder & Form Generator](https://www.typeform.com/ai)
- [Best Form Builders with MCP Server in 2026 | Tally](https://tally.so/help/best-mcp-form-builders)
- [Tally Changelog: Latest Product Updates & Releases](https://tally.so/changelog)
- [Tally MCP Server Introduction | Tally Developer Docs](https://developers.tally.so/api-reference/mcp)
- [The 10 Best AI Form Builders in 2026 (Tested + Compared) | Fillout Blog](https://www.fillout.com/blog/best-ai-form-builder)
- [8 Best GDPR Compliant Form Builders in 2026](https://formbuilder.tools/type/gdpr-compliant)
- [JotForm GDPR Compliance Center](https://www.jotform.com/gdpr-compliance/)
- [GDPR Compliance | JotForm AI Agents](https://www.jotform.com/ai/agents/features/gdpr-compliance/)
- [Formbricks GDPR Compliance Checklist 2026](https://formbricks.com/blog/gdpr-compliance-checklist-2025)
- [Honeypot vs CAPTCHA vs Turnstile Complete Comparison | Formgent](https://formgent.com/honeypot-vs-captcha-vs-turnstile/)
- [ALTCHA Privacy-First CAPTCHA Alternative](https://altcha.org/)
- [Best Self-Hosted CAPTCHA Alternatives to reCAPTCHA in 2026 | Pi Stack](https://www.pistack.xyz/posts/self-hosted-captcha-alternatives-recaptcha-mcaptcha-turnstile-2026/)
- [Honeypot, CAPTCHA, AI Anti-Bot Solution Comparison 2026 | Prospect Hub](https://prospect-hub.app/en/blog/honeypot-captcha-ai-anti-bot-comparison/)

---

## Picks (vorgeschlagen)

- [ ] 🔴 **P0 (Live-Production-Risk) — Anti-Spam-Trias jetzt: Honeypot + Captcha-Slot-Wiring + Rate-Limit-Erweiterung + IP-Consent-Gate + Feature-Flag-Gate B8-Public-Share bis Trias fertig**. Sprint-Owner: Backend-Lead. Aufwand: ~12 Tage. Frist: 2 Wochen. B8 ist live-deployt, jede Public-Form-Nutzung ist heute Spam-exponiert.

- [ ] 🔴 **P0 (Regulatorisch, 66-Tage-Deadline) — AI-Compliance-Foundation-Sprint W39-P0 unveraendert eskaliert: Multi-Provider-Router + Article-50-Disclosure + Meeting-AI-Summary-Retrofit**. Owner: Architecture-Lead + Backend-Lead. Aufwand: 6-8 Wochen. Frist: 2026-12-02 (Machine-Readable-Marking Grace-Period-Ende). Wave-7C Meeting-AI-Summary ist an Tag 57 Non-Compliance.

- [ ] 🟢 **P1 (Sales-Signal + Refactor-Beschleuniger) — MCP-Server + FormularePage-Refactor + Anti-Drift-Sweep (FieldOption #2, consent+rating #5+#6) Sprint-Bundle**. Owner: Backend-Lead + Frontend-Lead. Aufwand: 22-28 Tage. Frist: Q4-2026 vor DACH-Enterprise-RFP-Wave. MCP-Server-Fenster schliesst mit Q1-2027-Standard-Erwartung.

- [ ] 🟢 **P1 (AI-Formulare-Layer nach Foundation-Sprint) — `GenerateFromIntakeTarget()` als tightere Cross-Modul-Story auf B6-Registry aufgebaut**. Owner: Backend-Lead + Product. Aufwand: 3-4 Wochen. Frist: Q1-2027 sobald Foundation-Sprint fertig. Sales-Differenzierung gegen Typeform "Create form from HubSpot properties" — Cosmi kann es fuer *alle* eigenen Module + jedes registrierte Intake-Ziel.

- [ ] 🟡 **P2 (Sales-Amplification) — B6-Intake-Binding als Marketing-Case-Study + Sales-Slide + Blog-Post**. Owner: Product + Marketing. Aufwand: 3-5 Tage. Frist: Q4-2026 Sales-Kick-off. "Cosmi ist die einzige EU-Suite, die Formulare als First-Class-Modul-Ziel-Bindung behandelt — Bewerbungsformular → Helpdesk-Ticket mit einem Klick, native, DSGVO-konform."

- [ ] 🟡 **P2 (Governance-Fenster) — ISO/IEC 42001 (AI-Governance) Roadmap-Marker + SOC-2-Type-II Roadmap-Marker gemeinsam evaluieren fuer 2027-H1**. Owner: Security-Lead + Compliance. Typeform hat 42001 seit Juni 2026; Formbricks SOC-2-Type-II seit Q1 2026; Cosmi hat keins. Bei Q4-2026-DACH-Enterprise-RFPs werden beide gefragt.

- [ ] 🟢 **P2 (Team-Coordination) — Sprint-Prozess-Fix: FE-PR-mit-Schema-Aenderung braucht zwingend BE-PR-Referenz (PR-Gate) um weitere Drift zu vermeiden**. Owner: Engineering-Lead. Aufwand: 1 Tag Setup + Process-Change. Verhindert 4-5 weitere Drift-Achsen bis Zyklus 3.

- [ ] 🟢 **P2 (Deepdive-Prozess-Learning) — Baseline-Report-Sanity-Check-Regel dokumentieren: bei jeder Sicherheits-Kritik pruefen ob kritisierter Pfad kontrollflow-erreichbar ist (siehe IsPublic-Interpretations-Falle W25→W40)**. Owner: Intel-Autor. Aufwand: <1 Tag Doku-Update. Verhindert False-Positive-P0s in kommenden Deepdives.

- [ ] 🟢 **P2 (Followup-Marker 30d) — B8-Public-Share-Token Live-Traffic-Monitoring**: Wie viele Public-Submissions kommen ohne Anti-Spam-Trias durch? Wenn >0 Spam-Signal, Trias-Sprint sofort priorisieren. Frist: 2026-10-28 (KW44). Owner: DevOps + Backend-Lead.

- [ ] 🟢 **P2 (Konkurrenz-Followup) — Typeform ISO/IEC 42001 + Fillout AI-Free-Tier + Tally-MCP-Adoption in DACH-KMU-Markt tracken**: Sind diese Q3-2026-Features bei DACH-KMU-Prospects bereits Erwaehnungs-Themen in Sales-Calls? Wenn ja, Cosmi-Antwort priorisieren. Frist: 2026-11-15 (KW46) — vor Q4-DACH-Enterprise-RFP-Wave.
