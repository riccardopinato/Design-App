# Gentleface — audit delle icone animate (17/11/2026)

## Fonte e perimetro letto

- Link richiesto: https://gentleface.com/categories/animated
- Pagina ufficiale di dimostrazione: https://gentleface.com/animated-icons
- Guida codice e varianti: https://gentleface.com/use
- Catalogo singoli asset: https://gentleface.com/icons/{slug} (metadati: https://gentleface.com/icons/{slug}.json)
- Motion index dichiarato dal sito: https://gentleface.com/motion/index.json
- Licenza dichiarata sul sito: **MIT per le icone Gentleface**; al momento i bytes ZIP/SVG e la LICENSE allegata **non sono stati importati o verificati localmente**.
- Integrazione catalogo: **REFERENCE**; è un sito esterno, non è stato individuato e pin-nato un repository sorgente GitHub di questa specifica collezione.

La pagina ufficiale principale al 17 novembre riporta circa **4.035** icone statiche e **1.000** animate, ma altre pagine indicizzate della demo riportano **500** animate: il numero è variabile e disallineato tra pagine, quindi non viene registrato come inventario verificato. Il catalogo app include soltanto 28 candidati selezionati su base semantica, **non** una scansione esaustiva di tutte le icone.

## Cosa fornisce la fonte

- SVG statici su griglie pixel 16/20/24, varianti line/solid e corner round/soft/sharp; esempi di codice anche Flutter e Jetpack Compose per le **icone statiche**.
- Sottoinsieme animato come **SVG con animazione nativa SMIL/embedded**, senza libreria JS necessaria nel file SVG; web inline con helper optional per play, stop e toggle.
- Dimostrazioni: click, hover/focus (web), due stati, stato in corso, form, menu; fallback in posizione di riposo.
- Attribuzione/notice MIT da conservare in caso di copia, test di diritti per altri asset eventualmente distribuiti nello ZIP.

## Compatibilità tecnica

| Piattaforma | Impiego | Gate |
|---|---|---|
| Web/PWA | Potenzialmente diretto: SVG inline/locale + helper per play/pause, aria-label sull'azione, prefer-reduced-motion, pause offscreen | Test browser/device, offline, CSP/asset sanitization e licensing |
| Flutter Android/iOS | La scheda Flutter del sito mostra **icona statica**, non prova che SMIL funzioni con flutter_svg. Preferire icona vettoriale statica + `AnimatedSwitcher`/`AnimationController` e animazione semantica nativa. Valutare renderer SMIL solo con benchmark motivato. | Test widget, GPU, a11y, riduzione movimento, peso APK, test fisico |
| Android Jetpack Compose | Il sito espone ImageVector statico; per animazioni usare APIs Compose o AnimatedVectorDrawable/AnimatedImageVector (non import SMIL diretto per analogia). | Native Android correctness e lifecycle, TalkBack, risparmio energetico |
| Security/alarm status | Animazione solo dopo verifica stato reale; no finto scudo animato di default | Flag/servizio effettivo, fail-safe sempre statico/testo |

## Criteri pratici

1. Trigger evento: animation **una volta** dopo azione riuscita; toggle per play/pause, bookmark, occhio (se la sorgente dispone della coppia corretta).
2. Loop solo per carica, ricerca o trasferimento **realmente attivi e visibili**; sospendere offscreen, in background, quando disabilitati e con reduced-motion.
3. Niente animazione su ogni tap o su tutte le icone della bottom navigation; dare priorità a fluidità dell'app e semantica.
4. Le icone devono avere fallback statico e nome accessibile/localizzato nel bottone; una animazione non deve essere la sola spiegazione di loading/success/error.
5. In Flutter/Compose privilegiare l'Icon Adapter Pack già presente. Solo dopo test, eventuale modulo `AnimatedFactoryIcon` con lo stesso semantic ID e mapping a Gentleface.
6. Non aggiungere runtime JS/React in Flutter; non scaricare da CDN in app local-first. L'asset (se licenziato) va incluso localmente con versionamento e checksum.

## Cosa è stato verificato / non verificato

- **Verificato come documentazione pubblica:** esistenza sito e schede, dichiarazione MIT, formato e esempi del provider, varianti statiche, alcuni controlli «Copy animated SVG».
- **Non verificato:** bytes degli SVG animati, timing e capacità di pausa per ognuna delle 28 icone, qualità visiva effettiva su Flutter/Compose, piani di rilascio, test reali, footprint APK, pubblicazione asset.
- **Non importato:** 0 file SVG, 0 PNG, 0 package, 0 Golden, 0 risorse o licenze di terzi redistribuite.

## Fonti

1. [Demo Gentleface animated](https://gentleface.com/animated-icons)
2. [Gentleface pagina principale](https://gentleface.com/)
3. [Come usare Gentleface](https://gentleface.com/use)
4. [Documentazione ufficiale Android AnimatedImageVector](https://developer.android.com/develop/ui/compose/resources)
5. [Libreria Icon Adapter interna](../packs/icons/README.md)
