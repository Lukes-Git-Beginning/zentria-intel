---
year: 2026
week: 23
modul: wiki
created: 2026-06-01
routine: intel-monday-deepdive
model: claude-opus-4-7
runtime_minutes: 54
tokens_input: ~285000
tokens_output: ~14200
rotation_position: 4/15
---

# Deepdive: wiki (Mo W23/2026)

> **Vierter Deepdive der Rotation.** Vorgaenger: `crm-core` (W19, 2026-05-11), `dialer` (W20, 2026-05-18), `video` (W22, 2026-05-25). Naechstes Modul gemaess Rotation: **helpdesk** (KW24, 2026-06-08). Modul-Liste in `settings.yaml` `intel-monday-deepdive.rotation_modules`.

> **Stand Cosmi-Wiki (2026-06-01):** Backend `backend/internal/wiki/` (6 Files, ~750 LOC + 22300 Test-LOC, Coverage 38.2%, **seit S1.1 done 2026-04-18**). Postgres-FTS-german mit tsvector+GIN-Index, 5 Tabellen (Articles JSONB, Categories Hierarchie, Versions, Attachments, Share-Tokens), 15 gRPC-RPCs. Frontend `desktop/src/renderer/src/modules/wiki/` (12 .tsx Files, 1284 LOC). **Strukturelle Diskrepanz: Sources-YAML beschreibt "TipTap-Block-Editor" — der WikiEditor.tsx ist faktisch ein HTML-`<textarea>` mit Tag-Insertion-Buttons** (`<strong>`, `<em>`, `<h3>`, `<ul>`, `<a>`, `<code>`). Der Backend-JSONB-Schema-Slot fuer TipTap-Content existiert, das Frontend liefert ihn nicht. Mock-Store (`useWikiStore`) noch nicht durch TanStack-Query/Backend-Calls ersetzt.

> **Leit-Signal der Woche:** Drei Bewegungen kollidieren binnen 60 Tagen (April–Mai 2026) — (a) **AI-Wiki ist Tabellenstake geworden, nicht mehr USP**: Notion-AI in Business-Tier $20/Seat (4. Mai 2026 Pflicht-Bundle), Outline-AI-Answers Standard, Docmost-AI-Chat Enterprise (April 2026), Confluence-Rovo+Remix-Beta in Open-Beta, Nextcloud-Assistant cross-app-agentic in Hub 26 (Feb 2026); (b) **EU-Sovereignty-Wiki-Stack formiert sich**: XWiki+OpenProject-Partnership in openDesk (ZenDiS) als Bundle-Procurement-Vehikel fuer DACH-Public-Sector, FOSDEM-2026-Joint-Stand; (c) **EU-AI-Act Article 50 Disclosure-Pflicht ab 2. August 2026** trifft jeden Wiki-AI-Bot, jeden AI-Assistant, jeden AI-Suggest-Snippet — Cosmi hat heute weder AI-Wiki-Features noch eine Disclosure-Schicht, das ist gleichzeitig Chance (Greenfield) und Falle (jede AI-Wiki-Funktion ab heute muss Disclosure mitliefern). **Dieser Bericht empfiehlt drei Pflicht-Stakes vor Wiki-Welle 2 (Sprint 3).**

---

## State-of-the-Art

Der Knowledge-Base-/Wiki-Markt Mai 2026 ist nicht mehr "Notion vs Confluence" — er ist **viergleisig**: (1) Cloud-AI-Wiki (Notion, Confluence-Rovo, Slab+Glean, Outline-Cloud), (2) Open-Source-Self-Host mit AI-Beimischung (Docmost, Outline-Self-Host, Nextcloud-Collectives+Assistant, AFFiNE), (3) EU-Sovereign-Self-Host (XWiki+OpenProject in openDesk/ZenDiS, BookStack, Wiki.js), (4) Personal-Knowledge-Tools mit Team-Edge (Obsidian Sync, Logseq, Anytype). Cosmi-Wiki sitzt **in keiner dieser Kategorien sauber**: Cosmi ist Modul-im-ERP, nicht Standalone-Wiki — das ist die strategische Luecke und Chance zugleich.

Drei strukturelle Veraenderungen treiben den Markt seit Februar 2026:

(a) **AI-Search in Wikis ist kein Premium-Feature mehr, sondern Tabellenstake.** Notion hat im Mai 2025 (vor 12 Monaten) den AI-Add-on abgeschafft und AI-Agents/Ask-Notion in Business-Tier verschoben — am 4. Mai 2026 wurde der Credit-Mechanismus (10$/1000 Credits) GA, der Custom-Agents zu metered-Konsum macht. Outline hat AI-Answers seit Q2 2025 in Cloud-Edition. Docmost hat AI-Chat in Enterprise-Tier seit v0.80.0 (14. April 2026). Confluence-Rovo ist seit Anfang 2026 mit "Remix" (Pages → Charts/Slides/Prototypes via partner-Agents) in Open-Beta. **Wer 2026 ein Wiki ohne "Ask the workspace"-Suche pitcht, faellt in den Customer-Demos durch.** Cosmi-Wiki hat heute **keine** AI-Funktion — null Embeddings, null LLM-Call, null Disclosure-UI.

(b) **Block-Editor + Real-Time-Collab ist 2026 das technische Minimum.** TipTap-Editor + Yjs-Hocuspocus-Backend ist die de-facto-Open-Source-Stack-Kombination fuer Notion-aehnliche-Editoren. Outline nutzt ProseMirror+Yjs, Docmost nutzt TipTap, AFFiNE nutzt BlockSuite (proprietaer-aber-Open-Source), Nextcloud-Text nutzt Yjs. **Cosmi-Wiki hat den Backend-Slot (JSONB content + Versionierung via `wiki_versions`-Tabelle) korrekt — aber das Frontend ist ein `<textarea>` mit `Bold`/`Italic`/`Heading`-Buttons, die wortwoertlich `<strong>...</strong>` in den Text einfuegen.** Das ist ein 2018-Editor-Pattern. KMU-User vergleichen mit Google-Docs und Notion — sobald sie das Cosmi-Wiki oeffnen, ist die Wahrnehmung "Beta-Produkt" sofort gesetzt.

