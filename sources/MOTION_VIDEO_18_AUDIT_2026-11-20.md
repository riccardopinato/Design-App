# Audit completo: 18 fonti motion, VFX, video e audio — 20/11/2026

**18 input:** 17 repository GitHub + **1 servizio API (Openverse)** con repository GitHub ufficiale `WordPress/openverse` individuato e verificato. **Nessun duplicato repo esatto nel registro OSS precedente**. Baseline `App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835`, Master 27 / Golden Index 31 / Golden Registry 2, Design-App base `c34483036b2ca5ad068e9568a3a8ce3b6294296f`.

## Provenienza realmente controllata

- **18/18 README** letti dal repository effettivo e poi verificati anche al commit immutabile; i 18 README SHA blob corrispondono tra default branch e commit.
- **17/18 file LICENSE** della fonte letti. **Eccezione: `remotion-dev/skills`** non espone `LICENSE` né `LICENSE.md` nella root; e' stato verificato il file speciale `remotion-dev/remotion/LICENSE.md` relativo al runtime, ma questo non prova automaticamente la licenza riuso delle singole skill. Trattare queste skill come REFERENCE fino a verifica termini.
- **0** componenti copiati, **0** nuove UID, **0** asset/audio/video/font vendorizzati, **0** skill installate, **0** modifiche a Golden/Donor e consumer. Stato `REFERENCE` e ogni associazione `PROPOSED_ONLY`.

## Tabella delle fonti e limiti

