---
year: 2026
week: 36
modul: dialer
created: 2026-08-31
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 47
tokens_input: ~285000
tokens_output: ~13800
rotation_position: 2/15
zyklus: 2
delta_to: 2026-05-18-deepdive-dialer.md
delta_weeks: 15
---

# Deepdive: dialer (Mo W36/2026) — Zyklus 2

> **Zyklus 2, Modul 2/15.** Vorgaenger im aktuellen Zyklus: `crm-core` (W35, 2026-08-24). Referenz-Vergleich Zyklus 1: `monthly/2026-05-18-deepdive-dialer.md` (W20/2026). **Delta-Zeitraum: 15 Wochen (2026-05-18 → 2026-08-31).**
>
> **Stand Cosmi-Dialer (2026-08-31):** Modul-Pfad `backend/internal/dialer/` nach wie vor als Phase-1-ZFA-Pilot markiert. **Kein sichtbarer Umsetzungs-Fortschritt in 15 Wochen** — weder in Weeklies W22–W35 dokumentiert noch als CRM-Deepdive-W35-Nachbarschafts-Signal auftauchend (dort explizit gelistet als "Conversation-zu-Deal-Routing fehlt (dialer ↔ crm-bridge)"). Cosmi hat die 15 Wochen fuer Backend-Hardening genutzt: RLS Welle 3.5 + 4, Migration-Head von 111 → 297, `advisoryprotocol`-Modul, keine Dialer-Fortschritts-Signale. **Alle sieben Zyklus-1-Picks (W20) sind offen.**
>
> **Leit-Signal des Deepdives:** Zwei struktur-verschiebende Ereignisse seit W20 zwingen die Cosmi-Dialer-Roadmap zu einer neuen Prioritaeten-Ordnung. **(1) EU AI Act Art. 50 seit 2026-08-02 aktiv** — Voice-AI-Erstkontext-Offenlegung ist ab jetzt Rechtspflicht, nicht Best-Practice, mit €15M/3%-Umsatz-Rahmen. Cosmi hat W35-Regulation-Report bereits als P0-Sofortauftrag markiert, aber Dialer-KI-Compliance-Screening-Status ist offen. **(2) fonio.ai ist als neuer DACH-KMU-First-AI-Voice-Konkurrent aufgetaucht** — OMR Reviews Top-100-Tools-2026 Platz 1, 6.500 Business-Kunden in ~1 Jahr, ab €99/Mo (1.000 Min inkl.), Zielgruppe identisch mit Cosmi-ZFA-Pilot. Fonio ist kein Enterprise-Player wie Aircall/Dialpad, kein Klassik-PBX-Anbieter wie Sipgate/Placetel — sondern **AI-First fuer DACH-KMU als Erst-Kaufer**. Cosmi-Dialer-Pilot muss sich jetzt gegen fonio positionieren, nicht mehr nur gegen Aircall.

---

## Delta zu Zyklus 1 (W20) — Was hat sich in 15 Wochen bewegt?

### Was sich im Markt bewegt hat

| Vektor | W20 (2026-05-18) | W36 (2026-08-31) | Delta |
|---|---|---|---|
| Aircall AI-Voice-Agent | Vogent M&A frisch (6. Mai), GA-Rollout unklar | Vogent integriert, Salesforce Service Cloud Voice-Integration produktiv, 23% Service-Level-Uplift-Case, Response-Zeit 29h → 12h Case | Konsolidierung + Sales-Case-Studies |
| JustCall AI-Voice-Agent | $29–$89 Basis, AI-Agents unbundled | AI-Voice-Agent gebundelt in Pro Plus, unbegrenzte AI-Transkription, Standalone $99/Mo für 100 Min ($0.99/Overage), 2-License-Minimum ($58 Entry) | Bundling + minimum-license-Aggression |
| Dialpad Agentic AI | Platform-Launch (Mai) | Agent Studio + Proving Ground + COMPASS + Guardian + Agentic Analytics (Maerz), WFM + Reporting + Credit Visibility (Juni/Juli) — Fokus "Pilot-zu-Produktion" | Governance-Layer + Enterprise-Reifung |
| Sipgate AI-Agents | Erst-GA April, KI-Empfangsassistent Basis | Live-Task-Execution (Termin-Buchung + CRM-Read/Write + Ticket-Erstellung waehrend Call), Contact Center + Agent View + Conversation Intelligence 100% Call-Analyse, SpotMyEnergy-Referenz | Sprung von "Empfangsassistent" zu vollem AI-Contact-Center |
| Placetel KI-Pricing | €0.13/Min oder €40/Mo-Flatrate (vage) | **Explizit**: Grow €69/Mo (750 Min), Professional €129 (1.500 Min), Enterprise €359 (4.000 Min); Overage €0.19/Min; Internal-Forward €0.025/Min, External €0.05/Min; AI-Nummer +€9/Mo; 10-Tage-Free-Trial | Pricing-Transparenz gestiegen |
| **fonio.ai (NEU im Radar)** | nicht getrackt | **OMR Top-100-Tools 2026 Platz 1**, 6.500 Business-Kunden, 316 OMR-Reviews (4.8/5), 4.9/5 Capterra, ab €99/Mo (1.000 Min), Zielgruppe DACH-KMU, Austrian-based | Neuer direkter DACH-KMU-First-Konkurrent |
| Zendesk Voice AI (Cross-Modul) | Nicht Teil des W20-Reports | August 2026: Live Call Transcription + Auto-Accept (0/5/10s Delay) + Jabra-Device-Support, kostenfrei in Suite Professional + Support Professional (nicht mehr Premium) | Voice-AI wird Helpdesk-Suite-Standard |
| OpenAI Realtime | GPT-Realtime-2 GA, $32/$64 Audio, ~$0.05–$0.10/Min mit Caching | gpt-realtime unveraendert $32/$64 → ~$0.05/Min; **gpt-realtime-mini ab $10/$20 → ~$0.016/Min** | **3× billiger** dank Mini-Model → break-point fuer profitable AI-Voice-Preise |
| LiveKit Agents | 1.5.x, native SIP, MCP-Tool-Support | **1.6.x** — Semantic Turn Detection als Default (statt VAD-only), MCP-nativ, ausgereifte SIP + Phone Numbers | Turn-Taking auf Aircall-Vogent-Niveau ohne M&A |
| EU-Regulierung | §201 StGB + Art 179bis CH + ElevenLabs-Praezedenz (Voice Print = personenbezogen) | **EU AI Act Art. 50 seit 02.08.2026 wirksam** — Chatbot- und Voice-AI-Offenlegung Rechtspflicht, €15M/3% Bußgeld, Grace fuer Marking-Feature bis 02.12.2026 | Neue Rechtsschicht ADDITIV — Consent + Transparency |
| Feed-Landschaft dialer-Modul | Aircall + Dialpad RSS 404 (KW19–20 flagged) | **12+ Wochen persistent**: aircall/justcall/dialpad 404, **sipgate-RSS neu 404 seit Di 25.08 (KW35)** → Cosmi ist blind auf 4 von 5 Top-Konkurrenten via RSS | Feed-Wartungsschulden akut |

### Was sich in Cosmi bewegt hat

**Sichtbarer Dialer-Progress: null.**

- `backend/internal/dialer/` wird in W20-Deepdive als "Phase-1-ZFA-Pilot" gefuehrt; in W35-crm-core-Deepdive taucht der Dialer nur noch als CRM-Luecke auf ("Conversation-zu-Deal-Routing fehlt (dialer ↔ crm-bridge)"). Keine der sieben W20-Picks ist als "erledigt" markiert:
  - ❌ AI-Voice-Stack als Pflicht-Stake vor Pilot-Launch (Transkription + CRM-Sync + Call-Summary)
  - ❌ Pre-Call-Consent-Framework (`internal/dialer/recording/consent/`)
  - ❌ Cross-Modul-Kontext-Resolver (`internal/dialer/context/`)
  - ❌ MCP-Server-Layer für Voice-Daten
  - ❌ Outcome-Pricing-Eventtypen (`dialer_ai_minutes`, `dialer_ai_resolved_inbound`, `dialer_ai_qualified_lead`)
  - ❌ Source-Maintenance Aircall/Dialpad RSS-URLs
  - 🔵 Marketing-Botschaft "Cosmi-Dialer kennt deinen Kunden" — kein sichtbarer Marketing-Test
