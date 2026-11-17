# TrailPath — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Mappe outdoor forest/moss con controlli robusti e alto contrasto sul percorso.

**Temi candidati:** mappa; traccia; waypoint; offline.

## Superfici e placement proposti

1. selezione waypoint.
2. routing e stato GPS reale.
3. download GPX/mappe solo se funzione attiva.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | waypoint e posizione | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** map-pin, download, check. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- pulse waypoint solo dopo selezione.
- nessun motion che copra la rotta o i controlli.

## Cosa evitare

- UI decorativa che oscura la cartografia.
- presentare routing non funzionante come confermato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-004 — Emil Design Engineering | HIGH | map control and route-state transitions |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | map touch targets and offline states |
| DSK-009 — UI UX Pro Max | HIGH | map utility and nature-tech |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
