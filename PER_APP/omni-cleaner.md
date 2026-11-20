# Omni Cleaner — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/omni-cleaner.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/omni-cleaner.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Riconciliazione consumer — PR #35 e P1/P2 · 18/11/2026

**Evidenza consumer verificata:** Android Omni Cleaner PR #35 **merged** su main, commit `b2bd4381ddd6e7e880eebb3a25b6bee03d9aafec`, CI Android e screenshot API 35 PASS sul source head `3ae3487a164bb4eedb9cb0b4068477e074c22a31`; 20 screenshot sottoposti ad audit visivo. Il testo storico `PROPOSAL_ONLY` di questo dossier si riferisce esclusivamente all'intake del catalogo del 17 novembre, **non allo stato attuale del consumer**.

**Pattern adattati nel consumer (non import di codice di terzi):**
- `UIX-STYLE-006` / `DCL-002`: raggruppamento delle nove funzioni Clean, status `SOURCE_IMPLEMENTED / CI_TESTED`.
- `UIX-STYLE-009` / `DCL-007`: schede navigazione Privacy e Pro, status `SOURCE_IMPLEMENTED / CI_TESTED`.
- `DCL-004`: navigazione su schermate dedicate, status `SOURCE_IMPLEMENTED / CI_TESTED`.
- `DCL-006`: foto/video con `ContentScale.Fit` e video fullscreen nativo, status `SOURCE_IMPLEMENTED / EMULATOR_SMOKE`; la resa visiva dei fotogrammi non è ancora certificata.
- `DCL-005`: stati reali di scansione, nessun progresso inventato, status `SOURCE_IMPLEMENTED / CI_TESTED`.
- `WML-003`: idea di timeline, adattata tramite `VideoView + MediaController`, **non componente Watermelon implementato direttamente**.

