# CashMate AI — Dossier Design-App

**Registro permanente:** `PER_APP/cashmate-ai.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Blocchi finanziari verde/nero, gerarchia monetaria rigorosa; icone discrete, contrasto e semantica prioritarie.

**Categorie da studiare:** portafoglio · spese e incassi · grafici · sicurezza.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. dashboard saldi.
2. categorie transazione.
3. grafici trend.
4. backup soltanto se realmente disponibile.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | backup o cloud solo se implementato | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | MEDIUM | indicatori finanziari | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `gauge`, `check`, `lock`.

## Animazioni e feedback proposti

- feedback transazione salvata realmente.
- grafici stabili senza movimento che cambia lettura dei dati.

## Cosa evitare

- icone decorative accanto a ogni importo.
- usare colore solo per significato positivo/negativo.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | MEDIUM | financial data visual hierarchy |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | money formatting, disclosure and graphs |
| DSK-009 — UI UX Pro Max | HIGH | semantic finance palettes |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
