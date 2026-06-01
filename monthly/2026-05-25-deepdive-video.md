---
year: 2026
week: 22
modul: video
created: 2026-05-25
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 48
tokens_input: ~340000
tokens_output: ~12800
rotation_position: 3/15
---

# Deepdive: video (Mo W22/2026)

> **Dritter Deepdive der Rotation.** Vorgaenger: `crm-core` (W20, 2026-05-11) und `dialer` (W21, 2026-05-18). Naechstes Modul gemaess Rotation: **wiki** (KW23, 2026-06-01). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-Video (2026-05-25):** Modul-Pfade `backend/internal/work/livekit/` (5 Files, 812 LOC), `work/video/` (7 Files, 1281 LOC), `work/recording/` (8 Files, 2504 LOC). **R2-P0-Batch-A komplett** (LiveKit-Secrets-Assertion, Egress-Webhook, Pre-Recording-Consent 412, coturn live). **Funktional korrekt fuer ein 2024-Produkt — strukturell unkonkurrenzfaehig fuer einen 2026-Markt, der gerade vom "Video-Conf-Tool" zur "AI-Video-Agent-Platform" gekippt ist.**

> **Leit-Signal der Woche:** Drei Bewegungen kollidieren binnen 30 Tagen (24. Apr – 25. Mai 2026) — (a) **LiveKit-Stack-Drift**: Tech-Partner LiveKit positioniert sich seit Mai 2026 explizit als "Voice/Video-AI-Agent-Platform" (SAP-Joule-Partnership 12.05.2026, Custom-Voices 06.05.2026, Embed-on-any-Website 19.05.2026); (b) **EU-Sovereignty-Kipppunkt im Video-Segment**: OpenTalk statewide Schleswig-Holstein + Thueringen, France Visio mandatory CNRS 150k Users, Pexip+Wire-Allianz 12.05.2026, BSI C3A 27.04.2026; (c) **EU-AI-Act Disclosure-Pflicht ab 2. August 2026** fuer AI-Voice/Video-Agents — Cosmi muss VOR jedem AI-Feature ein Disclosure-Layer haben. **Dieser Bericht empfiehlt drei Pflicht-Stakes vor Video-Feature-Welle 2 (Sprint 3 / Welle 5).**

---

## State-of-the-Art

Der Video-Konferenz-Markt Mai 2026 durchlaeuft eine andere Bewegung als der Dialer-Markt (W21): nicht "AI-Welle ueberholt alle in 30 Tagen", sondern **zwei Lagerbildungen treffen aufeinander** —

1. **AI-Voice/Video-Platform-Lager** (LiveKit, Daily.co, Whereby Embedded) — Real-Time-Transcription <300ms, Custom-Voices, Voicemail/IVR-Detection, Live-Captions, Whisper-Auto-Summaries, Action-Item-Extraction.
2. **EU-Sovereign-Self-Host-Lager** (OpenTalk, Jitsi, BigBlueButton, Nextcloud Talk, Pexip+Wire, Tixeo) — DSGVO-native, BSI-C5/C3A, ANSSI, GDPR-Articles-12-14-Transparency-Enforcement-2026, MLS-E2EE.

Cosmi ist heute weder das eine noch das andere — Cosmi ist **"LiveKit-self-hosted-mit-Consent-Layer"**. Das war 2024 ein USP, ist 2025 ein Tabellenstake, und wird Q3 2026 ungenuegend.

Drei strukturelle Veraenderungen treiben den Markt seit Maerz 2026:

(a) **Per-Minute-Pricing-Modelle ueberholen Per-Seat-Modelle im Video-Segment frueher als erwartet.** Daily.co liefert $0.004/Participant-Minute + $0.003/Recording-Min in der oeffentlichen Preisliste. Aircall's Vogent-Akquisition (KW19) hat den Per-Minute-AI-Pricing-Standard fuer voice gesetzt; Daily.co erweitert das auf Video. **Cosmi's "4 EUR/Modul" Meetings-Position (vs. Zoom Pro 13-15 EUR) bleibt im Per-Seat-Modell verankert** — strukturell richtig fuer DACH-KMU-Mittelstand, aber die Vergleichsgrundlage hat sich verschoben.

(b) **E2EE im SFU-Kontext ist 2026 produktionsreif.** Jitsi Meet Electron 31.03.2026 mit E2EE-Beta out-of-the-box, OpenTalk SLAC-Vortrag 12.05.2026 zu "E2EE + Package-Based Installation", Pexip+Wire-Partnership 12.05.2026 mit MLS-E2EE. **LiveKit unterstuetzt E2EE via Insertable-Streams-API seit ueber einem Jahr** — Cosmi nutzt es nicht. (Recording-Egress mit E2EE bleibt der technisch harte Teil, weil Server die Frames nicht entschluesseln darf, aber Compliance-Erwartungen werden mit jeder Konkurrenz-Release verschoben.)

(c) **EU-AI-Act Disclosure ab 2. August 2026 wird verpflichtend** fuer AI-Voice/Video-Agents (3 Pflichten: Disclosure-UI, Audit-Logging, Modell-Provider-Compliance-Doc). Cosmi hat heute weder Disclosure-UI noch Audit-Log fuer Video-AI-Interaktionen, weil noch keine AI-Features im Video-Modul existieren. **Das ist gleichzeitig Chance (Greenfield) und Falle (jede zukuenftige AI-Feature in Video MUSS die Compliance-Schicht voraussetzen — nicht nachruesten).**

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. LiveKit (Tech-Partner, threat: low als Konkurrenz, aber HIGH als Stack-Drift-Risiko)**

LiveKit ist Cosmis Tech-Stack. Genau deshalb ist die Stack-Drift kritisch zu beobachten — wenn LiveKit's OSS-Server in 12 Monaten zum "Kommodity-Layer" wird und die AI-Inference-Schicht (LiveKit Inference, ai-coustics, Vogent-aehnliche-Modelle) die Differenzierung uebernimmt, sind Self-Host-Setups ohne native AI-Layer im Markt nicht mehr wettbewerbsfaehig.