(c) **EU-Sovereignty-Wiki-Stack ist im Public-Sector bereits Realitaet, im KMU-Mittelstand 2027.** XWiki+OpenProject sind seit Juli 2025 in offizieller Partnership, FOSDEM-2026 (Februar) erster Joint-Stand, beide sind im **openDesk-Bundle via ZenDiS (Center for Digital Sovereignty)** als Public-Sector-Procurement-Vehikel. XWiki hat 500+ Confluence-Migrationen. Salesforce-Quip-Retirement-Anouncement (Maerz 2026, full-cutoff 17. Februar 2026 fuer Non-Customers) hat eine **erste Welle deutscher Mittelstaendler** ausgeloest, die Wiki-Alternativen evaluieren. **Cosmi-Wiki kann hier nicht direkt mit XWiki konkurrieren (Cosmi ist KMU-ERP-Modul, nicht Standalone-Wiki). Cosmi gewinnt ueber "DSGVO-Wiki-IM-CRM-IM-Kalender"-Integration** — das ist die Luecke gegen XWiki, das standalone bleibt.

### Top-Konkurrenten — Was sie haben, was Cosmi nicht hat

**1. Notion (international, threat: medium fuer DACH-KMU, HIGH als Feature-Benchmark)**

Notion ist nicht direkter DACH-KMU-Konkurrent (Cloud-only, US-Hosting, $20/Seat fuer AI-Vollausstattung), aber **definiert die Feature-Erwartung der User**. Wer auch immer Cosmi-Wiki zum ersten Mal oeffnet, hat Notion im Hinterkopf.

- **Notion AI Agents (GA September 2025)**, **Custom Agents Credit-Modell ab 4. Mai 2026** ($10/1000 Credits), **AI Autofill** (v3.4 part 2, 14. April 2026), **Enterprise-Search-Connectors** Box+Salesforce hinzugefuegt April 2026 (Liste: Slack, GDrive, GitHub, Jira, MS-Teams, OneDrive, SharePoint, Salesforce, Box).
- **Verified-Pages** (Business+, Blue-Checkmark in Search/AI-Citations) — Admin-driven authoritative content flagging. **Dies ist das wichtigste 2026-Pattern**, das Cosmi adoptieren sollte: kuratierte Knowledge-Layer im AI-Suche-Ranking.
- **Slack-Agent-Replies in private channels** (1. Mai 2026) — Notion-Workspace + Slack als Knowledge-Loop.
- **Developer Platform** (Mai 2026) — Notion als "Place where work is executed by people AND software agents".
- **G2-Pain-Points (2026)**: "Performance noticeably slows" bei Datenbanken >100 Eintraege/komplexen Relations, "Offline editing still missing in 2026", "Mobile less responsive", "$20/Seat zu teuer fuer KMU mit nur 10-20 Wissens-Pflegern".
- **Pricing**: Free ($0), Plus $10/Seat, Business $20/Seat (incl. AI Agents + Ask Notion), Enterprise custom.
- **Gap zu Cosmi:** AI Agents (Ask Workspace, Custom Agents), Verified-Pages-Pattern, Enterprise-Search-Connectors, Block-Editor mit Slash-Commands, Databases mit Relations, Real-Time-Collab, Mobile Apps.
- **Strategischer Hinweis:** **Cosmi gewinnt nicht ueber "AI-besser-als-Notion"** — Notion hat 12-24 Monate Vorsprung im AI-Layer und Credit-Pricing. **Cosmi gewinnt ueber "DSGVO + Modul-Integration + KMU-Preis"**: Wiki-Artikel referenziert CRM-Deal, Helpdesk-Ticket triggert Wiki-Suggest, Vertrag-Modul verlinkt auf interne Compliance-Wiki-Seite — das ist Cosmi-USP, Notion kann das strukturell nicht. **Aber:** der Block-Editor MUSS Notion-Pattern matchen (Slash-Commands, drag-to-reorder, block-toggle), sonst greift der "Cosmi-fuehlt-sich-nicht-modern-an"-Effekt.

**2. Confluence + Rovo (Atlassian, international, threat: HIGH im Enterprise, medium im DACH-KMU)**

Confluence ist im DACH-Mittelstand erstaunlich verbreitet (Atlassian-Partner-Channel), aber unter zunehmendem Druck wegen Cloud-Push und DSGVO-Compliance-Sorgen.

- **Rovo Plattform** — AI-Search-cross-app (Confluence + Jira + Slack + 3rd-Party-Connectors), personalisierte Antworten ueber gesamten Toolstack.
- **Remix (Open-Beta 2026)** — Pages -> Charts, Infographics, Prototypes, Starter-Apps, Slides via Rovo + Partner-Agents. Quellen-Content bleibt intakt, AI-Transformation on-top.
- **Team '26 Announcements (April 2026, Anaheim)** — Teamwork-Graph + Rovo Studio + Strategy Collection + AIOps Partner-Ecosystem.
- **Pricing**: Free (bis 10 User), Standard $5.42/Seat, Premium $10.44/Seat, Enterprise custom (alle annual).
- **Compliance-Sorge (Q3 2026)**: **Default-Opt-in fuer Customer-Metadata + In-App-Content zum AI-Training ab 17. August 2026** — das ist 2 Wochen nach EU-AI-Act-Article-50-In-Kraft-Treten. Erwartung: DACH-Datenschutz-Beauftragte werden im Q3 2026 eine Welle von **Opt-out-Audits ausloesen**. Das ist Cosmi's Window: "Migration von Confluence wegen Data-Sovereignty-Sorgen".
- **Gap zu Cosmi:** Rovo-Search, Remix-AI-Transformations, Cross-Tool-Connectors, Verified-Content-Pattern, Templates-Library, Macros, Page-Approvals.
- **Strategischer Hinweis:** **Atlassian's August-2026-Default-Opt-in-Move ist EIN Marketing-Gegen-Anker**, den Cosmi nutzen muss: "Cosmi-Wiki: nie Training-Daten, immer Self-Host, IM-CRM-IM-Helpdesk-IM-Kalender". Das ist eine 1:1-Vergleichs-Folie fuer Sales-Pitch. **Pflicht: Webseite + Pitch-Deck-Slide bis Q3 2026 fertig.**

