---
id: W20-T04-i01
slug: kritisch-olg-hamm-unternehmen-haftet-fuer-chatbot--cross-w20
created: '2026-05-15'
weekday: friday
modules: []
themes: []
n_sources: 0
trend_score: 5
decision: inspire
---

**Quelle:** OLG Hamm (4. Zivilsenat), Urteil 13. Mai 2026. Klaeger: Verbraucherzentrale NRW. Beklagte: Aerzte-Praxis ("Dr. Rick & Dr. Nick"). Rechtsgrundlage: UWG-Irrefuehrungsverbot. Revision zum BGH zugelassen.

**Was neu ist:** Bisherige Haftungsdiskussionen fokussierten auf fehlerhafte Inputs (Prompt-Engineering, Trainingsdaten). Das OLG Hamm setzt einen anderen Massstab: **Das Ergebnis zaehlt, nicht der Weg dorthin.** Halluzinationswahrscheinlichkeit ist kein Haftungsausschlussgrund. Wer einen Chatbot betreibt, uebernimmt Redaktionsverantwortung fuer dessen Outputs.

**Cosmi-Implikation:** Jedes Cosmi-Modul das AI-generierte Texte nach aussen zeigt — `helpdesk/` (Auto-Triage, Drafts), `crm-core/` (AI-Kontaktnotizen, Forecast-Texte), `formulare/` (AI-ausgefuellte Felder), `vertraege/` (AI-Vertragsentwuerfe) — ist exponiert. Drei konkrete Handlungspflichten:

1. **Disclaimer-Pflicht** als Architektur-Constraint: `frontend/src/components/ai/AiGeneratedDisclaimer/` — jede AI-Ausgabe muss als "KI-generiert, nicht geprueft" erkennbar sein, technisch erzwungen.
2. **Human-in-the-Loop als Standard**: AI-Drafts duerfen nicht ohne menschliche Freigabe nach aussen gesendet werden. "Send"-Knopf darf nicht AI-initiiert sein. `backend/internal/helpdesk/ai/draft-policy/`.
3. **Opt-out pro Modul**: Cosmi-Kunden muessen AI-Features pro Modul deaktivieren koennen ohne Funktionsverlust. `backend/internal/core/feature-flags/ai-opt-out/`.

**Kombiniert mit EU AI Act Art. 50 (Deadline 2. August 2026)** ist das eine doppelte Compliance-Klammer: OLG-Hamm fuer Halluzinations-Haftung, EU AI Act fuer Disclosure-Pflicht. Beide muessen vor erstem AI-Feature-Launch erfuellt sein.

**Modul-Pfad:** `frontend/src/components/ai/AiGeneratedDisclaimer/`, `backend/internal/helpdesk/ai/draft-policy/`, `backend/internal/core/feature-flags/ai-opt-out/`

**Quellen:** 4 Items aus 3 Quellen (Heise OLG-Hamm, Heise EU AI Act Art. 50, Sifted ElevenLabs, Heise Apple vs EU)

**Trend-Score:** 0.91

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss

---
