# Tabletop Motion Alarm — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Antifurto tavolo: conto alla rovescia, sirena e stato armamento sempre chiari e robusti.

**Temi candidati:** allarme; movimento; PIN; dispositivo.

## Superfici e placement proposti

1. countdown prima di armamento.
2. stato sensori/arma.
3. sblocco PIN e segnalazione intruso.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-027 · shield-check](https://gentleface.com/icons/shield-check) | HIGH | allarme armato confermato | ANIMATION_UNVERIFIED |
| [ICO-028 · lock](https://gentleface.com/icons/lock) | HIGH | stato antifurto verificato | ANIMATION_UNVERIFIED |

**Nuove icone da cercare/disegnare:** shield-check, lock, bell-ring. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- transizione solo dopo armamento reale.
- no motion estetico durante sirena/controlli critici.

## Cosa evitare

- allarme armato visualizzato prematuramente.
- animazioni che impediscono accesso a Disarma.

## Fonti e skill di design

Nessuna skill dell'intake anti-slop mappata per questa destinazione.

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Countdown armamento 5 secondi con leggibilità e controllo Disarma prioritari. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.