**3. Outline (Open-Source + Cloud, international, threat: medium — Architektur-Vorbild)**

Outline ist die naechstgelegene Kombination aus "Open-Source Self-Host + moderner Block-Editor + AI-Search". Cosmi-Wiki sollte Outline als Architektur-Benchmark behandeln, nicht als Konkurrent.

- **v1.7.0 (24. April 2026)** — Email-Subscriptions mit diff-Notifications fuer Public-Documents, **Side-by-Side Revision-Comparisons** (sehr gefragtes UX-Pattern), Full-RTL-Support (Hebrew/Arabic), Command-Bar-Search in Public-Shares mit Recent-Document-Access, Auto-Collapse fuer lange Code-Blocks.
- **v1.7.1 (4. Mai 2026)** — **MCP-Tools erweitert um Breadcrumbs, Summaries, Document-Deletion** (Model-Context-Protocol-Integration fuer Cursor/Claude-Code/etc), Per-Share-Branding fuer Public-Shares, Rate-Limiting-Config fuer Self-Host.
- **v1.6.x (Maerz 2026)** — MCP-Server-Integration als Headline-Feature, GitLab-Issue-Previews, Presentation-Mode.
- **AI-Answers** (Settings → AI, Cloud-Edition) — Workspace-Daten kein AI-Training, aber Embeddings-Indexing on-demand. Erscheint in Search-Results + Slack-Search.
- **Pricing**: Cloud Free/Team $10/Seat, Self-Host kostenlos (Apache-Lizenz-Variante).
- **Tech-Stack**: ProseMirror+Yjs Real-Time-Collab, Markdown-First, Slack-Integration eingebaut.
- **Gap zu Cosmi:** Block-Editor mit Slash-Commands, Yjs-Real-Time-Collab, AI-Answers (Cloud), MCP-Server fuer LLM-Tool-Use, Side-by-Side-Diff-Comparison, Public-Share-Per-Share-Branding, Markdown-First-Approach.
- **Strategischer Hinweis:** **Outline ist die beste Architektur-Referenz fuer Cosmi-Wiki Phase 2.** Cosmi sollte ProseMirror/TipTap als Editor-Layer + Yjs+Hocuspocus als Collab-Backend evaluieren — beides Open-Source, beides EU-self-hostbar. **MCP-Server-Integration ab Phase 2 oeffnet Wiki fuer Cosmi-CLI-Bot / Claude-Code-Integration** (Cosmi-User koennte mit Cursor in Wiki-Content navigieren). Side-by-Side-Diff ist UX-Quick-Win.

**4. Docmost (Open-Source, international, threat: medium — direkter Self-Host-Konkurrent)**

Docmost ist der **am schnellsten wachsende Open-Source-Konkurrent in der "Notion-Self-Host-Alternative"-Kategorie**.

- **v0.90.0 (21. Mai 2026)** — **Synced-Blocks (Transklusion)**, Page-Labels, Indentation-Support, Table-Sorting, **Backlinks** (graphbasiert wie Logseq/Obsidian), Azure-Blob-Storage. **Enterprise**: Templates, PDF-Import, SCIM-Provisioning.
- **v0.80.0 (14. April 2026)** — **Favorites**, Space-Watching-Notifications, **AI Chat (Enterprise)**, **Page-Verification mit Approval-Workflow (Enterprise)** — direkt das Notion-Verified-Pattern adoptiert, Server-side PDF-Export-APIs (Enterprise).
- **v0.90.1 (28. Mai 2026)** — Security-Fixes.
- **Pricing**: Self-Host kostenlos (Community), Enterprise per-Seat.
- **Tech-Stack**: TipTap-Editor, Real-Time-Collab via Yjs (CRDT), PostgreSQL, Docker/On-Prem fuer GDPR/HIPAA/FedRAMP/ITAR.
- **Gap zu Cosmi:** Block-Editor (TipTap real produktiv), Real-Time-Collab, Synced-Blocks (Transklusion), Backlinks, AI-Chat (Enterprise), Page-Verification-Workflow, SCIM, Air-Gapped-Deployment-Doku.
- **Strategischer Hinweis:** **Docmost ist Cosmi-Wikis naechster direkter Architektur-Konkurrent im Self-Host-DACH-Markt** — gleicher Tech-Stack-Vibe (Postgres + TipTap + Docker), gleicher Target-Markt (KMU/Mid-Market). Docmost ist **2 Jahre alt** (vs. XWiki 15+), wachsendes Tempo (v0.80→v0.90 in 5 Wochen). **Cosmi-USP gegen Docmost: Modul-Integration im KMU-ERP** (Docmost ist Standalone-Wiki, kann nicht direkt Helpdesk-Ticket triggern). **Aber:** Docmost's Page-Verification + AI-Chat sind 2026-Standard, die Cosmi nachziehen muss.

**5. Nextcloud (DACH, EU-Sovereignty-Vorbild, threat: medium — Architektur-Lessons)**

Nextcloud Hub ist im DACH-KMU-Mittelstand-Markt der wichtigste **EU-souveraene Knowledge-Hub-Konkurrent** — primaer ueber Collectives (Wiki) + Notes-App + Assistant.

