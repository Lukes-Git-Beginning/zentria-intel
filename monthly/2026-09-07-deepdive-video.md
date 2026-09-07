---
year: 2026
week: 37
modul: video
created: 2026-09-07
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 51
tokens_input: ~310000
tokens_output: ~13600
rotation_position: 3/15
zyklus: 2
delta_to: 2026-05-25-deepdive-video.md
delta_weeks: 15
---

# Deepdive: video (Mo W37/2026) — Zyklus 2

> **Zyklus 2, Modul 3/15.** Vorgaenger im aktuellen Zyklus: `crm-core` (W35, 2026-08-24), `dialer` (W36, 2026-08-31). Referenz-Vergleich Zyklus 1: `monthly/2026-05-25-deepdive-video.md` (W22/2026). **Delta-Zeitraum: 15 Wochen (2026-05-25 → 2026-09-07).**
>
> **Stand Cosmi-Video (2026-09-07):** Erstes Modul in Zyklus 2, das **substantielle Umsetzung der Zyklus-1-Empfehlungen** vorweist. **Sechs von zehn Zyklus-1-Luecken sind heute geschlossen** — AI-Summary (Wave 7C, `llm.Client` via Ollama/OpenAI-kompatibel), Meeting-Chat (Migration 000225), Co-Hosts + Meeting-Lock (000226), CRM-Link auf Contact/Deal (000227), Breakout-Rooms (000235), Action-Item → Task-Konversion (`ConvertActionItemsToTasks` im meeting-Service). Migration-Head jetzt bei **325**, Cross-Modul-Bridge zu CRM ist Schema-live.
>
> **Leit-Signal des Deepdives:** Die Cosmi-Video-Roadmap hat in 15 Wochen genau die "einfachen" W22-Empfehlungen implementiert — und ist damit direkt in die **teuerste Zyklus-1-Warnung hineingelaufen**: **EU AI Act Art. 50 ist seit 2026-08-02 wirksames Recht**, mit €15M/3%-Umsatz-Rahmen. Cosmi hat `GenerateAISummary` produktiv, aber weder `AIDisclosureBanner` noch AI-Audit-Log-Layer. **Aus dem Zyklus-1-P0-Warnhinweis "vor jedem AI-Feature" ist ein aktives, laufendes Compliance-Risiko geworden — 36 Tage nach Inkrafttreten.** Gleichzeitig hat sich der Markt in zwei zusaetzliche Achsen bewegt, die Cosmi neu zwingen: **(a) OpenTalk hat auf LiveKit umgestellt** (`opentalk.eu/news/webrtc-upgrade-opentalk-switches-livekit`) — der DACH-Sovereignty-Konkurrent teilt jetzt Cosmis Tech-Stack und wird v25→v26 in <4 Monaten releasen; **(b) das Bot-free-Notetaker-Segment** (Jamie/DE, Seedext/FR) hat Enterprise-DACH als Zielsegment erobert und rahmt Consent-First-AI-Meeting-Assistenten als neue Kategorie. Cosmi-AI-Summary ist heute weder als "Bot-free" noch als "Compliance-First" positioniert.

---

## Executive Delta (W22 → W37)

**In 15 Wochen hat Cosmi mehr Video-Roadmap umgesetzt als Dialer- oder CRM-Core-Roadmap zusammen** — waehrend gleichzeitig das Marktfenster fuer "Compliance-First-AI-Video" und "OpenTalk-DACH-Gegen-Positionierung" akut geworden ist.

| Achse | Stand W22 (2026-05-25) | Stand W37 (2026-09-07) | Cosmi-Delta |
|---|---|---|---|
| Meeting-Kern | video/livekit/recording live, LOC ~4.600 | +meeting-Modul auf 5.977 LOC (`service.go` 1299 LOC, `postgres_repository.go` 777 LOC), 5 neue Meeting-Tabellen/Spalten, 8 neue gateway-Routen-Tests (`route_video_*_test.go` insg. 5.289 LOC) | ✅ **Substantieller Ausbau** |
| AI-Summary | 0 Zeilen, empfohlen als Sprint-3-Welle-6 nach Compliance-Stack | `GenerateAISummary` produktiv (meeting/service.go:551), `internal/llm/client.go` (183 LOC) mit Ollama-Default + OpenAI-Kompatibilitaet, gRPC `GenerateMeetingSummary` gewired (video_grpc.go:997), Migration 000228 `meetings.ai_summary` | ✅ **Umgesetzt — aber ohne Compliance-Layer** |
| Meeting-Chat | 0, nicht empfohlen | Migration 000225 `meeting_chat` + `SaveChatMessage/ListChatMessages` produktiv, tenant-RLS-scoped, append-only | ✅ **Zusatz-Feature ausserhalb W22-Empfehlung** |
| Co-Hosts + Lock | 0, nicht in W22-Fokus | Migration 000226 `meeting_cohosts` + `meetings.locked`, `PromoteCoHost/DemoteCoHost/ListCoHosts`, `isHostOrCoHost` in 5+ Autorisierungs-Pfaden | ✅ **Host-Governance-Layer neu** |
| CRM-Link (Cross-Modul-Bridge) | 0, Empfehlung 3 W22 | Migration 000227 `meetings.contact_id + deal_id` + Indizes, im Meeting-Modell serialisiert, im Repository INSERT/UPDATE/SELECT-Pfade | 🟡 **Schema live, Auto-Wire fehlt** (Bridge braucht Event auf MeetingEnd) |
| Breakout-Rooms | 0, W22-Pick "🔵 followup 180d" | Migration 000235 `meeting_breakout_rooms` + `meeting_breakout_assignments`, `CreateBreakoutRooms` im Service, Cleanup-Path bei MeetingEnd (service.go:436) | ✅ **12 Monate vor W22-Followup-Horizont geliefert** |
| Action-Item → Task-Bridge | 0, Empfehlung 3 W22 (Schema exist. Welle-4B) | `ConvertActionItemsToTasks` im meeting-Service (service.go:829) + `route_video_notes_and_action_items_test.go` (492 LOC Tests) | 🟡 **Konversion live, aber ohne AI-getriebene Extraktion** |
| Live-Transcription | 0, Empfehlung 2 W22 | 0 Code (grep `transcrib|whisper|caption|voxtral|jigasi`: 0 Hits in video/livekit/recording/meeting) | ❌ **Unveraendert — Markt-Tabellenstake weiterhin offen** |
| AI-Disclosure UI + Audit-Log | 0, Empfehlung 1 W22 als Pflicht-Blocker | 0 Code (grep `disclosure|ai_audit`: 0 Hits) | ❌❌ **Aus W22-P0-Warnung ist heute EU-AI-Act-Live-Risiko geworden** |
| E2EE (Insertable Streams) | 0, W22-Pick "🟡 followup 60d" | 0 Code (grep `e2ee|encryption|Insertable`: 0 Hits) | ❌ **Ungeliefert, Followup abgelaufen** |
| LiveKit-Tech-Stack | v1.11.0/v1.12.0-Ära, TURN-TTL neu | v1.13.6-Ära (26.08.2026): TURN-Concurrent-Quotas per-Participant, WARP-Experimental, WebSocket-Read-Limits, Pending-Tracks-Limits; Speechmatics-Linden-Modell in LiveKit-Inference (27.08.2026) | 🟡 **Cosmi-Version-Check offen** — `livekit.yaml` verwendet welche Server-Version? |
| DACH-Sovereignty-Konkurrent OpenTalk | Statewide-Deployments SH+TH, SLAC-E2EE-Roadmap-Promise | **OpenTalk hat WebRTC-Stack auf LiveKit umgestellt** (opentalk.eu/news/webrtc-upgrade-opentalk-switches-livekit), Releases v25.2 → v26.2.0 (2026-09-01), v26.1.2 (2026-08-25) — Tech-Stack-Konvergenz mit Cosmi | ⚠️ **USP-Kollision**: OpenTalk teilt jetzt Cosmi-Stack |
| EU AI Act Art. 50 | Warnung "greift 2026-08-02, 4-8 EW pro Modul" | **Seit 2026-08-02 aktives Recht**, €15M/3%-Umsatz-Rahmen, Transition fuer Marking-Feature bis 2026-12-02 | ⚠️ **Cosmi ist heute live-non-compliant fuer AI-Summary** |
| Pricing-Position Meetings | 4 EUR/Modul im W22-Report zitiert (aus .knowledge/pricing.md) | **"in Vorbereitung"** — pricing.md 2026-08-17 fuehrt Meetings ohne Preis, waehrend 13 Module buchbar sind. Zoom-Vergleich (13-15 EUR) bleibt stehen. | ⚠️ **Meetings ist bewusst nicht verkaeuflich** — bricht W22-Kalkuel |
| Bot-free-Notetaker-Kategorie | Randnotiz W22 ("Jamie/DE, Seedext/FR") | Ausgereifte Kategorie 2026: Jamie DACH-First, ISO27001+DORA, EU-Frankfurt-Hosting, ohne-Bot-lokal-first, Fellow/Shadow-Marktforschung-listet ~10 bot-free-Player | 🆕 **Neue Konkurrenz-Kategorie fuer Cosmi-AI-Summary** |
| Feed-Landschaft video-Modul | LiveKit-Releases 0, Whereby-Blog OK, Jitsi-Releases OK | LiveKit-Releases-Feed liefert **weiterhin 0 Items** (7 aufeinanderfolgende Werktage im W36 Morning laut daily-Reports); externe Web-Search deckt v1.13.4-v1.13.6 auf → **Feed hat Latenz vs. Realitaet** | ⚠️ **video.yaml-Feed-Konfig sollte gegen GitHub-Atom-URL vs. Server-Path validiert werden** |

