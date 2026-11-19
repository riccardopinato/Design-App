# Design-App

## Aggiornamento corrente — Uiverse Favorites

**Uiverse Favorites aggiornati (18/11/2026, 17:40 Italia):** 108 link unici, +11 rispetto al precedente export, 0 rimossi; catalogo totale **111/111** con sorgente originale HTML/CSS, zero mancanti. **736 abbinamenti su 25 app**, tutti PROPOSED_ONLY. [Catalogo](./UI-UX/UIVERSE/README.md) · [Analisi dei nuovi 11](./UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.md) · [Diff verificato](./UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json). La completezza dell'account Uiverse resta non certificata.

Central design library for Riccardo's App Factory.

Design-App is the fast-retrieval layer for visual styles, UI/UX patterns, motion,
design tokens, reusable first-party source snapshots and external design discovery.

## Authority

Design-App is a specialized library, not the global Factory authority.

Order of truth:
1. app Product Bible;
2. app roadmap;
3. App-Factory-Core CURRENT / Master / Golden;
4. app-specific architecture and implementation;
5. Design-App as reusable design donor/reference.

## What is already harvested

The initial Project harvest includes:
- Anna's Diary;
- Notes-Ecosistema;
- Wonderlog;
- FrameLab;
- World Days;
- Battery Guard;
- CamperBoss;
- FocuSense;
- Phone Guard;
- Pocket/Tabletop protection UX;
- 180FlipCharge branding direction;
- CashMate design direction;
- shared Project design frameworks;
- the 36 UI/UX/design repositories already catalogued in Analisi-delle-mie-stelle-github;
- 37 curated GitHub design, motion, audio and tooling sources from 2026-10-27;
- 22 extra app-design and visual interaction sources from 2026-10-30.

## Anteprime visuali di tutti i componenti

[Tabella canonica dei 478 componenti con colonna Anteprima](BIBLIOTECA_COMPONENTI/TABELLA_478.md) ·
[Tabelle con immagini filtrate per ciascuna app](BIBLIOTECA_COMPONENTI/PER_APP/README.md) ·
[Visualizzatore HTML con ingrandimento](docs/componenti.html).

Le miniature renderizzate sono riferimenti visivi: **110 Uiverse acquisiti dal loro codice HTML/CSS originale**;
le altre 368 voci sono esplicitamente in attesa di immagini verificate. Le viste per app
sono generate dalle relazioni di `BIBLIOTECA_COMPONENTI/CATALOGO.json`, senza
ricopiare o alterare le Product Bible.

## Fast lookup

Start here:
- registry/DESIGN_REGISTRY.yaml — canonical pattern/style IDs;
- sources/PROJECT_PATTERN_HARVEST.md — human-readable project harvest;
- registry/OSS_DESIGN_SOURCES.yaml — external discovery pool;
- tested/TESTED_REGISTRY.yaml — first-party reusable source inventory;
- tested/source_snapshots/ — pinned source code snapshots;
- sources/PROJECT_FILE_FRAMEWORKS.md — reusable design rules from older Project frameworks;
- sources/GITHUB_DESIGN_RESEARCH_2026-10-27.md — curated GitHub research and adoption tiers;
- sources/SOUND_DESIGN_GUIDE.md — semantic UI sound guidance and vetted audio sources;
- sources/GITHUB_DESIGN_RESEARCH_2026-10-30.md — 22 app-design/UI gallery and gesture sources;
- packs/ROADMAP_COPY_READY.md — implementation and acceptance sequence for 4 reusable packs.

## Maturity

DISCOVERY -> REFERENCE -> ADAPTED -> SOURCE_VERIFIED -> LIBRARY_VERIFIED -> COPY_READY

A working source app does not automatically make an extraction COPY_READY.

## Main style families

- STYLE-A — Editorial Personal / Anna's Diary
- STYLE-B — Editorial Knowledge / Notes
- STYLE-C — Colorful Travel / Wonderlog
- STYLE-D — Photographic Editorial Premium / FrameLab
- STYLE-E — Daily Editorial Color / World Days
- STYLE-F — Clean Green Utility / Battery Guard
- STYLE-G — Outdoor Utility / CamperBoss
- STYLE-H — Neon Analytics / FocuSense
- STYLE-I — Reliable Safety Utility / Phone Guard
- STYLE-J — Pocket/Bag Protection Status UX
- STYLE-K — Compact Pixel Utility Branding / 180FlipCharge
- STYLE-L — Green/Black Finance Blocks / CashMate
- STYLE-M — Forest/Moss Map Outdoor / TrailPath
- STYLE-N — Minimal Premium Safety Utility / Easy Debloat
- STYLE-O — Image-first Culinary Cards / In Cucina con gli Anime
- STYLE-P — Visual Alerts / AOD Circle / Luminous Infinite Circle

