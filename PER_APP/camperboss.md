# CamperBoss — Dossier Design-App

**Registro permanente:** `PER_APP/camperboss.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility camper outdoor verde/bosco e oro; uso in viaggio e offline con controlli facili da leggere.

**Categorie da studiare:** camper/van · acqua ed energia · aree sosta · tracciati.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. download pacchetti offline.
2. tap e aree sosta.
3. stati risorse e checklist.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | MEDIUM | tappe e pianificazione | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | pacchetti offline | VERIFIED_DETAIL |
| [ICO-007 · import](https://gentleface.com/icons/import) | MEDIUM | import dati offline | VERIFIED_DETAIL |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | aree sosta o tappe | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | MEDIUM | indicatori risorse camper | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `download`, `map-pin`, `calendar`.

## Animazioni e feedback proposti

- download soltanto durante trasferimento reale.
- microconferma dopo salvataggio tappa.

## Cosa evitare

- animazioni pesanti durante navigazione e GPS.
- simboli che confondono risorsa critica e stato estetico.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-008 — Better Interfaces (Jakub Krehel) | MEDIUM | offline guide accessibility |
| DSK-009 — UI UX Pro Max | HIGH | outdoor readability and maps |

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

- **Idea:** Memo di tappa camper solo in condizioni di utilizzo sicuro.
- **Collocazione candidata:** Diario tappa.
- **Adattamento estetico:** verde/bosco oro.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Travel stop information and offline guide. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Offline package preparation, show measured progress when possible. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Questa sezione contiene **proposte**; nessuna libreria installata, nessuna feature consumer confermata dal solo catalogo.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Album di tappe. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (MEDIUM)** — Soglie risorse o durata tappa. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (MEDIUM)** — Filtro date disponibilità/capacità solo se feature presente. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (MEDIUM)** — Organizza viaggio condiviso solo se supportato. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Check-list tappa o partenza solo quando programmata. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Tempo alla partenza concordata. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.


**Gate comune:** rispettare Product Bible, accessibilità, controlli di input alternativi, riduzione movimento, performance, colore e lingua; Flutter/Compose richiedono adattamento nativo dei componenti React. I riferimenti `Text Gradient`, `Notification List` e `Flip Clock` non hanno un file componente esatto verificato alla baseline e restano `REFERENCE`.

**Storico 17/11/2026:** proposte inserite in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, con provenienza e stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-024 · View On Map (HIGH)** — Visualizzazione area sosta o tappa. Evidenza: `SOURCE_FILE_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/view-on-map/base.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 1 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-002, DCL-004, DCL-007, DCL-010.
- **Schermate:** Dashboard viaggio, controlli.
- **Vincolo:** Offline e leggibilità in esterno prioritari.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**37 preferiti proposti per camperboss**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-012](https://uiverse.io/Admin12121/massive-dodo-67) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-012_original.html) |
| [UIV-013](https://uiverse.io/AqFox/young-dragon-29) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html) |
| [UIV-015](https://uiverse.io/FColombati/spotty-snake-82) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.css) |
| [UIV-016](https://uiverse.io/Gidarx/clever-panther-6) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-016_original.css) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-018](https://uiverse.io/JaydipPrajapati1910/average-shrimp-57) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-018_original.html) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-026](https://uiverse.io/Nawsome/brave-turtle-26) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-031](https://uiverse.io/Novaxlo/rotten-lionfish-4) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.css) |
| [UIV-036](https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-041](https://uiverse.io/Shoh2008/ugly-elephant-80) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-058](https://uiverse.io/cssbuttons-io/mean-dolphin-24) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-058_original.html) |
| [UIV-059](https://uiverse.io/cuzpq/gentle-goat-72) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-059_original.html) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-063](https://uiverse.io/dexter-st/tough-falcon-78) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-063_original.css) |
| [UIV-070](https://uiverse.io/gagan-gv/unlucky-yak-4) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html) |
| [UIV-071](https://uiverse.io/gharsh11032000/sour-vampirebat-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-071_original.html) |
| [UIV-072](https://uiverse.io/gsperandio/shaggy-kangaroo-12) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-078](https://uiverse.io/kennyotsu/giant-sloth-18) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-078_original.css) |
| [UIV-082](https://uiverse.io/kennyotsu/wise-rattlesnake-92) | CARD | Card di anteprima/collezione | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html) |
| [UIV-085](https://uiverse.io/m1her/odd-fireant-56) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.css) |
| [UIV-086](https://uiverse.io/mamyapro123/cuddly-warthog-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.css) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-090](https://uiverse.io/mobinkakei/strong-lizard-79) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-090_original.html) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Card di anteprima/collezione | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-100](https://uiverse.io/zanina-yassine/afraid-eel-50) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-100_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**4 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Input destinazione/itinerario anche offline | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-107](https://uiverse.io/elijahgummer/new-fly-30) | LOADER | Importazione dati offline in corso | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.css) |
| [UIV-109](https://uiverse.io/mamyapro123/curvy-bear-51) | FORM | Input destinazione/itinerario anche offline | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Input destinazione/itinerario anche offline | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).
