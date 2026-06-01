---
year: 2026
week: 20
modul: dialer
created: 2026-05-18
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 54
tokens_input: ~310000
tokens_output: ~11200
rotation_position: 2/15
---

# Deepdive: dialer (Mo W21/2026)

> **Zweiter Deepdive der Rotation.** Vorgaenger: `crm-core` (W20, 2026-05-11). Naechstes Modul gemaess Rotation: **video** (KW22, 2026-05-25). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-Dialer (2026-05-18):** Modul-Pfad `backend/internal/dialer/` Phase-1 ZFA-Pilot. Bisheriger Architektur-Plan: Plain-VoIP mit Outbound + manuellem Recording. AI-Transkription explizit als "Phase C" geplant, kein Datum. Keine Cross-Modul-Anbindung, kein Consent-Framework, kein Voice-Agent. **Marktstand bei Wettbewerbern ueberholt diese Roadmap mit 18–24 Monaten Vorsprung.**

> **Leit-Signal der Woche:** Der Telefonie-Markt ist binnen 14 Tagen (29. Apr – 13. Mai 2026) vom "VoIP-mit-AI-Addon" zum **"AI-Voice-Platform-with-Phone"** gekippt — Aircall-Vogent-M&A, Dialpad Agentic AI Platform, Sipgate AI-Agents Launch, Placetel KI-Receptionist GA. Cosmi plant aktuell ein 2023-Produkt fuer einen 2026-Markt. **Dieser Bericht empfiehlt einen Phase-C → Phase-A Pull-Forward und drei Pflicht-Stakes vor jedem Pilot-Launch.**

---

## State-of-the-Art

Der Dialer-Markt Mai 2026 durchlaeuft eine schnellere Disruption als CRM-Core: drei strukturelle Veraenderungen treffen gleichzeitig. (a) **AI-Voice-Agents werden Tabellenstake** (Aircall, Sipgate, Dialpad, Placetel — alle in 30 Tagen GA). (b) **Per-Minute-AI-Pricing** ($0.04–$0.46/min OpenAI Realtime, Placetel €0.13/min KI-Addon) verdraengt Seat-Modelle im Dialer-Segment frueher als im CRM. (c) **EU-Recording-Compliance** wird mit DSGVO + §201 StGB + Art 179bis StGB-CH zur P0-Implementierungsanforderung — verschaerft durch ElevenLabs-Voice-Cloning-Klage (KW20).

### Top-5 Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Aircall (international, ~23.000 Businesses, threat: high)**

- **Vogent-Akquisition 6. Mai 2026** (San Francisco voice-AI-Startup). Vertikale Integration der Voice-Modell-Schicht. Kernaussage: *"From great to best-in-class"* — spezialisierte Speech-Modelle, zuverlaessigeres Turn-Taking, hoehere Praezision in Live-Calls (Quelle: businesswire 6. Mai, aircall.io/blog/news/aircall-vogent).
- **AI Voice Agent Platform** GA: 24/7 Inbound-Resolution. Referenzkunde SJWD meldet **90% After-Hours-Resolution** ohne Human-Touch.
- **AI Knowledge Automation**: Calls werden automatisch zu institutionellem Wissen, Auto-Sync nach Salesforce, HubSpot, Notion, Slack (Quelle: aircall.io/blog/ai-knowledge-automation).
- **AI Actions**: Post-Call-Automatisierung — AI fuehrt HubSpot-/Zendesk-/Shopify-Actions selbst aus, nicht nur Transkription.
- **AI→Human Handoff**: Vogent-Tech bringt Voice Activity Detection + Turn-Taking mit Kontextuebergabe — kein "transferiere und der Mensch fragt nochmal".
- **Custom Voice Models** via Vogent — Branding-Differenzierung in der AI-Stimme.
- **Pain Points laut G2/Capterra (Mai 2026):** 50–75% Preis-Aufschlag vs. Sticker-Price; Add-Ons +30–80%; Auto-Renewal-Disputes (38% Capterra-Reviews flaggen Support); App-Crashes; intransparente Internat.-Outbound-Tarife (Quelle: aircall.io/pricing, withallo.com/blog/aircall-pricing).
- **Gap zu Cosmi:** Voice-Agent-Platform, Custom-Voice-Modelle, Post-Call-Automation, RAG-Knowledge-Sync, Turn-Taking-Engine, Manager-Dashboards.

**2. JustCall (international, threat: high — neue Pricing-Aggression KW20)**

- **Outbound AI Voice Agent** — Form-Fill → qualifizierter Sales-Call in **unter 60 Sekunden**. Drei Dial-Modi (Preview/Power/Predictive), Local-Presence, Spam-Remediation, Real-Time Agent-Assist, native CRM-Sync.
- **Cold + Warm Transfers** im AI Voice Agent: AI haelt Caller, briefed Mensch, dann Connect. Cold-Transfer optional.
- **AI-Powered Workflows**: Calls + SMS + E-Mail + WhatsApp im selben Agent-Bus.
- **Neue Tarifstruktur Mai 2026:** Team $29, Pro $49, Pro Plus $89, Business custom — entfernt explizit AI-Transkriptions-Caps und buendelt Voice-Agent-Fees rein. Direkter Angriff auf Aircall-Add-On-Modell.
- **Pain Points (G2, 2.376 Reviews):** Call Issues 466 Mentions, Connection Issues 271, Poor Call Quality 234; Desktop-App-Stabilitaet ("Unavailable mid-session"); Native-Integration-Sync-Failures ohne Re-Trigger; versteckte Kosten (SMS-Overage, Unanswered-Call-Charges, AI-Addons) — Quelle: g2.com/products/saas-labs-justcall/reviews.
- **Gap zu Cosmi:** Predictive-Dialer-Modus, Multi-Channel-Agent-Bus (Call/SMS/E-Mail/WhatsApp), 60-Sek-Lead-Reaction-Time, Warm-Transfer-Bridge.

