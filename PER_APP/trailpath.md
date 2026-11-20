# TrailPath — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/trailpath.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Mappe outdoor forest/moss con controlli robusti e alto contrasto sul percorso.

**Temi candidati:** mappa; traccia; waypoint; offline.

## Superfici e placement proposti

1. selezione waypoint.
2. routing e stato GPS reale.
3. download GPX/mappe solo se funzione attiva.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | waypoint e posizione | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** map-pin, download, check. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- pulse waypoint solo dopo selezione.
- nessun motion che copra la rotta o i controlli.

## Cosa evitare

- UI decorativa che oscura la cartografia.
- presentare routing non funzionante come confermato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-004 — Emil Design Engineering | HIGH | map control and route-state transitions |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | map touch targets and offline states |
| DSK-009 — UI UX Pro Max | HIGH | map utility and nature-tech |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (MEDIUM)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Route notes, never GPS map overlay. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (MEDIUM)** — Timeline percorso registrato solo se disponibile. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-024 · View On Map (HIGH)** — Dettaglio waypoint senza sostituire routing attuale. Evidenza: `SOURCE_FILE_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/view-on-map/base.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 1 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-001, DCL-005, DCL-007.
- **Schermate:** Mappa, percorso, statistiche.
- **Vincolo:** Routing e posizione corretti prima del polish.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse Favorites — archivio incrociato 18/11/2026

**4 preferiti proposti per trailpath**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa routing/traccia GPS reale con timeout/retry | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Scelta esclusiva accessibile | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa routing/traccia GPS reale con timeout/retry | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Card di anteprima/collezione | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**1 nuovi collegamenti** all'archivio Uiverse. Proposte estetiche, non modifiche funzionali o test runtime.

| Sorgente | Categoria | Superficie proposta | Fit | Codice originale |
|---|---|---|---|---|
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Attesa routing GPS con fallback errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |

Stato: **PROPOSED_ONLY**. Per il riuso rispettare Product Bible, accessibilità e test; loader solo per lavoro realmente attivo; nessuna autenticazione obbligatoria nuova.
[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## Fonti di design — 20/11/2026

[Audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press — **PROPOSED_ONLY**.
- **Realtime Colors** (`DESIGN-SITE-023`): Preview text/background/primary/secondary/accent combinations on real UI — **PROPOSED_ONLY**.

Nessun asset, font, logo o codice importato. Sono richiesti approvazione estetica, Product Bible, licenza e QA sulle schermate reali.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **ThinkUI** (`DESIGN-SITE-032`): Review offline navigation and failed-routing states from real interfaces — **PROPOSED_ONLY**.
- **Mobbin** (`DESIGN-SITE-033`): Benchmark GPS permission, no-route and retry UX from shipped navigation apps — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.