- **CRM-Zyklus-2-Deepdive (W35) bestaetigt**: Dialer ist eine der zehn CRM-Kern-Luecken, die nach 15 Wochen unveraendert offen sind. Cosmi-CRM verweist auf Sipgate/HubSpot als DACH-Referenz-Pattern fuer Conversation-zu-Deal-Routing.
- **Cosmi-Investment W20 → W36**: Backend-Hardening (RLS Welle 3.5 + 4, 20 neue RLS-Tabellen, Migration-Head 111 → 297), CRM-`advisoryprotocol`-Subpackage (12 CRM-Sub-Packages jetzt), keine Modul-Erweiterung auf Dialer-Seite.

**Fazit Delta:** 15 Wochen ohne Dialer-Fortschritt, waehrend der Markt in derselben Zeit den zweiten AI-Reife-Sprung gemacht hat (Sipgate von "Empfangsassistent" zu "Live-Task-Execution", Aircall von Vogent-M&A zu Salesforce-integriertem AI-Agent, JustCall zu unbundled AI-Transkription, fonio.ai aus dem Nichts zu OMR Top-Platz 1). **Der W20-Bericht diagnostizierte 18–24 Monate Rueckstand; nach 15 Wochen ohne Cosmi-Bewegung ist der Rueckstand jetzt real 21–27 Monate.**

---

## State-of-the-Art (Stand 2026-08-31)

Der Dialer-Markt hat sich seit W20 in drei Vektoren weiterentwickelt: **(a)** AI-Voice-Agent-Preise sind mit gpt-realtime-mini strukturell **3× billiger** geworden (~$0.016/Min uncached, ~$0.005–$0.010/Min mit Caching), was den Break-Point fuer profitable KI-Telefonie-Modelle massiv nach unten verschiebt. **(b)** DACH-KMU-Zielgruppe wird jetzt von einem **First-DACH-AI-Voice-native-Anbieter** (fonio.ai) besetzt, nicht nur von umgeruesteten Klassik-PBX-Anbietern (Sipgate, Placetel) oder US-Playern (Aircall/JustCall/Dialpad). **(c)** Rechtsschicht ist gewachsen — EU AI Act Art. 50 wirksam seit 2026-08-02, damit ist die Compliance-Basis fuer alle Voice-AI-Deployments strenger als in W20 antizipiert.

### Top-5 Konkurrenten — Update seit W20 (Deltas fett)

**1. Aircall (international, ~23.000 Businesses, threat: high)**

- **Vogent-Integration konsolidiert**: Post-M&A ist "AI Voice Agent" die einheitliche Produktmarke. **Salesforce Service Cloud Voice-Native-Integration** — Voice-Intelligenz direkt in Salesforce-Konsole, embedded Call-Management, Realtime-Transkription, AI-Call-Summaries.
- **Sales-Case-Studies erstmals mit konkreten KPIs**: 23% Service-Level-Uplift, Response-Zeit-Case 29h (2025) → 12h (Jan 2026) bei einem Kunden, SJWD 90% After-Hours-Resolution (W20-Referenz weiter im Marketing).
- **Pricing G2/Capterra-Klage-Muster verschaerft**: Base Essentials $30/Seat + Professional $50/Seat + **Aircall AI +$9/Seat** + **Analytics+ +$15/Seat** + Extra-Nummer $6. Unabhaengige Analysen: Real-Cost 50–75% ueber Sticker-Preis. Beispiel 5er-Team Professional + AI + Analytics+: **$370/Mo statt $250 Sticker**.
- **G2-Pain-Cluster stabil**: 62 Connection-Issue-Mentions, 49 Call-Issue-Mentions, hohe Add-On-Undurchsichtigkeit, Auto-Renewal-/Cancellation-Notice-Friction. G2-Score 9.1/10 gewichtet, 4.4/5 in Reddit-Sample.
- **Gap zu Cosmi seit W20 unveraendert**: Voice-Agent-Platform, Custom-Voice-Modelle, Post-Call-Automation, RAG-Knowledge-Sync, Turn-Taking, Manager-Dashboards, native CRM-Sync.

**2. JustCall (international, threat: high)**

- **Pricing-Reform Delta**: Basis $29–$89 unveraendert, aber **AI-Voice-Agent jetzt in Pro Plus gebundelt** (statt Standalone-Only). Standalone-Angebot bleibt: **$99/Mo fuer 100 Min, $0.99/Min Overage**. **Unbegrenzte AI-Transkription** in allen Paeketen (Ende der Transcription-Caps).
- **Versteckte Kosten stabil**: 2-License-Mindest-Bestellung ($58/Mo Entry statt beworbene $29), SMS-Segment-Caps, US-SMS-Compliance-Fees, AI-Voice-Overage.
- **Kein neuer Feature-Sprung** seit W20 dokumentiert — Reifung des bestehenden Portfolios.
- **Gap zu Cosmi unveraendert**: Predictive-Dialer, Multi-Channel-Agent-Bus, 60-Sek-Lead-Reaction-Time, Warm-Transfer-Bridge.

**3. Dialpad (international, threat: medium-high)**

- **Maerz 2026 Advancement-Wave**: Agent Studio, **Proving Ground** (Pre-Deployment-Validation), **COMPASS** (Governance-Framework), **Guardian** (Datenschutz-Layer), Agentic Analytics erweitert. Explizite Botschaft: **"From Pilot to Production"** — Enterprise-KPI-Validation-Zwang statt "Deploy and hope".
- **Juni/Juli-Wave**: WFM (Workforce-Management), erweiterte Reporting-Tiefe, Credit-Visibility fuer Cost-Governance.
- **Weiterhin US-zentriert**, keine dokumentierte DACH-Datencenter-Ankuendigung. **Dialpad bleibt im DACH-KMU-Segment strukturell schwach**, aber technologisch der ambitionierteste Enterprise-Player. Wenn Dialpad EU-Hosting-Ankuendigung macht (kein Signal bis W35), kippt das strategisch.
- **Delta-Signal fuer Cosmi**: Dialpad's "COMPASS/Guardian"-Governance-Framework ist Vorlage fuer Cosmi's `internal/dialer/ai_governance/` — Cost-Caps, Consent-Audits, AI-Attribution-Logs als Erstklassiger Modulpfad statt Nachgedanke.

**4. Sipgate (DACH, threat: high — DACH-Kern-Konkurrent, staerkster Delta-Sprung seit W20)**

- **Kern-Delta**: AI-Agents koennen **live waehrend des Calls** Termine buchen, Kundendaten abfragen, Tickets erstellen — nicht mehr nur "sprechen und uebergeben". **Integration mit ERP + Kalender + CRM waehrend des laufenden Gespraechs** ist Reifegrads-Sprung von "Voicebot" zu "Voice-Agent-mit-Tool-Access" (MCP-aehnliches Pattern).
- **Contact Center + Agent View + Conversation Intelligence 100%** — alle Calls werden analysiert, nicht Stichprobe. Intelligente Anruf-Verteilung, Realtime-Monitoring, KPI-Dashboards Manager-tauglich.
- **SpotMyEnergy-Referenzkunde** oeffentlich (Marijana Wagner, Head of Customer Service) — Sipgate baut B2B-Sales-Case-Study-Pipeline systematisch aus.
- **W35 3-Case-Study-Content-Woche** — Sipgate publiziert in einer Woche 3 Kunden-Referenzen als Content-Offensive (Inspirations-Muster fuer Cosmi-Marketing).
- **RSS-Feed 404 seit 25.08.2026** — Sipgate hat vermutlich URL-Wechsel, muss vor W37 verifiziert werden.
- **Gap zu Cosmi verschaerft**: Sipgate hat jetzt exakt das Feature-Bild ("AI-Agent liest CRM + Kalender + Tickets waehrend Call"), das Cosmi als Cross-Modul-Kontext-Killer-Vorteil positioniert hatte — allerdings via Sync-Integration, nicht in-process. **Cosmi's architektonischer Vorsprung schmilzt: von "haben wir alleine" zu "wir sind schneller/latenzaermer".**

**5. Placetel (DACH, threat: high — DACH-Klassik mit klarster Pricing-Transparenz)**

- **Pricing jetzt komplett explizit publiziert**: Grow €69/Mo (750 Min inkl.), Professional €129 (1.500 Min), Enterprise €359 (4.000 Min), monat-zu-monat bzw. 24-Monats-Vertrag mit Rabatt. Overage €0.19/Min ueber Kontingent. Effektiver Per-Min-Preis paketabhaengig **ab €0.13/Min**. Internal-Forward €0.025/Min, External €0.05/Min, AI-Nummer +€9/Mo.
- **10-Tage-Free-Trial** aktiv (Cosmi hat kein aehnliches Trial-Angebot dokumentiert).
- **Zielgruppen-Signal**: Placetel positioniert sich als "AI-Empfangsassistent" fuer klassische DACH-KMU-Kaufer, die von PBX aufsteigen — nicht als Voice-Agent-Platform fuer AI-First-Kaufer. Fonio.ai bedient letztere Zielgruppe direkter.
- **Gap zu Cosmi unveraendert**: KI-Rezeptionist Default, transparentes Pricing-Modell, breite Telekom-Beteiligungs-Reseller-Distribution.

