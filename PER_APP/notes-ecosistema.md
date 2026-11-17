# Notes-Ecosistema — Dossier Design-App

**Registro permanente:** `PER_APP/notes-ecosistema.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Workspace editoriale note/canvas, gerarchia leggibile, comandi semantici in equilibrio con UI bento.

**Categorie da studiare:** nota · cartelle · canvas · tag/bookmark · import/export.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. editor note e barra formattazione.
2. canvas e selezione strumenti.
3. ricerca e bookmark.
4. import/export.
5. stati protetti se disponibili.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | download esportazioni | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | HIGH | esportazione note | VERIFIED_DETAIL |
| [ICO-007 · import](https://gentleface.com/icons/import) | HIGH | import note | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | MEDIUM | immagini nelle note | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | HIGH | segnalibri note | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca note e canvas | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | strumenti visuali opzionali | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | MEDIUM | import o indicizzazione reale | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | modifica salvata | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | sync solo se backend attivo | VERIFIED_SITE |
| [ICO-022 · repeat](https://gentleface.com/icons/repeat) | MEDIUM | ripeti azione solo se reversibile | VERIFIED_DETAIL |
| [ICO-023 · eye](https://gentleface.com/icons/eye) | HIGH | mostra/nascondi pannello o contenuto | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | HIGH | archivio note con restore | VERIFIED_SITE |
| [ICO-025 · messages](https://gentleface.com/icons/messages) | MEDIUM | commenti collaborativi solo dove supportati | VERIFIED_DETAIL |
| [ICO-028 · lock](https://gentleface.com/icons/lock) | MEDIUM | sezioni protette solo se presenti | ANIMATION_UNVERIFIED |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `search`, `bookmark`, `export`.

## Animazioni e feedback proposti

- focus visivo del tool attivo.
- conferma salvataggio e sync solo se completati.
- minimo motion durante disegno a mano libera.

## Cosa evitare

- animazione nel tracciato ink che compromette precisione.
- toolbar troppo ricche.
- stati di sync non verificati.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | editor and responsive workflow refinement |
| DSK-002 — Impeccable | HIGH | editor density, hierarchy and responsive review |
| DSK-003 — Taste Skill | MEDIUM | web product landing, not the native editor |
| DSK-004 — Emil Design Engineering | HIGH | canvas/drag/selection and feedback |
| DSK-005 — Vercel Web Design Guidelines | HIGH | web editor/desktop accessibility |
| DSK-006 — Anthropic Frontend Design | HIGH | knowledge-workspace information hierarchy |
| DSK-007 — Hallmark | MEDIUM | landing feature stories |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | complex editor and long-text states |
| DSK-009 — UI UX Pro Max | HIGH | editor/canvas design-token consistency |
| DSK-010 — Stageshow | HIGH | workspace feature illustrations and demo |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
