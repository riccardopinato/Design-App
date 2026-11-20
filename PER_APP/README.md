# PER_APP — dossier permanenti di design e iconografia

## Uiverse — nuove associazioni nelle app

**79 nuovi candidati su 19 dossier**, per un totale di **736 relazioni su 25 app**, tutti PROPOSED_ONLY. [Matrice](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Refresh dei preferiti](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json). Nessun consumer modificato o nuova autenticazione obbligatoria.

Un dossier per ciascuna app o piattaforma della App Factory catalogata in Design-App. Conserva la direzione estetica, le idee iconografiche, il posizionamento su schermate, trigger animazione, limiti, fonti e verifiche, **senza confondere proposte con implementazioni**.

**Archivio canonico:** [REGISTRO_APP_DESIGN.json](./REGISTRO_APP_DESIGN.json) · [ICONE](../ICONE/README.md) · [UI-UX](../UI-UX/README.md) · [Mock-up](../MOCKUP%20ESTETICI/README.md).

**25 dossier**, 114 collegamenti a Gentleface, 96 collegamenti alle skill di design e 36 idee tematiche per Cooking Anime non ancora associate ad asset.

| App / piattaforma | Ambiti | Icone catalogate | Skill collegate | Scheda |
|---|---|---:|---:|---|
| 180FlipCharge | orientamento 180°, alimentazione/ricarica, tile rapido | 1 | 1 | [Dossier](./180flipcharge.md) |
| Anna's Diary | diario e ricordi, calendario, affetti e condivisione | 12 | 10 | [Dossier](./annas-diary.md) |
| App Factory Dashboard | repository e branch, capability/Golden, CI e build | 4 | 9 | [Dossier](./app-factory-dashboard.md) |
| Battery Guard | batteria, ricarica, risparmio energetico | 5 | 4 | [Dossier](./battery-guard.md) |
| BeerClass AI | bicchiere/beer mug, luppolo, valutazioni | 1 | 1 | [Dossier](./beerclass-ai.md) |
| CamperBoss | camper/van, acqua ed energia, aree sosta | 5 | 2 | [Dossier](./camperboss.md) |
| CashMate AI | portafoglio, spese e incassi, grafici | 2 | 3 | [Dossier](./cashmate-ai.md) |
| Cooking Anime | kawaii-gattini, food-japan, food-china | 5 | 7 | [Dossier](./cooking-anime.md) |
| Deskland Android | desktop, launcher, batteria/widget | 4 | 3 | [Dossier](./deskland-android.md) |
| Easy Debloat | package app, rimozione controllata, severità rischio | 2 | 1 | [Dossier](./easy-debloat.md) |
| Edu_01 Corpo Umano | organi, scheletro, sistemi corporei | 1 | 0 | [Dossier](./edu-01-corpo-umano.md) |
| FocusSense | attenzione, suono, luce | 2 | 3 | [Dossier](./focussense.md) |
| FrameLab | fotografia, editing, export | 5 | 8 | [Dossier](./framelab.md) |
| Notes-Ecosistema | nota, cartelle, canvas | 15 | 10 | [Dossier](./notes-ecosistema.md) |
| Omni Cleaner | galleria, video, eliminazione sicura | 10 | 7 | [Dossier](./omni-cleaner.md) |
| Phone Guard | protezione, avvisi, dispositivo | 1 | 0 | [Dossier](./phone-guard.md) |
| Pocket Guard | borsa, sensori, scudo | 3 | 1 | [Dossier](./pocket-guard.md) |
| Send-to-PC | PC, file, Wi-Fi | 2 | 0 | [Dossier](./send-to-pc.md) |
| SleepMax Coach | sonno, luna, sveglia | 4 | 1 | [Dossier](./sleepmax-coach.md) |
| Tabletop Motion Alarm | allarme, movimento, PIN | 2 | 0 | [Dossier](./tabletop-motion-alarm.md) |
| The Luminous Infinite Circle | cerchio luminoso, LED flash, notifica | 1 | 1 | [Dossier](./the-luminous-infinite-circle.md) |
| TrailPath | mappa, traccia, waypoint | 1 | 3 | [Dossier](./trailpath.md) |
| Web Utility Factory | strumenti, browser, SEO/ricerca | 0 | 4 | [Dossier](./web-utility-factory.md) |
| Wonderlog | viaggio, mappa, tappe | 13 | 7 | [Dossier](./wonderlog.md) |
| World Days | calendario, ricorrenza, storia | 13 | 10 | [Dossier](./world-days.md) |