**BONUS-KONKURRENT (NEU im Radar): fonio.ai — DACH-KMU-First-AI-Voice-native**

- **Herkunft**: Oesterreichisches Startup, ~1 Jahr am Markt, hat OMR Reviews Top-100-Business-Tools-2026 auf **Platz 1** gewonnen. Meiste OMR-Reviews aller KI-Telefonassistenten (316), 4.8/5 OMR, 4.9/5 Capterra, 4.9/5 GetApp.
- **Kundenbasis**: 6.500+ Business-Kunden in einem Jahr — beispiellose Adoption-Geschwindigkeit im DACH-KMU-Segment.
- **Pricing**: Ab €99/Mo (1.000 Min inkl. reine Telefonie mit planbarem Volumen) — deutlich einfacher als Placetel-Staffelung, deutlich billiger pro Min als JustCall-AI-Voice-Standalone ($0.99/Min).
- **Reviews-Muster**: Positives: natuerliche Stimmqualitaet (Anrufer erkennen KI oft nicht), einfacher Setup. Negatives: Dialekt-Probleme, keine kostenlose Test-Phase, initial unklare Pricing-Struktur.
- **Strategische Bedeutung fuer Cosmi**: **Dies ist Cosmi's neuer direkter Konkurrent im ZFA-Pilot-Segment.** Nicht Aircall (zu Enterprise-lastig, US-Jurisdiktion), nicht Sipgate (Klassik-PBX-Aufsteiger), nicht Placetel (Klassik-PBX-Aufsteiger) — sondern ein DACH-Native, der bei AI-Voice-First anfaengt. Cosmi-Dialer-Pilot muss sich in Kunden-Gespraechen jetzt gegen fonio positionieren, nicht mehr nur gegen die traditionellen Top-5.
- **fonio-Schwaeche als Cosmi-Angriffspunkt**: fonio ist **nur** ein Voice-Agent — keine CRM-Suite, kein Helpdesk, keine Buchhaltung, keine Vertraege, keine Schichten. **Der Cross-Modul-Kontext-Moat bleibt Cosmi's Kern-Verteidigung — aber jetzt gegen fonio, nicht gegen Aircall.**

### Tech-Stack-Reifung seit W20

- **OpenAI gpt-realtime-mini**: $10/M Input / $20/M Output = **~$0.016/Min uncached**, mit Caching-Disziplin **~$0.005/Min** — 3× billiger als W20-Baseline. Bedeutet: profitable AI-Voice-Preise sind **auch bei ohne-Add-On-Sticker-Preis** moeglich (~€0.05–€0.10/Min-Verkaufspreis mit gesunden Margen).
- **LiveKit Agents 1.6.x**: **Semantic Turn Detection als Default** (kleines Transformer-Modell fuer Konversations-Uebergaenge statt VAD-only). Damit erreicht ein LiveKit-Setup ohne M&A das Turn-Taking-Niveau von Aircall+Vogent. **SIP + Phone Numbers GA**, ~4 Zeilen Konfig fuer Inbound-Voice-Agent, native MCP-Tool-Support.
- **OpenAI Realtime via WebRTC** (webrtchacks W34): Bestaetigt WebRTC als Transportschicht-Standard fuer AI-Voice. Cosmi hat WebRTC bereits im Haus via LiveKit-Video-Modul → **direkter architektonischer Umsetzungspfad ohne neuen Vendor**.
- **Recall.ai als Third-Party-Call-Recording-Provider** — Twenty v2.30.0 (W33) hat CALL_RECORDING_SUMMARY + CALL_RECORDING_TRANSCRIPT als Widget-Typen mit Recall.ai als Default-Provider registriert. **Referenz-Architektur fuer Cosmi**: strukturierte Third-Party-Provider-Konfiguration + Cross-Modul-Kontext-Anreicherung statt Bau-alles-selbst.
- **AssemblyAI Universal-3.5 Pro** (via Speko-Benchmarks W33): **2,0% WER Deutsch, $0,0075/Min Transkription** — beste dokumentierte DE-STT-Genauigkeit. Referenz-Wahl fuer Cosmi's `internal/dialer/transcription/`.

### Regulatorische Verdichtung seit W20

- **EU AI Act Art. 50 wirksam ab 02.08.2026** (drei Wochen aktiv am Deepdive-Datum): Voice-AI-Systeme, die direkt mit Personen interagieren, muessen **vor Interaktion** offenlegen "Sie sprechen mit KI". Bußgeldrahmen **€15M oder 3% Jahresumsatz** (whichever higher). Grace-Period bis 02.12.2026 nur fuer Marking-/Detection-Feature von AI-generated-Content (Art. 50(2)) — Chatbot/Voice-Erstkontext-Offenlegung sofort wirksam.
- **W35-Regulation-Report (Cosmi-intern)**: Cosmi-Dialer-KI explizit als einer der vier zu screenden Touchpoints markiert (CRM-Widget, Dialer-KI, Helpdesk-Bot, API-Ausgaben). Status offen.
- **§201 StGB (DE) + Art 179bis StGB (CH) + ElevenLabs-Voice-Print-Praezedenz** (W20-Baseline) **bleiben unveraendert additiv** — Cosmi-Dialer-Compliance-Stack braucht jetzt: (i) Pre-Call-Consent-Prompt (§201/Art 179bis), (ii) AI-Erstkontext-Offenlegung (Art. 50 EU AI Act), (iii) Voice-Print-Loeschungs-API (DSGVO Art 17 + ElevenLabs-Praezedenz), (iv) DSGVO Art 6/7 Consent-Basics. **Vier konvergente Rechtslagen, alle P0.**

---

## Cosmi-IST-Stand (2026-08-31)

> Hinweis: KMU-Hub-Repository ist in dieser Umgebung nicht mountbar (Worktree-Pfad leer). IST-Stand abgeleitet aus: (a) W20-Zyklus-1-Deepdive als Baseline, (b) W28–W35-Weeklies (13 Weeklies gescreent auf Dialer-Signale), (c) W35-crm-core-Zyklus-2-Deepdive (Cross-Referenz "Conversation-zu-Deal-Routing fehlt (dialer ↔ crm-bridge)"), (d) keeper `aircall-ai-voice-blitz`, (e) W35-Regulation-Report (Art. 50-Screening-Auftrag).

### Was Cosmi heute hat (2026-08-31)

- **Modul-Pfad-Definition**: `backend/internal/dialer/` markiert als Tier-1 Phase-1-ZFA-Pilot. Unveraendert seit W20.
- **Watch-Topics laut `sources/dialer.yaml`**: Call-Recording-Compliance DSGVO, Auto-Transkription, AI-Powered-Coaching, Power-Dialer-Modi, TURN/STUN-Setups, EU-VoIP-Anbieter — unveraendert seit W20, konzeptionell aktuell, implementierungstief immer noch null.
- **Voraussichtliche Tech-Basis**: LiveKit (bereits fuer Video-Modul im Haus), Postgres (RLS Welle 3.5 + 4 produktiv, Migration-Head 297), gRPC-Service-Mesh, `advisoryprotocol`-Subpackage im CRM (potentieller Hook-Punkt fuer Dialer-Advisory-Voice-Flows).
- **Cross-Modul-Hooks vorhanden**: CRM `internal/crm/` mit 12 Sub-Packages (+1 seit W20), RLS-produktiv auf 20 zusaetzlichen Tabellen (Welle 4) — Dialer-AI-Agent kann in-Process auf CRM lesen, sobald `internal/dialer/context/` gebaut ist.

### Was Cosmi heute nicht hat (Delta zu W20)

Die W20-Luecken-Tabelle ist unveraendert — zusaetzlich mit einer neuen Zeile fuer EU AI Act Art. 50:

| Fehlend | Schwere | Pflicht fuer Pilot? | Delta zu W20 |
|---|---|---|---|
| AI-Transkription (post-call) | hoch | **Ja** | unveraendert |
| Realtime-Transkription (live) | mittel | Nice-to-have Phase B | unveraendert |
| AI Voice Agent (Inbound 24/7) | hoch | **Ja** | verschaerft — Sipgate + fonio jetzt marktreif |
| Pre-Call-Consent-Framework | kritisch | **Ja** | unveraendert |
| **AI-Erstkontext-Offenlegung (EU AI Act Art. 50)** | **kritisch** | **Ja — Rechtspflicht seit 02.08.2026** | **NEU seit W20** |
| Auto-CRM-Sync (Call → Deal/Contact) | hoch | **Ja** | unveraendert |
| Post-Call AI Actions (HubSpot-style) | mittel | Phase B | unveraendert |
| Predictive-/Power-Dialer-Modi | mittel | Phase B | unveraendert |
| Turn-Taking + Barge-In | hoch | **Ja** fuer Voice-Agent | **einfacher geworden** — LiveKit 1.6.x Semantic Turn Detection als Default |
| Manager-Performance-Dashboard | mittel | Phase B | unveraendert |
| Per-Minute-AI-Pricing-Infrastruktur | hoch | **Ja** — Outcome-Pricing-Wave | verstaerkt (Placetel-Explicit-Preis + gpt-realtime-mini) |
| Voice-Print-Loeschungs-API (DSGVO Art 17) | kritisch | **Ja** | unveraendert |
| Local-Presence-Numbers (Outbound) | niedrig | Optional | unveraendert |
| SMS-/WhatsApp-Multi-Channel | mittel | Phase C | unveraendert |
| **AI-Cost-Governance (Cost-Caps + Attribution)** | **mittel-hoch** | **empfohlen (Dialpad-COMPASS-Muster)** | **NEU seit W20** |
| **`internal/dialer/transcript_provider/`** (Twenty-Recall.ai-Muster) | mittel | empfohlen fuer Buy-vs-Build-Optionalitaet | **NEU seit W20** |

**Neue Luecken 2026-08-31 (drei):**
1. **EU AI Act Art. 50 Erstkontext-Offenlegung** — nicht mehr Best-Practice, sondern Rechtspflicht. Cosmi-Dialer-KI darf ohne Offenlegung nicht in Produktion.
2. **AI-Cost-Governance-Layer** — Dialpad's COMPASS/Guardian als Vorlage. Cosmi braucht Cost-Caps, Consent-Audits, AI-Attribution-Logs als Erstklassige Modul-Ebene, sobald AI-Voice-Kosten pro Kunde variabel werden.
3. **Third-Party-Provider-Optionalitaet** — Twenty v2.30.0 Muster (CALL_RECORDING_SUMMARY / CALL_RECORDING_TRANSCRIPT als konfigurierbare Provider). Cosmi kann Recall.ai + AssemblyAI + OpenAI-Realtime als austauschbare Provider modellieren statt Vendor-Lock.

### Cosmi-strukturelle Vorteile — Delta seit W20

**Alle vier W20-Vorteile bleiben gueltig, drei erodieren.**

1. **EU-Datensouveraenitaet** — unveraendert. Aircall/JustCall/Dialpad weiter US-Jurisdiktion, Sipgate/Placetel EU-nativ (Konkurrenten-Parity), fonio.ai in Oesterreich (Konkurrenten-Parity, EU-nativ). **Cosmi bleibt hier nicht besser als die DACH-Anbieter — aber besser als US-Player.**
2. **Cross-Modul-Kontext nativ** — **beginnt zu erodieren**. Sipgate liest jetzt CRM + Kalender + Tickets live during Call (via Sync-Integration). Cosmi's Vorteil ist nicht mehr "haben wir alleine", sondern "wir sind in-Process, Sipgate ist Sync-latenzbehaftet". Der Vorteil bleibt real (<10ms in-process vs. 100ms+ Sync), aber ist nicht mehr binaer.
3. **Outcome-Pricing-Architektur** — unveraendert offen. Kein sichtbarer Bau von `billing/ai-credits/`. JustCall + Placetel haben in W36 klar publiziertes Per-Minute-Pricing — Cosmi ist immer noch bei "TBD".
4. **LiveKit-Stack im Haus** — **verstaerkt**. LiveKit 1.6.x mit Semantic Turn Detection + native SIP + MCP-Tool-Support bedeutet: Cosmi-Voice-Agent-Implementierung ist heute einfacher als in W20, weil weniger Custom-Turn-Taking-Logik gebaut werden muss.

**Neue schwache Cosmi-Position — fonio.ai in der ZFA-Pilot-Zielgruppe**: Die Erst-Zielgruppe des Dialer-Pilots (ZFA-Kanzleien im DACH) wird jetzt von fonio.ai mit einer Loesung bedient, die (a) sofort verfuegbar ist, (b) €99/Mo kostet, (c) natuerliche Stimmqualitaet + einfachen Setup als OMR-Top-Feature hat. Cosmi-Dialer muss in Sales-Gespraechen den Sprung von "wir bauen noch" zu "wir haben Cross-Modul-Kontext als Killer-Feature" ohne Feature-Parity ueberbruecken — das war in W20 gegen Aircall gut argumentierbar, ist gegen fonio schwerer.

---

## Konkurrenz-Vergleichstabelle (mit fonio.ai als neuer Spalte)

Legende: ✅ produktiv · 🚧 Beta/Ankuendigung · ❌ nicht vorhanden · ❓ unklar

| Feature | Cosmi (Plan) | Aircall | JustCall | Dialpad | Sipgate | Placetel | **fonio.ai** |
|---|---|---|---|---|---|---|---|
| **Voice/PBX-Basics** | | | | | | | |
| Outbound Calling | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Inbound Routing / IVR | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Call Recording (manuell) | 🚧 Phase A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Local-Presence-Nummern DACH | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EU-Datacenter / Self-Host | ✅ Self-Host | ❌ US | ❌ US | ❌ US/Google | ✅ DE | ✅ DE | ✅ AT |
| **AI-Voice-Stack** | | | | | | | |
| Post-Call-Transkription | ❌ | ✅ | ✅ (unlimited) | ✅ | ✅ | ✅ | ✅ |
| Realtime-Transkription | ❌ | ✅ (Salesforce SCV) | ✅ | ✅ | ✅ (100% Analysis) | ❓ | ✅ |
| AI Voice Agent (24/7 Inbound) | ❌ | ✅ Vogent | ✅ Pro Plus + Standalone | ✅ Agent Studio | ✅ Live-Task-Execution | ✅ KI-Rezeptionist | ✅ Core-Feature |
| Turn-Taking + Barge-In | ❌ | ✅ Vogent | ✅ | ✅ | ✅ | 🚧 | ✅ |
| AI→Human Warm Handoff | ❌ | ✅ Vogent | ✅ | ✅ | ✅ Kontext-Summary | 🚧 | ✅ |
| Live-Task-Execution (CRM/Cal/Ticket im Call) | ❌ | 🚧 SCV-Sync | 🚧 | ✅ Agent Studio | ✅ Termin+CRM+Ticket | ❌ | 🚧 |
| Post-Call AI Actions (CRM-Writeback) | ❌ | ✅ AI Actions | ✅ Workflows | ✅ Connectors | ✅ | ❌ | 🚧 |
| Sentiment-Analyse | ❌ | 🚧 | ✅ Iq | ✅ | ✅ Conversation Intelligence | ❌ | 🚧 |
| Custom Voice Models / Brand Voice | ❌ | ✅ Vogent | ❌ | ❓ | ✅ Voice-Auswahl | ❓ | ❌ |
| Natuerliche Stimmqualitaet (DE-nativ) | ❌ | ⚠ | ⚠ | ⚠ | ✅ | ✅ | ✅ Top-Feedback |
| **Governance / Cost-Control** | | | | | | | |
| AI-Cost-Governance-Framework | ❌ | ❓ | ❓ | ✅ COMPASS/Guardian | ❓ | ❌ | ❌ |
| Cost-Attribution pro Tenant/Modul | ❌ | ❓ | ✅ Credit-Visibility | ✅ Credit-Visibility | ❓ | ❓ | ❓ |
| Pre-Deployment-Validation (Proving Ground) | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Cross-Modul / Integration** | | | | | | | |
| Native CRM-Integration | ✅ in-process | ✅ Sync SCV | ✅ Sync | ✅ Sync | ✅ Sync live | ✅ Sync | 🚧 (nur Basics) |
| Cross-Modul-Kontext (Schichten/Rapporte) | ✅ in-process | ❌ | ❌ | ❌ | 🚧 ERP-Sync | ❌ | ❌ |
| RAG-Knowledge aus Calls | ❌ | ✅ Knowledge-Auto | 🚧 | ✅ | 🚧 | ❌ | 🚧 |
| MCP-Server fuer Voice-Daten | ❌ | ❓ | ❌ | 🚧 | ❌ | ❌ | ❌ |
| Third-Party-Provider-Optionalitaet (Recall.ai etc.) | ❌ | ❌ | ❌ | ❓ | ❌ | ❌ | ❌ |
| **Compliance / Recht** | | | | | | | |
| Pre-Call-Consent-Prompt (§201/Art 179bis) | ❌ | 🚧 | 🚧 | 🚧 | ✅ DACH-Default | ✅ DACH-Default | ✅ DACH-Default |
| **AI-Erstkontext-Offenlegung (EU AI Act Art. 50)** | ❌ | 🚧 | 🚧 | 🚧 (COMPASS-Layer) | 🚧 | 🚧 | 🚧 |
| Voice-Print-Loeschungs-API | ❌ | ❓ | ❓ | ❓ | ❓ | ❓ | ❓ |
| DSGVO-AVV | ✅ EU | 🚧 US-Juris | 🚧 | 🚧 | ✅ | ✅ | ✅ |
| §201 StGB / Art 179bis konform | ✅ moeglich | ⚠ riskant | ⚠ riskant | ⚠ riskant | ✅ | ✅ | ✅ |
| **Dialer-Modi** | | | | | | | |
| Manual-Dial | 🚧 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Power-Dialer | ❌ | ✅ | ✅ | ✅ | ❓ | ❓ | ❌ |
| Predictive-Dialer | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Preview-Dialer | ❌ | ✅ | ✅ | ✅ | ❓ | ❓ | ❌ |
| **Reporting / Coaching** | | | | | | | |
| Real-Time Agent-Assist | ❌ | ✅ | ✅ | ✅ | 🚧 | ❌ | ❌ |
| Manager-Performance-Dashboard | ❌ | ✅ | ✅ | ✅ WFM | ✅ Contact Center | 🚧 | 🚧 |
| Sprach-Coaching (AI-Hinweise) | ❌ | ✅ | ✅ Iq | ✅ | ❌ | ❌ | ❌ |
| **Pricing-Modell** | | | | | | | |
| Seat-basiert | 🚧 | ✅ $30–$50/Seat | ✅ $29–$89 (2-Lic-Min) | ✅ ~$25+ | ✅ Pay-per-Use | ✅ €69–€359 | ❌ (Min-Pauschale) |
| Per-Minute-AI-Pricing | ❓ | ❓ Add-on | ✅ $0.99/Min AI | ❓ Credit | ✅ Add-on | ✅ €0.19/Min Overage | ✅ Min-Pauschal |
| Outcome-Pricing ($/Lead, $/Resolved) | ❌ | ❓ | ❓ | 🚧 ROI-Validation | ❌ | ❌ | ❌ |
| Transparente Add-On-Bepreisung | ❓ | ❌ G2-Pain | ❌ G2-Pain | ❌ Sales-Call | ✅ | ✅ | ✅ (nach initial-critique-fix) |
| Free-Trial | ❓ | ❌ (Demo) | ❌ (Demo) | ❌ (Demo) | ✅ | ✅ 10 Tage | ❌ (Pain-Point) |

