# Wonderlog — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/wonderlog.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Diario viaggi colorato, foto originali, punti mappa e timeline con microinterazioni naturali.

**Temi candidati:** viaggio; mappa; tappe; foto e ricordi.

## Superfici e placement proposti

1. selezione luoghi in mappa.
2. galleria viaggio.
3. salvataggio preferiti/tappe.
4. diario e date itinerario.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | MEDIUM | itinerario giornaliero | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | MEDIUM | guide o file offline | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | HIGH | export diario | VERIFIED_DETAIL |
| [ICO-007 · import](https://gentleface.com/icons/import) | MEDIUM | import itinerario | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | MEDIUM | galleria viaggio | VERIFIED_DETAIL |
| [ICO-009 · video](https://gentleface.com/icons/video) | MEDIUM | clip e ricordi del viaggio | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | MEDIUM | luoghi e tappe preferite | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca viaggi e luoghi | VERIFIED_DETAIL |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | selezione luogo | VERIFIED_SITE |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | luoghi preferiti | VERIFIED_SITE |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | ricorrenza in pianificazione dove implementata | VERIFIED_DETAIL |
| [ICO-025 · messages](https://gentleface.com/icons/messages) | MEDIUM | note condivise | VERIFIED_DETAIL |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | home viaggi | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** map-pin, images, star. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- feedback selezione waypoint con easing breve.
- transizione pagina foto senza tagli.

## Cosa evitare

- icone turistiche stereotipate.
- animazioni che peggiorano tracking GPS o map scroll.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | travel visual language and image-led views |
| DSK-002 — Impeccable | MEDIUM | travel cards and map overlay polish |
| DSK-004 — Emil Design Engineering | HIGH | map and journal transitions |
| DSK-006 — Anthropic Frontend Design | HIGH | colourful travel narrative |
| DSK-008 — Better Interfaces (Jakub Krehel) | MEDIUM | image/locale overflow checks |
| DSK-009 — UI UX Pro Max | HIGH | travel journal palette and components |
| DSK-010 — Stageshow | HIGH | travel journey product highlights |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Voice Orb — proposta futura (HIGH)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Audio-diario delle tappe e dei viaggi.
- **Collocazione candidata:** Dettaglio tappa/ricordo.
- **Adattamento estetico:** colori viaggio esistenti.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (HIGH)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (HIGH):** Open photographic travel memory cover. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Travel-card secondary metadata. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Travel diary and image-led lists. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Switch to a travel memory scene. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Map/diary offline loading. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (HIGH)** — Foto e memorie viaggio a card. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (HIGH)** — Timeline di tappe o media con data collegata. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (HIGH)** — Filtra tappe per intervallo date. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Condivisione viaggi se autenticazione approvata. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Titolo editoriale raccolte viaggio. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (MEDIUM)** — Condivisione diario viaggio con conferma reale. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Impegni di viaggio oggi solo se dati pianificati. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Tempo alla tappa/evento di viaggio. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-003 · Pulsating Dots (MEDIUM)** — Caricamento tappa. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/pulsating-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-007 · Apple Breathe (MEDIUM)** — Apertura diario viaggio. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-breathe.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-011 · Morph Loader (MEDIUM)** — Passaggio tra ricordi. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/morph-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-018 · Range Selection Slider (HIGH)** — Filtro date viaggio. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/range-selection-slider/base.tsx); già censito: `WML-004`. Stato: `PROPOSED_ONLY`.
- **DBM-024 · View On Map (HIGH)** — Anteprima mappa dei luoghi, mantenendo OSM se previsto. Evidenza: `SOURCE_FILE_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/view-on-map/base.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-030 · Infinite Spiral (MEDIUM)** — Showcase foto viaggio, non galleria principale. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 6 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `EXPERIENCE+OPERATE`, fit MEDIUM. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Diario viaggio, luoghi, mappa.
- **Miglioramento proposto:** Foto e ricordi protagonisti senza appesantire navigazione o routing; evitare scroll con layout disomogeneo.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Mappa/overlay non coprono CTA o contenuto
  - [ ] Fotografie nel loro formato originale
  - [ ] Schede lunghe e offline leggibili
  - [ ] Accesso a tappe e mappa senza route inventate

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-001, DCL-006, DCL-007, DCL-010.
- **Schermate:** Viaggi, diari, foto e mappa.
- **Vincolo:** No immagini tagliate; viaggio e navigazione non sacrificati.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-003 — [gharsh11032000/tricky-cheetah-78](https://uiverse.io/gharsh11032000/tricky-cheetah-78)**: Card contenuti/insight con reveal accessibile (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-003_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**40 preferiti proposti per wonderlog**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-013](https://uiverse.io/AqFox/young-dragon-29) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-022](https://uiverse.io/Lakshay-art/curvy-earwig-22) | INPUT | Ricerca o inserimento con label | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Scelta esclusiva accessibile | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-026](https://uiverse.io/Nawsome/brave-turtle-26) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-031](https://uiverse.io/Novaxlo/rotten-lionfish-4) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-031_original.css) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-036](https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html) |
| [UIV-037](https://uiverse.io/Prince4fff/slippery-baboon-37) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html) |
| [UIV-038](https://uiverse.io/Priyanshu02020/popular-puma-87) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.css) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-041](https://uiverse.io/Shoh2008/ugly-elephant-80) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-053](https://uiverse.io/barisdogansutcu/plastic-dolphin-67) | TOOLTIP | Aiuto contestuale non solo hover | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html) |
| [UIV-054](https://uiverse.io/byllzz/great-wombat-13) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-054_original.css) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-072](https://uiverse.io/gsperandio/shaggy-kangaroo-12) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html) |
| [UIV-073](https://uiverse.io/ilkhoeri/thin-bobcat-83) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-073_original.css) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-077](https://uiverse.io/kennyotsu/fast-emu-70) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-081](https://uiverse.io/kennyotsu/tender-badger-21) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-081_original.css) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Tappa o diario viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-097](https://uiverse.io/vamsidevendrakumar/soft-shrimp-94) | CARD | Tappa o diario viaggio | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**8 nuovi collegamenti** all'archivio Uiverse. Proposte estetiche, non modifiche funzionali o test runtime.

| Sorgente | Categoria | Superficie proposta | Fit | Codice originale |
|---|---|---|---|---|
| [UIV-101](https://uiverse.io/Javierrocadev/chatty-ladybug-95) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.css) |
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-107](https://uiverse.io/elijahgummer/new-fly-30) | LOADER | Calcolo itinerario o media in corso | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-107_original.css) |
| [UIV-109](https://uiverse.io/mamyapro123/curvy-bear-51) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.css) |
| [UIV-110](https://uiverse.io/roroland/average-horse-2) | TOOLTIP | Legenda mappa/tappe accessibile | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-110_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Input nuova tappa e descrizione viaggio | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Stato: **PROPOSED_ONLY**. Per il riuso rispettare Product Bible, accessibilità e test; loader solo per lavoro realmente attivo; nessuna autenticazione obbligatoria nuova.
[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).


## Fonti di design — 20/11/2026

[Audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [Matrice](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press — **PROPOSED_ONLY**.
- **Coolors** (`DESIGN-SITE-024`): Generate candidate 5-color palettes, then test in actual screen — **PROPOSED_ONLY**.
- **Cosmos** (`DESIGN-SITE-028`): Moodboard collections and search by color/similarity — **PROPOSED_ONLY**.

Nessun asset, font, logo o codice importato. Sono richiesti approvazione estetica, Product Bible, licenza e QA sulle schermate reali.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Best Designs on X** (`DESIGN-SITE-029`): Discover travel postcards, timelines and destination imagery presentation. **PROPOSED_ONLY**.
- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study trip timeline and map/filter mobile layouts. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): Trip summary, photo collage, next waypoint, offline state tiles. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.


## Nuove reference UI — 20/11/2026 (deduplica 15 → 3)

[Audit selettivo](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md) · [Matrice per-app](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json).

- **Mobbin** (`DESIGN-SITE-033`): Compare travel itinerary, saved trip and map-to-detail journeys — **PROPOSED_ONLY**.

Queste fonti non autorizzano il riutilizzo di screenshot o font senza licenza. Mobbin vieta l'archiviazione/mirroring dei contenuti; React Bits usa MIT + Commons Clause; ThinkUI richiede attivazione MCP a pagamento. Nessuna app o feature implementata da questo intake.


## Nuove referenze visuali e cromatiche — 20/11/2026

[Audit fonte e licenze](../sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md) · [Matrice app](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/CURATED_DESIGNS_UICOLOURS_APP_MAP_2026-11-20.json).

- **BestSaaSWebDesigns — Curated Designs** (`DESIGN-SITE-042`): Explore postcard, travel map and journey storytelling visual identities. **PROPOSED_ONLY**.
- **UIColours** (`DESIGN-SITE-043`): Develop mapped theme tokens for travel cards and daylight/dark outdoor readability. **PROPOSED_ONLY**.

Le palette e i mock-up gia' approvati hanno priorita'; la fonte non concede il riuso automatico di asset di brand/post X e non garantisce esportazione diretta in Flutter. Nessuna UI implementata o tema consumer modificato.