**Bottom line:** Cosmi hat die 15 Wochen produktiv genutzt und mehr Video-Features geliefert als in irgendeinem anderen Zyklus-2-Modul bisher gesehen. **Der Fortschritt hat aber die falsche Reihenfolge**: Die W22-Reihenfolge war (1) Compliance-Stack → (2) Live-Transcription → (3) Cross-Modul-Bridge. Geliefert wurde: (3) Cross-Modul-Bridge halb + AI-Summary + Chat + Co-Hosts + Breakout — waehrend (1) Compliance-Stack und (2) Live-Transcription unangetastet geblieben sind. **Konsequenz:** Cosmi hat heute ein produktives AI-Feature (`GenerateAISummary`), das seit 36 Tagen unter EU-AI-Act-Art.-50-Pflicht steht und keine Disclosure- oder Audit-Log-Schicht hat. Das ist P0 mit Rechtsrahmen.

---

## State-of-the-Art (Update W37)

Der Video-Markt hat sich seit W22 in drei Achsen weiterentwickelt: **(a)** **EU AI Act Art. 50 ist aus Warnung zu wirksamem Recht geworden** (2026-08-02) — alle AI-Voice/Video-Systeme brauchen Interaktions-Disclosure + Audit-Log; **(b)** **DACH-Sovereignty-Segment konsolidiert um LiveKit-Stack** — OpenTalk hat den WebRTC-Layer auf LiveKit umgestellt, damit teilen Cosmi und OpenTalk technische Grundlage und Bug-Landschaft; **(c)** **Bot-free-Notetaker-Kategorie ist zur eigenstaendigen Klasse geworden** — Jamie (Berlin) mit DACH-First-Positionierung + ISO 27001 + DORA, waehrend Otter/Fireflies-Kritik im Enterprise-DACH-Segment auf Vertriebs-Ebene angekommen ist.

### Top-Konkurrenten — Update seit W22 (Deltas fett)

**1. LiveKit (Tech-Partner, threat: low als Konkurrenz, verstaerkter Stack-Drift-Beobachtung)**

- **Server-Releases seit W22:** v1.12.0 (16.05.) → v1.13.3 (03.07.) → v1.13.4 (18.07.) → v1.13.5 (31.07.) → v1.13.6 (26.08.). Die 1.13.x-Serie fokussiert auf **Skalierungs-Governance**: per-Participant Concurrent-TURN-Quotas (v1.13.6), Pending-Tracks-Limits, WebSocket-Read-Message-Size-Limits, API-Request-Body-Limits, Webhook-erweiterte Room-Details, WARP-Experimental. **Direkter Cosmi-Impact**: Wenn Cosmi noch auf 1.11/1.12 lauft, ist der v1.13.6-Sprung zu Pending-Tracks-Limits eine Config-Migration (kein Breaking Change, aber Defaults geaendert).
- **LiveKit Inference — Speechmatics-Linden-Integration (27.08.2026):** Erste Speechmatics-Modell "purpose-built for voice agents" via LiveKit Inference gemuenzt, ein-Klick-Wechsel zwischen STT-Providern. **Direkter Cosmi-Impact**: Der Build-vs-Buy-Slot fuer STT-Provider (W22-Empfehlung 2, Mistral-Voxtral vs. Whisper-Self-Host) hat einen dritten Kandidaten — Speechmatics-Linden. EU-Hosting-Status weiter unklar, aber Speechmatics ist UK-based (post-Brexit-EU-Adequacy).
- **LiveKit Agents Python 1.5.0 → 1.6.7 in 18 Wochen (26 Releases, Delta W22):** Semantic Turn Detection standard, MCP-nativ, ausgereifte SIP-Integration. Voice-AI-Stack ist Framework-fertig, wenn Cosmi den Sprung machen will.
- **Gap zu Cosmi seit W22:** Inference-Layer nicht evaluiert, Agents-Framework nicht integriert, Server-Version-Check gegen aktuellen Stack offen.
- **Strategischer Hinweis:** OpenTalk hat den LiveKit-Sprung gemacht — Cosmi ist bereits dort. **Beide teilen jetzt einen Bug-Report-Kanal, einen Security-Patch-Zyklus und eine Tech-Stack-Reifekurve.** Das reduziert Cosmi-Alleinstellungsmerkmal "LiveKit-Self-Host-mit-Consent-Layer" — der Consent-Layer ist der einzig verbleibende Unterschied.

**2. OpenTalk (DACH, threat: HIGH → sehr HIGH — jetzt Stack-Konvergent zu Cosmi)**

- **WebRTC-Stack-Umstellung auf LiveKit** (`opentalk.eu/en/news/webrtc-upgrade-opentalk-switches-livekit`) — die Heinlein-Group hat den Janus-basierten Media-Server durch LiveKit ersetzt, nach Proof-of-Concept. Damit **teilt OpenTalk Cosmis Basis-Stack**. **Direkter Cosmi-Impact**: das USP-Argument "wir nutzen LiveKit self-hosted" ist bei OpenTalk-Vergleich nicht mehr differenzierend.
- **Release-Kadenz sichtbar:** v25.4.7 (Mai) → v26.1.2 (25.08.2026) → v26.2.0 (01.09.2026) — Major-Version-Bump 25→26 in <4 Monaten, wobei die konkreten E2EE-Beta-Announcements aus der SLAC-Roadmap-Promise Mai 2026 in der oeffentlichen Release-Note-Zusammenfassung bisher **nicht bestaetigt** sind (Release-Notes docs.opentalk.eu/releases/ mit den Detail-Features nicht abgefragt). **Cosmi-Beobachtungs-Pflicht**: opentalk-e2ee-rust-crate `opentalk-roomserver-module-e2ee` (lib.rs) existiert — E2EE-Implementation in Bearbeitung.
- **Zielgruppen-Ueberlappung:** Weiter Public-Sector (SH, TH, Bundesbehoerden) — kein direkter KMU-Bewerb, aber **Signal fuer DACH-Regulator-Trust** ist wichtig fuer Cosmi's Mittelstand-Verkaufsargument (BSI-C5-Analogie).
- **Gap zu Cosmi:** Statewide-Deployment-Referenzen, E2EE-Implementation-Fortschritt (Rust-Crate live), Managed-Service-Partnerschaft mit Telekom-Cloud.
- **Strategischer Hinweis:** OpenTalk ist jetzt der **Tech-Stack-Zwilling** von Cosmi im DACH-Video-Markt. Cosmi kann nicht mehr ueber "besseres LiveKit-Setup" gewinnen — Differenzierung muss auf (a) Modul-Integration (CRM/Work/Wiki) und (b) KMU-Zielgruppen-Fokus (OpenTalk zielt Behoerden/Grosskunden) reduzieren. **Der neue Cosmi-Pitch: "LiveKit-Video mit KMU-CRM-Bridge — nicht Behoerden-Standalone."**

**3. Jitsi Meet (open-source, threat: low — aber Feature-Vorbild)**

- **AV1 als Default-Video-Codec** — neue Baseline seit Mitte 2026, Bandwidth-Reduzierung ~30% bei gleicher Qualitaet. Cosmi-LiveKit unterstuetzt AV1 optional; Default-Konfig-Sweep waere sinnvoll.
- **E2EE-Perimeter unveraendert:** Media-Streams (Audio/Video/Screen) E2EE-fähig; **Chat, Polls, Recording, Transcription, Livestream nicht E2EE** (Jitsi-Doku 2026). Fundamentales SFU-E2EE-Problem bleibt: Recording-Server darf Frames nicht entschluesseln, deshalb entweder Client-Side-Recording oder Aussetzen von E2EE waehrend Aufzeichnung.
- **Google Summer of Code 2026** — 5 Projekte, u.a. AI-basierte Verbesserungen. Signal fuer OSS-Momentum.
- **Gap zu Cosmi:** AV1-Default, E2EE-Beta-Perimeter dokumentiert (fehlt bei Cosmi), Jigasi-Whisper-Transcription-Setup-Anleitungen breit im Netz.
- **Strategischer Hinweis:** **Jitsi bleibt der Feature-Vorbild-Benchmark** — was Jitsi kann und Cosmi nicht, wird in G2/Capterra-Feature-Vergleichen von Cosmi-Interessenten gefunden. E2EE-Perimeter-Doku ist ein 1-Tag-Job, der Cosmi vor "Habt-ihr-E2EE?"-Vertriebs-Blockaden schuetzt.

**4. Whereby (international, threat: medium)**