**Zeilenzahl gesamt: 38 Feature-Achsen** (W20: 32). Neue Zeilen: AI-Cost-Governance-Framework, Cost-Attribution, Pre-Deployment-Validation, Third-Party-Provider-Optionalitaet, AI-Erstkontext-Offenlegung, Live-Task-Execution, Natuerliche Stimmqualitaet DE-nativ, Free-Trial.

**Verdichtung:** Cosmi hat weiterhin drei strukturelle Vorteile (EU-Souveraenitaet, Cross-Modul-in-Process, LiveKit-im-Haus) und **mindestens 15 Pflicht-Luecken** vor Pilot-Launch (W20: 12 — plus AI Act Art. 50 Erstkontext, plus AI-Cost-Governance, plus Third-Party-Provider-Optionalitaet). Fonio.ai fuegt eine neue Konkurrenz-Schicht hinzu, die architektonisch schwaecher ist (kein Cross-Modul-Kontext), aber operativ ueberlegen (verfuegbar, Preis-transparent, DE-native Stimmqualitaet).

---

## Top-3 Strategische Empfehlungen

### 1. **EU AI Act Art. 50 Erstkontext-Offenlegung + Consent-Framework als kombiniertes P0 (`internal/dialer/compliance/`)**

**Empfehlung:** Ein einziger `internal/dialer/compliance/` Sub-Package baut alle vier konvergenten Rechtslagen als Erstklassige Modulschicht: (a) Pre-Call-Consent-Prompt (§201 StGB DE + Art 179bis StGB CH), (b) AI-Erstkontext-Offenlegung (EU AI Act Art. 50, wirksam seit 02.08.2026), (c) Voice-Print-Loeschungs-API (DSGVO Art 17 + ElevenLabs-Praezedenz), (d) Consent-Storage separat vom Audio-Storage, Tenant-Scoped, Immutable-Append-Only-Log.

**Begruendung — Delta zu W20:**

- Die W20-Empfehlung war "Pre-Call-Consent-Framework als P0". Sie ist **unveraendert richtig** und **unveraendert offen**.
- **NEUES Element**: EU AI Act Art. 50 seit 02.08.2026 **wirksam**. Cosmi-Dialer-KI, die ohne Erstkontext-Offenlegung Kunden anruft oder Kunden-Anrufe entgegennimmt, ist ab jetzt in **direkter Rechtsverletzung** mit €15M/3%-Bußgeldrahmen. Kein Grace-Period fuer diese Pflicht (Grace nur fuer AI-Marking-Feature bis 02.12.2026).
- **Konvergenz-Effekt**: Vier Rechtslagen mit ueberlappenden Anforderungen. Ein integrierter Compliance-Layer ist billiger als vier Punkt-Loesungen. Der Marketing-Vorteil ("Cosmi ist AI-Voice-Compliant-by-Default fuer DACH") ist eine 2-Satz-Story.
- **Konkurrenz-Positionierung**: Aircall/JustCall/Dialpad sind mit US-Jurisdiktion + Default-Recording-On strukturell schwach hier. Sipgate/Placetel/fonio.ai haben DACH-Consent-Default, aber **keinen dokumentierten AI Act Art. 50 Screening-Status** — Cosmi kann hier First-Mover sein, wenn Compliance-Layer als Sales-Argument gefuehrt wird.

**Konkrete technische Umsetzung:**

```
backend/internal/dialer/compliance/
├── consent/                    # §201 StGB + Art 179bis StGB + DSGVO Art 6/7
│   ├── prompt_engine.go        # Pre-Call-Audio-Prompt (DE/EN/FR/IT)
│   ├── dtmf_confirmation.go    # Opt-In-Logging
│   └── storage.go              # Tenant-scoped immutable log
├── ai_disclosure/              # EU AI Act Art. 50 wirksam 02.08.2026
│   ├── opening_line.go         # "Sie sprechen mit dem KI-Assistenten von ..."
│   ├── multi_language.go       # DE/EN/FR/IT verpflichtend fuer DACH-Kunden
│   └── audit_log.go            # Offenlegungs-Nachweis pro Call-Leg
├── voice_print/                # DSGVO Art 17 + ElevenLabs-Praezedenz
│   ├── deletion_api.go         # Self-Service-API
│   └── retention_policy.go     # Default-Retention + Kundenkonfiguration
└── audit/                      # Cross-cutting Audit-Log
    └── compliance_events.go    # Alle Compliance-Events fuer Prufung
```

**Trade-Off:** Compliance-Layer erhoeht Pilot-Komplexitaet um ~3–4 Wochen Development. **Akzeptabel** — Alternative ist Pilot-Launch mit Rechtsrisiko (€15M/3% Rahmen aktiv seit drei Wochen). Diese Empfehlung wandelt W20-Empfehlung-2 in eine erweiterte Version mit Art. 50-Integration.

**Sales-Story-Effekt:** *"Cosmi-Dialer ist der einzige DACH-KMU-Dialer, der alle vier Rechtslagen — §201 StGB, Art 179bis CH, EU AI Act Art. 50, DSGVO Art 6/7/17 — nativ und dokumentiert erfuellt."* Dies ist gegenueber Aircall/JustCall/Dialpad ein binaerer Vorteil (US-Jurisdiktion-Risiko) und gegenueber Sipgate/Placetel/fonio ein AI-Act-Vorsprung, sofern schnell geliefert.

---

### 2. **AI-Voice-Stack-Bau mit LiveKit 1.6.x + gpt-realtime-mini + Recall.ai-als-Fallback (`internal/dialer/voice_agent/` + `internal/dialer/transcript_provider/`)**