- **v1.12.0 (16.05.2026)** — Kritische Security-Change: **TURN-Credentials haben jetzt eine TTL**, ohne die der Client den Raum nicht joinen kann (Quelle: github.com/livekit/livekit/releases). **Direkter Cosmi-Impact:** der noch offene TURN-Wiring-Task (Sprint 2 S2.R2.1b, "TURN-Credentials im AccessToken") muss diese TTL-Semantik beruecksichtigen; sonst funktionieren coturn-Sessions nach kurzer Zeit nicht mehr. Auch: Auto-Create-Rooms-Token-Grant, SIP-Realm-Authentication.
- **v1.11.0 (17.04.2026)** — Data-Tracks default-on (realtime-streaming beyond audio/video). Eroeffnet eine neue Klasse von In-Call-Daten-Strom-Features (Live-Polls, Whiteboards, Shared-State).
- **LiveKit Inference (Mai 2026)** — Custom-Voices-Embedding via Inference-Platform, voicemail/IVR-Detection mit Outbound-Phone-Agents (13.05.2026), Embed-Voice-Agent-on-any-Website (19.05.2026), SAP-Joule-Partnership (12.05.2026, "intelligent voice for Joule"), telli/ai-coustics-Case-Study (20.05.2026).
- **LiveKit Agents v1.5.12 (21.05.2026)** — ElevenLabs Realtime STT, AI Pulse STT, Avatar-RPC, Background-Observer-Pattern fuer Voice-AI-Guardrails (Blog 16.04.2026).
- **Pricing**: Tier-basiert; Compliance-Features (HIPAA BAA, SOC 2) ab Scale-Tier+.
- **Gap zu Cosmi:** LiveKit baut die ganze AI-Inference-Schicht in eigene Tier; Cosmi nutzt LiveKit-OSS-Server und hat keine AI-Layer. Sub-Sekunden-Latenz Voice-AI-Pipeline, Custom-Voices, Embed-on-Website.
- **Strategischer Hinweis:** **Cosmi sollte LiveKit-Inference als Build-vs-Buy-Entscheidung explizit auf den Tisch legen** — nicht jedes AI-Voice-Feature muss in `backend/internal/work/video/ai/` selbst gebaut werden. Aber: LiveKit-Inference ist nicht EU-souveraen-hosted (Stand Mai 2026 unklar) — fuer Cosmi-USP "DSGVO-self-host" bleibt der Build-Path Pflicht fuer Pilot-Tenants in regulierten Branchen.

**2. Whereby (international, threat: medium)**

- **Whereby Embedded** — Video-Call-API per iframe + REST, eingebaut: Captions, Recording + Transcription, Screen-Share, Breakout-Rooms, Chat, Emoji-Reactions, Miro/Trello/YouTube-Integrationen.
- Blog 28.04.2026: "Everything to get started with Embedded", Blog 29.03.2026: "10 technical insights — native-feeling embedded video".
- **Pricing pain points (G2, 2026)**: "steep compared to competitors", "value-for-money decreased — reduced options while keeping pricing", "limited free plans" — strukturelle G2-Reviews zeigen, dass die Embedded-Plattform-Strategie Whereby in die "expensive für was geboten wird"-Wahrnehmung gebracht hat (Quelle: g2.com/products/whereby-meetings/reviews).
- **Gap zu Cosmi:** Live-Captions im SFU-Stream, Recording-Transcription Out-of-the-Box, Breakout-Rooms, iframe-Embed fuer Cosmi-fremde-Anwendungen.
- **Strategischer Hinweis:** Whereby Embedded ist im internationalen API-Video-Markt was Daily.co ist — beide skalieren ueber Embedded-API. Cosmi's "Embed-Cosmi-Video-in-Drittprodukt" ist heute kein Use-Case, sollte es auch nicht sein (Cosmi ist Endprodukt, nicht Plattform). **Whereby-Vergleich liefert vor allem Feature-Benchmark fuer In-Call-UX**, nicht Konkurrenz-Vergleich.

**3. Daily.co (international, threat: medium — AI-Voice-Cloud)**

- **Pipecat Cloud GA** — komplette Voice/Video-AI-Pipeline als Cloud-Service. Daily Bots, Daily Telephony, Pipecat-Framework als Open-Source-Layer + Cloud-Inference.
- **Pipecat 1.1.0 (27.04.2026)** — MistralSTTService (Voxtral Realtime API), Streaming-Transcription mit Interim-Results, automatischer Sprach-Detection, VAD-driven utterance lifecycle.
- **Deepgram-Partnership** — Live-Transcription < 300ms Latenz, 100% Deep-Learning-Modelle, NASA/Nvidia-Referenzkunden.
- **Pricing**: $0.004/Participant-Minute, $0.003/Recording-Min, 10000 free Minutes/Monat, graduated-pricing-Discounts (Quelle: daily.co/pricing/video-sdk).
- **Gap zu Cosmi:** Pipecat-aehnliches-Voice-AI-Framework, Streaming-Transcription Sub-Sekunde, Voxtral/Mistral-Integration (EU-Modell-Provider, **DSGVO-relevant**), Per-Minute-Pricing-Modell.
- **Strategischer Hinweis:** Mistral-Voxtral-Integration ist der eine Datenpunkt, der fuer Cosmi-DACH-Pitch relevant ist. **Mistral-Voxtral als EU-souveraener STT-Provider ist eine direkt evaluierbare Build-vs-Buy-Komponente fuer Cosmi-Video-AI-Layer** — vor Whisper-Self-Host.

**4. Jitsi Meet (open-source, threat: low — aber Architektur-Vorbild)**

- **Jitsi Meet 2.0.10978 (20.05.2026)** + **2.0.10888 (30.03.2026)** — automated Jenkins-Releases, kein detailliertes Changelog publiziert.
- **Jitsi Meet Electron Last Update 31.03.2026** — E2EE-Beta out-of-the-box (WebRTC Insertable-Streams-API, Chromium 83+).
- **Jigasi-Transcription** — multi-engine: Google Cloud STT, Vosk, custom-Whisper-Flavor, Oracle Cloud AI Speech. Faster-Whisper via Skynet-API ist die OSS-Self-Host-Variante.
- **Pain Points**: E2EE-Limitierung — Audio/Video/Screen-Share OK, Chat/Polls NICHT E2EE.
- **Gap zu Cosmi:** E2EE-Beta produktiv (auch wenn limitiert), Jigasi-Transcription-Architektur als Vorbild, Whisper-Self-Host-Stack erprobt.
- **Strategischer Hinweis:** **Jitsi ist nicht Konkurrent fuer Cosmi-KMU-Zielsegment** (Jitsi ist "kostenloses Internet-Service ODER aufwendiges Self-Host"). Aber: **Jitsi-Jigasi-Transcription-Service-Architektur ist 1:1 das, was Cosmi-Video als Whisper-Self-Host-Layer braucht** — externe gateway-app, die per WebSocket/REST in den SFU einklinkt, Audio-Stream abgreift, Whisper.cpp lokal laufen laesst, Subtitles als Data-Track zurueck in den Stream pumpt. Beispiel-Open-Source-Setup: jitsi.support/developer/setup-jitsi-whispercpp-transcriptions.

