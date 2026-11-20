# Web Utility Factory — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/web-utility-factory.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Landing e strumenti web SEO-first con UX sobria, interazioni leggere, accessibilità e tempi di caricamento prioritari.

**Temi candidati:** strumenti; browser; SEO/ricerca; conferma.

## Superfici e placement proposti

1. lista tool e ricerca.
2. stati vuoti/input/form.
3. download risultato soltanto se pronto.

## Icone Gentleface collegate (molti-a-molti)

Nessuna icona Gentleface associata direttamente: non assumere che un asset sia disponibile.

**Nuove icone da cercare/disegnare:** search, check, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- hover e feedback tastiera/mouse con prefers-reduced-motion.
- nessun loop decorativo sopra la form principale.

## Cosa evitare

- JS/icon-pack pesanti per aggiungere una semplice decorazione.
- sovraccarico bento che riduce conversione e SEO.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-003 — Taste Skill | HIGH | SEO utility site landing and conversion flows |
| DSK-005 — Vercel Web Design Guidelines | HIGH | SEO-first accessible utility web UI |
| DSK-007 — Hallmark | MEDIUM | landing experiments; prioritize SEO and speed |
| DSK-010 — Stageshow | MEDIUM | service landing feature illustrations |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Optional landing hero, never search results. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (MEDIUM):** Desktop marketing hero only, not utility workflow. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Marketing sections with text still indexable. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Real conversion/form request pending. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (HIGH)** — Hero web/pagina prodotto. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## Uiverse — proposte 18/11/2026

- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**8 preferiti proposti per web-utility-factory**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-067](https://uiverse.io/elijahgummer/young-horse-7) | RADIO | Scelta esclusiva accessibile | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-096](https://uiverse.io/solowzrd/wet-lionfish-63) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.css) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.


## Fonti esterne aggiunte — 20/11/2026 (15 URL, 14 servizi unici)

Intake visivo documentale: [audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice per app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro JSON](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Motion Sites** (`DESIGN-SITE-015`): Animated hero with reduced-motion fallback. **Stato: PROPOSED_ONLY**.
- **Motion Sites Studio** (`DESIGN-SITE-016`): AI-assisted website prototype comparison. **Stato: PROPOSED_ONLY**.
- **Land-book** (`DESIGN-SITE-017`): Pricing-page hierarchy with distinct comparison tiers. **Stato: PROPOSED_ONLY**.
- **Recent Design** (`DESIGN-SITE-018`): App icon and typography moodboards. **Stato: PROPOSED_ONLY**.
- **Landdding** (`DESIGN-SITE-019`): Sector-specific landing layouts for SaaS, utility and food. **Stato: PROPOSED_ONLY**.
- **SVGL** (`DESIGN-SITE-026`): Find official provider logos for legitimate integration badges. **Stato: PROPOSED_ONLY**.
- **Shots** (`DESIGN-SITE-027`): Create marketing phone/device mockups from own QA screenshots. **Stato: PROPOSED_ONLY**.

I pattern richiedono decisione di prodotto, valutazione della licenza e QA sulla schermata target. Nessun componente, font, foto o logo di terzi e' stato copiato; nessuna funzione consumer risulta implementata da questo intake.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **ReUI** (`DESIGN-SITE-031`): Study copy-and-own React sidebar, forms, stepper, sortable and data grid for Web products. **PROPOSED_ONLY**.

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **React Bits** (`DESIGN-SITE-034`): Use selective React button/card/text motion on promotional web pages after motion/performance checks — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **Scrolltide** (`DESIGN-SITE-035`): Scroll narrative reference for a distinctive landing page without copying paid templates — **PROPOSED_ONLY**.
- **Scroll Shaders** (`DESIGN-SITE-036`): Optional light Web hero shader with static reduced-motion fallback — **PROPOSED_ONLY**.
- **Snapblocks** (`DESIGN-SITE-037`): UNVERIFIED — examine blocks only once site and license are directly accessible — **PROPOSED_ONLY**.
- **Navbar Gallery** (`DESIGN-SITE-038`): Modern responsive navbar reference for product marketing — **PROPOSED_ONLY**.
- **Aceternity UI** (`DESIGN-SITE-040`): Selective modern cards, hero and motion UI on marketing site — **PROPOSED_ONLY**.
- **Chakra UI** (`DESIGN-SITE-041`): Framework comparison only for future React Web product, not a migration — **PROPOSED_ONLY**.
- **shadcn/ui — AI Elements** (`DESIGN-SUBL-002`): Optional Web agent UI using React-compatible source and checked license — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Compare high-quality promotional hero, feature blocks and CTA and follow author links. **PROPOSED_ONLY**.
- **UIColours** (`DESIGN-SITE-043`): Export candidate CSS variables/JSON design tokens for Web identity consistency. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.


## Motion UX, animazioni e video — lotto 18 fonti 20/11/2026

[Audit licenze e compatibilita'](../sources/MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](../sources/MOTION_VIDEO_18_PIPELINE_2026-11-20.md) · [Manifest SHA](../sources/MOTION_VIDEO_18_REGISTRY_2026-11-20.json).

- **reanimate** (`MOTION-OSS-001`): Study permitted marketing scroll motion; build a distinct implementation. **PROPOSED_ONLY**.
- **mg-styles-15** (`MOTION-OSS-003`): Develop a video trailer art-direction board, not imported clips. **PROPOSED_ONLY**.
- **cinetic** (`MOTION-OSS-006`): Create product trailers using authentic captured app screens and cleared soundtracks. **PROPOSED_ONLY**.
- **motionmaxxing** (`MOTION-OSS-007`): Apply motion quality gates to video marketing deliverables. **PROPOSED_ONLY**.
- **blender-skills** (`MOTION-OSS-009`): Original lightweight 3D campaign assets, with still fallback. **PROPOSED_ONLY**.
- **three.quarks** (`MOTION-OSS-010`): Optional Three.js marketing particle accent; reduced motion and performance budget. **PROPOSED_ONLY**.
- **react-postprocessing** (`MOTION-OSS-011`): Restrained Web 3D postproduction on standalone landing page. **PROPOSED_ONLY**.
- **tweakpane** (`MOTION-OSS-012`): Debug slider controls for motion prototypes; no production leak. **PROPOSED_ONLY**.
- **skills** (`MOTION-OSS-017`): Agent-assisted video generation with Remotion engine license gate. **PROPOSED_ONLY**.
- **FFmpeg** (`MOTION-OSS-018`): Offline video mux/encode for promotional clips and web publishing. **PROPOSED_ONLY**.

**Vincoli:** il media render resta separato dal runtime APK; Flutter/Compose devono usare il donor/framework nativo prima di TSX/JavaScript; licenza dell'asset e del runtime va verificata singolarmente. Nessuna modifica a Product Bible, UI, database, funzioni, codice, build o screenshot del consumer. Priorita' estetica agli asset e mock-up gia' scelti nel Design-App; a11y, reduced motion, FPS/batteria e privacy da validare in una eventuale implementazione.


## Jiro Build e Builder — fonti Web per marketing (20/11/2026)

[Audit, deduplica e licenze](../sources/JIRO_AND_15_DESIGN_LINKS_DEDUP_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.md) · [Mappa JSON](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.json).

- **Jiro Prompt Library** (`DESIGN-SITE-044`): Study editorial landing templates, feature/FAQ/pricing/CTA patterns; design with original source or licensed project use. **PROPOSED_ONLY**.
- **Jiro Builder** (`DESIGN-SUBL-003`): Evaluate a standalone Web-site prototype with chat editing, mobile preview, code ZIP export only on an eligible paid plan. **PROPOSED_ONLY**.

**Gate:** Jiro e' una libreria proprietaria di design Web/React e un servizio esterno di hosting; nessun widget Flutter/Compose importato e nessun piano acquistato. I Termini consentono i progetti propri/clienti ma vietano ricollezionare o rivendere componenti/template standalone, il che preclude il copy del catalogo nella nostra libreria. Il Builder Free prevede limiti crediti e inattivita' e l'esportazione ZIP richiede un piano. Gli asset e mock-up preferiti gia' approvati in Design-App prevalgono; nessun codice consumer, server, auth, dati, palette, release o design deciso è stato modificato.


## Motionary + 26 nuove fonti — 20/11/2026

[Audit e licenze](../sources/MOTIONARY_26_AUDIT_2026-11-20.md) · [Mappa per app](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.md).

- **STYLE26-24** (P2): Benchmark componenti web semanticamente accessibili — **PROPOSED_ONLY**.
- **STYLE26-21** (P2): Generare proposte landing con Stitch come reference, nessun deploy non autorizzato — **PROPOSED_ONLY**.

**Gate:** Product Bible e identità visiva approvata; i componenti Web non sono widget Flutter. Nessun consumer modificato né componenti copiati. Licenze, dipendenze, accessibilità, rendering e CI da verificare per ogni adozione.