**Correzioni aperte:** [PR #37](https://github.com/riccardopinato/Android-Omni-Cleaner/pull/37), ramo P1/P2 **DRAFT / CI_PENDING** al momento di questa annotazione. Include filtri Gallery responsive, selected states, gerarchia CTA, Bento, messaggi/provider e fixture video luminosa. Non promuovere nessuna di queste correzioni a `CI_TESTED` o `RUNTIME_VISUAL_REVIEWED` finché i gate esatti e la revisione delle nuove schermate non passano.

**Nessuna promozione implicita dei donor originali:** catalogo Uiverse, Watermelon, Gentleface e stili restano `REFERENCE / PROPOSED_ONLY` come componenti terzi. La precedente lista di fonti e preferenze resta integra, così come le condizioni di licenza e verifica.

## Identità e direzione visiva

Utility di pulizia con schermate separate e UI fluida: galleria foto/video a formato originale e player reale.

**Categorie da studiare:** galleria · video · eliminazione sicura · scansione · archivio.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. pulsanti per accedere alle singole funzioni.
2. galleria foto senza ritagli.
3. video player con play/pause e decisione prima dell'eliminazione.
4. scansione e progresso reale.
5. conferma eliminazione con reversibilità ove disponibile.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-005 · download](https://gentleface.com/icons/download) | MEDIUM | download solo se esiste funzione | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | HIGH | apertura galleria a dimensione intera | VERIFIED_DETAIL |
| [ICO-009 · video](https://gentleface.com/icons/video) | HIGH | player video in galleria | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | MEDIUM | filtri media e file | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | scansione in corso, mai fingere progressi | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | operazione completata con successo | VERIFIED_SITE |
| [ICO-020 · play](https://gentleface.com/icons/play) | HIGH | riproduzione video reale | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | HIGH | pausa player video | VERIFIED_SITE |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | loop player video se presente | VERIFIED_DETAIL |
| [ICO-023 · eye](https://gentleface.com/icons/eye) | HIGH | anteprima contenuti multimediali | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `images`, `video`, `play`, `pause`, `check`.

## Animazioni e feedback proposti

- transizione apertura galleria o player una sola volta.
- play/pause con stato leggibile.
- loader solo su scansione reale.

## Cosa evitare

- simulare la liberazione di spazio prima di terminarla.
- autoeliminare asset o presentare anteprime ritagliate.
- inseguire il design sacrificando frame rate.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | MEDIUM | less generic utility UI and state feedback |
| DSK-002 — Impeccable | HIGH | dedicated feature screens and gallery/video UX checks |
| DSK-004 — Emil Design Engineering | HIGH | smooth transitions between function screens |
| DSK-006 — Anthropic Frontend Design | MEDIUM | distinctive but restrained utility aesthetic |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | feature navigation, gallery and media controls |
| DSK-009 — UI UX Pro Max | HIGH | utility redesign with component variants |
| DSK-010 — Stageshow | MEDIUM | feature-page visuals using actual app flows |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (MEDIUM)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (HIGH)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Media galleries only when not virtualized. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Media scanning and file analysis only while truly active. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Anteprima di una selezione limitata, non galleria di eliminazione massiva. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (HIGH)** — Seek timeline video in player. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (HIGH)** — Filtra media per durata/dimensione/periodo non sostituisce anteprima. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-001 · Accordion Loader (HIGH)** — Analisi file in corso. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/accordion-loader.tsx); già censito: `AMX-006`. Stato: `PROPOSED_ONLY`.
- **DBM-002 · Classic Spinner (HIGH)** — Task breve con stato di attesa. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/classic-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-004 · App Icon Load (MEDIUM)** — Preparazione galleria media. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/app-icon-load.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-006 · Stacked Bar Pulse (HIGH)** — Scansione media in corso. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/stacked-bar-pulse.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-012 · Grid Dots (HIGH)** — Scansione batch media. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/grid-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-014 · Circular Bars (HIGH)** — Scansione e analisi effettiva. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/circular-bars.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-018 · Range Selection Slider (HIGH)** — Filtro dimensione/durata media. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/range-selection-slider/base.tsx); già censito: `WML-004`. Stato: `PROPOSED_ONLY`.
- **DBM-019 · Bar Cascade (HIGH)** — Analisi galleria in corso. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bar-cascade.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-020 · Concentric Squares (MEDIUM)** — Analisi contenuti. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-squares.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-022 · Bar Sweep (HIGH)** — Scansione file reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bar-sweep.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-023 · Conveyor Loop (MEDIUM)** — Elaborazione batch. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/conveyor-loop.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-026 · Newtons Cradle (MEDIUM)** — Scansione, solo se non rallenta UI. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/newtons-cradle.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-027 · Helix Spinner (MEDIUM)** — Loader sperimentale solo se costo grafico sostenibile. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-028 · Loader (MEDIUM)** — Selezione futura del loader coerente. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 14 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P1**, modalità `OPERATE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Home, schede funzione dedicate, galleria, player.
- **Miglioramento proposto:** Limitare la complessità della Home; trasformare azioni in schermate dedicate con stato esplicito; mostrare foto/video senza crop e con riproduzione verificata.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Galleria originale fit-contain e controlli video raggiungibili
  - [ ] Conferma distruttiva chiara e reversibilità quando possibile
  - [ ] Skeleton e spinner solo durante scansioni effettive
  - [ ] Navigazione e controlli senza ritagli su schermi stretti

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-002, DCL-004, DCL-005, DCL-006, DCL-007.
- **Schermate:** Home funzioni, scansione, galleria e player.
- **Vincolo:** No micro-animazioni nelle operazioni distruttive; foto/video a proporzioni originali.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-001 — [alexruix/tame-fly-42](https://uiverse.io/alexruix/tame-fly-42)**: Caricamento effettivo durante elaborazione (HIGH). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.
- **UIV-006 — [JustCode14/red-dingo-61](https://uiverse.io/JustCode14/red-dingo-61)**: Toggle semantico legato a impostazione reale (MEDIUM). Originale da estrarre.
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (HIGH). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**50 preferiti proposti per omni-cleaner**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-001](https://uiverse.io/alexruix/tame-fly-42) | LOADER | Caricamento effettivo durante elaborazione | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html) |
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-006](https://uiverse.io/JustCode14/red-dingo-61) | SWITCH | Toggle semantico legato a impostazione reale | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.css) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-013](https://uiverse.io/AqFox/young-dragon-29) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html) |
| [UIV-018](https://uiverse.io/JaydipPrajapati1910/average-shrimp-57) | SWITCH | Impostazioni scansione persistite | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-018_original.html) |
| [UIV-019](https://uiverse.io/JkHuger/new-deer-97) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca o inserimento con label | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-026](https://uiverse.io/Nawsome/brave-turtle-26) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html) |
| [UIV-027](https://uiverse.io/Nawsome/empty-snail-69) | SWITCH | Impostazioni scansione persistite | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-027_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-031](https://uiverse.io/Novaxlo/rotten-lionfish-4) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.css) |
| [UIV-032](https://uiverse.io/Praashoo7/lucky-hound-44) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-036](https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-041](https://uiverse.io/Shoh2008/ugly-elephant-80) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html) |
| [UIV-042](https://uiverse.io/Shoh2008/yellow-dolphin-16) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html) |
| [UIV-043](https://uiverse.io/Stavros2410/wet-duck-69) | INPUT | Ricerca file per nome con feedback chiaro | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.css) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-045](https://uiverse.io/Uncannypotato69/honest-starfish-32) | CHECKBOX | Selezione media prima di ogni eliminazione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.css) |
| [UIV-050](https://uiverse.io/andrew-manzyk/fast-vampirebat-53) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.css) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-052](https://uiverse.io/ashif_6672/rare-bat-68) | CARD | Card di riepilogo risultati | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.css) |
| [UIV-053](https://uiverse.io/barisdogansutcu/plastic-dolphin-67) | TOOLTIP | Aiuto contestuale non solo hover | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-064](https://uiverse.io/dopekid_9309/tiny-dog-80) | BUTTON | CTA per avviare scansione o aprire i risultati | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-068](https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione duplicati con preview/undo | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-072](https://uiverse.io/gsperandio/shaggy-kangaroo-12) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-079](https://uiverse.io/kennyotsu/selfish-bear-69) | CARD | Card per gruppo di duplicati | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.css) |
| [UIV-083](https://uiverse.io/kennyotsu/wonderful-firefox-31) | CARD | Card risultato di scansione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.css) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-088](https://uiverse.io/mobinkakei/great-skunk-8) | SWITCH | Impostazioni scansione persistite | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-088_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-093](https://uiverse.io/preet_7613/new-cougar-63) | CARD | Card riepilogo archiviazione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.css) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-096](https://uiverse.io/solowzrd/wet-lionfish-63) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.css) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Scansione memoria/duplicati con stato reale | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**2 nuove associazioni** da originali HTML/CSS pubblici Uiverse, nessuna modifica runtime dell'app.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Feedback scansione duplicati effettivamente avviata | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Informazioni su file duplicati prima della cancellazione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |

Stato: **PROPOSED_ONLY**; nessuna nuova funzione/login è autorizzata da questi suggerimenti.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi dei nuovi 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## DSK-011 — Unslop UI, audit sottrattivo (19/11/2026)

**PROPOSED_ONLY · fonte OSS MIT** [felipebasurto/unslop-ui @ cd891160453f26aaacc569bad96a8d10d595076d](https://github.com/felipebasurto/unslop-ui/tree/cd891160453f26aaacc569bad96a8d10d595076d). [Audit e limiti](../sources/UNSLOP_UI_AUDIT_2026-11-19.md) · [matrice di associazione](../UI-UX/UNSLOP_UI_APP_MAP_2026-11-19.json).

**Proposta:** Kotlin/Compose: valuta eyebrow non pertinenti, badge/dot di stato, grafici e pulizia della gerarchia; non alterare RC1, funzioni distruttive o la Home approvata. Le U1–U20 sono controlli diagnostici e alias degli AT-01…AT-64, non un nuovo tema. Riutilizzo **ADAPT_NATIVE / SOURCE_REVIEW**; nessun automatismo rimuove elementi, nessun consumer certificato da questo dossier. Product Bible e reference preferite restano prioritarie. Stato visivo/fisico: **NOT_VERIFIED**.


## Fonti di design — 20/11/2026

[AUDIT delle 15 fonti](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press — **PROPOSED_ONLY**.
- **Realtime Colors** (`DESIGN-SITE-023`): Preview text/background/primary/secondary/accent combinations on real UI — **PROPOSED_ONLY**.
- **Lucide** (`DESIGN-SITE-025`): Consistent stroke and semantic icon naming — **PROPOSED_ONLY**.
- **Shots** (`DESIGN-SITE-027`): Create marketing phone/device mockups from own QA screenshots — **PROPOSED_ONLY**.

Nessuna feature o risorsa esterna e' stata integrata. Richiesti Product Bible, approvazione estetica, licenze e QA runtime.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study storage cleaner permission, empty-state and confirmation flow patterns. **PROPOSED_ONLY**.
- **ReUI** (`DESIGN-SITE-031`): Adapt data table, filter and safe multi-step destructive action UX only if relevant. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): Storage and gallery overview tiles showing real scan results; respect safe delete and empty states. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **ThinkUI** (`DESIGN-SITE-032`): Benchmark safe review-delete-trash-undo flows without acquiring third-party screenshots — **PROPOSED_ONLY**.
- **Mobbin** (`DESIGN-SITE-033`): Inspect full consent, gallery preview, multi-select and deletion confirmation journey — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **AI Canvas** (`DESIGN-SITE-039`): Delete-with-undo countdown only with genuinely reversible trash operation — **PROPOSED_ONLY**.
- **Chakra UI** (`DESIGN-SITE-041`): Confirm-dialog and safe destructive action semantics — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Study distinct media-gallery and utility card composition, preserving current Color Bento direction. **PROPOSED_ONLY**.
- **UIColours** (`DESIGN-SITE-043`): Check Color Bento palette readability and status/destructive colour semantics using preview and contrast checks. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.