- **Hub 25 (Nextcloud 32, GA 27. September 2025, Patch 32.0.10 am 28. Mai 2026)** — Collectives+Notes+Assistant-Integration.
- **Hub 26 (Nextcloud 33, GA 18. Februar 2026)** — **Assistant mit Agent-Capabilities**: kann Calendar-Events erstellen, Talk-Nachrichten senden, Wetter abfragen, Daten aus Files/Collectives/Analytics lesen. **Erster echter cross-app-agentic Layer im DACH-Sovereignty-Stack**.
- **Assistant-Modelle**: Self-Host-LLM-Provider-Plugins (Llama-3, Mixtral, etc.) — kein Cloud-Lock-In.
- **Tech-Stack**: PHP-Backend, Vue.js-Frontend, eigene Editor-Schicht (Yjs-Real-Time-Collab in Files/Text-App), MariaDB/PostgreSQL.
- **Pricing**: Self-Host Open-Source, Enterprise-Support per-User.
- **Gap zu Cosmi:** Assistant cross-app-agentic, Self-Host-LLM-Provider-Pluggable-Stack, Collectives-Wiki+Notes-DACH-User-Base, openDesk-Inklusion (Public-Sector-Channel via ZenDiS).
- **Strategischer Hinweis:** **Nextcloud ist nicht direkter Konkurrent fuer Cosmi-KMU-ERP-Zielsegment** — Nextcloud-User sind oft Tech-affin/IT-Self-Host-faehig. Aber: **Nextcloud-Assistant-Architektur ist 1:1 das, was Cosmi-uebergreifend braucht** — Self-Host-LLM-Provider-Plugin-Layer + cross-Modul-agentic. Cosmi sollte Llama.cpp/Ollama als optionalen Inference-Layer evaluieren (Pflicht fuer Tenants in regulierten Branchen). **Konkrete Tech-Lesson:** Nextcloud nutzt **pgvector** seit Hub 22 fuer Embeddings — Cosmi-Postgres-Stack kann das ohne neuen DB-Service direkt aktivieren.

**6. XWiki + OpenProject (EU-Sovereignty-Stack, DACH-Public-Sector, threat: low fuer KMU-Markt — strategischer Channel-Konkurrent)**

XWiki ist nicht Cosmi-KMU-Zielsegment-Konkurrent, aber im **Public-Sector + DACH-Behoerden-Procurement** die direkte Wahl, und das ist der Kanal, in dem Cosmi mittelfristig wachsen koennte.

- **Partnership mit OpenProject seit 2. Juli 2025**, **FOSDEM 2026 Joint-Stand** (Brussels, Februar 2026), **openDesk-Bundle via ZenDiS** (Center for Digital Sovereignty, DE Bundesregierung).
- **OpenProject Jira-Migrator (offiziell ab Maerz 2026)** — Public-Sector-Migration-Vehikel.
- **500+ Confluence-Migrationen** (XWiki-eigene Zahl).
- **Tech-Stack**: Java + Spring + LucentDB/MariaDB/PostgreSQL, eigene Wiki-Syntax + WYSIWYG-Editor (CKEditor 5).
- **Pricing**: Self-Host kostenlos (LGPL), Enterprise-Support per-User.
- **Gap zu Cosmi:** openDesk/ZenDiS-Inklusion (Channel), Government-Track-Record, Confluence-Migrator, OpenProject-Bundle-Integration.
- **Strategischer Hinweis:** **XWiki ist Cosmi's Schatten-Konkurrent im Public-Sector-Channel** — wenn Cosmi je in DACH-Public-Sector-Procurement will (Bundeslaender, Stadtwerke, Krankenhaeuser), muss Cosmi entweder mit openDesk koexistieren ODER ZenDiS-Annaeherung suchen. **Realistische Empfehlung fuer 2026:** Public-Sector ignorieren, KMU-Mittelstand fokussieren, XWiki nur als Stand-der-EU-Sovereignty-Erwartung tracken.

---

## Cosmi-IST-Stand

Stand 2026-06-01, Reading `backend/internal/wiki/` + `desktop/src/renderer/src/modules/wiki/` + Migrations `000076_create_wiki.up.sql`.

**Backend (Production-ready, S1.1 done seit 2026-04-18, Coverage 38.2%):**

- **5 Datenbank-Tabellen** (Migration 000076):
  - `wiki_articles`: UUID-PK, tenant_id, title, slug, `content JSONB` (TipTap-Schema-Slot), `search_vector TSVECTOR` (GIN-Index), author_id, category_id, published bool, created_at/updated_at. UNIQUE (tenant_id, slug).
  - `wiki_categories`: hierarchisch via `parent_id` Self-FK ON DELETE SET NULL, position INT, UNIQUE (tenant_id, parent_id, name).
  - `wiki_versions`: article_id FK CASCADE, version_number, content JSONB, changed_by, changed_at. UNIQUE (article_id, version_number).
  - `wiki_attachments`: article_id FK CASCADE, file_ref TEXT, mime, size BIGINT.
  - `wiki_share_tokens`: article_id FK CASCADE, token TEXT UNIQUE, expires_at NULLABLE, permissions TEXT[].
- **FTS-Trigger** (Postgres-Standard): `setweight('A')` fuer Title + `setweight('B')` fuer `content->>'plain'`. German-Sprachkonfiguration. `BuildSearchQuery` in `fts.go` baut tsquery mit AND-Verknuepfung + prefix-Wildcard (`:*`) auf letztem Token.
- **Service-Layer** (`service.go`, 441 LOC): CRUD-Article, Update-with-Auto-Version-Snapshot, Slug-Uniqueness-Check, Category-Validation, Attachment-Upload, Share-Tokens (Schema da, Service-Methode nicht erkennbar in service.go — vermutlich in repo-Layer), 15 RPCs in `cmd/wiki/main.go` + `server/wiki_grpc.go`.
- **Multi-Tenant-Isolation**: alle Repository-Methoden parametrisiert auf `tenantID` — Tenant-Isolation-Tests in `tenant_isolation_phase2_test.go` (root-owned File, Sprint-2-R2-Compliance).
- **HTTP-Gateway-Route**: `gateway/route_wiki.go` — gRPC->REST-Mapping. Frontend-API-Calls via diese Route.

