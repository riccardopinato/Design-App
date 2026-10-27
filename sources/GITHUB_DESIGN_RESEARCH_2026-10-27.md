# GitHub Design Research — Curated Expansion 2026-10-27

Factory baseline: `riccardopinato/App-Factory-Core@7b84e33df715cf2a48bda7c7495d0690819bff0f`
Master: v26.6
Golden Index: v23

## Goal

Expand Design-App with repositories that materially improve mobile-app design work,
not merely repositories that happen to have attractive screenshots.

The search covered:
- design systems and tokens;
- Flutter UI and motion;
- Jetpack Compose / Kotlin;
- SwiftUI / Swift;
- iconography;
- component workbenches and visual regression;
- UI sound assets and audio playback.

All curated sources are pinned in `registry/OSS_DESIGN_SOURCES.yaml` to the
observed source commit. Cataloguing a repository does not approve a runtime
dependency or automatic code copy.

## Tier A — strongest additions

| Source | Why it matters |
| --- | --- |
| style-dictionary/style-dictionary | Cross-platform token build system; useful if Design-App evolves from documentation into generated Flutter/Compose/Swift tokens. |
| widgetbook/widgetbook | Natural Flutter component workbench for inspecting reusable widgets, states, themes and accessibility variants. |
| gskinner/flutter_animate | Small, expressive Flutter micro-interaction layer; suitable below Lottie/Rive in the motion hierarchy. |
| xvrh/lottie-flutter | Mature pure-Dart Lottie playback for bounded animations. |
| LottieFiles/dotlottie-flutter | Current official dotLottie/Lottie Flutter runtime and compact animation-container option. |
| rive-app/rive-flutter | Best fit when the animation is interactive or state-machine driven, not just decorative playback. |
| android/compose-samples | Official Compose reference for layouts, motion, accessibility and platform conventions. |
| android/nowinandroid | Large production-style Compose reference with adaptive UI patterns. |
| valentinilk/compose-shimmer | Focused loading/skeleton motion donor for Compose. |
| SwiftUIX/SwiftUIX | Broad SwiftUI primitive expansion and native-platform reference. |
| Orange-OpenSource/ouds-ios | Real-world SwiftUI design system, useful as an industrial component/token reference. |
| lucide-icons/lucide | Consistent neutral line-icon language; ISC with inherited Feather subset under MIT. |
| tabler/tabler-icons | Very broad MIT SVG icon system. |
| cashapp/paparazzi | Android screenshot/visual regression without device or emulator. |
| pointfreeco/swift-snapshot-testing | Strong Swift/SwiftUI snapshot-testing reference. |
| wyzowl/sfx-kit | 320 CC0 UI/animation sounds with machine-readable semantic metadata and timing. |
| Calinou/kenney-ui-audio | 50 compact CC0 UI sounds suitable for small app bundles. |
| bluefireteam/audioplayers | Cross-platform Flutter playback suitable for short UI SFX. |

## Tier B — useful by product

These are deliberately not default dependencies.

- `tokens-studio/figma-plugin`, `tokens-studio/sd-transforms`, `figma/code-connect`,
  `figma/sds`: useful when the workflow becomes Figma/token driven.
- `bdlukaa/fluent_ui`, `duobaseio/forui`: visual/component references, not reasons
  to abandon the Factory's Material 3 foundation.
- `JetBrains/compose-multiplatform`, `skydoves/Balloon`,
  `skydoves/landscapist`, `Trendyol/komposto`: specialized Kotlin/Compose donors.
- `exyte/PopupView`, `exyte/AnimatedTabBar`, `imodeveloper/dskit-swiftui`,
  `markiv/SwiftUI-Shimmer`: focused SwiftUI donors.
- `ionic-team/ionicons`: useful alternative mobile icon family.
- `Remix-Design/RemixIcon`: attractive neutral icon source, but its 2026 custom
  license forbids repackaging the icons as a standalone icon library. Use inside
  products or as reference, never mirror the pack into Design-App.
- `DevsDaddy/Unity-UI-Audio-Collection`: large SFX collection; repository is MIT,
  but asset scope should be rechecked before copying files into production.
- `google/oboe`: Android low-latency audio engine; disproportionate for ordinary
  tap/success sounds.
- `AudioKit/AudioKit`: powerful Apple audio stack; relevant only to apps with
  real synthesis/processing requirements.

## Motion hierarchy

The preferred motion decision is now:

```text
native/framework animation
-> lightweight micro-motion (flutter_animate / equivalent)
-> Lottie or dotLottie for bounded vector playback
-> Rive for interactive/stateful animation
```

Do not add a vector runtime for a fade, scale, selection transition or simple
progress state that the framework handles cleanly.

## Icon hierarchy

Default remains the icon family that best fits the product and platform. Avoid mixing
multiple line weights/styles within one surface.

Recommended discovery order:
1. Material Symbols / existing product icon language;
2. Lucide for neutral lightweight line icons;
3. Tabler when breadth is more important;
4. Ionicons for a more mobile-oriented family;
5. Remix Icon only under its specific license constraints.

Do not mirror whole icon repositories into Design-App. Store source/provenance and
vendor only the icons an app actually uses when the license permits.

## Visual QA

Design-App should increasingly treat visual correctness as testable:

- Flutter: Widgetbook can expose component/state/theme matrices; existing Flutter
  golden tests remain the runtime-native verification path.
- Android Compose: Paparazzi is a strong candidate for deterministic screenshot QA.
- SwiftUI: swift-snapshot-testing is the strongest candidate in this research batch.

A screenshot tool does not replace physical QA for insets, keyboard, animation,
performance or platform-specific rendering.

## License notes

The research explicitly checked repository or asset licenses for the sources most
likely to be copied:
- Forui code: MIT; bundled fonts include OFL-1.1 terms.
- Lucide: ISC, with a listed inherited Feather subset under MIT.
- Remix Icon: custom Remix Icon License v1.0; commercial in-app use is permitted,
  standalone repackaging is restricted.
- SFX Kit: CC0-1.0.
- Kenney UI Audio: CC0-1.0.
- Unity UI Audio Collection: MIT repository license; asset-level scope should still
  be rechecked before vendoring.

## Adoption rule

A source enters Design-App as DISCOVERY/REFERENCE. Promotion requires:
source ref + license + bounded reuse + adaptation notes + tests/evidence.

Popularity is not certification.
