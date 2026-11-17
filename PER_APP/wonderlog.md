# Wonderlog — Dossier Design-App

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