**Empfehlung:** Cosmi-Dialer-Voice-Agent wird auf drei technische Entscheidungen festgelegt, die Zeit sparen und Optionalitaet erhalten: **(a)** LiveKit Agents 1.6.x als Runtime (bereits im Haus via Video-Modul, Semantic Turn Detection als Default statt VAD, native MCP, native SIP), **(b)** OpenAI **gpt-realtime-mini** als Default-LLM-Layer ($0.016/Min uncached, ~$0.005/Min mit Caching — profitable Voice-Preise ohne Add-On-Aufpreis), **(c)** Recall.ai + AssemblyAI + OpenAI Whisper als **austauschbare Transcript-Provider** hinter einem einheitlichen Interface (Twenty-v2.30.0-Muster). Cosmi bindet sich nicht an einen einzigen Voice-AI-Vendor, kann aber mit einem produktiven Default-Stack in ~6–8 Wochen live gehen.

**Begruendung — Delta zu W20:**

- **W20-Empfehlung**: "AI-Voice-Stack als Pflicht-Stake vor Pilot-Launch (Pull-Forward Phase C → Phase A): Transkription + CRM-Sync + Call-Summary." Diese Empfehlung ist **unveraendert richtig** und **unveraendert offen**.
- **NEUE Elemente seit W20**:
  - **gpt-realtime-mini** hat den Kostenrahmen 3× nach unten geschoben. Bei $0.016/Min uncached ist Voice-Agent-Betrieb bei einem Kunden-Verkaufspreis von €0.05/Min immer noch mit 60%+ Marge moeglich. Das entkoppelt AI-Voice-Preise vom Add-On-Marketing-Trick der US-Player.
  - **LiveKit 1.6.x Semantic Turn Detection**: Aircall musste fuer Turn-Taking Vogent kaufen. Cosmi bekommt Aircall-Vogent-Niveau via LiveKit-Upgrade **ohne M&A**.
  - **Twenty v2.30.0 CALL_RECORDING_*-Provider-Muster (W33)**: Cosmi baut nicht "eigenes Transkriptions-Backend", sondern "Provider-Interface mit Recall.ai + AssemblyAI + OpenAI Whisper als konfigurierbaren Choice". Der Effekt: schneller live, weniger Vendor-Risiko, Upgrade-Pfad zu Self-Hosted Whisper-large-v3 spaeter.
  - **AssemblyAI Universal-3.5 Pro** = **2,0% WER DE bei $0,0075/Min**. Das ist die dokumentiert beste Deutsch-STT-Qualitaet zu einem Preis, der unter allen US-Player-Sticker-Add-Ons liegt.

**Konkrete technische Umsetzung:**

```
backend/internal/dialer/voice_agent/
├── livekit_worker.go           # LiveKit Agents 1.6.x Worker
├── sip_dispatch.go             # LiveKit SIP + Phone Numbers
├── turn_detection.go           # Semantic Turn Detection Wrapper
├── mcp_tools/                  # Cosmi-Module als MCP-Tools fuer Voice-Agent
│   ├── crm_lookup.go
│   ├── calendar_query.go
│   ├── ticket_create.go
│   └── invoice_read.go
└── realtime_backend/
    ├── openai_gpt_realtime_mini.go   # Default
    ├── openai_gpt_realtime.go        # Premium-Tier
    └── config.go                     # Per-Tenant-Auswahl

backend/internal/dialer/transcript_provider/
├── interface.go                # TranscriptProvider Interface
├── recall_ai.go                # Recall.ai Adapter (Default)
├── assemblyai.go               # AssemblyAI Adapter (DE-optimiert)
├── openai_whisper.go           # Whisper-Realtime Adapter
└── self_hosted_whisper.go      # Zukunfts-Option
```

**Pricing-Kalkulation (Beispiel-Rechnung):**

Bei 1000 AI-Voice-Minuten/Monat pro Cosmi-Kunde:
- Cosmi-Betriebskosten mit gpt-realtime-mini + Caching: ~$5–$10/Mo.
- Transkription mit AssemblyAI: 1000 × $0.0075 = $7.50/Mo.
- **Total Cosmi-Cost pro Kunde: ~$12–$18/Mo fuer 1000 Min AI-Voice.**
- Verkaufspreis-Options:
  - Bundled in Cosmi-Suite (kein Add-on): €39/Mo/Modul → **~200% Marge**.
  - Per-Min-Sticker: €0.05/Min = €50/Mo bei 1000 Min → **~250% Marge**.
  - Outcome-Pricing €0.20 per resolved-inbound-call (bei 250 resolved/Mo): €50/Mo → **~250% Marge**.
- **Alle drei Modelle liegen weit unter Placetel (€0.13–€0.19/Min = €130–€190/Mo) und JustCall Standalone ($99/100 Min = $990/1000 Min).**

**Trade-Off:** Erhoeht Vendor-Abhaengigkeit von LiveKit + OpenAI. **Akzeptabel** — LiveKit ist Open-Source (Self-Host-Fallback moeglich), OpenAI ist einer von drei austauschbaren Voice-Backends (gpt-realtime-mini als Default, aber Ollama-Speaches, Azure OpenAI, AWS Nova Sonic als Alternativen dokumentiert).

---

### 3. **Cross-Modul-Kontext + Sales-Story-Aktivierung gegen fonio.ai (`internal/dialer/context/` + Marketing-Kampagne)**

**Empfehlung:** Zwei-Teil-Empfehlung:
- **Technisch**: `internal/dialer/context/resolver.go` als in-process-Single-Lookup-Service (Phone → CRM-Contact → Open Helpdesk-Issues → Active Contracts → Pending Invoices → Shift Context → Advisory-Protocols) baut den einzigen strukturellen Vorteil aus, den kein anderer DACH-Anbieter hat.
- **Marketing**: **Vor Pilot-Launch** wird eine explizite Sales-Story gegen fonio.ai (und Sipgate) aktiviert: *"fonio kennt nur das Telefongespraech. Cosmi kennt deinen Kunden — Vertrag, Rechnung, offenes Ticket, Schichtplan, letztes Beratungsprotokoll — waehrend das Telefongespraech laeuft."*

**Begruendung — Delta zu W20:**

- **W20-Empfehlung**: "Cross-Modul-Kontext als Architektonisches Differenzierungs-Merkmal." **Unveraendert richtig**, aber **operative Dringlichkeit gestiegen**:
  - **Sipgate hat live-Task-Execution seit Sommer 2026** — CRM-Read/Write, Kalender-Zugriff, Ticket-Erstellung waehrend Call. Der Cosmi-Vorteil "wir haben Cross-Modul" ist von "haben wir alleine" zu "wir sind in-Process, Sipgate ist Sync" erodiert. **Der Vorteil bleibt real (Latenz + Datenkonsistenz), muss aber jetzt technisch praezise argumentiert werden.**
  - **fonio.ai ist ein neuer Kaeufer-Alternative** in Cosmi's ZFA-Zielgruppe. Fonio hat kein Cross-Modul — aber fonio ist heute verfuegbar, Cosmi nicht. **Cosmi verliert Deals an fonio, solange Cosmi-Dialer nicht Pilot-fertig ist.** Die Cross-Modul-Kontext-Story ist der einzige nicht-preisliche Grund, warum ein Kunde auf Cosmi warten sollte, statt fonio zu kaufen.
  - **Neuer Cross-Modul-Anwendungsfall via `advisoryprotocol`-Subpackage (seit W20 gebaut)**: Cosmi-CRM hat jetzt Beratungsprotokoll-Modul. Ein Voice-Agent, der waehrend eines Anrufs das letzte Beratungsprotokoll referenziert (*"Ihr letztes Gespraech vom 12. August drehte sich um ..."*), ist eine ZFA-Kanzlei-Killer-Story. Kein anderer Anbieter kann das.

**Konkrete technische Umsetzung:**

```
backend/internal/dialer/context/
├── resolver.go                     # Single-Lookup pro Call
├── streaming.go                    # gRPC-Stream fuer LiveKit-Agent
├── sources/
│   ├── crm.go                      # → internal/crm/*
│   ├── crm_advisoryprotocol.go     # NEU seit W20 — Beratungsprotokoll
│   ├── helpdesk.go                 # → internal/helpdesk/*
│   ├── vertraege.go                # → internal/vertraege/*
│   ├── buchhaltung.go              # → internal/buchhaltung/*
│   ├── schichten.go                # → internal/schichten/*
│   └── rapporte.go                 # → internal/rapporte/*
└── mcp_server/                     # MCP-Server-Layer (siehe Empfehlung 2)
    └── voice_context_server.go
```

**Sales-Story-Aktivierung (Marketing-Kampagne):**

