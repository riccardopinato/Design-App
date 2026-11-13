# Ruixen UI — studio sorgente, animazioni e riuso App Factory

Data di acquisizione: **2026-11-13**. Stato: **REFERENCE / SOURCE CANDIDATE** (NON CODE_DONOR certificato, NON GOLDEN, nessuna implementazione in app). Questo audit aggiunge un riferimento esterno curato, **non** un nuovo stile `UIR-xxxx` e non modifica le scelte prodotto approvate.

## Fonte e perimetro verificato

| Campo | Riferimento verificato |
|---|---|
| Sito ufficiale | [ruixen.com](https://ruixen.com/) |
| Documentazione | [ruixen.com/docs](https://ruixen.com/docs) · [Catalogo componenti](https://ruixen.com/docs/components) |
| Repository sorgente | [ruixenui/ruixen.com](https://github.com/ruixenui/ruixen.com) |
| Commit sorgente *immutabile* | [`f6b20860623fa39122ac2b5f0e5bd29a9eb10941`](https://github.com/ruixenui/ruixen.com/tree/f6b20860623fa39122ac2b5f0e5bd29a9eb10941) |
| Licenza **repository gratuito** | [MIT — LICENSE.md](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/LICENSE.md): mantenere notice MIT/copyright quando si copia codice |
| Licenza **Pro** | [Commercial license distinta](https://pro.ruixen.com/license): per prodotti finali licenziati; vietata redistribuzione sorgente premium come libreria/ripubblicazione pubblica; nessun Pro importato |
| Stack originale | React, TypeScript, Tailwind v3/v4, shadcn, Radix o Base UI e `motion/react` in alcune componenti |
| Directory sorgente | [`registry/ruixenui`](https://github.com/ruixenui/ruixen.com/tree/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui) |
| Inventario tecnico | [277 file TSX enumerati, SHA blob Git](./RUIXEN_UI_REGISTRY_INVENTORY_2026-11-13.json) — filename esistente verificato, *non* test runtime |
| Campione approfondito | 8 file letti: `calendar-planner`, `three-dwall-calendar`, `color-picker-input`, `magic-tree`, `gooey-dock`, `magnetic-tabs`, `badge-morph`, `load-ripple` |
| Selezione App Factory | [41 componenti comparate](./RUIXEN_UI_CURATED_APP_MAP_2026-11-13.json) · **19 priorità A** e **22 B** · **18 app candidate** |

La documentazione ufficiale dichiara **240+ sezioni/componenti** nel catalogo free e supporto a quattro combinazioni Tailwind × primitive. L'inventario locale a questo commit comprende **277 file `.tsx`** nella directory di sorgenti: un file non coincide necessariamente con una voce UI pubblicata, quindi questi conteggi non sono equivalenti. Le sezioni marketing sono l'obiettivo primario dichiarato del prodotto; le App UI sono una raccolta secondaria. La variante Pro è separata e non va confusa con la licenza MIT del repository gratuito.

## Decisione tecnica

**Per Web / Next.js:** Ruixen è un riferimento di implementazione **potenzialmente copiabile** con condizioni MIT, ma solo dopo controllo di dipendenze, asset proprietari, API effettiva, build, qualità, accessibilità e licenze transitivi. `npx shadcn@latest add "https://ruixen.com/r/<componente>"` è il percorso ufficiale per l'installazione; non eseguirlo indiscriminatamente nel Design-App.

**Per Flutter:** trattare il codice come *specifica comportamentale visiva*, non come plug-in Flutter. Replicare in Dart usando Flutter widgets, AnimatedSwitcher / AnimatedContainer / Tween / AnimationController, CustomPainter solo se utile, Haptics opzionali e test widget/golden **della nostra implementazione**, non del riferimento React. Riutilizzare prima DS-005, DS-017, DS-025, DS-032, DS-034 e le capability già registrate, evitando nuove dipendenze se possibili.

**Per Kotlin/Compose esistenti:** stessa strategia di adattamento nativo (Material 3, Animatable/Transition APIs), senza migrazioni motivate solo dallo stile.

### Osservazioni dal campione sorgente reale

- `calendar-planner`: timeline verticale, eventi con interfaccia `events/onAdd/onRemove`, import `motion/react`. Pattern buono per schermate Ricordi/eventi; non sostituisce sync o data model di Anna.
- `three-dwall-calendar`: profondità delle pagine, hover/spring e AudioContext sintetico: efficace come riferimento, ma per Android touch e APK leggeri servono una versione semplificata e suono disabilitabile.
- `color-picker-input`: swatch, alpha e codice HEX, ma **non è la stessa cosa** del picker HSV 2D + Hue già concordato per Anna's Diary.
- `magic-tree`: `MagicNode`, stato `expanded`, selezione nodo: mappare su canvas/cartelle Notes; non assicura virtualizzazione di alberi grandi.
- `gooey-dock` e `magnetic-tabs`: effetto spring e audio tick opzionale/da evitare per default; comportamenti basati su hover non si trasferiscono direttamente al touch.
- `badge-morph`: espone stati idle/loading/success/error; è utile come feedback *semantico* oltre che estetico, con testo alternativo e fallback statico.
- `load-ripple`: anelli CSS temporizzati per caricamento; non deve soppiantare messaggi di stato né rimanere attivo inutilmente in background.

## 41 riferimenti selezionati, ordinati per dominio

### calendari

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-001 | [Calendar Planner](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-planner.tsx) | A | Anna's Diary, World Days, Wonderlog | Timeline editoriale verticale per eventi e ricordi; preservare viste approvate | Non sostituire il calendario core; ridurre movimento |
| RUX-002 | [Three Dwall Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/three-dwall-calendar.tsx) | B | Anna's Diary, World Days, Deskland Android | Calendario cartaceo 3D a profondità e cambio mese | Hover non disponibile su mobile; CPU/suono opzionale |
| RUX-003 | [Calendar Wave](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-wave.tsx) | A | Anna's Diary, World Days | Animazione calendario e transizioni di selezione giorno | Controllare riduzione movimento e contrasto |
| RUX-004 | [Calendar Lume](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-lume.tsx) | B | Anna's Diary, World Days | Calendario di tipo visual-editorial con gerarchia giorno | Non alterare la palette rose/colore attuale |
| RUX-005 | [Calendar Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-scheduler.tsx) | A | Anna's Diary, CamperBoss, Wonderlog | Slot temporali e planning contestuale | Fusi orari DST, sovrapposizione eventi, scalabilità |
| RUX-006 | [Event Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/event-scheduler.tsx) | A | Anna's Diary, World Days, CamperBoss | Gestione eventi/programma e dettagli contestuali | Preferire engine dati esistente; nessuna sostituzione sync |
| RUX-007 | [Range Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/range-calendar.tsx) | A | Anna's Diary, Wonderlog, CamperBoss, TrailPath | Selezione intervalli date per viaggio o ricordi | Test selezione inclusiva, fusi orari, tastiera |

### controlli

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-008 | [Drum Picker](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/drum-picker.tsx) | B | Anna's Diary, SleepMax Coach, Cooking Anime | Picker a tamburo tattile per data/ora o dosi | Evitare componenti critici troppo decorativi |
| RUX-009 | [Scrub Datetime](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scrub-datetime.tsx) | B | Anna's Diary, Wonderlog, SleepMax Coach | Modifica rapida di date e ore con scrub | Alternative accessibili a input manuale e swipe |
| RUX-026 | [Fine Tune Slider](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/fine-tune-slider.tsx) | A | FocusSense, BeerClass AI, SleepMax Coach, Battery Guard | Slider fine per parametri e valutazioni | Accoppiamento valore numerico e input accessibile |
| RUX-027 | [Circular Stepper Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/circular-stepper-input.tsx) | B | FocusSense, Cooking Anime, SleepMax Coach | Stepper circolare per quantità e punteggi | Non imporre precisione tramite gesture unica |

### dati

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-028 | [Spark Chart](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/spark-chart.tsx) | A | FocusSense, CashMate AI, Battery Guard, App Factory Dashboard | Micrografici inline e trend quantitativi | Asse/scala, fallback testuale, dati reali |
| RUX-029 | [Animated Number Flip](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-number-flip.tsx) | B | App Factory Dashboard, CashMate AI, FocusSense | Transizione cifra KPI e contatori | Rispettare prefers-reduced-motion, stabilità cifra |

### feedback

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-037 | [Confetti Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/confetti-button.tsx) | B | World Days, Cooking Anime, FocusSense | Microcelebrazione di successo/achievement | Solo eventi significativi; riduzione movimento |
| RUX-038 | [Load Ripple](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/load-ripple.tsx) | B | FocusSense, Battery Guard, SleepMax Coach | Ripple animato per stato di attesa | Mai sostituire testo di caricamento, limiti cicli |

### marketing

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-036 | [Banner Countdown](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/banner-countdown.tsx) | B | World Days, App Factory Dashboard, Cooking Anime | Countdown ricorrenze e timer/promozioni | Non invadente; timezone e frame budget |
| RUX-040 | [Glow Link Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glow-link-button.tsx) | B | App Factory Dashboard, World Days, Cooking Anime | CTA con microglow per landing web | Non trasformare utility in landing pubblicitaria |
| RUX-041 | [Gradient Hero Showcase](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gradient-hero-showcase.tsx) | B | App Factory Dashboard, World Days, Cooking Anime | Hero di presentazione per siti/landing | Solo pagine web, non UI funzionale mobile |

### media

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-030 | [Card Stack](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/card-stack.tsx) | A | Anna's Diary, Notes-Ecosistema, Wonderlog, World Days | Impilamento schede e swipe di contenuti | Gerarchia, indicatori, undo e navigazione accessibile |
| RUX-031 | [Image Card Fan](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/image-card-fan.tsx) | A | Anna's Diary, Wonderlog, FrameLab, Notes-Ecosistema | Ventaglio fotografico per ricordi/album | Non duplicare immagini originali, hit target e prestazioni |
| RUX-032 | [Glass Image Compare](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-compare.tsx) | A | FrameLab, Wonderlog, Notes-Ecosistema | Confronto immagini affiancato con reveal slider | Performance su immagini grandi e descrizioni alternative |
| RUX-033 | [Glass Image Editor](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-editor.tsx) | B | FrameLab, Notes-Ecosistema | Pannello editing su immagine con effetto vetro | Usare tool editing nativo già presente, non sostituirlo |
| RUX-034 | [Coverflow Carousel](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/coverflow-carousel.tsx) | B | Wonderlog, Anna's Diary, World Days | Carousel galleria coverflow a profondità | Disabilitare prospettiva per riduzione movimento |
| RUX-035 | [Scroll Portrait Wall](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scroll-portrait-wall.tsx) | B | Wonderlog, FrameLab, Notes-Ecosistema | Masonry fotorealistica con scroll e movimento | Non forzare scroll-jacking; lazy loading |
| RUX-039 | [Live Waveform](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/live-waveform.tsx) | B | FocusSense, The Luminous Infinite Circle, Deskland Android | Visualizzazione forma d'onda per audio/stati | Solo con segnale reale, permessi e basso consumo |

### motion

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-017 | [Gooey Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gooey-dock.tsx) | B | Deskland Android, Notes-Ecosistema, App Factory Dashboard | Dock a ingrandimento spring e prossimità | Touch e hover divergono; costi animazione; audio off |
| RUX-018 | [Morphing Expandable Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/morphing-expandable-menu.tsx) | B | Deskland Android, Notes-Ecosistema, FocusSense | Menu espandibile con morph e focus contestuale | Non nascondere navigazione principale, reduced motion |
| RUX-019 | [Magnetic Tabs](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magnetic-tabs.tsx) | B | Anna's Diary, Deskland Android, Notes-Ecosistema | Tab con indicatore magnetico e spring | Tab accessibili; non introdurre audio di default |

### navigazione

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-014 | [Nested Dashboard Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/nested-dashboard-menu.tsx) | A | App Factory Dashboard, Notes-Ecosistema, Deskland Android | Navigazione nidificata per moduli, donor, capability | Ciclo focus, profondità massima, mobile fallback |
| RUX-015 | [Toolbar Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/toolbar-dock.tsx) | A | Notes-Ecosistema, Deskland Android, App Factory Dashboard | Barra utensili/dock contestuale per canvas o launcher | Non oscurare canvas e aree touch |
| RUX-016 | [Floating Toolbar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/floating-toolbar.tsx) | A | Notes-Ecosistema, FrameLab, Deskland Android | Comandi contestuali sul documento/media | Tasti hit target, no overlay persistenti invasivi |

### palette

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-010 | [Color Picker Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-picker-input.tsx) | A | Anna's Diary, Notes-Ecosistema, Deskland Android, World Days | Swatch HEX e alpha; confronto con picker HSV già deciso | Non sostituire HSV 2D+Hue senza test; normalizzare HSL/HSV/HEX |
| RUX-011 | [Color Emotion Select](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-emotion-select.tsx) | B | Anna's Diary, Notes-Ecosistema, FocusSense | Selettore di colori con significato emotivo contestuale | Accessibilità e label indipendenti dal colore |

### status

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-020 | [Badge Morph](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/badge-morph.tsx) | A | App Factory Dashboard, CashMate AI, FocusSense, Battery Guard | Badge che cambia fra idle/loading/success/error | Stato espresso in testo e colore; niente animazione perenne |
| RUX-021 | [Notification Inbox Popover](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notification-inbox-popover.tsx) | A | App Factory Dashboard, World Days, CashMate AI | Inbox notifiche raggruppate e azioni rapide | Non creare notifiche non richieste, svuotamento e accessibilità |
| RUX-022 | [Notifications Filter](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notifications-filter.tsx) | B | World Days, App Factory Dashboard, CashMate AI | Filtro e raggruppamento per notifiche | Tracciare stato letto/non letto senza ambiguità |

### workflow

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-023 | [Add Task Sheet](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/add-task-sheet.tsx) | A | Notes-Ecosistema, Anna's Diary, App Factory Dashboard | Creazione task da bottom sheet e campi rapidi | Persistenza reale, salvataggio e perdita stato |
| RUX-024 | [Wizard Stepper](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/wizard-stepper.tsx) | B | Cooking Anime, World Days, Easy Debloat | Wizard progressivo per onboarding o procedure | Validazione step e ripresa, ridurre animazioni |
| RUX-025 | [Slide To Delete Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/slide-to-delete-button.tsx) | B | Notes-Ecosistema, BeerClass AI, CashMate AI | Swipe con affordance di cancellazione | UNDO/conferma per dati importanti |

### workspace

| ID | Sorgente (file pinned) | Priorità | App candidate | Opportunità | Caveat |
|---|---|:---:|---|---|---|
| RUX-012 | [Magic Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magic-tree.tsx) | A | Notes-Ecosistema, App Factory Dashboard, Deskland Android | Albero di cartelle/nodi, espansione animata, selezione | Virtualizzare liste grandi, comportamento tastiera |
| RUX-013 | [Motion File Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/motion-file-tree.tsx) | A | Notes-Ecosistema, App Factory Dashboard, Send-to-PC | Albero file con transizioni e selezione progressiva | Separare file-system reale da visual tree |


## Ricerca inversa: app → componenti candidati

### Anna's Diary

**A** · [RUX-023 Add Task Sheet](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/add-task-sheet.tsx) — Creazione task da bottom sheet e campi rapidi

**A** · [RUX-001 Calendar Planner](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-planner.tsx) — Timeline editoriale verticale per eventi e ricordi; preservare viste approvate

**A** · [RUX-005 Calendar Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-scheduler.tsx) — Slot temporali e planning contestuale

**A** · [RUX-003 Calendar Wave](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-wave.tsx) — Animazione calendario e transizioni di selezione giorno

**A** · [RUX-030 Card Stack](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/card-stack.tsx) — Impilamento schede e swipe di contenuti

**A** · [RUX-010 Color Picker Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-picker-input.tsx) — Swatch HEX e alpha; confronto con picker HSV già deciso

**A** · [RUX-006 Event Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/event-scheduler.tsx) — Gestione eventi/programma e dettagli contestuali

**A** · [RUX-031 Image Card Fan](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/image-card-fan.tsx) — Ventaglio fotografico per ricordi/album

**A** · [RUX-007 Range Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/range-calendar.tsx) — Selezione intervalli date per viaggio o ricordi

B · [RUX-004 Calendar Lume](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-lume.tsx) — Calendario di tipo visual-editorial con gerarchia giorno

B · [RUX-011 Color Emotion Select](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-emotion-select.tsx) — Selettore di colori con significato emotivo contestuale

B · [RUX-034 Coverflow Carousel](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/coverflow-carousel.tsx) — Carousel galleria coverflow a profondità

B · [RUX-008 Drum Picker](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/drum-picker.tsx) — Picker a tamburo tattile per data/ora o dosi

B · [RUX-019 Magnetic Tabs](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magnetic-tabs.tsx) — Tab con indicatore magnetico e spring

B · [RUX-009 Scrub Datetime](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scrub-datetime.tsx) — Modifica rapida di date e ore con scrub

B · [RUX-002 Three Dwall Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/three-dwall-calendar.tsx) — Calendario cartaceo 3D a profondità e cambio mese

### App Factory Dashboard

**A** · [RUX-023 Add Task Sheet](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/add-task-sheet.tsx) — Creazione task da bottom sheet e campi rapidi

**A** · [RUX-020 Badge Morph](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/badge-morph.tsx) — Badge che cambia fra idle/loading/success/error

**A** · [RUX-012 Magic Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magic-tree.tsx) — Albero di cartelle/nodi, espansione animata, selezione

**A** · [RUX-013 Motion File Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/motion-file-tree.tsx) — Albero file con transizioni e selezione progressiva

**A** · [RUX-014 Nested Dashboard Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/nested-dashboard-menu.tsx) — Navigazione nidificata per moduli, donor, capability

**A** · [RUX-021 Notification Inbox Popover](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notification-inbox-popover.tsx) — Inbox notifiche raggruppate e azioni rapide

**A** · [RUX-028 Spark Chart](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/spark-chart.tsx) — Micrografici inline e trend quantitativi

**A** · [RUX-015 Toolbar Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/toolbar-dock.tsx) — Barra utensili/dock contestuale per canvas o launcher

B · [RUX-029 Animated Number Flip](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-number-flip.tsx) — Transizione cifra KPI e contatori

B · [RUX-036 Banner Countdown](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/banner-countdown.tsx) — Countdown ricorrenze e timer/promozioni

B · [RUX-040 Glow Link Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glow-link-button.tsx) — CTA con microglow per landing web

B · [RUX-017 Gooey Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gooey-dock.tsx) — Dock a ingrandimento spring e prossimità

B · [RUX-041 Gradient Hero Showcase](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gradient-hero-showcase.tsx) — Hero di presentazione per siti/landing

B · [RUX-022 Notifications Filter](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notifications-filter.tsx) — Filtro e raggruppamento per notifiche

### Battery Guard

**A** · [RUX-020 Badge Morph](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/badge-morph.tsx) — Badge che cambia fra idle/loading/success/error

**A** · [RUX-026 Fine Tune Slider](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/fine-tune-slider.tsx) — Slider fine per parametri e valutazioni

**A** · [RUX-028 Spark Chart](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/spark-chart.tsx) — Micrografici inline e trend quantitativi

B · [RUX-038 Load Ripple](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/load-ripple.tsx) — Ripple animato per stato di attesa

### BeerClass AI

**A** · [RUX-026 Fine Tune Slider](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/fine-tune-slider.tsx) — Slider fine per parametri e valutazioni

B · [RUX-025 Slide To Delete Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/slide-to-delete-button.tsx) — Swipe con affordance di cancellazione

### CamperBoss

**A** · [RUX-005 Calendar Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-scheduler.tsx) — Slot temporali e planning contestuale

**A** · [RUX-006 Event Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/event-scheduler.tsx) — Gestione eventi/programma e dettagli contestuali

**A** · [RUX-007 Range Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/range-calendar.tsx) — Selezione intervalli date per viaggio o ricordi

### CashMate AI

**A** · [RUX-020 Badge Morph](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/badge-morph.tsx) — Badge che cambia fra idle/loading/success/error

**A** · [RUX-021 Notification Inbox Popover](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notification-inbox-popover.tsx) — Inbox notifiche raggruppate e azioni rapide

**A** · [RUX-028 Spark Chart](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/spark-chart.tsx) — Micrografici inline e trend quantitativi

B · [RUX-029 Animated Number Flip](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-number-flip.tsx) — Transizione cifra KPI e contatori

B · [RUX-022 Notifications Filter](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notifications-filter.tsx) — Filtro e raggruppamento per notifiche

B · [RUX-025 Slide To Delete Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/slide-to-delete-button.tsx) — Swipe con affordance di cancellazione

### Cooking Anime

B · [RUX-036 Banner Countdown](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/banner-countdown.tsx) — Countdown ricorrenze e timer/promozioni

B · [RUX-027 Circular Stepper Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/circular-stepper-input.tsx) — Stepper circolare per quantità e punteggi

B · [RUX-037 Confetti Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/confetti-button.tsx) — Microcelebrazione di successo/achievement

B · [RUX-008 Drum Picker](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/drum-picker.tsx) — Picker a tamburo tattile per data/ora o dosi

B · [RUX-040 Glow Link Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glow-link-button.tsx) — CTA con microglow per landing web

B · [RUX-041 Gradient Hero Showcase](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gradient-hero-showcase.tsx) — Hero di presentazione per siti/landing

B · [RUX-024 Wizard Stepper](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/wizard-stepper.tsx) — Wizard progressivo per onboarding o procedure

### Deskland Android

**A** · [RUX-010 Color Picker Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-picker-input.tsx) — Swatch HEX e alpha; confronto con picker HSV già deciso

**A** · [RUX-016 Floating Toolbar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/floating-toolbar.tsx) — Comandi contestuali sul documento/media

**A** · [RUX-012 Magic Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magic-tree.tsx) — Albero di cartelle/nodi, espansione animata, selezione

**A** · [RUX-014 Nested Dashboard Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/nested-dashboard-menu.tsx) — Navigazione nidificata per moduli, donor, capability

**A** · [RUX-015 Toolbar Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/toolbar-dock.tsx) — Barra utensili/dock contestuale per canvas o launcher

B · [RUX-017 Gooey Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gooey-dock.tsx) — Dock a ingrandimento spring e prossimità

B · [RUX-039 Live Waveform](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/live-waveform.tsx) — Visualizzazione forma d'onda per audio/stati

B · [RUX-019 Magnetic Tabs](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magnetic-tabs.tsx) — Tab con indicatore magnetico e spring

B · [RUX-018 Morphing Expandable Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/morphing-expandable-menu.tsx) — Menu espandibile con morph e focus contestuale

B · [RUX-002 Three Dwall Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/three-dwall-calendar.tsx) — Calendario cartaceo 3D a profondità e cambio mese

### Easy Debloat

B · [RUX-024 Wizard Stepper](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/wizard-stepper.tsx) — Wizard progressivo per onboarding o procedure

### FocusSense

**A** · [RUX-020 Badge Morph](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/badge-morph.tsx) — Badge che cambia fra idle/loading/success/error

**A** · [RUX-026 Fine Tune Slider](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/fine-tune-slider.tsx) — Slider fine per parametri e valutazioni

**A** · [RUX-028 Spark Chart](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/spark-chart.tsx) — Micrografici inline e trend quantitativi

B · [RUX-029 Animated Number Flip](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-number-flip.tsx) — Transizione cifra KPI e contatori

B · [RUX-027 Circular Stepper Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/circular-stepper-input.tsx) — Stepper circolare per quantità e punteggi

B · [RUX-011 Color Emotion Select](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-emotion-select.tsx) — Selettore di colori con significato emotivo contestuale

B · [RUX-037 Confetti Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/confetti-button.tsx) — Microcelebrazione di successo/achievement

B · [RUX-039 Live Waveform](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/live-waveform.tsx) — Visualizzazione forma d'onda per audio/stati

B · [RUX-038 Load Ripple](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/load-ripple.tsx) — Ripple animato per stato di attesa

B · [RUX-018 Morphing Expandable Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/morphing-expandable-menu.tsx) — Menu espandibile con morph e focus contestuale

### FrameLab

**A** · [RUX-016 Floating Toolbar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/floating-toolbar.tsx) — Comandi contestuali sul documento/media

**A** · [RUX-032 Glass Image Compare](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-compare.tsx) — Confronto immagini affiancato con reveal slider

**A** · [RUX-031 Image Card Fan](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/image-card-fan.tsx) — Ventaglio fotografico per ricordi/album

B · [RUX-033 Glass Image Editor](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-editor.tsx) — Pannello editing su immagine con effetto vetro

B · [RUX-035 Scroll Portrait Wall](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scroll-portrait-wall.tsx) — Masonry fotorealistica con scroll e movimento

### Notes-Ecosistema

**A** · [RUX-023 Add Task Sheet](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/add-task-sheet.tsx) — Creazione task da bottom sheet e campi rapidi

**A** · [RUX-030 Card Stack](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/card-stack.tsx) — Impilamento schede e swipe di contenuti

**A** · [RUX-010 Color Picker Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-picker-input.tsx) — Swatch HEX e alpha; confronto con picker HSV già deciso

**A** · [RUX-016 Floating Toolbar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/floating-toolbar.tsx) — Comandi contestuali sul documento/media

**A** · [RUX-032 Glass Image Compare](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-compare.tsx) — Confronto immagini affiancato con reveal slider

**A** · [RUX-031 Image Card Fan](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/image-card-fan.tsx) — Ventaglio fotografico per ricordi/album

**A** · [RUX-012 Magic Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magic-tree.tsx) — Albero di cartelle/nodi, espansione animata, selezione

**A** · [RUX-013 Motion File Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/motion-file-tree.tsx) — Albero file con transizioni e selezione progressiva

**A** · [RUX-014 Nested Dashboard Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/nested-dashboard-menu.tsx) — Navigazione nidificata per moduli, donor, capability

**A** · [RUX-015 Toolbar Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/toolbar-dock.tsx) — Barra utensili/dock contestuale per canvas o launcher

B · [RUX-011 Color Emotion Select](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-emotion-select.tsx) — Selettore di colori con significato emotivo contestuale

B · [RUX-033 Glass Image Editor](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-editor.tsx) — Pannello editing su immagine con effetto vetro

B · [RUX-017 Gooey Dock](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gooey-dock.tsx) — Dock a ingrandimento spring e prossimità

B · [RUX-019 Magnetic Tabs](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/magnetic-tabs.tsx) — Tab con indicatore magnetico e spring

B · [RUX-018 Morphing Expandable Menu](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/morphing-expandable-menu.tsx) — Menu espandibile con morph e focus contestuale

B · [RUX-035 Scroll Portrait Wall](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scroll-portrait-wall.tsx) — Masonry fotorealistica con scroll e movimento

B · [RUX-025 Slide To Delete Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/slide-to-delete-button.tsx) — Swipe con affordance di cancellazione

### Send-to-PC

**A** · [RUX-013 Motion File Tree](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/motion-file-tree.tsx) — Albero file con transizioni e selezione progressiva

### SleepMax Coach

**A** · [RUX-026 Fine Tune Slider](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/fine-tune-slider.tsx) — Slider fine per parametri e valutazioni

B · [RUX-027 Circular Stepper Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/circular-stepper-input.tsx) — Stepper circolare per quantità e punteggi

B · [RUX-008 Drum Picker](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/drum-picker.tsx) — Picker a tamburo tattile per data/ora o dosi

B · [RUX-038 Load Ripple](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/load-ripple.tsx) — Ripple animato per stato di attesa

B · [RUX-009 Scrub Datetime](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scrub-datetime.tsx) — Modifica rapida di date e ore con scrub

### The Luminous Infinite Circle

B · [RUX-039 Live Waveform](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/live-waveform.tsx) — Visualizzazione forma d'onda per audio/stati

### TrailPath

**A** · [RUX-007 Range Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/range-calendar.tsx) — Selezione intervalli date per viaggio o ricordi

### Wonderlog

**A** · [RUX-001 Calendar Planner](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-planner.tsx) — Timeline editoriale verticale per eventi e ricordi; preservare viste approvate

**A** · [RUX-005 Calendar Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-scheduler.tsx) — Slot temporali e planning contestuale

**A** · [RUX-030 Card Stack](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/card-stack.tsx) — Impilamento schede e swipe di contenuti

**A** · [RUX-032 Glass Image Compare](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glass-image-compare.tsx) — Confronto immagini affiancato con reveal slider

**A** · [RUX-031 Image Card Fan](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/image-card-fan.tsx) — Ventaglio fotografico per ricordi/album

**A** · [RUX-007 Range Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/range-calendar.tsx) — Selezione intervalli date per viaggio o ricordi

B · [RUX-034 Coverflow Carousel](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/coverflow-carousel.tsx) — Carousel galleria coverflow a profondità

B · [RUX-035 Scroll Portrait Wall](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scroll-portrait-wall.tsx) — Masonry fotorealistica con scroll e movimento

B · [RUX-009 Scrub Datetime](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/scrub-datetime.tsx) — Modifica rapida di date e ore con scrub

### World Days

**A** · [RUX-001 Calendar Planner](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-planner.tsx) — Timeline editoriale verticale per eventi e ricordi; preservare viste approvate

**A** · [RUX-003 Calendar Wave](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-wave.tsx) — Animazione calendario e transizioni di selezione giorno

**A** · [RUX-030 Card Stack](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/card-stack.tsx) — Impilamento schede e swipe di contenuti

**A** · [RUX-010 Color Picker Input](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/color-picker-input.tsx) — Swatch HEX e alpha; confronto con picker HSV già deciso

**A** · [RUX-006 Event Scheduler](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/event-scheduler.tsx) — Gestione eventi/programma e dettagli contestuali

**A** · [RUX-021 Notification Inbox Popover](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notification-inbox-popover.tsx) — Inbox notifiche raggruppate e azioni rapide

B · [RUX-036 Banner Countdown](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/banner-countdown.tsx) — Countdown ricorrenze e timer/promozioni

B · [RUX-004 Calendar Lume](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/calendar-lume.tsx) — Calendario di tipo visual-editorial con gerarchia giorno

B · [RUX-037 Confetti Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/confetti-button.tsx) — Microcelebrazione di successo/achievement

B · [RUX-034 Coverflow Carousel](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/coverflow-carousel.tsx) — Carousel galleria coverflow a profondità

B · [RUX-040 Glow Link Button](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/glow-link-button.tsx) — CTA con microglow per landing web

B · [RUX-041 Gradient Hero Showcase](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/gradient-hero-showcase.tsx) — Hero di presentazione per siti/landing

B · [RUX-022 Notifications Filter](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/notifications-filter.tsx) — Filtro e raggruppamento per notifiche

B · [RUX-002 Three Dwall Calendar](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/three-dwall-calendar.tsx) — Calendario cartaceo 3D a profondità e cambio mese

B · [RUX-024 Wizard Stepper](https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/wizard-stepper.tsx) — Wizard progressivo per onboarding o procedure


## Generatori e asset utili (indipendenti dal React runtime)

- [Glassmorphism Generator](https://ruixen.com/tools): generatori visivi glass con blur, trasparenza, bordo; trascrivere in design token senza copiare il CSS letteralmente nel Dart.
- [CSS Gradient Generator](https://ruixen.com/tools): estrazione e normalizzazione di stop/angoli/gradiente per stili personalizzabili.
- [Shadow Generator](https://ruixen.com/tools): elevazioni e shadow multilayer; attenzione a costi GPU, contrasto e dark mode.
- [Shadcn Theme Generator](https://ruixen.com/tools): design tokens light/dark; mappare a `ColorScheme` Flutter e token del Factory DS.
- [Ruixen Layouts](https://ruixen.com/layouts): composizioni pagina completa, ottime per una dashboard web App Factory, non copiare come app nativa.
- [Ruixen MCP](https://ruixen.com/docs/mcp): integrazione catalogo pensata per tool di sviluppo; connessione/attivazione non effettuata né necessaria per questo intake.

## Integrazione nelle app: priorità e gate

| Maxi-step | Ambito | Deliverable misurabile | Gate |
|---|---|---|---|
| 1 | Catalogazione | Ingest 277 sorgenti (solo metadati) + 41 selezioni (presente in Design-App) | Risoluzione URL, pin commit, licenza gratuita MIT distinta da Pro |
| 2 | Microinterazioni | Proof of concept `badge-morph`, `magnetic-tabs`, `load-ripple` in Flutter web/lab isolato | reduced motion, semantica, zero sound di default, stress 60 fps target |
| 3 | Anna / Notes | Studio `calendar-planner`, `magic-tree`, `color-picker-input` | Rispetto scelte UI, picker HSV già approvato, no perdita dati |
| 4 | Factory dashboard / World Days | Test `nested-dashboard-menu`, `spark-chart`, `banner-countdown` | Non confondere dashboard dimostrativa con dati reali, nessuna modifica colori World Days |
| 5 | Consolidamento | Trasformare i prototipi validati in DS donor o componenti condivise solo quando migliorano UI e mantenibilità | Test, license notice, benchmark, screenshot regression, API stabile; promuovere a `COPY_READY` solo con evidenze |

## Criteri di esclusione e rischi

1. Ruixen **non è Flutter-ready**: le 277 sorgenti sono TSX React; nessun pacchetto Dart o APK è stato generato.
2. `motion/react`, CSS, DOM, hover, Web Audio, gradients e canvas richiedono traduzione concettuale su Flutter: confrontare l'originale visivamente, non copiare API web.
3. Per app protette (Pocket Guard, Tabletop Motion Alarm) sicurezza e affidabilità precedono animazioni decorative. Non iniettare JS/CSS esterno in schermate critiche.
4. Per qualsiasi sorgente, controllare licenza MIT file-level e dipendenze: l'uso di foto, loghi, musica e altri asset del sito potrebbe richiedere autorizzazioni indipendenti.
5. Licenza **Pro** non assimilabile alla MIT; nessuna componente Pro copiata o vendorizzata.
6. Verifica funzionale non eseguita: la lettura di source e la disponibilità del file non dimostrano una build passing o un comportamento accessibile.
7. Con le modifiche di questo intake non si creano nuovi `UIR`, `DS`, `CAP` o Golden; si aggiungono solo una sorgente esterna e opportunità di riuso da valutare.

## Provenienza

Fonte ufficiale: sito, docs, GitHub e licenze di Ruixen UI, verificati il 13/11/2026; commit Git immutabile `f6b20860623fa39122ac2b5f0e5bd29a9eb10941`. Gli URL del catalogo live possono cambiare, ma i link al codice sorgente nel mapping puntano al commit fissato. Stato dei dati: **SOURCE_PATH_VERIFIED** per 277 file, **SAMPLE_CODE_READ** per 8, **INTERNAL_IMPLEMENTATION_NOT_VERIFIED** per tutti.
