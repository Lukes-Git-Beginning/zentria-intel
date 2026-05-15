---
id: W20-T02-i01
slug: outcomecredits-based-ai-pricing-6-plattformen-in-1-cross-w20
created: '2026-05-15'
weekday: friday
modules: []
themes: []
n_sources: 0
trend_score: 5
decision: followup
followup_due: '2026-05-29'
---

| Datum | Plattform | Mechanismus |
|---|---|---|
| ~15. Apr | **HubSpot Breeze** | $0.50/resolved conversation, $1/qualified lead (live, +67% QoQ Credit-Verbrauch) |
| 30. Apr | **Twenty v2.1.1** | AI Credit-Cap an Entry-Points |
| 4. Mai | **Notion** | Custom Agents Credits, Pause bei Erschoepfung |
| 7. Mai | **Intercom Fin for Sales** | $10/qualified lead, $1/disqualified — Kunden definieren Kriterien |
| 8. Mai | **Intercom Fin for Ecommerce** | Shopify-native AI Agent |
| 11. Mai | **Zendesk** | Advanced AI in alle Plans, Consumption-Tracking (Rollout-Start) |
| 11.-14. Mai | **Twenty v2.4.0-v2.4.2** | Billing-Default-Feature-Flag aktiviert, Agent-Workflow-Runner |
| 13. Mai | **monday.com** | Vollstaendiger Umbau zur AI Work Platform mit Credits-Pricing |
| 13. Mai | **Lenny-Newsletter** | "SaaS Freemium funktioniert nicht fuer AI" — Framework (Usage-Intensity, Outcome, Compute-Modality) |

**Cosmi-Implikation:** `backend/internal/billing/ai-credits/` ist kein Q4-Backlog-Item — es ist Voraussetzung fuer jeden AI-Feature-Launch. Nachtraegliche Einfuehrung erzwingt Breaking Changes in bestehenden Kundenvertraegen. Architektur muss **multi-dimensional** sein: (1) Usage-Intensity (Token-Budget pro Tier), (2) Outcome (pro AI-Draft/Ticket-resolved/Vertrag-generiert), (3) Compute-Modality (Reasoning-Tasks separat). Twenty's Open-Source-Billing v2 ist die einzige analysierbare Referenz-Implementierung.

**Modul-Pfad:** `backend/internal/billing/ai-credits/`, `backend/internal/billing/ai_usage_events/` (event_type, tier_required, credits_consumed)

**Quellen:** 11 Items aus 7 Quellen (Diginomica, Intercom-Blog, HubSpot-Blog, Zendesk-Help, GitHub-Twenty, Lenny-Newsletter, Sifted)

**Trend-Score:** 0.95

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss

---
