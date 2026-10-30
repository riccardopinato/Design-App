# GitHub design research — 30 ottobre 2026

Factory baseline: `riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25` (v27 ACTIVE, Golden Index v23).
Prior batch: `sources/GITHUB_DESIGN_RESEARCH_2026-10-27.md`.
Registry: `registry/OSS_DESIGN_SOURCES.yaml`.

## Scope and decisions

22 new commit-pinned repositories have been added without duplicating the 73 existing sources.
Research emphasizes **UI design**, not just infrastructure: finished-screen galleries,
layout, typography, animation, native-platform polish, accessible interaction and
visual effects.

Sources are `REFERENCE` until extracted/adapted, tested, and licensed for intended
reuse. A listed GitHub project does **not** imply installation in any app.
Commit SHA and LICENSE at time of observation are stored in the registry.
Age/staleness of demos is a major factor in deciding between reference and code donor.

## Flutter — ready-to-study visual design

| Repository | Focus | License | Priority and use |
| --- | --- | --- | --- |
| [iampawan/Flutter-UI-Kit](https://github.com/iampawan/Flutter-UI-Kit) | Collection of Flutter app screens | Apache-2.0 | B: historical screens for hierarchy, not modern copy-ready code (last activity 2022) |
| [nathansdev/ContraFlutterKit](https://github.com/nathansdev/ContraFlutterKit) | Cohesive kit of 50+ screens | Apache-2.0 | B: visual ideation for consumer apps |
| [Codelessly/ResponsiveFramework](https://github.com/Codelessly/ResponsiveFramework) | Breakpoint-based adaptation | MIT | A: compare with existing Factory shell before adding dependency |
| [letsar/flutter_staggered_grid_view](https://github.com/letsar/flutter_staggered_grid_view) | Staggered/masonry layout | MIT | B: photo diary/editorial galleries; check current SDK/API |
| [canopas/animated_reorderable_list](https://github.com/canopas/animated_reorderable_list) | Drag-and-drop reorder motion | BSD-3-Clause | A: Notes, task lists, sorting and organizing |
| [ricardodalarme/flutter_card_swiper](https://github.com/ricardodalarme/flutter_card_swiper) | Swipeable card stack | MIT | B: swipe decisions, cards and gestures |
| [sdegenaar/liquid_glass_widgets](https://github.com/sdegenaar/liquid_glass_widgets) | Shader-based Liquid Glass, physical effects | MIT | A: Anna-like iOS design experiments, performance-fallback needed |
| [berkaycatak/adaptive_platform_ui](https://github.com/berkaycatak/adaptive_platform_ui) | Adaptive native iOS/Android components | MIT | A: native platform-fit and iOS 26+ UI; minimum-iOS requirements must be checked |
| [CRED-CLUB/neopop-flutter](https://github.com/CRED-CLUB/neopop-flutter) | Tactile NeoPOP buttons and surfaces | Apache-2.0 | B: product-specific style inspiration; do not mix indiscriminately |
| [Idean/Flutter-Neumorphic](https://github.com/Idean/Flutter-Neumorphic) | Light/dark neumorphic system | Apache-2.0 | C: historical style only; assess contrast and outdated APIs |

## Jetpack Compose / Kotlin

| Repository | Focus | License | Decision |
| --- | --- | --- | --- |
| [SimformSolutionsPvtLtd/SSComposeCookBook](https://github.com/SimformSolutionsPvtLtd/SSComposeCookBook) | Gallery/cookbook of native UI | MIT | B: screen and component inspiration; pinned head is a feature branch, so re-review before use |
| [meticha/material-3-expressive-catalog](https://github.com/meticha/material-3-expressive-catalog) | Modern Material 3 Expressive catalog | Apache-2.0 | A: high-value for Android utility polish |
| [canopas/compose-animations-examples](https://github.com/canopas/compose-animations-examples) | Compose animation examples | No repository license verified | B: **REFERENCE_ONLY**, no copying source |

## SwiftUI / native iOS design

| Repository | Focus | License | Decision |
| --- | --- | --- | --- |
| [amosgyamfi/open-swiftui-animations](https://github.com/amosgyamfi/open-swiftui-animations) | Spring, keyframe and symbol-effects gallery | Unlicense | A: native motion donor, check example-specific assets |
| [swiftui-lab/swiftui-hero-animations](https://github.com/swiftui-lab/swiftui-hero-animations) | matchedGeometryEffect hero transitions | MIT | B: older conceptual reference |
| [GetStream/accessible-inclusive-ios-animations](https://github.com/GetStream/accessible-inclusive-ios-animations) | Reduced-motion and inclusive motion | No repository license verified | A: **REFERENCE_ONLY**, accessibility lessons |
| [pixiv/charcoal-ios](https://github.com/pixiv/charcoal-ios) | Production design-system library | Apache-2.0 | B: architecture and component conventions |

## Web UI / patterns transferable to mobile

| Repository | Focus | License | Decision |
| --- | --- | --- | --- |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Modern component composition and visual defaults | MIT | A: reference for dialogs, forms, cards, navigation and aesthetics |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | Accessible unstyled interaction primitives | MIT | A: reference for keyboard focus, menus, popovers and modal states |
| [motiondivision/motion](https://github.com/motiondivision/motion) | High-quality React/JS motion and gestures | MIT | A: translate interaction intent into Flutter/Compose rather than adding JS |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Animated UI and polished effects | MIT | B: selective visual references; avoid gratuitous animation |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | Dense forms and data-heavy dashboards | MIT | B: useful in complex/admin UI, not every consumer app |

## Priority by current App Factory needs

- **Anna's Diary**: adaptive native UI; controlled Liquid Glass as optional experiment;
  accessible motion; hero transitions; richer screen composition without changing
  the approved Manrope/Lora and rose design direction.
- **Notes-Ecosistema**: reorderable lists, responsive masonry/editorial content, keyboard
  and focus behavior inspired by Radix, reduced motion.
- **Wonderlog / FrameLab**: staggered photo grids, clean consumer components,
  content-led transitions instead of decorative effects.
- **FocusSense / Phone Guard**: Material 3 Expressive and clear state animations,
  accessibility-first, no glass treatment on critical warning screens.
- **Cooking Anime**: visual galleries for product discovery, photo cards and responsive
  layout; no blind migration to a web UI framework.
- **AppLab**: component screenshot/diff tooling remains catalogued in the previous batch.

## Freshness, license and runtime cautions

- Older demo screens and libraries may use obsolete SDKs or APIs; they are not
  safe as turnkey implementation.
- A missing GitHub license is not permission to copy. Such projects remain
  idea/reference-only.
- Liquid Glass shader/blur cost must be measured on midrange Android and iOS;
  provide low-power/reduced-transparency or simplified fallback.
- Native/React reference patterns are **concept donors**, not a reason to introduce
  React or SwiftUI into a Flutter application.
- Avoid importing entire UI kits into small apps; extract only what the Product Bible
  and Factory component baseline do not already provide.

## Result

- Prior sources: 73 unique.
- Added: 22 commit-pinned sources.
- New total: 95 unique sources.
- New pattern IDs: DS-031 through DS-037.
- No external code/assets were vendored by this research.
- No component is automatically promoted to COPY_READY.