- **Whereby Embedded** unveraendert als iframe+REST-API-Video-Loesung positioniert, Blog-Kadenz kontinuierlich (fokussiert auf embedded-video-Use-Cases).
- G2-Pain-Cluster (aus W22-Report unveraendert): "steep pricing vs. competitors", "value-for-money decreased", "limited free plans" — Whereby bleibt in der "expensive-fuer-was-geboten-wird"-Wahrnehmung.
- **Gap zu Cosmi seit W22 nahezu unveraendert:** Live-Captions eingebaut, Recording+Transcription out-of-the-box, Miro/Trello/YouTube-Integrationen; Cosmi hat keins davon nativ.
- **Strategischer Hinweis:** Whereby ist **nicht Cosmi-Zielsegment** (Cosmi ist Endprodukt, Whereby ist Embed-Platform). Feature-Benchmark-Rolle unveraendert.

**5. Daily.co (international, threat: medium — AI-Voice-Cloud verbreitet)**

- **Pricing-Baseline unveraendert**: $0.004/Participant-Minute + $0.01349/min Recording + $0.0059/min Realtime-Transcription + $0.03/min HLS + $0.015/min RTMP. Pure-Pay-as-you-go, 10.000 Free-Minutes/Monat. Bis zu 100.000 gleichzeitige Sessions.
- **Pipecat Cloud** und **Daily Bots** als Voice-AI-Pipeline-Plattform gefestigt.
- **Gap zu Cosmi:** Realtime-Transcription $0.0059/min als Per-Minute-Baseline ist der Preis-Referenzpunkt, wenn Cosmi Live-Transcription baut. **Wenn Cosmi Whisper-Self-Host schafft, ist die interne Kostenrechnung <$0.001/min bei GPU-Auslastung** — Daily-Vergleich als Positionierungs-Vorteil fuer Cosmi-EU-Self-Host.
- **Strategischer Hinweis:** Mistral-Voxtral-Integration (W22-Empfehlung) bleibt relevant, plus **Speechmatics-Linden als dritte Option** (LiveKit-Inference-nativ, UK-Hosting).

**6. BigBlueButton (open-source, threat: low — aber 3.0-Reifung)**

- **BBB 3.0.x-Serie 2026 durchgehend gepflegt** (v3.0.23/24/25/26/27 seit W22, ~4-Wochen-Kadenz). Mongo→Hasura/GraphQL-Migration schon in 3.0 vollzogen; Plugin-System stabilisiert; Whiteboard-Panning ausserhalb Presenter-View, LiveKit-Dial-in-Audio-Integration.
- **Weiterhin Education-Fokus** (75% globaler LMS-Markt) — kein direkter KMU-Bewerb.
- **Gap zu Cosmi:** Plugin-System (Cosmi hat keins fuer Video), Whiteboard (tl;draw v2), Live-Captions-Plugin (Faster-Whisper), Hasura-basiertes Realtime-Sub.
- **Strategischer Hinweis:** **BBB-Plugin-System als Architektur-Vorbild** — wenn Cosmi Live-Transcription baut, sollte das als eigener Sidecar-Service (BBB-Plugin-Pattern) laufen, nicht in `internal/work/video/`. Auslagerung isoliert Whisper-CPU/GPU-Last vom Cosmi-Backend.

**7. Bot-free-Notetaker-Kategorie — NEU als Konkurrenz-Klasse (2026)**

- **Jamie (Berlin, DE, GDPR-First)** — bot-free lokaler Recorder auf Desktop, transkribiert lokal oder EU-Frankfurt-hosted, ISO 27001 + DORA zertifiziert, 100+ Sprachen, Audio-Delete-nach-Notes-fertig, EU-Server, keine Daten-Weitergabe. Positioniert als "Enterprise-tauglicher Otter-Ersatz fuer DACH".
- **Seedext (FR)** — analog, franzoesisch-first.
- **Shadow / Fellow / MeetingsAI** — internationale bot-free-Player, meist mit "AI runs on your device"-Positionierung.
- **Kategorie-Merkmal 2026**: **Nicht-als-Bot-in-Meeting-joinen**, sondern Desktop-App die System-Audio lokal recordet + transkribiert. **Umgeht Consent-Debatte** (weil kein zusaetzlicher Teilnehmer im Raum) und Enterprise-IT-Bot-Verbote.
- **Direkter Cosmi-Impact:** Cosmi-AI-Summary ist **nicht bot-free** und **nicht Enterprise-Compliance-brandmarkiert**. Cosmi-Meeting-AI-Summary ist bot-inhaerent (im Cosmi-Meeting selbst), das ist eine Kategorie-Wahl — aber die neue Klasse verlangt, dass Cosmi **die eigene Zugehoerigkeit erklaert**: "Cosmi ist NICHT bot-free — weil wir das Meeting sind, brauchen wir keinen Bot."
- **Strategischer Hinweis:** Jamie ist DACH-First-Konkurrent im Enterprise-Segment. Fuer Cosmi-KMU-Zielgruppe ist Jamie ergaenzend (kann ausserhalb Cosmi-Meetings genutzt werden), nicht ersetzend. **Aber Marketing-Botschaft "Cosmi-Meeting mit Compliance-First-AI-Summary" ist besetzbar**, wenn Empfehlung 1 (Disclosure+Audit-Log) geliefert wird.

### Querbewegungen seit KW22 — Markt-Lage September 2026

**EU AI Act Art. 50 seit 2026-08-02 aktives Recht:** Voice-AI-Erstkontext-Offenlegung + Chatbot-Disclosure + Deepfake-Marking sind ab jetzt Rechtspflicht — nicht Best-Practice. **€15M / 3% globaler Konzernumsatz-Rahmen fuer Verstoesse.** Fuer AI-generierte Ausgaben mit "Machine-Readable-Marking"-Pflicht (Art. 50(2)) gibt es Transition-Grace bis **2026-12-02** fuer Bestandsprodukte. **Cosmi-`GenerateAISummary` ist ab 02.08. formal disclosure-pflichtig** (Ausgabe an Menschen, ohne Interaktions-Marker) — mit Grace bis 02.12.2026 fuer Marking, aber Disclosure-UI und Audit-Log haben keine Grace.

**LiveKit-Speechmatics-Speechmatics-Linden (27.08.2026)** — via LiveKit-Inference GA verfügbar, spezifisch trainiert fuer Voice-Agent-Anwendungen. Signal, dass STT-Providermarkt sich in "Voice-Agent-optimierte Modelle" (Speechmatics-Linden, OpenAI-gpt-realtime-mini, Deepgram-Nova) und "generische STT" (Google/Azure) fragmentiert.

**OpenTalk-LiveKit-Umstellung**: **Der entscheidende DACH-Sovereignty-Konkurrent** hat den Tech-Stack an Cosmi angeglichen. Alle Cosmi-USP-Argumente ueber "LiveKit-Self-Host-mit-DSGVO" gelten jetzt fuer OpenTalk auch. **Der einzige verbleibende Cosmi-Vorteil** ist der Consent-Recording-Stack (kein Konkurrent hat das) und die Modul-Integration (OpenTalk hat kein CRM-Backend).

**Pricing-Position "Meetings in Vorbereitung" (2026-08-17)**: Cosmi-Website-Pricing-Katalog fuehrt Meetings ohne Preis, waehrend 13 andere Module buchbar sind. Das ist Signal, dass Meetings-Modul aktuell **nicht als Umsatz-Traeger geplant** ist, sondern als Kompletting-Feature fuer Kalender/CRM/Work-Modul-Kaeufer. **Konsequenz fuer Roadmap-Priorisierung**: Video-Feature-Ausbau muss durch Cross-Modul-Value (Meeting-verbessert-CRM/Work-Effizienz) begruendet werden — nicht durch eigene ARPU-Erwartungen.

---

## Cosmi-IST-Stand (Update 2026-09-07)

### Was seit W22 dazugekommen ist

**Backend — `backend/internal/work/meeting/` (5.977 LOC neu erfasst):**
- `service.go` (1299 LOC) — Meeting-Lifecycle mit Host-Governance (`isHostOrCoHost`), AI-Summary (`GenerateAISummary` ab :551), Breakout-Cleanup bei End (`:434, :442`), Chat-Persistence (`SaveChatMessage :886, ListChatMessages :926`), Action-Item-Conversion (`ConvertActionItemsToTasks :829`).
- `models.go` (167 LOC) — `Meeting{ContactID, DealID, AISummary, AISummaryAt, Locked}`, `MeetingCoHost`, `BreakoutRoom`, `BreakoutAssignment`.
- `postgres_repository.go` (777 LOC) + `postgres_repository_db_test.go` (946 LOC) — schema-korrekte Persistence mit `tenant_id`-Filter, RLS-getest.
- `occurrences.go` (153 LOC) + Tests (239 LOC) — Recurring-Meeting-Occurrence-Generierung.
- Isolation-Tests: `tenant_isolation_phase2_test.go` (87 LOC), `tenant_write_test.go` (122 LOC).

