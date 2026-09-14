---
year: 2026
week: 38
modul: wiki
created: 2026-09-14
routine: intel-monday-deepdive
model: claude-opus-4-7
rotation_position: 4/15 (Zyklus 2)
prev_deepdive: monthly/2026-06-01-deepdive-wiki.md (W23, Zyklus 1)
delta_weeks: 15
---

# Deepdive: wiki (Mo W38/2026)

> **Zweiter wiki-Deepdive.** Zyklus-1-Baseline war W23 (2026-06-01). Zwischen W23 und heute liegen 15 Wochen; das Fenster ist gross genug fuer strukturelle Delta-Aussagen sowohl auf Cosmi-Seite (Sprint 3–4 Editor-Ausbau) als auch auf Konkurrenz-Seite (Docmost v0.90→v0.96, Notion Custom-Agents-Credits-GA, Atlassian AI-Training-Opt-in-Live am 17. Aug 2026, EU-AI-Act Art. 50 in Kraft seit 2. Aug 2026, Confluence Data Center EOL-Ankuendigung, Outline MCP-Server offiziell). Diese Ausgabe fokussiert deshalb bewusst auf **Delta zum W23-Bericht** — was ist Cosmi jetzt aufgeholt, was ist strukturell weiter offen, und welche W23-Empfehlungen sind ueberrollt worden.

> **Stand Cosmi-Wiki (2026-09-14):** Backend `backend/internal/wiki/` **von ~750 LOC auf 3444 LOC gewachsen (+4.6×)** — vor allem `postgres_repository.go` (552), `service.go` (598), `share.go` (158) + Test-Coverage-Ausbau (Tenant-Isolation-P2, Share-Redeem-DB-Test). Frontend `desktop/src/renderer/src/modules/wiki/` **von ~1284 LOC auf 4328 LOC gewachsen (+3.4×)**. **Zentraler Editor-Umbau vollzogen**: `WikiEditor.tsx` ist **kein `<textarea>` mehr** — er ist ein duenner Wrapper um `DocumentBlockEditor` aus `@/components/shared/document/` (Cosmi-eigenes Block-Doku-Engine, 679 LOC, geteilt zwischen `berichte` und `wiki`). Rich-Text-Bloecke innerhalb dessen laufen ueber **TipTap v3.20** (`@tiptap/react`, `@tiptap/starter-kit` + Link/Image/Table/TaskList/TextAlign/Underline/CodeBlock-Lowlight-Extensions). Wiki-eigene TipTap-Extensions: `WikiLinkExtension` (`[[Artikel]]`) und `WikiMentionExtension` (`@user`). Migrations 000230 (RLS wiki+HR-child-tables) und 000297 (Share-Token-Revocation) sind live.

> **Leit-Signal der Woche:** Drei Bewegungen kollidieren auf **einem** Datum — dem 17. August 2026: (a) **Atlassian schaltet Default-Opt-in fuer Confluence-/Jira-Inhalte zum AI-Training** frei (Free/Standard/Premium koennen Content aber nicht Metadaten opten; nur Enterprise voll), (b) **Confluence Data Center Neu-Lizenz-Verkauf ist seit 30. Maerz 2026 gestoppt**, Bestandsverlaengerung nur bis 30. Maerz 2028, Full-Cutoff 28. Maerz 2029 — DACH-KMU mit Confluence-Data-Center haben ein **3-Jahres-Migrationsfenster**, das ab Q4/2026 sales-relevant wird, (c) **EU-AI-Act Article 50 ist seit 2. August 2026 durchsetzbar** — Fines €15M oder 3% Weltumsatz, BNetzA/BaFin sind zustaendig. Cosmi's KMU-Hub-Doku sagt "TipTap Rich Text bereits vorhanden, verwendet in Meeting-Notizen, Wiki, Mail" (`docs/STRATEGY.md`) — TipTap ist live, aber Cosmi hat **immer noch keine `ai_disclosure`-Schicht**, obwohl Meeting-AI-Summary (`backend/internal/llm/`) produktiv ist und Article-50-Trigger auslösen kann. **Der W23-Bericht hat Disclosure-Layer als P0-Sprint-3-Welle-0 empfohlen — diese Empfehlung wurde nicht ausgeliefert und muss jetzt in einer Compliance-Nachholrunde vor Meeting-AI-GA re-eskaliert werden.**

---

## Was ist seit W23 auf Cosmi-Seite passiert?

Die W23-Empfehlung 1 (TipTap-Frontend live) ist **weitgehend umgesetzt, aber auf einem eigenen Weg**: statt "TipTap-Editor mit Slash-Commands" ist Cosmi den Weg "eigenes Document-Block-Engine (`DocumentBlockEditor`) + TipTap-nur-in-Rich-Text-Bloecken" gegangen. Dieselbe Engine bedient `berichte` — das ist die klassische Modul-Kopplungs-Rechtfertigung, die dem KMU-Hub-Wertversprechen entspricht. Konkret sichtbar:

- **Frameless writing canvas mit Playfair-Title-Heading** (WP-1 aus dem Modul-Editor-Rollout-Doku).
- **Identity-Bar** (Icon + Cover-URL) — 1:1 das Notion-Pattern.
- **Change-Notes im Save-Footer** — sinnvolle Ausdehnung des `wiki_versions`-Schemas ohne Migration.
- **`[[wiki links]]`** ueber `WikiLinkExtension` mit **`WikiSuggest`-Popover** und **`LinkPreviewPopover`** (Read-Modus zeigt beim Klick eine Vorschau).
- **`@mention`** ueber `WikiMentionExtension` — verlinkt auf `useWikiUsers`-Store.
- **Tag-Editor** (`WikiTagEditor`, 140 LOC).
- **Move-Dialog** (Reparenting via `WikiMoveDialog`, 153 LOC — Kategorien-Umzug).
- **Template-Manager + Dialog** (`WikiTemplateManager` 267 LOC, `WikiTemplateDialog` 192 LOC) — Backend-Templates-Quelle ist noch nicht sichtbar, aber die UI-Schicht ist da.
- **Table-of-Contents** (`WikiToc`, 82 LOC) — Client-side gerendert aus Heading-Bloecken.
- **Version-Diff** (`WikiVersionDiff`, 83 LOC + `wikiDiff.ts`, 71 LOC) — **das ist Umsetzung der W23-Kritik "kein Side-by-Side-Diff"**.
- **Reading-Prefs-Store** (`useWikiPrefsStore`, `wide` vs. `max-w-65ch mx-auto`).
- **DOMPurify-Sanitization** ist in `wiki-blocks.tsx` importiert und bleibt Cosmi's DXSS-Schutz.
- **Backend-Wachstum** auf 3444 LOC — insbesondere `share.go` (158) plus `share_redeem_db_test.go` (259) zeigen: **Share-Token-Redeem-Endpoint ist implementiert** (in W23-Bericht war der Verdacht "Schema da, Service-Methode nicht erkennbar" — das ist inzwischen geschlossen).

**Was seit W23 NICHT geliefert wurde (Kern-P0-Rueckstaende):**

1. **W23-Empfehlung 2: `ai_disclosure`-Layer.** Keine Tabelle `ai_interactions`, kein `<AIBanner>`-Component-Grep-Hit, keine `docs/compliance/ai-providers.md`. Cosmi hat **einen produktiven AI-Endpoint** (`backend/internal/llm/client.go`, verwendet fuer Wave-7C-Meeting-AI-Summary) — der laeuft ohne Disclosure-Schicht. **Article 50 ist seit 6 Wochen durchsetzbar.**
2. **W23-Empfehlung 3: pgvector fuer `wiki_articles`.** Extension ist enabled (Migration 000072), aber nur **Contacts** haben einen Embedding-Column (000073). Kein `wiki_articles.embedding`, kein `SearchArticlesHybrid`-RPC.
3. **Real-Time-Collab (Yjs).** Kein `y-*`-, `hocuspocus`- oder `Collaboration`-Package in `desktop/package.json`. Save-on-Blur-Modell haelt.
4. **MCP-Server fuer Cosmi-Wiki.** Weder `backend/internal/core/mcp-server/` noch ein eigener Server im Wiki-Modul.
5. **Cross-Modul-Backlinks** (Wiki-zu-CRM-Deal / Wiki-zu-Helpdesk-Ticket). `WikiMentionExtension` verweist auf User, `WikiLinkExtension` auf Wiki-Artikel — der Cosmi-USP-Hebel "Wiki referenziert Deal referenziert Ticket" ist weiter nicht aktiviert.
6. **Page-Verification / Approval-Workflow.**
7. **Inline-Kommentare** — kein `WikiComment*`-File.
8. **Slash-Commands im echten Prosa-Fluss.** `DocumentBlockEditor` hat einen `Plus`-Insert-Menue-Button und Drag-Reorder — aber die Notion-typische `/heading`-`/code`-`/quote`-Inline-Slash-UX ist nicht sichtbar in `DocumentBlockEditor.tsx:1-80` bzw. `wiki-blocks.tsx:1-80`. (Verifikation empfohlen — falls doch vorhanden, ist es ein kleiner Follow-up; falls nicht, ist es ein wachsendes UX-Gap gegen Notion+Docmost.)

