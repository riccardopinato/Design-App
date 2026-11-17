# Deskland Android — Dossier Design-App

**Registro permanente:** `PER_APP/deskland-android.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Launcher Android interattivo con accenti desktop/spatial 3D; gesti e leggibilità prime, effetti visivi dopo stabilità.

**Categorie da studiare:** desktop · launcher · batteria/widget · meteo se reale.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. icone app nella home launcher.
2. drag/drop e selezione tile.
3. controlli player/effetti dove realmente presenti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-003 · battery-charging](https://gentleface.com/icons/battery-charging) | MEDIUM | widget stato batteria reale | VERIFIED_DETAIL |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | avvio animazione o elemento interattivo | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa effetti quando previsto | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | launcher home senza costi animazioni | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `home`, `play`, `battery-charging`.

## Animazioni e feedback proposti

- risposta drag a 60 fps e rilascio leggibile.
- transizione selezione/long-press sobria.

## Cosa evitare

- animazioni continue che rallentano il launcher.
- finti indicatori batteria o meteo.
- effetti sofisticati prima di eliminare i glitch.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | MEDIUM | launcher accessibility and touch-state review |
| DSK-004 — Emil Design Engineering | HIGH | long-press drag, icon motion and frame pacing |
| DSK-009 — UI UX Pro Max | HIGH | launcher spatial controls, only after functional stability |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
