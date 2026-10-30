# Factory Sound Flutter v0.1.0

Opt-in UI SFX playback adapter for the App Factory Semantic Sound Pack.

Status: **LIBRARY_VERIFIED** (exact-head Flutter analyzer, controller tests,
asset-bundle tests and demo analyzer passed). Native playback/volume/latency
remain NOT VERIFIED on hardware; not COPY_READY.
See `packs/sound/semantic/PROVENANCE.md` for CI evidence.

## Integration

Flutter >=3.27.0 / Dart >=3.6.0, with pinned
`audioplayers: 6.5.1` (MIT). This dependency is isolated to the sound
adapter: apps that need no audio should not install this package.

```yaml
dependencies:
  factory_sound_flutter:
    path: ../Design-App/packs/sound/adapters/flutter
```

Adjust the local path or vendor the bounded adapter into your app.
Do not depend on a floating Git branch for a production release.

```dart
import 'package:factory_sound_flutter/factory_sound_flutter.dart';

final sounds = SemanticSoundController(); // disabled by default
await sounds.setEnabled(true);  // only after the app/user enables sounds
sounds.setVolume(0.3);          // 0.0 .. 1.0
final status = await sounds.play(SemanticSound.success);

// Dispose with the appropriate app/service lifecycle.
await sounds.dispose();
```

For non-audio tests, inject a `SemanticSoundBackend` test double.

## Behavior

- Single audio player rather than overlapping effects.
- Soft default volume 0.35; volume values outside 0..1 are rejected.
- Muted/off requests do not reach the backend.
- Rate-limit repeated cues of the *same* category (120ms by default).
- Warning/error cues are not blocked by rapid selection cues.
- Playback failures return `SoundPlayStatus.failed` rather than crashing
  the initiating UI action.
- Widgets should display a state/semantic message independent of the sound.
- Critical alarms must use a separate reliable alarm subsystem.

## Tests / example

```bash
cd packs/sound/adapters/flutter
flutter pub get
flutter analyze lib test
flutter test --reporter expanded
cd example
flutter pub get
flutter analyze lib
```

The example UI includes a master enabled toggle, volume slider and all six
buttons; build platform runners with `flutter create .` in the example
directory if you need to test on a physical device.

Note: `flutter analyze` and widget tests verify package API, asset mapping
and controller policies, **not** actual hardware output, OS audio focus,
loudness normalization or device latency.

## Source and license

Six CC0 assets are included in `assets/` and have complete per-file
source provenance, SHA-256 and license at
`../../semantic/manifest.json`. The Flutter adapter is first-party code.
The external dependency is `audioplayers` 6.5.1 under MIT.
