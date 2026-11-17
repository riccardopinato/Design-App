# EaseUI, Amicro e riferimenti caricamento — matrice app × pattern

**Registrazione**: 17/11/2026 · Stato `REFERENCE`, per-app `PROPOSED_ONLY`. La fonte utente relativa ai loader è uno screenshot di chat, non un file vettoriale originale verificato. [Audit e licenze](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [JSON bidirezionale](./EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.json).

## Pattern

| ID | Pattern | Destinazione | Evidenza | App collegate |
|---|---|---|---|---|
| DSP-001 | [EaseUI Theme Toggle](https://devlibraries.com/libraries/easeui) | Transizione a reveal circolare/ripple fra tema chiaro e scuro; non sostituisce ThemeMode o Golden Theme M3 | SOURCE_FILE_READ | 18 |
| DSP-002 | [Card Stack Peel](https://devlibraries.com/libraries/amicro/card-stack-peel) | Carta sovrapposta che si solleva/ripiega per mostrare la successiva; NON navigazione universale | DESCRIPTIVE_CATALOG_ONLY | 9 |
| DSP-003 | [Accordion Blind Pull](https://devlibraries.com/libraries/amicro) | Tendina a lamelle che si espande verticalmente (utente ha corretto la prima associazione) | DESCRIPTIVE_CATALOG_ONLY | 13 |
| DSP-004 | [Interlocking Gear Step](https://devlibraries.com/libraries/amicro) | Ingranaggi controrotanti come segnale di elaborazione reale | DESCRIPTIVE_CATALOG_ONLY | 9 |
| DSP-005 | [Shutter Step Slices](https://devlibraries.com/libraries/amicro) | Comparsa progressiva a sottili bande orizzontali; non è l'accordion stesso | DESCRIPTIVE_CATALOG_ONLY | 10 |
| DSP-006 | Loading & Waiting Visual References (user screenshot) | Ulteriori animazioni mostrate nello screenshot dell'utente, da classificare per attese brevi/lunghe e progressi effettivi; identità/nome degli asset non verificati | USER_IMAGE_NOT_ARCHIVED_AS_BINARY | 17 |

## Per app

| App | Alta compatibilità | Compatibilità media |
|---|---|---|
| Anna's Diary | DSP-001, DSP-002, DSP-003 | DSP-005, DSP-006 |
| App Factory Dashboard | DSP-001, DSP-003, DSP-004, DSP-006 | DSP-002, DSP-005 |
| Battery Guard | DSP-001 | DSP-003, DSP-004, DSP-006 |
| BeerClass AI | — | DSP-001, DSP-002, DSP-003 |
| CamperBoss | DSP-003 | DSP-001, DSP-005, DSP-006 |
| CashMate AI | DSP-001 | DSP-003, DSP-006 |
| Cooking Anime | DSP-001, DSP-002, DSP-003, DSP-005 | DSP-006 |
| Deskland Android | — | DSP-001, DSP-005, DSP-006 |
| Easy Debloat | — | DSP-001, DSP-003, DSP-004, DSP-006 |
| FocusSense | — | DSP-001, DSP-004, DSP-006 |
| FrameLab | DSP-001, DSP-002, DSP-006 | DSP-004, DSP-005 |
| Notes-Ecosistema | DSP-001, DSP-002, DSP-003, DSP-006 | DSP-004, DSP-005 |
| Omni Cleaner | DSP-001, DSP-003, DSP-004, DSP-006 | DSP-002, DSP-005 |
| Send-to-PC | DSP-004, DSP-006 | — |
| SleepMax Coach | DSP-001 | — |
| TrailPath | — | DSP-001, DSP-003, DSP-006 |
| Web Utility Factory | DSP-001, DSP-006 | — |
| Wonderlog | DSP-001, DSP-002, DSP-003 | DSP-005, DSP-006 |
| World Days | DSP-001, DSP-003, DSP-006 | DSP-002, DSP-004, DSP-005 |

## Distinzioni essenziali

- `DSP-001` migliora l'animazione del *theme toggle* e **non sostituisce** ThemeMode Light/Dark/System o il Golden Theme M3.
- `DSP-002` gestisce **stack di card**, non ogni route.
- `DSP-003` è il **movimento a tendina espandibile**; `DSP-005` è la **comparsa a lamelle di contenuti**.
- `DSP-004` anima una elaborazione realmente attiva; `DSP-006` raccoglie altri spunti per attese, da classificare e verificare prima della scelta.
- Nessun nuovo pacchetto o codice runtime importato; 4 voci Amicro sono **descrizioni**, non file implementativi verificati. Screenshot dell'utente registrato **come nota di provenienza**, non immagine binaria persistita nel repo.