## Automatic intake

When a future app task or research discovers a reusable design pattern, library,
animation, component or repository, evaluate it for Design-App and register it when
useful. Third-party code must pass license/provenance checks before being copied.

See AGENTS.md for the operating contract.


## Intake visuale da 750 stelle GitHub (16 novembre 2026)

Il registro esterno include ora **105 fonti uniche**, delle quali 7 nuove dal censimento recente: tldraw, Excalidraw, xyflow, Markmap, OpenWidget, AppFlowy Editor, Nodus. [Audit source-pinned e crosswalk per app](sources/STARS_750_VISUAL_INTAKE_2026-11-16.md). Sono tutte REFERENCE, non COPY_READY; il perimetro commerciale/OSS dei file resta un gate indipendente.

## External design-source coverage

The external discovery pool now contains 95 unique repositories:
- 36 initial UI/UX discovery sources;
- 37 curated and commit-pinned sources from the 2026-10-27 research batch;
- 22 curated and commit-pinned app-design sources from the 2026-10-30 research batch.

The curated batches cover Flutter, Compose, SwiftUI, web accessibility, adaptive platform UI,
responsive layouts, Material 3 Expressive, motion, design tokens, iconography, visual QA,
UI sound design and finished-screen galleries.

No external runtime dependency is automatically admitted into an app merely because
it is catalogued here. Dependency Admission, license checks and per-app Product Bible
constraints still apply.


## COPY_READY development

Design-App keeps a separate execution roadmap for the Motion Pack,
Semantic Sound Pack, Icon Adapter Pack and Visual QA Kit:
`packs/ROADMAP_COPY_READY.md`.

The Flutter Motion Pack v0.1.0 is **COPY_READY at library level** with
Flutter analyzer/widget-test/example CI evidence, documented in
`packs/motion/flutter/PROVENANCE.md`. It is not cross-app certified.
Check `packs/PACK_REGISTRY.yaml` for the per-pack status.
The Semantic Sound Pack has six pinned CC0 WAVs, a checksum validator and
an optional Flutter adapter at `packs/sound/adapters/flutter/`.
It passed independent static/Flutter CI and is LIBRARY_VERIFIED.
Physical-device playback acceptance is still pending, so it is not COPY_READY.
The Icon Adapter Pack has 24 canonical semantic IDs with verified generated
Flutter and Compose adapters under `packs/icons/`.
Flutter is COPY_READY at library level; Compose is LIBRARY_VERIFIED
pending physical Android UI validation. Pack overall is LIBRARY_VERIFIED.
The Flutter Visual QA Kit under `packs/visual-qa/flutter/` has passed its
45-case layout matrix and four committed screenshot pixel comparisons:
LIBRARY_VERIFIED, still awaiting real-app integration before COPY_READY.
Compose/SwiftUI extensions remain planned.

## Audit remediation 2026-10-30

See `docs/AUDIT_REMEDIATION_v1.md` for the five-step corrective program,
`registry/PATTERN_PROVENANCE.json` for donor evidence leads, and
`docs/GITHUB_BRANCH_PROTECTION.md` for the outstanding repository-admin gate.
The first-party design code has no blanket external reuse license; see
`docs/LICENSE_POLICY.md`.


## Template Notion — catalogo di ricerca

[Apri Template Notion](docs/TEMPLATE_NOTION/README.md). Catalogazione di pattern, senza importare template commerciali in un'app.

## Archivio mock-up estetici

È disponibile [MOCKUP ESTETICI](./MOCKUP%20ESTETICI/README.md): cartelle per AESTHETIC, NEON, VINTAGE, PIXEL ART, POLAROID e ANIME; per ogni stile, immagini, app suggerite e classificazioni incrociate. Include [matrice app ⇄ stili](./MOCKUP%20ESTETICI/MATRICE_APP_STILI.md) e catalogo per il futuro caricamento degli asset. Le reference non modificano automaticamente Product Bible e roadmap.

## Archivio UI/UX

