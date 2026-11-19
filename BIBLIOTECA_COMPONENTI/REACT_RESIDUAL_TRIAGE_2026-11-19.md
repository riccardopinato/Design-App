# React source preview — triage aggiornato (19 novembre 2026)

## Inventario verificato sul ramo PR #54
- **460/480** PNG presenti, con provenienza e hash verificati dal generatore; **20/480** senza PNG.
- Sui **119** UID della baseline congelata: **99 recuperati**, **20 con blocco individuale**.
- Residuo, senza duplicazioni: **0 React**, **10 Flutter Component Library**, **10 source/asset mancanti**.
- I PNG isolati da TSX originali sono **`UNREVIEWED` nel Visual QA**: acquisizione fisica e SHA non dimostrano fedeltà o compatibilità con Flutter.
- I codici originali TSX, Dart, SVG e il doppio catalogo codice originale / Flutter sono rimasti separati e immutati.
- Factory baseline di questa lavorazione: `14722698bf92e80c526f5f1f211c8d694ce01fb9` (CURRENT / Master v27 / Golden Index v29).

## React risolti dal checkpoint 446/480
L'ultima diagnosi browser mostrava cache Vite `?v=` divergenti tra ReactDOM e componenti Framer/Radix. La soluzione verificata è una lista esplicita di `optimizeDeps.include` **con discovery dinamica attiva**, due acquisizioni concorrenti al massimo e le versioni Motion pin (`motion-dom 12.23.9`, `motion-utils 12.23.6` per `framer-motion 12.23.11`). I workflow recuperano solo sorgenti originali con checksum; le primitive Ruixen ausiliarie vengono dall'esatto commit MIT pinnato.

Le **13 catture React** aggiunte dopo il precedente checkpoint 446 sono:
- `RXN-video-text`: testo mascherato dal **video reale riprodotto dal componente TSX**, con `MediaStream` da canvas procedurale locale e gate su video + mask; non è una demo ufficiale con footage originale.
- `RXN-scrub-datetime`: contrasto corretto del testo bianco originale su sfondo scuro e inquadratura dei due controlli reali.
- `AMX-004`, `DBM-002`, `RXN-behavioral-history-select`, `RXN-carousel-3d-select`, `RXN-command-deck`, `RXN-file-tree`, `RXN-package-installer-tabs`, `RXN-ruixen-query-box`: source renders con API-specific fixtures.
- `AMX-002`, `DBM-011`, `DBM-016`: CursorTrail reale dopo evento mouse, MorphLoader scalato con i suoi parametri, Skeleton con dimensioni esplicite. Non sono immagini sostitutive.

## Ultimo React — recuperato e registrato

`RXN-glowing-send-input` è ora **risolto come anteprima documentale**. La pipeline source-only
`next_source_renderer` esegue l'originale TSX immutato nel runtime Next.js 16, con la
dipendenza originale `next/font/google` / Poppins effettivamente caricata, e dipendenze
Motion allineate. Il browser ha prodotto il PNG verificato e il manifest ha superato
tutti i gate di sorgente, font, hash e registro UID.

- Immagine fisica: `docs/assets/componenti/RXN-glowing-send-input.png`
- Fonte: Ruixen MIT, commit `f6b20860623fa39122ac2b5f0e5bd29a9eb10941`, blob `a7a0d3dd2785d9a708a5d8a654637547af2fa235`
- Evidenza: `BIBLIOTECA_COMPONENTI/ANTEPRIME_ORIGINI.json` — `PINNED_ORIGINAL_TSX_NEXTJS_RENDER`
- CI della cattura e pubblicazione: **PASS** GitHub Actions, cattura del 19/11/2026
- QA visivo: **UNREVIEWED**; ammissione Flutter/consumer: **NOT_VERIFIED**

## Recupero mirato Uiverse con CSS animato

Dal controllo dei **15 casi near-flat** dei 110 UID Uiverse, **14 PNG sono state
rigenerate** con animazioni CSS reali in esecuzione, non con animazioni
congelate al primo frame. I soli wrapper della cattura sono stati adattati
per contrasto, viewport e isolamento dei livelli; gli HTML/CSS originali non
sono stati modificati. Sui 14 casi è stata osservata una crescita misurabile
della deviazione standard dei pixel. La quindicesima, `UIV-088`, rimane
inalterata perché l'effetto originale è un piccolo switch neumorfico
volutamente poco contrastato e il test non ha dimostrato un miglioramento
sufficiente: non si inventa un restyling.

Registro prima/dopo per ogni UID:
`BIBLIOTECA_COMPONENTI/UIVERSE_LOWCONTRAST_RECOVERY.json`.
Sono **14 sostituzioni migliorative**, non 14 immagini in più nel catalogo.
La verifica di fedeltà visiva resta **UNREVIEWED**.

## Blocchi non React
- **10 FCL**: nove demo ufficiali non espongono contenuto direttamente catturabile e Book Shelf rimanda alla pagina errata; fonte/reference note, **nessuna PNG generica**. Registro `RECUPERO_119_ESITI.json` per ID.
- **10 fonti/asset**: originali di 9 componenti terzi non sufficientemente identificati e 1 immagine personale non allegata. Ogni ID è spiegato in `SOURCE_TRIAGE_10.md`; nessuna ricostruzione fittizia o attribuzione MIT non provata.

## Gate residui per PR/consumer
1. QA visivo umano/analisi schermate effettive per le PNG marcate `UNREVIEWED`, in particolare le catture dinamiche e i casi visivamente quasi uniformi. Non confondere screenshot presente con fedeltà approvata.
2. CI `push` e `pull_request` **sullo stesso HEAD** dopo ogni nuovo commit. I run `action_required` e i vecchi PASS non provano il nuovo HEAD.
3. Conservare SHA e manifest storici del renderer ogni volta che cambia `package.json` per non invalidare la provenienza delle PNG precedenti.
4. Nessuna promozione di componenti a `COPY_READY`, Golden o consumer Flutter senza codice nativo, test e adozione validata. Merge solo con i gate tecnici e autorizzativi realmente soddisfatti.

## Evidenza machine-readable e sorgenti
- `BIBLIOTECA_COMPONENTI/ANTEPRIME.json`
- `BIBLIOTECA_COMPONENTI/RENDER_ARCHIVED_TSX_BATCH_REPORT.json`
- `BIBLIOTECA_COMPONENTI/RECUPERO_119_ESITI.json` e `.md`
- `BIBLIOTECA_COMPONENTI/SOURCE_TRIAGE_10.md`
- `BIBLIOTECA_COMPONENTI/ruixen_renderer/vendor/ruixen/PROVENANCE_PINNED_UI.md`

**Stato:** 460 screenshot archiviate, 20 non disponibili con causa nominativa; PR #54 aperta, QA visivo e approvazione consumer ancora non certificati.