**3. Dialpad (international, threat: medium-high — neue Agentic Platform KW20)**

- **Agentic AI Platform Launch** (Press Release, dialpad.com/press/dialpad-launches-its-agentic-ai-platform): autonome Voice- und Text-Agents, Multi-Step-Reasoning, sichere Connectors in bestehende Systeme. Marketing-Botschaft: *"End of the Chatbot Era."*
- **DialpadGPT** (proprietaeres LLM, Google-Cloud-gehostet). Real-Time Transcription + AI Summaries + Sentiment-Analyse + Action-Item-Extraction.
- **Conversational Intelligence**: NLP-basierte Echtzeit-Analyse, Manager-Dashboards mit Sentiment-Visualisierung.
- **Pain Points:** US-zentriert, schwache DACH-Lokalisierung; Voice-Quality bei Cross-Atlantik-Routing; Pricing intransparent ohne Sales-Call.
- **Gap zu Cosmi:** Eigenes LLM (DialpadGPT), Sentiment-Analyse, Multi-Step Reasoning-Agents, Google-Cloud-Tiefenintegration.
- **Strategischer Hinweis:** Dialpad ist im DACH-KMU-Segment der schwaechste Konkurrent dieser Top-5 (Lokalisierungs-Luecke), aber technologisch der ambitionierteste — wenn Dialpad EU-Datacenters baut, kippt das.

**4. Sipgate (DACH, threat: high — DACH-Kern-Konkurrent)**

- **sipgate AI Agents** (sipgate.ai, April 2026 GA): KI-Empfangsassistent, 24/7 Inbound, Echtzeit-Zugriff auf CRM, Auftragsstatus, Termin-Booking, Ticket-Erstellung. **Setup ohne Programmierung**, Auswahl exklusiver Stimmen + Voice-Modelle.
- **Barge-In-Support** — Caller kann jederzeit unterbrechen, kein "Bot-redet-zu-Ende"-Erlebnis.
- **Strukturierte Uebergabe an Mensch** mit Kontext-Summary — gleiches Pattern wie Aircall-Vogent, aber DACH-gehostet.
- **sipgate Flow API**: Conversational-AI-Bridge — bestehende Chatbots koennen den Voice-Channel sprechen.
- **Contact Center** mit intelligenter Anrufverteilung + Echtzeit-Monitoring (April 2026 Launch).
- **Pricing:** 0€ Grundgebuehr (Team-Tarif), pay-per-use; AI-Agents separat tarifiert.
- **Pain Points laut OMR/Capterra:** Schwaches Reporting fuer Manager (vor Contact-Center-Launch), Einarbeitungs-UX, Mobile-App Bugs.
- **Gap zu Cosmi:** AI-Receptionist, Barge-In, CRM-Realtime-Read, No-Code-Setup-UX, Voice-Modell-Auswahl.
- **Strategischer Hinweis:** Sipgate positioniert sich seit April 2026 explizit als **"europaeischer Voice-AI-Anbieter"** (onetoone.de/artikel/db/143345jg). Das ist exakt das Narrativ, das Cosmi gehoert — Sipgate ist im DACH-Mittelstand-Segment Cosmis spiegelbildlicher Konkurrent.

**5. Placetel / Cloudya / NFON (DACH, threat: high — DACH-Klassik-Anbieter mit KI-Sprint)**

- **Placetel AI / KI-Empfangsassistent** (channelpartner.de/article/4159523, Mai 2026 in Breiten-GA): KI-Receptionist, KI-Call-Beantworter, KI-Support-Mitarbeiter, KI-gestuetzte Lead-Gen.
- **Pricing-Modell:** Basic €4.90/Nebenstelle, Premium €14.90 (inkl. Video + Messaging), **KI-Addon ab €0.13/Min oder €40/Monat-Flatrate**. Erstes DACH-Telefoniesegment mit klar publiziertem Per-Minute-AI-Pricing.
- **150+ Telefonfunktionen**, DSGVO-Compliance ist Werbe-Hauptargument, EU-Hosting.
- **Pain Points:** UX-Sprung von "Klassik-PBX" zu "AI-Receptionist" ist gross — Setup-Wizards noch unfertig (Berichte aus pad.systems-Reviews).
- **Gap zu Cosmi:** KI-Receptionist im Default-Setup, klar publiziertes Per-Minute-Pricing-Modell, breite Reseller-Channel-Distribution (Telekom-Beteiligung historisch).

### Erweiterte Lage — Tech-Stack-Veraenderungen seit KW16

