# Factory Visual QA — Flutter v0.1.0

A **test-only** visual QA starter kit with a deterministic screen fixture and a
copyable test harness; no production UI framework or runtime graphics packages.

Coverage: 9 form-factor/accessibility scenarios × 5 UI states = **45 widget
matrix cases**. Plus four committed image snapshots covering phone light
content, phone dark empty, tablet content and large-font error.

The 9 scenarios cover:
- 360x800 small phone, 412x915 large phone, 800x1200 tablet, 800x360 landscape;
- dark palette, 1.6 and 2.0 text scale with long strings;
- keyboard inset of 250dp, top/bottom system safe-area padding;
- reserved 56dp banner slot plus navigation and FAB.

States: loading, content, empty, error, offline.

## Adoption

Copy `test/support/visual_matrix.dart` and adjust your app's own test matrix
to pass its real screen to `pumpVisualScenario(tester, scenario: ..., child: ...)`.
Keep your own theme, data factories, product-safe-area and localization.

Do **not** add the demonstration fixture to a shipping app: the fixture exists
only to prove the test tooling. A project's Product Bible and Golden Theme M3
remain authoritative for layout and styling. When using this repository via a
path dependency, keep `factory_visual_qa` under **dev_dependencies**.

```yaml
dev_dependencies:
  factory_visual_qa:
    path: ../Design-App/packs/visual-qa/flutter
```

The test harness deliberately lives in `test/support`, not in app runtime.
Copy the harness file into the consuming app's `test/support` folder
(no new runtime dependency); adapt `QaFixture` to your own screen. No heavy
Widgetbook or screenshot plugin is required in this initial kit.

## Run

```bash
cd packs/visual-qa/flutter
flutter pub get
flutter analyze lib test
flutter test test/visual_matrix_test.dart
flutter test test/visual_golden_test.dart
flutter test
```

The four PNG baselines under `test/goldens/` **are committed**.
They were created on Linux with Flutter **3.47.9** (Dart 3.13.7);
standard CI is pinned to this SDK. A Flutter engine upgrade requires deliberate
review and separate baseline approval.

The baselines Normal
CI never runs `--update-goldens`. A real pixel change fails with diff assets
in `test/failures`. Review the diff and justify any update in the PR.

Only when an intentional design change is approved:

```bash
flutter test --update-goldens test/visual_golden_test.dart
```

Review exact changed PNG files, their source/toolchain SHA, and commit them.
A one-time bootstrap workflow for this branch may seed the first baselines
with a controlled bot commit. After that, immutable snapshots are the oracle.

## What the tests do *not* prove

- Widget tests are not physical Android/iOS screenshots, screen-reader sessions
  or instrumented OS/IME/gesture/cutout tests.
- The demo tests only the demo fixture, not Anna, CamperBoss, Notes or any
  other consuming app; integration pilot must follow.
- Font rasterization may vary with Flutter engine, host OS or font assets.
  Keep baseline host Linux and Flutter version aligned.
- Passing a 45-case demo matrix alone does not guarantee every real app
  has correct insets, ad overlays, localization or offline recovery.
- Native Compose Paparazzi and SwiftUI snapshot harnesses are separate
  planned follow-ups and are not marked implemented.

More detail: `../PROVENANCE.md` and `../manifest/visual_matrix.json`.
