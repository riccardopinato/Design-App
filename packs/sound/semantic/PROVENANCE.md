# Semantic Sound Pack — provenance ledger

componentId: PACK-SOUND-SEMANTIC
componentVersion: 0.1.0
originType: OSS_COPIED (6 CC0 unchanged WAV assets) + NEW_IMPLEMENTATION (Flutter control/adapter code)
factoryBaseline: riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25 (Master v27 ACTIVE)
sourceProjectOrRepo: wyzowl/sfx-kit
sourceRefOrCommit: 92780e7ab0cdfb557497a988089c47f46e8c7412
sourcePath: sounds/interface; sounds/notifications
sourceLicense: CC0-1.0 — LICENSE-CC0.txt
manifest: packs/sound/semantic/manifest.json
localFiles: packs/sound/adapters/flutter/assets/*.wav
externalRuntimeDependency: bluefireteam/audioplayers tag audioplayers-v6.5.1 (MIT)
sourceCodeCopied: No; only WAV assets were copied
testsExecuted: Python manifest SHA256/Git SHA1/WAV validation; flutter pub get; flutter analyze lib test; flutter test; example flutter pub get/analyze; Design-App registry validator
evidenceRefs: https://github.com/riccardopinato/Design-App/actions/runs/41049437359 ; https://github.com/riccardopinato/Design-App/actions/runs/41049437240
status: LIBRARY_VERIFIED
verifiedAt: 2026-10-30

## Adaptation summary

- Exactly six short WAV sounds selected; no full 320-item donor pack imported.
- Asset bytes preserved: Git blob SHA and SHA-256 recorded per file.
- Filenames normalized to six stable semantic IDs.
- Playback default OFF; explicit opt-in and a conservative volume.
- Flutter adapter isolated so apps that do not need sound stay dependency-free.
- Screen-reader, user settings persistence, OS audio focus and notifications
  remain owned by the consuming application.

## Known limitations

- WAVE PCM mono 48 kHz/24-bit sound decoder support needs real-device QA.
- Perceived loudness and output timing have not been measured on devices.
- No cross-app production integration or APK footprint measurement.
- Critical alarm reliability explicitly outside scope.
- CC0 license information is tracked and includes verbatim donor license text.
