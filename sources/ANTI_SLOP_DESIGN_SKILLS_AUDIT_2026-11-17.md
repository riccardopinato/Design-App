# Anti UI slop / design skills — Audit di 10 repository (17 novembre 2026)

**Ambito:** fonti esterne da valutare e catalogare in Design-App, NON installazione né integrazione automatica nelle app. Baseline App Factory `c5adc147046beb7024629466d10eeb799c3c2619` (Master v27; Golden Index v29). Materiale verificato: repository GitHub, HEAD immutabili, README, skill entrypoint e licenze principali; non è stato eseguito un audit del codice di tutte le sottodirectory, né build o test delle skill. Nuovi asset importati: **0**.

## Sintesi operativa

- **Mobile Flutter/Android:** prima UI UX Pro Max (`DSK-009`), Impeccable (`DSK-002`), Better Interfaces (`DSK-008`), Emil (`DSK-004`); Uizze (`DSK-001`) e Anthropic (`DSK-006`) come direzione estetica.
- **Web/PWA/SEO:** Vercel (`DSK-005`) per qualità e accessibilità; Taste (`DSK-003`) e Hallmark (`DSK-007`) per presentazione pubblica; mai trasporre JavaScript e CSS nelle app native.
- **Marketing/App Store:** Stageshow (`DSK-010`) per scene dimostrative dichiaratamente illustrative. Se si mostra una funzione come reale, il contenuto deve corrispondere a una funzione realmente implementata.
- **Riuso:** app ⇄ fonti [matrice leggibile](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md) / [JSON bidirezionale](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json). Le classi HIGH/MEDIUM sono proposte, non prove di integrazione.

## Provenienza e valutazione per fonte

### DSK-001 — Anti UI Slop / Uizze