**Frontend (Desktop Electron, 12 .tsx-Files, 1284 LOC):**

- `WikiPage.tsx` (221 LOC): 3-Spalten-Layout (Sidebar w-56 + List w-80 + Detail flex-1 + optional History-Panel w-64). Mock-Store `useWikiStore`, **noch keine TanStack-Query-Backend-Calls**. Pinning, status (draft/published/archived), tags, viewCount.
- `WikiEditor.tsx` (118 LOC): **KEIN TipTap. Plain HTML-`<textarea>` mit Tag-Insertion-Toolbar**. Bold/Italic/Heading2/List/Link/Code-Buttons fuegen wortwoertlich `<strong>...</strong>`, `<em>...</em>`, `<h3>...</h3>`, `<ul><li>...</li></ul>` in den Text ein. Ctrl+S = Save, Esc = Cancel. **Diskrepanz zu sources/wiki.yaml ("Block-Editor (TipTap)")**.
- `WikiArticle.tsx` (87 LOC), `WikiSidebar.tsx` (131), `WikiTreeNode.tsx` (70): View-Mode mit Tree-Navigation.
- `WikiVersionHistory.tsx` (51), `WikiVersionItem.tsx` (53): Versions-Listing.
- `WikiSearch.tsx` (32): Kompakte Searchbar — clientseitige Filter ueber `useWikiStore`-Mock, kein Backend-FTS-Call.
- `WikiTemplateDialog.tsx` (136), `WikiCategoryDialog.tsx` (126), `WikiShareDialog.tsx` (120), `WikiArticleHeader.tsx` (139): Dialog/UI-Komponenten.
- I18n via `react-i18next`.

**Pricing-Position** (aus `docs/PRICING.md`):
- Wiki: **2 EUR/Modul/User/Monat** vs Notion ab 8 EUR (Plus) / 20 EUR (Business+AI), Confluence ab 5 EUR (Standard) / 10 EUR (Premium). **Bis zu 75% guenstiger**, aber **ohne AI-Layer**, ohne Real-Time-Collab, ohne moderner Block-Editor.

**Was Cosmi-Wiki HAT (Highlights):**
- ✅ Multi-Tenant-Isoliert (Sprint-2-R2-Compliance)
- ✅ Postgres-FTS-german + tsvector+GIN (technisch sauber, sprachlich KMU-DACH-ready)
- ✅ Hierarchische Kategorien (parent_id)
- ✅ Versionierung mit automatischem Snapshot bei Content-Update (`UpdateArticle` saved version BEFORE overwriting)
- ✅ Attachments (File-Storage-Hook ueber `file_ref`)
- ✅ Share-Tokens (Schema vorhanden, Expiry + Permissions)
- ✅ Slug-Uniqueness per Tenant
- ✅ TipTap-JSON-Content-Schema im Backend (JSONB), bereit fuer Frontend-Adoption

**Was Cosmi-Wiki NICHT HAT (Stand 2026-06-01):**
- ❌ **Echter Block-Editor** (TipTap/BlockNote/Lexical/Plate) — Frontend ist `<textarea>` mit HTML-Tag-Insertion. **Single biggest gap**.
- ❌ **Real-Time-Collab** (Yjs / Hocuspocus / WebSocket-CRDT)
- ❌ **AI-Search / Ask-Workspace** (Embeddings, LLM-Call)
- ❌ **pgvector** / Semantic-Search
- ❌ **EU-AI-Act-Article-50-Disclosure-UI** (kein AI-Feature => noch keine Disclosure-Schicht, ABER: Pflicht-Vorbereitung)
- ❌ **Slash-Commands** ("/heading", "/list", "/code")
- ❌ **Backlinks / Bidirectional-Links** (Knowledge-Graph)
- ❌ **Synced-Blocks / Transklusion**
- ❌ **Page-Verification / Approval-Workflow** (Notion+Docmost-Pattern)
- ❌ **Side-by-Side Version-Diff** (Outline v1.7.0)
- ❌ **Public-Share-Viewer-Endpoint** (Share-Token-Schema da, aber Service-Methode + HTTP-Endpoint nicht erkennbar — moeglicherweise nicht implementiert)
- ❌ **Templates-Bibliothek** (Dialog-Komponente `WikiTemplateDialog` existiert, Backend-Templates-Quelle unklar)
- ❌ **Mobile-Editor** (Cosmi-Mobile-App noch nicht im Wiki-Modul-Routing)
- ❌ **TanStack-Query-Backend-Integration** im Frontend (Mock-Store statt echte API-Calls)
- ❌ **MCP-Server-Integration** (Outline v1.6/v1.7 — fuer LLM-Tool-Use)
- ❌ **Cross-Modul-Backlinks** (Wiki-Artikel zu CRM-Deal/Helpdesk-Ticket — der Cosmi-USP-Hebel, der noch komplett fehlt)
- ❌ **Page-Comments / Inline-Diskussion** (Notion+Confluence-Standard)

---

## Konkurrenz-Vergleichstabelle

