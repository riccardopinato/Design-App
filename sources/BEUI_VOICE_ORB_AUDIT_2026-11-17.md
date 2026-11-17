# beUI Voice Orb — audit della reference (17 novembre 2026)

**Scoperta:** [DevLibraries / Voice Orb](https://devlibraries.com/libraries/beui/voice-orb). La pagina esatta non era direttamente caricabile; è stata verificata tramite la directory indicizzata e le fonti ufficiali beUI.

## Sorgenti originali fissate

- **Web:** [beUI](https://beui.dev/components/agents/voice-orb) — repository `starc007/ui-components` @ `498eaba3a046181e4da7d867aac6b226e89f8ce9`.
  - `components/agents/voice-orb.tsx` — Git blob `bc67b2bd6a8b1ed329cdd624463672e85cacbce1`.
  - `components/agents/voice-orb/renderer.ts` — Git blob `83ce7ea141baba0685fb8ed319768a8726b85bba`.
- **React Native:** [beUI Native](https://beui.dev/react-native/voice-orb) — repository `starc007/beui-native` @ `ab3e58aa751bffccb725208db2c3740eb2bf643b`.
  - `src/components/voice-orb/README.md` — blob `36db5018630fb8f72d42de0f671c92ce42ea03aa`.
- **Licenza:** MIT nei due repository ufficiali, con obbligo di conservare copyright e notice in caso di riuso. **Le risorse beUI Pro sono distinte**.

## Cosa fa davvero

Voice Orb è una rappresentazione visiva di un livello audio normalizzato da 0 a 1. Il componente Web espone `activity`, `analyser` facoltativo fornito dall'app, `colors`, `active`, `speed`, `onError`. Disegna una sfera liquida con shader canvas/WebGL e sospende il rendering in condizioni non visibili o in errore; prevede riduzione del movimento e fallback. La versione mobile usa React Native, Reanimated e Skia.

**Non acquisisce il microfono, non registra, non salva e non trascrive audio.** Permessi, recorder, file, privacy, STT/TTS e playback sono funzionalità separate dell'app.

## Adattamento consigliato

Per Flutter: pattern visivo riproducibile con `CustomPainter` e `AnimationController` o widget simile, dopo benchmark di FPS e peso APK; evitare dipendenze grafiche pesanti per un effetto decorativo. Per Compose: canvas/animazioni native. Web React: considerare sorgente originale dopo dependency admission e test.

Gli stati minimi sono: `idle`, `permission_denied`, `recording`, `paused`, `processing`, `saved`, `playback`, `error`. **L'orb deve muoversi soltanto quando riceve audio reale mentre è visibile.** Ogni stato richiede testo accessibile, durata, controlli, fallback statico e reduced-motion; non basta cambiare colore. Niente animazioni GPU continue in background.

**Classificazione:** `UI_UX_REFERENCE`, `REFERENCE`, `PROPOSED_ONLY`. Nessuna app consumer modificata. Nessun componente Flutter, APK o test runtime realizzato da questo intake.

**Mappa:** [App candidate](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md) · [Origine DevLibraries](./DEVLIBRARIES_DISCOVERY_2026-11-17.md).
