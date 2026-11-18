# FrameLab — Dossier Design-App

**Registro permanente:** `PER_APP/framelab.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Editor fotografico premium editoriale: visuali originali grandi, gesti precisi, icone essenziali.

**Categorie da studiare:** fotografia · editing · export · media.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. barra strumenti editing.
2. galleria e anteprime.
3. salvataggio/export reale.
4. supporti media.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-006 · export](https://gentleface.com/icons/export) | HIGH | export media | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | HIGH | raccolta fotografie | VERIFIED_DETAIL |
| [ICO-009 · video](https://gentleface.com/icons/video) | MEDIUM | selezione e anteprima video | VERIFIED_DETAIL |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | anteprima multimediale | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa anteprima | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `images`, `export`, `video`.

## Animazioni e feedback proposti

- toggle strumento con stato evidente.
- micro-feedback export dopo completamento reale.

## Cosa evitare

- icone decorative sul contenuto fotografico.
- animazioni pesanti durante gesture di editing.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | photo and visual hierarchy |
| DSK-002 — Impeccable | HIGH | premium photo-editor controls |
| DSK-003 — Taste Skill | MEDIUM | editorial product landing |
| DSK-004 — Emil Design Engineering | HIGH | photo controls and gesture responsiveness |
| DSK-006 — Anthropic Frontend Design | HIGH | photographic editorial premium direction |
| DSK-007 — Hallmark | HIGH | editorial product showcase |
| DSK-009 — UI UX Pro Max | HIGH | photo UI token and contrast reference |
| DSK-010 — Stageshow | HIGH | visual editor demonstrations |

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

- **Idea:** Annotazione vocale di un progetto media se prevista.
- **Collocazione candidata:** Pannello note del progetto.
- **Adattamento estetico:** non sovrapporre alla foto.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (HIGH)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Marketing/gallery showcase only. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (MEDIUM):** Desktop editor hover mode only, not photo retouch controls. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Photo gallery non-editing view. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Open media album showcase, not destructive dialogs. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Export initialization only if determinate progress unavailable. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (HIGH)** — Selezione album/gallery in preview, no image crop. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (HIGH)** — Scrubbing foto/video/parametri con valori reali. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (HIGH)** — Regola parametri con bound reali se doppia soglia prevista. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Landing grafica, non etichette strumenti. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-011 · Morph Loader (HIGH)** — Anteprima media in elaborazione. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/morph-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-027 · Helix Spinner (MEDIUM)** — Anteprima render in corso. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-029 · Particle Shape Morph (MEDIUM)** — Presentazione media, non sopra editor. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-030 · Infinite Spiral (MEDIUM)** — Presentazione media a spirale se coerente con editor. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 4 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `OPERATE+EXPERIENCE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Editor media, galleria, pannelli di controllo.
- **Miglioramento proposto:** Rendere il contenuto foto centrale, strumenti secondari sobri e controlli riutilizzabili senza alterare il materiale originale.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Controlli e immagini non sovrapposti sui piccoli schermi
  - [ ] Colori/superfici dell'editor coerenti in light/dark
  - [ ] Modalità panoramica senza perdita funzionale
  - [ ] Operazioni export con feedback reale, progressi e ripristino

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-001, DCL-006, DCL-010, DCL-012.
- **Schermate:** Portfolio, foto, palette.
- **Vincolo:** Foto contenuto primario; controlli cromatici precisi.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-001 — [alexruix/tame-fly-42](https://uiverse.io/alexruix/tame-fly-42)**: Caricamento effettivo durante elaborazione (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**34 preferiti proposti per framelab**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-001](https://uiverse.io/alexruix/tame-fly-42) | LOADER | Caricamento effettivo durante elaborazione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html) |
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-015](https://uiverse.io/FColombati/spotty-snake-82) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.css) |
| [UIV-019](https://uiverse.io/JkHuger/new-deer-97) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-032](https://uiverse.io/Praashoo7/lucky-hound-44) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-038](https://uiverse.io/Priyanshu02020/popular-puma-87) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.css) |
| [UIV-042](https://uiverse.io/Shoh2008/yellow-dolphin-16) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-050](https://uiverse.io/andrew-manzyk/fast-vampirebat-53) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-050_original.css) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-068](https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-068_original.css) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Elaborazione foto/video effettiva | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**4 nuove associazioni** da originali HTML/CSS pubblici Uiverse, nessuna modifica runtime dell'app.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Form nome progetto e metadata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Rendering o esportazione media effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |
| [UIV-107](https://uiverse.io/elijahgummer/new-fly-30) | LOADER | Rendering o esportazione media effettiva | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.css) |
| [UIV-108](https://uiverse.io/guilhermeyohan/friendly-walrus-55) | FORM | Form nome progetto e metadata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-108_original.css) |

Stato: **PROPOSED_ONLY**; nessuna nuova funzione/login è autorizzata da questi suggerimenti.
**UIV-108**: solo ispirazione pixel-art generica. Non riusare personaggi, sprite, trade dress o marchi Nintendo senza licenza separata.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi dei nuovi 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).

## Flutter Gems / Forui / F22 — librerie UI native (18/11/2026)

Fonti: [Flutter Gems](https://fluttergems.dev/), [Forui Button](https://forui.dev/docs/widgets/form/button) e [F22 Labs 2026](https://www.f22labs.com/blogs/top-8-flutter-ui-libraries-for-2025-you-must-explore/). [Matrice bidirezionale](../UI-UX/FLUTTER_UI_LIBRARIES_APP_MAP_2026-11-18.json). **PROPOSED_ONLY, NOT_VERIFIED**: prima rispettare le reference utente in Design-App e Product Bible, poi verificare il package originale e il codice consumer.

| Libreria | Fit | Uso ipotizzato |
| --- | --- | --- |
| Mix | HIGH | palette/editor visual tokens |
| Forui | MEDIUM | pickers/settings |

Nessun package installato, nessuna modifica dati/architettura o Golden promosso; verifica Flutter SDK, dipendenze, APK size, accessibilità e performance necessaria prima dell'adozione.