| ID | Repo/API | Categoria | Licenza letta (con eccezioni) | Utilita' concreta | Avvertenze |
|---|---|---|---|---|---|
| MOTION-OSS-001 | [reanimate](https://github.com/NiazMorshed2007/reanimate) | AGENT SKILL | MIT | Reverse-engineer authorized video/Web/GIF/Lottie motion; Bun, browser, FFmpeg; Windows untested | Third-party visual identity and underlying animation remain separately protected |
| MOTION-OSS-002 | [motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | AGENT SKILL | MIT | Motion director intent, easing, timing, state and choreography principles | Implementation-agnostic; no Dart widgets or runtime API included |
| MOTION-OSS-003 | [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | VIDEO STYLE REFERENCE | MIT_ORIGINAL | 15 ten-second films, prompts, full source and rendering harness | Third-party fonts, glyph outlines and audio assets retain separate licenses |
| MOTION-OSS-004 | [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | ART EXPLAINER SKILL | MIT_CODE_DOCS_EXCEPTIONS | 36 art styles, nine explainer grammars, eight parametrized scene types | Arphic stroke data, SIL OFL fonts, artworks, mascot rights separately licensed |
| MOTION-OSS-005 | [anidoodle](https://github.com/alexgreensh/anidoodle) | CODE DRAWN ART | Apache-2.0 | Code-based doodle illustrations, looping Web art and scored films | Node/Playwright/FFmpeg production, not Flutter widget |
| MOTION-OSS-006 | [cinetic](https://github.com/Leonxlnx/cinetic) | VIDEO PRODUCTION SKILL | MIT_ORIGINAL | Agent-driven product launch and update films with brief, shots, music, QA and render | Remotion engine has separate commercial terms; all music/image assets individually licensed |
| MOTION-OSS-007 | [motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | VIDEO QUALITY SKILL | Apache-2.0_ORIGINAL | Agent taste and technical quality review for code-rendered motion graphics | NOTICE: bundled GSAP uses GreenSock Standard No Charge license; third-party dependencies not Apache |
| MOTION-OSS-008 | [manim](https://github.com/ManimCommunity/manim) | EDUCATIONAL VIDEO | MIT_DUAL_AUTHORS | Python equations, charts and animated educational explainers | Not realtime Flutter charts; renderer dependencies and accuracy validation |
| MOTION-OSS-009 | [blender-skills](https://github.com/EL4CTEO/blender-skills) | DESKTOP 3D SKILL | MIT | 28 Blender agent skills, Blender 5.2 LTS+; 5.3 recommended | PC render-only; no Blender runtime shipped on Android |
| MOTION-OSS-010 | [three.quarks](https://github.com/Alchemist0823/three.quarks) | WEB3D CODE DONOR | MIT | High-performance Web Three.js/TS particle emitter library | WebGL and GPU/battery overhead; needs native Flutter rewrite |
| MOTION-OSS-011 | [react-postprocessing](https://github.com/pmndrs/react-postprocessing) | WEB3D CODE DONOR | MIT | React Three Fiber postprocessing effects for Web 3D scenes | Web ecosystem only; visual access, readability and power guards |
| MOTION-OSS-012 | [tweakpane](https://github.com/cocopon/tweakpane) | DEVELOPER TOOL | MIT | Dependency-free JavaScript live parameter tuning panel | Prototype/editor only; do not ship debug controls by default |
| MOTION-OSS-013 | [effectcraft](https://github.com/storytold/effectcraft) | DESKTOP COMPOSITING | MIT_OR_APACHE-2.0_CODE | Rust video compositor with effect stack and presets, young project | Brand marks carved out; NOTICE/ATTRIBUTION assets separately licensed |
| MOTION-OSS-014 | [openverse](https://api.openverse.org/v1/) | MEDIA SEARCH API | MIT_CODE_ONLY; MULTIPLE_CC_PD_MEDIA | Openverse media search API https://api.openverse.org/v1/ for images and audio, credit/license fields | Every result has separate permissions; CC NC/ND assets may not fit commercial/derivative video |
| MOTION-OSS-015 | [librosa](https://github.com/librosa/librosa) | OFFLINE AUDIO ANALYSIS | ISC | Python audio MIR beat, tempo and onset analysis | Tempo estimates require checking; PC workflow, not phone runtime |
| MOTION-OSS-016 | [whisperX](https://github.com/m-bain/whisperX) | OFFLINE TRANSCRIPTION | BSD-2-Clause_CODE | Word-level forced alignment/optional diarization and transcription | Not perfect timecodes; model/pyannote permissions; privacy and hardware demands |
| MOTION-OSS-017 | [skills](https://github.com/remotion-dev/skills) | VIDEO AGENT SKILLS | NO_LICENSE_AT_SKILLS_ROOT; REMOTION_RUNTIME_CUSTOM | Official Remotion Agent Skills for code-driven React video production | No LICENSE/LICENSE.md found in skills root; engine Free/Company license not equivalent to MIT |
| MOTION-OSS-018 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | MULTIMEDIA TOOLCHAIN | LGPL-2.1+; GPL_OPTIONAL | Command line and library video/audio/codec/subtitle conversion and export | Actual binary build/codec license can impose GPL; local CLI separate from app redistribution |

[Manifest JSON con source commit e licenze](./MOTION_VIDEO_18_REGISTRY_2026-11-20.json) · [Matrice di 68 proposte su 13 app](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md) · [Pipeline](./MOTION_VIDEO_18_PIPELINE_2026-11-20.md).

## Verifica delle affermazioni originarie

- **`reanimate`** e' una skill che analizza il movimento da sito, MP4, GIF, Lottie o screenshot, da browser e frame. Non concede il diritto di clonare ogni animazione trovata online; i riferimenti originali, marchi, immagine coordinata, font e asset mantengono diritti separati. Requisiti: Bun 1.1+, macOS/Linux, Windows non testato nella documentazione.
- **`LottieFiles/motion-design-skill`** e' un insieme di principi, regole temporali e easing, non un SDK per Flutter. Priorita' molto alta per *interaction design*, ma dipendenze leggere e native vengono prima dei motori video.
- **`mg-styles-15`** effettivamente mostra 15 film da dieci secondi con prompt, source e renderer. Codice/prompts originali MIT; font/glyph sotto licenze come SIL OFL e file di terzi non diventano MIT.
- **`huashu-art-motion`** nella README corrente dichiara **36** stili artistici, non 35, con 9 grammatiche explanatory. Code/docs MIT, ma font SIL OFL, dati Arphic Public License e personaggi/illustrazioni non coperti dalla MIT.
- **`anidoodle`** codice Apache-2.0, produzione di artwork/doodle e video tramite browser e FFmpeg. Non e' un widget Dart o un asset pronto per app.
- **`cinetic`** crea filmati di lancio e aggiornamento da brief con QA; motore Remotion, musica e media richiedono licenze specifiche, nonostante l'originale skill sia MIT.
- **`motionmaxxing`** e' Apache-2.0 per il lavoro originale, ma `NOTICE` menziona **GSAP** (GreenSock Standard No Charge; licenza non open-source) e altri componenti/font con licenze autonome. Non trattare l'intero albero come Apache-2.0.
- **`Manim`** e' una libreria Python per grafici/formule/video e non una libreria di grafici Flutter; **Blender Skills** richiede Blender >=5.2 LTS (5.3 consigliato).
- **`three.quarks`** e **`react-postprocessing`** sono librerie Web Three.js/React Three Fiber, utili a prototipi 3D ma non importabili direttamente in Android/Flutter.
- **`Tweakpane`** serve a regolare parametri di prototipi JS, non a fornire i settings di produzione dell'app.
- **`EffectCraft`** e' uno strumento desktop Rust, pubblicato nel 2026; licenza originale dual MIT/Apache-2.0, ma `NOTICE` e `ATTRIBUTION.md` proteggono marchi, font e altri asset. Non e' un plugin Flutter pronto.
- **Openverse**: `https://api.openverse.org/v1/` e' API di ricerca di media aperti. **Il codice di `WordPress/openverse` e' MIT, le tracce/foto trovate NON sono MIT**. Verificare licenze CC0/CC BY/NC/ND caso per caso, autori, sorgenti, condizioni commerciali, eventuali campioni e attribuzioni. Una risposta API e' discovery, non certificazione di diritti.
- **`librosa`** (ISC) analizza tempo/onset/music information retrieval, con risultati da valutare e tempo di produzione; non richiede installazione sullo smartphone.
- **`WhisperX`** (BSD-2-Clause sul codice) offre trascrizione + forced alignment opzionale; sincronizzazione **non garantita al millisecondo** e trascrizioni/lingue richiedono QA, soprattutto contenuti medici. Modelli e speaker diarization (pyannote) hanno termini, accessi e privacy separati.
- **`remotion-dev/skills`** documenta best practices React/Remotion; **nessun LICENSE root rintracciato**. Il motore Remotion applica *Free License* e *Company License* in base all'uso/organizzazione; non dichiarare «MIT». Vedere https://www.remotion.dev/docs/license/pricing e https://www.remotion.dev/docs/terms.
- **`FFmpeg`** ha principalmente LGPL 2.1+, parti opzionali GPL: la licenza applicabile dipende dai flag e dai codec della build, specie se binari inclusi/distribuiti. Vedere https://www.ffmpeg.org/legal.html.

## Integrazione con le fonti gia' approvate da Design-App

Librerie Flutter motion **gia' presenti** in `registry/OSS_DESIGN_SOURCES.yaml`: `gskinner/flutter_animate` (composable motion), `xvrh/lottie-flutter`, `LottieFiles/dotlottie-flutter`, `rive-app/rive-flutter`. Questo lotto aggiunge **tooling produzione/regia e fonti di riferimento**, non sostituisce le opzioni piu' leggere native. La gerarchia rimane Golden/Donor interno → Design-App → nuovo OSS solo se necessario.

Il valore principale per la App Factory e' un processo di **visual QA e regia ripetibile**, con modelli di contenuto/diritti e produzioni video occasionali, senza gonfiare APK o introdurre dipendenze GPU/AI nei telefoni. La priorita' visiva dell'utente salvata nel repo Design-App prevale sui suggerimenti generici esterni, sempre entro a11y e regole tecniche.

## Distinzione di licenza e copyright

**Il titolo promozionale «copy any animation I see» e' una descrizione marketing, non una licenza**: si possono studiare e ricostruire idee generali di motion, con sorgente propria e diritti compatibili, ma non presumere legittimita' di clonazione pixel-perfect, asset protetti, filmati altrui, tracce musicali o marchi. Non scaricare massivamente visual da siti per addestramento/archivio senza condizioni. Ogni source code/asset import futuro ha un gate separato e traccia di provenienza.

## Riferimenti di verifica aggiuntivi

- https://github.com/Tejashmakwana/motionmaxxing/blob/main/NOTICE (GSAP e assets)
- https://github.com/storytold/effectcraft/blob/main/ATTRIBUTION.md (asset e marca)
- https://github.com/alchaincyf/huashu-art-motion/blob/main/README.en.md (36 stili e licenze eccezioni)
- https://api.openverse.org/v1/ (API), https://github.com/WordPress/openverse (codice)
- https://www.remotion.dev/docs/license/pricing (Remotion), https://www.ffmpeg.org/legal.html (FFmpeg)
