# Project Design Harvest — 2026-10-27

This document consolidates design decisions found across App Factory project chats,
project files and current first-party repositories. It is a retrieval index, not a
replacement for each app's Product Bible.

## Shared cross-app patterns

### DS-001 — Token-first visual system
Repeated across Anna's Diary, Wonderlog, Notes, FrameLab and other Factory guidance.
Use semantic color roles, typography roles, spacing, radii, motion durations,
component sizes and responsive breakpoints rather than screen-local arbitrary values.

Canonical recurring scales:
- spacing: 4 / 8 / 12 / 16 / 24 / 32, with 48 where larger rhythm is needed;
- radii: roughly 12 / 18-20 / 24-28 depending on visual family;
- feedback motion: about 120-160 ms;
- standard transitions: about 180-220 ms;
- emphasized/page transitions: about 220-280 ms;
- minimum touch target: 48 dp.

### DS-002 — Material 3 as infrastructure, not identity
Material 3 is the common technical base for most modern Flutter/Compose projects.
Consumer identity is layered on top through typography, surfaces, semantic colors,
hero composition, editorial imagery, gradients or domain-specific components.

### DS-003 — Responsive shell
Phone: NavigationBar / bottom navigation.
Tablet or wide desktop: NavigationRail or wider multi-pane layout.
The strongest first-party donors are Anna's Diary, Wonderlog and FrameLab.

### DS-004 — Progressive disclosure
High-frequency actions stay visible; secondary actions move behind More/Altro or a
secondary sheet. Anna's Unified Capture is the strongest current example:
Pensiero/Foto/Task/Voce first, Inbox/Appuntamento/Compleanno/Persona behind expansion.

### DS-005 — Functional motion + reduced motion
Use short state feedback, expansion, filter transitions, Hero only when content
continuity benefits. Disable or collapse transitions when the platform requests
reduced motion. Haptic feedback is subtle and action-linked, never decorative.

### DS-006 — State-complete screens
Every major surface should account for loading/skeleton, empty with useful CTA,
recoverable error, offline behavior and normal content. Do not ship a happy-path-only
screen.

### DS-007 — Quiet surfaces, stronger content
Zero/low elevation, border-defined cards and neutral surfaces recur across Notes,
Wonderlog, World Days, Battery Guard, FrameLab and Phone Guard. High visual energy is
reserved for hero content, state or a deliberate style family.

### DS-008 — Semantic visual accents
Color communicates domain/state, but never as the only signal. Anna uses distinct
accents for Today, Calendar, Memories, People, Shared, Workout, Vault and Ecosystem.
Phone Guard separates accent, warning and danger. World Days maps content categories
to visual keys and gradient families.

### DS-009 — Consumer-first information architecture
Avoid exposing architecture as navigation. Consolidate related views into one
product concept (for example Month + Week -> Calendar) and give first-class space to
the user's primary outcome.

### DS-010 — Ethical premium presentation
Premium surfaces use the same design system with a restrained accent and clear value.
No dark patterns; price, periodicity, restore and legal information remain readable.

## First-party style families

### STYLE-A — Editorial Personal / Anna's Diary
Sources:
- riccardopinato/Agenda-per-Anna
- project UX/design audits

Characteristics:
- personal, soft, consumer-oriented;
- neutral surfaces with user palette as identity rather than universal tint;
- domain semantic accents;
- spacing 4/8/12/16/24/32;
- radii 12/18/24/28;
- motion 120/180/260 ms;
- responsive NavigationBar -> NavigationRail;
- subtle selection/success haptics;
- contrast-aware accent surfaces;
- progressive disclosure;
- preferred shell direction: Oggi / Calendario / Ricordi / Altro with Capture first-class.

Best reuse:
- consumer diary/life apps;
- adaptive personal dashboards;
- capture-first products;
- accessible motion primitives.

### STYLE-B — Editorial Knowledge / Notes-Ecosistema
Source: riccardopinato/Notes-Ecosistema

Characteristics:
- warm neutral paper-like light canvas and dark slate surfaces;
- indigo primary + warm brown secondary;
- serif display/headline with sans body;
- 24 dp border-defined cards, zero elevation;
- editorial eyebrow, app title and section headers;
- 20 dp input radius, 20 dp FAB radius;
- block/editor/workspace interfaces;
- bottom sheets for intelligence, properties, research and quick switching;
- visual workspace / whiteboard / knowledge graph patterns.

Best reuse:
- notes;
- reading/writing;
- research;
- document/workspace products.

### STYLE-C — Colorful Travel / Wonderlog
Source: riccardopinato/Wonderlog

Characteristics:
- Material 3 fidelity scheme;
- rose seed #E85D75 + violet accent #7C5CE5;
- spacing 8/12/16/24/32;
- radii 12/20/28;
- border-defined low-elevation cards;
- 48 dp minimum interactive size;
- NavigationBar + NavigationRail;
- drag-handle bottom sheets;
- colorful consumer/travel feel without abandoning accessibility.

Best reuse:
- travel;
- itinerary;
- memory/trip consumer apps.

### STYLE-D — Photographic Editorial Premium / FrameLab
Source: riccardopinato/FrameLab-Google-AI-Studio

Characteristics:
- photography is the dominant visual asset;
- calm, precise, creative and premium without ostentation;
- large negative space, thin borders, light shadows;
- explicit rejection of neon, decorative glassmorphism, decorative gradients and continuous animation;
- neutral canvas/surface, forest-green accent, blue focus, restrained gold premium;
- 4 pt spacing grid;
- 12/16 dp radii;
- image/card Hero continuity only when useful;
- skeleton geometry matches final image geometry.

