# World Days — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Giornate del mondo: schede editoriali colorate, densità informativa elevata e palette esistente da mantenere.

**Temi candidati:** calendario; ricorrenza; storia; preferiti; offline.

## Superfici e placement proposti

1. scheda giornata e informazioni varie.
2. salvataggio preferiti.
3. navigazione calendario e download contenuti.
4. sezioni storiche multilingue.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | avviso contenuto disponibile | VERIFIED_SITE |
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | HIGH | navigazione giorni | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | contenuti offline | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | MEDIUM | condivisione/export soltanto se implementato | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | HIGH | salva ricorrenze | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca giornate | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | download e caricamento reale | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | download verificato | VERIFIED_SITE |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | MEDIUM | localizzazione evento solo se presente | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | download contenuti reale | VERIFIED_SITE |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | giornate preferite | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | MEDIUM | collezioni archiviate se supportate | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | home delle ricorrenze | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** calendar, bookmark, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- bookmark breve dopo salvataggio reale.
- download solo durante trasferimento.
- microtransizione giorno senza variare i colori.

## Cosa evitare

- spostare informazioni in icone senza testo.
- cambiare la palette che l'utente ha già approvato.
- celebrare un contenuto ancora non certificato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | daily content cards and empty-state polish |
| DSK-002 — Impeccable | HIGH | content density, long-copy and reader flow |
| DSK-003 — Taste Skill | MEDIUM | content discovery pages where web-native |
| DSK-004 — Emil Design Engineering | MEDIUM | subtle content-card transitions |
| DSK-005 — Vercel Web Design Guidelines | HIGH | content-heavy web views and navigation |
| DSK-006 — Anthropic Frontend Design | HIGH | recognizable day-story cards |
| DSK-007 — Hallmark | MEDIUM | public promotional pages |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | long story and multilingual layouts |
| DSK-009 — UI UX Pro Max | HIGH | information-card design and locale-aware typography |
| DSK-010 — Stageshow | HIGH | new rich-story feature preview |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Voice Orb — proposta futura (MEDIUM)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Memo personali su una ricorrenza solo se la funzione verrà prevista.
- **Collocazione candidata:** Spazio note utente separato dal contenuto editoriale.
- **Adattamento estetico:** palette attuale invariata.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (MEDIUM)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Optional cover of a story, never gating text. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Historical fact card front/back, keep full text accessible. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Long editorial history and day cards without hiding accessibility text. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Special day detail entrance only if subtle. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Content download or parsing while active. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Esplora giornate in evidenza senza perdere ricerca. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (MEDIUM)** — Selezione giorno opzionale con supporto date reali. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (MEDIUM)** — Filtra ricorrenze per intervallo del calendario. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Account volontario, non bloccare lettura del catalogo. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Accento su heading senza cambiare colori approvati. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Una ricorrenza del giorno nel riepilogo, non cancellare contenuti editoriali. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Conto alla rovescia fino alla prossima giornata selezionata. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-001 · Accordion Loader (HIGH)** — Caricamento contenuto attivo. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/accordion-loader.tsx); già censito: `AMX-006`. Stato: `PROPOSED_ONLY`.
- **DBM-002 · Classic Spinner (HIGH)** — Caricamento dettagli giornata. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/classic-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-003 · Pulsating Dots (MEDIUM)** — Consultazione dettagli. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/pulsating-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-004 · App Icon Load (MEDIUM)** — Prima lettura database offline. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/app-icon-load.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-008 · Fade Arc (MEDIUM)** — Caricamento storia. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/fade-arc.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-010 · Apple Pulse Dots (MEDIUM)** — Recupero scheda offline. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-pulse-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-015 · Intersecting Rings (MEDIUM)** — Sync contenuti scaricabili. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/intersecting-rings.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-016 · Skeleton (HIGH)** — Schede ricorrenze in attesa dati. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/skeleton.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-021 · Notification List (MEDIUM)** — Ricorrenze del giorno. Evidenza: `EXACT_SOURCE_NOT_LOCATED`; sorgente esatto da identificare; già censito: `WML-008`. Stato: `PROPOSED_ONLY`.
- **DBM-022 · Bar Sweep (MEDIUM)** — Caricamento catalogo. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bar-sweep.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-024 · View On Map (MEDIUM)** — Luogo evento soltanto se dato disponibile. Evidenza: `SOURCE_FILE_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/view-on-map/base.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-025 · Bouncing Lines (MEDIUM)** — Caricamento storia. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bouncing-lines.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 12 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P1**, modalità `READ+OPERATE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Elenco ricorrenze, dettaglio storia, ricerca.
- **Miglioramento proposto:** Gerarchia editoriale che renda leggibili periodi, anno di introduzione, storia e informazioni varie senza introdurre più card annidate.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Storie lunghe e sei lingue senza troncare contenuti importanti
  - [ ] Fonte e anno ignoto non mascherati da fatti certi
  - [ ] Stati offline/errore leggibili, non spinner infinito
  - [ ] Palette esistente conservata e tipografia uniforme

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-001, DCL-003, DCL-007, DCL-011.
- **Schermate:** Schede giornata e scoperta.
- **Vincolo:** Preservare colori già approvati, storia e fonti sopra il puro decorativo.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-001 — [alexruix/tame-fly-42](https://uiverse.io/alexruix/tame-fly-42)**: Caricamento effettivo durante elaborazione (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html).
- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**52 preferiti proposti per world-days**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-001](https://uiverse.io/alexruix/tame-fly-42) | LOADER | Caricamento effettivo durante elaborazione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html) |
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-019](https://uiverse.io/JkHuger/new-deer-97) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca o inserimento con label | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-032](https://uiverse.io/Praashoo7/lucky-hound-44) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-038](https://uiverse.io/Priyanshu02020/popular-puma-87) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.css) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-042](https://uiverse.io/Shoh2008/yellow-dolphin-16) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html) |
| [UIV-043](https://uiverse.io/Stavros2410/wet-duck-69) | UNKNOWN | Solo idea da classificare visivamente | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-043_original.css) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-050](https://uiverse.io/andrew-manzyk/fast-vampirebat-53) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.css) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-052](https://uiverse.io/ashif_6672/rare-bat-68) | UNKNOWN | Solo idea da classificare visivamente | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-052_original.css) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-064](https://uiverse.io/dopekid_9309/tiny-dog-80) | UNKNOWN | Solo idea da classificare visivamente | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-064_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-068](https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Caricamento delle storie locali | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-079](https://uiverse.io/kennyotsu/selfish-bear-69) | UNKNOWN | Solo idea da classificare visivamente | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-079_original.css) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Giornata e approfondimento storico | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-083](https://uiverse.io/kennyotsu/wonderful-firefox-31) | UNKNOWN | Solo idea da classificare visivamente | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-083_original.css) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Giornata e approfondimento storico | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Caricamento delle storie locali | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.