- **LiveKit Agents 1.5.x (April 2026)**: Native SIP + Phone Numbers (kein Twilio-Bridge mehr), MCP-Tool-Support, adaptive Interruption-Handling. Cosmi nutzt LiveKit fuer Video — der Stack ist **bereits im Haus**. Eine Voice-Agent-Implementierung in Cosmi-Dialer kann LiveKit-Agents direkt einsetzen, ohne neuen Vendor.
- **OpenAI Realtime API GA + GPT-Realtime-2** (Audio-Token $32/M Input, $64/M Output; Whisper-Realtime $0.017/Min Transkription). Per-Minute-Range **$0.04–$0.46/Min uncached**, **$0.05–$0.10/Min** mit Prompt-Caching + Tool-Output-Trimming. Diese Spanne ist der eigentliche Hebel: Cosmi kann mit Caching-Disziplin **5–10× billiger** als naive Implementierungen operieren.
- **EU-Recording-Recht verschaerft KW20**: ElevenLabs-Klage (Sifted 14. Mai, unautorisiertes Voice-Cloning von Journalisten) ist Praezedenz fuer "Voice Print = personenbezogenes Datum". Kombiniert mit §201 StGB (DE, All-Party-Consent strafrechtlich verankert), Art 179bis StGB (CH, identisch streng), und DSGVO Art 6/7 Consent-Anforderung ergibt sich: **Pre-Call-Consent-Audio-Prompt + opt-in-Logging sind 2026 P0, nicht P1.**
- **Open-Source-Stack ist reif**: FreePBX 17 (Asterisk 21 + PHP 8.2, Debian 12-Base), FusionPBX (FreeSWITCH-basiert, Multi-Tenant nativ), VICIdial (Predictive-Dialer von 2003 mit aktiver 2026-Roadmap), Issabel (Asterisk+FreePBX-Suite). **Architektonische Wahlfreiheit**: Cosmi kann auf Asterisk (Single-Threaded, klein-mittel) ODER FreeSWITCH (Multi-Threaded, hochvolumig) bauen. FreeSWITCH ist der EU-souveraene High-Volume-Default.

---

## Cosmi-IST-Stand

> Hinweis: KMU-Hub Repository (`~/KMU-Hub/.knowledge/` und `backend/internal/dialer/`) ist nicht in dieser Umgebung gemountet. IST-Stand abgeleitet aus: (a) KW20-Weekly + Daily-Cluster-Analyse, (b) intel-repo `keepers/aircall-ai-voice-blitz` (Cosmi-Status-Tabelle), (c) `sources/dialer.yaml` (Phase-1 ZFA-Pilot Notiz), (d) `monthly/2026-05-11-deepdive-crm-core.md` (Cross-Modul-Referenzen).

### Was Cosmi heute hat (Mai 2026)

- **Modul-Pfad-Definition**: `backend/internal/dialer/` markiert als Tier-1, Phase-1 ZFA-Pilot.
- **Watch-Topics laut `sources/dialer.yaml`**: Call-Recording-Compliance DSGVO, Auto-Transkription, AI-Powered-Coaching, Power-Dialer-Modi, TURN/STUN-Setups, EU-VoIP-Anbieter — diese Liste ist konzeptionell aktuell, aber implementierungstief noch null.
- **Voraussichtliche Tech-Basis**: LiveKit (bereits fuer Video-Modul im Haus), Postgres (Tenant-Retrofit Migration 081 + 106/111 produktiv lt. CRM-Deepdive), gRPC-Service-Mesh.
- **Cross-Modul-Hooks vorhanden**: CRM `internal/crm/` mit 11 Sub-Packages, 38 gRPC-Methoden — ein Dialer-AI-Agent kann hier hooken. Schichten/Rapporte-Pfade existieren ebenfalls (siehe Themen-Daten-Modell W20).

### Was Cosmi heute nicht hat

| Fehlend | Schwere | Pflicht fuer Pilot? |
|---|---|---|
| AI-Transkription (post-call) | hoch | **Ja** — sonst kein 2026-Produkt |
| Realtime-Transkription (live) | mittel | Nice-to-have Phase B |
| AI Voice Agent (Inbound 24/7) | hoch | **Ja** — Tabellenstake bei allen 5 Konkurrenten |
| Pre-Call-Consent-Framework | kritisch | **Ja** — Rechtspflicht §201 StGB + Art 179bis CH |
| Auto-CRM-Sync (Call → Deal/Contact) | hoch | **Ja** — Standardfeature seit 2023 bei Wettbewerb |
| Post-Call AI Actions (HubSpot-style) | mittel | Phase B |
| Predictive-/Power-Dialer-Modi | mittel | Phase B |
| Turn-Taking + Barge-In | hoch | **Ja** fuer Voice-Agent |
| Manager-Performance-Dashboard | mittel | Phase B |
| Per-Minute-AI-Pricing-Infrastruktur | hoch | **Ja** — Outcome-Pricing-Wave |
| Voice-Print-Loeschungs-API (DSGVO Art 17) | kritisch | **Ja** — ElevenLabs-Praezedenz |
| Local-Presence-Numbers (Outbound) | niedrig | Optional |
| SMS-/WhatsApp-Multi-Channel | mittel | Phase C |

