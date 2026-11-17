# Matrice bidirezionale — 10 skill di design ↔ app (17/11/2026)

> **PROPOSED_ONLY**: compatibilità ragionata, non approvazione prodotto, non integrazione e non test. Repo e commit verificati; stato delle stelle riferito dall'utente, non enumerato via API autenticata.

Fonte [audit dei dieci repository](../sources/ANTI_SLOP_DESIGN_SKILLS_AUDIT_2026-11-17.md) · [Registro JSON relazionale](./MATRICE_REPO_DESIGN_APP_2026-11-17.json). **10 fonti, 21 destinazioni, 96 associazioni (68 HIGH, 28 MEDIUM)**.

## Per repository

| ID | Repository | Ambito | HIGH | MEDIUM |
|---|---|---|---|---|
| DSK-001 | [Anti UI Slop / Uizze](https://github.com/uizze/uizze/tree/fc401e9e654cbafe427b0c98142fc8bccd0c4e7e) | DESIGN_INTELLIGENCE | Anna's Diary, Notes-Ecosistema, Wonderlog, FrameLab, World Days, App Factory Dashboard | Omni Cleaner, Cooking Anime |
| DSK-002 | [Impeccable](https://github.com/pbakaus/impeccable/tree/d41d9860b0094dcb68030657da63461212835aaa) | UI_UX_QA | Anna's Diary, Notes-Ecosistema, Omni Cleaner, World Days, Battery Guard, App Factory Dashboard, FrameLab | Wonderlog, CashMate AI, Deskland Android |
| DSK-003 | [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | WEB_DESIGN_TOOLING | App Factory Dashboard, Web Utility Factory, Cooking Anime | FrameLab, Notes-Ecosistema, Anna's Diary, World Days |
| DSK-004 | [Emil Design Engineering](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c) | MOTION_ENGINEERING | Anna's Diary, Notes-Ecosistema, Deskland Android, Omni Cleaner, Wonderlog, FrameLab, TrailPath | World Days, FocusSense |
| DSK-005 | [Vercel Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62) | WEB_UX_QA | App Factory Dashboard, Web Utility Factory, Notes-Ecosistema, Anna's Diary, World Days | Cooking Anime |
| DSK-006 | [Anthropic Frontend Design](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba) | VISUAL_ART_DIRECTION | Anna's Diary, Notes-Ecosistema, Wonderlog, FrameLab, World Days, Cooking Anime | Omni Cleaner, App Factory Dashboard |
| DSK-007 | [Hallmark](https://github.com/Nutlope/hallmark/tree/04977e15f3dfd6ee4b74c887dac3eb52665d6c92) | WEB_MARKETING_DESIGN | Cooking Anime, FrameLab | App Factory Dashboard, Anna's Diary, Notes-Ecosistema, World Days, Web Utility Factory |
| DSK-008 | [Better Interfaces (Jakub Krehel)](https://github.com/jakubkrehel/skills/tree/6c2120103600407a1a9986afd834e73144ef8998) | UI_UX_QA | Anna's Diary, Notes-Ecosistema, Omni Cleaner, World Days, Battery Guard, CashMate AI, App Factory Dashboard, TrailPath, FocusSense | CamperBoss, Wonderlog |
| DSK-009 | [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a41f7ca47b7541ad5c116495cbade3ee) | CROSS_PLATFORM_DESIGN_INTELLIGENCE | Anna's Diary, Notes-Ecosistema, World Days, Wonderlog, FrameLab, Battery Guard, Omni Cleaner, App Factory Dashboard, Deskland Android, CamperBoss, TrailPath, FocusSense, CashMate AI, Cooking Anime, Easy Debloat, Pocket Guard | SleepMax Coach, BeerClass AI, 180FlipCharge, The Luminous Infinite Circle |
| DSK-010 | [Stageshow](https://github.com/benjitaylor/skills/tree/299140fafd08df55a9c234e610c3f64af3f45531) | PRODUCT_MARKETING_VISUAL | Anna's Diary, Notes-Ecosistema, Cooking Anime, World Days, FrameLab, App Factory Dashboard, Wonderlog | Omni Cleaner, Battery Guard, Web Utility Factory |

## Per app / piattaforma

| App | Alta compatibilità | Compatibilità media |
|---|---|---|
| 180FlipCharge | — | DSK-009 |
| Anna's Diary | DSK-001, DSK-002, DSK-004, DSK-005, DSK-006, DSK-008, DSK-009, DSK-010 | DSK-003, DSK-007 |
| App Factory Dashboard | DSK-001, DSK-002, DSK-003, DSK-005, DSK-008, DSK-009, DSK-010 | DSK-006, DSK-007 |
| Battery Guard | DSK-002, DSK-008, DSK-009 | DSK-010 |
| BeerClass AI | — | DSK-009 |
| CamperBoss | DSK-009 | DSK-008 |
| CashMate AI | DSK-008, DSK-009 | DSK-002 |
| Cooking Anime | DSK-003, DSK-006, DSK-007, DSK-009, DSK-010 | DSK-001, DSK-005 |
| Deskland Android | DSK-004, DSK-009 | DSK-002 |
| Easy Debloat | DSK-009 | — |
| FocusSense | DSK-008, DSK-009 | DSK-004 |
| FrameLab | DSK-001, DSK-002, DSK-004, DSK-006, DSK-007, DSK-009, DSK-010 | DSK-003 |
| Notes-Ecosistema | DSK-001, DSK-002, DSK-004, DSK-005, DSK-006, DSK-008, DSK-009, DSK-010 | DSK-003, DSK-007 |
| Omni Cleaner | DSK-002, DSK-004, DSK-008, DSK-009 | DSK-001, DSK-006, DSK-010 |
| Pocket Guard | DSK-009 | — |
| SleepMax Coach | — | DSK-009 |
| The Luminous Infinite Circle | — | DSK-009 |
| TrailPath | DSK-004, DSK-008, DSK-009 | — |
| Web Utility Factory | DSK-003, DSK-005 | DSK-007, DSK-010 |
| Wonderlog | DSK-001, DSK-004, DSK-006, DSK-009, DSK-010 | DSK-002, DSK-008 |
| World Days | DSK-001, DSK-002, DSK-005, DSK-006, DSK-008, DSK-009, DSK-010 | DSK-003, DSK-004, DSK-007 |

## Utilizzi puntuali e motivazioni

### 180FlipCharge

- **DSK-009 (MEDIUM):** minimal control panel.

### Anna's Diary

- **DSK-001 (HIGH):** iOS Journal and pastel identity quality checks.
- **DSK-002 (HIGH):** reduce card overload while preserving diary identity.
- **DSK-003 (MEDIUM):** PWA marketing entry, not diary calendar UI.
- **DSK-004 (HIGH):** calendar gestures, Capture sheet and memory transitions.
- **DSK-005 (HIGH):** PWA accessibility and layout; native separately.
- **DSK-006 (HIGH):** coherent editorial diary personality.
- **DSK-007 (MEDIUM):** marketing site and app feature pages.
- **DSK-008 (HIGH):** readable diary and navigation review.
- **DSK-009 (HIGH):** rose editorial token system and calendar polish.
- **DSK-010 (HIGH):** feature showcase and app-store creative.

### App Factory Dashboard

- **DSK-001 (HIGH):** consistent design language and preview QA.
- **DSK-002 (HIGH):** cross-app visual acceptance gate.
- **DSK-003 (HIGH):** web landing and narrative hero.
- **DSK-005 (HIGH):** keyboard navigation, responsive dashboards and forms.
- **DSK-006 (MEDIUM):** non-generic web dashboard identity.
- **DSK-007 (MEDIUM):** public project showcase, not operations UI.
- **DSK-008 (HIGH):** responsive dashboard QA.
- **DSK-009 (HIGH):** cross-product visual catalog.
- **DSK-010 (HIGH):** portfolio project teasers.

### Battery Guard

- **DSK-002 (HIGH):** readable metrics and actionable status.
- **DSK-008 (HIGH):** information clarity and warning states.
- **DSK-009 (HIGH):** clean battery analytics theme.
- **DSK-010 (MEDIUM):** clean metrics app-store screenshots.

### BeerClass AI

- **DSK-009 (MEDIUM):** tasting cards and theme.

### CamperBoss

- **DSK-008 (MEDIUM):** offline guide accessibility.
- **DSK-009 (HIGH):** outdoor readability and maps.

### CashMate AI

- **DSK-002 (MEDIUM):** financial data visual hierarchy.
- **DSK-008 (HIGH):** money formatting, disclosure and graphs.
- **DSK-009 (HIGH):** semantic finance palettes.

### Cooking Anime

- **DSK-001 (MEDIUM):** image-first editorial cards.
- **DSK-003 (HIGH):** product/store marketing website.
- **DSK-005 (MEDIUM):** marketing and public site only.
- **DSK-006 (HIGH):** image-first culinary identity.
- **DSK-007 (HIGH):** public product marketing and themed campaign.
- **DSK-009 (HIGH):** image-first catalogue design.
- **DSK-010 (HIGH):** app store promotional cards.

### Deskland Android

- **DSK-002 (MEDIUM):** launcher accessibility and touch-state review.
- **DSK-004 (HIGH):** long-press drag, icon motion and frame pacing.
- **DSK-009 (HIGH):** launcher spatial controls, only after functional stability.

### Easy Debloat

- **DSK-009 (HIGH):** severity-safe utility tokens.

### FocusSense

- **DSK-004 (MEDIUM):** score motion without decorative loops.
- **DSK-008 (HIGH):** data viz semantics and contrast.
- **DSK-009 (HIGH):** neon analytics vs legibility balance.

### FrameLab

- **DSK-001 (HIGH):** photo and visual hierarchy.
- **DSK-002 (HIGH):** premium photo-editor controls.
- **DSK-003 (MEDIUM):** editorial product landing.
- **DSK-004 (HIGH):** photo controls and gesture responsiveness.
- **DSK-006 (HIGH):** photographic editorial premium direction.
- **DSK-007 (HIGH):** editorial product showcase.
- **DSK-009 (HIGH):** photo UI token and contrast reference.
- **DSK-010 (HIGH):** visual editor demonstrations.

### Notes-Ecosistema

- **DSK-001 (HIGH):** editor and responsive workflow refinement.
- **DSK-002 (HIGH):** editor density, hierarchy and responsive review.
- **DSK-003 (MEDIUM):** web product landing, not the native editor.
- **DSK-004 (HIGH):** canvas/drag/selection and feedback.
- **DSK-005 (HIGH):** web editor/desktop accessibility.
- **DSK-006 (HIGH):** knowledge-workspace information hierarchy.
- **DSK-007 (MEDIUM):** landing feature stories.
- **DSK-008 (HIGH):** complex editor and long-text states.
- **DSK-009 (HIGH):** editor/canvas design-token consistency.
- **DSK-010 (HIGH):** workspace feature illustrations and demo.

### Omni Cleaner

- **DSK-001 (MEDIUM):** less generic utility UI and state feedback.
- **DSK-002 (HIGH):** dedicated feature screens and gallery/video UX checks.
- **DSK-004 (HIGH):** smooth transitions between function screens.
- **DSK-006 (MEDIUM):** distinctive but restrained utility aesthetic.
- **DSK-008 (HIGH):** feature navigation, gallery and media controls.
- **DSK-009 (HIGH):** utility redesign with component variants.
- **DSK-010 (MEDIUM):** feature-page visuals using actual app flows.

### Pocket Guard

- **DSK-009 (HIGH):** protection state UI.

### SleepMax Coach

- **DSK-009 (MEDIUM):** calm routine controls.

### The Luminous Infinite Circle

- **DSK-009 (MEDIUM):** accessible visual-alert semantics.

### TrailPath

- **DSK-004 (HIGH):** map control and route-state transitions.
- **DSK-008 (HIGH):** map touch targets and offline states.
- **DSK-009 (HIGH):** map utility and nature-tech.

### Web Utility Factory

- **DSK-003 (HIGH):** SEO utility site landing and conversion flows.
- **DSK-005 (HIGH):** SEO-first accessible utility web UI.
- **DSK-007 (MEDIUM):** landing experiments; prioritize SEO and speed.
- **DSK-010 (MEDIUM):** service landing feature illustrations.

### Wonderlog

- **DSK-001 (HIGH):** travel visual language and image-led views.
- **DSK-002 (MEDIUM):** travel cards and map overlay polish.
- **DSK-004 (HIGH):** map and journal transitions.
- **DSK-006 (HIGH):** colourful travel narrative.
- **DSK-008 (MEDIUM):** image/locale overflow checks.
- **DSK-009 (HIGH):** travel journal palette and components.
- **DSK-010 (HIGH):** travel journey product highlights.

### World Days

- **DSK-001 (HIGH):** daily content cards and empty-state polish.
- **DSK-002 (HIGH):** content density, long-copy and reader flow.
- **DSK-003 (MEDIUM):** content discovery pages where web-native.
- **DSK-004 (MEDIUM):** subtle content-card transitions.
- **DSK-005 (HIGH):** content-heavy web views and navigation.
- **DSK-006 (HIGH):** recognizable day-story cards.
- **DSK-007 (MEDIUM):** public promotional pages.
- **DSK-008 (HIGH):** long story and multilingual layouts.
- **DSK-009 (HIGH):** information-card design and locale-aware typography.
- **DSK-010 (HIGH):** new rich-story feature preview.

## Confini di riuso

Per il **mobile Flutter/Compose**, solo principi e pattern trasferibili, con implementazione nativa; per le pagine **Web**, verificare strumenti e dipendenze effettive. Taste/Hallmark si applicano soprattutto al marketing web; Stageshow agli asset/promozioni, **non** a feature runtime. Prima di integrare: Product Bible, Golden e donor interni; poi licenza file/asset, test accessibilità/responsive/reduced motion, screenshot reali ed evidence AppLab. Nessuna app o Golden modificato da questa mappatura.
