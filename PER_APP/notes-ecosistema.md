# Notes-Ecosistema — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/notes-ecosistema.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/notes-ecosistema.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Workspace editoriale note/canvas, gerarchia leggibile, comandi semantici in equilibrio con UI bento.

**Categorie da studiare:** nota · cartelle · canvas · tag/bookmark · import/export.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. editor note e barra formattazione.
2. canvas e selezione strumenti.
3. ricerca e bookmark.
4. import/export.
5. stati protetti se disponibili.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | download esportazioni | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | HIGH | esportazione note | VERIFIED_DETAIL |
| [ICO-007 · import](https://gentleface.com/icons/import) | HIGH | import note | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | MEDIUM | immagini nelle note | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | HIGH | segnalibri note | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca note e canvas | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | strumenti visuali opzionali | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | MEDIUM | import o indicizzazione reale | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | modifica salvata | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | sync solo se backend attivo | VERIFIED_SITE |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | ripeti azione solo se reversibile | VERIFIED_DETAIL |
| [ICO-023 · eye](https://gentleface.com/icons/eye) | HIGH | mostra/nascondi pannello o contenuto | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | HIGH | archivio note con restore | VERIFIED_SITE |
| [ICO-025 · messages](https://gentleface.com/icons/messages) | MEDIUM | commenti collaborativi solo dove supportati | VERIFIED_DETAIL |
| [ICO-028 · lock](https://gentleface.com/icons/lock) | MEDIUM | sezioni protette solo se presenti | ANIMATION_UNVERIFIED |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `search`, `bookmark`, `export`.

## Animazioni e feedback proposti

- focus visivo del tool attivo.
- conferma salvataggio e sync solo se completati.
- minimo motion durante disegno a mano libera.

## Cosa evitare

- animazione nel tracciato ink che compromette precisione.
- toolbar troppo ricche.
- stati di sync non verificati.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | editor and responsive workflow refinement |
| DSK-002 — Impeccable | HIGH | editor density, hierarchy and responsive review |
| DSK-003 — Taste Skill | MEDIUM | web product landing, not the native editor |
| DSK-004 — Emil Design Engineering | HIGH | canvas/drag/selection and feedback |
| DSK-005 — Vercel Web Design Guidelines | HIGH | web editor/desktop accessibility |
| DSK-006 — Anthropic Frontend Design | HIGH | knowledge-workspace information hierarchy |
| DSK-007 — Hallmark | MEDIUM | landing feature stories |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | complex editor and long-text states |
| DSK-009 — UI UX Pro Max | HIGH | editor/canvas design-token consistency |
| DSK-010 — Stageshow | HIGH | workspace feature illustrations and demo |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Voice Orb — proposta futura (HIGH)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Note vocali e dettatura nell'editor.
- **Collocazione candidata:** Composer note/canvas.
- **Adattamento estetico:** palette editoriale attuale.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (HIGH)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Reveal visual board cover, not editor controls. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (MEDIUM):** Desktop web canvas hover option when drawing disabled. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Flashcard-style note study mode only if feature exists. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Long web notes and knowledge collections. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Switch workspaces when navigation is approved. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Real indexing/import/synchronization and pending note tasks. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Bacheca raccolta visuale, non l'editor principale. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (MEDIUM)** — Timeline registrazione vocale futura o revisioni. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (MEDIUM)** — Filtri data modifica o dimensione contenuti. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Login opzionale di sync se introdotto. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (HIGH)** — Invita collaboratore per spazio condiviso solo se autorizzato. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Task del giorno se la feature task è presente. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-001 · Accordion Loader (HIGH)** — Attesa indicizzazione o import effettiva. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/accordion-loader.tsx); già censito: `AMX-006`. Stato: `PROPOSED_ONLY`.
- **DBM-002 · Classic Spinner (HIGH)** — Apertura file o nota durante I/O. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/classic-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-003 · Pulsating Dots (HIGH)** — Salvataggio o recupero breve. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/pulsating-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-007 · Apple Breathe (MEDIUM)** — Salvataggio breve. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-breathe.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-010 · Apple Pulse Dots (HIGH)** — Indicatore salvataggio dati. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-pulse-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-011 · Morph Loader (MEDIUM)** — Caricamento bacheca. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/morph-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-015 · Intersecting Rings (HIGH)** — Sync reale note. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/intersecting-rings.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-016 · Skeleton (HIGH)** — Blocchi editoriali durante I/O, con layout stabile. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/skeleton.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-021 · Notification List (MEDIUM)** — Scadenze se feature presente. Evidenza: `EXACT_SOURCE_NOT_LOCATED`; sorgente esatto da identificare; già censito: `WML-008`. Stato: `PROPOSED_ONLY`.
- **DBM-023 · Conveyor Loop (MEDIUM)** — Import note reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/conveyor-loop.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-028 · Loader (MEDIUM)** — Studio semantica di caricamento. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-029 · Particle Shape Morph (MEDIUM)** — Vision board su web con riduzione movimento. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 12 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P1**, modalità `OPERATE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Editor, canvas, ricerca, Smart Inbox.
- **Miglioramento proposto:** Usare una gerarchia di comandi leggibile per il canvas e limitare la cascata di toolbar; distinguere cattura, modifica, sync e ricerca da decorazioni.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Canvas fruibile con tastiera/zoom e senza overlay sui controlli
  - [ ] Ricerca e filtri chiari con zero-result, loading ed errore
  - [ ] Valori e impostazioni conservano lo stato quando si cambia sezione
  - [ ] App non presenta salvataggio riuscito se non confermato

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-002, DCL-004, DCL-007, DCL-010, DCL-011.
- **Schermate:** Workspace, Inbox, Canvas, Web.
- **Vincolo:** Densità da workspace, niente dashboard scenografica senza funzione.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-001 — [alexruix/tame-fly-42](https://uiverse.io/alexruix/tame-fly-42)**: Caricamento effettivo durante elaborazione (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html).
- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (HIGH). Originale da estrarre.
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**67 preferiti proposti per notes-ecosistema**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-001](https://uiverse.io/alexruix/tame-fly-42) | LOADER | Caricamento effettivo durante elaborazione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html) |
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-016](https://uiverse.io/Gidarx/clever-panther-6) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.css) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-019](https://uiverse.io/JkHuger/new-deer-97) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca e filtri testuali | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-027](https://uiverse.io/Nawsome/empty-snail-69) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-027_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-032](https://uiverse.io/Praashoo7/lucky-hound-44) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-042](https://uiverse.io/Shoh2008/yellow-dolphin-16) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html) |
| [UIV-043](https://uiverse.io/Stavros2410/wet-duck-69) | INPUT | Ricerca e filtri delle note con label accessibile | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.css) |
| [UIV-045](https://uiverse.io/Uncannypotato69/honest-starfish-32) | CHECKBOX | Checklist note o attività con stato reale | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.css) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-049](https://uiverse.io/andrew-demchenk0/honest-stingray-90) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-049_original.html) |
| [UIV-050](https://uiverse.io/andrew-manzyk/fast-vampirebat-53) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.css) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-052](https://uiverse.io/ashif_6672/rare-bat-68) | CARD | Card di raccolta e workspace | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.css) |
| [UIV-053](https://uiverse.io/barisdogansutcu/plastic-dolphin-67) | TOOLTIP | Aiuto contestuale non solo hover | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-058](https://uiverse.io/cssbuttons-io/mean-dolphin-24) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-058_original.html) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-063](https://uiverse.io/dexter-st/tough-falcon-78) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.css) |
| [UIV-064](https://uiverse.io/dopekid_9309/tiny-dog-80) | BUTTON | CTA aggiunta o apertura nota | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-067](https://uiverse.io/elijahgummer/young-horse-7) | RADIO | Scelta esclusiva accessibile | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.css) |
| [UIV-068](https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione con semantica e feedback | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-071](https://uiverse.io/gharsh11032000/sour-vampirebat-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-071_original.html) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-078](https://uiverse.io/kennyotsu/giant-sloth-18) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.css) |
| [UIV-079](https://uiverse.io/kennyotsu/selfish-bear-69) | CARD | Card anteprima nota | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.css) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-082](https://uiverse.io/kennyotsu/wise-rattlesnake-92) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html) |
| [UIV-083](https://uiverse.io/kennyotsu/wonderful-firefox-31) | CARD | Card anteprima collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.css) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-085](https://uiverse.io/m1her/odd-fireant-56) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.css) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-088](https://uiverse.io/mobinkakei/great-skunk-8) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-088_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-093](https://uiverse.io/preet_7613/new-cougar-63) | CARD | Card nota o collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.css) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Scheda nota o lavagna | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Scheda nota o lavagna | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture opzionale fuori dall'area scrittura | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Ricerca semantica/indicizzazione solo se avviata | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**9 nuove associazioni** da originali HTML/CSS pubblici Uiverse, nessuna modifica runtime dell'app.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-101](https://uiverse.io/Javierrocadev/chatty-ladybug-95) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.css) |
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-103](https://uiverse.io/SyedShahzaib7/brave-dog-61) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Indicizzazione/esportazione reale con stato di errore e retry | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |
| [UIV-109](https://uiverse.io/mamyapro123/curvy-bear-51) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Spiegazione strumenti canvas e note | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Modulo nome lavagna, titolo nota o workspace, dati locali | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Stato: **PROPOSED_ONLY**; nessuna nuova funzione/login è autorizzata da questi suggerimenti.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi dei nuovi 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).

## Flutter Gems / Forui / F22 — librerie UI native (18/11/2026)

Fonti: [Flutter Gems](https://fluttergems.dev/), [Forui Button](https://forui.dev/docs/widgets/form/button) e [F22 Labs 2026](https://www.f22labs.com/blogs/top-8-flutter-ui-libraries-for-2025-you-must-explore/). [Matrice bidirezionale](../UI-UX/FLUTTER_UI_LIBRARIES_APP_MAP_2026-11-18.json). **PROPOSED_ONLY, NOT_VERIFIED**: prima rispettare le reference utente in Design-App e Product Bible, poi verificare il package originale e il codice consumer.

| Libreria | Fit | Uso ipotizzato |
| --- | --- | --- |
| Forui | HIGH | responsive workspaces/forms |
| Mix | HIGH | tokens for adaptive UI |
| shadcn_ui | MEDIUM | panel reference |
| FL Chart | MEDIUM | charts backed by real data |

Nessun package installato, nessuna modifica dati/architettura o Golden promosso; verifica Flutter SDK, dipendenze, APK size, accessibilità e performance necessaria prima dell'adozione.


## DSK-011 — Unslop UI, audit sottrattivo (19/11/2026)

**PROPOSED_ONLY · fonte OSS MIT** [felipebasurto/unslop-ui @ cd891160453f26aaacc569bad96a8d10d595076d](https://github.com/felipebasurto/unslop-ui/tree/cd891160453f26aaacc569bad96a8d10d595076d). [Audit e limiti](../sources/UNSLOP_UI_AUDIT_2026-11-19.md) · [matrice di associazione](../UI-UX/UNSLOP_UI_APP_MAP_2026-11-19.json).

**Proposta:** Workspace e canvas: ridurre decoro e ripetizioni solo dopo aver tutelato densità utile, editor, navigazione e persistenza. Le U1–U20 sono controlli diagnostici e alias degli AT-01…AT-64, non un nuovo tema. Riutilizzo **ADAPT_NATIVE / SOURCE_REVIEW**; nessun automatismo rimuove elementi, nessun consumer certificato da questo dossier. Product Bible e reference preferite restano prioritarie. Stato visivo/fisico: **NOT_VERIFIED**.


## Fonti esterne aggiunte — 20/11/2026 (15 URL, 14 servizi unici)

Intake visivo documentale: [audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice per app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro JSON](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Recent Design** (`DESIGN-SITE-018`): App icon and typography moodboards. **Stato: PROPOSED_ONLY**.
- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press. **Stato: PROPOSED_ONLY**.
- **Fontshare** (`DESIGN-SITE-022`): Pair serif editorial headings with neutral readable UI fonts. **Stato: PROPOSED_ONLY**.
- **Realtime Colors** (`DESIGN-SITE-023`): Preview text/background/primary/secondary/accent combinations on real UI. **Stato: PROPOSED_ONLY**.
- **Lucide** (`DESIGN-SITE-025`): Consistent stroke and semantic icon naming. **Stato: PROPOSED_ONLY**.
- **SVGL** (`DESIGN-SITE-026`): Find official provider logos for legitimate integration badges. **Stato: PROPOSED_ONLY**.
- **Shots** (`DESIGN-SITE-027`): Create marketing phone/device mockups from own QA screenshots. **Stato: PROPOSED_ONLY**.
- **Cosmos** (`DESIGN-SITE-028`): Moodboard collections and search by color/similarity. **Stato: PROPOSED_ONLY**.

I pattern richiedono decisione di prodotto, valutazione della licenza e QA sulla schermata target. Nessun componente, font, foto o logo di terzi e' stato copiato; nessuna funzione consumer risulta implementata da questo intake.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study modular note editor, canvas and productivity mobile flow templates. **PROPOSED_ONLY**.
- **ReUI** (`DESIGN-SITE-031`): Study task Kanban and rich filters as Web/UX references, not Flutter-ready code. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): Workspace bento of recent notes, projects, favorites, tasks and actionable capture. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **ThinkUI** (`DESIGN-SITE-032`): Review genuine capture/editor/empty-state UX with sources and state completeness — **PROPOSED_ONLY**.
- **Mobbin** (`DESIGN-SITE-033`): Study transitions from note listing to editor to collections and share/export — **PROPOSED_ONLY**.
- **React Bits** (`DESIGN-SITE-034`): Study animated list, collapsible details and card reveals; adapt natively in Flutter — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **Navbar Gallery** (`DESIGN-SITE-038`): Reference multi-level Web content navigation without importing desktop nav on mobile — **PROPOSED_ONLY**.
- **AI Canvas** (`DESIGN-SITE-039`): Signature pad and task cards, native Flutter adaptation only — **PROPOSED_ONLY**.
- **Chakra UI** (`DESIGN-SITE-041`): Accessible dialogs/actions as Web reference for native rewrite — **PROPOSED_ONLY**.
- **ReUI — Agent Ops Pro Blocks** (`DESIGN-SUBL-001`): Agent action queue as candidate only if AI functionality is product-approved — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Discover genuine dashboard/canvas interaction concepts and patterns, not clone social artwork. **PROPOSED_ONLY**.
- **UIColours** (`DESIGN-SITE-043`): Create candidate semantic tokens for ink, canvas, card, labels, accents and accessible contrast. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.


## Motion UX, animazioni e video — lotto 18 fonti 20/11/2026

[Audit licenze e compatibilita'](../sources/MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](../sources/MOTION_VIDEO_18_PIPELINE_2026-11-20.md) · [Manifest SHA](../sources/MOTION_VIDEO_18_REGISTRY_2026-11-20.json).

- **motion-design-skill** (`MOTION-OSS-002`): Set canvas interaction motion tokens for drag, zoom and tool changes. **PROPOSED_ONLY**.

**Vincoli:** il media render resta separato dal runtime APK; Flutter/Compose devono usare il donor/framework nativo prima di TSX/JavaScript; licenza dell'asset e del runtime va verificata singolarmente. Nessuna modifica a Product Bible, UI, database, funzioni, codice, build o screenshot del consumer. Priorita' estetica agli asset e mock-up gia' scelti nel Design-App; a11y, reduced motion, FPS/batteria e privacy da validare in una eventuale implementazione.


## Jiro Build e Builder — fonti Web per marketing (20/11/2026)

[Audit, deduplica e licenze](../sources/JIRO_AND_15_DESIGN_LINKS_DEDUP_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.md) · [Mappa JSON](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.json).

- **Jiro Prompt Library** (`DESIGN-SITE-044`): Explore feature storytelling for canvas, notebooks and privacy with genuine app screen captures. **PROPOSED_ONLY**.
- **Jiro Builder** (`DESIGN-SUBL-003`): Use Builder only to mock up a product marketing site, not authentication, realtime sync or the notes canvas. **PROPOSED_ONLY**.

**Gate:** Jiro e' una libreria proprietaria di design Web/React e un servizio esterno di hosting; nessun widget Flutter/Compose importato e nessun piano acquistato. I Termini consentono i progetti propri/clienti ma vietano ricollezionare o rivendere componenti/template standalone, il che preclude il copy del catalogo nella nostra libreria. Il Builder Free prevede limiti crediti e inattivita' e l'esportazione ZIP richiede un piano. Gli asset e mock-up preferiti gia' approvati in Design-App prevalgono; nessun codice consumer, server, auth, dati, palette, release o design deciso è stato modificato.


## Motionary + 26 nuove fonti — 20/11/2026

[Audit e licenze](../sources/MOTIONARY_26_AUDIT_2026-11-20.md) · [Matrice 20 proposte / 10 app](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.md). Le fonti nuove non sostituiscono mock-up già approvati, Product Bible, Golden o design token proprietari.

- **STYLE26-01** (P1): Microinterazioni card/board, espansione proprietà e undo con reduced motion — **PROPOSED_ONLY**.
- **STYLE26-25** (P2): Confronto canvas solo pattern; niente nuovo database o copia codice senza gate — **PROPOSED_ONLY**.

**Confini:** 0 componenti SwiftUI/TSX importati nel consumer; per Flutter/Compose serve implementazione compatibile e collaudo. Le licenze dei siti e delle risorse premium/media restano distinte. Motionary MIT richiede notice; Rare UI vieta redistribuzione di un port/libreria di componenti e impone attribuzione in prodotto quando applicabile. Nessun codice, dato, permesso, APK, design scelto o runtime consumer è stato modificato.
