# Design QA — cross-app review & evidence protocol

**Status:** PROCESS CANDIDATE · 2026-11-17 · **not a certified Golden or an app runtime test**.

Canonical technical contract: [App Factory Core / Design Visual QA Process](https://github.com/riccardopinato/App-Factory-Core/blob/main/contracts/DESIGN_VISUAL_QA_PROCESS_v1.md) (Core PR #100 until merged). This library stores proposed design opportunities, comparative reviews and reusable assets; App-Factory-Core owns Master/Golden technical and release authority, and each app Product Bible owns branding and scope.

## Recommended review sequence

1. Resolve factory SHA, app main SHA, Product Bible, roadmap, design tokens and current open UI PR ownership.
2. Define the target screens and important user journeys; choose code-first or mockup-first without changing product scope implicitly.
3. Capture **real** current screenshots using stable fixtures; annotate hierarchy, cards, typography, content truncation, contrast, touch access, navigation and errors.
4. Implement only approved bounded changes on an isolated branch and rerun focused tests; don't touch privacy, destructive mutations, billing or storage unless separately approved.
5. Capture after screenshots with **the same data/state, viewport, locale, theme and font scale**. Review visually, record findings and decisions. Do not auto-approve changed baselines.
6. Run relevant accessibility, responsive, localization, dark-mode, offline/empty/error, reduced-motion and performance checks. Native Android runtime, PWA and physical devices remain distinct.
7. Attach exact-head PR/CI/AppLab/device evidence and track `SOURCE_IMPLEMENTED`, `CI_TESTED`, `RUNTIME_VISUAL_REVIEWED`, `PHYSICAL_ACCEPTED` and `RELEASE_CERTIFIED` independently.
8. Extract a pattern for reuse only after implementation and proven provenance/license/consumer behavior. Keep recommendations `PROPOSED_ONLY` until then.

## Evidence acceptance

A pilot record is a **plan**, not proof. For each screen capture fill `screen_id`, `platform`, `source_sha`, `fixture_id`, `viewport`, `locale`, `theme`, `font_scale`, `state`, `before_image`, `after_image`, `reviewer`, `reviewed_at`, `test_run_url`, `findings` and `status`. Missing evidence must remain `NOT_VERIFIED`. If a baseline screenshot predates a UI PR, identify its source SHA and do not compare it as the same version.

**Technical PASS** (no clipping, focus, supported device states) and **visual acceptance** (appropriate hierarchy, coherence, real user-content legibility) are separate assessments. AppLab source gates, web detector and screenshot existence do not independently establish user approval.

Supported quality references: Impeccable DSK-002 (workflow), Theme M3 Golden (Flutter technical baseline), App Shell Visual QA draft (responsive/matrix), AppLab certified adapter (runtime evidence trust), and relevant first-party Design-App design references. Impeccable detector/hooks are for HTML/CSS/Web workflows; do not run them as a native Flutter/Compose certification.

## Pilot status

- **Anna's Diary**: Organic iOS Journal (rose/HSV, Manrope/Lora), Today/Calendar/Memories/Settings. Existing editorial UI and candidate PRs take precedence over this plan. Private Vault, shared sync, classic mode and existing writers excluded from design-only scope.
- **Android Omni Cleaner**: Compose Material 3 brand, Home/Clean/Gallery/video preview/Privacy. Safeguard file selection/trash and truthful storage accounting. A gallery preview must preserve original aspect ratio and playable videos require genuine media/runtime tests.

See [machine-readable pilot manifest](./DESIGN_QA_PILOTS_2026-11-17.json). Every pilot starts **NOT_VERIFIED**, intentionally; no screenshot or test is represented as completed merely by adding this document.
