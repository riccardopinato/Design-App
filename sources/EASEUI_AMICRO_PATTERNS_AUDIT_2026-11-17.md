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
| Card Stack Peel | `anim-card-peel` | `card-stack-peel` | Descrizione 3D peel, file source specifico non trovato |
| Accordion Blind Pull | `anim-blind-pull` | `accordion-blind` | Lamelle a tendina, file source specifico non trovato |
| Interlocking Gear Step | `anim-gear-step` | `gear-tooth-step` | Ingranaggi sincronizzati, file source specifico non trovato |
| Shutter Step Slices | `anim-shutter-blocks` | `shutter-step-slices` | Lamelle orizzontali in sequenza, file source specifico non trovato |

Il repo contiene **un diverso** componente `registry/ui/loading/gears.tsx` (blob `6cd0bcd36518813d9a3910c1d20a76ab3e99df7f`), ma **non è prova** che Interlocking Gear Step sia già disponibile con quel nome o qualità. Non eseguire CLI senza validare output e dipendenze.

## Protocollo di eventuale adattamento

- Flutter: preferire `ThemeMode` + `ColorScheme`, `AnimatedSwitcher`, `AnimatedSize`, `SlideTransition`, `AnimatedRotation`, `ExpansionTile`, senza aggiungere Motion/React.
- Compose: `MaterialTheme`, `AnimatedContent`, `AnimatedVisibility`, `animate*AsState`, animazioni native.
- Loading: `0–300 ms` senza spinner se possibile; attese brevi con feedback non invasivo, attese più lunghe con skeleton/spinner sobrio; percentuale solo se misurata; timeout/error/retry, non spinner infinito.
- Accessibilità: label, focus, 48 dp, riduzione movimento, contrasto scuro/chiaro, orientamento e font scaling; non occultare contenuti o rompere touch/gesture.
- Performance: loop solo in foreground/visibile e con lavoro reale; evitare GPU costosa, benchmark peso APK e FPS su device prima dell'adozione.

**Esito:** uno script EaseUI realmente letto e 4 voci Amicro metadata-only; un nuovo riferimento grafico dall'immagine dell'utente. Nessuna integrazione, Golden, asset o licenza extra automatica.
