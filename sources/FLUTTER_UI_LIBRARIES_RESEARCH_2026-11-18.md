# Flutter Gems / Forui / F22 Labs — visual library research (18/11/2026)
Status: REFERENCE, discovery only; no app or Golden modification.

## Accurate roles
- [Flutter Gems](https://fluttergems.dev/): categorized directory claiming 7,250+ Dart/Flutter packages. Useful sections: [Design System](https://fluttergems.dev/design-system/), [Widget Library](https://fluttergems.dev/widget-library-ui-framework/), [Animation](https://fluttergems.dev/animation-transition/), [Testing](https://fluttergems.dev/testing/) and [Performance](https://fluttergems.dev/performance-crash-insights/). Some categories say Last updated May 18 2026; DO NOT treat listing metadata as real-time certification.
- [Forui Button](https://forui.dev/docs/widgets/form/button): concrete Flutter library docs, not generic Flutter SDK guidance. `FButton` / `FButton.icon` / `FButton.raw`, primary, secondary, destructive, outline, ghost, sizes/loading; style CLI `dart run forui style create buttons`. Source [duobaseio/forui](https://github.com/duobaseio/forui) @ `5dbf97c926a53fcfe3436db1be6262ac40961db5`; retrieved pub.dev metadata shows code MIT + fonts OFL and SDK Flutter >=3.44 for versions >=0.22. Exact consumer compatibility untested.
- [F22 Labs comparison](https://www.f22labs.com/blogs/top-8-flutter-ui-libraries-for-2025-you-must-explore/): despite 2025 URL, article titled 'Top 8 Best Flutter UI Libraries for 2026' dated Aug 4. List: GetWidget (broad widgets), shadcn_ui (branded SaaS), Forui (responsive mobile/desktop), Mix (tokens/styling rather than widget suite), FL Chart (charts, not UI framework), macos_ui (macOS), Fluent UI (Windows), TDesign Flutter (enterprise, check alpha). Secondary opinion only; original licenses/SDK/maintainers separately verified before use.
- [GenUI Medium article](https://medium.com/@fluttergems/building-a-genui-sales-analytics-app-in-flutter-with-bring-your-own-byo-ai-model-provider-f875098d17b0): GenUI/A2UI, declarative schema-controlled catalog and Amazon Bedrock adapter. Original [ashitaprasad/genui_sales_analytics_app](https://github.com/ashitaprasad/genui_sales_analytics_app) includes Apache-2.0 license; illustrates `genui:^0.8.0`. Technical architecture, not aesthetic source. No implicit permission to add cloud/paid AI.
- [GitHub Flutter search](https://github.com/search?q=flutter&type=repositories): dynamic OSS discovery, not a package or license. Reconcile with internal donor catalog; verify exact repo commit/licensing.

## Product aesthetic direction 2026–27
Modern/youthful/premium is NOT equivalent to installing a ready-made theme. Prioritize visual references handpicked by the owner in Design-App when coherent with the app. Preserve product-specific typography, hierarchy, spacing, original media aspect, responsive navigation, intentional micro-motion, dark theme, accessibility and realistic empty/offline/error states. Benchmark actual premium consumer apps without copying their logos, photography or identity.

## Technical admission gate
1. Define target app and Product Bible; check internal Golden/donor and existing package inventory.
2. Choose only task-relevant Flutter Gems categories, then shortlist two or three original packages.
3. Read original pub.dev and GitHub LICENSE/tag; check Flutter/Dart SDK, platforms, dependencies, maintenance, perf, APK weight, privacy/permissions and asset rights.
4. Classify SOURCE_REFERENCE / CODE_DONOR_CANDIDATE / REJECTED. No auto-copy, auto-install, Golden promotion or migration of working state management.
5. Use scoped PR, design/mock-up approval, CI and device evidence before IMPLEMENTED/VERIFIED.

## Proposed app links
See [matrix](../UI-UX/FLUTTER_UI_LIBRARIES_APP_MAP_2026-11-18.json), 6 Flutter app profiles, 13 proposed associations. Not all app repo stacks were rechecked in this intake; verify exact consumer before implementing. All remain PROPOSED_ONLY.
