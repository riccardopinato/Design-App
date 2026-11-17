# Web Utility Factory — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Landing e strumenti web SEO-first con UX sobria, interazioni leggere, accessibilità e tempi di caricamento prioritari.

**Temi candidati:** strumenti; browser; SEO/ricerca; conferma.

## Superfici e placement proposti

1. lista tool e ricerca.
2. stati vuoti/input/form.
3. download risultato soltanto se pronto.

## Icone Gentleface collegate (molti-a-molti)

Nessuna icona Gentleface associata direttamente: non assumere che un asset sia disponibile.

**Nuove icone da cercare/disegnare:** search, check, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- hover e feedback tastiera/mouse con prefers-reduced-motion.
- nessun loop decorativo sopra la form principale.

## Cosa evitare

- JS/icon-pack pesanti per aggiungere una semplice decorazione.
- sovraccarico bento che riduce conversione e SEO.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-003 — Taste Skill | HIGH | SEO utility site landing and conversion flows |
| DSK-005 — Vercel Web Design Guidelines | HIGH | SEO-first accessible utility web UI |
| DSK-007 — Hallmark | MEDIUM | landing experiments; prioritize SEO and speed |
| DSK-010 — Stageshow | MEDIUM | service landing feature illustrations |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.
