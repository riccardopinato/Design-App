# Web Utility Factory — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Landing e strumenti web SEO-first con UX sobria, interazioni leggere, accessibilità e tempi di caricamento prioritari.

**Temi candidati:** strumenti; browser; SEO/ricerca; conferma.

## Superfici e placement proposti

1. lista tool e ricerca.
2. stati vuoti/input/form.
3. download risultato soltanto se pronto.

## Icone Gentleface collegate (molti-a-molti)

Nessuna icona Gentleface associata direttamente: non assumere che un asset sia disponibile.

**Nuove icone da cercare/disegnare:** search, check, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- hover e feedback tastiera/mouse con prefers-reduced-motion.
- nessun loop decorativo sopra la form principale.

## Cosa evitare

- JS/icon-pack pesanti per aggiungere una semplice decorazione.
- sovraccarico bento che riduce conversione e SEO.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-003 — Taste Skill | HIGH | SEO utility site landing and conversion flows |
| DSK-005 — Vercel Web Design Guidelines | HIGH | SEO-first accessible utility web UI |
| DSK-007 — Hallmark | MEDIUM | landing experiments; prioritize SEO and speed |
| DSK-010 — Stageshow | MEDIUM | service landing feature illustrations |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.
