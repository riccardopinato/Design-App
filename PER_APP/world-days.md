# World Days — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Giornate del mondo: schede editoriali colorate, densità informativa elevata e palette esistente da mantenere.

**Temi candidati:** calendario; ricorrenza; storia; preferiti; offline.

## Superfici e placement proposti

1. scheda giornata e informazioni varie.
2. salvataggio preferiti.
3. navigazione calendario e download contenuti.
4. sezioni storiche multilingue.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | avviso contenuto disponibile | VERIFIED_SITE |
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | HIGH | navigazione giorni | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | contenuti offline | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | MEDIUM | condivisione/export soltanto se implementato | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | HIGH | salva ricorrenze | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca giornate | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | download e caricamento reale | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | download verificato | VERIFIED_SITE |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | MEDIUM | localizzazione evento solo se presente | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | download contenuti reale | VERIFIED_SITE |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | giornate preferite | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | MEDIUM | collezioni archiviate se supportate | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | home delle ricorrenze | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** calendar, bookmark, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- bookmark breve dopo salvataggio reale.
- download solo durante trasferimento.
- microtransizione giorno senza variare i colori.

## Cosa evitare

- spostare informazioni in icone senza testo.
- cambiare la palette che l'utente ha già approvato.
- celebrare un contenuto ancora non certificato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | daily content cards and empty-state polish |
| DSK-002 — Impeccable | HIGH | content density, long-copy and reader flow |
| DSK-003 — Taste Skill | MEDIUM | content discovery pages where web-native |
| DSK-004 — Emil Design Engineering | MEDIUM | subtle content-card transitions |
| DSK-005 — Vercel Web Design Guidelines | HIGH | content-heavy web views and navigation |
| DSK-006 — Anthropic Frontend Design | HIGH | recognizable day-story cards |
| DSK-007 — Hallmark | MEDIUM | public promotional pages |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | long story and multilingual layouts |
| DSK-009 — UI UX Pro Max | HIGH | information-card design and locale-aware typography |
| DSK-010 — Stageshow | HIGH | new rich-story feature preview |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
