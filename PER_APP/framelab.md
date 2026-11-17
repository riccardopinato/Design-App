# FrameLab — Dossier Design-App

**Registro permanente:** `PER_APP/framelab.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Editor fotografico premium editoriale: visuali originali grandi, gesti precisi, icone essenziali.

**Categorie da studiare:** fotografia · editing · export · media.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. barra strumenti editing.
2. galleria e anteprime.
3. salvataggio/export reale.
4. supporti media.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-006 · export](https://gentleface.com/icons/export) | HIGH | export media | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | HIGH | raccolta fotografie | VERIFIED_DETAIL |
| [ICO-009 · video](https://gentleface.com/icons/video) | MEDIUM | selezione e anteprima video | VERIFIED_DETAIL |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | anteprima multimediale | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa anteprima | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `images`, `export`, `video`.

## Animazioni e feedback proposti

- toggle strumento con stato evidente.
- micro-feedback export dopo completamento reale.

## Cosa evitare

- icone decorative sul contenuto fotografico.
- animazioni pesanti durante gesture di editing.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | photo and visual hierarchy |
| DSK-002 — Impeccable | HIGH | premium photo-editor controls |
| DSK-003 — Taste Skill | MEDIUM | editorial product landing |
| DSK-004 — Emil Design Engineering | HIGH | photo controls and gesture responsiveness |
| DSK-006 — Anthropic Frontend Design | HIGH | photographic editorial premium direction |
| DSK-007 — Hallmark | HIGH | editorial product showcase |
| DSK-009 — UI UX Pro Max | HIGH | photo UI token and contrast reference |
| DSK-010 — Stageshow | HIGH | visual editor demonstrations |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