**Backend — `backend/internal/llm/` (183 LOC neu):**
- `client.go` — OpenAI-kompatibler Chat-Completion-Client, Default-Ziel **selbst-gehostetes Ollama-Instance** (EU-Souveraenitaet), OpenAI/OpenAI-Kompatible-Gateways als Optional-Ziel. Config: `Provider, BaseURL, Model, APIKey, TimeoutSeconds`. Retries (2×), initialer Backoff 500ms, Default-Timeout 120s. **Explizit "intentionally tiny — exposes only what meeting AI-summary (Wave 7C) needs"** — Kommentar in Datei.
- System-Prompt (`summarySystemPrompt`) **DE-first mit Sprach-Detect-Klausel**: "Antworte in der Sprache der Notizen".
- **Feature-Flag-Pattern**: Meeting-Service haelt `llm` als `*Client` (nicht Interface), `nil` = feature-off, `ErrLLMUnavailable` als Sentinel.

**Migrations 000225-000235 (Wave 6A + 7B + 7C):**
- **000225** `meeting_chat` — Tenant-RLS + append-only, `meeting_chat_meeting_created_idx`.
- **000226** `meeting_cohosts` + `meetings.locked` — Host-Governance-Layer.
- **000227** `meetings.contact_id + deal_id` — **Cross-Modul-Bridge Schema live** (FK auf `contacts(id)` + `deals(id)`, ON DELETE SET NULL, Partial-Indizes).
- **000228** `meetings.ai_summary + ai_summary_at` — AI-Summary-Persistence.
- **000235** `meeting_breakout_rooms + meeting_breakout_assignments` — Breakout-Feature-Complete.
- **000309** `meeting_notes_unique_index` — Race-Free-Notes-Insert.

**Gateway/HTTP — `backend/internal/gateway/route_video*.go` (5.289 LOC gesamt):**
- `route_video.go` (2.379 LOC) — kompletter Video-HTTP-Layer.
- Sub-Test-Files: `route_video_breakout_cohost_test.go` (625 LOC), `route_video_notes_and_action_items_test.go` (492 LOC), `route_video_meeting_lifecycle_test.go` (481 LOC), `route_video_recording_lifecycle_test.go` (216 LOC), `route_video_recording_test.go` (372 LOC), `route_video_webhook_test.go` (278 LOC), `route_video_test.go` (446 LOC) — **kompakter Test-Corpus fuer alle neuen Features**.

**gRPC — `backend/internal/server/video_grpc.go` (~1.700 LOC):**
- Neue RPCs: `GenerateMeetingSummary` (:997), `SaveMeetingNotes` (:1023), `GetMeetingNotes` (:1047), `GetPreviousMeetingNotes` (:1085), `ListMeetingOccurrences` (:1107), `CreateActionItem/UpdateActionItem/DeleteActionItem/ListActionItems` (:1147-:1239), `ConvertActionItemsToTasks` (:1265).
- Meeting-Proto-Mapping: `AiSummary` + `AiSummaryAt` in `meetingToProto` (:1590-:1594) → gRPC-Contract enthaelt AI-Summary-Fields.

**Recording-Modul — `backend/internal/work/recording/` (2.919 LOC, +415 seit W22):**
- `service.go` (729 LOC, +178 seit W22) — mehr Recording-Access-Logik: `ListRecordingsWithAccess`, `GetRecordingParticipants`, `GetRecordingDownloadURL` (mit MinIO-signed-URLs).
- Neuer `service_lifecycle_test.go` (441 LOC) — Lifecycle-Coverage.
- `postgres_repository_real_sql_test.go` (464 LOC) — echte SQL-Integrationstests.
- Consent-Stack aus W22 unveraendert produktiv (Migration 000107, Pre-Recording-Consent HTTP 412).

**LiveKit — `backend/internal/work/livekit/` (~1.061 LOC, +45 seit W22):**
- `room_manager.go` (202 LOC, +106) — erweiterte Room-Lifecycle-Verwaltung.
- Base-Layer unveraendert produktiv (v1.11/v1.12-Ära der Client-Library, Server-Version unbekannt).

### Was strukturell weiter fehlt — Cosmi-Luecken 2026-09-07

**P0 — Regulatorisch akut (EU AI Act Art. 50 seit 2026-08-02 aktiv):**

1. **AI-Disclosure-UI fuer `GenerateAISummary`** — Cosmi generiert AI-Meeting-Summaries produktiv (`meeting/service.go:551`, gRPC `video_grpc.go:997`), aber **kein UI-Banner "Diese Zusammenfassung wurde KI-generiert"**, kein Modell-Provider-Hinweis, kein Consent-Erfassungs-Punkt vor Generierung. **Live-Non-Compliance seit 36 Tagen**.
2. **AI-Audit-Log-Layer** — kein `ai_interactions`-Table, kein Append-Only-Audit-Trail fuer `(tenant_id, user_id, meeting_id, model_provider, model_id, prompt_hash, response_hash, started_at, completed_at)`. Ohne diese Basis ist ein Post-Incident-Audit "welche Meetings wurden von welchem Modell zusammengefasst" nicht rekonstruierbar. **Rechtsrahmen 15M/3%.**
3. **Machine-Readable-Marking** (Art. 50(2), Grace bis 2026-12-02) fuer die AI-Summary-Ausgabe — z.B. HTML-Micro-Tag `<span data-ai-generated="true">` oder Header-Feld `X-Cosmi-AI-Generated: true`. **90 Tage Frist verbleibend.**

**P1 — Markt-Tabellenstake weiterhin offen:**

4. **Live-Transcription** — 0 Code (`grep` bestaetigt). W22-Empfehlung 2 unangetastet. Whereby/Daily/Jitsi/BBB haben es alle. Fuer AI-Summary-Vertiefung (Zitat-Referenzen, Rueckverfolgung "wer hat wann was gesagt") ist Transkript-Speicherung Voraussetzung. **Empfehlung 2 aus W22 ist P1-Follow-Empfehlung 2026-09.**
5. **E2EE-Aktivierung** — 0 Code (`grep` bestaetigt). LiveKit-Insertable-Streams-API vorhanden, Cosmi nutzt sie nicht. Recording+E2EE bleibt technisch hart (Client-Side-Recording noetig), aber **E2EE fuer Nicht-Recording-Meetings ist ein 1-Sprint-Client-Config-Sprint**. Jitsi hat es seit >1 Jahr.
6. **Live-Captions** — folgt aus Live-Transcription; wenn Transcription da ist, ist Caption-Overlay-UI ~1-2 Sprints.
7. **AV1 als Default-Video-Codec** — Jitsi ist umgestiegen, LiveKit unterstuetzt es. Config-Sweep zur Bandwidth-Optimierung.

**P2 — Strategisch (Cross-Modul-Bridge halb-fertig):**

8. **Cross-Modul-Bridge Auto-Wire fehlt** — Schema `meetings.contact_id + deal_id` existiert (000227), aber **kein Event-Publisher bei MeetingEnd**, der `crm.activity.create` oder `work.task.create` triggert. `ConvertActionItemsToTasks` existiert als Service-Methode, aber wird nicht **automatisch** nach `GenerateAISummary` aufgerufen. Bridge braucht Cosmi-Event-Bridge-Wire in `internal/cross/event-bridge/` (existiert der Layer schon? — nicht in dieser Session gepr uft; folgt Zyklus-2-crm-Empfehlung "context-api P0").
9. **AI-Summary Post-Editing / Review-Flow** — heute ist die Summary read-only am Meeting. Kein Redaktions-Workflow fuer den Host, kein Feedback-Loop fuer Modell-Verbesserung, keine mehreren Versionen. Gute AI-Notetaker haben "Draft → Review → Publish"-Pattern.
10. **Meeting-Chat-Persistierung** produktiv (000225), aber **nicht AI-durchsuchbar** — der Chat-Kontext koennte fuer AI-Summary genutzt werden, wird aber ausschliesslich `notes` an das LLM uebergeben (`GenerateAISummary` verwendet nur `s.repo.GetAllNotes`, meeting/service.go:574).

**P3 — Beobachtung / Zukunft:**

