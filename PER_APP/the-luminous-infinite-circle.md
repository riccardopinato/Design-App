# The Luminous Infinite Circle — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Notifiche visive e AOD accessibili, priorità utenti con esigenze di accessibilità; animazione come segnale, non decorazione.

**Temi candidati:** cerchio luminoso; LED flash; notifica; accessibilità.

## Superfici e placement proposti

1. anteprima effetti AOD.
2. selezione modalità di avviso.
3. stato notifiche ricevute.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | feedback notifica senza sostituire allarme | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** bell-ring, check, gauge. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- anello solo per evento notificato e quando consentito.
- interrompi su silenzioso/risparmio secondo requisiti prodotto.

## Cosa evitare

- animazione persistente che consuma batteria.
- colore come unico canale di identificazione.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-009 — UI UX Pro Max | MEDIUM | accessible visual-alert semantics |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
