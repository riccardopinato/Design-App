# PER_APP — dossier permanenti di design e iconografia

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
