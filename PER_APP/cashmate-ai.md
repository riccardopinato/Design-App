# CashMate AI — Dossier Design-App

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
