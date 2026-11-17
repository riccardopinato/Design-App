# SleepMax Coach — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Routine serale sobria e calma; meno luminosità/movimento, accessibilità notturna.

**Temi candidati:** sonno; luna; sveglia; routine.

## Superfici e placement proposti

1. routine prima del sonno.
2. promemoria e sveglie.
3. ripetizione di appuntamenti.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | HIGH | promemoria routine | VERIFIED_SITE |
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | MEDIUM | programma routine | VERIFIED_SITE |
| [ICO-015 · heart-pulse](https://gentleface.com/icons/heart-pulse) | MEDIUM | benessere non medico con disclaimer | VERIFIED_DETAIL |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | ripeti routine | VERIFIED_DETAIL |

**Nuove icone da cercare/disegnare:** bell-ring, repeat, calendar. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- fade molto lento per un cambio di stato, non per ogni tap.
- conferma notifica pianificata dopo esito reale.

## Cosa evitare

- loop luminosi che disturbano l'utente.
- icone che suggeriscono misurazione clinica senza sensori.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-009 — UI UX Pro Max | MEDIUM | calm routine controls |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (HIGH)** — Durata routine e promemoria a intervalli. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (HIGH)** — Riepilogo routine sonno soltanto all'orario/avvio previsto. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Timer preparazione al riposo o routine reale. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-007 · Apple Breathe (HIGH)** — Preparazione routine non disturbante. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-breathe.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-010 · Apple Pulse Dots (MEDIUM)** — Riepilogo routine. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-pulse-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-013 · Clock Spinner (HIGH)** — Aggiornamento timer/pianificazione. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/clock-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-021 · Notification List (HIGH)** — Riepilogo routine effettive. Evidenza: `EXACT_SOURCE_NOT_LOCATED`; sorgente esatto da identificare; già censito: `WML-008`. Stato: `PROPOSED_ONLY`.
- **DBM-025 · Bouncing Lines (MEDIUM)** — Caricamento routine. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bouncing-lines.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 5 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.
