# React source preview — triage aggiornato (19 novembre 2026)

## Inventario verificato sul ramo PR #54
- **459/480** PNG presenti, con provenienza e hash verificati dal generatore; **21/480** senza PNG.
- Sui **119** UID della baseline congelata: **98 recuperati**, **21 con blocco individuale**.
- Residuo, senza duplicazioni: **1 React**, **10 Flutter Component Library**, **10 source/asset mancanti**.
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

## Unico blocco React residuo
| ID | Blocco verificato | Azione ammissibile |
|---|---|---|
| `RXN-glowing-send-input` | Sorgente originale richiede `next/font/google` e Poppins; import non risolvibile nel runtime Vite indipendente | Eseguire il componente nel runtime Next.js appropriato con font e licenza verificati, oppure ottenere screenshot upstream dell'esatto componente. Non sostituire font/TSX con stub, non considerare una UI riprodotta a mano come PNG sorgente |

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

**Stato:** 459 screenshot archiviate; la PR #54 resta aperta e non certificata visivamente.