11. **LiveKit-Server-Version-Check** — aktuelle Version im Cosmi-Deployment unbekannt. v1.13.6-Sprung bringt Concurrent-TURN-Quotas + Pending-Tracks-Limits (Skalierung).
12. **OpenTalk-Feature-Monitoring** — jetzt Tech-Stack-Konvergent, laufender Vergleichsbedarf.
13. **Bot-free-Notetaker-Ergaenzung** — Jamie-Integration als optionales "Externes-Meeting-mit-Cosmi-Sync"-Feature koennte KMU-Sales-Case-Studies liefern (Cosmi + Jamie fuer Nicht-Cosmi-Meetings).
14. **Per-Minute-Pricing-Vorbereitung** — solange Meetings-Modul "in Vorbereitung" ohne Preis ist, ist Per-Minute-Pricing-Modell auch strategisch. Wenn Meetings launched, muss Pricing-Klaerheit vorher da sein.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi 09/26 | Cosmi 05/26 (Delta) | LiveKit (Tech-Partner) | Whereby | Daily.co | Jitsi | OpenTalk | BigBlueButton |
|---|---|---|---|---|---|---|---|---|
| WebRTC SFU | ✅ via LiveKit | = | ✅ (eigen) | ✅ | ✅ | ✅ | ✅ **jetzt LiveKit** | ✅ mediasoup |
| Self-Host (EU) | ✅ Pilot | = | ✅ | ❌ SaaS | ❌ SaaS | ✅ | ✅ statewide | ✅ |
| Recording (Server-Side) | ✅ Egress | = | ✅ Egress | ✅ | ✅ | ✅ Jibri | ✅ Cloud-Service | ✅ bbb-webrtc-recorder |
| Pre-Recording-Consent (Initiator + Pflicht-Dialog) | ✅ **Welle 3+3.5** | = | ❌ (Recipe-Docs) | 🚧 Opt-In-UX | 🚧 | ❌ | ❌ | ❌ |
| Meeting-Chat (persistent, RLS-scoped) | ✅ **Migration 000225** | 🆕 | ✅ Data-Tracks | ✅ | ✅ | ✅ | ✅ | ✅ 3.0 verbessert |
| Co-Hosts + Meeting-Lock | ✅ **Migration 000226** | 🆕 | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| CRM-Link-Schema (Meeting↔Contact+Deal) | 🟡 **Schema 000227 live, Auto-Wire fehlt** | 🆕 | n/a | ❌ | ❌ | ❌ | ❌ (kein CRM) | ❌ |
| Meeting-End → CRM-Activity-Auto-Log | ❌ | = | n/a | n/a | n/a | n/a | n/a | n/a |
| Action-Item → Task-Konversion | ✅ **service.go:829** | 🆕 | n/a | ❌ | ❌ | ❌ | ❌ | ❌ |
| AI-Summary (LLM-generiert) | ✅ **`GenerateAISummary` W7C** | 🆕 | ✅ Agents-Framework | 🚧 | ✅ Pipecat | 🚧 GSoC 2026 | ❌ | ❌ |
| AI-Provider EU-souveraen (Default) | ✅ Ollama-Default (self-host) | 🆕 | 🟡 Inference (Cloud) | ❌ US-Cloud | ❌ US-Cloud | n/a | n/a | n/a |
| AI-Disclosure-UI (Art. 50 seit 02.08.) | ❌ **LIVE-NON-COMPLIANT** | 🆕-Risiko | n/a (Plattform) | 🚧 | 🚧 | n/a | n/a | n/a |
| AI-Audit-Log-Layer | ❌ | = | n/a | ❌ | ❌ | n/a | n/a | n/a |
| Machine-Readable-Marking (Art. 50(2) Grace-Frist 02.12.) | ❌ | = | n/a | ❌ | ❌ | n/a | n/a | n/a |
| Breakout-Rooms | ✅ **Migration 000235** | 🆕 | ✅ Multi-Room | ✅ | ✅ | ✅ | ✅ | ✅ |
| E2EE (Audio/Video/Screen) | ❌ (LiveKit-Capability weiter ungenutzt) | = | ✅ Insertable-Streams | ❌ | ❌ | ✅ Beta AV1 Default | 🚧 Rust-Crate `opentalk-roomserver-module-e2ee` | ❌ |
| Live-Transcription | ❌ | = | ✅ Inference + Speechmatics-Linden 08/26 | ✅ eingebaut | ✅ Deepgram $0.0059/min | ✅ Jigasi+Whisper | 🚧 | ✅ Plugin |
| Live-Captions | ❌ | = | ✅ | ✅ eingebaut | ✅ | ✅ | 🚧 | ✅ |
| TURN-Fallback (mit v1.13.6 Concurrent-Quotas) | ✅ coturn live seit 04/26 (Backend-Wiring S2.R2.1b weiter offen?) | 🟡 zu pruefen | ✅ v1.13.6 Per-Participant-Quotas | ✅ | ✅ | ✅ | ✅ | ✅ |
| Whiteboard / tl;draw | ❌ | = | ❌ (App-Layer) | ❌ (Miro-Integration) | ❌ | ✅ | ✅ | ✅ tl;draw v2 |
| AV1 Video-Codec | 🚧 LiveKit-Support optional, Cosmi-Config unklar | = | ✅ | 🚧 | ✅ | ✅ **Default 2026** | via LiveKit | 🚧 |
| Per-Minute-Pricing | ❌ | = | ✅ Tier+Usage | ❌ Seat | ✅ $0.004/min | n/a OSS | ❌ Managed-Service | n/a OSS |
| Meetings-Modul-Preis (Cosmi) | ⚠️ **"in Vorbereitung"** | Regress von 4€/W22-Zitat | n/a | n/a | n/a | n/a | n/a | n/a |
| Bot-free-Notetaker-Positionierung | ❌ (Cosmi ist Meeting-inhaerent) | = | n/a | n/a | n/a | n/a | n/a | n/a |
| Doppelklick-Guard + Offline-Queue (Frontend) | ✅ Welle 3.5 | = | n/a | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cross-Tenant-Tests (Recording+Meeting) | ✅ **12+ Tests** | +4 seit W22 | n/a | n/a | n/a | n/a | n/a | n/a |
| **Threat-Level fuer Cosmi-KMU-Markt** | **Self** | | **Tech-Drift** | **medium** | **medium** | **low** | **sehr HIGH (jetzt Stack-Zwilling)** | **low** |

**Lesehilfe:** ✅ vorhanden, 🚧 Beta/teilweise/Roadmap, ❌ fehlt, 🆕 seit W22 dazu, = unveraendert seit W22.

**Insights aus der Matrix:**
- **Cosmi hat in 15 Wochen 6 grosse Feature-Luecken zur Konkurrenz-Baseline geschlossen** (Chat, Co-Host, CRM-Link-Schema, AI-Summary, Breakout, Action-Item-Konversion). Das ist der schnellste Feature-Absoerp-Zyklus in irgendeinem Zyklus-2-Modul bisher.
- **Die drei uebrig gebliebenen Luecken haben sich jetzt priorisiert**: (1) AI-Disclosure/Audit ist von "Pflicht ab 08/26" zu "seit 36 Tagen Live-Risiko" geworden, (2) Live-Transcription bleibt Tabellenstake, (3) E2EE ist mit Jitsi-AV1-Default + OpenTalk-Rust-Crate deutlich sichtbarer Konkurrenz-Feature.
- **OpenTalk-LiveKit-Umstellung eliminiert Cosmi's "gleiche Stack-Basis"-Alleinstellung** — Cosmi muss auf Modul-Integration (CRM/Work/Wiki) und KMU-Zielgruppe zurueckziehen. Cross-Modul-Bridge Auto-Wire (P2-Lücke 8) wird damit strategisch akuter.
- **Cosmi hat einen echten Souveraenitaets-Differenzierer**: Ollama-Default fuer AI-Summary. Kein Konkurrent zeigt diese Klarheit ("EU-self-host als Default, Cloud-STT als Optional"). Marketing-Botschaft besetzbar, wenn Compliance-Layer da ist.

---

## Top-3 Strategische Empfehlungen

### 1. **AI-Disclosure-UI + Audit-Log-Layer sofort — EU AI Act Art. 50 ist seit 36 Tagen aktives Recht** (Sprint-Sofort-Aufnahme, P0 Rechtsrisiko)

**Warum:** Die W22-P0-Warnung ist Realitaet geworden. Cosmi hat `GenerateAISummary` als produktives Feature (meeting/service.go:551, gRPC video_grpc.go:997), das Meeting-Notizen an ein LLM sendet und die Ausgabe an den Host zurueckgibt. **Diese Interaktion faellt unter Art. 50 der EU AI Act, die seit 2026-08-02 wirksames Recht ist** — die Ausgabe muss als AI-generiert kenntlich gemacht sein (Disclosure gegenueber dem Empfaenger), die Interaktion muss auditierbar sein, und ab 2026-12-02 (Grace-Ende) muss die Ausgabe zusaetzlich machine-readable-marked sein (Art. 50(2)). **Cosmi hat heute keins davon.** Rechtsrahmen: **€15M oder 3% globaler Konzernumsatz** pro Verstoss. Selbst wenn die Enforcement-Realitaet in DACH langsam anlaeuft, ist ein pilotierter Kunde, der wegen eines nicht-disclosed AI-Summary in eine DSGVO-Anfrage geraet, ein direkter Reputations-Schaden.

Der Rueckstand ist mittlerweile 36 Tage. **Grace-Frist fuer Machine-Readable-Marking**: 86 Tage bis 2026-12-02.

**Scope (verpflichtender Minimum-Umfang):**

- **`backend/internal/cross/ai_audit/`** neuer Sub-Pkg:
  - Migration: `ai_interactions (id, tenant_id, user_id, feature, model_provider, model_id, input_hash TEXT NOT NULL, output_hash TEXT NOT NULL, prompt_version TEXT, started_at, completed_at, error TEXT NULL)` mit `enable_tenant_rls`.
  - Service: `RecordAIInteraction(ctx, feature, modelProvider, inputBytes, outputBytes) → interactionID` als append-only-Insert. Retention-Policy: mind. 6 Jahre (analog GoBD/DSGVO-Aufbewahrung).
  - Wire-Up: `meeting.Service.GenerateAISummary` ruft `ai_audit.RecordAIInteraction(ctx, "meeting_summary", cfg.Provider, notesHash, summaryHash)` in einem Defer-Block vor `UpdateAISummary`.
