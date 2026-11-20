# Motionary + altre 25 risorse — intake verificato del 20/11/2026

**Baseline Factory:** `4df94ac3b3ea22a2323634fe83c3c7770fe3b835` (CURRENT: Master v27, Golden Index v31).  
**Design-App preflight:** `32a89d433fffa60a2c4620a73555d0591dd365f1`.  
**Ambito:** classificazione nel Design-App, **senza implementazione nelle app** o installazione di servizi.

## Evidenze e decisione

- **26 collegamenti**: **15 nuovi** per questo censimento e **11 già rappresentati** come sito/skill/OSS o sotto-skill nel repository. Gli ID `STYLE26-xx` identificano *link del lotto*, **non** nuovi UID di componenti.
- **Motionary**: sito https://alanfeiyuchang.github.io/motionary-ios-animations/ e sorgente `alanfeiyuchang/motionary-ios-animations@38ca358f289a435ea0b4f0676648e831e147e9eb`. README + LICENSE originali letti. **839 animazioni, 15 categorie, 85 famiglie** dichiarate. Preview Web registrate e demo SwiftUI per iOS 18+; **non sono widget Flutter/Compose**. MIT, mantenendo notice. Il sito Web mostra registrazioni; interazione nativa/tuning nell'app iPhone.
- **Rare UI**: `swamimalode07/rare-ui@9523173c8896b0b9d5a87c8fbb8f45f97a7b068c`, README + LICENSE letti. **MIT + Commons Clause + attribuzione visibile**: ammessa adozione in prodotti secondo termini, **vietata ridistribuzione di componenti standalone, in bundle o come port**. Catalogare come REFERENCE, non importare nel nostro catalogo di componenti Flutter.
- **AI Canvas e React Bits già esistenti** (`DESIGN-SITE-039`, `DESIGN-SITE-034`). `jakubkrehel/skills`, `nextlevelbuilder/ui-ux-pro-max-skill` (`DSK-009`), `anthropics/skills`, Penpot, Excalidraw e tldraw compaiono già in fonti OSS/skill; sottocartelle Anthropic non diventano nuovi donor completi.
- **Stitch skills** (`google-labs-code/stitch-skills`) e **DESIGN.md** (`google-labs-code/design.md`) sono strumenti/contratti di documentazione/prototipazione, non componenti pronti da distribuire. `DESIGN.md` rimane una **vista derivata** dai token e dalle scelte approvate; non un secondo Product Bible.
- **Astryx** è un design system Web/React MIT; possibile reference per accessibilità, semantica e coerenza, **non** pacchetto Flutter o stile obbligatorio.
- **Remotion engine** e `remotion-dev/skills` sono sorgenti distinte: il secondo era già catalogato, il primo presenta **licenze commerciali specifiche**. Video editing, agent-browser, Figma MCP e tool DaVinci sono destinati a produzione, QA o prototipazione: non a runtime Android/iOS.

## Registro completo (26/26)

