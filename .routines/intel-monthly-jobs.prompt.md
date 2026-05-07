# Routine: intel-monthly-jobs

Cron: `0 7 15 * *` (15. d.M. 07:00 Berlin)
Modell: claude-sonnet-4-6
Max Output: 30000 Tokens
Max Runtime: 40 min
Pool-Threshold-Abort: 0.20

## Rolle

Job-Board-Signal + G2/Capterra-Review-Sweep. Was sagen Konkurrenz-Job-Postings ueber deren Strategie? Was sagen Reviews ueber Cosmi-Chancen?

## Workflow

### Job-Board-Signal

1. Pro Top-10 Konkurrent mit `linkedin_jobs_query` oder Web-Scrape-Konfiguration:
   - StepStone/Indeed: Public-Suche `<konkurrent>` + Stadtfilter (Berlin/Muenchen/Wien/Zurich)
   - Headless-Chromium-Scrape, max 20 Stellen pro Konkurrent
   - Cluster nach Rolle (Eng, PM, Sales, Customer Success, Ops)
2. **Signale interpretieren:**
   - 5+ Eng-Stellen offen -> grosse Tech-Investition vs Stillstand
   - Specialisierte Rollen (z.B. "AI Engineer", "Compliance Lead") -> strategische Richtung
   - Senior-Roles dominieren -> Reife-Phase

### G2/Capterra-Review-Sweep

1. Pro Konkurrent mit `g2_review_url`:
   - Scrape neue Reviews seit letztem Run
   - Filtere auf "Pain-Points" (Cons-Spalte)
   - Cluster Pain-Points
2. **Pain-Point-Mining:** Cosmi-Chance-Analyse — wo Konkurrenten schwach, ist Cosmi-Marketing-Hebel.

## Output-Schema

```markdown
---
year: 2026
month: 5
created: 2026-05-15
runtime_minutes: 35
job_postings_scanned: 142
reviews_scanned: 89
---

# Jobs + Reviews Mai 2026

## Job-Board-Signal

### Pipedrive — 23 offene Stellen DACH
- 8 Engineering (incl 3 "AI Engineer", 1 "ML Platform")
- 7 Sales
- 4 Customer Success
- 4 Sonstige
**Interpretation:** AI-Investment ist real und groß. Pipedrive haben dafuer einen eigenen ML-Platform-Team aufgebaut.

### HubSpot — 14 offene Stellen Berlin
... (analog)

### Stille Konkurrenten (keine offenen Stellen)
- Bexio (DACH-Niveau, normal)
- Centralstation CRM (klein)

## Review-Pain-Points (Cosmi-Chance-Analyse)

### Zendesk — Top-3 Pain-Points neue Reviews
1. **"Pricing nicht transparent"** (8 Reviews, 4 Sterne -> 2 Sterne)
   **Cosmi-Chance:** Cosmi-Pricing offen kommunizieren ist USP-Hebel.
2. **"AI-Drafts halluzinieren"** (5 Reviews)
   **Cosmi-Chance:** "Konservative AI" als Cosmi-Marketing-Botschaft.
3. ...

### sevDesk — Top-3 Pain-Points
... (analog)

## Cross-Pattern (was wiederholt sich bei mehreren Konkurrenten?)

- **Onboarding-Komplexitaet** ist 3x in Reviews genannt (Pipedrive, monday, Zoho)
  -> Cosmi-USP-Erweiterung: "1-Woche-Onsite" stoesst auf Marktbeduerfnis.

## Cosmi-Action-Items

[ ] 🟢 Pricing-Transparenz auf zentria.tech vor Launch ueberarbeiten
[ ] 🔵 "Konservative AI"-Marketing-Botschaft entwickeln (-> inspiration/)
[ ] 🟡 Onboarding-USP staerker kommunizieren (-> followup 14d, vor Launch)
```

## Discord-Push

Wenn `DISCORD_WEBHOOK_TRENDS`: poste 1 Embed pro Action-Item mit Buttons.

## Constraints

- Hard-Output-Cap 30000 Tokens.
- Web-Scraping-Failure-Handling: Quelle nach 3 Failures auto-mute, in `settings.yaml.muted_sources` ergaenzen.
- Telemetry.
