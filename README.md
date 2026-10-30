# Design-App

Central design library for Riccardo's App Factory.

Design-App is the fast-retrieval layer for visual styles, UI/UX patterns, motion,
design tokens, reusable first-party source snapshots and external design discovery.

## Authority

Design-App is a specialized library, not the global Factory authority.

Order of truth:
1. app Product Bible;
2. app roadmap;
3. App-Factory-Core CURRENT / Master / Golden;
4. app-specific architecture and implementation;
5. Design-App as reusable design donor/reference.

## What is already harvested

The initial Project harvest includes:
- Anna's Diary;
- Notes-Ecosistema;
- Wonderlog;
- FrameLab;
- World Days;
- Battery Guard;
- CamperBoss;
- FocuSense;
- Phone Guard;
- Pocket/Tabletop protection UX;
- 180FlipCharge branding direction;
- CashMate design direction;
- shared Project design frameworks;
- the 36 UI/UX/design repositories already catalogued in Analisi-delle-mie-stelle-github;
- 37 curated GitHub design, motion, audio and tooling sources from 2026-10-27;
- 22 extra app-design and visual interaction sources from 2026-10-30.

## Fast lookup

Start here:
- registry/DESIGN_REGISTRY.yaml — canonical pattern/style IDs;
- sources/PROJECT_PATTERN_HARVEST.md — human-readable project harvest;
- registry/OSS_DESIGN_SOURCES.yaml — external discovery pool;
- tested/TESTED_REGISTRY.yaml — first-party reusable source inventory;
- tested/source_snapshots/ — pinned source code snapshots;
- sources/PROJECT_FILE_FRAMEWORKS.md — reusable design rules from older Project frameworks;
- sources/GITHUB_DESIGN_RESEARCH_2026-10-27.md — curated GitHub research and adoption tiers;
- sources/SOUND_DESIGN_GUIDE.md — semantic UI sound guidance and vetted audio sources;
- sources/GITHUB_DESIGN_RESEARCH_2026-10-30.md — 22 app-design/UI gallery and gesture sources;
- packs/ROADMAP_COPY_READY.md — implementation and acceptance sequence for 4 reusable packs.

## Maturity

DISCOVERY -> REFERENCE -> ADAPTED -> SOURCE_VERIFIED -> LIBRARY_VERIFIED -> COPY_READY

A working source app does not automatically make an extraction COPY_READY.

## Main style families

- STYLE-A — Editorial Personal / Anna's Diary
- STYLE-B — Editorial Knowledge / Notes
- STYLE-C — Colorful Travel / Wonderlog
- STYLE-D — Photographic Editorial Premium / FrameLab
- STYLE-E — Daily Editorial Color / World Days
- STYLE-F — Clean Green Utility / Battery Guard
- STYLE-G — Outdoor Utility / CamperBoss
- STYLE-H — Neon Analytics / FocuSense
- STYLE-I — Reliable Safety Utility / Phone Guard
- STYLE-J — Pocket/Bag Protection Status UX
- STYLE-K — Compact Pixel Utility Branding / 180FlipCharge
- STYLE-L — Green/Black Finance Blocks / CashMate
- STYLE-M — Forest/Moss Map Outdoor / TrailPath
- STYLE-N — Minimal Premium Safety Utility / Easy Debloat
- STYLE-O — Image-first Culinary Cards / In Cucina con gli Anime
- STYLE-P — Visual Alerts / AOD Circle / Luminous Infinite Circle

## Automatic intake

When a future app task or research discovers a reusable design pattern, library,
animation, component or repository, evaluate it for Design-App and register it when
useful. Third-party code must pass license/provenance checks before being copied.

See AGENTS.md for the operating contract.


## External design-source coverage

The external discovery pool now contains 95 unique repositories:
- 36 initial UI/UX discovery sources;
- 37 curated and commit-pinned sources from the 2026-10-27 research batch;
- 22 curated and commit-pinned app-design sources from the 2026-10-30 research batch.

The curated batches cover Flutter, Compose, SwiftUI, web accessibility, adaptive platform UI,
responsive layouts, Material 3 Expressive, motion, design tokens, iconography, visual QA,
UI sound design and finished-screen galleries.

No external runtime dependency is automatically admitted into an app merely because
it is catalogued here. Dependency Admission, license checks and per-app Product Bible
constraints still apply.


## COPY_READY development

Design-App keeps a separate execution roadmap for the Motion Pack,
Semantic Sound Pack, Icon Adapter Pack and Visual QA Kit:
`packs/ROADMAP_COPY_READY.md`.

The Flutter Motion Pack v0.1.0 is **COPY_READY at library level** with
Flutter analyzer/widget-test/example CI evidence, documented in
`packs/motion/flutter/PROVENANCE.md`. It is not cross-app certified.
Check `packs/PACK_REGISTRY.yaml` for the per-pack status.
The Semantic Sound Pack has six pinned CC0 WAVs, a checksum validator and
an optional Flutter adapter at `packs/sound/adapters/flutter/`.
It passed independent static/Flutter CI and is LIBRARY_VERIFIED.
Physical-device playback acceptance is still pending, so it is not COPY_READY.
The Icon Adapter Pack has 24 canonical semantic IDs with verified generated
Flutter and Compose adapters under `packs/icons/`.
Flutter is COPY_READY at library level; Compose is LIBRARY_VERIFIED
pending physical Android UI validation. Pack overall is LIBRARY_VERIFIED.
Only Visual QA remains entirely planned.