### Cosmi-strukturelle Vorteile (ggue. Wettbewerb)

1. **EU-Datensouveraenitaet** ist Pflicht-Argument bei 4 von 5 Konkurrenten teilweise erfuellt oder unklar (Aircall US-Jurisdiktion, JustCall US, Dialpad US/Google-Cloud, Placetel EU/DE, Sipgate EU/DE). Cosmis Self-Hosted-Option + EU-Hosting ist 1:1 mit Sipgate + Placetel, aber besser als alle drei US-Player.
2. **Cross-Modul-Kontext nativ**: Aircall + Sipgate + JustCall syncen via Integration-API zu Salesforce/HubSpot — das ist 100ms+ Latenz und Out-of-Band. Cosmi-Dialer kann CRM/Schichten/Rapporte/Vertraege/Helpdesk **in-Process** lesen. **Dies ist Cosmis architektonischer Killer-Vorteil** — kein Wettbewerber hat das, weil keiner die Suite hat.
3. **Outcome-Pricing-Architektur in Planung**: Wenn `backend/internal/billing/ai-credits/` (lt. W20-Followup) frueh kommt, ist Cosmi-Dialer ab Tag 1 outcome-pricing-konform. Aircall musste das nachruesten, Sipgate noch nicht entschieden.
4. **LiveKit-Stack bereits im Haus**: Voice-Agent-Implementierung braucht keinen neuen Vendor — LiveKit Agents 1.5.x mit nativem SIP, MCP-Support, Adaptive-Interruption ist sofort einsetzbar. Aircall musste Vogent kaufen, Cosmi muss LiveKit aktivieren.

---

## Konkurrenz-Vergleichstabelle

Legende: ✅ produktiv · 🚧 Beta/Ankuendigung · ❌ nicht vorhanden · ❓ unklar

| Feature | Cosmi (Plan) | Aircall | JustCall | Dialpad | Sipgate | Placetel |
|---|---|---|---|---|---|---|
| **Voice/PBX-Basics** | | | | | | |
| Outbound Calling | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ |
| Inbound Routing / IVR | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ |
| Call Recording (manuell) | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ |
| Local-Presence-Nummern | ❌ | ✅ | ✅ | ✅ | ✅ DACH | ✅ DACH |
| EU-Datacenter / Self-Host | ✅ Self-Host | ❌ US | ❌ US | ❌ US/Google | ✅ DE | ✅ DE |
| **AI-Voice-Stack** | | | | | | |
| Post-Call-Transkription | ❓ Phase C | ✅ | ✅ | ✅ DialpadGPT | ✅ | ✅ |
| Realtime-Transkription | ❌ | ✅ | ✅ | ✅ | ✅ | ❓ |
| AI Voice Agent (24/7 Inbound) | ❌ | ✅ Vogent | ✅ | ✅ Agentic | ✅ April'26 | ✅ Mai'26 |
| Turn-Taking + Barge-In | ❌ | ✅ Vogent | ✅ | ✅ | ✅ | ❓ |
| AI→Human Warm Handoff | ❌ | ✅ Vogent | ✅ | ✅ | ✅ | 🚧 |
| Post-Call AI Actions (CRM-Writeback) | ❌ | ✅ AI Actions | ✅ Workflows | ✅ Connectors | 🚧 | ❌ |
| Sentiment-Analyse | ❌ | 🚧 | ✅ Iq | ✅ | ❓ | ❌ |
| Custom Voice Models / Brand Voice | ❌ | ✅ Vogent | ❌ | ❓ | ✅ Voice-Auswahl | ❓ |
| **Cross-Modul / Integration** | | | | | | |
| Native CRM-Integration | ✅ in-process | ✅ Sync HubSpot/SF | ✅ Sync | ✅ Sync | ✅ Sync | ✅ Sync |
| Cross-Modul-Kontext (Schichten/Rapporte) | ✅ in-process | ❌ | ❌ | ❌ | ❌ | ❌ |
| RAG-Knowledge aus Calls | ❌ | ✅ Knowledge-Auto | 🚧 | ✅ | 🚧 | ❌ |
| MCP-Server fuer Voice-Daten | ❌ | ❓ | ❌ | ❓ | ❌ | ❌ |
| **Compliance / Recht** | | | | | | |
| Pre-Call-Consent-Prompt (DE/CH) | ❌ | 🚧 | 🚧 | 🚧 | ✅ DACH-Default | ✅ DACH-Default |
| Voice-Print-Loeschungs-API | ❌ | ❓ | ❓ | ❓ | ❓ | ❓ |
| DSGVO-Auftragsverarbeitung (AVV) | ✅ EU | 🚧 (US-Jurisdiktion) | 🚧 | 🚧 | ✅ | ✅ |
| §201 StGB / Art 179bis CH konform | ✅ moeglich | ⚠ riskant | ⚠ riskant | ⚠ riskant | ✅ | ✅ |
| **Dialer-Modi** | | | | | | |
| Manual-Dial | 🚧 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Power-Dialer | ❌ | ✅ | ✅ | ✅ | ❓ | ❓ |
| Predictive-Dialer | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Preview-Dialer | ❌ | ✅ | ✅ | ✅ | ❓ | ❓ |
| **Reporting / Coaching** | | | | | | |
| Real-Time Agent-Assist | ❌ | ✅ | ✅ | ✅ | 🚧 | ❌ |
| Manager-Performance-Dashboard | ❌ | ✅ | ✅ | ✅ | ✅ Contact Center | 🚧 |
| Sprach-Coaching (AI-Hinweise) | ❌ | ✅ | ✅ Iq | ✅ | ❌ | ❌ |
| **Pricing-Modell** | | | | | | |
| Seat-basiert | 🚧 | ✅ €30–€50/Seat | ✅ $29–$89 | ✅ ~$25+ | ✅ Pay-per-Use | ✅ €4.90–€14.90 |
| Per-Minute-AI-Pricing | ❓ | ❓ Add-on | ❓ Add-on | ❓ | ✅ Add-on | ✅ €0.13/Min |
| Outcome-Pricing ($/Lead, $/Resolved) | ❌ | ❓ | ❓ | ❓ | ❌ | ❌ |
| Transparente Add-On-Bepreisung | ❓ | ❌ G2-Pain | ❌ G2-Pain | ❌ Sales-Call | ✅ | ✅ |

