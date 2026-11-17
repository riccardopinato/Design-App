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
