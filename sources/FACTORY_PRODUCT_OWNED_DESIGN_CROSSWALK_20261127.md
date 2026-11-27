# Design-App → Product-owned design: crosswalk 27/11/2026

**Authority**: App-Factory-Core `CURRENT.yaml` → Master v27 / Golden Index v31; Product Bible and owner-approved visual choices govern each app. This file is a curated routing/deduplication aid, not a second Golden or a global theme.

## What is new
Core PR #148 proposes `GOLDEN_PRODUCT_OWNED_DESIGN_SYSTEM_v1_DRAFT.txt` as **CANDIDATE**: it standardizes how to select, trace, adapt and validate visual references. It does not certify reusable code or alter approved app designs. The existing `GOLDEN_THEME_M3_FLUTTER_v1.txt` stays an **opt-in legacy implementation**, not the visual style baseline. Design-App `sources/MATERIAL3_OPTIONAL_REFERENCE_2026-11-19.md` already establishes this as optional; keep its reference ID and app matrix, do not duplicate them.

## Reference precedence and deduplication
1. Preserve target app Product Bible, prior approved mockups and explicit owner preferences.
2. Resolve existing UID/alias from `BIBLIOTECA_COMPONENTI/UID_REGISTRY.json`, then `CATALOGO.json`, source provenance and true implementation license.
3. Reuse an existing Design-App source/matrix entry and preferred component first. Do **not** create new UID or ingest the same product as another source.
4. Choose exactly one implementation owner for each token/widget: target app code. Design-App does not mutate app runtime by inclusion; Golden does not impose visible surfaces.
5. Favor direct reuse only when rights, stack and source-verification gates permit. React/TSX demos are not Flutter widgets; source-absent prototypes are REFERENCE_ONLY.
6. Apply AppLab visual + accessibility/exact-head checks after consumer integration. An approved mock-up and a green PR alone are not user-device acceptance.

## Existing sources → app decisions (REFERENCE, not blanket authorization)

| App | Existing visual reference / approved direction | Adaptation and guardrail |
|---|---|---|
| Anna's Diary | Organic iOS Journal; editorial diary; prior Ruixen and curated design references | Preserve rose/light brand where approved, Manrope/Lora, legible planner/diary layout; avoid repeated Material-like control clusters; do not touch Vault/security casually |
| Android Omni Cleaner | Color Bento Home, existing Linktree/Pop Fresh palette studies in `sources/CURATED_DESIGNS_UICOLOURS_AUDIT_2026-11-20.md` | Native Kotlin/Compose, one Home, explicit tool routes; no automatic M3-to-Flutter conversion or premature merge of draft #73/#76/#77 |
| Art Drift | Infinite gallery, art-first canvas and user-chosen joyful visual priority | Artwork image rights, immutable positions and performance take precedence over decorative effects; no artificial thumbnails |
| World Days | Editorial history and clean country/day information | Preserve historical/color identity; use authentic content and six-locale layouts; dynamic text/accessibility gate |
| Cooking Anime | Illustrated recipe experience and guided cooking | Preserve real reviewed recipe art and six-language content; do not assume an animation/source is licensed |
| CashMate AI | Minimal, clear finance-first dashboard | Data accuracy and privacy above color; no unsupported fake chart values or duplicate state stores |

## What is intentionally NOT done here
- No new UI component, UID, vendor dependency, image/font asset, design site ID, Golden promotion or consumer runtime code.
- No deletion of Material/Cupertino technical dependencies; visual direction and platform functionality are different concerns.
- No assertion that catalog references are copy-ready: use each item's recorded rights/validation state.
- No duplicate research dossiers for Dribbble/Collect UI, Ruixen, Motionary, Florent, Appllama, Uiverse or Watermelon already recorded under `sources/`.

## Consumer PR evidence checklist
For every future visual PR record (a) approved screen + source UID/ref, (b) source/asset rights and immutable SHA, (c) before/after matched screenshots, (d) component/token changes and no parallel theme, (e) dark/light/font-scale/localization/insets/focus checks, (f) exact-head CI plus physical user validation where required. Pending data or UX security gates stay pending.

References: `AGENTS.md`, `sources/MATERIAL3_OPTIONAL_REFERENCE_2026-11-19.md`, `sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md`, `sources/RUIXEN_UI_DESIGN_MOTION_AUDIT_2026-11-13.md`, `sources/APPLLAMA_MOTION_ART_STACK_AUDIT_2026-11-21.md`.
