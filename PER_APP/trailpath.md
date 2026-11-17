# TrailPath — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Mappe outdoor forest/moss con controlli robusti e alto contrasto sul percorso.

**Temi candidati:** mappa; traccia; waypoint; offline.

## Superfici e placement proposti

1. selezione waypoint.
2. routing e stato GPS reale.
3. download GPX/mappe solo se funzione attiva.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | HIGH | waypoint e posizione | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** map-pin, download, check. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- pulse waypoint solo dopo selezione.
- nessun motion che copra la rotta o i controlli.

## Cosa evitare

- UI decorativa che oscura la cartografia.
- presentare routing non funzionante come confermato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-004 — Emil Design Engineering | HIGH | map control and route-state transitions |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | map touch targets and offline states |
| DSK-009 — UI UX Pro Max | HIGH | map utility and nature-tech |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (MEDIUM)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (MEDIUM):** Route notes, never GPS map overlay. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.