Nuova sezione [UI/UX](./UI-UX/README.md) per catalogare tecniche visive, pattern e componenti: Neumorphism, Soft 3D, Glassmorphism, Neo-Apple, Nature-Tech, Bento UI, Pastel UI, Spatial 3D e Minimal Controls. Comprende [matrice molti-a-molti app ⇄ stili](./UI-UX/MATRICE_APP_STILI.md) e [classificazione degli esempi visibili nello screenshot](./UI-UX/RIFERIMENTI_DALLO_SCREENSHOT.md). Nessun asset di terzi è stato copiato.

## Riferimenti visuali forniti dall'utente — novembre 2026

[Catalogo UI/UX completo](./UI-UX/RIFERIMENTI_UTENTE_2026-11-12.md) · [Matrice per app](./UI-UX/MATRICE_APP_RIFERIMENTI_2026-11-12.md) · [Catalogo estetico](./MOCKUP%20ESTETICI/RIFERIMENTI_UTENTE_2026-11-12.md). 35 upload, 33 unici. Originali non pubblicati senza licenze/diritti verificati; nessuna app modificata.

## Riferimenti visuali forniti dall'utente — 13 novembre 2026

[Nuovo catalogo UI/UX 66 riferimenti](./UI-UX/RIFERIMENTI_UTENTE_2026-11-13.md) · [Registro JSON con SHA-256 e duplicati](./UI-UX/REGISTRO_RIFERIMENTI_UTENTE_2026-11-13.json) · [Matrice app](./UI-UX/MATRICE_APP_RIFERIMENTI_2026-11-13.md) · [Indice estetico](./MOCKUP%20ESTETICI/RIFERIMENTI_UTENTE_2026-11-13.md). 77 upload, 66 nuovi unici, 11 duplicati esatti. Il precedente lotto del 12/11 resta invariato (33 unici); totale due lotti: 99 unici. Materiale REFERENCE_ONLY: i file di terzi non sono stati ripubblicati e nessuna app è stata modificata.

## Matrice molti-a-molti App ↔ Stili (12–13/11/2026)

La classificazione trasversale dei **99 riferimenti unici** è consultabile [per app](./UI-UX/PER_APP_STILI_2026-11-13.md) oppure [per stile](./UI-UX/PER_STILE_APP_2026-11-13.md). Il [registro relazionale JSON](./UI-UX/MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json) contiene **254 coppie stile–app** e **771 link stile–app–reference**, con viste coerenti derivate dalle stesse associazioni. Gli originali restano fuori dal repository pubblico fino a verifica dei diritti di redistribuzione.

## Dichiarazione personale sulla licenza dei riferimenti — 13 novembre 2026

L'utente dichiara una **licenza personale** per tutte le immagini dei lotti 12–13/11/2026 (99 JPG distinti). La [dichiarazione e il perimetro](./UI-UX/DICHIARAZIONE_LICENZA_PERSONALE_2026-11-13.md) sono registrati nei due cataloghi JSON. Stato: `USER_DECLARED_PERSONAL_LICENSE`, non prova indipendente della licenza o di un permesso di redistribuzione pubblica. Le classificazioni e le associazioni molti-a-molti rimangono invariate.


## Anteprime immediate dei riferimenti UIR

