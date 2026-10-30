# Semantic Sound Pack v0.1.0

Six short, **CC0** user-interface sound effects with semantic names and exact
source-byte provenance. This is an optional supplement to visual feedback; it is
not an alarm/alert reliability subsystem.

## Cue mapping

| Cue | Source | Duration |
| --- | --- | --- |
| selection | click-tap-soft.wav | 16 ms |
| success | notification-success-soft.wav | 530 ms |
| warning | notification-attention-soft.wav | 328 ms |
| error | notification-error-soft.wav | 567 ms |
| completion | notification-success-flourish.wav | 535 ms |
| notification_soft | notification-message-in-soft.wav | 423 ms |

Exactly 346,574 bytes of WAV assets (mono, 48 kHz, 24-bit PCM). No gigantic
asset packs or background streaming.

Assets are vendored under `../adapters/flutter/assets/` so that the Flutter
package can be used directly via a path dependency; the canonical
`manifest.json` lives here and tracks each exact source path, source blob
SHA, SHA-256, format, duration and size.

The six sounds come from [wyzowl/sfx-kit](https://github.com/wyzowl/sfx-kit)
at source commit `92780e7ab0cdfb557497a988089c47f46e8c7412`.
License: **CC0-1.0**, copied verbatim as `LICENSE-CC0.txt`. The
sound files were copied unchanged from the source repository, with renamed
destination files mapped to stable semantic identifiers.

## Reproducible integrity checks

From Design-App root:

```bash
python3 packs/sound/semantic/validate_assets.py
```

Validation checks all six SHA-256 digests and Git blob SHAs, WAV header
structure, PCM format, duration, source licensing metadata and total size.
It also checks exact filenames and prevents a path traversal in the manifest.

## Usage boundaries

- Default sound setting is OFF; the app must opt in.
- The user can mute sounds and adjust their volume.
- Meaningful state must be conveyed visually and through accessibility
  semantics; an audio failure must not prevent the real action.
- No critical/safety alarms, notification delivery guarantee or background
  audio assumptions.
- Platform audio focus, consent/preferences persistence, haptics, interruptions
  and store policy are owned by the consuming application.
- Real-device compatibility and perceived loudness/latency are not proven by
  static tests. **Do not promote to COPY_READY before physical QA.**

For Flutter integration, see `../adapters/flutter/README.md`.
