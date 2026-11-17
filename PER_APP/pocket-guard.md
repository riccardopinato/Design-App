# Pocket Guard — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Protezione tasca/borsa, pannelli di stato sensori e viaggio; priorità sicurezza e risparmio batteria.

**Temi candidati:** borsa; sensori; scudo; PIN; viaggio.

## Superfici e placement proposti

1. attivazione protezione e diagnostica.
2. Journey Guard.
3. sblocco PIN/biometria.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-004 · battery-low](https://gentleface.com/icons/battery-low) | MEDIUM | avviso stato batteria dispositivo | VERIFIED_DETAIL |
| [ICO-027 · shield-check](https://gentleface.com/icons/shield-check) | HIGH | protezione effettivamente attiva e sana | ANIMATION_UNVERIFIED |
| [ICO-028 · lock](https://gentleface.com/icons/lock) | HIGH | PIN o biometria con stato reale | ANIMATION_UNVERIFIED |

**Nuove icone da cercare/disegnare:** shield-check, lock, battery-low. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- microconferma armamento soltanto dopo avvenuto.
- stop animazioni durante monitoraggio in background.

## Cosa evitare

- falso scudo verde quando permessi o sensori sono disattivati.
- lavoro continuo GPU mentre sorveglia.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-009 — UI UX Pro Max | HIGH | protection state UI |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-005 · Face Id Scan (HIGH)** — Conferma sblocco sicurezza solo dopo API OS. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/face-id-scan.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 1 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.
