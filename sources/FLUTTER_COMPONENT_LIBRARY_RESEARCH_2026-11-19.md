# Flutter Component Library — catalogo di riferimento e audit 19 novembre 2026

**Fonte primaria:** https://fluttercomponentlibrary.com/  
**ID sito:** DESIGN-SITE-015 · **Stato:** REFERENCE_ONLY_PENDING_SOURCE_LICENSE  
**Obiettivo:** componenti moderni e curati come spunto per app Flutter 2026–27, in modo coerente con l'identita' di ciascuna app.

## Esame del sito (verificato vs non verificato)

Le schede dei 15 componenti elencati nel [JSON di catalogo/mapping](../UI-UX/FLUTTER_COMPONENT_LIBRARY_APP_MAP_2026-11-19.json) sono raggiungibili in forma di pagine testuali: riportano nome, categoria, demo, percorsi di file Dart e istruzioni di copia. Alcune riportano dipendenze pub. La homepage risulta dinamica e il contenuto non e' stato integralmente acquisito; **non sono stati letti i Dart sorgenti completi dai file indicati**, ne' trovata una licenza del codice/asset o un repository ufficiale di questa raccolta chiaramente verificati. I nomi dei file dichiarati e i package vanno verificati alla fonte, non trattati come prove di disponibilita'.

Il sito dice di copiare il codice, ma un invito pubblicato nella pagina non prova da solo i diritti di riuso commerciale e la compatibilita' del sorgente. Pertanto non usare COPY_READY, NON copiare codice/asset dal sito finche' fonte/licenza per-file non sono verificati. E' possibile studiare la struttura di un componente e scrivere **un'implementazione originale**.

## Componenti campionati

| ID | Nome | Pagina | Dart dichiarato | Dipendenza dichiarata |
|---|---|---|---|---|
| FCL-001 | Docking Bar | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/docking-bar.html) | `lib/components/docking_bar.dart` | Non elencata (non significa assente) |
| FCL-002 | Custom Buttons | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/custom-buttons.html) | `lib/components/custom_action_button.dart` | Non elencata (non significa assente) |
| FCL-003 | Filter Button | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/filter-button.html) | `lib/components/filter_button.dart` | Non elencata (non significa assente) |
| FCL-004 | Banner Info | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/banner-info.html) | `lib/components/info_banner.dart` | Non elencata (non significa assente) |
| FCL-005 | Bottom Sheet | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/bottom-sheet.html) | `lib/components/bottom_sheet_widget.dart` | Non elencata (non significa assente) |
| FCL-006 | Book Shelf | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/book-shelf.html) | `lib/components/book_shelf.dart` | Non elencata (non significa assente) |
| FCL-007 | Slide To Act | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/slide-to-act.html) | `lib/components/slide_to_act_widget.dart` | `slide_to_act: ^2.0.2` |
| FCL-008 | FAQ Widget | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/faq-widget.html) | `lib/components/faq_widget.dart` | `flutter_easy_faq: ^1.0.1` |
| FCL-009 | Stepper | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/stepper.html) | `lib/components/custom_stepper.dart` | `easy_stepper: ^0.8.1` |
| FCL-010 | Slider | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/slider.html) | `lib/components/custom_slider.dart` | Non elencata (non significa assente) |
| FCL-011 | Plan Card | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/plan-card.html) | `lib/components/plan_card_component.dart` | Non elencata (non significa assente) |
| FCL-012 | Scratcher | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/scratcher.html) | `lib/components/custom_scratcher.dart` | `scratcher: ^2.5.0` |
| FCL-013 | Page Flipper | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/page-flipper.html) | `lib/components/flip_page_widget.dart` | Non elencata (non significa assente) |
| FCL-014 | Drawer | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/drawer.html) | `lib/components/drawer_widget.dart` | Non elencata (non significa assente) |
| FCL-015 | Draggable FAB | [Apri scheda](https://fluttercomponentlibrary.com/pages/components/draggable-fab.html) | `lib/components/draggable_fab.dart` | `floating_draggable_widget: ^2.3.0` |

Tutte le descrizioni («beautiful», «responsive», «optimized») sono **claim del catalogo**, non test Flutter/AppLab verificati. Demo iframe non prova la resa Android/iOS nativa.

## Procedura d'uso per un redesign o nuovo componente

1. Verificare prima il design scelto dall'utente in Design-App, Product Bible, mock-up approvati e il look attuale dell'app.
2. Verificare Golden/donor interni e widget Flutter gia' presenti. Solo dopo cercare una categoria pertinente in Flutter Component Library e confrontare 1–3 alternative utili.
3. Conservare link singolo del componente, Dart source file **realmente acquisito** (oppure UNKNOWN), SPDX/LICENCE valida, eventuali asset e dipendenze reali. Per copia nel repo serve licenza esplicita e attribution ove richiesto; senza, REFERENCE_ONLY e reimplementazione originale.
4. Adattare token, gerarchia, colore, icone, motion e navigation per evitare look stock/ChatGPT; non aggiungere shader/animazioni decorative o package pesanti senza valore concreto.
5. Validare responsive, font scale, semantica/accessibilita', layout insets, stati loading/empty/error/offline, light/dark e reduced-motion; controllare peso APK e build.
6. Documentare screenshot prima/dopo e review estetica dell'utente prima di dichiarare visual PASS. Nessuna promozione Golden/donor o implementazione dichiarata in assenza di prove.

## Applicazioni candidate

| App | Componenti proposti | Motivazione |
|---|---|---|
| annas-diary | FCL-001, FCL-005, FCL-006 | Only if compatible with the already approved bottom navigation; no silent redesign; Contextual sheets for action groups with privacy boundaries; Memory collection display only if editorial and approved |
| notes-ecosistema | FCL-003, FCL-005, FCL-014 | Content search and filter semantics; Selection context actions without disrupting canvas; Responsive navigation, keep editor/canvas controls reachable |
| world-days | FCL-004, FCL-003, FCL-008 | Historical context or editorial callouts; real sourced information only; Filter by region, country, category and verified story availability; Expandable explanations without repetitive nested cards |
| battery-guard | FCL-004, FCL-010, FCL-005 | Battery condition alerts grounded in actual device data; Preference thresholds only where operating-system behavior allows; Technical drill-down without obscuring current telemetry |
| camperboss | FCL-009, FCL-008, FCL-005 | Multi-step trip/camper checklist or setup when real flow exists; Offline help and structured setup instructions; Contextual actions usable offline |
| framelab | FCL-002, FCL-001, FCL-005 | Buttons and control demonstrations customized to app design tokens; Navigational prototype only if its product architecture calls for it; Responsive control panels and settings |

L'associazione e' puramente progettuale (**PROPOSED_ONLY**). Non impone cambi di schermata o di navigazione e non certifica lo stack runtime attuale dei singoli consumer. Altre schede possono essere proposte solo con effettiva esigenza per quell'app.

**File:** [JSON bidirezionale](../UI-UX/FLUTTER_COMPONENT_LIBRARY_APP_MAP_2026-11-19.json) con tutte le schede e i relativi percorsi, sorgenti e stati. Nessun codice di terzi copiato. Nessuna app o package installato.