## Protocollo di aggiornamento per evitare la perdita delle idee

1. Quando un'interazione definisce un'icona, un'animazione, uno stile, un posizionamento, una variante, un vincolo o una critica, aggiorna il profilo **dell'app pertinente**, il registro canonico e il dossier Markdown **nella stessa PR**, mantenendo lo storico.
2. Conserva **fonte, data, motivazione e stato**: `PROPOSAL_ONLY`, `APPROVED_DESIGN`, `IMPLEMENTED`, `VERIFIED`, `REJECTED`. Una proposta non diventa approvazione soltanto perché compare in Design-App.
3. Riusa gli ID `ICO-...` per Gentleface, `DSK-...` per le skill e `CAI-...` per i concetti kawaii/cibo di Cooking Anime. Gli ID `CAI` sono **idee da cercare/disegnare**, non icone Gentleface verificate.
4. Per nuove app aggiungi `PER_APP/<slug>.md` e un nuovo record nel registro: inserisci link, schermate, categorie, stato e verifiche previste. Non sovrascrivere le scelte prodotto confermate.
5. Prima di importare codice o asset: Product Bible, licenza specifica, provider/commit e attribuzione, UI family coerente, fallback statico, reduced-motion, testi accessibili, impatto APK/FPS e test runtime sul dispositivo.
6. Preferisci modifiche incrementali con PR e CI; lascia documentati gli elementi esclusi o rinviati, senza cancellarli.

**Perimetro:** catalogazione di raccomandazioni Design-App. Non è stato verificato il codice consumer; nessun nuovo asset importato o funzionalità implementata. La vera autorità rimane Product Bible/roadmap/code dei repo app.

## Proposte di interazione vocale — Voice Orb

Per il componente [beUI Voice Orb indicizzato da DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) sono state salvate **10 candidature condizionate** nei rispettivi dossier e nel JSON sotto `voice_ui_candidates`. [Mappa completa](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md). La disponibilità del microfono, la trascrizione e la registrazione effettiva rimangono fuori perimetro. Ogni futura evoluzione preserva lo storico senza sovrascrivere le precedenti scelte.

## Pattern di tema, movimento e attesa — intake 17/11/2026

[EaseUI/Amicro: matrice su 19 app](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md), con **76 associazioni PROPOSED_ONLY**: Theme Toggle chiaro/scuro, Card Stack Peel, Accordion Blind Pull, Interlocking Gear Step, Shutter Step Slices e riferimento screenshot a caricamenti/tempi d'attesa. Ogni dossier pertinente e il [registro JSON canonico](./REGISTRO_APP_DESIGN.json) conservano i collegamenti nello storico. Per i quattro effetti del primo intake Amicro è stata individuata l'implementazione originale dopo una seconda ricognizione; resta indispensabile validarli prima del riuso.

## Sei componenti Amicro aggiuntivi — 17/11/2026

[Nuovo catalogo Amicro](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md): sei link utente, 19 dossier pertinenti aggiornati, 60 nuove associazioni proposte (18 HIGH, 42 MEDIUM). Il [registro canonico](./REGISTRO_APP_DESIGN.json) conserva gli ID `AMX-...`, la collocazione, i limiti di accessibilità e la distinzione codice verificato/concetto non verificato. La ricerca ha inoltre rettificato l'evidenza dei quattro precedenti effetti Amicro (ora file esistenti individuati, sempre senza test di integrazione).

## Nuove proposte Watermelon UI — 17/11/2026

[Watermelon, matrice delle nove reference](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md) · [registro relazionale](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.json). **17 app e 73 collegamenti** aggiunti ai dossier e alla fonte canonica JSON. La [scheda Anna's Diary](./annas-diary.md) contiene requisiti non implementati per **riepilogo eventi Home Oggi** alla prima apertura del giorno oppure a un orario definito, **Carousel Slider** per Ricordi, picker, invito spazio condiviso e opzionale countdown. La presentazione in-app non implica notifiche di sistema, autenticazione o salvataggio già funzionanti.

## Nuova raccolta DevLibraries Bookmarks — 17/11/2026

Tre screenshot condivisi dall'utente sono stati convertiti in [30 voci verificabili come nomi e anteprime](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) e [120 abbinamenti su 20 app](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). Ogni dossier interessato e il [registro JSON](./REGISTRO_APP_DESIGN.json) conservano i riferimenti e lo storico. Per [Anna's Diary](./annas-diary.md) la preview di Notification List ora risulta confermata **visivamente**, ma l'implementazione del componente e del riepilogo quotidiano in Home Oggi resta **non verificata e non approvata**. I PNG sono allegati alla chat, non presenti nel repository.