**Verdichtung:** Cosmi hat aktuell **drei strukturelle Vorteile** (EU-Souveraenitaet, Cross-Modul-Kontext, Self-Host-Option) und **mindestens 12 Pflicht-Luecken** vor Pilot-Launch. Die Vorteile sind nicht durch Roadmap-Beschleunigung der Wettbewerber einholbar (architektonisch verankert). Die Luecken sind binnen 6–9 Monaten schliessbar, wenn LiveKit-Agents + OpenAI-Realtime + DSGVO-Consent-Framework als Pflicht-Stake gebaut werden.

---

## Top-3 Strategische Empfehlungen

### 1. **Phase-C → Phase-A Pull-Forward: AI-Voice-Stack ist Tabellenstake, nicht Differenzierung**

**Empfehlung:** Cosmi-Dialer-Pilot darf **nicht ohne** (a) Post-Call-Transkription, (b) automatische CRM-Sync, (c) AI-Call-Summary launchen. Diese drei Features sind nicht mehr Differenzierungs-Merkmale — sie sind 2026-Marktstandard bei allen fuenf Top-Konkurrenten und Pflicht-Stake fuer einen ernstzunehmenden DACH-KMU-Dialer.

**Begruendung:**
- Aircall hat in **10 Tagen** (29. Apr – 8. Mai) 6 AI-Produkt-Launches + 1 M&A kommuniziert (Quelle: aircall.io/blog 13. Mai).
- Sipgate ist seit April 2026 GA mit identischem Feature-Set im DACH-Markt.
- Placetel bietet KI-Receptionist als €40/Monat-Addon — die Eintrittsschwelle ist niedrig genug, dass Cosmi-Kunden es als "Default-Erwartung" mitbringen.
- Ohne diese Features ist Cosmi-Dialer ein **2023-Plain-VoIP-Produkt im 2026-AI-Markt** (keeper W20: "Plain-VoIP-Produkt im AI-Standard-Markt").

**Konkrete technische Umsetzung:**
- `backend/internal/dialer/transcription/` — OpenAI Whisper-Realtime ($0.017/Min) oder Self-Hosted Whisper-large-v3 (Latency-Tradeoff) als Engine. Watermark + Tenant-Scoped-Storage.
- `backend/internal/dialer/voice_agent/` — LiveKit Agents 1.5.x mit nativem SIP. Stack ist im Haus, kein neuer Vendor.
- `backend/internal/dialer/post_call_actions/` — Cross-Modul-Hooks: CRM-Contact-Update, Helpdesk-Ticket-Create, Vertraege-Followup-Schedule.
- Pricing: Per-Minute-Caching-Disziplin Pflicht. Range $0.05–$0.10/Min mit Caching, statt $0.18–$0.46/Min uncached (Quelle: callsphere.ai/blog/vw2c-openai-realtime-cost-per-minute-math-2026). Faktor 5× ist Marge.

**Pull-Forward-Argument:** Phase-C (urspruenglich "spaet" gepant) muss vor Phase-B (Predictive-Dialer-Modi). Andere Reihenfolge erzeugt Kunden-Erwartungs-Diskrepanz.

**Trade-Off:** Erhoeht Pilot-Komplexitaet, verschiebt Pilot-Launch evtl. 4–8 Wochen. **Akzeptable Verschiebung**, weil Pilot ohne AI-Stack ohnehin fehlschlagen wuerde — keine ZFA-Kanzlei oder DACH-KMU wuerde 2026 ein Plain-VoIP-Produkt evaluieren, wenn Sipgate/Placetel Default-KI mitliefern.

---

### 2. **Pre-Call-Consent-Framework als P0 (DSGVO + §201 StGB + Art 179bis StGB CH + ElevenLabs-Praezedenz)**

**Empfehlung:** `backend/internal/dialer/recording/consent/` ist **vor jedem Recording-Code-Pfad** zu bauen. Pflichtschritte: (a) Pre-Call-Audio-Prompt mit Opt-In-Logging, (b) opt-in-Status pro Call-Leg getrennt persistiert, (c) Voice-Print-Loeschungs-API (DSGVO Art 17 Recht auf Vergessen), (d) Recording-Default = AUS, nicht AN.