| ID | Risorsa | Stato | Classe | Vincolo principale |
|---|---|---|---|---|
| STYLE26-01 | [Motionary iOS Animations](https://alanfeiyuchang.github.io/motionary-ios-animations/) | NEW | UI_MOTION_REFERENCE | 839 effects, 15 categories, 85 families; SwiftUI iOS18+, native adaptation required |
| STYLE26-02 | [AI Canvas](https://aicanvas.me/) | EXISTING: DESIGN-SITE-039 | REACT_DESIGN_SYSTEM | Free React design systems, not a Flutter library |
| STYLE26-03 | [Jakub Krehel design skills](https://github.com/jakubkrehel/skills) | EXISTING: OSS_REGISTRY | AGENT_DESIGN_SKILLS | Animation, a11y, UI polish and writing; skill, not runtime UI |
| STYLE26-04 | [oakoss agent skills](https://github.com/oakoss/agent-skills) | NEW | AGENT_SKILLS_COLLECTION | 112 skill curation claim, not 112 installed skills |
| STYLE26-05 | [Rare UI](https://rareui.com/) | NEW | ANIMATED_REACT_COMPONENTS | React/TSX Tailwind Motion; non-shippable as Flutter component library |
| STYLE26-06 | [React Bits](https://reactbits.dev/) | EXISTING: DESIGN-SITE-034 | ANIMATED_REACT_COMPONENTS | Already audited; no new UID |
| STYLE26-07 | [DaVinci Resolve MCP](https://github.com/samuelgursky/davinci-resolve-mcp) | NEW | VIDEO_PRODUCTION_TOOL | DaVinci automation; desktop workflow, no mobile UI |
| STYLE26-08 | [auto-editor](https://github.com/WyattBlue/auto-editor) | NEW | VIDEO_EDITING_TOOL | Cutting silence and pacing, requires media QA |
| STYLE26-09 | [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | NEW | VIDEO_ANALYSIS_TOOL | Detect scene changes, not a motion design system |
| STYLE26-10 | [MoviePy](https://github.com/Zulko/moviepy) | NEW | VIDEO_EDITING_LIBRARY | Offline programmatic editing; codec deps separate |
| STYLE26-11 | [Remotion runtime](https://github.com/remotion-dev/remotion) | NEW: runtime; existing remotion-dev/skills separate | REACT_VIDEO_ENGINE | Engine licensing independent of already recorded remotion agent skills |
| STYLE26-12 | [video-use](https://github.com/browser-use/video-use) | NEW | VIDEO_AGENT_TOOL | Tool candidate for editing; never assert final quality without inspection |
| STYLE26-13 | [21st.dev Magic MCP](https://github.com/21st-dev/magic-mcp) | NEW | AI_UI_GENERATION_TOOL | Web UI generation and agent interface; not Flutter source |
| STYLE26-14 | [Figma Context MCP](https://github.com/GLips/Figma-Context-MCP) | NEW | DESIGN_CONTEXT_TOOL | Transfer Figma context to agents; permissions and file ownership remain separate |
| STYLE26-15 | [Penpot](https://github.com/penpot/penpot) | EXISTING: OSS_REGISTRY | DESIGN_TOOL | Open-source design platform previously catalogued |
| STYLE26-16 | [agent-browser](https://github.com/vercel-labs/agent-browser) | NEW | AGENT_BROWSER_QA_TOOL | Browser QA automation, requires consent for external sites |
| STYLE26-17 | [UI UX Pro Max skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | EXISTING: DSK-009 / OSS_REGISTRY | DESIGN_SKILL | Existing categorized style/palette/font system; avoid duplicate skills |
| STYLE26-18 | [Anthropic canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | EXISTING: umbrella anthropics/skills | VISUAL_CREATION_SKILL | Poster/visual asset skill; not a Flutter widget |
| STYLE26-19 | [Anthropic pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | EXISTING: same umbrella | PRESENTATION_SKILL | Slide authoring, no UI runtime |
| STYLE26-20 | [Anthropic theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | EXISTING: same umbrella | THEME_SKILL | Branding/slide themes; derivative design reference |
| STYLE26-21 | [Google Stitch skills](https://github.com/google-labs-code/stitch-skills) | NEW | AGENT_UI_GENERATION_SKILLS | Prompt-to-screen prototyping; not an implemented app UI |
| STYLE26-22 | [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | EXISTING: same umbrella | FRONTEND_DESIGN_SKILL | Web design guidance; adapt for mobile carefully |
| STYLE26-23 | [Google DESIGN.md](https://github.com/google-labs-code/design.md) | NEW | DESIGN_SYSTEM_DOCUMENTATION | Machine-readable design identity spec; derived view, not parallel Product Bible |
| STYLE26-24 | [Meta Astryx](https://github.com/meta/astryx) | NEW | REACT_DESIGN_SYSTEM | Enterprise UI components; benchmark, no Material/brand adoption |
| STYLE26-25 | [Excalidraw](https://github.com/excalidraw/excalidraw) | EXISTING: OSS_REGISTRY | CANVAS_TOOL | Already in Notes/canvas donor inventory |
| STYLE26-26 | [tldraw](https://github.com/tldraw/tldraw) | EXISTING: OSS_REGISTRY | INFINITE_CANVAS_SDK | Already in Notes/canvas donor inventory |

## Motionary: famiglie da selezionare prima di integrarle

1. **Spring e scale del press** — feedback tattile su azioni reali, senza delay percepito.
2. **Morph card → dettaglio** — utile per Ricordi e gallery; preservare foto e stato dello scroll.
3. **Navigation/segmented transitions** — orientare chiaramente la vista attiva, non rincorrere icone.
4. **Day/night e toggle** — usare preferenze persistenti reali, non cambiare tema soltanto nell'animazione.
5. **Count-up e data charts** — animare veri dati, mai risultati simulati.
6. **Progress e feedback** — progressi determinati o indeterminati veritieri con cancel/error/retry.
7. **Gesture, rubber-band e inertia** — limite fisico, annullamento e accessibilità da verificare.
8. **Background/Shader** — ultimi nella priorità per batteria, contrasto, FPS, peso APK e reduced motion.

**Fattibilità:** Flutter `AnimatedSwitcher`, `AnimationController`, `TweenAnimationBuilder`, `Hero`, `CustomPainter` o `ImplicitlyAnimatedWidget` quando appropriato; Kotlin/Compose animazioni native. Non copiare SwiftUI come Dart e non aggiungere motori Lottie/Rive/3D senza motivazione. Valutare a11y, 48 dp, riduzione movimento, interruzioni, jank e screenshot comparativi sul consumer.

## Diritti, stato e criteri di maturità

- Link pubblici/README verificati **non** equivalgono a runtime testato: tutte le proposte sono `PROPOSED_ONLY`.
- Nessun source code, screenshot, GIF, SVG, font, video o materiale premium terzo archiviato in questo lotto; **0 UID nuovi**, **0 APK** e **0 modifiche consumer**.
- Dove il campo licenza dice `LICENSE_REVIEW_REQUIRED`, la provenienza è letta ma non esiste diritto di riuso attestato in questo intake; nessun copia/incolla.
- Ogni adozione futura richiede Product Bible/tema già scelto, file implementativo e licenza per voce, dependency gate, implementazione nativa, test e PR exact-head.

**Mappa applicazioni:** [JSON](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.json) · [riepilogo](../UI-UX/MOTIONARY_26_APP_MAP_2026-11-20.md).  
**Registro machine-readable:** [MOTIONARY_26_REGISTRY_2026-11-20.json](./MOTIONARY_26_REGISTRY_2026-11-20.json).
