# Audit delle 15 risorse di design AI/visual — 2026-11-20

**Origine:** elenco di 15 URL condivisi dall'utente il 20/11/2026. **14 servizi distinti**: godly.website reindirizza a recent.design. Factory baseline: `riccardopinato/App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835`, CURRENT Master 27, Golden Index 31, Registry 2. Design-App base: `7383cc331920e85ed14ca79af77229bc725fd2bb`.

**Classificazione:** REFERENCE_ONLY / PROPOSED_ONLY, salvo Lucide gia' referenziato nell'Icon Adapter Pack; zero codice, asset, font, screenshot di terzi o nuove dipendenze importati, zero consumer modificati, zero Golden promossi. Nessun aumento di score costituisce un test Flutter.

## Inventario e giudizio

| # | Fonte | Priorita' | Accesso/gratuita' | Evidenza | Prima applicazione concreta |
|---:|---|---|---|---|---|
| 1 | [Motion Sites](https://motionsites.ai/) | B | FREE_SAMPLES; FULL_ACCESS_LIMITS_NOT_FULLY_VERIFIED | DIRECT_PAGE_VERIFIED | Animated hero with reduced-motion fallback |
| 2 | [Motion Sites Studio](https://studio.motionsites.ai/) | C | PAID_PLANS_VISIBLE; FREE_TIER_NOT_CONFIRMED | DIRECT_FETCH_UNAVAILABLE_PRICING_INDEXED | AI-assisted website prototype comparison |
| 3 | [Land-book](https://land-book.com/) | A_WEB | FREEMIUM_FREE_LIMITED_PRO_FROM_6_USD_MONTH | HOME_403; SECTIONS_PRICING_VERIFIED | Pricing-page hierarchy with distinct comparison tiers |
| 4 | [Recent Design](https://recent.design/) | A | PUBLIC_BROWSING; ACCOUNT_FEATURE_LIMITS_UNVERIFIED | DIRECT_PAGE_VERIFIED | App icon and typography moodboards |
| 5 | [Landdding](https://landdding.com/) | B_WEB | FREE_BROWSING; PRO_EXTENDS_ACCESS | DIRECT_PAGE_VERIFIED | Sector-specific landing layouts for SaaS, utility and food |
| 6 | [Font in Logo](https://fontinlogo.com/) | B | FREE_FONT_PREVIEWS_GENERATORS; VERIFY_INDIVIDUAL_FONT | DIRECT_PAGE_VERIFIED | Match editorial title typography to product tone |
| 7 | [Godly](https://godly.website/) | alias → Recent | SAME_AS_RECENT | VERIFIED_REDIRECT_TO_RECENT_DESIGN | Solo alias |
| 8 | [60FPS](https://60fps.design/) | A | PUBLIC_GALLERY; PAID_OR_ADDITIONAL_FEATURES_NOT_ASSERTED | DIRECT_PAGE_VERIFIED | Contextual bottom sheets, card transitions, long press |
| 9 | [Fontshare](https://fontshare.com/) | A | FREE_TO_USE_SUBJECT_TO_PER_FONT_LICENSE | JS_REQUIRED; FONT_AND_LICENSE_PAGES_INDEXED | Pair serif editorial headings with neutral readable UI fonts |
| 10 | [Realtime Colors](https://realtimecolors.com/) | A | FREE_CLAIM_CONFIRMED_OFFICIAL | DIRECT_PAGE_VERIFIED | Preview text/background/primary/secondary/accent combinations on real UI |
| 11 | [Coolors](https://coolors.co/) | B | FREEMIUM; FREE_PALETTES_LIMITED | HOME_403; PUBLIC_PALETTE_PAGES_VERIFIED | Generate candidate 5-color palettes, then test in actual screen |
| 12 | [Lucide](https://lucide.dev/) | A_EXISTING | FREE_OPEN_SOURCE | DIRECT_SITE_AND_GITHUB_LICENSE_VERIFIED | Consistent stroke and semantic icon naming |
| 13 | [SVGL](https://svgl.app/) | B_RESTRICTED | PUBLIC_FREE_API_RATE_LIMITED | DIRECT_API_DOCS_VERIFIED | Find official provider logos for legitimate integration badges |
| 14 | [Shots](https://shots.so/) | A_MARKETING | FREE_BASIC_PRO_TIERS | DIRECT_PAGE_AND_TERMS_VERIFIED | Create marketing phone/device mockups from own QA screenshots |
| 15 | [Cosmos](https://cosmos.so/) | A | FREE_USE_WITH_OPTIONAL_PREMIUM | DIRECT_PAGE_VERIFIED | Moodboard collections and search by color/similarity |

## Schede e caveat individuali

### 1. Motion Sites — https://motionsites.ai/
- **Ruolo:** `AI_WEB_DESIGN_PROMPT_GALLERY`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** PROMPTS_AND_SHOWCASES_NOT_ASSUMED_REUSABLE.
- **Uso consigliato:** Animated hero with reduced-motion fallback; Motion-first landing sections driven by content rather than decoration.
- **Destinazioni:** web-utility-factory, app-factory-dashboard.
- **Limite:** Prompt counts advertised by social post not independently verified; web-specific prompt results are not Flutter code.

### 2. Motion Sites Studio — https://studio.motionsites.ai/
- **Ruolo:** `AI_WEBSITE_BUILDER`; **stato:** `DIRECT_FETCH_UNAVAILABLE_PRICING_INDEXED`; **licenza/diritti:** GENERATED_CODE_OWNERSHIP_TERMS_NEED_REVIEW.
- **Uso consigliato:** AI-assisted website prototype comparison.
- **Destinazioni:** web-utility-factory, app-factory-dashboard.
- **Limite:** Not admitted as equivalent to Lovable, code donor, or a free builder without direct live test.

### 3. Land-book — https://land-book.com/
- **Ruolo:** `CURATED_WEB_SECTIONS`; **stato:** `HOME_403; SECTIONS_PRICING_VERIFIED`; **licenza/diritti:** THIRD_PARTY_SHOTS_REFERENCE_ONLY.
- **Uso consigliato:** Pricing-page hierarchy with distinct comparison tiers; Searchable landing sections by style/color/type.
- **Destinazioni:** web-utility-factory, app-factory-dashboard, cashmate-ai.
- **Limite:** Individual captured websites remain third-party copyright; useful principally Web/PWA/Store landing.

### 4. Recent Design — https://recent.design/
- **Ruolo:** `CURATED_MULTI_DISCIPLINE_GALLERY`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** THIRD_PARTY_SHOTS_REFERENCE_ONLY.
- **Uso consigliato:** App icon and typography moodboards; Editorial/mobile layout comparison.
- **Destinazioni:** annas-diary, notes-ecosistema, framelab, cooking-anime, web-utility-factory.
- **Limite:** Legacy godly.website points to this same service; indexed once only.

### 5. Landdding — https://landdding.com/
- **Ruolo:** `LANDING_GALLERY_AND_TEMPLATES`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** DESIGNS_AND_TEMPLATES_HAVE_PER_ITEM_RIGHTS.
- **Uso consigliato:** Sector-specific landing layouts for SaaS, utility and food; Filter content by industry and frontend platform.
- **Destinazioni:** web-utility-factory, app-factory-dashboard, cooking-anime.
- **Limite:** Page is useful for marketing references; downloading a template is a distinct licensing check.

### 6. Font in Logo — https://fontinlogo.com/
- **Ruolo:** `TYPOGRAPHY_BRAND_STUDY`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** FONT_LICENSE_PER_FAMILY; BRANDS_AND_TRADEMARKS_SEPARATE.
- **Uso consigliato:** Match editorial title typography to product tone; Use commercially licensed alternatives, not copied brand logos.
- **Destinazioni:** cooking-anime, world-days, framelab, annas-diary.
- **Limite:** Font lookalikes are not a license to copy a protected wordmark, title or trademark.

### 7. Godly — https://godly.website/
- **Ruolo:** `REDIRECT_ALIAS`; **stato:** `VERIFIED_REDIRECT_TO_RECENT_DESIGN`; **licenza/diritti:** SAME_AS_RECENT.
- **Uso consigliato:** Registrare soltanto il reindirizzamento all'origine canonica Recent Design.
- **Destinazioni:** nessuna aggiuntiva.
- **Limite:** Alias of DESIGN-SITE-018; not an additional unique service.

### 8. 60FPS — https://60fps.design/
- **Ruolo:** `MOBILE_WEB_INTERACTION_REFERENCE`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** VIDEOS_AND_SCREENSHOTS_REFERENCE_ONLY.
- **Uso consigliato:** Contextual bottom sheets, card transitions, long press; Swipe delete with explicit undo and stateful completion; Meaningful gallery transitions and reduced-motion variants.
- **Destinazioni:** annas-diary, notes-ecosistema, omni-cleaner, framelab, wonderlog, deskland-android, battery-guard, trailpath.
- **Limite:** Many filters (Calendar, Bottom Sheet, Delete, Empty State, Shared Element, Scrub); recordings do not supply Flutter code.

### 9. Fontshare — https://fontshare.com/
- **Ruolo:** `FONT_DISTRIBUTION`; **stato:** `JS_REQUIRED; FONT_AND_LICENSE_PAGES_INDEXED`; **licenza/diritti:** PER_FONT_ITF_FFL_OR_SIL_OFL; REDISTRIBUTION_RESTRICTIONS_VARY.
- **Uso consigliato:** Pair serif editorial headings with neutral readable UI fonts; Create character-set/language coverage checklist before choosing a family.
- **Destinazioni:** annas-diary, notes-ecosistema, world-days, framelab, cooking-anime, app-factory-dashboard.
- **Limite:** No font binary copied; only shortlist names with independently verified font family page and terms.

### 10. Realtime Colors — https://realtimecolors.com/
- **Ruolo:** `COLOR_TOKEN_LIVE_PREVIEW`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** EXPORTED_PALETTE_VALUES_ONLY; CHECK_SERVICE_TERMS_FOR_OTHER_ASSETS.
- **Uso consigliato:** Preview text/background/primary/secondary/accent combinations on real UI; Compare light/dark/contrast and export token candidates.
- **Destinazioni:** annas-diary, notes-ecosistema, omni-cleaner, cashmate-ai, battery-guard, focussense, trailpath, world-days.
- **Limite:** A website mockup is not proof that a Flutter component passes accessibility contrast or native rendering.

### 11. Coolors — https://coolors.co/
- **Ruolo:** `COLOR_PALETTE_GENERATOR`; **stato:** `HOME_403; PUBLIC_PALETTE_PAGES_VERIFIED`; **licenza/diritti:** PALETTE_VALUES_REFERENCE; ASSET_EXPORT_AND_TERMS_CHECK.
- **Uso consigliato:** Generate candidate 5-color palettes, then test in actual screen; Use generated harmony only as a starting point for semantic tokens.
- **Destinazioni:** framelab, annas-diary, world-days, cooking-anime, wonderlog.
- **Limite:** Do not assert unrestricted free exports/saves or full homepage access.

### 12. Lucide — https://lucide.dev/
- **Ruolo:** `OPEN_SOURCE_ICON_SET`; **stato:** `DIRECT_SITE_AND_GITHUB_LICENSE_VERIFIED`; **licenza/diritti:** ISC_LIBRARY; NO_BRAND_LOGOS.
- **Uso consigliato:** Consistent stroke and semantic icon naming; Map candidate glyphs to existing factory semantic icon adapter.
- **Destinazioni:** omni-cleaner, notes-ecosistema, cashmate-ai, app-factory-dashboard, battery-guard, annas-diary.
- **Limite:** Already referenced in packs/icons/PROVENANCE.md; no duplicate runtime pack or Flutter donor admitted.

### 13. SVGL — https://svgl.app/
- **Ruolo:** `BRAND_LOGO_DISCOVERY_AND_API`; **stato:** `DIRECT_API_DOCS_VERIFIED`; **licenza/diritti:** BRAND_TRADEMARK_PERMISSION_PER_LOGO; CODE_LICENSE_SEPARATE.
- **Uso consigliato:** Find official provider logos for legitimate integration badges; Use metadata/API for discovery only; cache and permission review.
- **Destinazioni:** notes-ecosistema, app-factory-dashboard, web-utility-factory.
- **Limite:** API says do not clone SVGL product; site notes logo permission. Never mass-bundle provider logos.

### 14. Shots — https://shots.so/
- **Ruolo:** `PRODUCT_MOCKUP_TOOL`; **stato:** `DIRECT_PAGE_AND_TERMS_VERIFIED`; **licenza/diritti:** OUTPUT_TERMS_AND_UPLOADED_ASSET_RIGHTS_REVIEW.
- **Uso consigliato:** Create marketing phone/device mockups from own QA screenshots; Create consistent portrait/landscape Play Store image compositions.
- **Destinazioni:** omni-cleaner, annas-diary, notes-ecosistema, framelab, cooking-anime, world-days, web-utility-factory.
- **Limite:** Promotional renders do not replace authentic in-app screenshots or runtime visual QA.

### 15. Cosmos — https://cosmos.so/
- **Ruolo:** `VISUAL_COLLECTION_AND_DISCOVERY`; **stato:** `DIRECT_PAGE_VERIFIED`; **licenza/diritti:** THIRD_PARTY_IMAGES_REFERENCE_ONLY.
- **Uso consigliato:** Moodboard collections and search by color/similarity; Trace artist and source of visual reference; Explore collections/vision-board organization without copying thumbnails.
- **Destinazioni:** annas-diary, notes-ecosistema, framelab, wonderlog, cooking-anime, world-days.
- **Limite:** Do not upload/re-host copyrighted images from Cosmos as app assets without distinct permission.

## Pattern estratti, non nuovi widget copiati

1. **MOTION-REVIEW-01:** movimento funzionale bottom sheet/quick actions/tap/long-press (60FPS); verificare durata, gesto annullabile, reduced-motion e jank reale in Flutter.
2. **MOTION-REVIEW-02:** swipe to delete solo con conferma/undo o Safe Trash, mai eliminazione irreversibile nascosta dietro un'animazione (Omni Cleaner, Notes, Anna).
3. **COLOR-REVIEW-01:** token `text/background/primary/secondary/accent` su viste vere, con dark mode, contrasto e gerarchia (Realtime Colors, Coolors).
4. **TYPE-REVIEW-01:** shortlist di font con supporto per tutti i locale, test font scale e licenza singola (Fontshare, Font in Logo); Anna mantiene per default Manrope/Lora finche' non approvato altro.
5. **ICON-REVIEW-01:** audit di coerenza tra icone e semantica: riusare prima `packs/icons`, solo dopo considerare Lucide/nuovo adapter; SVG brand SVGL separati dai simboli UI.
6. **EDITORIAL-REVIEW-01:** collections/moodboard con provenance e contenuti realmente proprietari (Cosmos, Recent) per Ricordi, Notes canvas, FrameLab; no copia di opere altrui.
7. **MARKETING-REVIEW-01:** layout di landing e pricing allineati all'offerta reale (Land-book, Landdding, Motion Sites); SEO Web via stack web, non trapiantare template React dentro Flutter.
8. **STORE-REVIEW-01:** usare Shots con screenshot autentici e dichiarazione delle immagini promozionali, mantenendo separato il visual QA runtime.

## Confronti e falsi claim da evitare

- Il claim sociale **«15 strumenti gratuiti»** e' impreciso: Land-book, Coolors, Shots, Cosmos, MotionSites e Studio hanno tier/limitazioni o accesso non interamente verificabile. Realtime Colors si dichiara 100% gratis; Lucide e' open source ISC. Non assumere che ogni asset mostrato sia licenziato.
- **«Oltre 1.000 prompt»** Motion Sites non e' certificato come conteggio esatto; catalogo dinamico e varie pagine commerciali. Motion Sites Studio non e' stato testato: accesso diretto non riuscito.
- **Godly = Recent** al momento della visita: un solo ID canonico, alias storico conservato.
- **Lucide ≠ SVG di marchi**: icone open source ISC; SVGL e' un repertorio di loghi e API soggetta a rate limit, con diritti dei marchi separati.
- **Galleria ≠ componente Flutter**: video, CSS, screenshot o prompt sono riferimenti; il codice originale e i test Flutter non sono acquisiti con questo lotto.

## Fonti puntuali di verifica (20/11/2026)

- Motion Sites: https://motionsites.ai/ ; Motion Studio pricing ricercabile: https://studio.motionsites.ai/pricing (fetch non riuscito)
- Land-book sezioni/piano: https://land-book.com/sections/pricing (Basic limitato, Pro da $6/mese)
- Recent: https://recent.design/ ; Godly alias: https://godly.website/
- Landdding: https://landdding.com/ ; Font In Logo: https://www.fontinlogo.com/
- 60FPS: https://60fps.design/ ; Fontshare (sito JS-only): https://fontshare.com/ ; esempio license family: https://www.fontshare.com/fonts/ranade
- Realtime Colors: https://www.realtimecolors.com/ ; Coolors: https://coolors.co/ (home 403, palette pubbliche accessibili)
- Lucide: https://lucide.dev/ ; licenza: https://github.com/lucide-icons/lucide/blob/main/LICENSE
- SVGL API: https://svgl.app/docs/api (API libera, rate-limited, divieto di replica del servizio)
- Shots: https://shots.so/ ; termini: https://shots.so/terms (Free/Basic/Pro)
- Cosmos: https://www.cosmos.so/ ; Premium: https://help.cosmos.so/en/articles/11717954-cosmos-premium

## Proposta di esecuzione

1. Per Omni Cleaner: 60FPS delete/preview/undo + palette Realtime Colors + Lucide valutato rispetto all'Icon Adapter (priorita' estetica alta).
2. Per Anna's Diary: transizioni Calendario/Crea/Ricordi 60FPS e raccolte/moodboard Cosmos (preservare stile gia' approvato e sicurezza dei dati).
3. Per Notes: microinterazioni canvas, collezioni visuali e iconografia coerente.
4. Per portfolio Web Utility/App Factory Dashboard: Land-book/Landdding come reference di landing/pricing, Shots per marketing.
5. Dopo approvazione per-app: mock-up, Product Bible, QA visivo su fixture reali, accessibilita', performance e solo dopo codice/PR consumer. Non cambiare le app da questo intake.