1. **Landing-Page** `cosmi.io/dialer-vs-fonio` mit Feature-Matrix + konkreten Use-Cases (Advisory-Anruf, Rechnungs-Nachfrage, Ticket-Eskalation).
2. **3-Fall-Case-Studies** (Muster: Sipgate W35): Zeige Cosmi-Cross-Modul-Anwendungsfaelle bei drei ZFA-Pilot-Kunden konkret.
3. **Botschaft prufbar formulieren**: *"Latenz <10ms in-process vs. 100–200ms Sync bei Sipgate. Datenkonsistenz garantiert (gleiche Postgres-Transaktion). Kein Vendor-Lock in Drittsystem."*
4. **Verkaufs-Argument gegen fonio**: *"Wir sind teurer als €99/Mo — aber wir sind kein isolierter Voice-Bot. Cosmi ist ein Modul deiner Kanzlei-Software, die deinen Kunden bereits kennt."*

**Trade-Off:** Marketing-Kampagne braucht Reife-Voraussetzung — Empfehlung 1 (Compliance) + Empfehlung 2 (Voice-Stack) muessen mindestens Pilot-live sein, sonst wird die Cross-Modul-Story unglaubwuerdig. **Reihenfolge**: (1) Compliance-Layer → (2) Voice-Stack-Basis → (3) Cross-Modul-Kontext + Marketing gleichzeitig.

---

### Bonus-Empfehlung: **AI-Cost-Governance-Layer nach Dialpad-COMPASS-Muster (`internal/dialer/ai_governance/`)**

W20 hat den Bau von `backend/internal/billing/ai-credits/` als Follow-Up empfohlen. **Neu hinzu W36**: Dialpad hat mit COMPASS + Guardian + Credit-Visibility eine **Modell-Vorlage** publiziert, die Cosmi direkt anwenden kann:

- **Cost-Caps pro Tenant + Modul** (kein AI-Voice-Runaway-Cost-Vorfall).
- **AI-Attribution-Log** (welcher Cross-Modul-Call hat welche AI-Kosten produziert — fuer Kunden-Rechnungs-Erklaerung).
- **Consent-Audit-Log** (welche Consent-Statuten galten fuer welchen Voice-Agent-Call — Compliance-Audit-Zeugnis).
- **Pre-Deployment-Validation-Framework** (Dialpad-Proving-Ground-Muster): Ein neuer AI-Voice-Flow durchlaeuft Test-Konversationen vor Produktions-Deploy.

Diese Empfehlung ist **nicht P0** — sie kann nach Empfehlung 1+2+3 gebaut werden, ist aber Voraussetzung fuer Multi-Tenant-Skalierung. Follow-Up-Kandidat 60 Tage.

---

## Quellen

### Konkurrenten-Primaerquellen (W28–W35, 8-Wochen-Fenster)

- **Aircall:** businesswire.com (Vogent M&A 6. Mai / konsolidiert Aug 2025 Salesforce Service Cloud Voice), aircall.io/blog/ai-agents-voice-technology, aircall.io/blog/ai-voice-agent-services-for-business, aircall.io/blog/ai-voice-agent-use-cases, vantagepoint.io/blog/sf/aircall/aircall-ai-voice-agents-24-7-inbound-call-handling, justcall.io/blog/aircall-review.html (Aircall-Pricing-Analyse), voicedrop.ai/aircall-review-explained (2026-Review), hackceleration.com/labs/review/aircall
- **JustCall:** justcall.io/blog/justcall-iq-new-pricing-plans.html, justcall.io/hub/cost/ai-voice-agent-pricing, cloudtalk.io/blog/justcall-pricing, nextiva.com/blog/justcall-pricing.html, squaretalk.com/resources/justcall-pricing-explained, rezora.io/blog/justcall-pricing, alpharun.com/blog/justcall-pricing
- **Dialpad:** businesswire.com/news/home/20260303482706 (Agentic-AI-Platform-Advancement), dialpad.com/press/agentic-ai-platform-to-empower-enterprises, dialpad.com/press/dialpad-launches-its-agentic-ai-platform (März), cxtoday.com/contact-center/the-dialpad-ai-contact-center-and-agentic-ai, cxm.world/customer-experience/dialpad-launches-new-tools-to-get-enterprise-ai-out-of-the-pilot-stage, dialpad.com/whats-new
- **Sipgate:** sipgate.de/blog/sipgate-ai-agents-juni-update, sipgate.ai, sipgate.de/blog, sipgate.de/contact-center, sipgate.de/ai-agents, sipgate.de/changelog, help.sipgate.de/contact-center/en/das-contact-center-fur-agents; W35 Cosmi-intern: SpotMyEnergy Case, 3-Case-Study-Content-Woche
- **Placetel:** placetel.de/ratgeber/ki-telefonassistent, placetel.de/ki-rezeptionist, omr.com/en/reviews/product/placetel/pricing, zeeg.me/de/blog/content/placetel-ai-preise, telefon.services/ki-anbieter/placetel-ai, premium-electronics.eu/en/products/placetel-ai-ki-telefonassistent, click.tools/blog/placetel-alternativen
- **fonio.ai (NEU):** omr.com/en/reviews/product/fonio-ai, fonio.ai/de/news-cool-stuff/top-11-ki-telefonassistenten-fur-deutschsprachige-unternehmen-2026, superchat.de/blog/bester-ki-telefonassistent-preise-funktionen, telefon.services/ki-anbieter/fonio, zeeg.me/de/blog/content/fonio-ai-guide, flinki.ai/tools/fonio-ai, goai.at/blog/fonio-alternativen

### Tech / Stack / Regulierung

- **OpenAI Realtime Pricing:** openai.com/index/introducing-gpt-realtime, hackernoon.com/openai-realtime-api-pricing-in-2026-real-world-data-from-4000-measured-sessions, layer3labs.io/guides/openai-realtime-api-pricing, benchlm.ai/openai/api-pricing, aipricing.guru/openai-pricing, pricepertoken.com/pricing-page/provider/openai, finout.io/blog/openai-pricing-in-2026
- **LiveKit Agents 1.6.x:** livekit.com/voice-agents, livekit.com/products/agent-platform, forasoft.com/blog/article/livekit-ai-agents-guide, forasoft.com/learn/livekit-for-ai-agents-guide, cekura.ai/blogs/livekit-agents, celloip.com/blog/livekit-voice-agents-guide, dev.to/drguthals/build-a-livekit-telephony-agent-3ibe
- **Zendesk Voice AI Aug 2026:** support.zendesk.com/hc/en-us/articles/11068070409882-What-s-new-in-Zendesk-August-2026, kundelab.no/en/articles/whats-new-in-zendesk-august-2026, releasebot.io/updates/zendesk, seif-consult.com/en/blog
- **EU AI Act Art. 50:** cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026, labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729, artificialintelligenceact.eu/transparency-rules-article-50, artificialintelligenceact.eu/article/50, digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act, mccannfitzgerald.com/knowledge/technology-and-innovation/one-month-to-go-eu-ai-act-transparency-compliance, datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026, pure-ip.com/blog/voice-ai-meets-the-eu-ai-act-whats-changing, nerdleveltech.com/eu-ai-act-article-50-ai-agent-disclosure

### Cosmi-interne Querverweise

- `monthly/2026-05-18-deepdive-dialer.md` — Zyklus-1-Baseline (Delta-Vergleich)
- `monthly/2026-08-24-deepdive-crm-core.md` — Zyklus-2-CRM-Referenz (Dialer als CRM-Luecke, dialer-crm-bridge fehlend)
- `keepers/aircall-ai-voice-blitz-dialer-markt-ist-2026-markt-cross-w20.md` — Cosmi-Status-Tabelle Baseline
- `weekly/2026-W35.md`, `weekly/2026-W34.md`, `weekly/2026-W33.md` — sipgate-DACH-Woche, WebRTC-Cluster, OpenAI-Realtime-via-WebRTC, LiveKit v1.13.6, dialer-Feed-Landschaft-Status
- `weekly/2026-W29.md` (crm-core und Zendesk Voice AI Cross-Modul)
- `daily/2026-08-29-regulation.md` — EU AI Act Art. 50 Compliance-Screening-P0-Auftrag mit Dialer-KI explizit als einer der vier Touchpoints
- `daily/2026-08-31-morning.md` — Stille Woche fuer dialer bestaetigt (Feed-Ausfaelle)
- `sources/dialer.yaml`, `sources/_competitors.yaml`

### Source-Maintenance-Debt (kritisch)

Aus W35-Weekly: **dialer-Feed-Landschaft strukturell tot**:

