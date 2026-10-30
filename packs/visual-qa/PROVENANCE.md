# Factory Visual QA Kit — provenance

componentId: PACK-VISUAL-QA
componentVersion: 0.1.0
originType: NEW_IMPLEMENTATION
factoryBaseline: riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25 (Master v27 ACTIVE)
goldenReference: golden/ui/GOLDEN_APP_SHELL_RESPONSIVE_VISUAL_QA_FLUTTER_v1_DRAFT.txt
goldenStatus: DRAFT (not certified)
sourceProjectOrRepo: riccardopinato/Design-App
externalSourcesConsulted: cashapp/paparazzi; pointfreeco/swift-snapshot-testing; widgetbook/widgetbook
externalCodeCopied: false
externalAssetFilesCopied: false
flutterRuntimeExternalDependencies: 0
flutterTestDependencies: flutter_test (Flutter SDK)
format: Linux Flutter golden pixel snapshots plus layout/semantics assertions
flutterVersion: 3.47.9
dartVersion: 3.13.7
goldenInitialCommit: 8388e31f5cdce514bcf4492f1f45b5bc3b62ada3
goldenInitialWorkflow: https://github.com/riccardopinato/Design-App/actions/runs/41059220975
goldenBaselineFiles: 4 (under packs/visual-qa/flutter/test/goldens/)
targetsImplemented: Flutter test harness, 9 form-factor scenarios, 5 states
targetsPlanned: Compose Paparazzi / SwiftUI snapshot harness
physicalDeviceEvidence: NOT VERIFIED
consumerAppIntegration: NOT VERIFIED
status: LIBRARY_VERIFIED
verifiedAt: 2026-10-30
testedSourceSha: 32350363e8b82fc5dad94c2a5b1e94787794cc27
testsExecuted: flutter pub get; flutter analyze lib test; 45-state matrix; 4 PNG golden pixel comparisons; full flutter test; example analyze; repository structural validation
evidence:
  - https://github.com/riccardopinato/Design-App/actions/runs/41059634636
  - https://github.com/riccardopinato/Design-App/actions/runs/41059634257
evidence: To be recorded after exact-head PR CI and committed baselines

Use this pack to verify screen behavior, not to claim a design was approved.
To become COPY_READY, the 4 reference PNGs must be committed, and the exact
head must pass matrix tests and real comparison against unchanged PNGs.
A subsequent consumer-app pilot and physical/device verification remain
separate levels under the App Factory evidence ladder.