- Ogni identificativo `UIR-xxxx` nelle matrici e nelle schede è un collegamento diretto alla rispettiva immagine JPEG. Per i 66 file nuovi il link è relativo a `main`; per i 33 originali della [PR #17](https://github.com/riccardopinato/Design-App/pull/17), ancora non integrati, il collegamento usa il commit che contiene gli asset.
- [Anteprime espandibili direttamente in GitHub](./UI-UX/ANTEPRIME_99.md): cliccare il nome UIR per mostrare/nascondere l'immagine senza lasciare la pagina.
- [Visualizzatore HTML con sovrimpressione](./docs/index.html): ricerca, filtri app/stile, tastiera, collegamento condivisibile `#UIR-0036`. **Il file HTML su github.com viene mostrato come codice**; per usarlo come sito va attivato GitHub Pages su `main /docs` (vedi [istruzioni](./docs/README.md)).

La classificazione resta molti-a-molti, con un solo file JPG per riferimento; la visualizzazione non trasforma automaticamente una reference in una capability implementata.

## Nuova fonte esterna: Ruixen UI (2026-11-13)

[**Ruixen UI**](https://ruixen.com/) è stata integrata come riferimento per componenti UI, microinterazioni, generatori visivi e motion. Registrati [277 file sorgente React con SHA Git](sources/RUIXEN_UI_REGISTRY_INVENTORY_2026-11-13.json) e [41 pattern selezionati per 18 app](sources/RUIXEN_UI_CURATED_APP_MAP_2026-11-13.json), con [audit, licenze, casi d'uso e roadmap](sources/RUIXEN_UI_DESIGN_MOTION_AUDIT_2026-11-13.md). Voce inserita nel [registro OSS](registry/OSS_DESIGN_SOURCES.yaml). **Stato: REFERENCE, non implementazione né Golden**. Per Flutter mantenere reimplementazione nativa e QA, per web codice MIT soggetto a dependency/asset audit; Pro separato.

## 10 nuovi repository anti-slop / design skills — 17 novembre 2026

Analizzati e registrati **10 repository di design-agent skills**, verificando README, entrypoint, licenze principali e HEAD immutabili. [Audit approfondito](sources/ANTI_SLOP_DESIGN_SKILLS_AUDIT_2026-11-17.md) · [Matrice repository ⇄ app](UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md) · [Registro bidirezionale JSON](UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).

Totale sorgenti esterne nel registro OSS Design-App: **119 uniche** (105 precedenti + 10 skill + 2 beUI + 2 EaseUI/Amicro). Le nuove fonti sono **REFERENCE**, le associazioni sono `PROPOSED_ONLY`: nessuna libreria installata nelle app, nessuna copia di asset esterni, nessuna modifica a Golden o Product Bible. Gli abbinamenti coprono UI/UX audit, design intelligence cross-platform, motion, qualità Web/PWA e marketing visivo (ambiti distinti). Le stelle sono dichiarate dall'utente, non confermate con enumerazione API autenticata.

## ICONE — raccolta statica e animata (17 novembre 2026)

Nuova sezione autonoma [**ICONE**](./ICONE/README.md) che collega fonti, licenze, anteprime e possibili usi nelle app. La prima fonte è [Gentleface Animated Icons](https://gentleface.com/categories/animated), con [28 icone candidate](./ICONE/ANTEPRIME.md) e [114 proposte molti-a-molti su 24 destinazioni](./ICONE/MATRICE_APP_ICONE.md). Il [registro relazionale JSON](./ICONE/REGISTRO_ICONE.json) conserva il collegamento app ↔ icona, lo stato dell'animazione e i semantic ID già esistenti. [Audit tecnico/licenza](./ICONE/GENTLEFACE_AUDIT_2026-11-17.md) · [Protocollo per Flutter, Compose e Web](./ICONE/GUIDA_INTEGRAZIONE.md).

**Stato:** REFERENCE / PROPOSED_ONLY. Zero SVG importati, zero app modificate, zero nuove librerie runtime e nessun nuovo Golden. Le animazioni Gentleface sono SVG native per Web; per Flutter e Compose serve verifica o adattamento nativo. Non sostituisce il pacchetto semantico esistente `packs/icons`.

## Dossier di design permanenti per ogni app — 17 novembre 2026

La sezione [**PER_APP**](./PER_APP/README.md) conserva una scheda dedicata per **25 app e piattaforme**: identità visiva, posizioni consigliate delle icone, categorie tematiche, trigger animazioni, limiti, fonti, stato e storico delle proposte. [Registro centrale JSON](./PER_APP/REGISTRO_APP_DESIGN.json) con **114 riferimenti a icone Gentleface** e **96 abbinamenti a skill di design** (dati di matrice, non funzionalità implementate).

La scheda [Cooking Anime](./PER_APP/cooking-anime.md) conserva **36 idee iconografiche** tra gattini kawaii, sushi, ramen, onigiri, bento, cibo cinese, motivi stagionali e comandi standard. **Quelle icone tematiche sono idee da reperire o disegnare, non file Gentleface verificati.** La sezione include regole per aggiornare le proposte in una PR senza perdere lo storico. Tutte le idee restano `PROPOSAL_ONLY`, subordinate alle Product Bible e ai repository reali delle app.

## Nuova fonte di design e componente Voice Orb — 17 novembre 2026

[**DevLibraries**](https://devlibraries.com/) è censito come portale di ricerca di componenti, UI, animazioni e skill: [registrazione e regole di intake](./sources/DEVLIBRARIES_DISCOVERY_2026-11-17.md) · [directory sorgenti](./sources/DESIGN_RESEARCH_SITES.json). Un portale non attribuisce automaticamente licenze di riuso alle librerie indicizzate.

Da [Voice Orb su DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) sono stati individuati e fissati i due repository originali MIT di beUI (Web e React Native): [audit](./sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [mappa a 10 app](./UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md). Per le future note vocali la sfera reagirà al microfono soltanto dopo l'implementazione di un recorder reale e di tutti gli stati e permessi. [Dossier per-app](./PER_APP/README.md) aggiornati. **Stato REFERENCE/PROPOSED_ONLY: nessun audio recorder, libreria o feature consumer implementati**.

## Temi, tendine, passaggi e caricamenti (17 novembre 2026)

Registrate [**EaseUI**](https://devlibraries.com/libraries/easeui) e [**Amicro**](https://devlibraries.com/libraries/amicro/card-stack-peel) nelle [fonti di design](./sources/DESIGN_RESEARCH_SITES.json), con [audit delle licenze e sorgenti](./sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) e [matrice molti-a-molti](./UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md): **5 pattern nominati e un ulteriore riferimento da screenshot** sui tempi di attesa, **19 app e 76 associazioni**. Tutte le proposte sono conservate nei [dossier per app](./PER_APP/README.md) e nel JSON canonico. Le quattro animazioni Amicro della prima selezione sono state successivamente individuate nei file implementativi originali; nessuna risulta collaudata in Flutter. Anche il file EaseUI Theme Toggle è stato esaminato. Zero modifiche ai consumer, zero pacchetti/asset importati, nessun Golden promosso.

## Amicro — sei nuovi componenti mappati per app (17/11/2026)

Sono archiviati [CurtainReveal, Cursor Trail, Perspective Flip, Scroll Reveal, Spatial Door Portal e Accordion Loader](./UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md), con [registro JSON](./UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.json), [audit sorgente](./sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) e [dossier PER_APP aggiornati](./PER_APP/README.md). **6 riferimenti, 19 app, 60 associazioni**, 4 file originali letti, 2 componenti il cui nome esatto non ha trovato riscontro nel repository al commit fissato. L'intake precedente Amicro è stato rettificato con percorsi ed export realmente presenti. Nessuna app o dipendenza modificata; tutte le assegnazioni restano `PROPOSED_ONLY`.

## Watermelon UI — Ricordi, selettori, modali e promemoria (17 novembre 2026)

Nuovo intake [**Watermelon UI**](https://ui.watermelon.sh/) tramite [DevLibraries](https://devlibraries.com/libraries/watermelon): [audit dei 9 componenti](./sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md), [matrice molti-a-molti](./UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md) e [registro JSON](./UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.json). **17 app, 73 associazioni**, sei sorgenti React/Motion originali letti e tre nomi esatti non rintracciati nella baseline. Il riferimento originale è MIT, ma asset/dipendenze vanno verificati singolarmente. [Anna's Diary](./PER_APP/annas-diary.md) contiene proposte dettagliate per Ricordi (carousel), giornata (riepilogo impegni) e selettori; i dossier delle app sono stati sincronizzati. **REFERENCE/PROPOSED_ONLY**: nessuna funzionalità mobile, notifiche OS, OAuth, codice o asset importati.

## DevLibraries Bookmarks — 30 riferimenti da screenshot (17/11/2026)

Dopo l'intake iniziale della pagina Bookmarks, sono stati ricevuti **3 screenshot utente** e registrati [**30 componenti**](./sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) (23 Amicro, 3 Watermelon, 4 senza provider certo). [Registro JSON machine-readable](./sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.json) con link GitHub originali, SHA, stato e [**matrice 120 abbinamenti su 20 app**](./UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md); [procedura di intake aggiornata](./sources/DEVLIBRARIES_BOOKMARKS_INTAKE.md). Tre voci erano già censite (nessuna duplicazione dei source repo). **I PNG originali restano nella conversazione**: il repo conserva metadati/hash e inventario testuale ma non contiene i file immagine. Tutto `REFERENCE/PROPOSED_ONLY`; non ci sono nuove implementazioni consumer.

## Impeccable Designing — qualità estetica e UX trasversale (17/11/2026)

La [guida ufficiale](https://impeccable.style/designing/) è stata approfondita e collegata all'**Impeccable già censito come `DSK-002`**, senza duplicare donor, sorgenti o capacità. [Analisi incrementale](./sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · [8 controlli e 10 app già collegate](./UI-UX/IMPECCABLE_DESIGNING_APP_MATRIX_2026-11-17.json) · [dossier per-app](./PER_APP/README.md). Metodo: Start/Improve/Check/Maintain, mockup-first o code-first, critique + harden + polish, `DESIGN.md` come documento derivato dalle scelte della Product Bible. **Detector e hooks automatici analizzano Web, non Flutter nativo**. Tutti i criteri sono `PROPOSED_ONLY`, non QA già eseguiti o promozioni Golden.

## Visual research — Dribbble + Collect UI (2026–27)

Added [source-grounded audit](sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) and [15-app crosswalk of 12 design patterns](UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md). Direction: product-owned, premium, clean visual identity without an automatic framework aesthetic. References are not external assets or ready-to-copy code.

## Uiverse — codice sorgente e collegamenti per app (18/11/2026)

[Catalogo dei nove link](./UI-UX/UIVERSE/README.md) · [Archivio HTML/CSS](./UI-UX/UIVERSE/CODICE_SORGENTE/README.md) · [Matrice app ⇄ componente](./UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md). **20 app e 64 associazioni PROPOSED_ONLY.** Sei sorgenti originali MIT verificati e salvati, tre HTML/CSS ancora non reperiti. Preferenze documentate: sfondo amir_6539, loader «Stiamo facendo la magia», libro animato per Ricordi. Nessuna modifica nei consumer, nessun Golden promosso.

## Favorites Uiverse — archivio personale 97 collegamenti (18/11/2026)

[Catalogo 100 componenti Uiverse](./UI-UX/UIVERSE/README.md) · [97 favorites importati](./UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [57 file HTML/CSS originali](./UI-UX/UIVERSE/CODICE_SORGENTE/README.md) · [43 gap di estrazione](./UI-UX/UIVERSE/FAVORITES/CODICE_NON_REPERITO.md) · [657 legami molti-a-molti su 25 app](./UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md). Zero componenti integrati direttamente nei consumer, nessun Golden promosso; la completezza dell'account resta da confrontare con il conteggio Uiverse.

## Aggiornamento recupero pubblico (2026-11-18)

Originali HTML/CSS aggiunti: **43**; catalogo **100/100**; Favorites **97/97**; codice non recuperato **0**. Provenienza e checksum in [RECUPERO_API](../UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json). Le cifre precedenti documentano lo stato storico prima di questo recupero. Nessuna adozione o test su app consumer.

## Aggiornamento recupero pubblico (2026-11-18)

Originali HTML/CSS aggiunti: **11**; catalogo **111/111**; Favorites **108/108**; codice non recuperato **0**. Provenienza e checksum in [RECUPERO_API](../UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json). Le cifre precedenti documentano lo stato storico prima di questo recupero. Nessuna adozione o test su app consumer.

## Biblioteca componenti — indice canonico e sorgenti offline

[Apri la biblioteca](BIBLIOTECA_COMPONENTI/README.md) · [Catalogo JSON](BIBLIOTECA_COMPONENTI/CATALOGO.json) · [Ricerca locale](BIBLIOTECA_COMPONENTI/cerca.py).

Dal 19 novembre 2026, l'archivio contiene **478 componenti canonici e 4 alias**: 277 sorgenti TSX Ruixen originali MIT appena acquisiti, 111 file originali Uiverse gia' in repo e altre reference non copiate senza prova di sorgente/diritti. **425 record canonici** hanno un file sorgente locale (una variante Uiverse duplicata e' alias, non una seconda voce). Gli originali TSX/HTML/CSS sono materiale di adattamento, NON nuovi widget Flutter pronti o una certificazione delle app. La priorita' del gusto dell'utente, Product Bible e Golden tecnici non cambia.

### Acquisizione aggiuntiva Amicro, Watermelon, EaseUI — 19/11/2026

Importati e verificati altri **38** originali React/TSX da tre repository MIT gia' catalogati: **30 Amicro**, **7 Watermelon**, **1 EaseUI**. Le licenze originali e i pin SHA sono in [sorgenti e provenance](BIBLIOTECA_COMPONENTI/sorgenti/README.md). Totale attuale: **425** sorgenti canonici archiviati e **53** reference senza codice locale. Nessun Flutter widget o app consumer modificati.
