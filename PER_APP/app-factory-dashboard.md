# App Factory Dashboard — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/app-factory-dashboard.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/app-factory-dashboard.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Pannello operativo tecnico: densità controllata, bento strutturato, badge semantici e qualità visiva verificabile.

**Categorie da studiare:** repository e branch · capability/Golden · CI e build · priorità.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. stato CI/PR/merge.
2. ricerca repository e capability.
3. schede progetti e dipendenze.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca repository e capability | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | scoperta capability | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | job realmente verificato | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | HIGH | stato CI/portfolio | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `check`, `search`, `gauge`.

## Animazioni e feedback proposti

- conferma job solo dopo risposta GitHub.
- caricamento soltanto durante richieste effettive.

## Cosa evitare

- animazioni che fanno apparire eseguiti task non avvenuti.
- mini-illustrazioni che nascondono lo stato.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | consistent design language and preview QA |
| DSK-002 — Impeccable | HIGH | cross-app visual acceptance gate |
| DSK-003 — Taste Skill | HIGH | web landing and narrative hero |
| DSK-005 — Vercel Web Design Guidelines | HIGH | keyboard navigation, responsive dashboards and forms |
| DSK-006 — Anthropic Frontend Design | MEDIUM | non-generic web dashboard identity |
| DSK-007 — Hallmark | MEDIUM | public project showcase, not operations UI |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | responsive dashboard QA |
| DSK-009 — UI UX Pro Max | HIGH | cross-product visual catalog |
| DSK-010 — Stageshow | HIGH | portfolio project teasers |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Voice Orb — proposta futura (MEDIUM)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Cattura vocale di idee o note di progetto.
- **Collocazione candidata:** Composer idea/nota.
- **Adattamento estetico:** UI tecnica e leggibile.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

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

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Optional visual feature showcase. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (HIGH):** Desktop web navigation experimentation. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Portfolio project front/back preview only. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Long dashboard sections on desktop web. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Workspace section showcase with stable route. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Fetching CI/repository statuses, not fake build progress. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Questa sezione contiene **proposte**; nessuna libreria installata, nessuna feature consumer confermata dal solo catalogo.

- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (HIGH)** — Accesso dashboard web solo se auth reale esiste. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Header promozionale soltanto, non badge CI. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (HIGH)** — Invita teammate ai workspace solo con backend permessi e ruoli. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Bloccanti operativi del giorno se derivati da stati reali. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.


**Gate comune:** rispettare Product Bible, accessibilità, controlli di input alternativi, riduzione movimento, performance, colore e lingua; Flutter/Compose richiedono adattamento nativo dei componenti React. I riferimenti `Text Gradient`, `Notification List` e `Flip Clock` non hanno un file componente esatto verificato alla baseline e restano `REFERENCE`.

