# Audit sorgente — EaseUI e Amicro (17 novembre 2026)

## Riferimenti utente

- [EaseUI su DevLibraries](https://devlibraries.com/libraries/easeui): tema chiaro/scuro.
- [Amicro Card Stack Peel](https://devlibraries.com/libraries/amicro/card-stack-peel): transizione di schede/sezioni.
- **Accordion Blind Pull**: apertura a tendina (correzione esplicita rispetto al link duplicato).
- **Interlocking Gear Step**: per caricamento.
- **Shutter Step Slices**: comparsa a tendina/sezioni.
- **Screenshot aggiuntivo in chat**: altri caricamenti/tempi di attesa, senza identificazione affidabile del file originale: nessun file incorporato o dichiarato scaricato.

## Evidenza sorgente e licenze

**EaseUI**: `rjcuff/easeui` commit `8292b45cc31d17b824d1caed6867b8f60428822a`, file `components/motion/theme-toggle.tsx` blob `69d6711aa860b3784fa5a27f3dcad925baa333ed`, LICENSE root **MIT** (compresa l'attribuzione aggiuntiva nel notice); prodotto easeUI Pro separato. Il sorgente espone `circle` / `ripple`, `startViewTransition`, `next-themes`, fallback senza API e `useReducedMotion`. È React Web, non Flutter; il Golden Theme M3 esistente resta la fonte per tema effettivo Light/Dark/System, preferenze, colori e token.

**Amicro**: `Subhan-code/Amicro--Micro-transitions-` commit `fa5f8ffbe39537a8db191806066b8773c47c82e9`, LICENSE root **MIT**. Tutti i quattro nomi richiesti sono presenti nel file `src/data/cssAnimationsData.ts`, blob `396fda2c071064e4dce29290ac088f35f8bdab3a`:

| Nome | ID catalogo | CLI dichiarata | Stato effettivo |
|---|---|---|---|
| Card Stack Peel | `anim-card-peel` | `card-stack-peel` | Descrizione 3D peel, SOURCE_FILE_READ: `src/components/css-animations/physics/MechanicalPhysicsTrios.tsx` · export `CardStackPeel` · blob `012685b393beaa846136e155b38016c63cd4f122` |
| Accordion Blind Pull | `anim-blind-pull` | `accordion-blind` | Lamelle a tendina, SOURCE_FILE_READ: `src/components/css-animations/physics/ElasticVariations.tsx` · export `BlindPull` · blob `18e083c97e6ef82f49b86e7538623a4d347b79b8` |
| Interlocking Gear Step | `anim-gear-step` | `gear-tooth-step` | Ingranaggi sincronizzati, SOURCE_FILE_READ: `src/components/css-animations/physics/ElasticDeformTrios.tsx` · export `GearToothStep` · blob `6c93dcbb1857d3b7e0579c9ea96eaa1f5af92bc6` |
| Shutter Step Slices | `anim-shutter-blocks` | `shutter-step-slices` | Lamelle orizzontali in sequenza, SOURCE_FILE_READ: `src/components/css-animations/physics/InertiaPhysicsExperiments.tsx` · export `ShutterStepBlocks` · blob `a266bc0021a4c9f400f81328356cc6f5a2a18812` |

Il repo contiene **un diverso** componente `registry/ui/loading/gears.tsx` (blob `6cd0bcd36518813d9a3910c1d20a76ab3e99df7f`), ma **non è prova** che Interlocking Gear Step sia già disponibile con quel nome o qualità. Non eseguire CLI senza validare output e dipendenze.

## Protocollo di eventuale adattamento

- Flutter: preferire `ThemeMode` + `ColorScheme`, `AnimatedSwitcher`, `AnimatedSize`, `SlideTransition`, `AnimatedRotation`, `ExpansionTile`, senza aggiungere Motion/React.
- Compose: `MaterialTheme`, `AnimatedContent`, `AnimatedVisibility`, `animate*AsState`, animazioni native.
- Loading: `0–300 ms` senza spinner se possibile; attese brevi con feedback non invasivo, attese più lunghe con skeleton/spinner sobrio; percentuale solo se misurata; timeout/error/retry, non spinner infinito.
- Accessibilità: label, focus, 48 dp, riduzione movimento, contrasto scuro/chiaro, orientamento e font scaling; non occultare contenuti o rompere touch/gesture.
- Performance: loop solo in foreground/visibile e con lavoro reale; evitare GPU costosa, benchmark peso APK e FPS su device prima dell'adozione.

**Esito aggiornato:** cinque sorgenti implementative lette (EaseUI + quattro Amicro) e un riferimento grafico dall'immagine dell'utente. Nessuna integrazione, Golden, asset o licenza extra automatica.

## Rettifica di provenienza — seconda verifica 17/11/2026

La prima ricognizione aveva registrato erroneamente i quattro effetti come soli record di catalogo. L'analisi ampliata del repository **al medesimo commit** ha individuato i file e le funzioni indicati nella tabella. La precedente valutazione è conservata qui come storico di una verifica incompleta, ma non rappresenta più lo stato tecnico corrente. **`SOURCE_FILE_READ` non equivale a compilazione, test, disponibilità Flutter o `COPY_READY`.** Nessun componente è stato importato nelle app. [Dettaglio successivo e nuovi pattern Amicro](./AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md).
