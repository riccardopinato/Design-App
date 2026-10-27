# Sound Design Guide — App Factory

## Purpose

Treat sound as part of interaction design while keeping utility apps quiet,
accessible and predictable.

Sound is not a default requirement. It should be used only when it improves:
- confirmation;
- urgency;
- timing;
- delight in a bounded high-value moment;
- accessibility as an additional channel.

## Semantic sound set

Prefer a very small reusable vocabulary:

| Semantic event | Typical sound |
| --- | --- |
| selection | very subtle tick/click; often haptic-only is better |
| success | short positive chime/pop |
| warning | restrained attention tone |
| error | short negative cue, never punitive or excessively loud |
| completion | slightly richer success cue for finished process |
| notification | product-appropriate alert respecting platform policy/preferences |
| timer/countdown | sparse timing cue when the product requires it |
| critical alarm | separate product capability; never use decorative UI SFX as the alarm engine |

Do not sonify every button press.

## Interaction rules

- Never rely on sound alone to communicate success, warning, error or safety state.
- Pair meaningful sound with visual/semantic state and, when appropriate, haptic feedback.
- Provide a way to disable non-critical app sounds when the product uses them repeatedly.
- Respect platform audio conventions, focus/session rules and user expectations.
- Avoid sudden high-volume playback.
- Normalize perceived loudness across the local sound set.
- Keep UI sounds short and small; do not ship a 67 MB sound pack because one app needs six clips.
- Preload only when latency is perceptible and justified.
- Critical alarm products follow their own reliability/escalation requirements.

## Vetted asset sources

### wyzowl/sfx-kit — preferred semantic source
Pinned ref: `92780e7ab0cdfb557497a988089c47f46e8c7412`
License: CC0-1.0.

Why it is unusually useful:
- 320 original WAV effects;
- categories include Interface, Notifications, Time, Digital and Data;
- machine-readable `sounds.json`;
- each sound includes use/avoid guidance, tags, duration, sync point and level metadata.

Use it as the primary discovery pool, then vendor only the few selected files into
an app when appropriate.

### Calinou/kenney-ui-audio — preferred tiny UI pool
Pinned ref: `8c3d81b9159d058c444f89d12d518276b0b09345`
Asset license: CC0-1.0.

Contains 50 UI effects for buttons, switches and generic clicks. Useful when a small
conventional sound vocabulary is enough.

### DevsDaddy/Unity-UI-Audio-Collection — secondary discovery
Pinned ref: `661c9f25f615bda2aedb8cc8a40c711b3842d107`.
Repository license: MIT.

Large 200+ clip catalogue. Recheck asset-level licensing before production vendoring.

## Playback/runtime guidance

### Flutter
`bluefireteam/audioplayers`
Pinned ref: `7358eba581cb7ee3d0f048ff5170bb605776c9f3`
License: MIT.

Candidate for ordinary short UI sounds. Do not add it to an app that has no actual
sound requirement.

### Android native
Prefer platform APIs for ordinary UI feedback. `google/oboe` is a specialized
low-latency engine and should be admitted only when latency/audio complexity is a
real product requirement.

### Apple native
Prefer platform audio APIs for simple UI sounds. `AudioKit/AudioKit` is appropriate
for synthesis, processing or advanced audio products, not for a simple success chime.

## Suggested Design-App evolution

Future COPY_READY sound work should extract a tiny, normalized semantic pack rather
than mirror whole external libraries. A reasonable first pack would be:

```text
ui_selection
ui_success
ui_warning
ui_error
ui_complete
ui_notification_soft
```

Each asset should carry:
- source repo/ref;
- source file;
- license;
- duration;
- loudness/normalization note;
- intended semantic event;
- apps using it;
- physical-device evidence where latency matters.
