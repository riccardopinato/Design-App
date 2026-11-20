# Florent Ademaj — 5 link per design stack (20/11/2026)

**Origine:** [post X](https://x.com/MaybeFlorent/status/2123518669657710910). **Factory baseline** `4df94ac3b3ea22a2323634fe83c3c7770fe3b835`; **Design-App HEAD preflight** `1e9a51b873971b96152cfb222c68d042ae0797c0`. Fonti esterne verificate tramite pagine ufficiali ove disponibili; Shipframe non caricabile direttamente dal crawler.

## Deduplica e classification
5 URL, 4 provider unici, 2 provider **nuovi** (Shipframe e Oversight Supply), 2 **già censiti** (Mobbin `DESIGN-SITE-033`, Fontshare `DESIGN-SITE-022`).
Oversight ha **due sotto-pagine** dello stesso provider, non due siti autonomi: `DESIGN-SITE-048` con `DESIGN-SUBL-004` (Sections) e `DESIGN-SUBL-005` (Videos).
Non sono stili/componente runtime Flutter automaticamente. In questo lotto: **0 UID**, **0 sorgenti importati**, **0 font binari**, **0 screenshot terzi**, **0 video/templates acquistati**, **0 modifiche alle app**.

| Link | Classificazione | Riuso concreto | Confine |
|---|---|---|---|
| [Shipframe](https://getshipframe.com/) | STORE_SCREENSHOT_CREATOR | App Store/Google Play screenshots da catture reali | Prodotto proprietario, tool direttamente non verificabile, pagamento da confermare |
| [Oversight Sections](https://supply.madebyoversight.com/sections) | WEBSITE_SECTION_LIBRARY | Landing Web: hero, scroll story, feature, pricing, FAQ | sezioni/template proprietari, free dopo account, no mirror o bundle del catalogo |
| [Mobbin](https://mobbin.com/) | APP_UX_REFERENCE | Flussi reali di onboarding, navigazione, premium, sicurezza | già presente; niente copia/redistribuzione screenshot |
| [Fontshare](https://fontshare.com/) | TYPOGRAPHY_REFERENCE | Type pairing e gerarchia app/Web | già presente; controllare per famiglia SIL OFL oppure ITF FFL prima di incorporare font |
| [Oversight Videos](https://supply.madebyoversight.com/videos) | VIDEO_AGENT_SKILLS | Explainer di prodotto/feature, clip marketing | template/skill proprietari, strumenti locali richiesti; niente Android runtime |

## Evidenze pubbliche e limitazioni

- **Shipframe:** dominio esatto non disponibile al fetch diretto; post del creatore su Reddit il 16/11/2026 e directory di terzi del 18/11 descrivono editor screenshot nel browser, iOS/Android, circa 16 temi, privacy locale e prezzo **$19 una tantum** dopo free con watermark. **Prezzo, termini/privacy e qualità export non confermati direttamente dal dominio ufficiale**: segnare `PARTIALLY_VERIFIED`, non comprare né integrare codice non disponibile.
  - https://www.reddit.com/r/SideProject/comments/1xxztg0/your_apps_deserve_good_screenshots/
  - https://www.thinkai.it/en/ai-tools/
- **Oversight Sections:** catalogo ufficiale al check mostra **70 sezioni, 41 gratuite con account e 29 Pro** (il numero varia: alcuni snapshot mostrano 65/24); piano Sections **$15/mese**. Pagine esemplari: [Collage](https://supply.madebyoversight.com/sections/portfolio-collage) e [Studio](https://supply.madebyoversight.com/sections/pricing-studio). Il servizio offre prompt + codice via login per sezioni free, ma **non significa licenza libera di ripubblicare i sorgenti in una biblioteca di componenti concorrente**. Termini: https://supply.madebyoversight.com/terms.
- **Oversight Videos:** pagina ufficiale distingue **Rays gratuito con account** da tre skill premium **Small details. Big difference**, **Organic**, **Kiln**; i video richiedono tool di creazione locali/Claude Code. Pricing **$9.99/mese o $79.99/anno** (USD, piani video separati dalle sezioni). Non acquistato. Fonti: https://supply.madebyoversight.com/videos e https://supply.madebyoversight.com/pricing/videos.
- **Fontshare:** uso personale/commerciale gratuito dichiarato ma **licenza differente per font** (SIL OFL e ITF Free Font License). Nessun download/vendorizzazione indiscriminata. Fonti: https://www.fontshare.com/about e https://fontshare.com/licenses/sil-ofl.
- **Mobbin:** `DESIGN-SITE-033` già verificato. La ricerca dei percorsi reali è reference di UX, non permesso di archiviare schermate di altre app. Fonte: https://mobbin.com/.

## Priorità per App Factory

1. **Shipframe per release/marketing**: pilota su screenshot reali e anonimi di Omni Cleaner, Cooking Anime, World Days e Wonderlog; output PNG e specifiche store da verificare prima di pubblicare. Alternative first-party AppLab/CI e template propri preferite per produzione scalabile.
2. **Mobbin (esistente)**: ricerca mirata su sicurezza cancellazione, premium e flussi completi delle app, niente clone pixel-to-pixel.
3. **Fontshare (esistente)**: verifiche caso per caso di lingua, diacritici, cifra, font weight e licenza; non cambiare Manrope/Lora o token già scelti senza approvazione.
4. **Oversight Sections**: reference e possibile editor per siti di presentazione, non componente Flutter/Compose già pronto. Il codice in un progetto specifico richiede licenza e dependency admission.
5. **Oversight Videos**: marketing remoto/offline, media originali, diritti video/music/voice; **non** dentro APK e nessun abbonamento attivato.

**Mappa multi-app:** [JSON](../UI-UX/FLORIENT_STACK_5_APP_MAP_2026-11-20.json) · [Markdown](../UI-UX/FLORIENT_STACK_5_APP_MAP_2026-11-20.md). Source catalog unico per sotto-pagine, preservati gli ID Mobbin e Fontshare. Tutte proposte `PROPOSED_ONLY`.
