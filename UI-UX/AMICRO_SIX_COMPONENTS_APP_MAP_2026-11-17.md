# Amicro — sei nuovi componenti e matrice per app (17 novembre 2026)

**Sorgente:** [Amicro](https://github.com/Subhan-code/Amicro--Micro-transitions-), commit `fa5f8ffbe39537a8db191806066b8773c47c82e9`; scoperta tramite i **sei link DevLibraries forniti dall'utente**. [Audit e limiti](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [JSON bidirezionale](./AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.json). Tutto `REFERENCE` / `PROPOSED_ONLY` — nessuna modifica ai consumer.

6 riferimenti, 19 app, 60 abbinamenti (18 HIGH e 42 MEDIUM). Quattro file sorgente letti, due componenti con nome esatto non trovati: non affermare che siano importabili.

## Per componente

| ID | Componente | Stato sorgente | Ambito | App candidate |
|---|---|---|---|---:|
| AMX-001 | [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) | SOURCE_FILE_READ | CONTEXTUAL_CONTENT_REVEAL | 9 |
| AMX-002 | [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) | SOURCE_FILE_READ | POINTER_FEEDBACK | 5 |
| AMX-003 | [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) | EXACT_SOURCE_NOT_LOCATED | UNVERIFIED_CARD_3D_FLIP | 8 |
| AMX-004 | [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) | SOURCE_FILE_READ | SCROLL_TRIGGERED_ENTRANCE | 15 |
| AMX-005 | [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) | EXACT_SOURCE_NOT_LOCATED | UNVERIFIED_SPATIAL_PAGE_TRANSITION | 8 |
| AMX-006 | [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) | SOURCE_FILE_READ | INDETERMINATE_LOADING | 15 |

## Per app

| App | Compatibilità alta | Compatibilità media |
|---|---|---|
| [Anna's Diary](../PER_APP/annas-diary.md) | AMX-004 | AMX-001, AMX-003, AMX-005, AMX-006 |
| [App Factory Dashboard](../PER_APP/app-factory-dashboard.md) | AMX-002, AMX-004, AMX-006 | AMX-001, AMX-003, AMX-005 |
| [Battery Guard](../PER_APP/battery-guard.md) | — | AMX-004, AMX-006 |
| [BeerClass AI](../PER_APP/beerclass-ai.md) | — | AMX-003, AMX-004 |
| [CamperBoss](../PER_APP/camperboss.md) | AMX-006 | AMX-004 |
| [CashMate AI](../PER_APP/cashmate-ai.md) | — | AMX-004 |
| [Cooking Anime](../PER_APP/cooking-anime.md) | AMX-001, AMX-004 | AMX-003, AMX-005, AMX-006 |
| [Deskland Android](../PER_APP/deskland-android.md) | AMX-005 | AMX-001, AMX-002, AMX-006 |
| [Easy Debloat](../PER_APP/easy-debloat.md) | — | AMX-006 |
| [Edu_01 Corpo Umano](../PER_APP/edu-01-corpo-umano.md) | AMX-003 | AMX-004 |
| [FocusSense](../PER_APP/focussense.md) | — | AMX-006 |
| [FrameLab](../PER_APP/framelab.md) | — | AMX-001, AMX-002, AMX-004, AMX-005, AMX-006 |
| [Notes-Ecosistema](../PER_APP/notes-ecosistema.md) | AMX-004, AMX-006 | AMX-001, AMX-002, AMX-003, AMX-005 |
| [Omni Cleaner](../PER_APP/omni-cleaner.md) | AMX-006 | AMX-004 |
| [Send-to-PC](../PER_APP/send-to-pc.md) | AMX-006 | — |
| [TrailPath](../PER_APP/trailpath.md) | — | AMX-004 |
| [Web Utility Factory](../PER_APP/web-utility-factory.md) | AMX-004 | AMX-001, AMX-002, AMX-006 |
| [Wonderlog](../PER_APP/wonderlog.md) | AMX-001, AMX-004 | AMX-003, AMX-005, AMX-006 |
| [World Days](../PER_APP/world-days.md) | AMX-004, AMX-006 | AMX-001, AMX-003, AMX-005 |

## Confini

- `AMX-002 Cursor Trail` è destinato a **mouse/trackpad Web/desktop**: non applicarlo indiscriminatamente al touch.
- `AMX-006 Accordion Loader` non è `DSP-003 Accordion Blind Pull`: il primo segnala attesa **indeterminata** (quattro barre), il secondo espande un pannello.
- `AMX-003 Perspective Flip` e `AMX-005 Spatial Door Portal` restano riferimenti dal titolo URL; non c'è un file sorgente confermato per quelle **denominazioni esatte** nel commit esaminato.
- Nessuna dipendenza npm/Flutter, plugin, codice, APK o Golden implementato. Rispettare Product Bible, riduzione movimento, accessibilità, gestione stati errore e performance.
