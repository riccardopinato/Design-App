# Design-App — doppio codice per UID

Il file `FLUTTER_VARIANTS.json` espone per ciascuno dei **480 UID**:

- **Codice originale**: file TSX, HTML/CSS oppure Dart esistente, con riferimento e licenza originali.
- **Codice Flutter**: file Dart fisico separato (quando già convertito), oppure uno stato verificabile di conversione mancante.
- **Stato e gate**: `ADAPTER_DRAFT_UNVERIFIED_CONSUMER`, `NATIVE_DART_DEPENDENCY_GATE`, `PENDING_FLUTTER_REWRITE`, `SOURCE_NOT_ARCHIVED`.

**Non si cancella o sovrascrive nessun originale.** Il porting Flutter è una riscrittura controllata, non una trascrizione automatica JSX→Dart: si conservano funzionalità UX, motion e stati con API/semantica Flutter, rispettando il design già approvato per la singola app.

I primi tre file Dart sono in `flutter_adapters/`. Per i due Forui già nativi il link Flutter punta al Dart originale: il pacchetto è riutilizzabile solo dopo valutazione di Flutter 3.50+, dipendenze, font, dimensione e test nell'app. Per gli altri componenti la cella Flutter rimane **Da convertire** o **Sorgente originale non disponibile**.

Processo per le wave successive: codice sorgente e licenza → studio del comportamento e screenshot → file Flutter affiancato → widget test e flutter analyze → confronto visivo e accessibilità → consumer pilot → eventuale riuso copy-ready verificato. Una stessa conversione può servire più app, senza modificare la fonte originale.

La colonna Flutter del catalogo è un riferimento al file Dart completo, non una copia parziale dei frammenti nel Markdown. Non dichiarare porting completo né compliance production prima dei rispettivi gate.

## Gentleface native source intake

The official Gentleface website exposes MIT SVG originals and full Flutter/Dart `CustomPainter` widgets, discoverable at `/icons/<slug>.md`. The source intake stores **28 SVG originals** and **28 native Dart files** separately with independent SHA256 and official URLs; these are **live-source hashes, not pinned Git commit SHA**. The original source and native Dart must never overwrite each other. This package is not a verified app consumer or Golden by itself.