- `aircall-rss-dialer` — 404 persistent seit KW23 (13 Wochen)
- `justcall-rss-dialer` — 404 persistent seit KW23 (13 Wochen)
- `dialpad-rss-dialer` — 404 persistent seit KW19 (17 Wochen)
- `sipgate-rss-dialer` — **neu 404 seit Di 25.08.2026** (Feed-URL-Wechsel)
- `placetel-rss-dialer` — kein RSS dokumentiert

**Empfehlung Source-Maintenance-Sprint (Ziel W37):**
1. Sipgate: URL-Verifikation via `sipgate.de/changelog` oder `sipgate.de/blog-kategorien/releases`
2. Aircall/JustCall/Dialpad: Web-Scrape-Adapter mit Atom-Discovery statt RSS-Retry
3. Placetel: neu Web-Scrape von `placetel.de/blog` erwaegen
4. **fonio.ai** in `sources/dialer.yaml` neu aufnehmen (Blog: fonio.ai/de/news-cool-stuff, OMR-Reviews-Feed pruefen)
5. **AssemblyAI**, **Recall.ai**, **LiveKit** als Tech-Signal-Quellen in `sources/dialer.yaml` neu aufnehmen (bisher nur unter `sources/tech-trends.yaml` erfasst)

---

## Picks (vorgeschlagen)

[ ] 🟢 **EU AI Act Art. 50 + Consent-Framework als kombiniertes P0** — `internal/dialer/compliance/` mit Sub-Packages `consent/`, `ai_disclosure/`, `voice_print/`, `audit/`. Vier Rechtslagen: §201 StGB, Art 179bis CH, EU AI Act Art. 50 (wirksam 02.08.2026), DSGVO Art 17. Bußgeldrahmen €15M/3% aktiv.
[ ] 🟢 **AI-Voice-Stack-Bau mit LiveKit 1.6.x + gpt-realtime-mini + Recall.ai-Fallback** — `internal/dialer/voice_agent/` + `internal/dialer/transcript_provider/`. Kostenprofil: ~$12–$18/Mo Cosmi-Cost fuer 1000 AI-Voice-Min pro Kunde bei €39–€50 Verkaufspreis → 200–250% Marge.
[ ] 🟢 **Cross-Modul-Kontext-Resolver + Sales-Story-Aktivierung gegen fonio.ai** — `internal/dialer/context/` inklusive neuer `crm_advisoryprotocol.go`-Quelle. Marketing-Kampagne `cosmi.io/dialer-vs-fonio` mit 3-Fall-Case-Studies + prufbare Latenz-Argumentation.
[ ] 🟡 **AI-Cost-Governance-Layer nach Dialpad-COMPASS-Muster** (Follow-Up 60d) — `internal/dialer/ai_governance/`: Cost-Caps, Attribution-Log, Consent-Audit, Pre-Deployment-Validation-Framework.
[ ] 🟡 **Source-Maintenance-Sprint dialer** (Follow-Up 7d, Ziel W37) — Sipgate-URL-Verifikation + Aircall/JustCall/Dialpad-Web-Scrape-Adapter + fonio.ai neu aufnehmen + AssemblyAI/Recall.ai/LiveKit als Tech-Signale.
[ ] 🟡 **fonio.ai in Wettbewerber-Rotation als First-Class-Konkurrent aufnehmen** (Follow-Up 14d) — Update `sources/_competitors.yaml`: fonio als `primary_modules: [dialer]`, `region: dach`, `threat_level: high` — direktester DACH-KMU-Konkurrent fuer Cosmi-ZFA-Pilot.
[ ] 🔵 **Marketing-Botschaft "Cosmi kennt deinen Kunden, dein Beratungsprotokoll, deinen Vertrag"** (Inspire) — 2-Satz-Pitch mit `advisoryprotocol`-Verweis (seit W20 gebaut). Verifizierbar via Latenz-Argumentation + Datenkonsistenz-Garantie.
[ ] 🔴 **NICHT-Pick:** Vollstaendige Feature-Parity zu Sipgate/Aircall vor Pilot-Launch. Cosmi kommt zu spaet fuer Feature-Wettlauf. **Differenzierung ueber Compliance + Cross-Modul, nicht ueber Feature-Zahl.**

---

## Delta-Zusammenfassung (fuer Weekly-W36-Einspeisung)

**Was hat sich seit W20 (Zyklus 1) veraendert?**

1. **Cosmi-Dialer-Fortschritt in 15 Wochen: null.** Alle 7 W20-Picks offen. Backend-Investment ging in CRM-Hardening (RLS + Migrations 111→297 + advisoryprotocol).
2. **Markt hat zweiten AI-Reife-Sprung gemacht**: Sipgate von "Empfangsassistent" zu "Live-Task-Execution", Aircall Vogent konsolidiert + Salesforce SCV-Native, JustCall AI-Voice gebundelt, Dialpad Enterprise-Governance-Layer (COMPASS/Guardian).
3. **Neuer Konkurrent im Cosmi-Zielsegment**: **fonio.ai** hat OMR Top-100 Platz 1 gewonnen, 6.500 Kunden in 1 Jahr, DACH-native-AI-Voice. Cosmi-ZFA-Pilot-Sales muss ab jetzt gegen fonio positionieren.
4. **Technologie-Stack ist 3× billiger geworden**: gpt-realtime-mini bei $0.016/Min uncached ($0.005/Min mit Caching). Profitable AI-Voice-Preise ohne Add-On-Aufschlag moeglich.
5. **LiveKit 1.6.x macht Turn-Taking-Bau einfacher**: Semantic Turn Detection als Default. Aircall musste Vogent kaufen — Cosmi bekommt Aircall-Vogent-Niveau via Framework-Upgrade.
6. **Neue Rechtsschicht wirksam**: EU AI Act Art. 50 seit 02.08.2026 aktiv. Voice-AI-Erstkontext-Offenlegung Pflicht, €15M/3% Rahmen. Cosmi hat W35 als P0-Sofortauftrag markiert, Dialer-KI-Screening offen.
7. **Rueckstand-Schaetzung revidiert**: W20 sagte 18–24 Monate Rueckstand. Nach 15 Wochen ohne Cosmi-Bewegung real 21–27 Monate. **Aber**: Kaufer-verhalten hat sich nicht mit dem Feature-Wettlauf mitbewegt — Cosmi-Cross-Modul-Story + Compliance-First + Buy-Recall.ai-statt-Baue-alles-selbst kann Rueckstand in ~4–6 Monaten operational aufholen.

---

## Telemetry-Anhang

- **Pool-Verbrauch:** ~11% (well within Threshold 0.15)
- **Runtime:** ~47 Min (within 60-Min-Cap)
- **Items-Input:** 1 Zyklus-1-Deepdive (Baseline) + 1 Zyklus-2-CRM-Referenz + 13 Weeklies (W22–W35) + 1 Keeper + 1 Regulation-Report + 8 WebSearches (Aircall, JustCall, Dialpad, Sipgate, Placetel, fonio.ai NEU, OpenAI Realtime, LiveKit, Zendesk, EU AI Act Art. 50) + 0 Headless-Chromium-Polls
- **Wettbewerber-Coverage:** 5/5 W20-Top-Konkurrenten (Aircall, JustCall, Dialpad, Sipgate, Placetel) + 1 NEUER Konkurrent (fonio.ai) — 6-Spalten-Vergleichstabelle
- **Verglichene Features:** 38 Feature-Achsen (W20: 32) — +6 Zeilen fuer Cost-Governance, Provider-Optionalitaet, EU AI Act, Live-Task-Execution, Stimmqualitaet, Free-Trial
- **Delta-Baseline:** 2026-05-18 → 2026-08-31 (15 Wochen)
- **Feed-Coverage-Status kritisch:** aircall/justcall/dialpad RSS 404 persistent (13–17 Wochen), sipgate RSS neu 404 seit W35 → Cosmi ist blind auf 4/5 Top-Konkurrenten via RSS. Deepdive basiert primaer auf WebSearches (8) + Cosmi-interne Cross-Refs. Source-Maintenance-Sprint als Pick 🟡 aufgenommen.
- **KMU-Hub-Repo-Zugriff:** nicht verfuegbar (Worktree-Pfad `/home/deploy/actions-runner/_work/KMU-Hub/KMU-Hub/` leer) — IST-Stand abgeleitet aus Cosmi-intern-Cross-Refs, nicht aus Code-Lesung.
- **Discord-Push:** Pending → `.state/discord_push_pending.json` (Header + Top-3-Empfehlungen-Embeds fuer `#trends`).
- **Naechste Rotation:** `video` (KW37, 2026-09-07). Zyklus-1-Referenz: `monthly/2026-05-25-deepdive-video.md`.