Best reuse:
- photography;
- media curation;
- premium editorial products.

### STYLE-E — Daily Editorial Color / World Days
Source: riccardopinato/World-Days

Characteristics:
- editorial calendar + globe;
- highly visual but lightweight;
- violet base seed;
- category-specific multi-stop gradients;
- deterministic visual_key -> icon + color family;
- generated geometric artwork with translucent orbs and large watermark icon;
- 24-28 dp hero/card radii;
- large date treatment, swipeable/editorial cards and local share-card composition;
- no requirement for heavy per-item imagery.

Best reuse:
- editorial catalogs;
- daily-return content;
- shareable cards;
- visually rich apps with tight APK budgets.

### STYLE-F — Clean Green Utility / Battery Guard
Source: riccardopinato/Battery_Guard

Characteristics:
- green semantic identity;
- Material 3;
- 72 dp navigation bar;
- surfaceContainerLow cards;
- 24 dp card radius;
- 52 dp full-width primary actions;
- 18 dp button radius;
- light/dark scheme.

Best reuse:
- battery/device-health utilities;
- simple monitoring dashboards.

### STYLE-G — Outdoor Utility / CamperBoss
Source: riccardopinato/CamperBoss

Characteristics:
- forest primary, moss dark accent, gold secondary;
- dark charcoal/night and warm day surfaces;
- 72 dp navigation bar;
- filled inputs with 16 dp radius;
- bold compact headings with slightly negative letter spacing;
- Material tap targets padded;
- utility readability with travel/outdoor identity.

Best reuse:
- camper/outdoor/travel utility apps.

### STYLE-H — Neon Analytics / FocusSense
Source: riccardopinato/FocuSense

Characteristics:
- dark navy gradient backdrop;
- low-opacity blue/cyan ambient circles;
- gradient cards with 22 dp radius and thin accent border;
- cyan/blue/green/purple semantic accents;
- gradient primary button;
- outline secondary button;
- selected pills;
- gradient progress bar;
- 270-degree score ring with glow layer and terminal dot;
- data/dashboard feel rather than generic Material cards.

Best reuse:
- focus/productivity dashboards;
- gamified analytics;
- sensor/score visualizations.

### STYLE-I — Reliable Safety Utility / Phone Guard
Source: riccardopinato/Phone-Guard

Characteristics:
- stable branded green accent (dynamic color intentionally disabled);
- dark hero/slate identity with explicit warning amber and danger red;
- shape scale 8/12/18/24/30 dp;
- clean zero-elevation utility panels;
- 48 dp choices/secondary actions;
- 56 dp primary actions;
- selected choice uses accent fill with accessible foreground;
- red high-visibility triggered warning state;
- mode/status/diagnostic presentation for protection products.

Best reuse:
- anti-theft;
- safety;
- device utility;
- diagnostic and protection state UX.

### STYLE-J — Pocket/Bag Protection Status UX
Sources:
- Pocket Guard project chats;
- Tabletop Motion Alarm donor lineage;
- Phone Guard consolidation

Characteristics:
- shield/status-centric home;
- explicit state labels such as waiting / detected / protected / alarm;
- sensor capability/status list;
- sensitivity, sound, vibration and flash controls;
- clear armed/unarmed state;
- PIN/biometric disarm flow;
- countdown and escalation UI;
- diagnostics/history are first-class trust surfaces.

Best reuse:
- sensor-driven protection utilities.

### STYLE-K — Compact Pixel Utility Branding / 180FlipCharge
Source: project design decision

Characteristics:
- very small utility footprint;
- 180-degree rotation metaphor;
- pixel-art icon direction;
- utility-first UI with minimal permanent surface.

Best reuse:
- ultra-small single-purpose utilities and Quick Settings companion products.

### STYLE-L — Green/Black Finance Blocks / CashMate AI
Source: project design decision

Characteristics:
- strong green/black block identity;
- finance dashboard emphasis;
- premium/goal surfaces should preserve the same high-contrast visual language.

Status:
- CHAT_DEFINED; source repository not available in the current connected GitHub set.

## Interaction patterns worth reusing immediately

1. Adaptive NavigationBar -> NavigationRail.
2. Progressive action disclosure.
3. Editorial eyebrow + serif title + sans body.
4. Border-defined zero-elevation cards.
5. Semantic domain accents.
6. Contrast-aware accent surface generation.
7. 48 dp selectable chips/choices.
8. 52-56 dp full-width primary utility CTA.
9. Category -> visual-key -> generated gradient artwork.
10. Neon metric card + score ring.
11. State/status card for protection/device health.
12. Skeleton with same final geometry.
13. Contextual bottom sheet with drag handle.
14. Central Capture / primary creation affordance.
15. Empty/error/offline/retry primitives.
16. Reduced-motion-aware transition primitive.
17. Selection/success haptic primitive.
18. Responsive maximum content width rather than infinitely stretching content.
19. Visual warning escalation screen for urgent safety state.
20. Canvas/whiteboard interaction family: pan/zoom/draw/select/resize/snapping/layers as a bounded workspace pattern.

## External discovery already available
The initial UI/UX/design source pool comes from
riccardopinato/Analisi-delle-mie-stelle-github and is mirrored separately in
registry/OSS_DESIGN_SOURCES.yaml. External sources are discovery/reference until
license and actual reuse scope are checked.
