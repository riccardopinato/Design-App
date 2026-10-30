# Five-step corrective audit implementation

Source: Design-App main@8c49dda98f8a074abac2ae84262d7e3948ab6324
Factory: App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25
Audit date: 2026-10-30

1. GitHub: enforce on every PR the validator, Motion, Sound, Icon
   Flutter/Compose and Visual QA checks. Configure actual branch protection
   with repository admin permissions as detailed in GITHUB_BRANCH_PROTECTION.md.
   Resolve or explicitly explain historical review findings.
2. Visual QA: bundle Material icons, use real font in golden tests,
   regenerate four PNGs, compare exact stable baselines in CI and test the
   interactive landscape demo.
3. Registry: update to Master v27; reconcile DS-009/DS-010 identifiers;
   add 37-pattern immutable snapshot provenance locator and validate it.
4. Motion/Icon: minimum touch width, preserve OS reduced motion,
   bundle icon font and pin CI actions.
5. World Days pilot: test genuine ObservanceCard widget, not a demo fixture;
   run existing app checks; no production app changes.

Not proven by test-only CI: physical-device runtime, APK size change,
Android accessibility service output or Play distribution. Do not mark
these PASS without the appropriate evidence.