**5. OpenTalk (DACH, threat: HIGH — direkter EU-Sovereignty-Konkurrent)**

- **OpenTalk 25.4.7** (Mai 2026) — Stabilitaets-, Security-, UX-Optimierung; Software-Update fuer Cloud-Service am 20.04.2026.
- **Statewide-Deployments**: Schleswig-Holstein + Thueringen, Bundesbehoerden via Open Telekom Cloud (Managed Service Partnership).
- **SLAC 11-13.05.2026 Berlin** — Stefan Sydow ueber "The Future of OpenTalk: End-to-End Encryption and Package-Based Installation" am 12.05.2026 — **E2EE wird Roadmap-Promise fuer 2026/2027**.
- **OpenTalk Cloud Service erweitert um Recording + Streaming** (Press-Release 2026).
- **GDPR-native, Open-Source, deutsch (Heinlein-Group, Berlin)**.
- **Gap zu Cosmi:** Statewide-Deployment-Erfahrung, Telekom-Cloud-Partnerschaft (B2B-Channel), E2EE-Roadmap-Promise, Recording+Streaming-Cloud-Service.
- **Strategischer Hinweis:** **OpenTalk ist Cosmis spiegelbildlicher Konkurrent im EU-Sovereignty-DACH-Video-Markt** — gleiche USP-Positionierung ("DSGVO-native Self-Host EU-Video"), aber 18-24 Monate weiter im Go-to-Market (Statewide-Deals existieren). Cosmi gewinnt nicht ueber "DSGVO-besser" — Cosmi gewinnt ueber **"DSGVO + Modul-Integration im KMU-ERP"**: Calendar-Event → 1-Click-Meeting-Link, Activity-Auto-Log nach Meeting-End, CRM-Deal-Aktivitaet aus Meeting-Transcript. **OpenTalk ist Video-Standalone — das ist die Luecke, in die Cosmi-Video stoesst.**

**6. BigBlueButton (open-source, threat: low — Education-Fokus, aber Tech-Lessons)**

- **BBB 3.0.25** + Patches 3.0.23/3.0.24 (Security). **Kurento Media Server ENTFERNT**, Live-Media via mediasoup, Recording via bbb-webrtc-recorder (eigener Service).
- tl;draw v2.0.0-alpha.19 fuer Whiteboard.
- transparentListenOnly-Toggle — User-State-Wechsel ohne Rejoin.
- Cache fuer Presentation-Assets auf S3/MinIO.
- **Live-Transcription**: Browser-SpeechRecognition (Chrome/Edge/Safari) im offiziellen Plugin + Community-Plugins mit Faster-Whisper.
- **Pricing**: Open-Source, kein Per-User-Subscription. Konsumiert von 75% des globalen LMS-Marktes (Canvas, Moodle, Sakai etc.).
- **Pain Points**: Self-Host-Komplexitaet "significant technical knowledge in server admin, networking, system maintenance", max 100 participants in vielen Setups.
- **Gap zu Cosmi:** Whiteboard (tl;draw v2), Polls, Hand-Raise, transparentListenOnly-Pattern, mediasoup-Tech-Stack-Reife.
- **Strategischer Hinweis:** **BBB ist Education-Markt, nicht KMU-Business-Markt.** Aber: das **Kurento-zu-mediasoup-Beispiel ist Tech-Stack-Validation fuer Cosmi-Roadmap** — wenn LiveKit-OSS sich strategisch nicht weiterentwickelt, ist mediasoup-Direct das naechstgroesste OSS-SFU. Build-vs-Buy-Hebel falls LiveKit-Stack-Drift kritisch wird.

**7. Pexip + Wire / Tixeo (EU-Sovereign-Enterprise, threat: medium-low — andere Tier)**

- **Pexip + Wire Partnership (12.05.2026)** — Sovereign EU video + MLS-E2EE Messaging, AFCEA TechNet Cyber Bonn (12.05.2026). Government/Defense/Critical-Infrastructure-Fokus.
- **Tixeo** — ANSSI-zertifiziert, French-only-Hosting, Full-E2EE, Government-/Regulated-Industry-Reference.
- **France Visio** — Mandatory fuer CNRS bis Maerz 2026 (150k User), Defense + National-Health-Insurance bis 2026, alle Behoerden bis 2027. **Strukturell relevant**: nationalstaatliche Sovereignty-Mandates verschaerfen sich, nicht der KMU-Markt — aber Markt-Signal kaskadiert in Enterprise/Mittelstand.
- **Strategischer Hinweis:** Diese Tier ist **nicht Cosmi-Wettbewerbs-Tier**. Aber: **France-Visio-Mandate signalisiert Government-Tendenz, die innerhalb von 12-24 Monaten in regulierten DACH-Branchen (Healthcare, Energie, Anwaltsbueros) ankommt**. Cosmi-Vertraege-Modul plus Cosmi-Video-Modul mit DSGVO-/BSI-C5-/C3A-Konformitaet wird in dem Segment zum strategischen Verkaufsargument.

### Querbewegungen seit KW16 — Markt-Lage Mai 2026

**EU AI Act Disclosure-Pflicht 2. August 2026:** Anrufender muss informiert werden, dass er mit AI-Agent spricht; Audit-Logging fuer alle AI-Interaktionen; Modell-Provider-Compliance-Dokumentation. **Aufwand-Schaetzung pro Modul (intel-deep 2026-05-08): 4-8 Engineer-Weeks fuer Audit-Trail + Disclosure-UI.** Cosmi-Video muss diese Schicht VOR jedem AI-Feature haben — sonst wird jeder spaetere AI-Feature-Launch von Compliance blockiert oder als Compliance-Risiko ausgeliefert.

**BSI C5:2026 + C3A (27.04.2026):** BSI hat neue Criteria fuer Cloud-Autonomie publiziert — "Criteria enabling Cloud Computing Autonomy". Komplementaer zu C5 (Security) wird Sovereignty jetzt messbar. **Direktes Cosmi-USP-Potential**: Cosmi-Video als "C5- und C3A-evaluierbar" zu positionieren, ist im DACH-KMU-/Mittelstand-Vertrieb ein konkretes Verkaufsargument.

**GDPR-Articles-12-14-Coordinated-Enforcement-2026:** EDPB hat Transparenz + Information-Obligations als Fokus des 2026 Enforcement-Frameworks gewaehlt, 25 DPAs beteiligt. "Implied consent is dead" — Plattformen muessen "explicit Opt-In prompts" fuer Recording und AI-Summarization-Features haben. **Cosmi's Pre-Recording-Consent-Stack (Welle 3+3.5) ist regulatorisch genau auf diesem Pfad** — aber AI-Summarization-Opt-In fehlt komplett, weil das Feature noch nicht existiert.

