# Watermelon — componenti e applicabilità per app · 17/11/2026

**Origine:** [DevLibraries / Watermelon](https://devlibraries.com/libraries/watermelon) e [repository originale Watermelon UI](https://github.com/WatermelonCorp/watermelon-platform/tree/9d6defcf89880d0a00fbccad773c046bb51d7afb), MIT per repository; [audit e vincoli](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md). [Registro JSON](./WATERMELON_NINE_APP_MAP_2026-11-17.json). Lo stato è **REFERENCE / PROPOSED_ONLY**; app non modificate.

**9 riferimenti**, 17 destinazioni, **73 relazioni** (24 HIGH / 49 MEDIUM); 6 file implementativi verificati, 3 nomi esatti non trovati nella baseline.

## Per componente

| ID | Nome | Evidenza | App candidate |
|---|---|---|---:|
| WML-001 | [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) | `SOURCE_FILE_READ` | 9 |
| WML-002 | [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) | `SOURCE_FILE_READ` | 8 |
| WML-003 | [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) | `SOURCE_FILE_READ` | 9 |
| WML-004 | [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) | `SOURCE_FILE_READ` | 10 |
| WML-005 | [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) | `SOURCE_FILE_READ` | 7 |
| WML-006 | [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) | `EXACT_SOURCE_NOT_LOCATED` | 7 |
| WML-007 | [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) | `SOURCE_FILE_READ` | 7 |
| WML-008 | [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) | `EXACT_SOURCE_NOT_LOCATED` | 8 |
| WML-009 | [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) | `EXACT_SOURCE_NOT_LOCATED` | 8 |

## Per app

| App | Alta compatibilità | Compatibilità media |
|---|---|---|
| [Anna's Diary](../PER_APP/annas-diary.md) | WML-001, WML-002, WML-004, WML-007, WML-008 | WML-003, WML-005, WML-006, WML-009 |
| [App Factory Dashboard](../PER_APP/app-factory-dashboard.md) | WML-005, WML-007 | WML-006, WML-008 |
| [Battery Guard](../PER_APP/battery-guard.md) | — | WML-002, WML-004 |
| [BeerClass AI](../PER_APP/beerclass-ai.md) | — | WML-001, WML-002, WML-003 |
| [CamperBoss](../PER_APP/camperboss.md) | — | WML-001, WML-002, WML-004, WML-007, WML-008, WML-009 |
| [CashMate AI](../PER_APP/cashmate-ai.md) | WML-004, WML-005 | WML-007, WML-008 |
| [Cooking Anime](../PER_APP/cooking-anime.md) | WML-006, WML-009 | WML-001, WML-002, WML-003, WML-005, WML-007 |
| [FocusSense](../PER_APP/focussense.md) | WML-004 | WML-002, WML-003, WML-009 |
| [FrameLab](../PER_APP/framelab.md) | WML-001, WML-003, WML-004 | WML-006 |
| [Notes-Ecosistema](../PER_APP/notes-ecosistema.md) | WML-007 | WML-001, WML-003, WML-004, WML-005, WML-008 |
| [Omni Cleaner](../PER_APP/omni-cleaner.md) | WML-003, WML-004 | WML-001 |
| [SleepMax Coach](../PER_APP/sleepmax-coach.md) | WML-002, WML-008 | WML-009 |
| [Tabletop Motion Alarm](../PER_APP/tabletop-motion-alarm.md) | — | WML-009 |
| [TrailPath](../PER_APP/trailpath.md) | — | WML-003 |
| [Web Utility Factory](../PER_APP/web-utility-factory.md) | WML-006 | — |
| [Wonderlog](../PER_APP/wonderlog.md) | WML-001, WML-003, WML-004 | WML-005, WML-006, WML-007, WML-008, WML-009 |
| [World Days](../PER_APP/world-days.md) | — | WML-001, WML-002, WML-004, WML-005, WML-006, WML-008, WML-009 |

## Il caso Anna's Diary

[Proposta puntuale Home Oggi e Ricordi](../PER_APP/annas-diary.md). Priorità di design: **WML-008** promemoria in-app nella Home Oggi (non un servizio di notifica già realizzato), **WML-001** carosello Ricordi con foto originali e navigazione accessibile, **WML-002** ruler opzionale selezione giorno, **WML-007** invito allo spazio condiviso con API reali. Il countdown WML-009 è puramente opzionale e non deve dominare la Home.

Per WML-008 distinguere badge/riepilogo interno visibile alla prima apertura giornaliera, eventuale fascia oraria configurabile e notifica OS in background, che richiede permessi, pianificazione e test separati. La schermata Oggi deve restare stabile e non duplicare avvisi.
