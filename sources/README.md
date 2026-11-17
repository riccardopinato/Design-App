# Fonti di riferimento per design, animazioni e UX

Questa directory contiene studi di sorgenti esterne e donatori candidati, non necessariamente componenti già approvati per l'integrazione nelle app. La fonte autoritativa delle registrazioni resta [`registry/OSS_DESIGN_SOURCES.yaml`](../registry/OSS_DESIGN_SOURCES.yaml).

## Nuove stelle GitHub — canvas, workflow, editor e widget · 16 novembre 2026

- [7 nuove fonti visive con commit, licenza e crosswalk app](./STARS_750_VISUAL_INTAKE_2026-11-16.md): tldraw, Excalidraw, xyflow, Markmap, OpenWidget, AppFlowy Editor, Nodus. Maturità REFERENCE; non COPIA PRONTA. Indice canonico: `registry/OSS_DESIGN_SOURCES.yaml`.

## Dock e widget Windows · 16 novembre 2026

- [OpenTaskbar MIT e lumabar proprietario: crosswalk visuale e di riuso](./GITHUB_DOCK_WIDGET_REFERENCE_2026-11-16.md). Registrati in `registry/OSS_DESIGN_SOURCES.yaml` come REFERENCE, non COPY_READY.

## Ruixen UI · 13 novembre 2026

- **[Audit completo e mappa app → pattern](./RUIXEN_UI_DESIGN_MOTION_AUDIT_2026-11-13.md):** fonte, licenze, analisi di motion e 41 pattern per 18 app, con 5 maxi-step operativi.
- **[Catalogo ragionato JSON](./RUIXEN_UI_CURATED_APP_MAP_2026-11-13.json):** ID `RUX-001` ecc., priorità, app candidate, rischio, collegamenti ai file React immutabili.
- **[Inventario tecnico JSON](./RUIXEN_UI_REGISTRY_INVENTORY_2026-11-13.json):** 277 file TypeScript/TSX con percorsi, SHA Git e classi euristiche.
- [Sito ufficiale](https://ruixen.com/) · [Docs](https://ruixen.com/docs) · [GitHub sorgente MIT](https://github.com/ruixenui/ruixen.com) · [Licenza Pro separata](https://pro.ruixen.com/license).

**Da non confondere:** codice TSX disponibile ≠ componente compilato e validato in Flutter. Nessuna nuova capability, UIR o Golden viene assegnata da questo intake.

## Ricerche precedenti

- [GitHub UI/UX — 27 ottobre 2026](./GITHUB_DESIGN_RESEARCH_2026-10-27.md)
- [GitHub UI/UX — 30 ottobre 2026](./GITHUB_DESIGN_RESEARCH_2026-10-30.md)
- [Harvest dei pattern App Factory](./PROJECT_PATTERN_HARVEST.md)

## DevLibraries e beUI Voice Orb — 17/11/2026

- [DevLibraries — portale di design e discovery](./DEVLIBRARIES_DISCOVERY_2026-11-17.md), [registro dei siti con ruolo/licenza](./DESIGN_RESEARCH_SITES.json): cercare componenti, librerie e skill e poi verificare i sorgenti originali.
- [beUI Voice Orb — audit con commit sorgente e licenze MIT](./BEUI_VOICE_ORB_AUDIT_2026-11-17.md): sfera reattiva al livello audio; non è un recorder o STT; WebGL/React e Skia/React Native, non Flutter pronto.
- [Matrice Voice Orb → 10 app candidate](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md) e [dossier PER_APP](../PER_APP/README.md). Stati REFERENCE/PROPOSED_ONLY, nessuna modifica consumer.

## EaseUI e Amicro — temi, transizioni, tendine e caricamenti · 17/11/2026

- [Audit dei cinque pattern nominati e uno screenshot di caricamenti](./EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md): sorgenti MIT con commit; uno script EaseUI verificato, quattro implementazioni Amicro successivamente individuate nei sorgenti originali, una proposta visuale non vendorizzata.
- [Matrice pattern ↔ 19 app](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md), [registro bidirezionale JSON](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.json), [dossier singole app](../PER_APP/README.md).
- [Directory fonti](./DESIGN_RESEARCH_SITES.json) ampliata con EaseUI/Amicro; licenze dei singoli asset da verificare prima del riuso.

## Amicro — sei componenti, verifica sorgenti ampliata

[Audit del nuovo gruppo](./AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [matrice per 19 app](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md). Quattro nuovi effetti (CurtainReveal, Cursor Trail, Scroll Reveal, Accordion Loader) hanno file sorgente individuati; per Perspective Flip e Spatial Door Portal i **nomi esatti non sono verificati** nel codice originale. Il [precedente audit](./EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) è stato aggiornato: quattro effetti prima classificati soltanto come descrizioni hanno invece file implementativi nominati. Provenienza letta, nessun runtime Flutter né Copy-Ready convalidato.

## Watermelon UI — nove componenti con focus Anna's Diary

[Audit tecnico e diritti](./WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [matrice per app](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md) · [repository sorgente](https://github.com/WatermelonCorp/watermelon-platform). Sei componenti dispongono di codice React verificato; Text Gradient, Notification List e Flip Clock non hanno un file esatto nel commit consultato. Per l'idea del riepilogo Home Oggi conservare il requisito utente, ma **non trattare una UI di notifica come un servizio di scheduling o come una notifica OS**.