**Voice/Video-AI-Marktfraktur (Q1+Q2 2026):** "Bot-Fatigue" — Enterprise-IT und Legal-Teams bannen Otter.ai/Fireflies wegen Consent-Verletzungen + LLM-Training-Risiken. Markt-Shift zu **bot-free, local-first AI-Notetakers** (Jamie aus DE, Seedext aus FR). Cosmi-Video hat hier **strukturellen Vorteil**, weil das Recording-Consent-Framework bereits live ist — aber kein Notetaker-Feature.

---

## Cosmi-IST-Stand

### Was existiert (Stand 2026-05-25)

**Backend** — `backend/internal/work/livekit/` (812 LOC):
- `service.go` (195 LOC): LiveKit-JWT-AccessToken-Generation, optional TURN-Credentials via HMAC-SHA1 (coturn REST API spec), `IsEnabled()`/`IsTURNEnabled()`-Feature-Flags, `LIVEKIT_API_KEY/SECRET/WS_URL`+`TURN_SECRET/COTURN_HOST`-Env.
- `room_manager.go` (96 LOC) + `egress_manager.go` (69 LOC) + `service_test.go` (452 LOC).
- **R2-P0.2 LiveKit-Secrets-Startup-Assertion** — Prod crasht bei `devkey/devsecret` (`310c803`).

**Backend** — `backend/internal/work/video/` (1281 LOC, 7 Files):
- Models, Postgres-Repository, Service (385 LOC), Tenant-Isolation-Tests, Repository-Interfaces.
- **gRPC `video_grpc.go`** — `tenant_id` aus `middleware.GetTenantID(ctx)` (Welle 3.5).
- **Migration 119**: 4 Dialer/Recording-Tabellen tenant_id-Backfill, `consent_records.tenant_id` von NULLABLE auf NOT NULL.

**Backend** — `backend/internal/work/recording/` (2504 LOC, 8 Files):
- Models, Postgres-Repository, Service (551 LOC), Service-Tests (1116 LOC), RLS-Tests.
- **Pre-Recording-Consent-Stack** (Migration 000107, R2-P0.4): `recordings.pre_recording_consent_at`, `initiator_consent_id`, `recording_consents.responded_at`, Partial-Index.
- **HTTP 412 Precondition Failed** auf `POST /api/v1/video/recordings/start` wenn Pre-Consent fehlt; aufgerufen ueber `POST /api/v1/video/recordings/{id}/initiator-consent`.
- **Recording-Robustness Welle 3.5**: Pre-Consent-Check VOR `CreateRecording` (verhindert Orphan-Rows), `MarkInitiatorConsent` + `GetPreConsentStatus` mit `WHERE id=$1 AND tenant_id=$2` + `RowsAffected==0`-Sentinel, RBAC-Permission-Middleware vor Endpoint.
- **Egress-Webhook `egress_ended`** (R2-P0.5, `d8f89d4`) — setzt `recordings.status=completed` + `file_url`.
- **Cross-Tenant-Tests**: 4 W3.5-Cases (`/recordings/{id}/initiator-consent`: no-tenant, empty-tid, valid-tid, two-tenant) + 4 Sprint-3-F6 DB-Backed.

**Frontend** — `desktop/src/renderer/src/features/video/`:
- `RecordingInitiatorDialog.tsx` — Radix AlertDialog, non-dismissible, ZWINGEND vor `startRecording`.
- `RecordingConsentDialog.tsx` — `i18n-trusted` t(...)-Rendering.
- `RecordingActiveBanner.tsx` — roter Top-Stripe waehrend Aufnahme.
- `CallControls.tsx` — Doppelklick-Guard via `startRecording.isPending`/`stopRecording.isPending`/`confirmInitiatorConsent.isPending`, try/catch + `sonner.toast.error`.
- i18n-Keys `recordingBanner.*` + `recordingInitiator.*` in de/en/fr/it (4 Sprachen).
- **API-Client** auf `authenticatedFetch.ts`-Helper umgestellt (Welle-4B-Refactor); Offline-Queue mit 409-Retry-Class (in-flight wird re-tried statt silently dropped).

**Infra** — `deploy/`:
- LiveKit + LiveKit-Egress als Docker-Container (Ports 7880/7881/7882). 
- LiveKit-Secrets via `livekit-secrets.yaml`-Render-Overlay (`render-configs.sh` + `deploy.sh` Step 2.5 + `envsubst`).
- **coturn live seit 2026-04-19**: Hetzner CAX11 FSN1, `turn.zentria.tech:3478`. LiveKit `use_external_ip:true` aktiv.

**Pricing-Position** (.knowledge/pricing.md): Meetings = **4 EUR/Modul** (vs. Zoom Pro 13-15 EUR im Vergleich). ORBIT-Wizard hat MEETING_SETUPS als eigenen Schritt 4.

### Was strukturell fehlt — Cosmi-Luecken

**Pflicht-Lueck (P0, blockiert):**

1. **LiveKit-TURN-Wiring im Backend** (Sprint-2-Task S2.R2.1b — coturn live, aber AccessToken-TURN-Credentials werden nicht uebergeben). Verstaerkt durch LiveKit v1.12.0-TTL-Aenderung: alte coturn-only-Setups ohne TTL-Awareness werden brechen.
2. **Kein AI-Disclosure-UI-Baustein** (`backend/internal/cross/compliance/ai-disclosure/`) — Pflicht VOR jedem AI-Feature im Video-Modul, sonst EU-AI-Act-Compliance-Risiko ab 2. August 2026.
3. **Kein AI-Audit-Log-Layer** (`backend/internal/cross/ai-audit/`) — analoge Pflicht.
4. **E2EE nicht aktiviert** — LiveKit unterstuetzt es via Insertable-Streams-API, aber Cosmi-LiveKit-Config + Frontend-SDK-Integration fehlt. Bei Recording bleibt E2EE konzeptionell hart (Server muss Frames nicht entschluesseln koennen — Egress + Storage-Strategy braucht Re-Design).

**Hoher-Hebel (P1):**