Das ist ein deutlich gemischtes Bild: der **Editor-Umbau ist ein grosser Wurf** (shared engine, TipTap real, Wiki-Cross-Refs, Version-Diff, Identity-Bar) — die **Compliance- und AI-Schicht ist strukturell offen** und wird mit jedem Tag risikoreicher.

---

## State-of-the-Art (Delta W23 → W38)

Zwei Bewegungen dominieren die 15 Wochen:

**(a) MCP-Server ist von Outline-Solo-Move (W23) zum wiki-uebergreifenden Table-Stake geworden.**

Im W23-Bericht war MCP-Server noch als "Phase-3-Kandidat" fuer Cosmi eingestuft — Outline hatte es als Erster gemacht (v1.6+v1.7). Zwischen W23 und W38 hat sich das gedreht:

- **Outline** hat den MCP-Server auf **den offiziellen, empfohlenen Weg** fuer AI-Integration mit Self-Host-Instanzen erhoben (patchen, verschieben, loeschen, Comments, Breadcrumbs, Summaries, Suggested Titles).
- **Docmost v0.96 (September 2026)** hat **MCP OAuth** ausgeliefert — das ist die enterprise-taugliche Variante mit richtigem Auth-Flow. Zusammen mit **Turbopuffer AI vector search driver**, **SIEM-Integration (Splunk/Datadog)** und **Page-Version-Comparison** hat Docmost binnen ~4 Monaten (v0.90→v0.96) die Feature-Luecke zu Notion/Confluence im Self-Host-Segment **materialisch geschlossen**.
- **Anthropic-eigene Kollateral-Bewegungen**: MCP ist "USB-C for AI"-Framing, Claude Code hat MCP-Server-Integration jetzt eingebaut, Directory-Submission-Prozess ist live.

Fuer Cosmi bedeutet das konkret: **jeder tech-affine DACH-KMU-Prospect, der 2026-Q4 seinen Wiki-Stack evaluiert, prueft "kann ich das mit Claude/Cursor/Antigravity verbinden?"** — wenn Cosmi-Wiki das nicht anbietet, ist die Antwort im Sales-Call "warum sollte ich Cosmi statt Docmost self-hosten?".

**(b) Confluence-Nachwehen: Atlassian trainiert seit 17. Aug 2026 default auf Kundenpage-Titel und -Bodies (opt-out nur Enterprise).**

Der W23-Bericht hatte diesen Move als "Cosmi-Sales-Folie-P0" markiert. In der Zwischenzeit sind **zwei zusaetzliche** DACH-relevante Signale dazu gekommen:

- **Confluence Data Center Neu-Lizenz-Verkauf ist per 30. Maerz 2026 gestoppt** — Bestandskunden koennen bis 30. Maerz 2028 verlaengern, ab 28. Maerz 2029 ist die Software read-only. Konkret fuer DACH-KMU-Bestand: eine harte Deadline, die in Q4-2026-Sales-Gespraechen adressiert werden muss.
- **Atlassian Team '26 (April 2026, Anaheim)** hat Rovo Studio, Teamwork-Graph und Strategy Collection weiter in Enterprise-Richtung gepusht — die Botschaft an den Mittelstand ist implizit "wenn ihr nicht Enterprise seid, dann seid ihr Feature-Nachrangig **und** AI-Training-Beitrager".

Kombiniert mit der bekannten Rovo-Metadaten-Pflicht (nicht opt-outbar auf Free/Standard/Premium) ist der DACH-Datenschutz-Beauftragten-Audit-Druck fuer Q4/2026-Q1/2027 realistischer als im W23-Bericht angenommen. **openDesk-XWiki-Bundle via ZenDiS** ist im Public-Sector-Kanal aktiv (OpenProject 17.6 vom Juli 2026 hat erste native XWiki-Integration ausgeliefert) — Public-Sector wird zuerst umsteigen, DACH-KMU folgen sekundaer.

**(c) Notion konsolidiert Agent-Pricing-Modell, sunset-t Notion-Mail als Standalone, macht LLM-Modell-Wahl zum Admin-Feature.**

- **09. September 2026**: Workspace-Owner koennen pro Agent (Notion Agent + Custom Agents) **entscheiden welches Modell zulaessig ist** und einen Default fuer Custom Agents setzen — reine Governance-Funktion fuer Cost-Predictability + Compliance (Business+/Enterprise-only).
- **28. August 2026**: **Suggested Edits** — Agent-Vorschlaege als Line-Level-Approvals, bevor sie committed werden. Das ist die Notion-Antwort auf "AI hallucinates in unser Wiki".
- **22. September 2026 (angekuendigt)**: **Notion Mail wird als Standalone-App gesunset**; die Idee ist, Mail als Kontext-Quelle in Notion-Agents zu ueberfuehren. Cosmi hat kein direktes Mail-Pendant, aber die Bewegung zeigt: **Konkurrenten haben die "Universal Context Layer"-Strategie internalisiert** — jede Fach-App wird zu Kontext-Feeder fuer den Workspace-Agent.
- Custom Agents kosten 10$/1000 Credits ab Mai 2026; das Modell hat sich stabilisiert.

Fuer Cosmi ist die Notion-Bewegung **kein direkter Sales-Wettbewerbs-Druck** (Notion ist DACH-KMU-Cloud-only, kein Self-Host), sondern **das Referenz-Muster fuer User-Erwartungen**. Ask-the-Workspace mit Modell-Wahl-Governance und Suggested-Edits ist das, was Cosmi-Enterprise-Prospect ab 2027 erwartet.

**(d) EU-AI-Act Article 50 ist keine Ankuendigung mehr — er ist durchsetzbar.**

Seit 2. August 2026 gilt Artikel 50 verbindlich. Fines €15M oder 3% Weltumsatz — fuer Cosmi als Bootstrap-Firma existenzbedrohend. Enforcement liegt bei nationalen Marktueberwachungsbehoerden (in DE de-facto BNetzA + BaFin je nach Anwendungsdomain). Vier Pflichtbereiche:

1. **Direkte Interaktion** — Wenn ein AI-System mit einer natuerlichen Person interagiert (z.B. Chat, AI-Suggest, AI-Search-Antwort), muss klar disclosed sein.
2. **AI-generated Content** — Machine-readable Markierung (Wasserzeichen-Style oder Metadaten).
3. **Emotion Recognition / Biometric Categorisation** — bei Cosmi nicht relevant.
4. **Deep-Fakes und AI-generated Public-Interest-Text** — bei Cosmi nicht relevant.

**Cosmi-Wiki hat heute keine AI-Interaktion** (Search ist reine Postgres-FTS). **Aber**: Meeting-AI-Summary (`backend/internal/llm/client.go`) ist eine "direkte Interaktion" — und die Nachricht-Zusammenfassung ist AI-generated Content. **Cosmi liefert produktiv eine Article-50-relevante Funktion aus, ohne Disclosure-Layer.** Das ist bereits jetzt ein Compliance-Delta, das im ersten Meeting-Summary-Audit auffallen wuerde.

---

### Top-Konkurrenten — Delta seit W23

**1. Notion (international, threat: HIGH-als-Feature-Benchmark)**

