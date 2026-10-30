# Historical PR review triage — 2026-10-30

The eight open inline threads across merged PR #1, #4, #5, #6, #7
were inspected individually. Completion requires reviewing exact-head
audit PR results before marking corresponding GitHub threads resolved.

| PR | Review point | Remediation | Status |
|----|--------------|-------------|--------|
| #1 | Patterns lacked deterministic source pointers | registry/PATTERN_PROVENANCE.json links all 37 IDs to donor refs, immutable first-party snapshot blob SHA when available, and explicit unverified donors | Implemented; direct per-pattern equivalence NOT asserted |
| #1 | DS-009/DS-010 ID collision | Harvest headings are no longer incorrectly named DS-009/DS-010 | Implemented |
| #4 | Selection tile minimum width | MotionSelectionTile minWidth=48 plus targeted tiny-child test | Implemented |
| #4 | Demo disables user OS reduced-motion preference | Local toggle OR inherited disableAnimations | Implemented |
| #5 | Test package asset key questioned | Previously observed Flutter CI GREEN on same rootBundle loads; test failure was not reproduced. Asset source SHA and bundle checks remain. Retest exact audit PR head. | Evidence based |
| #6 | Material icon font absent in Flutter sample | uses-material-design:true in package+example, visual golden regression checks use actual OTF | Implemented |
| #7 | Golden screenshots with missing icon glyphs | MaterialIcons + real text font loaded; four reviewed, re-pinned PNG files; seed workflow removed | Implemented |
| #7 | Landscape showcase may overflow | Entire preview uses full-window Stack; controls are floating menu; example landscape widget tests | Implemented |

Unresolved independent acceptance:
- repository main ruleset requires GitHub admin, issue #8;
- snapshot leads are not equivalent to direct validation for every design
  pattern; promote specific entries only with scoped implementation evidence;
- physical-device validation is not implied by this PR.
