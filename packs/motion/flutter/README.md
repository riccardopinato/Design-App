# Factory Motion — Flutter v0.1.0

**Status: COPY_READY at library level** (Flutter analyze, widget tests, example
analysis and registry validation passed on the pinned package source SHA).
This is **not** cross-app, physical-device or Play-release certification.
See `PROVENANCE.md` for exact CI evidence.

Small, dependency-free UI motion primitives for Flutter applications.
Built for App Factory's Material 3 baseline; works with app-specific themes.

## Included

| Widget | What it does |
| --- | --- |
| `MotionSwap` | Fade, fade-scale, fade-slide between keyed UI states |
| `MotionExpand` | Animated expand/collapse; hidden controls are removed from tree |
| `MotionSelectionTile` | 48dp-minimum touch area, selected surface state |
| `MotionCompletionBadge` | Visual + spoken success feedback with localized semantics |
| `MotionSkeleton` | Static, dimension-matched loading placeholders |
| `MotionHero` | Opt-out Hero flights for reduced-motion users |
| `FactoryMotionPolicy` | Respect `disableAnimations` and `accessibleNavigation` |
| `FactoryMotionTokens` | Feedback 160 ms, standard 220 ms, emphasized 260 ms |

The pack intentionally **does not** bundle Lottie, Rive, image assets,
custom fonts, audio players or a theme replacement.

## Integration

From an app repository, declare a local/path dependency to this directory:

```yaml
dependencies:
  factory_motion:
    path: ../Design-App/packs/motion/flutter
```

The path is illustrative: use the actual relative path in your environment.
If the app must be buildable without a sibling checkout, vendor this *bounded*
package under the app repository with provenance, or publish a properly versioned
internal package. Do not depend on a floating Git branch in release builds.

Import:

```dart
import 'package:factory_motion/factory_motion.dart';
```

State swap example:

```dart
MotionSwap(
  motionKey: loading,
  effect: FactoryMotionEffect.fadeSlide,
  child: loading
      ? const MotionSkeleton(width: 240, height: 56)
      : const Text('Content ready'),
)
```

Expand/collapse example:

```dart
MotionExpand(
  expanded: expanded,
  child: const Text('Details'),
)
```

App-specific localization is required when using
`MotionCompletionBadge(semanticLabel: ...)`.

## Demo and tests

```bash
cd packs/motion/flutter
flutter pub get
flutter analyze lib test
flutter test

# Example source is independently analyzed:
cd example
flutter pub get
flutter analyze lib
```

The `example/lib/main.dart` file is a self-contained interactive showcase,
with light/dark and reduced-motion toggles. To run it as a standalone
Android/iOS/web app, from the example directory generate platform runners with
`flutter create .` and then `flutter run`. Do not commit generated runners
as part of the lightweight package unless a shipping target needs them.

## Accessibility and limits

- Reduced motion is decided at the widget's BuildContext from MediaQuery
  `disableAnimations` or `accessibleNavigation`.
- `MotionSwap` can retain an **outgoing** keyed widget during its transition.
  Do not use it to switch focus owners or sensitive interactive controls; use
  `MotionExpand` or direct state replacement instead.
- `MotionCompletionBadge` accepts a caller-provided localized semantic label.
- `MotionSkeleton` has no semantics by default: the owning screen should
  announce loading *once*. An optional localized label is available.
- `MotionHero` disables its own Hero flight for reduced-motion users. It does
  not control the navigator's route transition.
- Changes to platform settings mid-animation are resolved at rebuild; callers
  should rebuild when their accessibility settings change.
- Motion never conveys critical status by itself. Text, semantics and state must
  remain available without animation.
- This package does not define a universal `MaterialApp`, typography,
  colors or the app's Product Bible.

## Performance/dependency budget

Runtime dependencies: **Flutter SDK only**.
External animation runtime count: **0**.
Bundled fonts, audio, images, and binary assets: **0**.
Finite implicit/framework animations only; skeletons do not shimmer forever.

Release-size impact still requires measurement in an actual consuming app.
The source-only pack does not prove an APK size delta.

## Provenance / maturity

See `PROVENANCE.md`. This module was independently authored for the Factory
with native Flutter APIs. External GitHub animation libraries in the catalog
were evaluated as architectural references only; their code was not copied.

Status may be promoted to `LIBRARY_VERIFIED` after the package's exact-head
Flutter tests pass; `COPY_READY` additionally requires all gates in
`packs/ROADMAP_COPY_READY.md`. Cross-app certification is a later pilot.