## Impeccable Designing — raccomandazioni UX e QA per 10 app

Le 10 app già associate a Impeccable (`DSK-002`) nella [matrice originaria](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md) ora hanno **8 quality gates** e controlli contestuali aggiunti nei rispettivi dossier e nel [registro JSON per app](./REGISTRO_APP_DESIGN.json). [Analisi completa](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md). Stato `PROPOSED_ONLY/NOT_EXECUTED`, nessuna app collaudata o modificata, nessuna nuova libreria o donor duplicato.

## Direzione visiva 2026/27 — Dribbble e Collect UI

[Matrice per app e pattern](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md) · [Registro JSON](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.json). 15 app candidate, 12 pattern; i dossier e i profili restano PROPOSAL_ONLY / NOT_VERIFIED. La Product Bible governa scelte e priorità effettive.

## Uiverse — 18/11/2026

I dossier delle **20 app compatibili** e il registro canonico contengono le 64 relazioni con i nove componenti Uiverse. [Matrice](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [sorgenti](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md) · [registro](../UI-UX/UIVERSE/REGISTRO_COMPONENTI.json). Nessun cambiamento nelle app, nessuna implementazione certificata.

## Favorites Uiverse — tutti i 25 dossier (18/11/2026)

Il [registro centrale per-app](./REGISTRO_APP_DESIGN.json) e i dossier Markdown per **25 app** sono sincronizzati con [657 associazioni](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json). I **97 favorites esportati** mappano 54 sorgenti originali disponibili e 43 da recuperare. Nessuna adozione runtime/Golden viene implicata dai suggerimenti.

## Aggiornamento recupero pubblico (2026-11-18)

Originali HTML/CSS aggiunti: **43**; catalogo **100/100**; Favorites **97/97**; codice non recuperato **0**. Provenienza e checksum in [RECUPERO_API](../UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json). Le cifre precedenti documentano lo stato storico prima di questo recupero. Nessuna adozione o test su app consumer.

## Aggiornamento recupero pubblico (2026-11-18)

Originali HTML/CSS aggiunti: **11**; catalogo **111/111**; Favorites **108/108**; codice non recuperato **0**. Provenienza e checksum in [RECUPERO_API](../UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json). Le cifre precedenti documentano lo stato storico prima di questo recupero. Nessuna adozione o test su app consumer.


## Intake 15 siti esterni — 20/11/2026

**14 profili con nuove proposte, 68 associazioni, 14 siti unici (15 URL; Godly reindirizza a Recent).** La [matrice dedicata](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md), il [JSON relazionale](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json) e l'[audit dei siti](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) integrano i dossier e `REGISTRO_APP_DESIGN.json` senza creare consumer implementati. Tutte le associazioni restano PROPOSED_ONLY.


## Nuovi siti Figma/ReUI/Best Designs — 20/11/2026

**12 dossier aggiornati, 31 relazioni PROPOSED_ONLY**, 3 fonti di scoperta distinte e il file specifico Figma Bento Widget Templates (nodi reali e categorie con provenienza). [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Registro JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json) · [Audit](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md). Il file Figma e' distinto dalla directory Community. ReUI Free e' React/TypeScript e non fornisce Dart Flutter pronto. Nessun asset acquisito.


## Nuove risorse UI deduplicate — 20 novembre 2026

**12 URL gia' archiviati, nessun nuovo audit; 3 nuove fonti e 22 associazioni su 12 dossier**. [Matrice](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/UI_SOURCES_3_APP_MAP_2026-11-20.json) · [Analisi licenze e duplicati](../sources/UI_SOURCES_DEDUP_THINKUI_MOBBIN_REACTBITS_2026-11-20.md). Integrazioni consumer/Flutter non eseguite; tutto **PROPOSED_ONLY**.


## Nuovi riferimenti Web/Agent UI — 20/11/2026

**11 dossier aggiornati, 37 relazioni PROPOSED_ONLY**, con 7 fonti nuove, 2 sottopagine di ReUI/shadcn gia' noti senza duplicati e 1 shortlink t.co da risolvere. [Matrice](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.md) · [Registro](../UI-UX/DESIGN_SOURCES_AGENTS_SCROLL_APP_MAP_2026-11-20.json) · [Audit](../sources/DESIGN_SOURCES_AGENTS_SCROLL_2026-11-20.md). Nessun consumer modificato, licenze per singolo elemento e accessibilita'/FPS richieste prima dell'implementazione.