5. **Keine Live-Transcription** — kein Whisper-Self-Host-Layer, kein Jigasi-aehnlicher-Gateway-Service. Markt-Stake. (`grep transcription|whisper|caption` ueber das ganze video/livekit/recording-Modul: 0 Hits.)
6. **Keine AI-Meeting-Summaries / Action-Items** — kein Notetaker-Feature, obwohl Cosmi-Pre-Consent-Stack die Compliance-Grundlage bereits hat (Differenzierung gegenueber Otter/Fireflies, wenn aktiviert).
7. **Cross-Modul-Bridge fehlt**: Meeting-End → Activity-Auto-Log in CRM-Modul, Action-Item-Extraction → Task-Create in Work-Modul, Recording-Search via FTS in Wiki-Modul. Heute kein Wire-Up.
8. **Kein Whiteboard / Polls / Hand-Raise / Breakout-Rooms** — Tabellenstake im Markt seit Jahren, im Cosmi-Backend nicht modelliert. Wichtigkeit fuer KMU-Use-Cases prufen — Whiteboard ist Education-USP, fuer KMU-Sales-Calls weniger relevant; Breakout-Rooms relevant fuer KMU-Workshops.

**Mittel-Hebel (P2):**

9. **Embedded-API fehlt** — Cosmi-Video kann nicht in Drittprodukte eingebettet werden. Strategisch evt. korrekt (Cosmi ist Endprodukt, nicht Plattform).
10. **Per-Minute-Pricing nicht modelliert** — `backend/internal/billing/`-Schicht hat kein "Meeting-Minute-Counter"-Konzept. Heute irrelevant (Cosmi-Pricing ist Per-Modul), aber wird relevant wenn AI-Per-Minute-Pricing am Markt zementiert wird.
11. **Keine Voice-Modell-Auswahl / Custom-Voices** — bedeutet nichts solange kein AI-Voice-Feature existiert. P3-Hebel post-AI-Roadmap.
12. **Live-Captions** — wenn Live-Transcription da ist, ist Live-Caption-UI ein 1-2-Sprint-Followup.

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | LiveKit (Tech-Partner) | Whereby | Daily.co | Jitsi | OpenTalk | BigBlueButton |
|---|---|---|---|---|---|---|---|
| WebRTC SFU | ✅ via LiveKit | ✅ (eigen) | ✅ | ✅ | ✅ | ✅ | ✅ mediasoup |
| Self-Host (EU) | ✅ Pilot | ✅ | ❌ (SaaS) | ❌ (SaaS) | ✅ | ✅ statewide | ✅ |
| Recording (Server-Side) | ✅ Egress | ✅ Egress | ✅ | ✅ | ✅ Jibri | ✅ Recording+Streaming | ✅ bbb-webrtc-recorder |
| Pre-Recording-Consent (Initiator + Pflicht-Dialog) | ✅ **Welle 3+3.5** | ❌ (Recipe-Docs) | 🚧 Opt-In-UX | 🚧 | ❌ | ❌ | ❌ |
| E2EE (Audio/Video/Screen) | ❌ (LiveKit-Capability ungenutzt) | ✅ Insertable-Streams | ❌ | ❌ | ✅ Beta | 🚧 Roadmap-Promise SLAC | ❌ |
| TURN-Fallback | ✅ coturn live (Backend-Wiring offen) | ✅ TTL v1.12.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Live-Transcription | ❌ | ✅ Inference + STT-Provider | ✅ eingebaut | ✅ Deepgram <300ms | ✅ Jigasi+Whisper | 🚧 | ✅ Plugin (Chrome/Edge/Safari) |
| AI-Meeting-Summaries | ❌ | ✅ Agents-Framework | 🚧 | ✅ Pipecat | 🚧 | ❌ | ❌ |
| Action-Item-Extraction | ❌ | ✅ Agents | 🚧 | ✅ | ❌ | ❌ | ❌ |
| Live-Captions | ❌ | ✅ | ✅ eingebaut | ✅ | ✅ | 🚧 | ✅ |
| Whiteboard / tl;draw | ❌ | ❌ (App-Layer) | ❌ (via Miro-Integration) | ❌ | ✅ | ✅ | ✅ tl;draw v2 |
| Breakout-Rooms | ❌ | ✅ Multi-Room | ✅ | ✅ | ✅ | ✅ | ✅ |
| Custom-Voices (AI) | ❌ | ✅ Inference (06.05.2026) | ❌ | ✅ | ❌ | ❌ | ❌ |
| Voice-Agent-Embed-on-Site | ❌ | ✅ (19.05.2026) | ✅ Embedded-API | ✅ | ❌ | ❌ | ❌ |
| Per-Minute-Pricing | ❌ Per-Modul 4€ | ✅ Tier+Usage | ❌ Seat | ✅ $0.004/min | n/a OSS | ❌ Managed-Service | n/a OSS |
| EU AI Act Disclosure-UI (ab 2026-08-02) | ❌ | n/a (Plattform) | ❌ | ❌ | ❌ | n/a | n/a |
| BSI C5 / C3A-evaluierbar | 🚧 (kein Audit) | ❌ | ❌ | ❌ | 🚧 | ✅ Telekom-Cloud | 🚧 |
| MLS-E2EE Messaging-Bridge | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cross-Modul: Calendar→Meeting-Link | ✅ `GenerateRoomName` deterministic | n/a | n/a | n/a | n/a | n/a | n/a |
| Cross-Modul: Meeting→Activity-Log (CRM) | ❌ | n/a | n/a | n/a | n/a | n/a | n/a |
| Cross-Modul: Action-Items→Tasks (Work) | ❌ (Schema vorbereitet `meeting_action_items`) | n/a | n/a | n/a | n/a | n/a | n/a |
| Doppelklick-Guard + Offline-Queue (Frontend) | ✅ Welle 3.5 | n/a | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cross-Tenant-Tests (Recording) | ✅ 8 Tests | n/a | n/a | n/a | n/a | n/a | n/a |
| **Threat-Level fuer Cosmi-KMU-Markt** | **Self** | **Tech-Drift** | **medium** | **medium** | **low** | **HIGH** | **low** |

**Lesehilfe:** ✅ vorhanden, 🚧 Beta/teilweise/Roadmap-Promise, ❌ fehlt.

**Lese-Insight aus der Matrix:** Cosmi besitzt **vier Differenzierer**, die kein einziger Konkurrent in dieser Tier hat: (1) Pre-Recording-Consent als Pflicht-Initiator-Dialog mit Tenant-Filter und Cross-Tenant-Tests, (2) gRPC-Tenant-Spoof-Hardening, (3) Doppelklick-Guard + Offline-Queue als Frontend-First-Class-Pattern, (4) Calendar-deterministische Room-Names fuer 1-Click-Meeting-Links aus Event-IDs. **Cosmi besitzt gleichzeitig zehn Tabellenstakes-Luecken** — und das Marktfenster fuer Live-Transcription + AI-Summaries schliesst sich Q3 2026 (Bot-free-Lager wird Standard, EU-AI-Act-Disclosure wird Pflicht).

