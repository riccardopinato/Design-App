# App Factory Icon Adapter Pack v0.1.0

**Status: implemented; final COPY_READY decision depends on exact-head CI.**

A canonical list of 24 semantic UI icon keys used in Flutter and Jetpack
Compose. This is an *adapter*, not a third-party icon library.

## Design

- Canonical source of truth: `manifest/icons.json`.
- Deterministic generator: `python3 manifest/generate.py`.
- Drift validator: `python3 manifest/generate.py --check`.
- One default family: **Material Icons Filled (core)**.
- No copied SVGs, image files or custom font binaries.
- Flutter uses icons from the Flutter SDK.
- Compose uses explicit `material-icons-core` (small core set, 1.7.3 in JVM harness).
- No `material-icons-extended` dependency; apps must include core icons explicitly when not already present.
- IDs are stable API identifiers: do not rename or recycle them.

Semantic IDs: add, back, calendar, call, check, close, delete, edit,
favorite, home, info, location, lock, mail, menu, more, notifications,
person, refresh, search, settings, share, star, warning.

These icons represent *concepts*, not pre-translated user-facing words.
Apps must pass localized accessible labels to interactive controls. Decorative
instances should not create redundant screen-reader announcements.

## Flutter

`flutter/` is a standalone Flutter package named `factory_icons`.
It offers `FactoryIconKey`, `FactoryIcon`, `FactoryIconButton`.
Copy into an app or use a checked-out local path dependency:

```yaml
dependencies:
  factory_icons:
    path: ../Design-App/packs/icons/flutter
```

```dart
FactoryIconButton(
  icon: FactoryIconKey.calendar,
  tooltip: appLocalizations.openCalendar,
  onPressed: openCalendar,
)
```

Buttons require a nonempty localized tooltip and use a minimum 48dp
interactive target. Passive status icons can accept a localized
`semanticLabel`, while decorative icons leave it null.
Theme colors, icon sizing and screen density are governed by the app theme.

## Jetpack Compose

`compose/` contains the Kotlin adapter and a standalone Gradle JVM harness.
Integrate `GeneratedFactoryIconKeys.kt` and `FactoryIconWidgets.kt`
into an existing Compose app. The Gradle harness uses Compose Material and
Material3 and does not introduce a new icon graphics engine.

```kotlin
FactoryIconButton(
    key = FactoryIconKey.CALENDAR,
    contentDescription = stringResource(R.string.open_calendar),
    onClick = ::openCalendar,
)
```

The `back` icon uses the auto-mirrored Compose arrow for RTL locales.
The consuming app owns the actual navigation and localization.

## Validation

```bash
python3 manifest/generate.py --check
python3 -m unittest discover -s manifest -p 'test_*.py'
cd flutter && flutter pub get && flutter analyze lib test && flutter test
cd ../compose && gradle --no-daemon test
```

CI runs Flutter analyzer/widget tests/showcase, Compose Kotlin compile/JVM
tests and deterministic generator/schema checks. A passing CI establishes
library-level correctness only; production app integration and physical
rendering are separate evidence gates.

## Palette and licensing

Only the standard Material core icon family is used, avoiding different
visual weights within one app. Apps can opt for another *whole* family later
via a separate adapter; they should not mix families arbitrarily.

The Material icon source is [google/material-design-icons](https://github.com/google/material-design-icons),
observed at commit `10ecc14790612ca8fd164e3f4ffe9c16fc50d5b7`,
licensed **Apache-2.0**. No source icons were copied from GitHub.
The actual images are resolved through the Flutter/AndroidX frameworks
already declared by each consumer. See `PROVENANCE.md`.

## Known limitations

- Visual similarity does not imply pixel-identical rendering across SDKs.
- Material glyph sets can evolve when Flutter or AndroidX versions change;
  pin the app toolchain and run the snapshot/visual-qa suite when upgrading.
- Compose JVM tests do not prove real Android TalkBack/large-text/raster
  behavior; native device verification is still required for certification.
- Current implementation is the **filled** family only, not per-icon outline
  alternates, icon packs, colors or icon artwork creation.
