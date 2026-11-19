# Battery Guard — Dossier Design-App

**Registro permanente:** `PER_APP/battery-guard.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility verde e pulita; l'informazione sulla batteria deve rimanere prioritaria rispetto all'estetica.

**Categorie da studiare:** batteria · ricarica · risparmio energetico · allerta.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. stato batteria reale e gauge.
2. indicatore di carica.
3. avvisi soglia batteria.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | avviso batteria non critico | VERIFIED_SITE |
| [ICO-003 · battery-charging](https://gentleface.com/icons/battery-charging) | HIGH | stato carica reale | VERIFIED_DETAIL |
| [ICO-004 · battery-low](https://gentleface.com/icons/battery-low) | HIGH | soglia batteria realmente rilevata | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | MEDIUM | analisi dati in corso | VERIFIED_DETAIL |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | HIGH | stato batteria | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `battery-charging`, `battery-low`, `gauge`.

## Animazioni e feedback proposti

- carica pulsante solo mentre la ricarica è effettiva e schermata visibile.
- successo cambio impostazione dopo conferma.

## Cosa evitare

- fake animation che implica protezione attiva.
- consumo energetico dell'animazione superiore al suo valore.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | HIGH | readable metrics and actionable status |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | information clarity and warning states |
| DSK-009 — UI UX Pro Max | HIGH | clean battery analytics theme |
| DSK-010 — Stageshow | MEDIUM | clean metrics app-store screenshots |

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
- **DSP-003 · Accordion Blind Pull (MEDIUM)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Long battery diagnostics explanations. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Diagnostics computation if measured. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Questa sezione contiene **proposte**; nessuna libreria installata, nessuna feature consumer confermata dal solo catalogo.

- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (MEDIUM)** — Regola soglie con limiti reali. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (MEDIUM)** — Soglia batteria solo con modalità intervallo reale. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.


**Gate comune:** rispettare Product Bible, accessibilità, controlli di input alternativi, riduzione movimento, performance, colore e lingua; Flutter/Compose richiedono adattamento nativo dei componenti React. I riferimenti `Text Gradient`, `Notification List` e `Flip Clock` non hanno un file componente esatto verificato alla baseline e restano `REFERENCE`.

**Storico 17/11/2026:** proposte inserite in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, con provenienza e stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-006 · Stacked Bar Pulse (MEDIUM)** — Raccolta diagnostica reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/stacked-bar-pulse.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-008 · Fade Arc (MEDIUM)** — Aggiornamento misure. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/fade-arc.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-014 · Circular Bars (HIGH)** — Analisi batteria con campionamento attivo. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/circular-bars.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-017 · Concentric Ring (MEDIUM)** — Attesa elaborazione diagnostica. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-ring.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-022 · Bar Sweep (MEDIUM)** — Diagnostica in corso. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bar-sweep.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 5 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `OPERATE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Dashboard batteria e diagnostica.
- **Miglioramento proposto:** Portare percentuale, stato, limite e prossima azione in evidenza, evitando metriche decorative e gerarchia piatta.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Numeri con unità e segnalazione di dato non disponibile
  - [ ] Contrasto light/dark con font grande
  - [ ] Nessuna pseudo-misura di precisione o azione inesistente
  - [ ] Layout safe-area e badge AdMob non invasivi

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-003, DCL-005, DCL-008, DCL-011.
- **Schermate:** Stato batteria, sessioni e grafici.
- **Vincolo:** Grafici reali; overhead GPU e consumo prossimi a zero.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-001 — [alexruix/tame-fly-42](https://uiverse.io/alexruix/tame-fly-42)**: Caricamento effettivo durante elaborazione (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.
- **UIV-006 — [JustCode14/red-dingo-61](https://uiverse.io/JustCode14/red-dingo-61)**: Toggle semantico legato a impostazione reale (MEDIUM). Originale da estrarre.
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**37 preferiti proposti per battery-guard**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-001](https://uiverse.io/alexruix/tame-fly-42) | LOADER | Caricamento effettivo durante elaborazione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html) |
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-006](https://uiverse.io/JustCode14/red-dingo-61) | SWITCH | Toggle semantico legato a impostazione reale | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-012](https://uiverse.io/Admin12121/massive-dodo-67) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-012_original.html) |
| [UIV-018](https://uiverse.io/JaydipPrajapati1910/average-shrimp-57) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-018_original.html) |
| [UIV-020](https://uiverse.io/JkHuger/selfish-bulldog-36) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-027](https://uiverse.io/Nawsome/empty-snail-69) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-027_original.html) |
| [UIV-028](https://uiverse.io/Nawsome/kind-mole-87) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-049](https://uiverse.io/andrew-demchenk0/honest-stingray-90) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-049_original.html) |
| [UIV-051](https://uiverse.io/andrew-manzyk/young-walrus-64) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-051_original.css) |
| [UIV-053](https://uiverse.io/barisdogansutcu/plastic-dolphin-67) | TOOLTIP | Aiuto contestuale non solo hover | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html) |
| [UIV-055](https://uiverse.io/chase2k25/modern-stingray-54) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-055_original.css) |
| [UIV-058](https://uiverse.io/cssbuttons-io/mean-dolphin-24) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-058_original.html) |
| [UIV-059](https://uiverse.io/cuzpq/gentle-goat-72) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-059_original.html) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-065](https://uiverse.io/dovatgabriel/massive-vampirebat-17) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-065_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-071](https://uiverse.io/gharsh11032000/sour-vampirebat-66) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-071_original.html) |
| [UIV-074](https://uiverse.io/jeremy_4982/massive-falcon-52) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-074_original.css) |
| [UIV-084](https://uiverse.io/lukepadiachy/funny-moose-89) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html) |
| [UIV-085](https://uiverse.io/m1her/odd-fireant-56) | SWITCH | Stato avviso realmente attivo | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.css) |
| [UIV-086](https://uiverse.io/mamyapro123/cuddly-warthog-66) | SWITCH | Stato avviso realmente attivo | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.css) |
| [UIV-088](https://uiverse.io/mobinkakei/great-skunk-8) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-088_original.html) |
| [UIV-089](https://uiverse.io/mobinkakei/grumpy-turtle-41) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html) |
| [UIV-090](https://uiverse.io/mobinkakei/strong-lizard-79) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-090_original.html) |
| [UIV-094](https://uiverse.io/satyamchaudharydev/splendid-husky-54) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html) |
| [UIV-096](https://uiverse.io/solowzrd/wet-lionfish-63) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-096_original.css) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |
| [UIV-099](https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75) | LOADER | Aggiornamento statistiche batteria | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html) |
| [UIV-100](https://uiverse.io/zanina-yassine/afraid-eel-50) | SWITCH | Stato avviso realmente attivo | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-100_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**2 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-106](https://uiverse.io/doniaskima/cowardly-frog-28) | LOADER | Aggiornamento telemetria batteria realmente in corso | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-106_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Spiegazione dello stato della carica | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).

## Flutter Gems / Forui / F22 — librerie UI native (18/11/2026)

Fonti: [Flutter Gems](https://fluttergems.dev/), [Forui Button](https://forui.dev/docs/widgets/form/button) e [F22 Labs 2026](https://www.f22labs.com/blogs/top-8-flutter-ui-libraries-for-2025-you-must-explore/). [Matrice bidirezionale](../UI-UX/FLUTTER_UI_LIBRARIES_APP_MAP_2026-11-18.json). **PROPOSED_ONLY, NOT_VERIFIED**: prima rispettare le reference utente in Design-App e Product Bible, poi verificare il package originale e il codice consumer.

| Libreria | Fit | Uso ipotizzato |
| --- | --- | --- |
| FL Chart | HIGH | actual charging/history charts |

Nessun package installato, nessuna modifica dati/architettura o Golden promosso; verifica Flutter SDK, dipendenze, APK size, accessibilità e performance necessaria prima dell'adozione.

## Material 3 — opzione selettiva, non obbligo (19/11/2026)

Fonte: [Material Design 3](https://m3.material.io/) · [studio e confini](../sources/MATERIAL3_OPTIONAL_REFERENCE_2026-11-19.md) · [matrice per app](../UI-UX/MATERIAL3_OPTIONAL_APP_MAP_2026-11-19.json).

Fit ipotizzato: **MEDIUM**. Possibile ambito: battery diagnostics/settings and compact summary widgets; avoid stock dashboard look.

**PROPOSED_ONLY / NOT_VERIFIED.** M3 non e' obbligatorio e non e' vietato; prima considerare Product Bible e stili Design-App curati dall'utente. Verificare se il consumer e' Flutter o Kotlin/Compose e se usa gia' M3. Nessuna installazione o modifica automatica, nessuna certificazione estetica senza prove su schermata reale.