---

## Top-3 Strategische Empfehlungen

### 1. **AI-Compliance-Stack VOR jedem Video-AI-Feature** (Sprint-3-Welle-5 Pflicht-Blocker)

**Warum:** Die Sprint-3-Roadmap plant aktuell keine AI-Features im Video-Modul, aber der Markt waelzt seit April 2026 vom "Video-Conf-Tool" zur "AI-Video-Platform" um (LiveKit-Inference, Pipecat-Cloud, Daily-Bots, sipgate-AI-Receptionist analog im Voice-Bereich). **Sobald das erste Cosmi-Video-AI-Feature (Live-Transcription / Auto-Summary / Action-Item-Extraction) gebaut wird, MUSS die Compliance-Schicht stehen.** EU-AI-Act Disclosure-Pflicht greift 2. August 2026 (sofern Deadline nicht doch verschoben wird) — bei Verstoss bis 7% des globalen Konzernumsatzes Strafe. Aufwand-Schaetzung (intel-deep 2026-05-08): **4-8 Engineer-Weeks** pro Standard-Risk-Use-Case fuer Audit-Trail + Disclosure-UI.

**Scope:**
- `backend/internal/cross/compliance/ai-disclosure/` — UI-Component-Library + Backend-API: `BeginAIInteraction(ctx, interactionType, modelProvider)` → setzt Audit-Log-Entry + zeigt Disclosure-UI-Banner.
- `backend/internal/cross/ai-audit/` — Append-Only-Log mit `(tenant_id, user_id, interaction_id, model_provider, model_id, compliance_doc_url, started_at, ended_at, redactions)`.
- Modell-Provider-Compliance-Dokumentation: Anthropic Claude und Mistral Voxtral haben publizierte EU-AI-Act-Compliance-Docs (Stand Mai 2026 evaluieren). Whisper-Self-Host benoetigt eigene Risk-Assessment-Dokumentation.
- Frontend: `<AIDisclosureBanner />` Komponente in `desktop/src/renderer/src/features/_shared/compliance/`, integriert in alle Voice/Video/Chat-Flows die LLM/STT/TTS touchieren.

**Aufwand:** 6-8 Engineer-Weeks (1 Sprint Backend + Frontend-Library, plus 1 Sprint Modul-Integrationen).

**Strategische Veredelung:** **"AI-Compliance-Badge" als sichtbares UI-Feature** vermarkten — DACH-KMU-Kunden im regulierten Mittelstand sehen das als Verkaufsargument, nicht als Last. Verbindung zu BSI C5 + C3A: Cosmi-AI-Compliance-Stack wird Teil der C3A-Evaluierbarkeit.

**Threat-Klasse:** **A — blockierend fuer alle Video-AI-Features**.

### 2. **Live-Transcription via Whisper-Self-Host als naechster Video-Feature-Schritt** (Sprint-3-Welle-6, nach Empfehlung 1)

**Warum:** Live-Transcription ist Tabellenstake im Markt 2026 — Whereby/Daily/Jitsi/BBB haben es alle, Cosmi hat es nicht. **Whisper-Self-Host loest gleich vier Probleme**: (a) Compliance — Audio bleibt auf Cosmi-Infra, kein US-Cloud-STT-Provider, DSGVO-by-default; (b) Pricing — Tier-spezifisch in Cosmi-Pricing-Modell einbaubar (Tier-1 nicht, Tier-2+ enabled), keine Per-Minute-Cloud-Kosten; (c) Architektur-Vorbild — Jigasi-Pattern bei Jitsi ist 1:1 anwendbar (Sidecar-Service als WebRTC-Listener, Whisper.cpp lokal, Subtitles als LiveKit-Data-Track zurueck); (d) Build-Path zu AI-Summaries — Transcription ist Voraussetzung fuer Notetaker/Action-Item-Extraktion.

**Scope:**
- `backend/internal/work/video/transcription/` neuer Sub-Pkg:
  - `whisper_sidecar/` — Go-Service, der als LiveKit-Participant joinst, Audio-Frames abgreift, an Whisper.cpp-Process (gRPC oder Unix-Socket) weiterleitet, Streaming-Result als LiveKit-Data-Track publisht.
  - `mistral_voxtral/` — Alternative STT-Provider als Build-vs-Buy-Slot (Pipecat 1.1.0-Pattern, EU-souveraen).
  - `provider_selector` — Tenant-Setting: `whisper_self_host` | `mistral_voxtral` | `disabled`.
- Frontend: Live-Caption-Overlay (`features/video/LiveCaptions.tsx`), Opt-In-Toggle pro Tenant + pro Meeting (Default-Off — explizit-Opt-In wegen GDPR-2026-Enforcement).
- Migrations: `meeting_transcripts (id, meeting_id, tenant_id, language, status, started_at, completed_at)`, `meeting_transcript_segments (transcript_id, t_start_ms, t_end_ms, speaker_id, text)`.
- AI-Disclosure-Banner aus Empfehlung 1 integriert.

**Aufwand:** 8-12 Engineer-Weeks (Sidecar-Service + Frontend + Mistral-Voxtral-Build-vs-Buy-Eval + Schema/Migrations).

**Verbindung zu Cosmi-Pricing:** Live-Transcription nur in Tier-2+ aktivieren, als "AI-Module-Add-On" fuer +X EUR/Tenant-Monat positioniert (vergleichbar mit Placetel KI-Add-On €40/Monat Flatrate aus Dialer-Deepdive W21). Vermeidet Per-Minute-Pricing-Komplexitaet, bleibt im Cosmi-Per-Modul-Modell.

**Threat-Klasse:** **A — Markt-Tabellenstake fehlt; Empfehlung 1 muss zuerst stehen**.

### 3. **Cross-Modul-Bridge: Meeting-End → CRM-Activity + Work-Task-Auto-Create** (Sprint-3-Welle-7, post-Transcription)

**Warum:** Das ist Cosmis spiegelbildlich-konsequenter Differenzierer gegenueber OpenTalk (Standalone) und gegenueber LiveKit-Inference (Plattform). OpenTalk-Vortrag SLAC 12.05.2026 betont E2EE — aber OpenTalk hat KEIN CRM/Work-Backend zum bruecken. LiveKit-SAP-Joule-Partnership 12.05.2026 zeigt das Muster ("intelligent voice for Joule") — Cosmi kann das fuer KMU-CRM-Use-Cases analog bauen, aber mit DACH-KMU-Pricing statt SAP-Enterprise-Pricing. **Das ist exakt das Land, in das die Cosmi-Modul-USP zielt**, und es ist heute komplett ungenutzt.

