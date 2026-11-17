# Amicro — audit 6 componenti richiesti (17/11/2026)

**Base verificata:** [repository originale Amicro](https://github.com/Subhan-code/Amicro--Micro-transitions-/tree/fa5f8ffbe39537a8db191806066b8773c47c82e9) @ `fa5f8ffbe39537a8db191806066b8773c47c82e9`, licenza **MIT** nel file LICENSE root; ogni dipendenza e asset richiede controllo autonomo. I sei URL DevLibraries sono stati provati direttamente ma non caricabili nel browser disponibile; denominazioni user-supplied confrontate con file del repository originale. Dove manca corrispondenza esatta, lo dichiariamo apertamente.

| Componente richiesto | Evidenza sorgente | Riuso consentito al momento |
|---|---|---|
| [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) | [`src/components/css-animations/physics/CurtainReveal.tsx`](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/src/components/css-animations/physics/CurtainReveal.tsx) (blob `60ec9f5d9b996301899fc75be9ed4d029fc5ac80`; export `Curtain`) | `REFERENCE_ONLY` / `PROPOSED_ONLY` |
| [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) | [`registry/ui/cursor/cursor-trail.tsx`](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/cursor/cursor-trail.tsx) (blob `df9715526996a0ae36731125e12a69807627ad93`; export `CursorTrail`) | `REFERENCE_ONLY` / `PROPOSED_ONLY` |
| [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) | Nessun file del componente con nome esatto identificato nel commit fissato | `REFERENCE_ONLY` / `PROPOSED_ONLY` |
| [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) | [`registry/ui/scroll/scroll-reveal.tsx`](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/scroll/scroll-reveal.tsx) (blob `548a9ddff684ed94574f537a24820d5871e419d8`; export `ScrollReveal`) | `REFERENCE_ONLY` / `PROPOSED_ONLY` |
| [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) | Nessun file del componente con nome esatto identificato nel commit fissato | `REFERENCE_ONLY` / `PROPOSED_ONLY` |
| [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) | [`registry/ui/loading/accordion-loader.tsx`](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/accordion-loader.tsx) (blob `de8a6b9ded9d668daf5da92e8eee829f4c18e1f3`; export `AccordionLoader`) | `REFERENCE_ONLY` / `PROPOSED_ONLY` |

## Dettaglio del comportamento dedotto dal codice (solo dove presente)

- **CurtainReveal:** componente React `Curtain` con interazione hover/click, keyframe CSS e loop di showcase di default. Adattare a durata finita, focus e trigger espliciti.
- **Cursor Trail:** ascolta `mousemove` a livello finestra e crea punti con spring seguendo il cursore. Condizionare a fine pointer e reduced motion; evitare oneri CPU in background. Non ha significato operativo per touch Android.
- **Scroll Reveal:** `whileInView`, fade + offset e scala in ingresso, `once:true`. Evitare di far rientrare contenuti o animare valori critici.
- **Accordion Loader:** `AccordionLoader` con quattro barre che animano `scaleX` e loop ogni 1,5 s con ritardo; è un *indeterminate loader*, non restituisce progresso numerico.
- **Perspective Flip / Spatial Door Portal:** il concetto di flip/porta spaziale discende dalle etichette inviate. Non è dimostrata una loro implementazione specifica nel repository; verificare sorgente originale prima di copiature, CLI o test di qualità.

## Product e QA gate

1. Ogni app mantiene identità, Golden, navigazione e scelta di design autorizzata nella Product Bible; i link sono idee da testare.
2. Flutter: riusare prime `AnimatedSwitcher`, `AnimatedOpacity`, `AnimatedSize`, `SlideTransition`, `RotationTransition` / `CustomPainter` solo se necessario; Compose: `AnimatedVisibility`, `AnimatedContent`, `animate*AsState`. Niente porting diretto dei file TSX.
3. Preferire animazioni piccole, terminate, semanticamente motivate. Fermare loop non visibili; rispettare reduced motion, contrasto, 48 dp e long-text/font-scale.
4. Loader: partire da stato backend/IO reale, timeout/error/retry e percentuale solo se misurabile. Non mascherare operazioni lente con movimenti infiniti.
5. Web: verificare prestazioni sulla viewport, mouse/touch e accessibilità tastiera; Cursor Trail non è per touch.

**Stato:** 4 sorgenti individuate, 2 denominazioni non verificate, 0 consumer aggiornati, 0 asset copiati, 0 componenti certificati.

## Rettifica documentale sul precedente intake Amicro

Ulteriore ricerca nel **medesimo commit** ha permesso di identificare i file effettivi di Card Stack Peel, Accordion Blind Pull, Interlocking Gear Step e Shutter Step Slices che il primo audit descriveva soltanto come metadata di catalogo. La rettifica della provenienza va riportata nel vecchio registro: `SOURCE_FILE_READ` significa file **letto**, non code review, test, compatibilità Flutter o COPY_READY.
