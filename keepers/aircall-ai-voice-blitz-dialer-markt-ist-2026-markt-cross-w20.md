---
id: W20-T03-i01
slug: aircall-ai-voice-blitz-dialer-markt-ist-2026-markt-cross-w20
created: '2026-05-15'
weekday: friday
modules: []
themes: []
n_sources: 0
trend_score: 5
decision: keep
---

Aircall hat in 10 Tagen einen vollstaendigen AI-Voice-Platform-Pivot kommuniziert:

| Feature | Status Aircall | Status Cosmi-Dialer |
|---|---|---|
| Call-Transkription | ✅ AI Knowledge Automation (RAG + CRM-Sync) | ❓ geplant Phase C |
| Institutionelles Wissen aus Calls | ✅ Auto-Sync zu Salesforce/HubSpot/Notion/Slack | ❌ |
| 24/7 AI Inbound Agent | ✅ Voice Agent Platform (90% After-Hours-Resolution bei SJWD) | ❌ |
| Post-Call-Automatisierung | ✅ AI Actions (HubSpot/Zendesk/Shopify-Actions live) | ❌ |
| AI→Human Handoff mit Kontext | ✅ Vogent-Tech (Voice Activity Detection, Turn-Taking) | ❌ |
| Custom Voice Models | ✅ Vogent-Akquisition | ❌ |

Plus: JustCall AI→Live Rep warm handoff ist Standard im Markt. Sipgate (DACH-relevant) positioniert eigene AI-Agents. **23.000 Businesses bei Aircall, keine explizite EU-Sovereignty-Argumentation kommuniziert.**

**Cosmi-Implikation:** Cosmi-Dialer-Pilot ist ohne AI-Transkription+CRM-Sync ein Plain-VoIP-Produkt im AI-Standard-Markt. Die minimale AI-Tabellenstake fuer einen 2026-DACH-KMU-Dialer-Launch ist: (1) Transkription, (2) automatische CRM-Sync, (3) Call-Summary. Alles darueber ist Differenzierung — diese drei sind Pflicht. Architektonisches Differenzierungsmerkmal: Cosmi-Dialer muss Cross-Modul-Kontext nutzen (CRM-Daten, Schichtplaene, Rapporte) — kein isolierter Dialer. **Plus ElevenLabs-Klage** zeigt: Call-Recording braucht Pre-Call-Consent-Framework als P0.

**Modul-Pfad:** `backend/internal/dialer/transcription/`, `backend/internal/dialer/context/` (Cross-Modul-Zugriff), `backend/internal/dialer/recording/consent/`

**Quellen:** 7 Items aus 4 Quellen (Aircall-Blog ×5, JustCall-Blog, Sipgate-Blog, Sifted-ElevenLabs)

**Trend-Score:** 0.84

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss

---
