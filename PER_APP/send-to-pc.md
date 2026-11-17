# Send-to-PC — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Trasferimento file LAN QR/Wi-Fi, feedback immediato sulla consegna e stato di connessione.

**Temi candidati:** PC; file; Wi-Fi; QR; trasferimento.

## Superfici e placement proposti

1. selezione file e dispositivo.
2. progresso upload realmente tracciato.
3. conferma ricezione e errori.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | trasferimento in corso | VERIFIED_DETAIL |
| [ICO-025 · messages](https://gentleface.com/icons/messages) | MEDIUM | stati trasferimento con etichette testuali | VERIFIED_DETAIL |

**Nuove icone da cercare/disegnare:** loader, check, messages. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- progress loop solo quando byte trasferiti.
- check solo con ricevuta endpoint.

## Cosa evitare

- successo prima di completare il trasferimento.
- icone oscillanti durante ricerca in background.

## Fonti e skill di design

Nessuna skill dell'intake anti-slop mappata per questa destinazione.

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
