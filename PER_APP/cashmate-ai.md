# CashMate AI — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/cashmate-ai.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/cashmate-ai.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Blocchi finanziari verde/nero, gerarchia monetaria rigorosa; icone discrete, contrasto e semantica prioritarie.

**Categorie da studiare:** portafoglio · spese e incassi · grafici · sicurezza.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. dashboard saldi.
2. categorie transazione.
3. grafici trend.
4. backup soltanto se realmente disponibile.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | backup o cloud solo se implementato | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | MEDIUM | indicatori finanziari | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `gauge`, `check`, `lock`.

## Animazioni e feedback proposti

- feedback transazione salvata realmente.
- grafici stabili senza movimento che cambia lettura dei dati.

## Cosa evitare

- icone decorative accanto a ogni importo.
- usare colore solo per significato positivo/negativo.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | MEDIUM | financial data visual hierarchy |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | money formatting, disclosure and graphs |
| DSK-009 — UI UX Pro Max | HIGH | semantic finance palettes |

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
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Financial report sections, never animate values misleadingly. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Questa sezione contiene **proposte**; nessuna libreria installata, nessuna feature consumer confermata dal solo catalogo.

- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (HIGH)** — Filtri somme e periodi spese. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (HIGH)** — Registrazione/login dove backend supportato. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (MEDIUM)** — Flusso onboarding importazione controllato, non accesso condiviso implicito. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Scadenze spese solo se dati registrati realmente. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.


**Gate comune:** rispettare Product Bible, accessibilità, controlli di input alternativi, riduzione movimento, performance, colore e lingua; Flutter/Compose richiedono adattamento nativo dei componenti React. I riferimenti `Text Gradient`, `Notification List` e `Flip Clock` non hanno un file componente esatto verificato alla baseline e restano `REFERENCE`.

