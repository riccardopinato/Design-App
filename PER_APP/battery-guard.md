# Battery Guard — Dossier Design-App

**Registro permanente:** `PER_APP/battery-guard.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility verde e pulita; l'informazione sulla batteria deve rimanere prioritaria rispetto all'estetica.

**Categorie da studiare:** batteria · ricarica · risparmio energetico · allerta.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. stato batteria reale e gauge.
2. indicatore di carica.
3. avvisi soglia batteria.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | avviso batteria non critico | VERIFIED_SITE |
| [ICO-003 · battery-charging](https://gentleface.com/icons/battery-charging) | HIGH | stato carica reale | VERIFIED_DETAIL |
| [ICO-004 · battery-low](https://gentleface.com/icons/battery-low) | HIGH | soglia batteria realmente rilevata | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | MEDIUM | analisi dati in corso | VERIFIED_DETAIL |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | HIGH | stato batteria | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `battery-charging`, `battery-low`, `gauge`.

## Animazioni e feedback proposti

- carica pulsante solo mentre la ricarica è effettiva e schermata visibile.
- successo cambio impostazione dopo conferma.

## Cosa evitare

- fake animation che implica protezione attiva.
- consumo energetico dell'animazione superiore al suo valore.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | HIGH | readable metrics and actionable status |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | information clarity and warning states |
| DSK-009 — UI UX Pro Max | HIGH | clean battery analytics theme |
| DSK-010 — Stageshow | MEDIUM | clean metrics app-store screenshots |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (MEDIUM)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* DESCRIPTIVE_CATALOG_ONLY; status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* DESCRIPTIVE_CATALOG_ONLY; status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.