| Feature | Cosmi | Notion (Business) | Confluence (Premium) | Outline (Self-Host) | Docmost (Enterprise) | Nextcloud Hub 26 | XWiki + openDesk |
|---|---|---|---|---|---|---|---|
| Block-Editor (Slash-Commands) | ❌ (textarea) | ✅ | ✅ | ✅ ProseMirror | ✅ TipTap | ✅ Yjs-Text | ✅ CKEditor 5 |
| Real-Time-Collab (CRDT) | ❌ | ✅ | ✅ | ✅ Yjs | ✅ Yjs | ✅ Yjs | 🚧 limitiert |
| Postgres-FTS (de) | ✅ tsvector | ✅ Cloud | ✅ | ✅ | ✅ | ✅ | ✅ |
| Semantic-Search (pgvector/Embeddings) | ❌ | ✅ Ask-Notion | ✅ Rovo | ✅ AI-Answers | ✅ AI-Chat | ✅ Assistant | ❌ |
| AI-Agents / Ask-Workspace | ❌ | ✅ Custom Agents | ✅ Rovo+Remix | ✅ AI-Answers | ✅ AI-Chat | ✅ cross-app | ❌ |
| EU-AI-Act-Disclosure-UI (Aug 2026 Pflicht) | ❌ | 🚧 unclear | 🚧 unclear | 🚧 unclear | 🚧 unclear | 🚧 LLM-Wahl-Disclosure-Layer-da | n/a (kein AI) |
| Versionierung (auto-snapshot) | ✅ | ✅ 90d (Business) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Side-by-Side-Diff | ❌ | ✅ | ✅ | ✅ v1.7.0 | 🚧 | 🚧 | ✅ |
| Backlinks / Knowledge-Graph | ❌ | 🚧 limitiert | ❌ | ✅ | ✅ v0.90 | 🚧 | ✅ |
| Synced-Blocks / Transklusion | ❌ | ✅ | ❌ | ❌ | ✅ v0.90 | ❌ | ✅ |
| Page-Verification (Verified-Page) | ❌ | ✅ Business+ | ❌ | ❌ | ✅ Enterprise | ❌ | ❌ |
| Hierarchische Kategorien | ✅ | ✅ (Pages-Tree) | ✅ Spaces | ✅ Collections | ✅ Spaces | ✅ Circles | ✅ Spaces |
| Attachments | ✅ | ✅ | ✅ | ✅ | ✅ Azure-Blob | ✅ | ✅ |
| Public-Share-Tokens | ✅ Schema | ✅ | ✅ | ✅ Per-Share-Branding | ✅ | ✅ | ✅ |
| Templates-Library | 🚧 Dialog-UI | ✅ | ✅ | ✅ | ✅ Enterprise | 🚧 | ✅ |
| Cross-Modul-Integration (Wiki↔CRM/Helpdesk) | ❌ (USP-Hebel offen!) | ❌ (Standalone) | 🚧 Jira-Link | ❌ | ❌ | 🚧 limitiert | 🚧 OpenProject-Link |
| Mobile-Editor | ❌ | ✅ (lang) | ✅ | ✅ | ✅ | ✅ | 🚧 |
| MCP-Server (LLM-Tool-Use) | ❌ | ❌ | ❌ | ✅ v1.6+v1.7 | ❌ | ❌ | ❌ |
| Page-Comments / Inline-Diskussion | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Approval-Workflow | ❌ | ✅ Business+ | ✅ | ❌ | ✅ Enterprise | ❌ | ✅ |
| SCIM-Provisioning | ❌ | ✅ Enterprise | ✅ Premium | 🚧 | ✅ Enterprise | 🚧 | ✅ |
| EU-Self-Host (DSGVO-nativ) | ✅ | ❌ Cloud-only | 🚧 Data-Center | ✅ | ✅ Air-Gap | ✅ | ✅ openDesk |
| Open-Source | ❌ proprietaer | ❌ | ❌ | ✅ (Apache) | ✅ (Community) | ✅ (AGPL) | ✅ (LGPL) |
| Pricing/Seat (DACH-KMU) | **2 EUR Modul** | $20 Business+AI | $10.44 Premium | $0 Self / $10 Cloud | Self $0 / Ent custom | Self $0 / Ent ~5 EUR | Self $0 / ZenDiS-Bundle |
| KMU-ERP-Modul-Integration | ✅ USP-Anker | ❌ | ❌ | ❌ | ❌ | 🚧 | ❌ |
| Markt-Reife / Sales-Track-Record | 🚧 Beta | ✅ Massmarkt | ✅ Enterprise | ✅ Mid-Market | 🚧 Wachstum | ✅ DACH | ✅ Gov |

**Lesart der Tabelle:**

Cosmi-Wiki hat **2 strukturelle Vorteile** (EU-Self-Host, Modul-Integration im KMU-ERP) gegen **8-10 strukturelle Defizite** (Block-Editor, Real-Time-Collab, AI-Layer, Backlinks, Mobile, etc.). **Der Modul-Integration-Vorteil ist heute NUR ein theoretischer Anker** — es gibt keine implementierten Cross-Modul-Backlinks (Wiki-zu-CRM-Deal, Wiki-zu-Helpdesk-Ticket), die Cosmi gegen Notion/Confluence ueberhaupt sales-faehig machen wuerden. Das ist die zentrale Diagnose dieses Deepdives: **Cosmi-Wikis USP ist konzeptionell stark, implementationsseitig noch nicht aktiviert.**

---

## Top-3 Strategische Empfehlungen

### 1. **TipTap-Frontend live + Block-Editor-Parity (P0 Pflicht, Sprint 3 Welle 1)**

**Problem**: WikiEditor.tsx ist ein 2018-Editor-Pattern. Backend-Schema (JSONB content) ist seit April 2026 TipTap-ready, Frontend liefert HTML-Strings. KMU-User vergleichen mit Notion/Google-Docs — Cosmi faellt sofort als "Beta" durch.

**Empfehlung**: TipTap v3 + Yjs-CRDT-Provider (vorbereitet, aber nicht in Sprint 3 aktiviert) + Slash-Commands ("/heading1", "/list", "/code", "/table", "/image", "/divider") + Drag-to-Reorder + Block-Toggle + Image-Inline-Upload (an `wiki_attachments` Tabelle). **Zeitschaetzung 5-7 Sprints**. Yjs-Aktivierung als Phase 2 (Sprint 4-5), zunaechst Save-on-Blur reicht fuer KMU-Internal-Wiki.

**Begruendung**: 
- Backend-JSONB-Schema-Slot wartet seit 7 Wochen — verschwendete Optionalitaet.
- Wettbewerb (Docmost, Outline, Nextcloud, AFFiNE) hat alle TipTap/ProseMirror/Yjs-Stack. Cosmi ist 18-24 Monate hinter Open-Source-State-of-the-Art.
- Pricing-Vorteil (2 EUR vs 8-20 EUR) wird durch "ungewohntes Editor-Pattern" sofort egalisiert. KMU-Wechsel-Threshold liegt nicht bei Preis, sondern bei "fuehlt sich modern an oder nicht".

