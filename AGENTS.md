# AGENTS.md — Design-App

## Role
Design-App is the specialized design library for the App Factory.

It stores reusable visual patterns, UI/UX references, motion patterns, design tokens,
first-party source snapshots, tested components and external design sources.

It does NOT replace:
- App-Factory-Core CURRENT / Master / Golden Rules;
- a product's Product Bible;
- a product's roadmap;
- the app repository's own architecture and source of truth.

## Intake rule
Whenever work on an App Factory project discovers a reusable design pattern,
animation, library, component, layout, interaction or external repository, evaluate
it for Design-App without waiting for a separate request.

## Maturity states
DISCOVERY -> REFERENCE -> ADAPTED -> SOURCE_VERIFIED -> LIBRARY_VERIFIED -> COPY_READY

Definitions:
- DISCOVERY: interesting source, not yet evaluated enough for reuse.
- REFERENCE: useful visual/interaction idea; not necessarily copyable code.
- ADAPTED: normalized for App Factory conventions.
- SOURCE_VERIFIED: implementation already works/tests in the source app.
- LIBRARY_VERIFIED: extracted version has its own validation evidence.
- COPY_READY: safe rapid-reuse asset with provenance, license and usage notes.

Never label an item COPY_READY solely because the source repository works.

## Reuse hierarchy
1. Design-App COPY_READY / LIBRARY_VERIFIED item.
2. App-Factory-Core Golden or certified internal donor when applicable.
3. Design-App SOURCE_VERIFIED first-party pattern.
4. Design-App REFERENCE / external OSS source.
5. New implementation.

## Provenance
Every significant item must record:
- source repository/chat/document;
- immutable source ref or file blob when available;
- source path;
- license/ownership;
- reuse mode: COPY | ADAPT | REFERENCE_ONLY;
- validation level;
- known constraints.

## External code
Before copying third-party code:
- verify LICENSE/SPDX;
- prefer maintained sources;
- do not copy code with absent, ambiguous or incompatible license;
- use those sources as REFERENCE_ONLY and reimplement independently.

Do not copy logos, brand identity, proprietary illustrations or recognizable
third-party product identity.

## Design principles
- Material 3 can be the technical foundation without forcing a generic Material look.
- Maintain one coherent icon language.
- Use design tokens rather than screen-local arbitrary values.
- Prefer progressive disclosure over crowded surfaces.
- Respect reduced-motion/accessibility preferences.
- Minimum interactive targets should normally be 48 dp where platform conventions apply.
- Empty/loading/error/offline states are part of the design.
- Motion must clarify state, attention or feedback; decorative noise is not a goal.
- Responsive layouts should adapt navigation and information density, not merely stretch phone UI.

## Source snapshots
Files under tested/source_snapshots/ are first-party snapshots copied from working
app repositories for fast retrieval. Their header/provenance record identifies the
source. A snapshot remains pinned; updates create a new version rather than silently
rewriting history when the behavior materially changes.