- **Frontend `desktop/src/renderer/src/features/_shared/compliance/AIDisclosureBanner.tsx`**:
  - Radix-Alert-Banner "Diese Zusammenfassung wurde von einem KI-Modell erstellt (Anbieter: {Provider}, Modell: {Model}). Sie ist automatisch generiert und kann Fehler enthalten." — angezeigt vor jedem `GenerateAISummary`-Trigger UND als persistente Bezeichnung neben `ai_summary`-Anzeige.
  - i18n-Keys `aiDisclosure.*` in de/en/fr/it (Cosmi-Standard).
  - **Consent-Erfassung** (nicht optional): einmalige Modal-Bestaetigung "Ich verstehe, dass diese Notizen an ein KI-System uebermittelt werden" bevor die erste Summary generiert wird — persistiert per User + Tenant.
- **Machine-Readable-Marking (bis 02.12.):** HTML-Wrapper um AI-Summary-Rendering `<div data-ai-generated="true" data-ai-provider="{provider}" data-ai-model="{model}" data-ai-generated-at="{ts}">…</div>` + gRPC-Response-Header `X-AI-Generated: true` bei Endpoints, die AI-Content ausliefern.
- **`internal/llm/client.go`** um Provider-Metadata erweitern: `Summarize()` returned `(text string, meta InteractionMeta{Provider, Model, InputTokens, OutputTokens})` statt nur `string` — damit Audit-Log Provider/Modell-Info hat.

**Aufwand:** **4-6 Engineer-Weeks** (2 Backend-Sprints: Audit-Log + LLM-Client-Refactor + Meeting-Integration; 1 Frontend-Sprint: Disclosure-Banner + Consent-Modal + i18n). **Aufwand-Reduktion vs. W22-Schaetzung von 6-8 EW** — weil nur eine AI-Feature-Instanz (Summary) existiert und der Compliance-Layer bewusst schlank gebaut werden kann.

**Strategische Veredelung:** **"Cosmi-AI-Compliance-First" als sichtbares UI-Feature vermarkten** — DACH-KMU-Compliance-Officers sehen einen aktiv angezeigten Disclosure-Banner mit auditierbarem Log als Verkaufsargument. Verbindung zu Zyklus-1-crm-Empfehlungen (AEO-Content-Welle): AEO-Artikel "So faellt Cosmi-AI-Summary unter EU AI Act Art. 50 — und warum das gut ist" adressiert direkt die Compliance-getriebene KMU-Kaeufer-Persona.

**Threat-Klasse:** **A — Live-Rechtsrisiko seit 2026-08-02.**

### 2. **Cross-Modul-Bridge Auto-Wire fertigstellen: MeetingEnd → CRM-Activity, AISummary → Wiki-Index, ActionItem → Task-Auto-Create** (Sprint-1-2 nach Empfehlung 1)

**Warum:** Die Schema-Grundlage ist durch Migration 000227 (`meetings.contact_id + deal_id`) und die Service-Methode `ConvertActionItemsToTasks` (meeting/service.go:829) bereits gelegt. **Was fehlt, ist der Auto-Wire**: heute muss jemand manuell `ConvertActionItemsToTasks` aufrufen, und Meeting-End erzeugt keine CRM-Activity-Row. **Damit bleibt der USP-Wert der Bridge unrealisiert** — Cosmi-Video hat die Datenstruktur, aber nicht die Sales-Story "nach dem Meeting sind Follow-ups automatisch im Task-Board und die Aktivitaet im CRM gelogged." Diese Sales-Story ist genau das, was Cosmi vs. OpenTalk (kein CRM), vs. Whereby/Daily (kein CRM), vs. Zoom (nur mit HubSpot/Salesforce-Konnektor) differenziert.

Zusatz-Kontext aus dieser Session: die crm-core-W35-Zyklus-2-Empfehlung war `backend/internal/ai/context-api/` — d.h. der Meeting→CRM-Wire kann als **erster Konsument des context-api-Layers** gebaut werden, wenn dieser P0-Task angegangen wird. Zwei Fliegen, eine Klappe.

**Scope:**

- **`backend/internal/cross/event-bridge/meeting/`** (neu):
  - Subscriber auf `MeetingEnded`-Event (bereits publisher-seitig in `EndMeeting`-gRPC?): wenn `meeting.ContactID != nil` OR `meeting.DealID != nil`, dann `crm.Service.CreateActivity(ctx, ActivityInput{Type: "meeting", ContactID, DealID, Title: meeting.Title, StartedAt, EndedAt, Notes: meeting.PublicNotes})`.
  - Subscriber auf `AISummaryGenerated`-Event: wenn ein wiki-Indexer existiert, `wiki.Service.IndexDocument(ctx, WikiDocInput{Kind: "meeting_summary", Content: summary, RefID: meeting.ID, MeetingContactID, MeetingDealID})` fuer Full-Text-Cross-Modul-Suche.
  - Subscriber auf `ActionItemCreated`-Event: **hier bewusst NICHT auto-createn** (verhindert Task-Spam) — sondern eine **UI-One-Click-Batch-Konversion** in der Meeting-Nachbereitung. `ConvertActionItemsToTasks` bleibt manuell-gefeuert, aber der UI-Trigger wird prominent platziert.
- **Meeting-Service** publiziert die drei Events synchron nach den entsprechenden Aktionen: `EndMeeting()` → `MeetingEnded`, `GenerateAISummary()` → `AISummaryGenerated`, `CreateActionItem()` → `ActionItemCreated`.
- **Tests**: Cross-Modul-Integration-Tests in `internal/gateway/` — `route_video_meeting_lifecycle_test.go` erweitern um "nach EndMeeting existiert eine crm_activity-Row".
- **Backfill-Migration** (optional): `contact_id`/`deal_id`-Backfill fuer bestehende Meetings via Calendar-Event-Assoziation.

**Aufwand:** **3-5 Engineer-Weeks** (1 Sprint: Event-Bridge + Subscriber; 1 Sprint: UI-Wire + Tests). Aufwand-Reduktion vs. W22-Schaetzung von 3-4 EW weil zusaetzlich `AISummaryGenerated` → Wiki-Index dazukommt.

**Strategische Veredelung:** **KMU-Pilot-Reference-Case** — "Handwerksbetrieb X macht 20 Sales-Meetings/Woche, danach ohne manuellen Aufwand: alle Aktivitaeten im CRM, alle Follow-ups im Task-Board, alle Summaries im Wiki durchsuchbar." Konkret quantifizierbarer Zeit-Gewinn (~15 min/Meeting × 20 = 5h/Woche) → verkaufbare ROI-Story. Direkt an OpenTalk-Standalone-Positionierung vorbei.

**Threat-Klasse:** **B — kein Pilot-Blocker, aber strategisch akuter Differenzierer nach OpenTalk-Stack-Konvergenz.**

### 3. **Live-Transcription via Whisper-Self-Host + Speechmatics-Linden-Optional-Path** (Sprint-3-Welle-8, nach Empfehlung 1+2)

**Warum:** W22-Empfehlung 2 unveraendert korrekt, aber jetzt mit einer neuen Provider-Optionen: **Speechmatics-Linden ist seit 27.08.2026 als STT-Provider in LiveKit-Inference verfuegbar** (`globenewswire.com/news-release/2026/08/27/3352093/0/en/speechmatics-and-livekit`). Damit hat der Build-vs-Buy-Slot drei Kandidaten: (a) **Whisper-Self-Host** (Ollama-Analog fuer STT, EU-souveraen, unter Cosmi-Kontrolle), (b) **Mistral-Voxtral** (EU-Provider, DSGVO-relevant), (c) **Speechmatics-Linden** (UK-based, Voice-Agent-optimiert, LiveKit-Inference-nativ). **Priorisierung fuer Cosmi**: Whisper-Self-Host als Default (analog Ollama fuer LLM), Speechmatics-Linden als Optional-Cloud-Slot fuer Cosmi-Meetings, die STT-Qualitaet ueber Selbst-Host stellen.

Die drei Argumente aus W22 gelten unveraendert: (a) DSGVO-by-default via Self-Host, (b) Pricing im Tier-Modell einbaubar (Whisper-Self-Host = kein Per-Minute-Cloud-Cost), (c) Jigasi-Architektur-Vorbild, (d) Voraussetzung fuer AI-Summary-Verbesserung (Zitat-Referenzen aus Transcript).

**Ein neues Argument seit W22:** Cosmi-AI-Summary heute arbeitet nur auf `notes` (meeting/service.go:574 `s.repo.GetAllNotes`). **Wenn Live-Transcription existiert, kann `GenerateAISummary` auf `transcript ∪ notes` operieren** — deutlich hoehere Summary-Qualitaet + Bot-free-analoge Positionierung (Cosmi zeichnet nichts extern auf, alles bleibt im Cosmi-SFU).

**Scope:**

- **`backend/internal/work/video/transcription/`** (neu):
  - `whisper_sidecar/` — Go-Service, joined als LiveKit-Participant, greift Audio-Frames via LiveKit-Server-SDK ab, leitet an lokalen Whisper.cpp (gRPC oder UNIX-Socket) weiter, publisht Streaming-Result als LiveKit-Data-Track. Deployment-Analog zu Ollama-Sidecar.
  - `provider_selector.go` — Tenant-Setting `stt_provider ∈ { whisper_self_host | speechmatics_linden | mistral_voxtral | disabled }`, Default `whisper_self_host`.
