# Factory Motion Flutter — provenance ledger

componentId: PACK-MOTION-FLUTTER
componentVersion: 0.1.0
originType: NEW_IMPLEMENTATION
owner: riccardopinato / App Factory
factoryBaseline: riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25
sourceRepo: riccardopinato/Design-App
sourcePath: packs/motion/flutter
sourceRef: this PR's merge commit when available
sourceLicense: first-party original code; Design-App repository license not asserted
externalCodeCopied: false
reuseScope: Flutter Android/iOS/Web presentation widgets
adaptationSummary: Native framework state transitions with shared timing and OS accessibility policy
dependenciesAdded: Flutter SDK only; flutter_test for test
securityNotes: No I/O, telemetry, permissions, network, assets or persisted data
licenseNotes: MIT/BSD external donors were *consulted*, not imported or vendored
testsExecuted: To be filled from exact-head CI evidence
evidenceRefs: To be filled after validation
status: IMPLEMENTED_PENDING_VALIDATION
verifiedAt: null

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

- Flutter analyze of package.
- Flutter widget tests of effect variants, reduced motion, accessibility,
  selection minimum touch size, completion badge, skeleton and dark mode.
- Example package analysis.
- CI exact-head PASS, followed by main post-merge PASS.
- Physical-device and consuming-app size certification: NOT VERIFIED.

A green source-app test is **not** evidence for this separately extracted package.