- **Repo/commit:** [uizze/uizze @ fc401e9e654c](https://github.com/uizze/uizze/tree/fc401e9e654cbafe427b0c98142fc8bccd0c4e7e)
- **File esaminato:** [`skills/anti-ui-slop/SKILL.md`](https://github.com/uizze/uizze/blob/fc401e9e654cbafe427b0c98142fc8bccd0c4e7e/skills/anti-ui-slop/SKILL.md); README del repository.
- **Licenza rilevata:** MIXED: root MIT; anti-ui-slop Apache-2.0; service/assets separately licensed. Evidenza: `LICENSING.md`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `DESIGN_INTELLIGENCE` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Design contract, product-specific references, required UI states and finish gate; image-to-UI and UI Radar as separate optional workflows.
- **Limite:** Primarily web/iOS instructions, not a native Flutter package. Hosted MCP is paid and reference images are not automatically redistributable.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** NEO-APPLE, PASTEL UI, DESIGN SYSTEM.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Wonderlog (HIGH), FrameLab (HIGH), World Days (HIGH), App Factory Dashboard (HIGH), Omni Cleaner (MEDIUM), Cooking Anime (MEDIUM).

### DSK-002 — Impeccable

- **Repo/commit:** [pbakaus/impeccable @ d41d9860b009](https://github.com/pbakaus/impeccable/tree/d41d9860b0094dcb68030657da63461212835aaa)
- **File esaminato:** [`.agents/skills/impeccable/SKILL.md`](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/.agents/skills/impeccable/SKILL.md); README del repository.
- **Licenza rilevata:** Apache-2.0 (root); per-file/engine assets still require checking. Evidenza: `LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `UI_UX_QA` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Structured critique/audit, layout, typography, visual polish, accessibility, responsive and resilient UI states; deterministic anti-slop detector.
- **Limite:** UX rules transfer conceptually to native apps; its own engine and browser instrumentation do not run as Flutter widgets.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** DESIGN SYSTEM, MINIMAL CONTROLS, EDITORIAL UI.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Omni Cleaner (HIGH), World Days (HIGH), Battery Guard (HIGH), App Factory Dashboard (HIGH), FrameLab (HIGH), Wonderlog (MEDIUM), CashMate AI (MEDIUM), Deskland Android (MEDIUM).

### DSK-003 — Taste Skill

- **Repo/commit:** [Leonxlnx/taste-skill @ f6b76575f949](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8)
- **File esaminato:** [`skills/taste-skill/SKILL.md`](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md); README del repository.
- **Licenza rilevata:** MIT (root); photo/icon asset-level licenses and credits must be checked. Evidenza: `LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `WEB_DESIGN_TOOLING` / B; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Web art direction, palette/font selection, hero layouts, copy checks and real-browser consistency/performance gate at multiple viewport widths.
- **Limite:** Web-first HTML/CSS/React/Vue/Svelte/Astro workflow; not suitable as a runtime Flutter donor. Preserve existing approved app brand.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** EDITORIAL UI, BENTO UI, DESIGN SYSTEM.
- **App candidate:** App Factory Dashboard (HIGH), Web Utility Factory (HIGH), Cooking Anime (HIGH), FrameLab (MEDIUM), Notes-Ecosistema (MEDIUM), Anna's Diary (MEDIUM), World Days (MEDIUM).

### DSK-004 — Emil Design Engineering

- **Repo/commit:** [emilkowalski/skills @ 64eb3deb9a5f](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c)
- **File esaminato:** [`skills/emil-design-eng/SKILL.md`](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/emil-design-eng/SKILL.md); README del repository.
- **Licenza rilevata:** MIT (root). Evidenza: `LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `MOTION_ENGINEERING` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Interaction motion, gesture physics, meaningful easing/duration, animation performance and break-ui stress checks; includes native-adjacent guidance.
- **Limite:** Examples skew web/React/Expo; implement with Flutter Animation/Compose native primitives and respect reduced-motion/performance.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** MINIMAL CONTROLS, NEO-APPLE, NAVIGATION UI.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Deskland Android (HIGH), Omni Cleaner (HIGH), Wonderlog (HIGH), FrameLab (HIGH), TrailPath (HIGH), World Days (MEDIUM), FocusSense (MEDIUM).

### DSK-005 — Vercel Web Design Guidelines

- **Repo/commit:** [vercel-labs/agent-skills @ 1a2c79d4e6c4](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62)
- **File esaminato:** [`skills/web-design-guidelines/SKILL.md`](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/web-design-guidelines/SKILL.md); README del repository.
- **Licenza rilevata:** NOASSERTION at repository root; inspect each file and upstream live guidelines. Evidenza: `NOT_PRESENT_AT_ROOT`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `WEB_UX_QA` / A_WEB; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Web accessibility, keyboard/focus, form validation, responsive typography, image performance, URL-driven state and localization; skills fetch external guideline version.
- **Limite:** Rule source is fetched live from vercel-labs/web-interface-guidelines, not pinned by this skill; do not treat web DOM rules as Android APIs.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** DESIGN SYSTEM, NAVIGATION UI, MINIMAL CONTROLS.
- **App candidate:** App Factory Dashboard (HIGH), Web Utility Factory (HIGH), Notes-Ecosistema (HIGH), Anna's Diary (HIGH), World Days (HIGH), Cooking Anime (MEDIUM).

### DSK-006 — Anthropic Frontend Design

- **Repo/commit:** [anthropics/skills @ e4bb5d960d87](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba)
- **File esaminato:** [`skills/frontend-design/SKILL.md`](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md); README del repository.
- **Licenza rilevata:** Apache-2.0 for skills/frontend-design (per-skill); other skill assets separate. Evidenza: `skills/frontend-design/LICENSE.txt`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `VISUAL_ART_DIRECTION` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Distinctive subject-grounded visual direction, typography, palette, layout narrative and self-critique; avoid templated frontend patterns.
- **Limite:** Creative frontend design guidance, not a finished mobile component; native UI must preserve Product Bible and platform behavior.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** EDITORIAL UI, PASTEL UI, BENTO UI.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Wonderlog (HIGH), FrameLab (HIGH), World Days (HIGH), Cooking Anime (HIGH), Omni Cleaner (MEDIUM), App Factory Dashboard (MEDIUM).

### DSK-007 — Hallmark

- **Repo/commit:** [Nutlope/hallmark @ 04977e15f3df](https://github.com/Nutlope/hallmark/tree/04977e15f3dfd6ee4b74c887dac3eb52665d6c92)
- **File esaminato:** [`skills/hallmark/SKILL.md`](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/skills/hallmark/SKILL.md); README del repository.
- **Licenza rilevata:** MIT root and skills/hallmark/LICENSE; photo/theme assets require per-file checks. Evidenza: `skills/hallmark/LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `WEB_MARKETING_DESIGN` / B; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** 50 web themes, functional marketing page composition, redesign and render audit, real photographed assets with credits, custom page direction.
- **Limite:** Do not replace in-app native layouts with its website themes or reuse third-party brand/photos without license review.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** BENTO UI, EDITORIAL UI, SPATIAL 3D.
- **App candidate:** Cooking Anime (HIGH), FrameLab (HIGH), App Factory Dashboard (MEDIUM), Anna's Diary (MEDIUM), Notes-Ecosistema (MEDIUM), World Days (MEDIUM), Web Utility Factory (MEDIUM).

### DSK-008 — Better Interfaces (Jakub Krehel)

- **Repo/commit:** [jakubkrehel/skills @ 6c2120103600](https://github.com/jakubkrehel/skills/tree/6c2120103600407a1a9986afd834e73144ef8998)
- **File esaminato:** [`skills/better-interface/SKILL.md`](https://github.com/jakubkrehel/skills/blob/6c2120103600407a1a9986afd834e73144ef8998/skills/better-interface/SKILL.md); README del repository.
- **Licenza rilevata:** MIT (root). Evidenza: `LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `UI_UX_QA` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Evidence-based design review across accessibility, copy, spacing, typography, color, interactive states; separate change-scoped interface review and stress scenarios.
- **Limite:** Web-specific ARIA/focus rules are references only for native mobile semantics; do not claim a review without exact source and rendered evidence.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** DESIGN SYSTEM, MINIMAL CONTROLS, NAVIGATION UI.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Omni Cleaner (HIGH), World Days (HIGH), Battery Guard (HIGH), CashMate AI (HIGH), App Factory Dashboard (HIGH), TrailPath (HIGH), FocusSense (HIGH), CamperBoss (MEDIUM), Wonderlog (MEDIUM).

### DSK-009 — UI UX Pro Max

- **Repo/commit:** [nextlevelbuilder/ui-ux-pro-max-skill @ e59ff376a41f](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a41f7ca47b7541ad5c116495cbade3ee)
- **File esaminato:** [`.claude/skills/ui-ux-pro-max/SKILL.md`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/.claude/skills/ui-ux-pro-max/SKILL.md); README del repository.
- **Licenza rilevata:** MIT (root); premium assets/features excluded; font/icon assets separately. Evidenza: `LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `CROSS_PLATFORM_DESIGN_INTELLIGENCE` / A; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Searchable local palettes, font pairings, style taxonomy, UX rules, design system token output; explicit Flutter and Jetpack Compose stack guidance.
- **Limite:** Generated suggestions are options, not certified standards. Compare to existing design tokens/approved identity; benchmark Flutter impact before use.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** DESIGN SYSTEM, NEO-APPLE, BENTO UI, PASTEL UI, NATURE-TECH, MINIMAL CONTROLS.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), World Days (HIGH), Wonderlog (HIGH), FrameLab (HIGH), Battery Guard (HIGH), Omni Cleaner (HIGH), App Factory Dashboard (HIGH), Deskland Android (HIGH), CamperBoss (HIGH), TrailPath (HIGH), FocusSense (HIGH), CashMate AI (HIGH), Cooking Anime (HIGH), Easy Debloat (HIGH), Pocket Guard (HIGH), SleepMax Coach (MEDIUM), BeerClass AI (MEDIUM), 180FlipCharge (MEDIUM), The Luminous Infinite Circle (MEDIUM).

### DSK-010 — Stageshow

- **Repo/commit:** [benjitaylor/skills @ 299140fafd08](https://github.com/benjitaylor/skills/tree/299140fafd08df55a9c234e610c3f64af3f45531)
- **File esaminato:** [`stageshow/SKILL.md`](https://github.com/benjitaylor/skills/blob/299140fafd08df55a9c234e610c3f64af3f45531/stageshow/SKILL.md); README del repository.
- **Licenza rilevata:** MIT for stageshow/ (not blanket repo); bundled third-party brand assets carry separate notices. Evidenza: `stageshow/LICENSE`; richiede sempre gate dei file/asset inclusi.
- **Categoria / priorità:** `PRODUCT_MARKETING_VISUAL` / A_MARKETING; **maturità REFERENCE**, modalità `REFERENCE_ONLY_PENDING_CONSUMER_GATE`.
- **Valore rilevato:** Believable product UI stills, bento feature cards, framed screenshots, animated cursor walkthroughs and recorded product demos.
- **Limite:** Marketing mockups do not prove app features or runtime QA. Avoid fabricated product claims and unlicensed third-party marks.
- **Famiglie di stile già esistenti collegate (tag, NON nuovi stili):** BENTO UI, SPATIAL 3D, EDITORIAL UI.
- **App candidate:** Anna's Diary (HIGH), Notes-Ecosistema (HIGH), Cooking Anime (HIGH), World Days (HIGH), FrameLab (HIGH), App Factory Dashboard (HIGH), Wonderlog (HIGH), Omni Cleaner (MEDIUM), Battery Guard (MEDIUM), Web Utility Factory (MEDIUM).

## Sovrapposizioni / deduplicazione

| Esigenza | Fonte principale | Complementari | Riuso interno prima dell'OSS |
|---|---|---|---|
| Qualità UI/anti-slop | DSK-002 | DSK-001, DSK-008 | Design-App Visual QA Kit; Golden App Shell (draft) |
| Sistema visivo cross-platform | DSK-009 | DSK-006, DSK-001 | DS-001 token-first; DS-002 Material 3 infrastruttura; Golden Theme M3 |
| Motion e gestures | DSK-004 | DSK-008 | Motion Flutter Pack v0.1.0; DS-005 |
| Web audit/accessibilità | DSK-005 | DSK-002, DSK-008 | Design-App Visual QA + test reali Web |
| Web art direction | DSK-003 | DSK-007, DSK-006 | Identità approvata app/landing, no sostituzione implicita |
| Illustrazione marketing | DSK-010 | DSK-007 | Screenshot e funzionalità reali del prodotto |

## Gate di ammissione e sicurezza

1. **REFERENCE, non COPY_READY:** nessun pacchetto Flutter, test fisico o integrazione di app è stato prodotto da questo audit. Le descrizioni dei creator non dimostrano automaticamente qualità o prestazioni.
2. **Licenza:** DSK-001 ha materiali MIT + Apache-2.0 con NOTICE; DSK-005 non espone una LICENSE root nel commit fissato e rimane NOASSERTION; DSK-006 è Apache-2.0 per la specifica skill; DSK-010 è MIT per stageshow ma gli asset brand separati hanno condizioni proprie. Per gli altri verificare comunque librerie, foto, font, immagini, CLI e dipendenze prima di copiare.
3. **Stack e privacy:** niente installazioni npm/skill o MCP pagati automatici, niente token o chiamate esterne, niente modifica codice app. Il catalogo non trasforma snippet React in widget Flutter.
4. **Product Bible:** Anna conserva editorial Lora/Manrope e palette rosa approvate; World Days conserva i colori approvati; Notes e Omni Cleaner conservano i flussi funzionali; Deskland stabilizza il launcher prima di motion avanzato.
5. **Validazione di un futuro consumer:** requisito/schermata espliciti, confronto con pattern/Golden interni, implementazione minima su ramo dedicato, test e screenshot responsive, a11y, localizzazione, performance, evidence AppLab e conferma d'identità dell'artefatto dove rilevante.
6. **Stelle:** i 10 link sono stati forniti dall'utente, che riferisce di averli aggiunti tramite token. Il connettore corrente non ha enumerato lo stato star per repo: registrare `USER_REPORTED`, non `GITHUB_STAR_VERIFIED`.

## Esito

**10 repository source-pinned, 10 schede di provenienza, 96 abbinamenti proposti e un registro relazionale bidirezionale.** 0 codice/asset terzi copiati, 0 consumer modificati, 0 test runtime esterni dichiarati, 0 promozioni Golden. Il prossimo passo eventuale è scegliere un consumer e una sola schermata prima di un proof-of-concept.