**Scope:**
- `backend/internal/cross/event-bridge/`-Erweiterung um drei Events:
  - `MeetingEnded` → `crm.activity.create(type='meeting', participants, transcript_url, duration_ms)`.
  - `ActionItemExtracted` (post-Transcription/Summary) → `work.task.create(title, assignee, due_date_hint, source_meeting_id)`. Schema `meeting_action_items` existiert bereits (Welle-4B-Migration), wird heute aber nicht von einer AI-Pipeline befuellt — nur manuell via UI.
  - `MeetingRecordingArchived` → `wiki.fts.index(transcript_text, meeting_metadata)` fuer Cross-Modul-Suche.
- Service-Wirings auf existierende RPCs: `crm_grpc.CreateActivity`, `work_grpc.CreateTask`, `wiki_grpc.IndexDocument`. **Keine neuen Endpoints** — nur Event-Subscriber + Mapping-Logik.
- Aufwand-Multiplikator-Effekt: jede neue Cross-Modul-Bridge erhoeht den User-perceived-Wert pro Cosmi-Tier ohne lineare Aufwands-Steigerung.

**Aufwand:** 3-4 Engineer-Weeks (Event-Bridge-Erweiterung + RPC-Wirings + Tests). Vergleichsweise gering, weil Schema + RPCs schon existieren.

**Strategische Veredelung:** Cosmi-Pitch fuer KMU-Sales: "Nach jedem Sales-Call (= Cosmi-Meeting + Dialer-Recording) sind die Action-Items automatisch in der Aufgabenliste des Account-Owners und die CRM-Aktivitaet ist gelogged — ohne dass jemand tippt." Differenzierer 1:1 gegen alle Listenkonkurrenten (Whereby/Daily/Jitsi/OpenTalk/BBB).

**Threat-Klasse:** **B — kein Pilot-Blocker, aber strategischer Multi-Modul-Multiplikator**.

---

## Quellen (Top-Quellen die diesen Bericht stuetzen)

**Cosmi-IST-Stand:**
- `/opt/kmuhub/.knowledge/architektur.md`, `api.md`, `security.md`, `deployment.md`, `integrationen.md`, `pricing.md`, `milestones.md`, `datenbank.md`, `testing.md`, `troubleshooting.md`
- `/opt/kmuhub/backend/internal/work/livekit/{service,room_manager,egress_manager,service_test}.go` (812 LOC)
- `/opt/kmuhub/backend/internal/work/video/{service,postgres_repository,tenant_isolation_test}.go` (1281 LOC)
- `/opt/kmuhub/backend/internal/work/recording/{service,service_test,postgres_repository,rls_test}.go` (2504 LOC)
- Cosmi Pre-Recording-Consent: Migration 000107, R2-P0.4 (commit `f6af609`), Welle 3.5 Recording-Robustness (`d443ab4`)
- Cosmi TURN: coturn live `turn.zentria.tech:3478` (Session 2026-04-19), Sprint-2 S2.R2.1b LiveKit-Wiring offen

**Markt / Konkurrenz (Web-Fetch + Web-Search Mai 2026):**
- LiveKit Server Releases v1.12.0 (16.05.2026) + v1.11.0 (17.04.2026): github.com/livekit/livekit/releases
- LiveKit Blog April-Mai 2026 (15 Posts gefetcht): livekit.com/blog/ (SAP-Joule 12.05.2026, telli+ai-coustics 20.05.2026, Custom-Voices 06.05.2026, Embed-on-Website 19.05.2026, Voicemail-Detection 13.05.2026, Data-Tracks 03.04.2026)
- LiveKit Agents v1.5.12 (21.05.2026): github.com/livekit/agents/releases
- LiveKit Python SDK v1.1.8 (13.05.2026), v1.1.7 (27.04.2026), v1.1.6 (16.04.2026)
- Jitsi Meet Releases 2.0.10978 (20.05.2026) + 2.0.10888 (30.03.2026): github.com/jitsi/jitsi-meet/releases
- Jitsi E2EE Status: jitsi.org/e2ee-in-jitsi, Electron-Client mit E2EE-Beta 31.03.2026
- Jigasi-Transcription-Architektur: github.com/jitsi/jigasi, jitsi.support/developer/setup-jitsi-whispercpp-transcriptions
- BigBlueButton 3.0.25 + Kurento-zu-mediasoup-Migration: docs.bigbluebutton.org/new-features
- BBB-Live-Transcription-Plugin (Browser-SpeechRecognition + Faster-Whisper): github.com/bigbluebutton/plugin-live-transcription, github.com/bigbluebutton-bot/transcription-service
- Whereby Embedded Blog: whereby.com/blog/embedded/ (28.04.2026), G2-Reviews 2026 (Pricing-Pain-Points)
- Daily.co Pricing: daily.co/pricing/video-sdk/ ($0.004/min + $0.003/min Recording, 10k free min/month)
- Pipecat 1.1.0 (27.04.2026): github.com/pipecat-ai/pipecat/releases, MistralSTTService-Voxtral-Integration
- OpenTalk 25.4.7 + Telekom-Cloud-Partnership + SLAC-Vortrag 12.05.2026: opentalk.eu/en/news/, opentalk.eu/en/news/opentalk-slac-2026-open-source-and-digital-sovereignty-practice
- Pexip+Wire Partnership 12.05.2026: wire.com/en/blog/pexip-and-wire-join-forces-to-advance-sovereign-european-communications
- France Visio Mandate (CNRS 150k bis Maerz 2026): thestack.technology/france-to-scrap-zoom-meet-webex-for-homegrown-rival
- BSI C5:2026 + C3A (27.04.2026): bsi.bund.de/EN/Themen/.../C5_2025_node.html, b2b-cyber-security.de/en/BSI-publishes-C3A-cloud-sovereignty-becomes-measurable
- EDPB Coordinated Enforcement 2026 (GDPR Art 12-14 Transparency): summarizemeeting.com/en/faq/gdpr-meeting-recording

**EU-AI-Act / Compliance:**
- EU AI Act Disclosure-Pflicht 2. August 2026: hklaw.com/en/insights/publications/2026/04/us-companies-face-eu-ai-acts-possible-august-2026-compliance-deadline, secureprivacy.ai/blog/eu-ai-act-2026-compliance

