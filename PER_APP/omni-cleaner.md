# Omni Cleaner — Dossier Design-App

**Registro permanente:** `PER_APP/omni-cleaner.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility di pulizia con schermate separate e UI fluida: galleria foto/video a formato originale e player reale.

**Categorie da studiare:** galleria · video · eliminazione sicura · scansione · archivio.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. pulsanti per accedere alle singole funzioni.
2. galleria foto senza ritagli.
3. video player con play/pause e decisione prima dell'eliminazione.
4. scansione e progresso reale.
5. conferma eliminazione con reversibilità ove disponibile.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-005 · download](https://gentleface.com/icons/download) | MEDIUM | download solo se esiste funzione | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | HIGH | apertura galleria a dimensione intera | VERIFIED_DETAIL |
| [ICO-009 · video](https://gentleface.com/icons/video) | HIGH | player video in galleria | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | MEDIUM | filtri media e file | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | scansione in corso, mai fingere progressi | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | operazione completata con successo | VERIFIED_SITE |
| [ICO-020 · play](https://gentleface.com/icons/play) | HIGH | riproduzione video reale | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | HIGH | pausa player video | VERIFIED_SITE |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | loop player video se presente | VERIFIED_DETAIL |
| [ICO-023 · eye](https://gentleface.com/icons/eye) | HIGH | anteprima contenuti multimediali | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `images`, `video`, `play`, `pause`, `check`.

## Animazioni e feedback proposti

- transizione apertura galleria o player una sola volta.
- play/pause con stato leggibile.
- loader solo su scansione reale.

## Cosa evitare

- simulare la liberazione di spazio prima di terminarla.
- autoeliminare asset o presentare anteprime ritagliate.
- inseguire il design sacrificando frame rate.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | MEDIUM | less generic utility UI and state feedback |
| DSK-002 — Impeccable | HIGH | dedicated feature screens and gallery/video UX checks |
| DSK-004 — Emil Design Engineering | HIGH | smooth transitions between function screens |
| DSK-006 — Anthropic Frontend Design | MEDIUM | distinctive but restrained utility aesthetic |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | feature navigation, gallery and media controls |
| DSK-009 — UI UX Pro Max | HIGH | utility redesign with component variants |
| DSK-010 — Stageshow | MEDIUM | feature-page visuals using actual app flows |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