**Risiko**: TipTap-Editor ist groesser als 7-Sprint-Schaetzung, Slash-Commands-UX ist Detail-aufwendig. Mitigation: **Phase 1 (Sprint 3) nur Block-Editor ohne Slash-Commands** — Toolbar bleibt, aber statt textarea echter TipTap mit Bold/Italic/Headings/Lists/Links/Code als TipTap-Extensions, nicht HTML-Strings. **Phase 2 (Sprint 4) Slash-Commands + Drag-to-Reorder**. **Phase 3 (Sprint 5+) Yjs-CRDT-Aktivierung.**

**Picks**: 🟢 P0 Sprint-3-Roadmap-Move

---

### 2. **EU-AI-Act-Article-50-Disclosure-Layer VOR jedem AI-Wiki-Feature (P0 Pflicht, Sprint 3 Welle 0)**

**Problem**: EU-AI-Act Article 50 wird am **2. August 2026** in Kraft treten. **Jeder generative AI-System, der mit natuerlichen Personen interagiert**, muss Disclosure-UI haben ("Sie interagieren mit einem AI-System"). Markierungs-Pflicht fuer AI-generierte Inhalte (machine-readable). **Cosmi hat heute KEINE Disclosure-UI, weil noch keine AI-Wiki-Features existieren — aber das ist die Falle: jedes erste AI-Feature in Wiki (AI-Search, Ask-Cosmi, AI-Suggest, AI-Auto-Tagging, AI-Summary) muss am Tag eins Disclosure-konform sein.**

**Empfehlung**:
- **Compliance-Foundation-Sprint (Sprint 3, Welle 0)**: Build a Cosmi-uebergreifenden `ai_disclosure`-Layer:
  - DB-Tabelle `ai_interactions` (interaction_id, tenant_id, user_id, modul, feature, model_provider, prompt_hash, completion_hash, disclosure_shown_at, timestamp). Audit-Log.
  - Frontend-Komponente `<AIBanner>` (lucide-Icon "Sparkles" + Tooltip "Diese Funktion nutzt ein KI-System (Anbieter: $provider). Antworten koennen falsch sein. EU-AI-Act Art. 50.").
  - **Markierungs-Pattern**: Backend-Response-Format mit `is_ai_generated: true` + watermark-style HTML-Class `ai-generated-content` (CSS-Underline + Tooltip "AI-generiert").
  - **Modell-Provider-Compliance-Doc**: `docs/compliance/ai-providers.md` — Liste aller verwendeten LLM-Provider (OpenAI/Anthropic/Mistral/Self-Host) + EU-AI-Act-Klassifikation.
- **Phase 2 (Sprint 4+)**: Erst NACH Disclosure-Layer-Live wird AI-Search in Wiki aktiviert. **Kein AI-Feature ohne Disclosure**.

**Begruendung**:
- Aug 2026 Frist ist nicht verschiebbar.
- Cosmi-Self-Host-USP wird durch Compliance-Schmerz amplifiziert: Notion/Confluence haben am 17. August 2026 Atlassian-Default-AI-Training-Opt-in — DACH-Datenschutzbeauftragte werden Alternativen audit-en. **Cosmi mit fertiger Disclosure-Layer ist genau zur richtigen Zeit das richtige Produkt.**
- Greenfield-Vorteil: weil Cosmi heute KEINE AI-Features hat, kann der Disclosure-Layer von Grund auf richtig gebaut werden — keine Legacy-AI-Calls nachzuruesten.

**Risiko**: Disclosure-Layer kann ueberdimensioniert werden (Compliance-Theatre). Mitigation: **Minimaler MVP** — 1 Tabelle, 1 React-Komponente, 1 Compliance-MD-File. Erst wenn Phase-2-AI-Feature kommt, wird das vollstaendige Audit-Logging gebraucht.

**Picks**: 🟢 P0 Compliance-Sprint-Move

---

### 3. **pgvector + Hybrid-Search (BM25-FTS + Semantic) als Cosmi-uebergreifender Layer (P1, Sprint 4)**

**Problem**: Cosmi-Wiki-Suche ist reine Postgres-FTS-german (tsvector + GIN). 2026 erwarten Nutzer "Ask-the-Workspace"-AI-Search. Aber Cosmi will (a) DSGVO-self-host bleiben und (b) keine externen LLM-Kosten in der Basis-Pricing-Position. Loesung: **Embeddings-Layer auf pgvector**, das schon im Postgres-Server laeuft. Kein neuer DB-Stack, kein neuer Service.

**Empfehlung**:
- **pgvector-Extension** in Cosmi-Postgres aktivieren (Postgres ≥ 12, Extension-Install + Migration `000XYZ_add_pgvector.up.sql`).
- **Embedding-Spalte** `wiki_articles.embedding VECTOR(768)` (bge-m3 oder ein anderes EU-souveraenes 768-dim Modell — Cosmi nutzt bge-m3-self-hosted laut `settings.yaml`).
- **Backfill-Worker**: Beim Create/Update von Article — Embedding via `embeddings_endpoint` (Ollama-Default in `settings.yaml` schon vorbereitet, kein neuer Infra-Stack).
- **Hybrid-Search-RPC**: `SearchArticlesHybrid(tenant, query, mode)`. Mode: `fts_only` / `semantic_only` / `hybrid` (Reciprocal-Rank-Fusion). Default: hybrid.
- **Cosmi-uebergreifende Anwendung**: Same Pattern fuer `helpdesk_tickets`, `crm_deals`, `vertraege_documents` — schoepft "Ask-Cosmi"-Layer ohne LLM-Call. **Erstmal nur Retrieval, kein Generation. Das ist 80% des Wertes ohne 100% des Compliance-Risikos.**

