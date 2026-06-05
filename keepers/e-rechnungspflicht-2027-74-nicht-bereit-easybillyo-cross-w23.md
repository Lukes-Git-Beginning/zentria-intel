---
id: W23-T04-i01
slug: e-rechnungspflicht-2027-74-nicht-bereit-easybillyo-cross-w23
created: '2026-06-05'
weekday: friday
modules: []
themes: []
n_sources: 0
trend_score: 5
decision: keep
---

**Easybill veröffentlicht am Mi 03.06. YouGov-Studie (n=502 deutsche Unternehmen)** — die erste belastbare Marktforschung zur B2B-XRechnungs-Pflicht ab 01.01.2027:

| Kennzahl | Wert |
|---|---|
| Komplett bereit für E-Rechnungspflicht 2027 | **26%** |
| Nie eine E-Rechnung versandt | **33%** |
| Implementierungs-Status: abgeschlossen | 24% |
| Implementierungs-Status: in Bearbeitung | 38% |
| Implementierungs-Status: nicht gestartet / frühe Planung | **29%** |
| Haupthürde: technische Implementierung | 36% |
| Haupthürde: rechtliche Unklarheit | 29% |
| Haupthürde: fehlendes Wissen | 27% |
| Aktuelle Nutzung: Buchhaltungssoftware | 39% (höchste Adoption) |
| Aktuelle Nutzung: Excel | 11% |
| Aktuelle Nutzung: Word | 10% |

**Quote Benjamin Klein (easybill-CEO):** *"Moderne Software erstellt konforme E-Rechnungen mit wenigen Klicks, zu minimalen monatlichen Kosten. Das Tool existiert und ist erschwinglich — was jetzt fehlt, ist die Entscheidung, zu beginnen."*

**Plus regulatorische Klammer:**
- **Versandpflicht ab 01.01.2027 für Unternehmen mit > €800.000 Vorjahresumsatz** (Sa-Reg 30.05. carry-forward)
- **Versandpflicht ab 01.01.2028 für alle B2B-Unternehmen**
- Aktuell zugelassene Formate: **XRechnung 3.0.2** (B2G, reines XML), **ZUGFeRD 2.4** (B2B, PDF+XML)
- Lexware-Konkurrent veröffentlicht Mai-Compliance-Serie zur EU AI Act + Steuerkanzlei (Di 02.06.) — Steuerberater werden als "Compliance-Multiplikatoren" positioniert (sie führen Mandanten durch KI- + E-Rechnungs-Regulierung).
- Gradient Labs (London/EU-Fintech-AI) verdoppelt Series A auf $26 Mio. — CommerzVentures als Lead-Investor (DACH-Finanzakteure suchen aktiv EU-AI-Finanzlösungen).

**Cosmi-Implikation:** Dies ist der schärfste **Cosmi-spezifische Widerspruch des Tages** — und der schärfste konkrete Akquisitions-Trigger des Quartals.

1. **74% Marktlücke ist zeitgebunden.** 7 Monate bis 01.01.2027. Easybill nutzt die Studie als Awareness-Funnel (Awareness → Entscheidung → Tool-Wahl). Cosmi kann denselben Funnel nutzen, mit dem Differenzierungsargument: **"XRechnung+ZUGFeRD ist in Cosmi eingebaut UND direkt mit CRM, Schichten, Rapporten verknüpft — kein Einzeltool, sondern integrierter Workflow."**

2. **Verifikations-P0:** Hat Cosmi-Buchhaltung XRechnung 3.0.2 / ZUGFeRD 2.4 vollständig implementiert? Mi-Evening dokumentiert: "kein Code-Fund in `backend/internal/buchhaltung/` zum Zeitpunkt der Intel-Recherche." Wenn die Implementierung fehlt, ist das **P0 vor Buchhaltungs-Launch — Frist 01.01.2027, nicht "Phase Roadmap"**. Sprint-4-Normalisierung muss XRechnung+ZUGFeRD-3.0 mitnehmen.

3. **Steuerberater-Channel als Multiplikator:** Lexware positioniert Steuerberater als Compliance-Vermittler. Cosmi sollte diesen Channel parallel adressieren — **Cosmi-Partner-Programm für DACH-Steuerkanzleien** als Distributions-Funnel. Modul-Pfad: `marketing/channel/steuerberater-partner-programm/`.

4. **Frist-Druck als Marketing-Asset:** Die 7-Monats-Frist ist kein Risiko — sie ist der wertvollste Verkaufsbeschleuniger des Jahres. Cosmi-Landingpage: **"01.01.2027: Sind Sie bereit?"** mit Self-Service-Compliance-Check als Lead-Magnet.

**Modul-Pfad:** `backend/internal/buchhaltung/einvoice/xrechnung/` (P0 vor Launch), `backend/internal/buchhaltung/einvoice/zugferd/` (P0), `backend/internal/buchhaltung/einvoice/peppol/` (B2G), `marketing/channel/steuerberater-partner-programm/`, `marketing/campaign/2027-readiness-check/`.

**Quellen:** 6 Items aus 4 Quellen (Easybill/YouGov, Lexware-Blog, Sifted-Gradient-Labs, BMWK-via-Sa-Reg-30.05.).

**Trend-Score:** 0.88 (höchste DACH-KMU-Spezifik aller Cluster).

[ ] 🟢 Keep | [ ] 🟡 Followup | [ ] 🔵 Inspire | [ ] 🔴 Dismiss

---
