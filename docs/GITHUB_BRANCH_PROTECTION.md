# Design-App main protection — repository-admin gate

State: **REQUIRES_ADMIN_ACTION** (verified 2026-10-30: main was unprotected;
no repository rulesets configured). This file does not enforce GitHub settings.

Admin action: Settings -> Rules -> Rulesets -> New branch ruleset.
Enforcement status: Active. Target: default branch (`main`).
Rules:
- require pull request before merge; disallow direct pushes;
- require status checks from GitHub Actions on the **latest PR head**;
- required context names (each workflow is triggered on every PR):
  `validate`, `motion-flutter`, `sound-pack`,
  `icon-manifest`, `icon-flutter`, `icon-compose`,
  `flutter-visual-qa`;
- require branches to be up to date with target before merge, or merge queue;
- require all conversations resolved;
- prevent force pushes and branch deletion;
- restrict bypass permissions to explicit emergency admins only;
- check whether self-approval restrictions permit a solo-maintainer
  workflow before choosing mandatory independent reviewer count.

After applying: verify the ruleset is Active and a deliberately failing
test PR cannot be merged or pushed directly to main. Record evidence in
`docs/GITHUB_RULESET_EVIDENCE.md` and close the admin issue.
Never label the branch protected merely because this checklist exists.

Checks and PR review must remain on the exact final head; ignored skipped
checks are not evidence of validation.