**Begruendung**:
- pgvector ist Postgres-native, kein neuer Service, keine neuen Backup-Strategien, keine neuen Storage-Costs.
- Nextcloud nutzt pgvector seit Hub 22 — ist bewaehrter Stack im DACH-Sovereignty-Markt.
- "Hybrid-Search-ohne-LLM" liefert DACH-KMU-User-Wow-Effekt (semantische Suche auf intern Wiki!) ohne EU-AI-Act-Article-50-Trigger (Retrieval ist keine Generation).
- ABER: bei Anzeige als "AI-Search" sollte Disclosure-Layer (Empfehlung 2) bereits live sein.

**Risiko**: bge-m3 self-hosted Embeddings sind 1-2 Sekunden pro Article — Backfill von 10000 Wiki-Artikeln dauert ~3-5h. Mitigation: async-Worker mit Progress-Tracking.

**Picks**: 🟡 P1 Sprint-4-Roadmap-Move (-> followup 30d)

---

## Quellen

**Cosmi-Repo (intern):**
- `backend/internal/wiki/service.go` (441 LOC) — CRUD-Logic + Auto-Versioning
- `backend/internal/wiki/fts.go` — tsquery-Builder + clean-Token-Helper
- `backend/internal/wiki/models.go` — Article/Version/Attachment/Category/ShareToken-Structs
- `backend/migrations/000076_create_wiki.up.sql` — 5 Tabellen + FTS-Trigger
- `desktop/src/renderer/src/modules/wiki/WikiEditor.tsx` — **Diskrepanz: HTML-textarea statt TipTap**
- `desktop/src/renderer/src/modules/wiki/WikiPage.tsx` — 3-Spalten-Layout + Mock-Store
- `docs/ROADMAP.md` — S1.1 wiki done 2026-04-18, Coverage 38.2%
- `docs/PRICING.md` — Wiki 2 EUR/Modul

**Konkurrenz / Markt-Signale:**
- Notion AI Custom Agents Credit-Modell (4. Mai 2026) — [notion.com/help/enterprise-search](https://www.notion.com/help/enterprise-search)
- Notion Pricing 2026 — [notion.com/pricing](https://www.notion.com/pricing)
- Confluence Rovo + Remix-Open-Beta + Team '26 — [atlassian.com/software/confluence/ai](https://www.atlassian.com/software/confluence/ai)
- Atlassian Default-AI-Training-Opt-in ab 17. August 2026 — Atlassian Cloud Changes Blog Mar 2026
- Outline v1.7.0 (24. Apr 2026), v1.7.1 (4. Mai 2026) — [github.com/outline/outline/releases](https://github.com/outline/outline/releases)
- BookStack v26.05 (28. Mai 2026), v26.03.5 Security (21. Mai 2026) — [github.com/BookStackApp/BookStack/releases](https://github.com/BookStackApp/BookStack/releases)
- Docmost v0.90.0 (21. Mai 2026) Synced-Blocks+Backlinks, v0.80.0 (14. Apr 2026) AI-Chat+Page-Verification — [github.com/docmost/docmost/releases](https://github.com/docmost/docmost/releases)
- Obsidian Mobile 2.0 + Bases + Neuron Local-AI — Obsidian Roadmap
- Nextcloud Hub 26 / Nextcloud 33 (18. Feb 2026) — Assistant agentic — [nextcloud.com/assistant/](https://nextcloud.com/assistant/)
- XWiki + OpenProject Partnership / openDesk via ZenDiS — [openproject.org/blog/open-source-jira-confluence-alternative](https://www.openproject.org/blog/open-source-jira-confluence-alternative/)
- EU-AI-Act Article 50 — [artificialintelligenceact.eu/article/50](https://artificialintelligenceact.eu/article/50/)
- AFFiNE / BlockSuite Editor — [affine.pro/blog](https://affine.pro/blog)
- Notion G2-Reviews 2026 Pain-Points (slow with large DBs, expensive, offline missing) — [g2.com/products/notion/reviews](https://www.g2.com/products/notion/reviews)
- Confluence Self-Host Alternatives 2026 — [euroalternative.eu/alternatives/confluence](https://euroalternative.eu/alternatives/confluence)
- TipTap Collaboration via Yjs+Hocuspocus — [tiptap.dev/docs/collaboration](https://tiptap.dev/docs/collaboration/getting-started/overview)

---

## Picks (vorgeschlagen)

[ ] 🟢 P0 — TipTap-Frontend live (Sprint 3 Welle 1) — Backend-Schema wartet seit 7 Wochen
[ ] 🟢 P0 — EU-AI-Act-Article-50-Disclosure-Layer (Sprint 3 Welle 0) — vor jedem AI-Feature, Frist 2. Aug 2026
[ ] 🟡 P1 — pgvector + Hybrid-Search Cosmi-uebergreifend (Sprint 4) — [-> followup 30d]
[ ] 🟡 P2 — Cross-Modul-Backlinks (Wiki↔CRM/Helpdesk) — Cosmi-USP-Aktivierung, [-> followup 60d]
[ ] 🟡 P2 — Page-Verification-Workflow (Notion/Docmost-Pattern) — Verified-Pages-Pattern in AI-Search-Ranking, [-> followup 60d]
[ ] 🟢 Marketing — Sales-Folie "Cosmi vs Atlassian-17.-Aug-Default-Opt-in" — bis Q3 2026 fertig
[ ] ⚪ Watch — Docmost-Tempo (v0.80 → v0.90 in 5 Wochen) — alle 4 Wochen prüfen ob neue Features Cosmi kopieren-muss
[ ] ⚪ Watch — XWiki+OpenProject openDesk-Adoption im Public-Sector — nur tracking, kein Action
[ ] ⚪ Watch — Outline MCP-Server-Pattern (LLM-Tool-Use) — Phase-3-Kandidat fuer Cosmi-CLI-Bot-Integration