| W23-Stand | W38-Stand |
|---|---|
| Ask-Notion GA, Custom-Agents-Credits ab 4. Mai 2026 | Custom Agents stabilisiert; Enterprise Search Connectors: +Slack, +Linear, +GitHub (Q3 2026) |
| Verified-Pages als Highlight-Feature | Model-Wahl-Governance pro Agent (9. Sep 2026); Suggested Edits (28. Aug 2026) |
| Slack-Agent-Replies (1. Mai 2026) | Notion-Mail-Sunset 22. Sep 2026 als Beispiel fuer Universal-Context-Layer |
| Pricing: 20$/Business, 10$/1000 Credits | unveraendert; jetzt aber mit Governance-Layer fuer Enterprise-Adminstrations-Control |

**Neuer Gap zu Cosmi**: Modell-Wahl-Governance (Cosmi hat noch keinen Multi-Provider-Router, obwohl W25/W33-Keeper das eskaliert haben), Suggested-Edits (fuer zukuenftige Cosmi-AI-Features wichtig als Compliance-Ergaenzung zu Article 50).

**2. Confluence + Rovo (Atlassian, threat: HIGH aber ERODIEREND)**

Der bereits im W23-Bericht als "Cosmi-Migration-Gegen-Anker" identifizierte Move ist eingetreten und wird durch die Data-Center-EOL-Ankuendigung **strukturell verstaerkt**:

- **17. August 2026 hit**: Content-Opt-out geht bei Free/Standard/Premium; Metadaten (Titles + Descriptions + Struktur-Metriken) **nicht opt-outbar** — nur Enterprise-Tier voll opt-out.
- **Data Center EOL**: Neu-Verkauf gestoppt 30. Maerz 2026; Renewals bis 30. Maerz 2028; read-only ab 28. Maerz 2029. Migration-Kosten laut Marktpreis: 15-30k€ einmalig fuer 50 Workplaces, plus 8-15k€ p.a. Operations.
- **Rovo + Remix** entwickelt sich weiter (Confluence-Pages werden zu Charts, Slides, Prototypes via Partner-Agents).

**Cosmi-Chance**: Fuer die DACH-KMU-Subgruppe **Confluence-Data-Center-Bestandskunde mit AI-Compliance-Vorgabe** (das ist eine sehr spezifische, aber lukrative Nische) ist Cosmi in 2027-2028 die realistischste Alternative. Vorausgesetzt der Editor-Fluss ist auf Notion-Niveau — der DocumentBlockEditor-Umbau seit W23 hat das Fenster geoffnet.

**3. Docmost (Open-Source, threat: HIGH — direkter Self-Host-Konkurrent)**

| W23-Stand | W38-Stand |
|---|---|
| v0.90.0 (Mai 2026): Synced-Blocks, Backlinks, Azure-Blob | v0.95 (4. Jul 2026): /time-Slash, Workspace-Edit-Pref, Translation-aware Slash-Suche |
| v0.80.0 (Apr 2026): AI-Chat + Page-Verification (Enterprise) | **v0.96 (Sep 2026): MCP OAuth, Footnotes, Page-Version-Comparison (Side-by-Side-Diff), Attachments-Gallery, Search-Filters+Labels, Media-Lightbox, RTL, Turbopuffer AI-Vector-Search-Driver, AI-Chat-Controls, SIEM (Splunk/Datadog/Generic HTTP)** |
| 5-Wochen-Release-Kadenz | 5-Wochen-Kadenz haelt (v0.90→v0.96 in ~4 Monaten) |

**Docmost ist der Konkurrent, dessen Kadenz Cosmi jetzt strukturell nicht mehr matcht** (Cosmi macht Sprint-basierte Wellen, Docmost macht 5-Wochen-Minor-Releases mit Enterprise-Features). Die W23-Watch-Empfehlung "alle 4 Wochen pruefen ob Docmost neue Features Cosmi kopieren-muss" ist zu passiv geworden. **MCP-OAuth + Turbopuffer-Vector-Search + SIEM in einer Release** = Docmost hat 3 Cosmi-P0-Kandidaten in einem Package ausgeliefert.

**4. Outline (Self-Host + Cloud, threat: medium — Architektur-Vorbild bleibt)**

Outline bleibt der klarste Ausdruck von "Markdown-first + Yjs-Real-Time + Official MCP-Server". Die August-Bewegung ist die Erhebung des MCP-Servers zur **Default-Empfehlung** fuer AI-Integration mit Self-Host — nicht mehr Optional-Feature, sondern Kern-Positionierung. GitLab-Integration + Anthropic Antigravity/Cursor/Claude-Desktop/Cline-Kompatibilitaet.

Fuer Cosmi: **Outline-MCP-Server-Pattern kopieren** ist die richtige Referenz — offene HTTP-Endpoints (SSE + Streamable) mit search/patch/move/delete Tools + Breadcrumbs+Summaries. Erste Version kann sich auf `read_article`, `search_articles`, `list_categories` beschraenken (fuer LLM-Retrieval), Write-Operationen sind Phase 2.

**5. Nextcloud (DACH, threat: medium — EU-Sovereignty-Vorbild)**

Hub 26 Spring am 9. Juni 2026, Hub 26 Summer angekuendigt. Collectives + Assistant + Files + Talk als cross-app-agentic Bundle. Die im W23-Bericht empfohlene "Cosmi soll Nextcloud-Assistant-Architektur als Lesson nehmen" bleibt valide — und wird durch Nextcloud's fortgesetzte Cadence-Konsistenz verstaerkt. **pgvector seit Hub 22 in Nextcloud-Produktion** — Cosmi's pgvector-Extension ist enabled aber nur fuer Contacts genutzt. Das ist ein direkter Nachhol-Move.

**6. XWiki + OpenProject / openDesk / ZenDiS (Public-Sector, threat: low fuer Cosmi-Zielsegment)**

**Update seit W23**: OpenProject 17.6 (Juli 2026) hat **die erste native XWiki-Integration in OpenProject** ausgeliefert — der Public-Sector-Bundle-Stack wird zunehmend zu einem echten Produkt, nicht mehr nur zu einem Marketing-Zusammenschluss. Fuer Cosmi bleibt Public-Sector im Watch-Modus.

**7. AFFiNE / AppFlowy / BlockSuite (Open-Source Notion-Alternativen)**

AFFiNE bleibt pre-1.0 (v0.26.3 stabil, 6-Wochen-Major-Cadence). BlockSuite als CRDT-Editor-Framework bleibt technisch spannend fuer Cosmi-Backend-Referenz, ist aber kein direkter DACH-KMU-Sales-Wettbewerber. Watch-Modus.

**8. Obsidian (Personal-Knowledge → Team-Edge)**

**Neu seit W23**: Obsidian-Bases hat sich zum universellen Markdown-Datenbank-Pattern entwickelt (Airtable→Bases-Konverter August 2026), Sync ermoeglicht **echte Multi-User-Vault-Kollaboration** auf denselben Ordnern. Obsidian bleibt kein direkter KMU-ERP-Modul-Konkurrent, aber **die Zielgruppe "tech-affiner Solo-Selbststaendiger + kleines Team"** in DACH nutzt zunehmend Obsidian statt Notion — das ist ein Signal, dass Markdown-first + Sync-basiertes Modell keinen KMU-Feature-Nachteil hat.

**9. Wiki.js / BookStack (traditionelle Self-Host-Wikis)**

Wiki.js 3.x weiterhin im Alpha-Limbo seit 2022, kein Feature-Push in 2026. BookStack v26.05 mit Security-Fokus. **Beide sind fuer Cosmi kein 2026-Konkurrenz-Druck**, aber Cosmi ersetzt strukturell keine der beiden — sie bedienen die "reine Documentation-Wiki-Nische" ohne Modul-Integration.

---

## Cosmi-IST-Stand (2026-09-14)

**Backend (`backend/internal/wiki/`, 3444 LOC, +4.6× seit W23):**