- **`backend/migrations/000330_meeting_transcripts.up.sql`**: `meeting_transcripts (id, meeting_id, tenant_id, language, status, provider, started_at, completed_at)` + `meeting_transcript_segments (transcript_id, t_start_ms, t_end_ms, speaker_id, text)` mit RLS.
- **Frontend `LiveCaptions.tsx`**: Overlay-Component + Opt-In-Toggle pro Meeting (Default-Off, expliziter Consent-Recording-Style-Prompt).
- **Integration mit Empfehlung 1**: AI-Disclosure-Banner (aus Empfehlung 1) auch fuer Transcription-Trigger, Audit-Log-Entry pro Transcript-Run.
- **`GenerateAISummary` erweitern**: wenn `meeting_transcripts` fuer diese Meeting-ID existiert, in den LLM-Prompt einbinden — bessere Summary-Qualitaet + Zitat-Referenzen (Deeplinks in Transcript-Segments).

**Aufwand:** **8-12 Engineer-Weeks** (2 Backend-Sprints Whisper-Sidecar + Provider-Selector, 1 Backend-Sprint Schema+Migration, 2 Frontend-Sprints LiveCaptions+Consent+Playback). Aufwand unveraendert vs. W22.

**Strategische Veredelung**: **Cosmi-Video-AI-Tier positioniert**: Basis = Meetings ohne AI (Tier-1), Tier-2 = Meetings + AI-Summary (Ollama-Self-Host), Tier-3 = Meetings + AI-Summary + Live-Transcription + Cross-Modul-Bridge. Setzt Cosmi-Pricing-Klarheit voraus (heute "in Vorbereitung") — kann kombiniert werden mit Meetings-Modul-Preis-Launch.

**Threat-Klasse:** **A — Markt-Tabellenstake, aber priorisiert HINTER Empfehlung 1 (Rechtsrisiko).**

---

## Quellen (Top-Quellen die diesen Bericht stuetzen)

**Cosmi-IST-Stand (Code + Migrations):**
- `/opt/kmuhub/backend/internal/work/meeting/service.go` (1.299 LOC — GenerateAISummary, isHostOrCoHost, PromoteCoHost, CreateBreakoutRooms, SaveChatMessage, ConvertActionItemsToTasks)
- `/opt/kmuhub/backend/internal/work/meeting/models.go` (167 LOC — Meeting mit ContactID/DealID/AISummary/Locked, MeetingCoHost, BreakoutRoom, BreakoutAssignment)
- `/opt/kmuhub/backend/internal/work/meeting/postgres_repository.go` (777 LOC)
- `/opt/kmuhub/backend/internal/llm/client.go` (183 LOC — Ollama-Default + OpenAI-kompatibel, Summarize()-Methode, feature-flag via nil-Client)
- `/opt/kmuhub/backend/internal/server/video_grpc.go` (~1.700 LOC — GenerateMeetingSummary, SaveMeetingNotes, ConvertActionItemsToTasks, AiSummary im Proto-Mapping)
- `/opt/kmuhub/backend/internal/gateway/route_video*.go` (5.289 LOC — 8 Sub-Test-Files inkl. `route_video_breakout_cohost_test.go`, `route_video_notes_and_action_items_test.go`)
- `/opt/kmuhub/backend/migrations/000225_create_meeting_chat.up.sql`
- `/opt/kmuhub/backend/migrations/000226_meeting_cohosts_and_lock.up.sql`
- `/opt/kmuhub/backend/migrations/000227_meeting_crm_link.up.sql`
- `/opt/kmuhub/backend/migrations/000228_meeting_ai_summary.up.sql`
- `/opt/kmuhub/backend/migrations/000235_meeting_breakout_rooms.up.sql`
- `/opt/kmuhub/backend/migrations/000309_meeting_notes_unique_index.up.sql`
- `/opt/kmuhub/backend/internal/work/recording/service.go` (729 LOC, +178 seit W22) — Pre-Consent-Stack aus W22 unveraendert produktiv
- `/opt/kmuhub/backend/internal/work/livekit/{service,room_manager,egress_manager}.go` (1.061 LOC, +45 seit W22)
- `/opt/kmuhub/.knowledge/pricing.md` (Stand 2026-08-17: Meetings "in Vorbereitung", 13 Module buchbar, Modul-x-User-Modell)
- `/opt/kmuhub/.knowledge/milestones.md` (Welle-4B-Kontext: video_grpc.StartRecording tenant_id-Fix, ConvertActionItemsToTasks uuid.Nil-Guard)

**Markt / Konkurrenz (Web-Search + Referenz-Reports):**
- LiveKit Server Releases v1.12.0 → v1.13.6 (26.08.2026): github.com/livekit/livekit/releases (Per-Participant TURN Concurrent-Quotas, Pending-Tracks-Limits, WebSocket-Read-Message-Limits, WARP-Experimental)
- Speechmatics-Linden + LiveKit-Inference (27.08.2026): globenewswire.com/news-release/2026/08/27/3352093/0/en/speechmatics-and-livekit-target-the-accuracy-gap-breaking-voice-agents-in-production
- OpenTalk WebRTC-Umstellung auf LiveKit: opentalk.eu/en/news/webrtc-upgrade-opentalk-switches-livekit
- OpenTalk Releases v25.4.7 → v26.1.2 (25.08.2026) → v26.2.0 (01.09.2026): docs.opentalk.eu/releases/
- OpenTalk-E2EE Rust-Crate `opentalk-roomserver-module-e2ee`: lib.rs
- Jitsi AV1 als Default-Video-Codec 2026, GSoC 2026 (5 Projekte): jitsi.org/blog/
- BigBlueButton 3.0.x-Serie (v3.0.23-v3.0.27 seit W22, ~4-Wochen-Kadenz): github.com/bigbluebutton/bigbluebutton/releases
- Daily.co Pricing 2026 (unveraendert $0.004/participant-min + $0.0059/min Realtime-Transcription + $0.01349/min Recording): daily.co/pricing/
- Bot-free-Notetaker-Kategorie: meetjamie.ai/blog/gdpr-note-takers-in-europe, fellow.ai/blog/bot-free-ai-note-takers/, shadow.do/blog/best-ai-meeting-note-takers-that-dont-join-as-a-bot-2026
- Jamie (DE) — ISO 27001 + DORA, EU-Frankfurt-Hosting: meetjamie.ai

**EU AI Act — Art. 50 seit 2026-08-02:**
- EU AI Act Article 50 In Force Since 2 August 2026: regulation-ai.eu/en/transparency-obligations/
- Article 50 Transparency Rules Practical Guide: artificialintelligenceact.eu/transparency-rules-article-50/
- Enforcement Framework + Bussgeld €15M / 3%: brightdefense.com/news/eu-ai-act-delay-keeps-2026-compliance-pressure/
- Compliance-Checklist Providers/Deployers: resemble.ai/resources/eu-ai-act-article-50-compliance-checklist-for-providers-and-deployers
- Transition-Grace fuer Machine-Readable-Marking bis 2026-12-02: hard2bit.com/en/blog/ai-act-article-50-ai-transparency-chatbots-deepfakes/

**Interne Referenz-Reports (zentria-intel):**
- `monthly/2026-05-25-deepdive-video.md` (Zyklus 1, W22 — Referenz fuer Delta-Vergleich)
- `monthly/2026-08-24-deepdive-crm-core.md` (Zyklus 2, W35 — crm-context-api-Empfehlung als Wire-Basis fuer Meeting-CRM-Bridge)
- `monthly/2026-08-31-deepdive-dialer.md` (Zyklus 2, W36 — EU AI Act Art. 50 als Query-Signal, Delta-Format-Vorbild)
- `daily/2026-09-07-morning.md` (video: 0 Items, LiveKit-Releases-Feed 0 neu — bestaetigt Feed-Latenz)

---

## Picks (vorgeschlagen)

[ ] 🟢 **AI-Disclosure-UI + `internal/cross/ai_audit/`-Layer** — EU AI Act Art. 50 Live-Compliance seit 2026-08-02, Machine-Readable-Marking Grace bis 2026-12-02. Aufwand 4-6 EW. **Bedrohungsklasse A — LIVE-Rechtsrisiko.** Sofort-Aufnahme in Sprint-Backlog.

[ ] 🟢 **Cross-Modul-Bridge Auto-Wire: MeetingEnd → CRM-Activity, AISummary → Wiki-Index** — Schema 000227 live, Service `ConvertActionItemsToTasks` live; nur Event-Bridge + Subscriber + UI-Wire fehlen. Aufwand 3-5 EW. **Bedrohungsklasse B — strategischer Differenzierer nach OpenTalk-Stack-Konvergenz.**

[ ] 🟢 **Live-Transcription via Whisper-Self-Host (Default) + Speechmatics-Linden-Optional-Slot** — Markt-Tabellenstake weiterhin offen, jetzt zusaetzlich Voraussetzung fuer verbesserte AI-Summary-Qualitaet (transcript ∪ notes). Aufwand 8-12 EW. **Bedrohungsklasse A — nach Empfehlung 1.**

