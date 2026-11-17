# App Factory Visual QA — first pilot evidence reconciliation (17/11/2026)

## Canonical governing sources

- App Factory Core CURRENT v27 / Golden Index 29; Design Review process PR [#100](https://github.com/riccardopinato/App-Factory-Core/pull/100), merged main `d660cccd57f2e252c573c484457f1ae9234b1e33`.
- Design-App DSK-002/Impeccable source PR [#34](https://github.com/riccardopinato/Design-App/pull/34) and evidence validator PR [#35](https://github.com/riccardopinato/Design-App/pull/35), merged main `2cc06729bc5228a631b3b836143e26017e900f53`.
- **No Golden admission change**: Theme M3 remains COPY-READY, App Shell/Visual QA remains DRAFT. These records are project evidence, not a new Golden or a new product requirement.

## Pilot A — Anna's Diary

- Original app main baseline: `e769b2173e9e391615b26c872a7e691f621f9dd7`.
- PR [#350](https://github.com/riccardopinato/Agenda-per-Anna/pull/350) source head `cdd94fbf67cfe281aa61be3b13d402ba24e595cb`; merged main `f1e63c06703d80c66908e97a251cbfe72f652bc8`.
- Exact-source [Development checks](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/44125713758), UI5 source check, both capture workflows PASS.
- [Calendar screenshot run](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/44125713889): 12 Flutter-rendered synthetic empty/populated CalendarHub, Month, Agenda and Week screenshots, artifact ID `14347795940`.
- [Organic Journal screenshot run](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/44125713697): 7 Flutter-rendered secondary screens, Memories empty/populated, Settings, Explore/More, artifact ID `14346319713`.
- Source and screenshot integrity were repaired in pilot: PR-only capture uses `github.event.pull_request.head.sha` for checkout and artifact identity, rather than GitHub synthetic merge SHA.
- Assistant visually inspected the combined 19 static screenshots: coherent editorial direction; potential Capture FAB overlay on daily-context card (requires hit-target test), some week-day empty/populated outputs visually near-identical (requires fixture validation), palette coverage differs between Calendar Rose and Journal Sage. These are preliminary findings, not a user approved design or regression baseline.
- Existing approved prior baseline of the *same* screen/data/viewport is not supplied. **Visual regression PASS NOT VERIFIED.** Physical Android, PWA device, TalkBack and user aesthetic acceptance NOT VERIFIED.

## Pilot B — Android Omni Cleaner

- Original app main baseline: `984474d9af62d8b7e17b975a31332161f24f2df7`.
- PR [#28](https://github.com/riccardopinato/Android-Omni-Cleaner/pull/28) exact source head `0790bb30a922f661a9cd0a6341aa6fd78164eb2e`; merged main `bc1b9227dfcd1636ec53c061c8eafa72614ff749`.
- [Android CI](https://github.com/riccardopinato/Android-Omni-Cleaner/actions/runs/44126023030) PASS: locale parity, Kotlin unit tests and debug APK/instrumented-test APK compilation.
- Source changes: uncropped preview `ContentScale.Fit`; bounded ratio from frame, photo fullscreen source decode with EXIF orientation, safe missing URI fallback; real native `VideoView` controls inside non-destructive full-screen viewer; EN/IT/ES/FR/PT strings; JVM ratio tests. Existing MediaStore/Trash/Undo and cleaner engines unchanged.
- Two Codex P2 comments (unreadable photo and EXIF) addressed in code, tests/build green, review threads resolved. No new third-party media dependency.
- This supports **source-integrated and CI-tested scoped primitive** in one application, not a tested native video player on hardware, not cross-app reuse and **not LIBRARY_VERIFIED or COPY_READY**. Actual media playback, codecs, lifecycle, partial media permissions, 48MP images, accessibility and device battery/memory testing remain NOT VERIFIED.

## Reuse decision

`DES-REUSE-002` (*Image aspect-ratio-safe media viewing*) now carries pinned single-consumer CI evidence, but stays **REFERENCE**. It is not a generalized library, and its video lifecycle has not yet been run and verified across Android devices. `DES-REUSE-001` (status-aware states) and `DES-REUSE-003` (purposeful motion) remain reference-only without consumer proof.

## What is complete vs open

| Dimension | State | Evidence |
|---|---|---|
| Factory process contract | MERGED / CI PASS | Core #100 |
| Design library governance + validation | MERGED / CI PASS | Design-App #35 |
| Anna source visual capture pipeline | MERGED / CI PASS; CAPTURED | Anna #350 and both actions artifacts |
| Anna visual approval / regression | NOT VERIFIED | No approved baseline/user sign-off |
| Omni gallery source + tests | MERGED / CI PASS | Omni #28 |
| Omni video/photo native physical QA | NOT VERIFIED | Runtime/physical test not run |
| Cross-app COPY_READY / Golden promotion | NOT MET | No independent verified adaptation |

**Recommended follow-through:** verify the Anna overlap and fixture findings in its existing UI owner issue #327; run manual Android/physical Gallery playback and memory tests on an exact Omni APK; after real evidence, adapt the minimum generic preview function for another independent consumer if useful, then evaluate promotion under the existing Golden admission contract.
