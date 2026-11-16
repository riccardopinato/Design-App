# GitHub Stars 750 — intake Design-App di 7 fonti visuali (16 novembre 2026)

Questo dossier integra 7 riferimenti nell’archivio Design-App. Sono **REFERENCE**, non nuovi stili personali, screenshot riutilizzabili, Golden, componenti compilati o permessi d'uso universali.
Fonte: [audit generale 110 nuove stelle](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/main/research/CLASSIFICA_CURATA_110_2026-11-16.md), [crosswalk con OSS95](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/main/research/INCROCIO_OSS95_2026-11-16.md). Baseline Factory `c5adc147046beb7024629466d10eeb799c3c2619`.

| Fonte e HEAD immutabile | Pattern | Applicazione primaria | Licenza/gate |
|---|---|---|---|
| [tldraw/tldraw](https://github.com/tldraw/tldraw/tree/9751764b0f69aa8cd22d5e2021b778132a6f7ed5) | Canvas extensible: shapes, gestures, media, snapping and runtime API | Notes-Ecosistema | REFERENCE_ONLY; SDK licensing gate |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw/tree/82190fb28f58070b34b4017e70c0e2e83701a8e3) | Hand-drawn canvas, shape library and mobile interaction | Notes-Ecosistema | MIT CODE ONLY AFTER PER-FILE REVIEW |
| [xyflow/xyflow](https://github.com/xyflow/xyflow/tree/0814ffa1b23bb29048b329c03c211f335bdd6571) | Interactive graphs, node edges, agent/workflow layout | App Factory Control Center | MIT; React/Svelte/Vue, not native Flutter |
| [markmap/markmap](https://github.com/markmap/markmap/tree/c09e4837c0ee5428c02e65cc728c1daf28ee1ec0) | Markdown to editable/viewable mindmaps, SVG/canvas rendering and export | Notes-Ecosistema | MIT; native Flutter conceptual rewrite |
| [alztrk/OpenWidget](https://github.com/alztrk/OpenWidget/tree/7c8ff5aad7a77b34c952c9c66d4077039754dbb1) | Floating Windows widget, hotkey, adaptive size, game-mode activity reduction | App Factory Control Center | MIT; Windows native only |
| [AppFlowy-IO/appflowy-editor](https://github.com/AppFlowy-IO/appflowy-editor/tree/01eccc6ee36bd07698bd80915289fe7070478cd2) | Flutter rich-text block components, selection, slash shortcuts and toolbar | Notes-Ecosistema | README dual AGPL-3.0/MPL-2.0, require legal/file review |
| [sorenwacker/nodus](https://github.com/sorenwacker/nodus/tree/14f1ff6e43a95d9a29eec8eb3fb718af4049b56c) | Canvas-as-document, linked PDF highlights, citations, storylines | Notes-Ecosistema | NOASSERTION / reference-only |

## Opportunità di progetto

**Notes-Ecosistema:** combinare canvas e blocchi con ID oggetto canonici, editor ricco senza perdita su import/export Markdown, mindmap derivate dalle note, PDF evidenziati come riferimenti. Prima confrontare CAP-0028, CAP-0029, CAP-0098, CAP-0149, CAP-0161 e il codice realmente in `main`; non aggiungere un secondo engine di canvas o sync.

**App Factory Control Center:** vista nodi/collegamenti per dipendenze build, stage CI, agenti e blocchi (xyflow), eventualmente widget Windows locale per stato PR/CI (OpenWidget) soltanto con dati GitHub verificati. Non far partire servizi/cookie/polling autonomi senza consenso.

**Deskland Android:** dall’OpenWidget Windows prendere soltanto policy di HUD e visibilità e riduzione consumo in gioco; non trasferire Win32, WPF e hook di taskbar al Flutter/Kotlin wallpaper.

**Anna's Diary:** nessuna nuova architettura proposta. Le priorità restano l’estetica iOS Journal e le feature già censite; pattern editor e widget richiedono gate prodotto.

## Provenienza e licensing

- `tldraw`: README/documentazione API canvas verificati; metadata SPDX NOASSERTION, SDK soggetto a licenza/prodotto separati: **REFERENCE_ONLY**.
- `AppFlowy Editor`: README dichiara dual-license AGPL-3.0 / MPL-2.0, non assumere MIT. Eventuali copy richiedono audit file e compatibilità.
- `Nodus`: metadata GitHub NOASSERTION; nessun copia codice senza LICENSE controllata.
- `OpenWidget`, `Excalidraw`, `xyflow`, `Markmap`: GitHub metadata MIT, ma controllare file/dependencies/assets e termini branding prima di importare; Flutter nativo richiede adattamento originale.
- Zero codice o asset esterni aggiunti; zero test d’implementazione consumer, zero livelli SOURCE_VERIFIED/LIBRARY_VERIFIED.

## Gate di avanzamento

Se viene approvato un singolo pattern: confrontare Product Bible e codice consumer HEAD, definire delta misurabile, implementare su PR isolata, visual QA, accessibilità, reduced-motion, performance, test exact-head e collaudo fisico dove necessario. Conservare commit e file source nel provenance ledger.
