# CamperBoss — Dossier Design-App

**Registro permanente:** `PER_APP/camperboss.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility camper outdoor verde/bosco e oro; uso in viaggio e offline con controlli facili da leggere.

**Categorie da studiare:** camper/van · acqua ed energia · aree sosta · tracciati.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. download pacchetti offline.
2. tap e aree sosta.
3. stati risorse e checklist.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | MEDIUM | tappe e pianificazione | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | pacchetti offline | VERIFIED_DETAIL |
| [ICO-007 · import](https://gentleface.com/icons/import) | MEDIUM | import dati offline | VERIFIED_DETAIL |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | aree sosta o tappe | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | MEDIUM | indicatori risorse camper | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `download`, `map-pin`, `calendar`.

## Animazioni e feedback proposti

- download soltanto durante trasferimento reale.
- microconferma dopo salvataggio tappa.

## Cosa evitare

- animazioni pesanti durante navigazione e GPS.
- simboli che confondono risorsa critica e stato estetico.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-008 — Better Interfaces (Jakub Krehel) | MEDIUM | offline guide accessibility |
| DSK-009 — UI UX Pro Max | HIGH | outdoor readability and maps |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
