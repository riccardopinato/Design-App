# Deskland Android — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/deskland-android.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/deskland-android.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Launcher Android interattivo con accenti desktop/spatial 3D; gesti e leggibilità prime, effetti visivi dopo stabilità.

**Categorie da studiare:** desktop · launcher · batteria/widget · meteo se reale.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. icone app nella home launcher.
2. drag/drop e selezione tile.
3. controlli player/effetti dove realmente presenti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-003 · battery-charging](https://gentleface.com/icons/battery-charging) | MEDIUM | widget stato batteria reale | VERIFIED_DETAIL |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | avvio animazione o elemento interattivo | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa effetti quando previsto | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | launcher home senza costi animazioni | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `home`, `play`, `battery-charging`.

## Animazioni e feedback proposti

- risposta drag a 60 fps e rilascio leggibile.
- transizione selezione/long-press sobria.

## Cosa evitare

- animazioni continue che rallentano il launcher.
- finti indicatori batteria o meteo.
- effetti sofisticati prima di eliminare i glitch.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | MEDIUM | launcher accessibility and touch-state review |
| DSK-004 — Emil Design Engineering | HIGH | long-press drag, icon motion and frame pacing |
| DSK-009 — UI UX Pro Max | HIGH | launcher spatial controls, only after functional stability |

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

- **Idea:** Overlay per futuro agente o note vocali solo se previsti.
- **Collocazione candidata:** Pannello vocale separato dal launcher.
- **Adattamento estetico:** effetto launcher leggero.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Launcher side panel after stabilization. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (MEDIUM):** Only with proven mouse/trackpad connected, avoid launcher CPU impact. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (HIGH):** Enter a launcher room/panel only after launcher stabilizes. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** First launcher data loading only, never on every home action. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-004 · App Icon Load (HIGH)** — Avvio launcher con inizializzazione effettiva. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/app-icon-load.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-009 · Terminal Loader (MEDIUM)** — Diagnostica developer opzionale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/terminal-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-012 · Grid Dots (MEDIUM)** — Preparazione pannello app. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/grid-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-017 · Concentric Ring (MEDIUM)** — Caricamento pannello widget. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-ring.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-020 · Concentric Squares (MEDIUM)** — Caricamento launcher con modalità risparmio movimento. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-squares.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-029 · Particle Shape Morph (MEDIUM)** — Effetto visivo accessorio dopo stabilità launcher. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-030 · Infinite Spiral (MEDIUM)** — Esperimento visuale dopo collaudo FPS. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 7 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `OPERATE+EXPERIENCE`, fit MEDIUM. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Launcher, scene e overlay.
- **Miglioramento proposto:** Conservare l'impatto immersivo senza perdere usabilità del launcher o performance Android; motion solo quando utile.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] FPS e rendering scenico misurati su device
  - [ ] Overlay e controlli accessibili, nessun bottone fuori schermo
  - [ ] Animazioni sospese in background/riduzione movimento
  - [ ] Home avviabile anche quando asset dinamici non caricano

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-004, DCL-008, DCL-012.
- **Schermate:** Home launcher e transizioni.
- **Vincolo:** Prima rendere launcher affidabile e fluido.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**24 preferiti proposti per deskland-android**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-013](https://uiverse.io/AqFox/young-dragon-29) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html) |
| [UIV-016](https://uiverse.io/Gidarx/clever-panther-6) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.css) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-019](https://uiverse.io/JkHuger/new-deer-97) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-026](https://uiverse.io/Nawsome/brave-turtle-26) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html) |
| [UIV-031](https://uiverse.io/Novaxlo/rotten-lionfish-4) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.css) |
| [UIV-032](https://uiverse.io/Praashoo7/lucky-hound-44) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html) |
| [UIV-036](https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html) |
| [UIV-041](https://uiverse.io/Shoh2008/ugly-elephant-80) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html) |
| [UIV-042](https://uiverse.io/Shoh2008/yellow-dolphin-16) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html) |
| [UIV-050](https://uiverse.io/andrew-manzyk/fast-vampirebat-53) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.css) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-063](https://uiverse.io/dexter-st/tough-falcon-78) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.css) |
| [UIV-068](https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.css) |
| [UIV-072](https://uiverse.io/gsperandio/shaggy-kangaroo-12) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-078](https://uiverse.io/kennyotsu/giant-sloth-18) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.css) |
| [UIV-082](https://uiverse.io/kennyotsu/wise-rattlesnake-92) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-096](https://uiverse.io/solowzrd/wet-lionfish-63) | PATTERN | Texture background con gate contrasto/FPS | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.css) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture background con gate contrasto/FPS | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**1 nuove associazioni** da originali HTML/CSS pubblici Uiverse, nessuna modifica runtime dell'app.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-108](https://uiverse.io/guilhermeyohan/friendly-walrus-55) | FORM | Form interattivo del launcher, originalità grafica vincolante | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.css) |

Stato: **PROPOSED_ONLY**; nessuna nuova funzione/login è autorizzata da questi suggerimenti.
**UIV-108**: solo ispirazione pixel-art generica. Non riusare personaggi, sprite, trade dress o marchi Nintendo senza licenza separata.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi dei nuovi 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## Fonti di design — 20/11/2026

[Audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press — **PROPOSED_ONLY**.

Nessun asset, font, logo o codice importato. Sono richiesti approvazione estetica, Product Bible, licenza e QA sulle schermate reali.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **React Bits** (`DESIGN-SITE-034`): Study light-motion effects as references only, not GPU-heavy permanent launcher background — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **Scroll Shaders** (`DESIGN-SITE-036`): Visual inspiration; no permanent GPU shader without device FPS/battery evidence — **PROPOSED_ONLY**.
- **AI Canvas** (`DESIGN-SITE-039`): Agent presence indicator derived from real status, not fake animation — **PROPOSED_ONLY**.
- **ReUI — Agent Ops Pro Blocks** (`DESIGN-SUBL-001`): Agent step trace and approval workflow as architecture reference only — **PROPOSED_ONLY**.
- **shadcn/ui — AI Elements** (`DESIGN-SUBL-002`): Agent status and confirmation UX references for native implementation — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Review 3D spatial scene and motion concepts as references only; maintain device performance gating. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.


## Motion UX, animazioni e video — lotto 18 fonti 20/11/2026

[Audit licenze e compatibilita'](../sources/MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](../sources/MOTION_VIDEO_18_PIPELINE_2026-11-20.md) · [Manifest SHA](../sources/MOTION_VIDEO_18_REGISTRY_2026-11-20.json).

- **motion-design-skill** (`MOTION-OSS-002`): Document consistent physics/interaction pacing with FPS and battery limits. **PROPOSED_ONLY**.
- **blender-skills** (`MOTION-OSS-009`): Prototype own low-poly 3D desk/world assets via desktop Blender, then optimize exports. **PROPOSED_ONLY**.
- **three.quarks** (`MOTION-OSS-010`): Evaluate Web particle prototype, only port after GPU and battery evaluation. **PROPOSED_ONLY**.
- **react-postprocessing** (`MOTION-OSS-011`): Reference bloom/depth effects without assuming WebGL-to-native interoperability. **PROPOSED_ONLY**.
- **tweakpane** (`MOTION-OSS-012`): Developer-only motion/scene parameter adjustment panel, excluded from release. **PROPOSED_ONLY**.

**Vincoli:** il media render resta separato dal runtime APK; Flutter/Compose devono usare il donor/framework nativo prima di TSX/JavaScript; licenza dell'asset e del runtime va verificata singolarmente. Nessuna modifica a Product Bible, UI, database, funzioni, codice, build o screenshot del consumer. Priorita' estetica agli asset e mock-up gia' scelti nel Design-App; a11y, reduced motion, FPS/batteria e privacy da validare in una eventuale implementazione.


## Motionary + 26 nuove fonti — 20/11/2026

[Audit e licenze](../sources/MOTIONARY_26_AUDIT_2026-11-20.md) · [Matrice 20 proposte / 10 app](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.md). Le fonti nuove non sostituiscono mock-up già approvati, Product Bible, Golden o design token proprietari.

- **STYLE26-01** (P1): Gesture spring/drag in home, solo se misurate su device — **PROPOSED_ONLY**.
- **STYLE26-24** (P2): Confronto token UI del pannello impostazioni; niente componenti React nel launcher — **PROPOSED_ONLY**.

**Confini:** 0 componenti SwiftUI/TSX importati nel consumer; per Flutter/Compose serve implementazione compatibile e collaudo. Le licenze dei siti e delle risorse premium/media restano distinte. Motionary MIT richiede notice; Rare UI vieta redistribuzione di un port/libreria di componenti e impone attribuzione in prodotto quando applicabile. Nessun codice, dato, permesso, APK, design scelto o runtime consumer è stato modificato.


## Design stack Florent — 5 link (20/11/2026)

[Audit licenze e fonti](../sources/FLORIENT_STACK_5_AUDIT_2026-11-20.md) · [Mappa per-app](../UI-UX/FLORIENT_STACK_5_APP_MAP_2026-11-20.md). Nessun cambiamento automatico dell'identità visiva approvata.

- **STACK5-05 · P2**: Video promozionale scene del launcher con riprese reali o ricostruzione dichiarata. **PROPOSED_ONLY**.

**Gate:** Shipframe screenshot autentici senza dati personali, Oversight solo reference o uso licenziato in progetto, Mobbin niente mirror di screenshot terzi, Fontshare licenza per famiglia; nessun file/asset copiato in questo lotto. Prima di applicare in app: Product Bible, codice consumer, test QA e approvazione.
