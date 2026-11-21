# Cooking Anime — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/cooking-anime.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/cooking-anime.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Identità image-first culinaria anime, con accenti kawaii controllati. Core UI leggibile, motivi illustrati per categorie e stati speciali. Distinguere coerentemente cucina giapponese, cinese e altri contesti senza stereotipi.

**Categorie da studiare:** kawaii-gattini · food-japan · food-china · anime-seasonal · ui-standard.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. Home con motivo brand (mascotte, ciotola o sakura).
2. Ricette con icona ricettario/bento e fotografia prioritaria.
3. Categorie con sushi, ramen, onigiri, dumpling o bao coerenti con ricetta.
4. Preferiti con cuore o stella leggibile.
5. Profilo con avatar gatto opzionale.
6. Sfide/collezioni/achievement soltanto se le funzioni esistono.
7. Empty state di ricerca o raccolta con gattino chef.
8. Loading con vapore della ciotola, solo durante vera attesa.
9. Salvataggio e ricetta completata con sparkle/check dopo conferma.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-009 · video](https://gentleface.com/icons/video) | MEDIUM | contenuti video dove disponibili | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | novità editoriali senza claim AI | VERIFIED_DETAIL |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | ricette favorite | VERIFIED_SITE |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | riproduzione video ricetta | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa tutorial | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `kawaii-cat-chef`, `sushi`, `ramen`, `onigiri`, `bento`, `chopsticks`, `sakura`.

## Catalogo tematico Cooking Anime (NON sorgenti verificate)

I seguenti 36 concetti provengono dalla richiesta dell'utente e dai suggerimenti in chat del 17/11/2026. Non sono presentati come icone disponibili in Gentleface né come asset già licenziati: lo stato è `DESIGN_IDEA`, provider `NOT_SELECTED`.

| Categoria | Concept | Destinazioni | Motion | Disponibilità |
|---|---|---|---|---|
| kawaii-gattini | Mascotte gattino con cappello da chef (`CAI-gattino-chef`) | home, empty-state, onboarding | STATIC_OR_BRIEF_ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Testolina di gattino (`CAI-testolina-gatto`) | profilo, stato-personalizzato | STATIC | da cercare/verificare |
| kawaii-gattini | Zampetta (`CAI-zampetta`) | badge, collezione, progresso | ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Faccina kawaii (`CAI-faccina-kawaii`) | feedback, empty-state | ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Avatar gattino (`CAI-gattino-avatar`) | profilo, personalizzazione | STATIC | da cercare/verificare |
| food-japan | Sushi (`CAI-sushi`) | categorie, suggerimenti | ON_SELECT | da cercare/verificare |
| food-japan | Ciotola di ramen con vapore (`CAI-ramen`) | categorie, loading | ONLY_LOADING_VISIBLE | da cercare/verificare |
| food-japan | Onigiri (`CAI-onigiri`) | categorie, tag | ON_SELECT | da cercare/verificare |
| food-japan | Bento box (`CAI-bento`) | ricette, categorie | STATIC | da cercare/verificare |
| food-japan | Bacchette (`CAI-bacchette`) | categoria, ricetta | STATIC | da cercare/verificare |
| food-japan | Teiera (`CAI-teiera`) | bevande, categorie | STATIC | da cercare/verificare |
| food-japan | Ciotola di riso (`CAI-riso`) | ingredienti, tag | STATIC | da cercare/verificare |
| food-japan | Pesce (`CAI-pesce`) | ingredienti, tag | STATIC | da cercare/verificare |
| food-japan | Dolcetto/mochi (`CAI-mochi-dessert`) | dessert, categorie | STATIC | da cercare/verificare |
| food-china | Ravioli cinesi jiaozi (`CAI-jiaozi-dumplings`) | categoria-cucina-cinese | STATIC | da cercare/verificare |
| food-china | Bao al vapore (`CAI-bao`) | categoria-cucina-cinese | STATIC | da cercare/verificare |
| food-china | Wok (`CAI-wok`) | preparazioni-cinesi | STATIC | da cercare/verificare |
| food-china | Cestello a vapore in bambù (`CAI-cestello-bambu`) | tecniche-cottura | STATIC | da cercare/verificare |
| food-china | Tazza da tè cinese (`CAI-te-cinese`) | bevande | STATIC | da cercare/verificare |
| anime-seasonal | Fiore di sakura (`CAI-sakura`) | sezioni, ricorrenze-stagionali | STATIC | da cercare/verificare |
| anime-seasonal | Torii (`CAI-torii`) | contenuti-situati-in-giappone | STATIC | da cercare/verificare |
| anime-seasonal | Lanterna (`CAI-lanterna`) | contenuti-culturali-coerenti | STATIC | da cercare/verificare |
| anime-seasonal | Ventaglio (`CAI-ventaglio`) | decorazione-contestuale | STATIC | da cercare/verificare |
| anime-seasonal | Nuvola stilizzata (`CAI-nuvola-stilizzata`) | header, empty-state | STATIC | da cercare/verificare |
| anime-seasonal | Stellina/sparkle (`CAI-sparkle`) | successo, badge, preferiti | ON_CONFIRMED_EVENT | da cercare/verificare |
| ui-standard | Casetta semplice (`CAI-home`) | navigazione-principale | STATIC | da cercare/verificare |
| ui-standard | Libro ricette (`CAI-ricettario`) | navigazione-ricette | STATIC | da cercare/verificare |
| ui-standard | Griglia categorie (`CAI-categorie`) | navigazione-categorie | STATIC | da cercare/verificare |
| ui-standard | Cuore preferito (`CAI-cuore`) | preferiti | ON_CONFIRMED_TOGGLE | da cercare/verificare |
| ui-standard | Lente ricerca (`CAI-search`) | ricerca | STATIC | da cercare/verificare |
| ui-standard | Ingranaggio impostazioni (`CAI-settings`) | impostazioni | STATIC | da cercare/verificare |
| ui-standard | Condividi (`CAI-share`) | condivisione | STATIC | da cercare/verificare |
| ui-standard | Modifica (`CAI-edit`) | editor-ricette-se-presente | STATIC | da cercare/verificare |
| ui-standard | Elimina (`CAI-delete`) | rimozione-con-conferma | STATIC | da cercare/verificare |
| ui-standard | Profilo (`CAI-profile`) | profilo | STATIC | da cercare/verificare |
| ui-standard | Conferma (`CAI-check`) | salvataggio, reazione | ON_CONFIRMED_EVENT | da cercare/verificare |

**Direzione consigliata**: un unico illustratore/pack vettoriale per icone kawaii, gastronomiche e decorative; non confondere giapponese/cinese. Per le azioni principali restano icone standard (lente, impostazioni, modifica, cestino, condividi) con priorità alla leggibilità. L'atmosfera anime non implica il riuso di marchi/personaggi protetti.

## Animazioni e feedback proposti

- cuore o stella con transizione discreta alla conferma preferito.
- vapore ramen o ciotola solo in caricamento visibile.
- gattino chef felice dopo completamento ricetta confermato.
- nessun loop perpetuo su listati ricette.

## Cosa evitare

- sostituire Cerca, Modifica, Elimina, Condividi o Impostazioni con simboli difficili da capire.
- mescolare emoji, outline, 3D, flat e pixel art senza un'unica grammatica.
- associare cibo cinese a simboli giapponesi o viceversa indiscriminatamente.
- usare bandiere o torii come sinonimo generico di 'Asia'.
- replicare personaggi o loghi anime protetti.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | MEDIUM | image-first editorial cards |
| DSK-003 — Taste Skill | HIGH | product/store marketing website |
| DSK-005 — Vercel Web Design Guidelines | MEDIUM | marketing and public site only |
| DSK-006 — Anthropic Frontend Design | HIGH | image-first culinary identity |
| DSK-007 — Hallmark | HIGH | public product marketing and themed campaign |
| DSK-009 — UI UX Pro Max | HIGH | image-first catalogue design |
| DSK-010 — Stageshow | HIGH | app store promotional cards |

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

- **Idea:** Appunti vocali personali durante una ricetta.
- **Collocazione candidata:** Dettaglio ricetta, non overlay costante.
- **Adattamento estetico:** anime/kawaii senza distrarre dalla ricetta.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (HIGH)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (HIGH)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (HIGH):** Reveal recipe collections or seasonal illustrated cover. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Recipe card front/back only for compact information. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Recipe collections and long article sections. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Enter themed category, not every navigation. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Recipe content retrieval only while active. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Ricette suggerite con foto. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (MEDIUM)** — Quantità porzioni/tempo cottura se configurabili. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (MEDIUM)** — Timer ricetta, con input numerico alternativo. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Account volontario solo se previsto dal prodotto. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (HIGH)** — Titolo identità ricette/kawaii se il branding lo consente. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (MEDIUM)** — Condivisione raccolte ricette se supportata. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (HIGH)** — Timer cottura ricetta solo con vera gestione background/avvisi. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-002 · Classic Spinner (MEDIUM)** — Caricamento ricette. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/classic-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-004 · App Icon Load (MEDIUM)** — Splash di brand durante dati iniziali. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/app-icon-load.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-008 · Fade Arc (HIGH)** — Apertura ricetta o media. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/fade-arc.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-011 · Morph Loader (HIGH)** — Caricamento ricetta brandizzato senza bloccare comandi. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/morph-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-013 · Clock Spinner (MEDIUM)** — Inizializzazione timer ricetta. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/clock-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-016 · Skeleton (HIGH)** — Card ricette con layout foto. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/skeleton.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-020 · Concentric Squares (MEDIUM)** — Brand loading opzionale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-squares.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-025 · Bouncing Lines (HIGH)** — Caricamento ricetta con movimento contenuto. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bouncing-lines.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-026 · Newtons Cradle (MEDIUM)** — Attesa durante elaborazione non critica. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/newtons-cradle.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-027 · Helix Spinner (MEDIUM)** — Variazione visuale di caricamento. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-029 · Particle Shape Morph (MEDIUM)** — Hero di sezione o transizione celebrativa non continua. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-030 · Infinite Spiral (MEDIUM)** — Galleria promozionale tematica. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 12 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Uiverse — proposte 18/11/2026

- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**28 preferiti proposti per cooking-anime**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-013](https://uiverse.io/AqFox/young-dragon-29) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-015](https://uiverse.io/FColombati/spotty-snake-82) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.css) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-026](https://uiverse.io/Nawsome/brave-turtle-26) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-031](https://uiverse.io/Novaxlo/rotten-lionfish-4) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.css) |
| [UIV-036](https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-038](https://uiverse.io/Priyanshu02020/popular-puma-87) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.css) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-041](https://uiverse.io/Shoh2008/ugly-elephant-80) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-072](https://uiverse.io/gsperandio/shaggy-kangaroo-12) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**6 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Input ricetta, ingredienti o titolo | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Input ricetta, ingredienti o titolo | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Input ricetta, ingredienti o titolo | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-107](https://uiverse.io/elijahgummer/new-fly-30) | LOADER | Caricamento ricetta o salvataggio realmente in corso | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.css) |
| [UIV-108](https://uiverse.io/guilhermeyohan/friendly-walrus-55) | FORM | Input ricetta, ingredienti o titolo | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.css) |
| [UIV-109](https://uiverse.io/mamyapro123/curvy-bear-51) | FORM | Input ricetta, ingredienti o titolo | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.
**UIV-108**: riferimento pixel art che menziona Mario. Non importare personaggi, sprite, identità o marchi Nintendo senza diritti specifici.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## DSK-011 — Unslop UI, audit sottrattivo (19/11/2026)

**PROPOSED_ONLY · fonte OSS MIT** [felipebasurto/unslop-ui @ cd891160453f26aaacc569bad96a8d10d595076d](https://github.com/felipebasurto/unslop-ui/tree/cd891160453f26aaacc569bad96a8d10d595076d). [Audit e limiti](../sources/UNSLOP_UI_AUDIT_2026-11-19.md) · [matrice di associazione](../UI-UX/UNSLOP_UI_APP_MAP_2026-11-19.json).

**Proposta:** Ricette e schede image-first: esaminare badge, aiutanti didascalici e gerarchia; mantenere ingredienti, allergeni e traduzioni corretti. Le U1–U20 sono controlli diagnostici e alias degli AT-01…AT-64, non un nuovo tema. Riutilizzo **ADAPT_NATIVE / SOURCE_REVIEW**; nessun automatismo rimuove elementi, nessun consumer certificato da questo dossier. Product Bible e reference preferite restano prioritarie. Stato visivo/fisico: **NOT_VERIFIED**.


## Fonti di design — 20/11/2026

[Audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Recent Design** (`DESIGN-SITE-018`): App icon and typography moodboards — **PROPOSED_ONLY**.
- **Landdding** (`DESIGN-SITE-019`): Sector-specific landing layouts for SaaS, utility and food — **PROPOSED_ONLY**.
- **Font in Logo** (`DESIGN-SITE-020`): Match editorial title typography to product tone — **PROPOSED_ONLY**.
- **Fontshare** (`DESIGN-SITE-022`): Pair serif editorial headings with neutral readable UI fonts — **PROPOSED_ONLY**.
- **Coolors** (`DESIGN-SITE-024`): Generate candidate 5-color palettes, then test in actual screen — **PROPOSED_ONLY**.
- **Shots** (`DESIGN-SITE-027`): Create marketing phone/device mockups from own QA screenshots — **PROPOSED_ONLY**.
- **Cosmos** (`DESIGN-SITE-028`): Moodboard collections and search by color/similarity — **PROPOSED_ONLY**.

Nessun asset, font, logo o codice importato. Sono richiesti approvazione estetica, Product Bible, licenza e QA sulle schermate reali.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Best Designs on X** (`DESIGN-SITE-029`): Collect food/illustration art-direction references with creator attribution. **PROPOSED_ONLY**.
- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study image-first recipe browsing and saved collections. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): Recipe discovery and favorites tiles with images and prep time. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **ThinkUI** (`DESIGN-SITE-032`): Compare saved recipes and ingredient-step reading flows using evidence, not cloned assets — **PROPOSED_ONLY**.
- **Mobbin** (`DESIGN-SITE-033`): Study discover-to-recipe-to-favorites interaction flows — **PROPOSED_ONLY**.
- **React Bits** (`DESIGN-SITE-034`): Consider restrained recipe-card entrances on Web, preserving content-first browsing — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **Scrolltide** (`DESIGN-SITE-035`): Editorial Web launch page visual inspiration — **PROPOSED_ONLY**.
- **Aceternity UI** (`DESIGN-SITE-040`): Editorial recipe tiles and light image transitions — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Collect food-inspired illustration composition and hero treatments for app promotion. **PROPOSED_ONLY**.
- **UIColours** (`DESIGN-SITE-043`): Test recipe category palette and card text contrast, without copying food-brand identities. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.


## Motion UX, animazioni e video — lotto 18 fonti 20/11/2026

[Audit licenze e compatibilita'](../sources/MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](../sources/MOTION_VIDEO_18_PIPELINE_2026-11-20.md) · [Manifest SHA](../sources/MOTION_VIDEO_18_REGISTRY_2026-11-20.json).

- **motion-design-skill** (`MOTION-OSS-002`): Animate recipe step feedback without disrupting legibility. **PROPOSED_ONLY**.
- **mg-styles-15** (`MOTION-OSS-003`): Use motion styles as references for original recipe launch videos. **PROPOSED_ONLY**.
- **huashu-art-motion** (`MOTION-OSS-004`): Illustrated cooking explainer idea with original non-copyrighted characters. **PROPOSED_ONLY**.
- **anidoodle** (`MOTION-OSS-005`): Create original recipe-process drawings for promotional content. **PROPOSED_ONLY**.
- **cinetic** (`MOTION-OSS-006`): Promo recipes and features; no Remotion engine shipped with Flutter. **PROPOSED_ONLY**.
- **motionmaxxing** (`MOTION-OSS-007`): Polish cinematic recipe teaser composition with GSAP license checked. **PROPOSED_ONLY**.
- **effectcraft** (`MOTION-OSS-013`): Compose licensed recipe launch clips with original art. **PROPOSED_ONLY**.
- **openverse** (`MOTION-OSS-014`): Discover permitted background music, not assume free commercial rights. **PROPOSED_ONLY**.
- **librosa** (`MOTION-OSS-015`): Align recipe teaser cuts to original or cleared music beats offline. **PROPOSED_ONLY**.
- **whisperX** (`MOTION-OSS-016`): Draft multilingual recipe teaser captions with transcript review. **PROPOSED_ONLY**.
- **skills** (`MOTION-OSS-017`): External build workflow for approved recipe tutorial teaser videos. **PROPOSED_ONLY**.
- **FFmpeg** (`MOTION-OSS-018`): Social video export with 16:9 and 9:16 compositions and subtitle tracks. **PROPOSED_ONLY**.

**Vincoli:** il media render resta separato dal runtime APK; Flutter/Compose devono usare il donor/framework nativo prima di TSX/JavaScript; licenza dell'asset e del runtime va verificata singolarmente. Nessuna modifica a Product Bible, UI, database, funzioni, codice, build o screenshot del consumer. Priorita' estetica agli asset e mock-up gia' scelti nel Design-App; a11y, reduced motion, FPS/batteria e privacy da validare in una eventuale implementazione.


## Jiro Build e Builder — fonti Web per marketing (20/11/2026)

[Audit, deduplica e licenze](../sources/JIRO_AND_15_DESIGN_LINKS_DEDUP_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.md) · [Mappa JSON](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.json).

- **Jiro Prompt Library** (`DESIGN-SITE-044`): Prepare landing page layout ideas for recipe search, localized value proposition and app store entry points. **PROPOSED_ONLY**.
- **Jiro Builder** (`DESIGN-SUBL-003`): Test a separate marketing microsite only; do not import Jiro output as mobile recipe code. **PROPOSED_ONLY**.

**Gate:** Jiro e' una libreria proprietaria di design Web/React e un servizio esterno di hosting; nessun widget Flutter/Compose importato e nessun piano acquistato. I Termini consentono i progetti propri/clienti ma vietano ricollezionare o rivendere componenti/template standalone, il che preclude il copy del catalogo nella nostra libreria. Il Builder Free prevede limiti crediti e inattivita' e l'esportazione ZIP richiede un piano. Gli asset e mock-up preferiti gia' approvati in Design-App prevalgono; nessun codice consumer, server, auth, dati, palette, release o design deciso è stato modificato.


## Motionary + 26 nuove fonti — 20/11/2026

[Audit e licenze](../sources/MOTIONARY_26_AUDIT_2026-11-20.md) · [Matrice 20 proposte / 10 app](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.md). Le fonti nuove non sostituiscono mock-up già approvati, Product Bible, Golden o design token proprietari.

- **STYLE26-01** (P1): Step ricetta: avanzamento reale e transizioni tra passaggi — **PROPOSED_ONLY**.
- **STYLE26-11** (P2): Video promo ricette prodotti offline; engine web separato dall'APK e verifica licenza — **PROPOSED_ONLY**.

**Confini:** 0 componenti SwiftUI/TSX importati nel consumer; per Flutter/Compose serve implementazione compatibile e collaudo. Le licenze dei siti e delle risorse premium/media restano distinte. Motionary MIT richiede notice; Rare UI vieta redistribuzione di un port/libreria di componenti e impone attribuzione in prodotto quando applicabile. Nessun codice, dato, permesso, APK, design scelto o runtime consumer è stato modificato.


## Design stack Florent — 5 link (20/11/2026)

[Audit licenze e fonti](../sources/FLORIENT_STACK_5_AUDIT_2026-11-20.md) · [Mappa per-app](../UI-UX/FLORIENT_STACK_5_APP_MAP_2026-11-20.md). Nessun cambiamento automatico dell'identità visiva approvata.

- **STACK5-01 · P1**: Screenshot Google Play verticali con immagini genuine delle ricette e didascalie multilingua. **PROPOSED_ONLY**.
- **STACK5-05 · P2**: Video esplicativo breve sul percorso ricetta, ingredienti e passaggi; stile coerente, risorse originali. **PROPOSED_ONLY**.
- **STACK5-04 · P2**: Valutare font editoriali leggibili per schede promozionali, senza cambiare la UI approvata. **PROPOSED_ONLY**.

**Gate:** Shipframe screenshot autentici senza dati personali, Oversight solo reference o uso licenziato in progetto, Mobbin niente mirror di screenshot terzi, Fontshare licenza per famiglia; nessun file/asset copiato in questo lotto. Prima di applicare in app: Product Bible, codice consumer, test QA e approvazione.


## Appllama · Dissolve · Libraries.dev — 21/11/2026

[Audit di fonti e licenze](../sources/APPLLAMA_MOTION_ART_STACK_AUDIT_2026-11-21.md) · [Mappa per app](../UI-UX/APPLLAMA_MOTION_ART_APP_MAP_2026-11-21.md).

- **DESIGN-SITE-049 — P2:** Flow recipe discovery, pagine dettagli e paywall comparati, contenuti originali. `PROPOSED_ONLY`.
- **DESIGN-SITE-059 — P2:** Tessere video/card Web per landing di presentazione e marketing. `PROPOSED_ONLY`.

Nessun video/file terzo inserito nel repo; i materiali ricevuti sono descritti con SHA256 e non sono sorgente COPY_READY. Prima del riuso: Product Bible, licenza, compatibilità Flutter/Compose/Web, accessibilità/motion reduced e QA.
