# Phone Guard — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Utility protezione affidabile; etichette di rischio, gravità e stato servizio verificabili.

**Temi candidati:** protezione; avvisi; dispositivo; diagnostica.

## Superfici e placement proposti

1. stato protezione corrente.
2. warning e allarme solo se veri.
3. impostazioni permessi e servizio.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-027 · shield-check](https://gentleface.com/icons/shield-check) | HIGH | stato protezione confermato | ANIMATION_UNVERIFIED |

**Nuove icone da cercare/disegnare:** shield-check, check, bell-ring. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- attivazione solo dopo conferma stato servizio.
- warning breve con alternativa accessibile.

## Cosa evitare

- scudo sempre animato anche con servizio inattivo.
- tocco che sembra un 'PASS' senza diagnosi.

## Fonti e skill di design

Nessuna skill dell'intake anti-slop mappata per questa destinazione.

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
