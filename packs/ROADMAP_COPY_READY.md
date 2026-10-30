# Design-App — COPY_READY Pack Roadmap (approved direction)

Status: APPROVED_DIRECTION / MOTION_FLUTTER_COPY_READY_LIBRARY_LEVEL
Updated: 2026-10-30
Factory baseline: App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25 (v27 ACTIVE).
Scope: library modules for future reuse; **no automatic app-repo changes**.

The objective is to replace repeated design work with small, auditable, low-footprint
packs. This roadmap approves the order and acceptance gates; it is not a claim that
any module has been implemented, tested or certified.

## Global promotion gate

DISCOVERY -> REFERENCE -> ADAPTED -> SOURCE_VERIFIED -> LIBRARY_VERIFIED -> COPY_READY.

A pack becomes COPY_READY only when it has:
1. explicit ownership, source/provenance, license and exact source revision;
2. minimal reusable API and documented compatibility/boundaries;
3. test harness executing on the actual target stack;
4. light and dark themes plus accessibility checks where applicable;
5. failure/empty/reduced-motion and relevant fallback behavior;
6. a demo/examples surface (screen or component workbench);
7. an install/copy guide and dependency/size impact assessment;
8. GREEN validation on the exact integrated PR head;
9. evidence that its **extracted** implementation works, not only that the donor app works.

COPY_READY is **not** CERTIFIED cross-app. An additional integration pilot/reuse
is required before promoting to certified golden status.

## Step 1 — Motion Pack (highest priority)

Flutter v0.1.0 implementation is at `packs/motion/flutter/` with widget tests,
an interactive example and dedicated GitHub Actions. Its library-level
`COPY_READY` status is backed by exact-source package/registry CI; check
`packs/PACK_REGISTRY.yaml` and the provenance ledger for evidence.
Compose and SwiftUI adapters are not yet implemented.


Proposed paths:
- `packs/motion/flutter/`
- `packs/motion/compose/` (follow-up)
- `packs/motion/swiftui/` (follow-up)

Candidate primitives:
- state transition (fade/scale/slide);
- restrained success/completion;
- selection/expand-collapse;
- hero continuity contract;
- skeleton (when the dependency is justified);
- reduced-motion-aware alternatives.

First donor hierarchy: framework-native -> existing Anna/FrameLab motion ->
`gskinner/flutter_animate` -> Lottie/dotLottie -> Rive only if interaction requires it.
No heavy runtime by default.

Acceptance: Flutter widget tests on semantics, durations, accessibility and
reduced motion; demo and bundle/dependency measurements.

## Step 2 — Semantic Sound Pack

The six CC0 WAV files, pinned manifest, integrity validator, optional Flutter
adapter, controller tests and preview are implemented and independently
LIBRARY_VERIFIED under `packs/sound/`. **Physical-device playback QA remains
required** before promoting this pack to COPY_READY.
See `packs/PACK_REGISTRY.yaml` for CI evidence.


Proposed paths:
- `packs/sound/semantic/`
- `packs/sound/adapters/flutter/`

Semantic IDs:
`selection`, `success`, `warning`, `error`, `completion`, `notification_soft`.

Source candidates: `wyzowl/sfx-kit` (CC0 metadata), Kenney UI Audio (CC0),
`bluefireteam/audioplayers` (MIT) only where platform playback is needed.

Select **only** specific assets, validate file hashes/encoding/durations/loudness,
retain attribution/source data, and keep any delivered pack small. Support a muted
mode. Critical alarms are explicitly out of scope.

Acceptance: asset manifest + checksum validator + semantic mapping tests,
on-device timing/volume acceptance for the product using it.

## Step 3 — Icon Adapter Pack

The first 24-key semantic manifest, generated Flutter/Compose adapters, Flutter
widget tests, Compose JVM harness and deterministic drift validation have
passed exact-source CI under `packs/icons/`.
Flutter adapter: **COPY_READY library-level**; Compose adapter:
**LIBRARY_VERIFIED**, pending real Android UI/semantics test and consumer pilot.
Aggregate pack: LIBRARY_VERIFIED. Provenance/evidence: `packs/icons/PROVENANCE.md`.


Proposed paths:
- `packs/icons/manifest/`
- `packs/icons/flutter/`
- `packs/icons/compose/`

Provide semantic icon IDs decoupled from vendor names (e.g. add, calendar, edit,
home, warning, success), a single default family per app, optional alternate
family mappings and a license/provenance manifest.

Sources: Material Symbols (existing), Lucide, Tabler, Ionicons.
Do not mirror entire icon packs. RemixIcon is reference/in-app-use only under its
custom license; not a standalone redistributed pack.

Acceptance: no missing mappings, light/dark legibility, consistent geometry,
minimum touch target where interactive, icon-level license inventory.

## Step 4 — Visual QA Kit

Proposed paths:
- `packs/visual-qa/flutter/`
- `packs/visual-qa/compose/`
- `packs/visual-qa/swiftui/`

Flutter widget/golden tests with optional Widgetbook component gallery,
Compose screenshot tests (Paparazzi), SwiftUI snapshots
(pointfreeco/swift-snapshot-testing).

Matrix:
- narrow phone; standard phone; tablet/rail as target;
- light/dark/system; scaled text; accessibility;
- focus/keyboard; long localized strings;
- loading/empty/error/offline states;
- overlays/safe-area/ad-slot collisions.

Acceptance: stable baseline images in CI with actionable pixel diffs and
explicit anti-flake strategy. No claims of physical-device validation based
on screenshot CI alone.

## No-duplication and build policy

- Preserve existing Golden Theme M3 and app-specific design identity.
- Do not introduce a separate renderer or full UI framework just for a few effects.
- Refactor the copy target only as needed to integrate.
- Each pack has its own version, use-case boundaries, copy/paste/install guide,
  dependency policy and provenance.
- Integration into any specific app remains governed by that app's Product Bible
  and roadmap.