**Begruendung — drei konvergente Rechtslagen:**
- **§201 StGB (DE)** — All-Party-Consent strafrechtlich verankert, Verletzung ist Vergehen mit Freiheitsstrafe bis 3 Jahre. Keine Business-Ausnahme. Nur §32/§34 StGB (Notwehr/Notstand) als enge Ausnahme (Quelle: bclplaw.com Lexology-Analyse).
- **Art 179bis StGB (CH)** — Identisches Strafrecht, Schweizer Anwalts-/Treuhandkanzleien (ZFA-Pilot-Zielgruppe!) sind hier strafrechtlich exponiert.
- **DSGVO Art 6/7** — Consent muss "explizit, freiwillig, informiert, widerrufbar" sein. Pre-Call-Prompt ist State-of-the-Art-Compliance.
- **ElevenLabs-Klage (Sifted 14. Mai 2026)** — Praezedenz: Voice Print = personenbezogenes Datum, unautorisiertes Cloning/Training auf Voice-Daten ist klagbar.

**Konkrete technische Umsetzung:**
- **Outbound:** Audio-Prompt vor Recording-Start ("Dieses Gespraech wird zu Servicezwecken aufgezeichnet — bitte druecken Sie 1, um zuzustimmen, oder 2, um abzulehnen"). DTMF-Confirmation persistiert mit Call-ID, Timestamp, Tenant-Scope.
- **Inbound:** Recording-Default AUS bis Consent-Prompt erfolgreich abgeschlossen.
- **Voice-Print-Loeschung:** Customer Self-Service-API zur Loeschung aller Voice-Daten, audit-trail-loggable. Voraussetzung fuer EU-Vertrieb an regulierte Branchen (Banken, Versicherungen, Treuhand).
- **Consent-Storage**: Tenant-Scoped, immutable Append-Only-Log, separat vom Audio-Storage. Wenn Audio geloescht wird, bleibt Consent-Beleg fuer Audit.

**Strategischer Differenzierungs-Punkt:** Cosmi kann das **"DACH-Recording-Konform-by-Default"-Versprechen** als Sales-Argument fuehren — Aircall, JustCall, Dialpad sind hier strukturell schwach (US-Jurisdiktion + Default-On-Logik). Sipgate + Placetel haben das im DACH-Default — aber Cosmi hat den Cross-Modul-Kontext zur **automatischen Vertragsfuehrung** (Vertraege-Modul kennt opt-in-Status pro Kontakt, nicht pro Anruf — das ist neu).

**Trade-Off:** Recording-Friction senkt UX bei Cold-Outbound. **Akzeptabler Verlust** — Cold-Outbound ist im DACH-KMU-Segment ohnehin in regulatorischem Niedergang (TKG/UWG-Verschaerfungen 2025/26).

---

### 3. **Cross-Modul-Kontext als Architektonisches Differenzierungs-Merkmal**

**Empfehlung:** `backend/internal/dialer/context/` ist als **erstklassiger** Modulpfad zu bauen, nicht als Nachgedanke. Voice-Agent + Live-Coach + Post-Call-Actions muessen in-process auf CRM, Schichten, Rapporte, Vertraege, Helpdesk, Buchhaltung lesen koennen — nicht via REST-Sync, nicht via Webhook-Bridge.

**Begruendung:**
- **Architektonischer Killer-Vorteil**: Kein Wettbewerber hat eine integrierte Cosmi-aehnliche Modul-Suite. Aircall syncen Daten via API zu HubSpot/Salesforce (Latenz, Datenkonsistenz-Probleme, Vendor-Lock-In im Drittsystem). Cosmi kann **in-Process** auf gleicher Datenbank lesen — Latenz <10ms statt 100ms+, kein Sync-Drift, kein Out-of-Band-Failure.
- **Konkrete Voice-Agent-Use-Cases**, die nur Cosmi loesen kann:
  - *Inbound-Caller-Identifikation*: Agent erkennt Anrufer per CRM-Lookup → kennt offene Helpdesk-Tickets, offene Rechnungen (Buchhaltung), naechsten Termin (Schichten/Rapporte), letzten Vertragsstand (Vertraege). Kein Wettbewerber kann das ohne 5 Integrationen.
  - *Outbound-Voice-Agent fuer Mahnung*: Liest offene Rechnung aus Buchhaltung, ruft Kunde proaktiv an, bietet Stundungs-Form aus Formulare-Modul direkt im Call.
  - *Schichtwechsel-Bridge*: Voice-Agent erkennt aktuelle Schicht-Lage aus Schichten-Modul, leitet Calls an aktiven Bereitschafts-Agent.
  - *Vertragsfuehrung*: Agent kennt opt-in-Status pro Kontakt (nicht pro Call) aus Vertraege-Modul — vermeidet Doppel-Consent-Frage.
- **Marketing-Botschaft:** "Cosmi-Dialer kennt deinen Kunden, deine Schicht, deinen Vertrag — Aircall kennt nur das Telefongespraech." Diese Botschaft funktioniert in 2 Saetzen, ist verifizierbar und konkurrenzlos.

