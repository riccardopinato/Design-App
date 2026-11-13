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
The Flutter Visual QA Kit under `packs/visual-qa/flutter/` has passed its
45-case layout matrix and four committed screenshot pixel comparisons:
LIBRARY_VERIFIED, still awaiting real-app integration before COPY_READY.
Compose/SwiftUI extensions remain planned.

## Audit remediation 2026-10-30

See `docs/AUDIT_REMEDIATION_v1.md` for the five-step corrective program,
`registry/PATTERN_PROVENANCE.json` for donor evidence leads, and
`docs/GITHUB_BRANCH_PROTECTION.md` for the outstanding repository-admin gate.
The first-party design code has no blanket external reuse license; see
`docs/LICENSE_POLICY.md`.


## Template Notion — catalogo di ricerca

[Apri Template Notion](docs/TEMPLATE_NOTION/README.md). Catalogazione di pattern, senza importare template commerciali in un'app.

## Archivio mock-up estetici

È disponibile [MOCKUP ESTETICI](./MOCKUP%20ESTETICI/README.md): cartelle per AESTHETIC, NEON, VINTAGE, PIXEL ART, POLAROID e ANIME; per ogni stile, immagini, app suggerite e classificazioni incrociate. Include [matrice app ⇄ stili](./MOCKUP%20ESTETICI/MATRICE_APP_STILI.md) e catalogo per il futuro caricamento degli asset. Le reference non modificano automaticamente Product Bible e roadmap.

## Archivio UI/UX

Nuova sezione [UI/UX](./UI-UX/README.md) per catalogare tecniche visive, pattern e componenti: Neumorphism, Soft 3D, Glassmorphism, Neo-Apple, Nature-Tech, Bento UI, Pastel UI, Spatial 3D e Minimal Controls. Comprende [matrice molti-a-molti app ⇄ stili](./UI-UX/MATRICE_APP_STILI.md) e [classificazione degli esempi visibili nello screenshot](./UI-UX/RIFERIMENTI_DALLO_SCREENSHOT.md). Nessun asset di terzi è stato copiato.

## Riferimenti visuali forniti dall'utente — novembre 2026

[Catalogo UI/UX completo](./UI-UX/RIFERIMENTI_UTENTE_2026-11-12.md) · [Matrice per app](./UI-UX/MATRICE_APP_RIFERIMENTI_2026-11-12.md) · [Catalogo estetico](./MOCKUP%20ESTETICI/RIFERIMENTI_UTENTE_2026-11-12.md). 35 upload, 33 unici. Originali non pubblicati senza licenze/diritti verificati; nessuna app modificata.

## Riferimenti visuali forniti dall'utente — 13 novembre 2026

[Nuovo catalogo UI/UX 66 riferimenti](./UI-UX/RIFERIMENTI_UTENTE_2026-11-13.md) · [Registro JSON con SHA-256 e duplicati](./UI-UX/REGISTRO_RIFERIMENTI_UTENTE_2026-11-13.json) · [Matrice app](./UI-UX/MATRICE_APP_RIFERIMENTI_2026-11-13.md) · [Indice estetico](./MOCKUP%20ESTETICI/RIFERIMENTI_UTENTE_2026-11-13.md). 77 upload, 66 nuovi unici, 11 duplicati esatti. Il precedente lotto del 12/11 resta invariato (33 unici); totale due lotti: 99 unici. Materiale REFERENCE_ONLY: i file di terzi non sono stati ripubblicati e nessuna app è stata modificata.

## Matrice molti-a-molti App ↔ Stili (12–13/11/2026)

La classificazione trasversale dei **99 riferimenti unici** è consultabile [per app](./UI-UX/PER_APP_STILI_2026-11-13.md) oppure [per stile](./UI-UX/PER_STILE_APP_2026-11-13.md). Il [registro relazionale JSON](./UI-UX/MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json) contiene **254 coppie stile–app** e **771 link stile–app–reference**, con viste coerenti derivate dalle stesse associazioni. Gli originali restano fuori dal repository pubblico fino a verifica dei diritti di redistribuzione.