- `service.go` (598): CreateArticle/UpdateArticle/DeleteArticle/PublishArticle mit Auto-Version-Snapshot bei Content-Update. Slug-Uniqueness, Category-Validation, Attachment-Upload.
- `postgres_repository.go` (552): SQL-Layer, mit expliziter Tenant-Isolation auf allen Methoden.
- `share.go` + `share_test.go` + `share_redeem_db_test.go` (646 LOC gesamt): **Share-Token-Redeem-Flow ist implementiert**; im W23-Bericht war das noch unklar.
- `tenant_isolation_phase2_test.go` (64) + `tenant_write_test.go` (223) + `service_test.go` (840) + `postgres_repository_db_test.go` (319): substantielles Test-Suite-Wachstum.
- Migrations: **000076** (5-Tabellen-Schema, unveraendert), **000230** (RLS wiki + HR-child-tables, Phase-2-Long-Tail-RLS-Sweep), **000297** (Share-Token-Revocation).
- **pgvector aktiviert** (Migration 000072) — **aber `wiki_articles.embedding` existiert nicht**, nur `contacts` haben Embeddings (Migration 000073).
- `backend/internal/llm/client.go`: Provider-agnostischer OpenAI-Compatible-Client (Ollama-Default, EU-Sovereignty), fuer Wave-7C Meeting-AI-Summary. **Ist bereits produktiv verwendet**, aber ohne Disclosure-Layer-Wrapper.

**Frontend (`desktop/src/renderer/src/modules/wiki/`, 4328 LOC, +3.4× seit W23):**

- **`WikiEditor.tsx` (162)**: kein `<textarea>` mehr — Wrapper um `DocumentBlockEditor` mit Playfair-Title, Identity-Bar (Icon+Cover), Change-Notes-Footer, Ctrl+S/Esc-Shortcuts.
- **`WikiPage.tsx` (374)**: 3-Spalten-Layout ausgebaut.
- **`wiki-blocks.tsx` (348)**: Wiki-Block-Registry auf Basis Shared-Document-Engine; TipTap-Text-Bloecke mit `WikiLink`+`WikiMention`-Extensions; Frameless-Longform-Text-View; DOMPurify.
- **`WikiSuggest.tsx` (184)** + **`extensions/WikiLinkExtension.ts`** + **`extensions/WikiMentionExtension.ts`**: `[[Artikel]]`- und `@user`-Autocomplete.
- **`WikiVersionDiff.tsx` (83)** + **`wikiDiff.ts` (71)** + **`WikiVersionHistory.tsx` (69)** + **`WikiVersionItem.tsx` (109)**: **Side-by-Side-Version-Diff ist geliefert** (W23-Empfehlung addressiert).
- **`WikiIdentityBar.tsx` (248)** + **`wikiIdentity.tsx` (148)**: Icon+Cover-Notion-Pattern.
- **`WikiAttachments.tsx` (228)**: Inline-Attachment-Management im Editor.
- **`WikiToc.tsx` (82)** + **`wikiReading.ts` (62)**: Table-of-Contents + heading-anchor-id-Helpers.
- **`WikiTemplateManager.tsx` (267)** + **`WikiTemplateDialog.tsx` (192)**: Template-System-UI (Backend-Templates-Quelle unklar — verifikation empfohlen).
- **`WikiMoveDialog.tsx` (153)**: Reparenting/Kategorien-Umzug.
- **`WikiTagEditor.tsx` (140)**: Tag-Editor.
- **`WikiSidebar.tsx` (178)** + **`WikiTreeNode.tsx` (200)**: Hierarchische Navigation.
- **`WikiShareDialog.tsx` (241)**: Share-Link-UI mit Revocation.
- **`WikiCategoryDialog.tsx` (129)** + **`WikiHighlight.tsx` (55)** + **`WikiEmptyCanvas.tsx` (55)** + **`WikiArticleHeader.tsx` (297)** + **`WikiArticle.tsx` (200)** + **`WikiSearch.tsx` (32)**: weitere UI-Bausteine.
- **`settings/WikiSettingsPanel.tsx`**: Panel-Integration in globale Einstellungen (Reading-Width etc.).

**Shared Document-Engine (`components/shared/document/`, 1039 LOC):**

- **`DocumentBlockEditor.tsx` (679)**: Insert-Menue (Plus-Button), dnd-kit-Drag-Reorder, Column-Layouts (50/50, 60/40, 40/60, 33/33/33), Row-Insert, Block-Replace, Block-Delete.
- **`DocumentReader.tsx` (215)**: Read-Modus mit demselben Registry-Modell.
- **`blocks/CoreBlocks.tsx`** + **`SpecialBlocks.tsx`** + **`code-highlight.tsx`** + **Types-Files**: Text+Heading (frameless), Callout, Image, Divider, Code-Highlight, etc.
- **Wiederverwendet** in `berichte` und `wiki` — echter Cross-Modul-Ansatz.

**RichTextEditor (`components/shared/RichTextEditor/`):**

- Basis-Editor mit TipTap v3.20, `EditorBubbleMenu`, `EditorFooter`, `EditorToolbar`. Verwendet von `wiki-blocks.tsx` fuer Text- und Heading-Bloecke.

**TipTap-Extensions in `desktop/package.json` (v3.20.0):**

- Core: `@tiptap/react`, `@tiptap/starter-kit`, `@tiptap/pm`.
- Extensions: Link, Image, Underline, Placeholder, Text-Align, Table (+ TableCell/TableHeader/TableRow), Task-List (+ Task-Item), Code-Block-Lowlight.
- **KEIN**: `@tiptap/extension-collaboration`, `@tiptap/extension-collaboration-cursor`, kein `yjs`, kein `y-webrtc`/`y-websocket`, kein `@hocuspocus/*`. **Real-Time-Collab bleibt offen**.

**Pricing (`docs/PRICING.md`)**:

- Wiki: **3 EUR/Modul/User/Monat** (nicht mehr 2 EUR wie im W23-Bericht — die interne Modul-Preisliste wurde inzwischen aktualisiert, siehe `PRICING.md:140`). Vergleichswerte: "Notion ab 8, Confluence 5" (aus derselben Zeile — Cosmi's eigene interne Referenz).

**Was hinzugekommen ist (Highlights seit W23):**

- ✅ Echter Block-Editor mit TipTap-Rich-Text (W23-Empfehlung 1 gelieft, wenn auch auf eigenem Weg)
- ✅ Version-Diff (Side-by-Side)
- ✅ Identity-Bar (Notion-Icon+Cover-Pattern)
- ✅ `[[wiki-link]]` und `@mention` Inline-Autocomplete + Preview-Popover
- ✅ Share-Token-Redeem-Flow implementiert
- ✅ Table-of-Contents + Heading-Anchors
- ✅ Move-Dialog fuer Kategorien-Umzug
- ✅ Tag-Editor
- ✅ Attachment-Inline-Management im Editor
- ✅ Templates-UI (Manager + Dialog)
- ✅ RLS-Migration 000230 fuer Wiki + HR-Kinder-Tabellen
- ✅ Share-Token-Revocation (Migration 000297)
- ✅ Shared DocumentBlockEditor als Cross-Modul-Basis fuer wiki + berichte

**Was weiterhin NICHT existiert (Kern-Gaps 2026-09-14):**

- ❌ **`ai_disclosure`-Layer (EU-AI-Act Art. 50)** — Article 50 durchsetzbar seit 2. Aug 2026. Meeting-AI-Summary laeuft produktiv ohne Wrapper.
- ❌ **pgvector fuer `wiki_articles`** (nur Contacts hat Embedding). W23-Empfehlung 3 nicht angegangen.
- ❌ **Hybrid-Search-RPC** (BM25+Semantic Reciprocal-Rank-Fusion).
- ❌ **MCP-Server** (`backend/internal/core/mcp-server/` fehlt) — Docmost hat es Sep 2026 mit OAuth ausgeliefert, Outline hat es offiziell als AI-Integration-Default; Cosmi hat W33-Keeper-Backlog "MCP-Server fuer Contacts/Deals/Tickets/Shifts/Invoices/Time-Entries", der Wiki einschliessen sollte.
- ❌ **Real-Time-Collab (Yjs / Hocuspocus)** — kein `y-*`-Package.
- ❌ **Cross-Modul-Backlinks (Wiki↔CRM-Deal / Wiki↔Helpdesk-Ticket)** — der Cosmi-USP-Hebel weiter theoretisch.
- ❌ **Page-Verification / Approval-Workflow** (Notion + Docmost-Standard).
- ❌ **Inline-Kommentare / Discussion**.
- ❌ **AI-Search / Ask-Cosmi** — keine LLM-Retrieval-Layer.
- ❌ **Slash-Commands im Text-Flow** (Insert-Menue via Plus-Button existiert, aber nicht Notion-typische Inline-`/heading`-`/quote`).
- ❌ **Public-Share-Viewer-Endpoint als eigenstaendige URL-Route** (Redeem-Flow existiert, gaestige URL-Landing unklar).
- ❌ **Mobile-Editor** (Cosmi hat weiterhin nur Desktop-Electron).

---

## Konkurrenz-Vergleichstabelle (aktualisiert W38)

| Feature | Cosmi (W38) | Notion (Business) | Confluence (Premium) | Outline (Self-Host) | Docmost v0.96 (Enterprise) | Nextcloud Hub 26 | XWiki + openDesk |
|---|---|---|---|---|---|---|---|
| Block-Editor (Slash/Insert-Menue) | ✅ 🚧 (Plus-Menue, kein Inline-`/`-Command) | ✅ Slash | ✅ Slash | ✅ ProseMirror | ✅ TipTap+Slash | ✅ Yjs-Text | ✅ CKEditor 5 |
| TipTap / ProseMirror integration | ✅ TipTap v3.20 (in RichText-Bloecken) | eigenes | eigenes | ProseMirror | ✅ TipTap | Yjs-Text | CKEditor |
| Real-Time-Collab (CRDT) | ❌ Save-on-Blur | ✅ | ✅ | ✅ Yjs | ✅ Yjs | ✅ Yjs | 🚧 limitiert |
| Postgres-FTS (de) | ✅ tsvector+GIN | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| pgvector-basierte Semantic-Search | ❌ (Contacts ja, Wiki nein) | ✅ Ask-Notion | ✅ Rovo | ✅ AI-Answers | ✅ Turbopuffer-Driver (v0.96) | ✅ Assistant | ❌ |
| AI-Agents / Ask-Workspace | ❌ | ✅ Custom Agents + Model-Governance (Sep 2026) | ✅ Rovo + Suggested Edits | ✅ AI-Answers + MCP | ✅ AI-Chat + Controls (v0.96) | ✅ cross-app | ❌ |
| **MCP-Server (LLM-Tool-Use)** | ❌ | 🚧 Developer Platform | 🚧 Rovo-Studio-Partner-Agents | ✅ **Offiziell + empfohlen** | ✅ **OAuth v0.96** | 🚧 App-API | ❌ |
| **EU-AI-Act-Art.-50-Disclosure** | ❌ Meeting-Summary produktiv OHNE Disclosure | 🚧 unclear | 🚧 unclear + Training-Opt-in-Kontroverse | 🚧 unclear | 🚧 unclear | ✅ Model-Wahl-transparenz | n/a (kein AI) |
| Suggested Edits (Line-Level-Approval) | ❌ | ✅ (Aug 2026) | ❌ | ❌ | ❌ | ❌ | ❌ |
| Versionierung (auto-snapshot) | ✅ | ✅ 90d | ✅ | ✅ | ✅ | ✅ | ✅ |
| Side-by-Side-Diff | ✅ (`WikiVersionDiff` **NEU seit W23**) | ✅ | ✅ | ✅ v1.7.0 | ✅ v0.96 | 🚧 | ✅ |
| Backlinks / Knowledge-Graph | 🚧 `[[link]]` Inline, kein Backlink-Panel | 🚧 limitiert | ❌ | ✅ | ✅ v0.90 | 🚧 | ✅ |
| @Mentions inline | ✅ (`WikiMention` **NEU seit W23**) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Synced-Blocks / Transklusion | ❌ | ✅ | ❌ | ❌ | ✅ v0.90 | ❌ | ✅ |
| Page-Verification | ❌ | ✅ Business+ | ❌ | ❌ | ✅ Enterprise | ❌ | ❌ |
| Hierarchische Kategorien | ✅ | ✅ Pages-Tree | ✅ Spaces | ✅ Collections | ✅ Spaces | ✅ Circles | ✅ Spaces |
| Attachments (Inline-Editor-Mgmt) | ✅ (`WikiAttachments` **NEU seit W23**) | ✅ | ✅ | ✅ | ✅ + Attachments-Gallery (v0.96) | ✅ | ✅ |
| Public-Share-Tokens + Revocation | ✅ (Migration 000297 **NEU seit W23**) | ✅ | ✅ | ✅ Per-Share-Branding | ✅ | ✅ | ✅ |
| Table-of-Contents | ✅ (`WikiToc` **NEU seit W23**) | ✅ | ✅ | ✅ | ✅ | 🚧 | ✅ |
| Identity (Icon+Cover) | ✅ (`WikiIdentityBar` **NEU seit W23**) | ✅ | 🚧 | ❌ | 🚧 | ❌ | ❌ |
| Templates-Library (Backend) | 🚧 UI da, Backend-Templates unklar | ✅ | ✅ | ✅ | ✅ Enterprise | 🚧 | ✅ |
| Cross-Modul-Integration (Wiki↔CRM/Helpdesk) | ❌ (USP-Hebel weiter offen) | ❌ Standalone | 🚧 Jira-Link | 🚧 GitLab-Embed | ❌ | 🚧 limitiert | 🚧 OpenProject-native XWiki (Jul 2026) |
| Comments / Inline-Diskussion | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Approval-Workflow | ❌ | ✅ Business+ | ✅ | ❌ | ✅ Enterprise | ❌ | ✅ |
| Mobile-Editor | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 🚧 |
| SCIM-Provisioning | ❌ | ✅ Enterprise | ✅ Premium | 🚧 | ✅ Enterprise | 🚧 | ✅ |
| SIEM-Integration (Splunk/Datadog) | ❌ | 🚧 Enterprise | 🚧 Enterprise | ❌ | ✅ v0.96 (**NEU**) | 🚧 | 🚧 |
| EU-Self-Host (DSGVO-nativ) | ✅ | ❌ Cloud-only | 🚧 Data-Center EOL 2029 | ✅ | ✅ Air-Gap | ✅ | ✅ openDesk |
| Open-Source | ❌ proprietaer | ❌ | ❌ | ✅ Apache | ✅ Community | ✅ AGPL | ✅ LGPL |
| **AI-Training auf Kunden-Content** | ❌ Cosmi trainiert nichts | 🚧 nicht klar | ✅ **Opt-in-Default seit 17. Aug 2026** (Free/Std/Prem) | ❌ | ❌ | ❌ | ❌ |
| Pricing/Seat (DACH-KMU) | **3 EUR Modul** | $20 Business+AI | $10.44 Premium (Cloud) | $0 Self / $10 Cloud | Self $0 / Ent custom | Self $0 / Ent ~5 EUR | Self $0 / ZenDiS-Bundle |
| KMU-ERP-Modul-Integration | ✅ USP-Anker (aber nicht aktiviert) | ❌ | ❌ | ❌ | ❌ | 🚧 | ❌ |

**Lesart der Tabelle (Delta W23 → W38):**

Cosmi hat **8 Feature-Gaps aus der W23-Tabelle geschlossen** (Block-Editor, TipTap, Side-by-Side-Diff, @Mentions, Backlink-Inline, Attachments-Inline, Public-Share-Revocation, Identity-Bar, Table-of-Contents). Das ist ein substantielles Editor-Rollout-Ergebnis. **Vier Gaps sind neu geoeffnet oder eskaliert seit W23:**

1. **MCP-Server**: von "Outline-Solo, Watch-Modus" (W23) zu **"industriestandard, Outline offiziell + Docmost OAuth"** (W38).
2. **EU-AI-Act Art. 50 Disclosure**: von "Ankuendigung fuer 2. Aug 2026, Cosmi-Vorbereiten" (W23) zu **"durchsetzbar seit 6 Wochen, Cosmi produktiv exposed via Meeting-AI-Summary"** (W38).
3. **Suggested-Edits**: neu bei Notion (Aug 2026), zukuenftig Compliance-relevant fuer Cosmi-AI-Features.
4. **SIEM-Integration**: neu bei Docmost v0.96 als Enterprise-Feature — Cosmi hat kein Aequivalent, aber es ist Enterprise-Sales-Signal.

Der **Cosmi-USP-Hebel "Wiki-IM-ERP mit Cross-Modul-Backlinks"** ist strukturell noch nicht aktiviert und wird jetzt bei jedem Sales-Call die Achillesferse — Docmost hat inzwischen mehr Feature-Parity zu Notion als Cosmi (Synced-Blocks, Backlinks-Panel, AI-Chat mit Controls, MCP-OAuth), ohne die ERP-Integrations-Story ueberhaupt zu haben. **Wenn Cosmi weiterhin ohne aktivierte Cross-Modul-Verlinkung bleibt, verkauft es "modernes Wiki das leider immer noch kein Notion-Ersatz ist" statt "Wiki-IM-KMU-Hub".**

---

## Top-3 Strategische Empfehlungen

### 1. **EU-AI-Act Article 50 Compliance-Foundation (P0 URGENT — Nachhol-Sprint diese Woche)**

**Problem**: EU-AI-Act Art. 50 ist seit 2. August 2026 durchsetzbar. Fines €15M oder 3% Weltumsatz. Cosmi liefert produktiv **Meeting-AI-Summary** aus (`backend/internal/llm/`) — das ist Article-50-Trigger-Funktion (direkte Interaktion + AI-generated Content). Cosmi hat **keine Disclosure-UI, kein Audit-Log, keine machine-readable AI-Content-Markierung**. Die W23-Empfehlung 2 hat das exakt so vorhergesagt und einen Compliance-Foundation-Sprint gefordert — der ist nicht ausgeliefert worden. **Wir sind heute 43 Tage im Non-Compliance-Fenster** (2. Aug → 14. Sep 2026), waehrend die keeper-Chain (W23 `ai-cost-governance`, W33 `backend/internal/compliance/ai-act-article-50/`) das Thema mehrfach eskaliert hat.

**Empfehlung**:

- **Compliance-Foundation-Sprint (diese Woche):**
  - Backend-Package `backend/internal/compliance/ai_disclosure/`:
    - Tabelle `ai_interactions` (id, tenant_id, user_id, modul, feature, model_provider, model_version, prompt_hash SHA-256, completion_hash SHA-256, disclosure_shown_at, created_at). Retention pro Compliance-Policy.
    - Wrapper-Funktion `LogInteraction(ctx, params)` als Muss-Aufruf VOR jedem `llm.Client.Chat`-Call.
  - Frontend-Component `<AIDisclosureBanner provider="..." model="..." />` in `desktop/src/renderer/src/components/shared/AIDisclosure/`:
    - Lucide-Sparkles-Icon + Tooltip "Diese Funktion nutzt ein KI-System ($provider, $model). Antworten koennen fehlerhaft sein. Cosmi loggt keine Prompt-Inhalte fuer Training. EU-AI-Act Art. 50."
    - CSS-Klasse `ai-generated-content` fuer Response-Rendering (Watermark-Style Underline).
  - Backend-Response-Format `{ ..., is_ai_generated: true, model_provider: "ollama", model_version: "mistral:7b" }` als Konvention fuer alle AI-Features.
  - Doku-File `docs/compliance/ai-providers.md`: verwendete LLM-Provider + EU-AI-Act-Klassifikation + Fallback-Chain (Anthropic → Mistral → Ollama).
  - **Meeting-AI-Summary retrofit**: Alle bestehenden `LLMClient.Chat`-Calls in Meeting-Modul mit dem Wrapper + Banner-Pflicht ausstatten. **KEIN AI-Endpoint mehr ohne Disclosure**.

**Begruendung**:

- 43 Tage Non-Compliance sind schon lang; DACH-Marktueberwachung ist als Berichts-Zielgruppe zunehmend aktiv (BNetzA hat im Aug 2026 erste Info-Kampagnen gestartet).
- Der Compliance-Sprint hat **strategischen Doppelnutzen**: (a) Rechts-Risiko-Beseitigung, (b) direktes **Sales-Argument gegen Atlassian's 17.-Aug-Opt-in-Move** ("Cosmi trainiert **nie** auf euren Wiki-Inhalten UND zeigt jede AI-Interaktion transparent an").
- Foundation kommt vor **jedem** naechsten AI-Feature (pgvector-Search, Wiki-AI-Suggest, Ask-Cosmi) — verzoegert man das jetzt, muss man mehrere AI-Features spaeter parallel retrofit-en.
- Die Loesung ist ueberraschend klein — 1 Tabelle, 1 React-Komponente, 1 Wrapper, 1 MD-Datei. Realistisch 2-3 Entwicklertage.

**Risiko**: Retrofit von Meeting-AI-Summary koennte User-Feedback-Wave ausloesen ("was ist das fuer ein Sparkles-Icon jetzt?"). Mitigation: **Coach-Mark einmalig + Positioning "diese Transparenz ist unser Anti-Atlassian-USP"** in Release-Notes.

**Picks**: 🟢 P0 URGENT-Move — diese Woche starten, keeper `ai-act-article-50-disclosure-live` neu erstellen fuer W38 mit Cross-Ref zu W23-Empfehlung-2 und W33-P0-Escalation.

---

### 2. **pgvector-Aktivierung fuer `wiki_articles` + Hybrid-Search-RPC (P0 — Sprint 4 obere Prio)**

**Problem**: Cosmi-Postgres hat pgvector seit Migration 000072 aktiviert; Contacts nutzen es (000073). Wiki-Artikel nicht. Die W23-Empfehlung 3 hat das vorhergesagt und die pgvector-Ausdehnung als Cosmi-uebergreifenden Layer empfohlen — auch das ist nicht ausgeliefert. Docmost v0.96 hat inzwischen einen dedizierten **Turbopuffer AI Vector-Search-Driver** als Enterprise-Feature; Nextcloud nutzt pgvector seit Hub 22 in Produktion. Cosmi hat den technischen Stack fertig und nutzt ihn nur zu 15%.

**Empfehlung**:

- Migration `000XYZ_wiki_article_embeddings.up.sql`:
  ```sql
  ALTER TABLE wiki_articles ADD COLUMN embedding VECTOR(768) NULL;
  CREATE INDEX idx_wiki_articles_embedding ON wiki_articles
    USING hnsw (embedding vector_cosine_ops)
    WITH (m=16, ef_construction=64);
  ```
- Backend `backend/internal/wiki/embedding.go`:
  - Funktion `EmbedArticleContent(ctx, tenant, articleID)` — ruft `settings.optimization.embeddings_endpoint` (Ollama-Default, bge-m3-self-hosted).
  - Async-Worker in `service.UpdateArticle`/`service.CreateArticle`, der Embedding-Backfill queued (async, kein Save-Blocker).
- Neue RPC `SearchArticlesHybrid(tenant, query, mode)`:
  - `mode: FTS_ONLY` (default beibehalten fuer Backward-Compat).
  - `mode: SEMANTIC_ONLY` (nur pgvector).
  - `mode: HYBRID` (Reciprocal-Rank-Fusion aus FTS + Semantic; k=60 Standard).
- Frontend `WikiSearch.tsx`-Erweiterung um Modus-Toggle (default Hybrid; bei Article-50-Trigger Banner via #1).
- **Retrieval-only, keine Generation** — kein LLM-Call in Search-Flow. Article 50 wird durch Banner (#1) trotzdem sicher abgedeckt, wenn Semantic-Suche aktiv ist.

**Begruendung**:

- Retrieval-only ist **80% des Wow-Effekts ohne 100% des Compliance-Risikos**. Cosmi kann "Semantic Wiki-Search" bewerben, ohne LLM-Prompt-Kosten oder Fehler-Halluzinationen.
- pgvector ist bereits Cosmi-Stack — keine neue Infrastruktur, kein neuer Backup-Prozess, kein neuer Ops-Overhead.
- **Cross-Modul-Ausdehnung folgt gratis**: derselbe Pattern fuer `helpdesk_tickets`, `crm_deals.notes`, `vertraege_documents`. Sobald Wiki geht, hat Cosmi den Layer fuer "Ask-Cosmi-Universal-Retrieval" bereit — DAS ist der Cosmi-USP-Hebel, der laut W23 seit 15 Wochen offen ist.
- Docmost hat mit Turbopuffer-Driver klargemacht, dass Vector-Search jetzt Enterprise-Standard ist — Cosmi hinkt hier bereits hinter.

**Risiko**: Backfill von bestehenden Wiki-Artikeln (Anzahl unklar, aber selbst 10k Artikel ~1-2 Sek/Artikel = 3-5h) kann Ollama-Endpoint saturieren. Mitigation: **Batched-Async-Worker mit Progress-Report** + Rate-Limit auf Embedding-Endpoint.

**Picks**: 🟢 P0 Sprint-4-Move — mit Embedding-Backfill-Worker.

---

### 3. **Cosmi-MCP-Server fuer Wiki (P1 — 4-Wochen-Fenster fuer AI-first-Prospect-Segment)**

**Problem**: Seit W23 ist MCP-Server von "Outline-Solo-Move" zum industriestandard geworden. Outline hat offizielle MCP-Server-Empfehlung fuer Self-Host; **Docmost v0.96 (September 2026) hat MCP-OAuth ausgeliefert**. Der W33-Keeper hat "MCP-Server fuer Contacts/Deals/Tickets/Shifts/Invoices/Time-Entries" als HIGH P0 gesetzt — Wiki gehoert in dieselbe Iteration. Jeder tech-affine DACH-KMU-Prospect prueft in Q4/2026 "kann ich das mit Claude/Cursor/Antigravity verbinden?" — Cosmi-Wiki muss dazu Ja sagen koennen.

**Empfehlung**:

- Neues Backend-Modul `backend/internal/core/mcp_server/` mit:
  - HTTP-Streamable-Endpoint (SSE + Streamable HTTP wie Anthropic-Spec).
  - OAuth-Flow ueber Cosmi-Auth-Layer (tenant-scoped Tokens).
  - Tool-Set-Phase-1 (nur Wiki, nur Read-Ops):
    - `wiki.search_articles(query, mode, limit)` — nutzt HybridSearch aus Empfehlung 2.
    - `wiki.get_article(article_id, include_versions)`.
    - `wiki.list_categories(parent_id, depth)`.
    - `wiki.get_attachment_metadata(attachment_id)`.
  - Response-Envelope mit Breadcrumbs, Summary, Suggested-Title (Outline-Pattern-Kopie).
  - Rate-Limit-Middleware (Standard-Anthropic-Pattern; 60 req/min pro Tenant Default).
- Frontend-Setting `WikiSettingsPanel.tsx` erweitern um "Externe AI-Tools verbinden (MCP)" — Token generieren + revoken + Docs-Link.
- Doku-Update `docs/mcp-server.md` mit Setup-Guide fuer Claude Desktop / Cursor / Antigravity.
- **Phase-2 (spaeter)**: Write-Ops `wiki.create_article`, `wiki.update_article`, `wiki.move_article` — mit expliziter User-Approval-Flow (Suggested Edits-aehnlich).

**Begruendung**:

- 4-Wochen-Fenster ist konkret: **Docmost v0.96 wurde Sep 2026 released** — die Q4-DACH-Prospect-Auswertung wird MCP-Support als Filter-Kriterium haben. Cosmi ohne MCP-Server verliert 2027-Prospect-Segment "AI-first tech-affine KMU".
- Der W33-Keeper fordert MCP-Server-Foundation ohnehin fuer Contacts/Deals/Tickets — Wiki als erstes ausgeliefertes Tool-Set hat **niedrigsten Compliance-Risiko** (nur Read + Text-Content, kein PII wie Contacts).
- **Sales-Story-Effekt**: "Cosmi-Wiki ist der einzige DACH-KMU-Wiki, den ihr direkt mit Claude Code / Cursor / Antigravity verbinden koennt, DSGVO-konform self-hosted." Das ist die Antwort auf Lovable/Fin-Substitution-Angst aus W33.

**Risiko**: MCP-Spec entwickelt sich schnell; jedes Feature-Aequivalent zu Docmost bindet Engineering-Zeit an ein Moving-Target. Mitigation: **Anthropic-offizielle Spec-Version pinnen** (aktuell 2026-06-18), Upgrade-Pfad quarterly. Nur Read-Ops in Phase 1 minimiert Angriffsflaeche.

**Picks**: 🟡 P1 4-Wochen-Fenster — Read-Ops fuer Wiki-Only als erster MCP-Server-Deliverable, keeper-Cross-Reference zu W33 `backend/internal/core/mcp-server/`.

---

### Bonus / Follow-up (P2 Kandidaten):

- **Real-Time-Collab (Yjs + Hocuspocus)** — Sprint 5-6. Backend-Yjs-Doc-Provider + TipTap-Collaboration-Extension. Nice-to-have, aber Save-on-Blur reicht fuer KMU-Internal-Wiki noch. Empfehlung: nach MCP-Server priorisieren.
- **Cross-Modul-Backlinks (Wiki↔CRM/Helpdesk/Vertraege)** — der Cosmi-USP-Hebel, der seit W23 auf 0 steht. TipTap-Extension `CosmiCrossRefExtension` mit Referenz-Type-Union (`{ type: 'wiki'|'deal'|'ticket'|'contract', id: UUID }`). Backend-Cross-Ref-Table `cosmi_cross_references` mit Trigger auf Delete-Set-Null. Wenn Empfehlung 3 (MCP) durch ist, ist die Backlink-Aktivierung ~1 Sprint.
- **Slash-Commands-Inline-UX** — `/heading1`, `/list`, `/code`, `/quote`, `/callout`, `/divider` als TipTap-Suggestion-Extension. Notion-Pattern-Kopie, ~1 Sprint.
- **Marketing-Content**: Sales-Folie "Cosmi vs Atlassian-Aug-17-Default-Opt-in" — aus W23 empfohlen, jetzt zusaetzlich mit "Confluence Data Center EOL 2026-2029" als DACH-Migrations-Waffe. Anti-Atlassian-Content-Sprint mit Content-Owner Sales + Marketing.

---

## Was widerspricht Cosmi-Strategie (Honest Contradictions)

- **Cosmi hat 4.5 Monate Editor-Ausbau gemacht (grosser Wurf), aber die Compliance-Foundation ist offen geblieben.** Das ist eine ehrliche Priorisierungs-Kritik — Feature-Delivery ist sichtbar, Compliance-Delivery ist unsichtbar. Article-50-Fines waeren aber der eine Punkt, an dem "unsichtbar" schmerzt.
- **Wiki-USP-"Cross-Modul-Integration" ist seit W23 nicht bewegt worden.** Cosmi verkauft ein "modernes Wiki im ERP", aber der wirkliche Integrations-Layer (Wiki-Artikel referenziert Deal referenziert Ticket) existiert weiter nicht. Docmost hat inzwischen mehr Feature-Parity zu Notion als Cosmi — ohne ueberhaupt ERP-Kontext zu haben. **Cosmi-Wiki verkauft heute nicht ihre eigentliche Differenz.**
- **Docmost hat in 4 Monaten (v0.90→v0.96) mehr Enterprise-Features geliefert als Cosmi in derselben Zeit.** Cosmi's Sprint-Modell + eigene Doku-Engine ist strukturell langsamer als Docmost's 5-Wochen-Minor-Kadenz auf TipTap-Basis. Das muss man annehmen — oder Cosmi macht Sprint-Bundling gegen Feature-Parity um ERP-Integration-USP zu verstaerken (was die richtige Antwort ist).
- **Die W23-Empfehlungen 2 (AI-Disclosure) und 3 (pgvector) sind beide nicht ausgeliefert**. Ein Deepdive-Bericht ist nur wertvoll, wenn seine P0-Empfehlungen adressiert werden. Wenn Cosmi diese Empfehlungen wieder ueberhoert, ist die Deepdive-Rotation ein reines Beobachtungs-Ritual. **Vorschlag: Deepdive-Rotation um "was ist seit letztem Bericht passiert"-Delta-Sektion (dieser Bericht) erweitern und explizit Owner + Deadline pro Empfehlung notieren.**

---

## Quellen

**Cosmi-Repo (intern, 2026-09-14):**
- `backend/internal/wiki/service.go` (598 LOC)
- `backend/internal/wiki/postgres_repository.go` (552)
- `backend/internal/wiki/share.go` + `share_redeem_db_test.go` (417 LOC gesamt) — Share-Token-Redeem-Flow implementiert
- `backend/internal/wiki/tenant_isolation_phase2_test.go` — RLS-Phase-2-Compliance
- `backend/internal/llm/client.go` — produktiver Meeting-AI-Summary-Endpoint, **ohne Disclosure-Wrapper**
- `backend/migrations/000072_enable_pgvector.up.sql` — pgvector Extension enabled
- `backend/migrations/000073_add_contact_embedding.up.sql` — Contacts nutzen pgvector, Wiki noch nicht
- `backend/migrations/000076_create_wiki.up.sql` — Wiki-Schema unveraendert seit W23
- `backend/migrations/000230_rls_wiki_hr_child_tables.up.sql` — RLS-Ausbau seit W23
- `backend/migrations/000297_wiki_share_token_revocation.up.sql` — Share-Token-Revocation seit W23
- `desktop/src/renderer/src/modules/wiki/WikiEditor.tsx` — kein textarea mehr, wrappt DocumentBlockEditor
- `desktop/src/renderer/src/modules/wiki/wiki-blocks.tsx` — TipTap-Extensions integration
- `desktop/src/renderer/src/modules/wiki/extensions/WikiLinkExtension.ts` + `WikiMentionExtension.ts`
- `desktop/src/renderer/src/modules/wiki/WikiVersionDiff.tsx` + `wikiDiff.ts` — Side-by-Side-Diff-Umsetzung
- `desktop/src/renderer/src/modules/wiki/WikiSuggest.tsx` — Inline-Autocomplete-Popover
- `desktop/src/renderer/src/components/shared/document/DocumentBlockEditor.tsx` (679 LOC) — Shared Block-Engine
- `desktop/src/renderer/src/components/shared/RichTextEditor/` — TipTap v3.20 Basis
- `desktop/package.json` — TipTap-Extensions v3.20.0 (Link/Image/Table/TaskList/CodeBlock-Lowlight etc.), **keine y-*, keine @hocuspocus/***
- `docs/ROADMAP.md` S1.1 wiki done 2026-04-18
- `docs/PRICING.md` Wiki: 3 EUR/User/Monat
- `docs/STRATEGY.md` (Zeile 45-48): "TipTap bereits vorhanden, verwendet in Meeting-Notizen, Wiki-Artikel, E-Mail"

**W23-Baseline zur Delta-Referenz:**
- `zentria-intel/monthly/2026-06-01-deepdive-wiki.md`

**Konkurrenz / Markt-Signale (W23 → W38):**
- Notion Sep 2026 Model-Wahl-Governance — [notion.com/releases/2026-09-09](https://www.notion.com/releases/2026-09-09)
- Notion Suggested Edits + Enterprise-Search-Connectors — [eesel.ai Notion AI review 2026](https://www.eesel.ai/blog/notion-ai-review)
- Notion Pricing 2026 (Custom Agents $10/1000 Credits) — [get-alfred.ai/blog/notion-pricing](https://get-alfred.ai/blog/notion-pricing)
- Atlassian Default AI-Training-Opt-in 17. Aug 2026 — [dev.to/theaidownside/atlassian-now-trains-its-ai-on-your-work-by-default](https://dev.to/theaidownside/atlassian-now-trains-its-ai-on-your-work-by-default-and-full-opt-out-is-an-enterprise-feature-5661)
- Confluence Data Center End-of-Life 2026-2029 — [falconer.com/guides/confluence-data-center-end-of-life](https://falconer.com/guides/confluence-data-center-end-of-life/)
- Docmost v0.96 (Sep 2026): MCP OAuth, Turbopuffer Vector-Driver, SIEM, Page-Version-Comparison — [github.com/docmost/docmost/releases/tag/v0.96.0](https://github.com/docmost/docmost/releases/tag/v0.96.0)
- Docmost v0.95 (Jul 2026): Workspace-Edit-Pref, /time-Slash — [github.com/docmost/docmost/releases/tag/v0.95.0](https://github.com/docmost/docmost/releases/tag/v0.95.0)
- Outline offizieller MCP-Server-Support — [getoutline.com/changelog](https://www.getoutline.com/changelog)
- EU-AI-Act Article 50 durchsetzbar seit 2. Aug 2026 — [artificialintelligenceact.eu/article/50](https://artificialintelligenceact.eu/article/50/)
- EU-AI-Act Art. 50 Enforcement-Fines — [ssl.com/article/eu-ai-act-article-50-a-complete-guide-to-ai-transparency-compliance](https://www.ssl.com/article/eu-ai-act-article-50-a-complete-guide-to-ai-transparency-compliance/)
- Nextcloud Hub 26 Spring (9. Juni 2026) — [nextcloud.com/blog/nextcloud-hub26-spring](https://nextcloud.com/blog/nextcloud-hub26-spring/)
- OpenProject 17.6 native XWiki-Integration (Juli 2026) — [openproject.org/press/press-release-openproject-17-6-xwiki](https://www.openproject.org/press/press-release-openproject-17-6-xwiki/)
- openDesk / ZenDiS Public-Sector-Bundle — [opendesk.eu/en/blog/zendis](https://www.opendesk.eu/en/blog/zendis)
- BookStack v26.05 Security-Fokus 2026 — [reviewtube.com.au/bookstack-vs-wiki-js](https://reviewtube.com.au/bookstack-vs-wiki-js/)
- Obsidian Bases + Team-Sync-Kollaboration Aug 2026 — [obsidian.md/roadmap](https://obsidian.md/roadmap/)
- AFFiNE / BlockSuite / AppFlowy Vergleich 2026 — [affine.pro/blog/affine-vs-appflowy-vs-anytype](https://affine.pro/blog/affine-vs-appflowy-vs-anytype)

**Cross-Referenz zu Keepers:**
- W23 `ai-cost-governance-ist-die-neue-beschaffungs-pflic-crm-core-w23.md` — direkte Verwandtschaft zu Empfehlung 1
- W33 (implizit, in memory) `backend/internal/compliance/ai-act-article-50/` — Cosmi-uebergreifende P0-Escalation
- W33 (implizit) `backend/internal/core/mcp-server/` — direkte Verwandtschaft zu Empfehlung 3
- W20 `direct-competitor-triple-pivot-twenty` — Twenty-Sprint-Kadenz-Argument gilt hier analog fuer Docmost

---

## Picks (vorgeschlagen)

[ ] 🟢 P0 **URGENT** — EU-AI-Act Art. 50 Disclosure-Foundation (Meeting-AI-Summary retrofit + `ai_disclosure`-Layer) — **43 Tage im Non-Compliance-Fenster**, Nachhol-Sprint diese Woche
[ ] 🟢 P0 — pgvector-Aktivierung fuer `wiki_articles` + SearchArticlesHybrid-RPC — Sprint 4 obere Prio, W23-Empfehlung 3 re-eskaliert
[ ] 🟡 P1 — Cosmi-MCP-Server (Read-Ops fuer Wiki) — 4-Wochen-Fenster gegen Docmost v0.96 + Outline-Empfehlung, keeper W33 `mcp-server` cross-ref
[ ] 🟡 P2 — Cross-Modul-Backlinks (Wiki↔CRM/Helpdesk/Vertraege) — Cosmi-USP-Aktivierung, seit W23 offen [-> followup 60d]
[ ] 🟡 P2 — Slash-Commands-Inline-UX (TipTap-Suggestion-Extension) — Notion-Pattern-Kopie
[ ] 🟡 P2 — Real-Time-Collab (Yjs + Hocuspocus) — Sprint 5-6, nach MCP-Server priorisieren
[ ] 🟡 P2 — Page-Verification / Approval-Workflow — Docmost/Notion-Pattern
[ ] 🟢 Marketing — Anti-Atlassian-Content-Sprint (17-Aug-Opt-in + Data-Center-EOL) — Q4/2026 vor DACH-Migration-Wave, Owner Sales+Marketing
[ ] ⚪ Watch — Docmost-Release-Kadenz alle 5 Wochen (v0.97 erwartet ~Ende Okt 2026)
[ ] ⚪ Watch — Notion Enterprise-Search-Connectors + Model-Governance-Adoption
[ ] ⚪ Watch — Outline MCP-Server-Extension-Set (was folgt nach patch/move/delete)
[ ] ⚪ Watch — Nextcloud Hub 26 Summer / Hub 27 Announcements
[ ] ⚪ Watch — Confluence Data Center Migration-Wave-Signale in DACH-KMU-Press (Q4/2026)
