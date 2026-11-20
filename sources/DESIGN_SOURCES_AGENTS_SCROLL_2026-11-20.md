# Design source intake — 7 nuovi, 2 sottopagine, 1 link irrisolto (20/11/2026)

**Fonte:** elenco utente di 4 design sites, 5 agent UI libraries e un t.co senza nome. **Baseline Factory:** `4df94ac3b3ea22a2323634fe83c3c7770fe3b835` Master 27, Golden Index 31, Registry 2. Design-App base `27b5e95da7f58ceccb5b898db2a6fad73a6fed01`.

| ID | Fonte | Classificazione | Licenza e limiti |
|---|---|---|---|
| DESIGN-SITE-035 | [Scrolltide](https://www.scrolltide.co/) | REFERENCE · WEB_CINEMATIC_PROMPTS | PROPRIETARY; PAID_PERSONAL_CLIENT_USE; NO_TEMPLATE_PROMPT_REDISTRIBUTION |
| DESIGN-SITE-036 | [Scroll Shaders](https://scrollshaders.com/) | REFERENCE · WEBGL2_SHADER_MOTION | PROPRIETARY_COMMERCIAL_USE_IN_FINISHED_PROJECT; NO_SHADER_PACK_REDISTRIBUTION |
| DESIGN-SITE-037 | [Snapblocks](https://snapblocks.site/) | DISCOVERY · UI_BLOCKS_TO_VERIFY | UNVERIFIED_DO_NOT_COPY; SNAPBLOCKS_GITHUB_REPO_NOT_PROVEN_CONNECTED |
| DESIGN-SITE-038 | [Navbar Gallery](https://www.navbar.gallery/) | REFERENCE · WEB_NAVIGATION_REFERENCES | THIRD_PARTY_DESIGN_SCREENSHOTS; NO_AUTOMATIC_REPUBLICATION |
| DESIGN-SITE-039 | [AI Canvas](https://aicanvas.me/components) | REFERENCE · REACT_COMPONENT_MCP_REGISTRY | MIT_FOR_FREE_CODE; SPECIFIC_LINE_ICONS_PREMIUM_LICENSE_AND_CREDIT; PREMIUM_SEPARATE |
| DESIGN-SITE-040 | [Aceternity UI](https://ui.aceternity.com/components) | REFERENCE · REACT_NEXTJS_MOTION_UI | FREE_COMPONENT_RIGHTS_PER_ITEM; PREMIUM_BLOCKS_TEMPLATES_SEPARATE_LICENSE |
| DESIGN-SITE-041 | [Chakra UI](https://chakra-ui.com/docs/components/concepts/overview) | REFERENCE · ACCESSIBLE_REACT_FRAMEWORK | MIT_REPOSITORY; DEPENDENCIES_LICENSE_PER_ITEM |

## Risultati della verifica diretta

### Scrolltide
Prompt e template per siti Web dinamici. FAQ, Terms e prezzi confermano asset/prompt/source su piani a pagamento; versione mensile con limite 10 nuovi premium/settimana e collezione 3D riservata a Yearly/Lifetime. La licenza permette siti propri e clienti, vieta rivendere/redistribuire template/prompt e riutilizzare filmati/screenshots del portale in marketing. Fonti: https://www.scrolltide.co/terms · https://www.scrolltide.co/pricing.

### Scroll Shaders
Shader WebGL2 seamless (React TSX e HTML/JS), export MP4, still ad alta risoluzione. Solo demo e preview gratuite: piani osservati **$29/month, $129/year, $239 lifetime**. Royalty-free nell'app/sito finale, non asset packs/rivendita. Supportano pause offscreen, pixel density limit, reduced-motion still, ma richiedono controlli GPU/FPS/consumo su hardware reale. Fonti: https://scrollshaders.com/pricing · https://scrollshaders.com/license.

### Snapblocks
**Non verificato dalla fonte primaria:** sito non letto direttamente. Una directory terza lo descrive come libreria di blocchi o componenti scroll-driven con copia codice e piano gratuito. Non attribuire automaticamente il repository GitHub `snapblocks/snap-components` al dominio senza prova: potrebbe essere un progetto indipendente. Stato **DISCOVERY_ONLY**, licenza UNKNOWN, non importare source. Fonte secondaria: https://design.agentik-os.com/tools/snapblocks.site.

### Navbar Gallery
Galleria pubblica di nav Web: sticky, dropdown, mega menu, sidebar, search, announcement, full screen e breadcrumb. Esempi di siti reali sono reference, non riutilizzo libero di screenshot/loghi. Web design, non navigazione Flutter pronta. Fonte: https://www.navbar.gallery/.

### AI Canvas
Registry React / shadcn, componenti free con MIT in `aicanvas-me/aicanvas@2c6d537db053a0f82911394e92c85d81554a36b9`, account gratuito per leggere sorgenti/MCP; Premium distinto. ATTENZIONE: le **Line icons hanno licenza AI Canvas Premium con requisito di credito**, non MIT indiscriminato. Componenti free di interesse: Delete Button con conto alla rovescia + undo, Upload Progress, Expanding Tabs, Signature Pad, Card Stack, New Project Modal; per agenti alcune schermate sono Premium. Il pattern undo richiede una vera funzione recupero file/dati. Fonti: https://aicanvas.me/components · https://aicanvas.me/docs · https://aicanvas.me/pricing.

### Aceternity UI
React/Next.js + Tailwind/Motion; raccolta free con navbar, card, Bento Grid, Carousel, Empty States e motion, blocchi/template premium su licenza distinta e assets di terzi da verificare per item. Mobile: hover-only non trasferibile. Fonti: https://ui.aceternity.com/components · https://ui.aceternity.com/licence.

### Chakra UI
Framework React con primitive accessibili e styling semantico; `chakra-ui/chakra-ui@4fca0889be532fced536b77e1dff982001ebc672`, licenza MIT verificata. Tecnologie Web/React, NON Dart/Flutter. Da valutare solo per specifico consumer Web e mai come cambio implicito di framework/branding. Fonti: https://chakra-ui.com/docs/components/concepts/overview · https://github.com/chakra-ui/chakra-ui.

## Due sottopagine utili di provider gia' presenti (non nuovi siti)

**ReUI Agents (DESIGN-SUBL-001)**, `DESIGN-SITE-031`: https://reui.io/blocks/solutions/agents. 10 **Pro blocks**, NON compresi nei 1.265 esempi free: operations dashboard, run queue, trace run, agent tool access matrix, action approval inbox, playbook wizard, failed-run triage, evaluation report, memory manager, run configuration. Valore primario per App Factory Agent e Dashboard, ma non una implementazione verificata ne' un'autorizzazione a eseguire tool.

**shadcn/ui AI Elements (DESIGN-SUBL-002)**, `shadcn-ui/ui` gia' nel registro OSS: https://ui.shadcn.com/docs/ai-elements. Dall'ottobre 2026 include Trace, Code Block e modelli di chat/message/tool/reasoning; utile per agenti React/Next e ref per versioni native. **Non duplicare provider OSS**, conservare URL come deep link.

Metadata e URL delle due sotto-risorse: [registro specializzato](../sources/DESIGN_EXISTING_SITES_DEEP_LINKS_2026-11-20.json).

## Link t.co non identificato

`https://t.co/rJcbTbEz28`: risoluzione con browser e richiesta HTTP fallita (cache miss / DNS). `UNRESOLVED_SHORT_URL`, nessuna destinazione inventata, non aggiunto al catalogo siti. Serve URL esteso per una futura valutazione.

## Idee per app e controlli

[Matrice markdown](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [JSON](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.json). **37 idee PROPOSED_ONLY su 11 app**; i consumer, Product Bible, Factory Golden, donor non sono stati modificati. Nessuna credenziale, abbonamento, componente Pro, SVG di terzi, shader o screenshot copiati. Flutter/Compose richiedono implementazioni native originali con accessibilita', riduzione moto, stati reali e collaudo su device. Evitare shader permanenti in battery-monitor e launcher. Per agenti: consent/approvazioni reali, audit, limite privilegi e trace non si simulano con UI decorativa.