**Interne Aggregations-Berichte (zentria-intel):**
- `daily/2026-05-08-evening.md` (LiveKit 2026 AI-Voice/Video-Agents-Transformation, EU-AI-Act-Disclosure-Pflicht-Section)
- `daily/2026-05-13-evening.md` (Voice-Markt-Kontext)
- `daily/2026-05-14-evening.md` (Build-vs-Buy-Logik fuer Voice/Video)
- `weekly/2026-W20.md` (video=0 Items, Markt-ruhig im Cosmi-Polling)
- `monthly/2026-05-18-deepdive-dialer.md` (Voice-AI-Markt-Pattern uebertragbar auf Video)

---

## Picks (vorgeschlagen)

[ ] 🟢 **AI-Compliance-Stack VOR jedem Video-AI-Feature** — Sprint-3-Welle-5 Pflicht-Aufnahme. `backend/internal/cross/compliance/ai-disclosure/` + `backend/internal/cross/ai-audit/` + Frontend-Disclosure-Banner. EU-AI-Act-Deadline 2026-08-02. Aufwand 6-8 EW. **Bedrohungsklasse A — blockierend.**

[ ] 🟢 **LiveKit-TURN-AccessToken-Wiring fertigstellen (S2.R2.1b)** — coturn lebt, AccessToken-Propagation fehlt. Verstaerkt durch LiveKit v1.12.0-TTL-Pflicht (TURN-Credentials brauchen TTL — Backend muss diese setzen). Aufwand <1 EW. **Bedrohungsklasse A — bestehender Sprint-2-Task offen.**

[ ] 🟢 **Live-Transcription via Whisper-Self-Host + Mistral-Voxtral-Build-vs-Buy-Eval** — Sprint-3-Welle-6, nach Compliance-Stack. Jigasi-Pattern adaptieren. Aufwand 8-12 EW. **Bedrohungsklasse A — Markt-Tabellenstake.**

[ ] 🟡 **Cross-Modul-Bridge: MeetingEnded → CRM-Activity, ActionItemExtracted → Work-Task, MeetingRecordingArchived → Wiki-FTS** — Sprint-3-Welle-7. Schema existiert (`meeting_action_items`), nur Event-Bridge + RPC-Wirings + Tests fehlen. Aufwand 3-4 EW. **Bedrohungsklasse B — strategischer Multi-Modul-Multiplikator.**

[ ] 🟡 **E2EE-Aktivierung (Insertable-Streams-API) als Tier-2+-Feature** — LiveKit-Capability ungenutzt. Recording-Egress + E2EE bleibt konzeptionell hart (Server soll Frames nicht entschluesseln) — entweder Opt-In ohne Server-Side-Recording, oder Client-Side-Recording-Egress-Workaround. **Spec + Architektur-Eval in 1 Sprint, Implementation 1-2 Sprints**. → followup 60d.

[ ] 🟡 **BSI C5 + C3A Audit-Vorbereitung fuer Cosmi-Video** — explizite Sovereignty-Evaluierbarkeit als Vertriebsargument im regulierten DACH-Mittelstand. Kein Code, aber Doc + ggf. externer Audit-Berater-Eval. → followup 90d.

[ ] 🟠 **OpenTalk-Monitoring im W22/W23-Polling-Tier** — DACH-Sovereignty-Konkurrent Nr 1, Statewide-Deployments + Telekom-Cloud-Partnership + E2EE-Roadmap. Heute nicht in `sources/video.yaml`-Feeds. Hinzufuegen: opentalk.eu/news-Feed + GitHub-Releases. → followup 14d (Source-Add).

[ ] 🟠 **Pre-Recording-Consent UX-Test mit Pilot-Kunden** — Cosmi hat das Welle-3+3.5-Pattern jetzt seit ~4 Wochen produktiv. UX-Friction-Eval (Doppel-Dialog-Burden bei jedem Recording) + ggf. "Tenant-weit-vorab-vereinbart"-Opt-In-Flag (DPIA-konform). → followup 30d.

[ ] 🔵 **LiveKit-Inference-Build-vs-Buy-Eval** — wenn Cosmi-Whisper-Self-Host-Pfad genommen wird, ist LiveKit-Inference als Alternativ-Anbieter trotzdem zu evaluieren (Cost/Quality/EU-Hosting-Position). LiveKit-EU-Hosting-Status Mai 2026 unklar — prufen. → followup 60d.

[ ] 🔵 **Per-Minute-Counter-Schema im Billing-Modul** — heute irrelevant (Cosmi-Per-Modul-Pricing), wird relevant wenn Per-Minute-AI-Pricing Markt-Standard wird. Vorbereitende Schema-Spec ohne Implementation. → followup 90d.

[ ] 🔵 **Whiteboard / Polls / Breakout-Rooms als Tier-2-Add-Ons** — Markt-Tabellenstakes, fuer KMU-Workshop-Use-Cases relevant. Build-Aufwand erheblich (Whiteboard >12 EW), Buy-Path via tl;draw v2 OSS-Embed prufen. → followup 180d.

---

## Telemetrie

- **Routine:** intel-monday-deepdive
- **Modul:** video (3/15 Rotation, dritte Iteration)
- **Quellen gepollt:** 5 Modul-Konkurrenz-Feeds (video.yaml) + 14 KMU-Hub-Knowledge-Files + 12 Live-WebSearches + 4 Live-WebFetches (LiveKit-Server-Releases, LiveKit-Blog, Jitsi-Releases, BBB-Releases-Index)
- **Konkurrenz-Datenpunkte:** LiveKit 12, Whereby 4, Daily.co 5, Jitsi 5, BigBlueButton 4, OpenTalk 6, Pexip+Wire 3, Tixeo 1, Visio/France 2
- **G2/Capterra-Reviews:** Whereby + BBB qualitativ via WebSearch zusammengefasst (kein Headless-Chromium-Scrape im Scope, G2 blockt Bot-Scrapes ohne JS)
- **EU-AI-Act-Bezug:** Disclosure-Pflicht 2. August 2026 — kritischer Treiber fuer Empfehlung 1
- **BSI-Bezug:** C5:2026 + C3A (27.04.2026) — direkter Cosmi-USP-Hebel
- **Naechstes Modul gemaess Rotation:** **wiki** (KW23, Mo 2026-06-01)
- **State-File:** `.state/deepdive_rotation.json` aktualisiert

---

*Generiert: 2026-05-25 — Dritter Deepdive der Rotation. Modul-Liste 15 (settings.yaml), naechste Iteration desselben Moduls fruehestens KW36/2026 (07.09.2026, ca. 15 Wochen). Strategischer Fokus dieses Berichts: Cosmi-Video ist als Produkt funktional, aber strukturell vom Markt 2026 ueberholt — drei Pflicht-Stakes (AI-Compliance-Stack, Live-Transcription, Cross-Modul-Bridge) schliessen die Luecke vor Q3 2026.*
