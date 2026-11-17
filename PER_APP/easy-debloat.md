# Easy Debloat — Dossier Design-App

**Registro permanente:** `PER_APP/easy-debloat.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility sicurezza minimale premium: SAFE/CAUTION/DANGEROUS sempre espliciti e accessibili.

**Categorie da studiare:** package app · rimozione controllata · severità rischio · diagnostica.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. lista applicazioni e dettagli.
2. flusso disattivazione/disinstallazione con conferma.
3. esiti Shizuku/ADB e prerequisiti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-023 · eye](https://gentleface.com/icons/eye) | MEDIUM | espandi dettagli app | VERIFIED_SITE |
| [ICO-027 · shield-check](https://gentleface.com/icons/shield-check) | MEDIUM | operazione sicura ma mai garanzia assoluta | ANIMATION_UNVERIFIED |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `eye`, `check`, `shield-check`.

## Animazioni e feedback proposti

- conferma azione solo dopo esito comando reale.
- breve espansione dettagli senza movimento eccessivo.

## Cosa evitare

- scudo o check che implica protezione automatica.
- rosso/verde come unico canale informativo.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-009 — UI UX Pro Max | HIGH | severity-safe utility tokens |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.
