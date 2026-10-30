# Factory Motion Flutter — provenance ledger

componentId: PACK-MOTION-FLUTTER
componentVersion: 0.1.0
originType: NEW_IMPLEMENTATION
owner: riccardopinato / App Factory
factoryBaseline: riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25
sourceRepo: riccardopinato/Design-App
sourcePath: packs/motion/flutter
sourceRef: ed3382fc82d25065b15712be2d243e32cf20ef1d (package-tested PR head)
sourceLicense: first-party original code; Design-App repository license not asserted
externalCodeCopied: false
reuseScope: Flutter Android/iOS/Web presentation widgets
adaptationSummary: Native framework state transitions with shared timing and OS accessibility policy
dependenciesAdded: Flutter SDK only; flutter_test for test
securityNotes: No I/O, telemetry, permissions, network, assets or persisted data
licenseNotes: MIT/BSD external donors were *consulted*, not imported or vendored
testsExecuted: flutter pub get; flutter analyze lib test; flutter test --reporter expanded; example flutter pub get; example flutter analyze lib; Design-App registry validation
evidenceRefs: https://github.com/riccardopinato/Design-App/actions/runs/41044887710 ; https://github.com/riccardopinato/Design-App/actions/runs/41044887705
status: COPY_READY
verifiedAt: 2026-10-30

## Design lineage (ideas only)

- Internal donor: Anna's Diary / FrameLab — restrained 120–260ms functional
  transitions, semantic colors, accessibility, low-noise UI.
- Factory rule: GOLDEN_THEME_M3_FLUTTER_v1 and
  GOLDEN_APP_SHELL_RESPONSIVE_VISUAL_QA_FLUTTER_v1_DRAFT.
- GitHub reference: gskinner/flutter_animate@62c12040b1e3f80403b4fbfa48649155df006eb5
  (BSD-3-Clause). No source code copied; tiny framework-native solution preferred.
- GitHub reference: xvrh/lottie-flutter@a662621ae02998cf3482a6b8619ec05d63f2eebd
  (MIT). No dependency or vector assets copied.
- GitHub reference: rive-app/rive-flutter@6f853e45d380f5b2bfccc893b08037e03e292a3b
  (MIT). No dependency or animations copied.

## Open verification

- [PASS CI] Flutter analyze of package.
- [PASS CI] Flutter widget tests of effect variants, reduced motion, accessibility,
  selection minimum touch size, completion badge, skeleton and dark mode.
- [PASS CI] Example package analysis.
- [PASS CI] Exact initial package head ed3382fc82d25065b15712be2d243e32cf20ef1d.
- [REQUIRED] Final metadata-head PR CI and merged-main CI must also pass.
- [NOT VERIFIED] Physical-device and consuming-app size certification.

A green source-app test is **not** evidence for this separately extracted package.