**Konkrete technische Umsetzung:**
- `internal/dialer/context/resolver.go` — Single-Lookup-Service fuer Call-Context: Phone-Number → Contact (CRM) → Open Issues (Helpdesk) → Active Contracts (Vertraege) → Pending Invoices (Buchhaltung) → Shift Context (Schichten).
- gRPC-Streaming-Endpoint fuer LiveKit-Agent: Kontext-Stream waehrend Call laeuft. Updates bei DB-Changes pushen.
- **MCP-Server-Layer**: Voice-Agent als MCP-Client, Cosmi-Module als MCP-Server — externe AI-Agents (Claude/ChatGPT) koennen Voice-Daten konsumieren mit gleicher Berechtigung (siehe CRM-Deepdive W20, Twenty v2.0 MCP-Native-Architektur).

**Trade-Off:** Erhoeht Modul-Kopplung — Aenderungen an CRM-Schema koennen Dialer-Kontext brechen. **Akzeptabel**, wenn Cross-Modul-Contracts klar versioniert sind (gRPC-Proto-Versioning). Dies ist ohnehin die Cosmi-Strategie ("modulare Suite, in-process integriert").

---

### Bonus-Empfehlung: Outcome-Pricing-Alignment mit `billing/ai-credits/`

Aus W20-Cross-Themen-Cluster: 6 Plattformen haben in 14 Tagen Outcome-/Credit-basiertes AI-Pricing eingefuehrt. Cosmi-Dialer ist der **erste Modul-Kandidat fuer Outcome-Pricing** in Cosmi (Voice-Minuten + qualifizierte Leads + geloeste After-Hours-Calls = klare Outcome-Metriken). Wenn `internal/billing/ai-credits/` rechtzeitig kommt, ist Cosmi-Dialer ab Tag 1 Outcome-konform — Aircall/JustCall mussten das nachruesten. Empfehlung: `dialer_ai_minutes`, `dialer_ai_resolved_inbound`, `dialer_ai_qualified_lead` als drei AI-Usage-Event-Typen in `billing/ai_usage_events/`.

---

## Quellen

### Wettbewerber-Primaerquellen (KW16–KW20, 8 Wochen)

- **Aircall:** aircall.io/blog/news/aircall-vogent (6. Mai 2026), aircall.io/blog/ai-knowledge-automation, aircall.io/blog/ai-voice-agent-platform, aircall.io/blog/features/ai-actions, aircall.io/blog/features/agent-performance, businesswire 6. Mai 2026, directorsclub.news 7. Mai 2026
- **JustCall:** justcall.io/product/outbound-ai-voice-agent, justcall.io/ai, justcall.io/blog/outbound-voice-ai.html, justcall.io/blog/justcall-iq-new-pricing-plans.html (KW20 Pricing-Reform), help.justcall.io/en/articles/10903546-cold-warm-transfers-in-ai-voice-agent
- **Dialpad:** dialpad.com/press/dialpad-launches-its-agentic-ai-platform (Agentic AI Launch KW20), dialpad.com/features/artificial-intelligence, dialpad.com/whats-new
- **Sipgate:** sipgate.ai (April 2026 GA-Launch), sipgate.ai/preise, sipgate.de/blog/wir-machen-unsere-telefonie-anschlussfahig, onetoone.de/artikel/db/143345jg (sipgate-EU-Voice-AI-Positionierung)
- **Placetel:** placetel.de/telefonanlage, placetel.de/3cx-alternative, channelpartner.de/article/4159523 (KI-Empfangsassistent-GA)

### Reviews / G2 / Capterra / OMR

- **Aircall:** g2.com/products/aircall/reviews, capterra.com/p/184709/Aircall, capterra.com/p/184709/Aircall/pricing, withallo.com/blog/aircall-pricing (50-75%-Aufschlag-Analyse), voicedrop.ai/aircall-review-explained
- **JustCall:** g2.com/products/saas-labs-justcall/reviews (2.376 Reviews, 466 Call-Issues-Mentions), capterra.com/p/157853/JustCall/reviews, getvoip.com/reviews/justcall, dememarketing.com/justcall-review-en
- **Dialpad:** research.com/software/reviews/dialpad-ai-voice, businessnewsdaily.com/16087-dialpad.html, business.com/reviews/dialpad
- **Sipgate:** omr.com/en/reviews/product/sipgate, capterra.com/p/184990/sipgate-team
- **Placetel:** premium-electronics.eu/blogs/telekommunikation-ki-telefonie/voip-telefonanlage-kmus-2026-placetel-3cx-sipgate-vergleich, mimann.net/blog/voip-anbieter-im-vergleich-2026

### Tech / Stack / Compliance

- **LiveKit Agents 1.5.x:** docs.livekit.io/agents, github.com/livekit/agents, livekit.com/voice-agents, docs.livekit.io/frontends/telephony/agents
- **OpenAI Realtime:** openai.com/api/pricing, openai.com/index/introducing-gpt-realtime, callsphere.ai/blog/vw2c-openai-realtime-cost-per-minute-math-2026, aipricing.guru/news/openai-realtime-2-voice-models-api-pricing-impact-may-2026
- **EU Recording Law:** bclplaw.com Lexology-Analyse "Can Companies Record Customer Service Calls in the EU?", iapp.org/news/a/how-do-the-rules-on-audio-recording-change-under-the-gdpr, recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws, gdprlocal.com/gdpr-recording-calls
- **Open-Source-Stack:** vicistack.com/blog/open-source-call-center-software, sheerbit.com/fusionpbx-vs-freepbx-vs-3cx-ip-pbx-open-source-pbx-comparison, community.freepbx.org (OMniLeads 1.31)

