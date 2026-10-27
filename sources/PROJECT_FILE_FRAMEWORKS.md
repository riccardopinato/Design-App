# Reusable Design Frameworks Harvested from Project Files

This file indexes design rules already used in the wider App Factory project before
Design-App existed. They are kept as framework references and must be reconciled with
the current App-Factory-Core baseline before being promoted to reusable implementation.

## Sources

- APP_EMPIRE_BUILDER_PROMPT_MASTER_COMPLETO.txt
- SHOS_v4_STEP_4_Design_UX_Layer_Prompt.txt

## Reusable principles

### Design is part of release quality
A technically working screen is not sufficient if it is visually generic,
inconsistent, overloaded or inaccessible.

### Design source-of-truth artifacts
Useful per-app artifacts repeatedly defined in the project:
- Design Bible / visual direction;
- design tokens;
- component style guide;
- asset direction;
- store visuals;
- microcopy guidance.

Design-App centralizes reusable parts, while each app keeps its own product-specific
brand and design decisions.

### Token families
Before large UI work, define:
- semantic colors;
- typography roles;
- spacing;
- radii;
- shadows/elevation;
- gradients;
- motion durations;
- icon sizes;
- component sizes.

### UI excellence gate
Review screens for:
- visual hierarchy;
- information density;
- spacing rhythm;
- typography;
- color discipline/contrast;
- card composition;
- button hierarchy;
- icon consistency;
- whitespace;
- perceived speed;
- accessibility;
- dark mode;
- loading/empty/error polish;
- premium feel without visual noise.

### Friction reduction
Prefer:
- fewer taps;
- fewer screens;
- fewer forms;
- fewer simultaneous decisions;
- clear defaults;
- fast first success;
- strong hierarchy;
- progressive disclosure;
- useful recovery states.

### Motion
Motion should:
- clarify state;
- guide attention;
- provide feedback;
- add restrained delight.

Avoid continuous decorative motion or animation that blocks interaction.

### Trend/reference pool
Previously discussed visual directions that can be evaluated per product, never
blindly applied:
- bento layouts;
- controlled glassmorphism;
- Material 3 Expressive;
- floating/large rounded cards;
- deep gradients;
- neon/arcade;
- cozy/pastel;
- minimal premium;
- progress rings;
- animated onboarding;
- haptic feedback;
- skeleton loading;
- illustrated empty states;
- Lottie/Rive.

These are REFERENCE patterns, not defaults. The product category and existing
first-party donors decide whether they are appropriate.

## Current normalization
Design-App translates these legacy framework ideas into:
- registry/DESIGN_REGISTRY.yaml;
- sources/PROJECT_PATTERN_HARVEST.md;
- tested/TESTED_REGISTRY.yaml;
- tested/source_snapshots/.

Current App-Factory-Core remains authoritative for Factory-wide governance.