[ ] 🟡 **LiveKit-Server-Version-Check + Upgrade-Plan v1.11/12 → v1.13.6** — Per-Participant TURN Concurrent-Quotas + Pending-Tracks-Limits + Webhook-Room-Details. Skalierungs-Governance-Sprung. Config-Migration ohne Breaking-Changes. Aufwand <1 EW (nach Check). → followup 14d.

[ ] 🟡 **E2EE-Aktivierung als Tier-2+-Feature (Meetings ohne Recording)** — LiveKit-Insertable-Streams-API weiter ungenutzt. Recording+E2EE technisch hart (Client-Side-Recording), aber E2EE-only-Meetings ist ein Sprint. Konkurrenz-Feature bei Jitsi (Default+AV1), OpenTalk (Rust-Crate live). Aufwand 1-2 Sprints. → followup 60d.

[ ] 🟡 **Meetings-Modul-Preis-Klaerung** — heute "in Vorbereitung" ohne Preis, Zoom-Vergleich 13-15 EUR unrealistisch als Solo-Preisanker. Empfehlung: Meetings-Tier-Modell (Tier-1 Basic = frei-mit-Kalender-Modul-Kauf, Tier-2 = +AI-Summary +4 EUR, Tier-3 = +Transcription +8 EUR). Strategie-Entscheid, kein Code. → followup 30d.

[ ] 🟡 **OpenTalk-Monitoring vertiefen** — jetzt Stack-Konvergent (LiveKit), E2EE-Rust-Crate live. `sources/video.yaml` um opentalk-releases-Feed erweitern + GitHub-Watches. Aufwand <1 EW Feed-Wartung. → followup 14d.

[ ] 🟠 **AI-Summary auf transcript ∪ notes erweitern** (post-Empfehlung 3) — wenn Live-Transcription existiert, `GenerateAISummary` erweitern um Transcript-Kontext, mit Deeplink-Zitat-Referenzen. Aufwand 1-2 Sprints (nach Empfehlung 3). → followup 120d.

[ ] 🟠 **AV1 als Default-Video-Codec pruefen** — Jitsi umgestiegen, LiveKit unterstuetzt es. Bandwidth-Reduktion ~30% bei gleicher Qualitaet. Config-Sweep in `livekit.yaml`. Aufwand <1 EW. → followup 90d.

[ ] 🔵 **Jamie/Seedext-Integration als "Cosmi-Extern-Sync"-Optional-Feature** — Bot-free-Notetaker-Kategorie ist etabliert, Cosmi kann Jamie-Notes-Import-Endpoint anbieten fuer Meetings ausserhalb Cosmi. Marketing-Story "Cosmi arbeitet mit dem, was DACH-Enterprise nutzt". → followup 180d.

[ ] 🔵 **Per-Meeting-Analytics + Manager-Dashboards** — vgl. Aircall/Dialpad-Reportings. Wenn AI-Summaries + Transcripts existieren, Manager-View auf "Meeting-Durchsatz, Themen-Cluster, Action-Item-Erfuellungsquote". → followup 180d.

[ ] 🔵 **Pre-Recording-Consent UX-Metriken** — der Consent-Stack lebt seit ~5 Monaten. Wie oft wird Recording gestartet? Wie oft brechen Nutzer wegen Consent ab? Telemetrie-Auswertung als Basis fuer W22-Follow-Pick "Doppel-Dialog-Burden". → followup 60d.

---

## Was widerspricht Cosmi-Strategie? (Ehrliche Contradictions)

- **Cosmi-AI-Summary-Default via Ollama** ist strategisch stark (EU-Souveraenitaet), aber **operativ fragil**: Ollama-Instances haben je nach Modell (Llama-3.x, Mistral, Gemma) unterschiedliche Zusammenfassungs-Qualitaet, und die Standard-Ollama-Instance (kein GPU) laesst Meeting-Summaries ~30s-2min brauchen. Fuer KMU-Pilot-Kunden ohne GPU-Sidecar ist das ein UX-Problem. **Positionierungs-Frage**: Ist "self-host mit Latency" akzeptabler Trade-off vs. "Cloud-STT/LLM mit Compliance-Layer"? Sollte Empfehlung 1 (Compliance) ausreichen, um Cloud-Provider akzeptabel zu machen?
- **Cross-Modul-Bridge (Empfehlung 2)** verlangt, dass `internal/cross/event-bridge/` bereits existiert (oder gebaut wird) — dies wurde in dieser Session nicht verifiziert. Wenn kein Event-Bus da ist, ist Empfehlung 2 aufwaendiger als die 3-5 EW-Schaetzung.
- **Meetings-Modul-Preis "in Vorbereitung"** signalisiert, dass Cosmi-Product-Management aktuell **keine Umsatz-Erwartung** an das Video-Modul hat. Alle drei Empfehlungen fuegen Aufwand hinzu (Compliance + Bridge + Transcription = 15-23 EW). **Ohne Preis-Klaerheit ist der Business-Case fuer diese 15-23 EW opak.** Der Deepdive-Bericht kann Aufwand quantifizieren, aber nicht die Priorisierung gegen andere Roadmap-Streams.
- **OpenTalk-Stack-Konvergenz reduziert Cosmi-USP**: Der W22-Bericht rahmt Cosmi als "LiveKit-Self-Host-mit-Consent-Layer". Diese Beschreibung passt jetzt auch auf OpenTalk. Cosmi muss die Positionierung auf "Modul-Integriertes-LiveKit-Video" reduzieren — was Empfehlung 2 (Cross-Modul-Bridge) zum strategischen Kern macht.
- **Feed-Konfiguration `sources/video.yaml`**: Der Morning-Report bestaetigt "0 Items, keine neuen LiveKit-Releases" — obwohl Live-Web-Search 5 Server-Releases seit W22 findet. **Cosmi-Intel-System ist im Video-Modul aktuell markt-blind** (LiveKit-releases-Atom-Feed liefert nichts trotz Release-Aktivitaet). Ein 1-h-Fix-Task fuer den video-Feed sollte parallel zu den Empfehlungen laufen.

---

## Telemetrie

- **Routine:** intel-monday-deepdive
- **Modul:** video (3/15 Rotation, Zyklus 2)
- **Zyklus-1-Referenz:** monthly/2026-05-25-deepdive-video.md (W22/2026)
- **Delta-Wochen:** 15 (2026-05-25 → 2026-09-07)
- **Quellen gepollt:** 5 Modul-Konkurrenz-Feeds (video.yaml) + KMU-Hub-Code + 15 Migrations-Files gepolled + 6 Live-WebSearches (LiveKit, OpenTalk, Jitsi, Whereby/Daily, BBB, Bot-free-Kategorie, EU AI Act Art. 50)
- **Konkurrenz-Datenpunkte:** LiveKit 8 (Releases + Speechmatics-Linden), OpenTalk 4 (Stack-Umstellung + Releases + E2EE-Crate), Jitsi 3 (AV1, GSoC, E2EE-Perimeter), BBB 2 (3.0.x-Serie, Whiteboard), Whereby+Daily 2, Jamie/Seedext 3
- **Cosmi-Progress-Verifikation:** 6 Migrations (000225-000228 + 000235 + 000309) gelesen, 5 Go-Files geprueft (meeting/service+models+postgres_repo, llm/client, video_grpc), Grep-Verifikation fuer "transcrib|whisper|caption|disclosure|ai_audit|e2ee|Insertable" = **0 Hits** bestaetigt
- **EU-AI-Act-Bezug:** Art. 50 seit 2026-08-02 aktiv (36 Tage vor Report-Datum); Machine-Readable-Marking Grace-Frist bis 2026-12-02 (86 Tage verbleibend) — kritischer Treiber fuer Empfehlung 1
- **Naechstes Modul gemaess Rotation:** **wiki** (KW38, Mo 2026-09-14) — Zyklus-2-Erstlauf des Wiki-Moduls
- **State-File:** `.state/deepdive_rotation.json` wird aktualisiert
- **Bemerkung Feed-Health:** LiveKit-Releases-Feed (`sources/video.yaml`) liefert 0 Items trotz nachweislich 5 Releases seit W22 → Feed-Config-Fix als Nebenauftrag (siehe Contradictions)

---

*Generiert: 2026-09-07 — Dritter Deepdive der Zyklus-2-Rotation. Cosmi-Video-Modul ist das erste in Zyklus 2, das signifikante Umsetzung von Zyklus-1-Empfehlungen zeigt (AI-Summary, Chat, Cohost, CRM-Link-Schema, Breakout, Action-Item-Konversion). Der Fortschritt hat aber die falsche Reihenfolge gewaehlt: die W22-P0-Warnung "AI-Compliance-Stack VOR jedem AI-Feature" wurde uebersprungen, waehrend AI-Features (GenerateAISummary) live gingen. Kombiniert mit EU AI Act Art. 50 seit 2026-08-02 aktivem Recht ergibt sich ein **Live-Rechtsrisiko, das binnen 4-6 Engineer-Weeks entschaerft werden kann** — plus zwei Follow-Streams (Cross-Modul-Bridge Auto-Wire, Live-Transcription) fuer die naechsten 90 Tage. Naechste Video-Iteration Zyklus 3 fruehestens W02/2027 (12.01.2027).*