**Storico 17/11/2026:** proposte inserite in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, con provenienza e stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-018 · Range Selection Slider (HIGH)** — Range importo e periodo. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/range-selection-slider/base.tsx); già censito: `WML-004`. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 1 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `OPERATE`, fit MEDIUM. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Transazioni, grafici, filtri e budget.
- **Miglioramento proposto:** Dati economici e movimenti confrontabili, meno elementi decorativi, feedback esplicito di salvataggio/import.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Valori monetari precisi e unità non ambigue
  - [ ] Contrasto leggibile per stato negativo/positivo, anche senza colori
  - [ ] Filtri/intervalli con range valido
  - [ ] Error/empty/retry e login opzionale chiari

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-002, DCL-003, DCL-005, DCL-007.
- **Schermate:** Saldo, spese, budget, dettagli.
- **Vincolo:** Privacy, accuratezza valori, niente false metriche.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (MEDIUM). Originale da estrarre.
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**35 preferiti proposti per cashmate-ai**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-016](https://uiverse.io/Gidarx/clever-panther-6) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.css) |
| [UIV-018](https://uiverse.io/JaydipPrajapati1910/average-shrimp-57) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-018_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca o inserimento con label | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-059](https://uiverse.io/cuzpq/gentle-goat-72) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-059_original.html) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-063](https://uiverse.io/dexter-st/tough-falcon-78) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-067](https://uiverse.io/elijahgummer/young-horse-7) | RADIO | Scelta esclusiva accessibile | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-078](https://uiverse.io/kennyotsu/giant-sloth-18) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.css) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |
| [UIV-082](https://uiverse.io/kennyotsu/wise-rattlesnake-92) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html) |
| [UIV-086](https://uiverse.io/mamyapro123/cuddly-warthog-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.css) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |
| [UIV-100](https://uiverse.io/zanina-yassine/afraid-eel-50) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-100_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**6 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-101](https://uiverse.io/Javierrocadev/chatty-ladybug-95) | FORM | Accesso Google opzionale o modifica profilo, senza nuovo provider | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.css) |
| [UIV-103](https://uiverse.io/SyedShahzaib7/brave-dog-61) | FORM | Accesso Google opzionale o modifica profilo, senza nuovo provider | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-103_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Accesso Google opzionale o modifica profilo, senza nuovo provider | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Accesso Google opzionale o modifica profilo, senza nuovo provider | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Legenda dei termini o indicatori finanziari | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Accesso Google opzionale o modifica profilo, senza nuovo provider | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## Fonti esterne aggiunte — 20/11/2026 (15 URL, 14 servizi unici)

Intake visivo documentale: [audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice per app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro JSON](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Land-book** (`DESIGN-SITE-017`): Pricing-page hierarchy with distinct comparison tiers. **Stato: PROPOSED_ONLY**.
- **Realtime Colors** (`DESIGN-SITE-023`): Preview text/background/primary/secondary/accent combinations on real UI. **Stato: PROPOSED_ONLY**.
- **Lucide** (`DESIGN-SITE-025`): Consistent stroke and semantic icon naming. **Stato: PROPOSED_ONLY**.

I pattern richiedono decisione di prodotto, valutazione della licenza e QA sulla schermata target. Nessun componente, font, foto o logo di terzi e' stato copiato; nessuna funzione consumer risulta implementata da questo intake.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study legible finance dashboard mobile design systems. **PROPOSED_ONLY**.
- **ReUI** (`DESIGN-SITE-031`): Study dense analytics tables, chart and filters with semantic states. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): At-a-glance spend/budget/category stats with accessible semantic colors. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **ThinkUI** (`DESIGN-SITE-032`): Study real finance overview, add-expense and paywall flows as research-only — **PROPOSED_ONLY**.
- **Mobbin** (`DESIGN-SITE-033`): Analyze real transaction entry, insight and subscription screens for sequencing — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Fonti AI agent/Web/motion — 20/11/2026 (7 nuove, 2 approfondimenti)

[Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md) · [Matrice per-app](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Deep link ReUI/shadcn](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

- **Chakra UI** (`DESIGN-SITE-041`): Financial form/validation semantics, not Flutter copy-paste — **PROPOSED_ONLY**.

**Gate:** premium/proprietary/non-verified sources not imported, React/JS is not Dart, animations must respect reduced-motion and measurable state, GPU/performance/battery gates for shaders; per-app Product Bible and visual decisions before consumer implementation. The t.co short URL is unresolved. No code/tests of this consumer performed.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **UIColours** (`DESIGN-SITE-043`): Evaluate chart categorical colours, income/outgo status and foreground/background contrast. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.


## Motion UX, animazioni e video — lotto 18 fonti 20/11/2026

[Audit licenze e compatibilita'](../sources/MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](../sources/MOTION_VIDEO_18_PIPELINE_2026-11-20.md) · [Manifest SHA](../sources/MOTION_VIDEO_18_REGISTRY_2026-11-20.json).

- **manim** (`MOTION-OSS-008`): Optional finance education charts, not live app UI. **PROPOSED_ONLY**.

**Vincoli:** il media render resta separato dal runtime APK; Flutter/Compose devono usare il donor/framework nativo prima di TSX/JavaScript; licenza dell'asset e del runtime va verificata singolarmente. Nessuna modifica a Product Bible, UI, database, funzioni, codice, build o screenshot del consumer. Priorita' estetica agli asset e mock-up gia' scelti nel Design-App; a11y, reduced motion, FPS/batteria e privacy da validare in una eventuale implementazione.


## Jiro Build e Builder — fonti Web per marketing (20/11/2026)

[Audit, deduplica e licenze](../sources/JIRO_AND_15_DESIGN_LINKS_DEDUP_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.md) · [Mappa JSON](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.json).

- **Jiro Prompt Library** (`DESIGN-SITE-044`): Study fintech landing structure, trust messaging, responsible financial copy and clear value proposition. **PROPOSED_ONLY**.
- **Jiro Builder** (`DESIGN-SUBL-003`): Consider draft Web campaign layout; never copy bank branding or claim automatic security compliance. **PROPOSED_ONLY**.

**Gate:** Jiro e' una libreria proprietaria di design Web/React e un servizio esterno di hosting; nessun widget Flutter/Compose importato e nessun piano acquistato. I Termini consentono i progetti propri/clienti ma vietano ricollezionare o rivendere componenti/template standalone, il che preclude il copy del catalogo nella nostra libreria. Il Builder Free prevede limiti crediti e inattivita' e l'esportazione ZIP richiede un piano. Gli asset e mock-up preferiti gia' approvati in Design-App prevalgono; nessun codice consumer, server, auth, dati, palette, release o design deciso è stato modificato.
