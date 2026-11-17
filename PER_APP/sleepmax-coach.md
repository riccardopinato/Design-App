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