**Storico 17/11/2026:** proposte inserite in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, con provenienza e stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-001 · Accordion Loader (HIGH)** — Fetch stato CI. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/accordion-loader.tsx); già censito: `AMX-006`. Stato: `PROPOSED_ONLY`.
- **DBM-006 · Stacked Bar Pulse (MEDIUM)** — Elaborazione stato progetto. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/stacked-bar-pulse.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-009 · Terminal Loader (HIGH)** — Task di pipeline CI con output reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/terminal-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-012 · Grid Dots (HIGH)** — Caricamento repository/capability. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/grid-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-014 · Circular Bars (MEDIUM)** — Elaborazione metrica. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/circular-bars.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-016 · Skeleton (HIGH)** — Dashboard con placeholder stabili. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/skeleton.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-019 · Bar Cascade (MEDIUM)** — Elaborazione batch. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bar-cascade.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-020 · Concentric Squares (MEDIUM)** — Inizializzazione vista dati. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-squares.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-021 · Notification List (MEDIUM)** — Attività operative se pianificate. Evidenza: `EXACT_SOURCE_NOT_LOCATED`; sorgente esatto da identificare; già censito: `WML-008`. Stato: `PROPOSED_ONLY`.
- **DBM-023 · Conveyor Loop (HIGH)** — Coda job effettiva. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/conveyor-loop.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-026 · Newtons Cradle (MEDIUM)** — Task pipeline in attesa. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/newtons-cradle.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-028 · Loader (HIGH)** — Reference comparativa tra spinner, dots, bars e varianti. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 12 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P1**, modalità `OPERATE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Progetti, Golden, donor, blocchi, roadmap.
- **Miglioramento proposto:** Distinguere implementato/verificato e PR aperte/merge; ridurre duplicazioni di card e far emergere decisioni e blocchi.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Stato mostrato con evidenza e ultima verifica, non solo colore
  - [ ] Filtri efficienti e gestione empty/error
  - [ ] Keyboard focus e responsive table/list
  - [ ] Non confondere progressi proposti con certificati

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-002, DCL-005, DCL-010.
- **Schermate:** Portfolio, roadmap, stato e gate.
- **Vincolo:** Separare implementato, verificato e roadmap; non simulare CI.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**46 preferiti proposti per app-factory-dashboard**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-016](https://uiverse.io/Gidarx/clever-panther-6) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.css) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca o inserimento con label | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Scheda donor/capability/Golden | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-045](https://uiverse.io/Uncannypotato69/honest-starfish-32) | CHECKBOX | Checklist dei controlli di verifica | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-045_original.css) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-053](https://uiverse.io/barisdogansutcu/plastic-dolphin-67) | TOOLTIP | Stato e significato di una capability | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-063](https://uiverse.io/dexter-st/tough-falcon-78) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Scheda donor/capability/Golden | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-078](https://uiverse.io/kennyotsu/giant-sloth-18) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.css) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Scheda donor/capability/Golden | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |
| [UIV-082](https://uiverse.io/kennyotsu/wise-rattlesnake-92) | CARD | Scheda donor/capability/Golden | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-093](https://uiverse.io/preet_7613/new-cougar-63) | CARD | Card progetto o capability | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-093_original.css) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-096](https://uiverse.io/solowzrd/wet-lionfish-63) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.css) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Scheda donor/capability/Golden | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**8 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-101](https://uiverse.io/Javierrocadev/chatty-ladybug-95) | FORM | Form gestione idea, capability o filtri dell'inventario | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.css) |
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Form gestione idea, capability o filtri dell'inventario | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-103](https://uiverse.io/SyedShahzaib7/brave-dog-61) | FORM | Form gestione idea, capability o filtri dell'inventario | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Form gestione idea, capability o filtri dell'inventario | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Form gestione idea, capability o filtri dell'inventario | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Verifica repository GitHub realmente avviata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Tooltip differenza Implemented/Verified e evidenze | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Form gestione idea, capability o filtri dell'inventario | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## Fonti esterne aggiunte — 20/11/2026 (15 URL, 14 servizi unici)

Intake visivo documentale: [audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice per app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro JSON](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Motion Sites** (`DESIGN-SITE-015`): Animated hero with reduced-motion fallback. **Stato: PROPOSED_ONLY**.
- **Motion Sites Studio** (`DESIGN-SITE-016`): AI-assisted website prototype comparison. **Stato: PROPOSED_ONLY**.
- **Land-book** (`DESIGN-SITE-017`): Pricing-page hierarchy with distinct comparison tiers. **Stato: PROPOSED_ONLY**.
- **Landdding** (`DESIGN-SITE-019`): Sector-specific landing layouts for SaaS, utility and food. **Stato: PROPOSED_ONLY**.
- **Fontshare** (`DESIGN-SITE-022`): Pair serif editorial headings with neutral readable UI fonts. **Stato: PROPOSED_ONLY**.
- **Lucide** (`DESIGN-SITE-025`): Consistent stroke and semantic icon naming. **Stato: PROPOSED_ONLY**.
- **SVGL** (`DESIGN-SITE-026`): Find official provider logos for legitimate integration badges. **Stato: PROPOSED_ONLY**.

I pattern richiedono decisione di prodotto, valutazione della licenza e QA sulla schermata target. Nessun componente, font, foto o logo di terzi e' stato copiato; nessuna funzione consumer risulta implementata da questo intake.