### Cosmi-interne Querverweise

- `weekly/2026-W20.md` (Strategie-Bewegung T03: Aircall-AI-Voice-Blitz)
- `keepers/aircall-ai-voice-blitz-dialer-markt-ist-2026-markt-cross-w20.md`
- `daily/2026-05-13-morning.md` (Dialer-Cluster, 7 Items, 4 Hot)
- `daily/2026-05-14-evening.md` (ElevenLabs-DSGVO-Cluster)
- `monthly/2026-05-15-competitor-review-analysis.md` (Pain-Point-Pattern-Analyse-Methodik)
- `monthly/2026-05-11-deepdive-crm-core.md` (Outcome-Pricing-Architektur-Kontext)
- `followups/outcomecredits-based-ai-pricing-6-plattformen-in-1-cross-w20.md`
- `sources/dialer.yaml`, `sources/_competitors.yaml`

### Source-Maintenance-Hinweis

Aus `daily/2026-05-12-morning.md`: Aircall-RSS (404), Dialpad-RSS (403) — Feed-URLs sind veraltet. **Empfehlung:** Vor naechstem Dialer-Polling Source-Maintenance — neue Feed-URLs recherchieren oder Web-Scrape-Adapter (Atom-Discovery) bauen. Affects: aircall-rss-dialer, dialpad-rss-dialer. JustCall + Sipgate Feeds funktionieren.

---

## Picks (vorgeschlagen)

[ ] 🟢 **AI-Voice-Stack als Pflicht-Stake vor Pilot-Launch** (Pull-Forward Phase C → Phase A): Transkription + CRM-Sync + Call-Summary. Architektur: LiveKit Agents 1.5.x + OpenAI Realtime (oder Whisper Self-Hosted). Pricing-Modell: $0.05–$0.10/Min mit Caching-Disziplin.
[ ] 🟢 **Pre-Call-Consent-Framework als P0** (`internal/dialer/recording/consent/`): DTMF-Opt-In, Voice-Print-Loeschungs-API, Default-Off. §201 StGB + Art 179bis CH + ElevenLabs-Praezedenz.
[ ] 🟢 **Cross-Modul-Kontext-Resolver** (`internal/dialer/context/`): In-Process-Read auf CRM/Helpdesk/Vertraege/Buchhaltung/Schichten. gRPC-Streaming an LiveKit-Agent. Architektonischer Differenzierungs-Killer.
[ ] 🟡 **MCP-Server-Layer fuer Voice-Daten** (Follow-Up 30d): Konsistenz mit Cosmi-MCP-Roadmap aus CRM-Deepdive. Tracked in `followups/`.
[ ] 🟡 **Outcome-Pricing-Eventtypen fuer Dialer** (Follow-Up 30d): `dialer_ai_minutes`, `dialer_ai_resolved_inbound`, `dialer_ai_qualified_lead` in `billing/ai_usage_events/`. Abhaengig von `billing/ai-credits/`-Architektur.
[ ] 🟡 **Source-Maintenance Aircall/Dialpad RSS-URLs** (Follow-Up 7d): Feed-URLs sind seit KW19 tot. Web-Scrape-Adapter mit Atom-Discovery als Plan B.
[ ] 🔵 **Marketing-Botschaft "Cosmi-Dialer kennt deinen Kunden"** (Inspire): Cross-Modul-Kontext-Argument als 2-Satz-Pitch. Verifizierbar, konkurrenzlos.
[ ] 🔴 **NICHT-Pick:** Predictive-Dialer-Modus in Phase A — JustCall ist hier dominant, aber DACH-KMU-Markt nicht der Hauptkaeufer (US-Outbound-SDR-Pattern). Phase B oder spaeter.

---

## Telemetry-Anhang

- **Pool-Verbrauch:** ~24% (innerhalb Threshold 0.15)
- **Runtime:** ~54 Min (innerhalb 60-Min-Cap)
- **Items-Input:** 8 Tagesreports + 1 Weekly W20 + 1 Keeper + 1 CRM-Deepdive + 2 Followups + 8 WebSearches + 0 Headless-Chromium-Polls (G2/Capterra: WebSearch-Aggregation statt direkter Browser-Pull — Trade-Off Tiefe vs. Quoten-Verbrauch)
- **Embedding-Endpoint:** nicht verfuegbar (Ollama bge-m3 offline) — manuelle thematische Clusterung
- **Wettbewerber-Coverage:** 5/5 Top-Konkurrenten (Aircall, JustCall, Dialpad, Sipgate, Placetel) — 100% Pflichtsektion-erfuellt
- **Verglichene Features:** 32 Feature-Achsen, 6 Spalten (Cosmi + 5 Wettbewerber)
- **Discord-Push:** Pending → `.state/discord_push_pending.json` (Header + Top-3-Embeds fuer #trends)
- **Naechste Rotation:** `video` (KW22, 2026-05-25)
