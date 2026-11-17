#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def fail(message: str):
    print(f"ERROR: {message}")
    raise SystemExit(1)

registry = (ROOT / "registry" / "DESIGN_REGISTRY.yaml").read_text(encoding="utf-8")
oss = (ROOT / "registry" / "OSS_DESIGN_SOURCES.yaml").read_text(encoding="utf-8")
tested = (ROOT / "tested" / "TESTED_REGISTRY.yaml").read_text(encoding="utf-8")
coverage = (ROOT / "sources" / "COVERAGE.md").read_text(encoding="utf-8")

pattern_ids = re.findall(r"^\s+- id:\s+(DS-\d+)\s*$", registry, re.MULTILINE)
style_ids = re.findall(r"^\s+- id:\s+(STYLE-[A-Z]+)\s*$", registry, re.MULTILINE)
all_ids = pattern_ids + style_ids

if len(all_ids) != len(set(all_ids)):
    fail("duplicate design/style IDs")

expected_patterns = [f"DS-{i:03d}" for i in range(1, 38)]
if pattern_ids != expected_patterns:
    fail(f"pattern IDs are not the canonical DS-001..DS-037 sequence: {pattern_ids}")

expected_styles = [f"STYLE-{chr(ord('A') + i)}" for i in range(16)]
if style_ids != expected_styles:
    fail(f"style IDs are not the canonical STYLE-A..STYLE-P sequence: {style_ids}")

repos = re.findall(r'repo:\s*"([^"]+)"', oss)
# Preserve the 95-source historical baseline, and audit explicit new intake batches.
ruixen_intake = len(re.findall(r"^\s+batch:\s+RUIXEN_UI_2026_11_13\s*$", oss, re.MULTILINE))
if ruixen_intake != 1:
    fail(f"expected exactly one Ruixen external intake, found {ruixen_intake}")
dock_intake = len(re.findall(r"^  - batch_id: DOCK_WIDGET_2026_11_16$", oss, re.MULTILINE))
if dock_intake != 1:
    fail(f"expected one 2026-11-16 dock intake, found {dock_intake}")
visual_intake = len(re.findall(r"^  - batch_id: STAR_VISUAL_2026_11_16$", oss, re.MULTILINE))
if visual_intake != 1:
    fail(f"expected exactly one 2026-11-16 visual stars intake, found {visual_intake}")
skills_intake = len(re.findall(r"^  - batch_id: ANTI_SLOP_DESIGN_SKILLS_2026_11_17$", oss, re.MULTILINE))
if skills_intake != 1:
    fail(f"expected one 2026-11-17 design skill intake, found {skills_intake}")
expected_source_count = 95 + ruixen_intake + 2 * dock_intake + 7 * visual_intake + 10 * skills_intake
if len(repos) != expected_source_count or len(set(repos)) != expected_source_count:
    fail(f"expected {expected_source_count} unique OSS design sources, found {len(repos)} / {len(set(repos))} unique")
for required in ("ruixenui/ruixen.com", "alztrk/opentaskbar", "Acadbek/lumabar"):
    if repos.count(required) != 1:
        fail(f"external source missing or duplicated: {required}")
if not (ROOT / "sources" / "GITHUB_DOCK_WIDGET_REFERENCE_2026-11-16.md").is_file():
    fail("dock reference audit document is missing")
for required in ("tldraw/tldraw", "excalidraw/excalidraw", "xyflow/xyflow", "markmap/markmap",
                 "alztrk/OpenWidget", "AppFlowy-IO/appflowy-editor", "sorenwacker/nodus"):
    if repos.count(required) != 1:
        fail(f"new visual source missing or duplicated: {required}")
if not (ROOT / "sources" / "STARS_750_VISUAL_INTAKE_2026-11-16.md").is_file():
    fail("2026-11-16 visual stars audit documentation missing")
# 2026-11-17 agent design skills must be registered source-pinned with a bidirectional proposed-only app map.
for required in ("uizze/uizze", "pbakaus/impeccable", "Leonxlnx/taste-skill",
                 "emilkowalski/skills", "vercel-labs/agent-skills", "anthropics/skills",
                 "Nutlope/hallmark", "jakubkrehel/skills",
                 "nextlevelbuilder/ui-ux-pro-max-skill", "benjitaylor/skills"):
    if repos.count(required) != 1:
        fail(f"design skills intake missing or duplicated: {required}")
skills_audit = ROOT / "sources" / "ANTI_SLOP_DESIGN_SKILLS_AUDIT_2026-11-17.md"
skills_map_path = ROOT / "UI-UX" / "MATRICE_REPO_DESIGN_APP_2026-11-17.json"
skills_view = ROOT / "UI-UX" / "MATRICE_REPO_DESIGN_APP_2026-11-17.md"
if not all(p.is_file() for p in (skills_audit, skills_map_path, skills_view)):
    fail("design skill intake audit/map/view missing")
skills_map = json.loads(skills_map_path.read_text(encoding="utf-8"))
skills_sources = skills_map.get("sources", [])
skills_links = skills_map.get("associations", [])
skills_counts = skills_map.get("counts", {})
if skills_map.get("batch_id") != "ANTI_SLOP_DESIGN_SKILLS_2026_11_17":
    fail("design skills map wrong batch id")
if len(skills_sources) != 10 or len({x.get("id") for x in skills_sources}) != 10:
    fail("design skills must have ten unique source IDs")
if {x.get("repo") for x in skills_sources} - set(repos):
    fail("design skill map contains sources absent in OSS registry")
if any(not re.fullmatch(r"[0-9a-f]{40}", str(x.get("ref", ""))) for x in skills_sources):
    fail("design skill source HEAD not pinned to 40-char SHA")
if any(x.get("maturity") != "REFERENCE" for x in skills_sources):
    fail("unverified design skill was prematurely promoted")
if len(skills_links) != skills_counts.get("associations"):
    fail("design skill association count mismatch")
if any(e.get("status") != "PROPOSED_ONLY" or e.get("fit") not in ("HIGH", "MEDIUM")
       for e in skills_links):
    fail("design skill app association promoted without consumer evidence")
if len({(e.get("source_id"), e.get("app")) for e in skills_links}) != len(skills_links):
    fail("duplicate design skill app association")
if {e.get("source_id") for e in skills_links} - {s.get("id") for s in skills_sources}:
    fail("design skill association links to unknown source")
if len(skills_map.get("by_app", {})) != skills_counts.get("apps"):
    fail("design skill by-app view count mismatch")
for app, linked in skills_map.get("by_app", {}).items():
    if {(x.get("source_id"), x.get("fit")) for x in linked} != {
         (e.get("source_id"), e.get("fit")) for e in skills_links if e.get("app") == app}:
        fail(f"design skill by-app links out of sync: {app}")
for source_id, linked in skills_map.get("by_source", {}).items():
    if {(x.get("app"), x.get("fit")) for x in linked} != {
         (e.get("app"), e.get("fit")) for e in skills_links if e.get("source_id") == source_id}:
        fail(f"design skill by-source links out of sync: {source_id}")

ruixen_index = json.loads((ROOT / "sources" / "RUIXEN_UI_REGISTRY_INVENTORY_2026-11-13.json").read_text(encoding="utf-8"))
ruixen_curated = json.loads((ROOT / "sources" / "RUIXEN_UI_CURATED_APP_MAP_2026-11-13.json").read_text(encoding="utf-8"))
files = ruixen_index.get("files", [])
candidates = ruixen_curated.get("items", [])
if len(files) != 277 or len({f.get("slug") for f in files}) != 277:
    fail("Ruixen inventory must contain exactly 277 distinct TSX references")
if len(candidates) != 41 or len({c.get("id") for c in candidates}) != 41:
    fail("Ruixen curated map must contain exactly 41 distinct references")
if len({app for c in candidates for app in c.get("apps", [])}) != 18:
    fail("Ruixen app crosswalk must cover 18 apps")
file_by_slug = {f["slug"]: f for f in files}
for candidate in candidates:
    source = file_by_slug.get(candidate.get("slug"))
    if not source or source.get("blob_sha") != candidate.get("pinned_code_sha"):
        fail(f"Ruixen source mismatch for {candidate.get('id')}")
    if candidate.get("code_imported") or candidate.get("status") != "REFERENCE_NOT_ADOPTED":
        fail(f"Ruixen {candidate.get('id')} prematurely marked as adopted")
if ruixen_index.get("immutable_commit") != ruixen_curated.get("immutable_commit"):
    fail("Ruixen source commit mismatch across catalogues")
if not (ROOT / "sources" / "RUIXEN_UI_DESIGN_MOTION_AUDIT_2026-11-13.md").is_file():
    fail("Ruixen design motion audit missing")

curated_count = len(re.findall(r"^\s+batch:\s+CURATED_2026_10_27\s*$", oss, re.MULTILINE))
if curated_count != 37:
    fail(f"expected 37 sources in CURATED_2026_10_27, found {curated_count}")

source_ref_count = len(re.findall(r'^\s+source_ref:\s+"[0-9a-f]{40}"\s*$', oss, re.MULTILINE))
if source_ref_count < 59:
    fail(f"expected at least 59 pinned curated source refs, found {source_ref_count}")

sound_count = len(re.findall(r"^\s+domain:\s+sound\s*$", oss, re.MULTILINE))
new_batch_count = len(re.findall(r"^\s+batch:\s+CURATED_2026_10_30\s*$", oss, re.MULTILINE))
if new_batch_count != 22:
    fail(f"expected 22 sources in CURATED_2026_10_30, found {new_batch_count}")

if sound_count != 6:
    fail(f"expected 6 curated sound sources, found {sound_count}")

snapshot_paths = re.findall(r"path:\s*([^,}\n]+)", tested)
snapshot_paths = [p.strip() for p in snapshot_paths if p.strip().startswith("tested/source_snapshots/")]
if len(snapshot_paths) != 18:
    fail(f"expected 18 registered source snapshots, found {len(snapshot_paths)}")

for rel in snapshot_paths:
    if not (ROOT / rel).is_file():
        fail(f"registered snapshot missing: {rel}")

coverage_rows = [
    line for line in coverage.splitlines()
    if line.startswith("| ") and not line.startswith("|---") and "App / product" not in line
]
if len(coverage_rows) < 19:
    fail(f"coverage matrix unexpectedly small: {len(coverage_rows)}")

required = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "sources" / "PROJECT_PATTERN_HARVEST.md",
    ROOT / "sources" / "PROJECT_FILE_FRAMEWORKS.md",
    ROOT / "sources" / "GITHUB_DESIGN_RESEARCH_2026-10-27.md",
    ROOT / "sources" / "SOUND_DESIGN_GUIDE.md",
    ROOT / "sources" / "GITHUB_DESIGN_RESEARCH_2026-10-30.md",
    ROOT / "packs" / "ROADMAP_COPY_READY.md",
    ROOT / "packs" / "PACK_REGISTRY.yaml",
    ROOT / "packs" / "motion" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "factory_motion.dart",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "src" / "motion_policy.dart",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "src" / "motion_widgets.dart",
    ROOT / "packs" / "motion" / "flutter" / "test" / "factory_motion_test.dart",
    ROOT / "packs" / "motion" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "motion" / "flutter" / "PROVENANCE.md",
    ROOT / ".github" / "workflows" / "motion-pack-flutter.yml",
    ROOT / "packs" / "sound" / "semantic" / "manifest.json",
    ROOT / "packs" / "sound" / "semantic" / "LICENSE-CC0.txt",
    ROOT / "packs" / "sound" / "semantic" / "validate_assets.py",
    ROOT / "packs" / "sound" / "semantic" / "README.md",
    ROOT / "packs" / "sound" / "semantic" / "PROVENANCE.md",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "factory_sound_flutter.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "semantic_sound.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "audio_backend.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "sound_controller.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "test" / "semantic_sound_test.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / ".github" / "workflows" / "semantic-sound-pack.yml",
    ROOT / "packs" / "icons" / "manifest" / "icons.json",
    ROOT / "packs" / "icons" / "manifest" / "generate.py",
    ROOT / "packs" / "icons" / "manifest" / "test_manifest.py",
    ROOT / "packs" / "icons" / "README.md",
    ROOT / "packs" / "icons" / "PROVENANCE.md",
    ROOT / "packs" / "icons" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "factory_icons.dart",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "src" / "factory_icon_widgets.dart",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "src" / "generated_factory_icon_keys.dart",
    ROOT / "packs" / "icons" / "flutter" / "test" / "factory_icons_test.dart",
    ROOT / "packs" / "icons" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "icons" / "compose" / "build.gradle.kts",
    ROOT / "packs" / "icons" / "compose" / "settings.gradle.kts",
    ROOT / "packs" / "icons" / "compose" / "src" / "main" / "kotlin" / "factory" / "icons" / "GeneratedFactoryIconKeys.kt",
    ROOT / "packs" / "icons" / "compose" / "src" / "main" / "kotlin" / "factory" / "icons" / "FactoryIconWidgets.kt",
    ROOT / "packs" / "icons" / "compose" / "src" / "test" / "kotlin" / "factory" / "icons" / "FactoryIconMappingTest.kt",
    ROOT / ".github" / "workflows" / "icon-adapter-pack.yml",
    ROOT / "packs" / "visual-qa" / "manifest" / "visual_matrix.json",
    ROOT / "packs" / "visual-qa" / "manifest" / "validate_matrix.py",
    ROOT / "packs" / "visual-qa" / "PROVENANCE.md",
    ROOT / "packs" / "visual-qa" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "visual-qa" / "flutter" / "README.md",
    ROOT / "packs" / "visual-qa" / "flutter" / "lib" / "factory_visual_qa.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "lib" / "src" / "qa_fixture.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "support" / "visual_matrix.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "visual_matrix_test.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "visual_golden_test.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "visual-qa" / "compose" / "README.md",
    ROOT / "packs" / "visual-qa" / "swiftui" / "README.md",
    ROOT / ".github" / "workflows" / "visual-qa-flutter.yml",
]
for path in required:
    if not path.is_file():
        fail(f"required file missing: {path.relative_to(ROOT)}")


# Audit hardening: fail closed on stale Factory baselines, identity collisions
# and provenance locators that silently lose their source file or blob hash.
if not re.search(r"commit: e9507056601c4a6751510da4c5d1f61601a5dc25", registry):
    fail("design registry Factory baseline does not match pinned v27")
if not re.search(r'master: "27"', registry):
    fail("design registry Master must be v27")

harvest = (ROOT / "sources" / "PROJECT_PATTERN_HARVEST.md").read_text(encoding="utf-8")
for conflicting in ("### DS-009 — Consumer-first", "### DS-010 — Ethical premium"):
    if conflicting in harvest:
        fail(f"harvest stable ID conflicts with canonical registry: {conflicting}")

ledger = json.loads((ROOT / "registry" / "PATTERN_PROVENANCE.json").read_text(encoding="utf-8"))
if ledger.get("schema_version") != 1:
    fail("unsupported pattern provenance schema")
items = ledger.get("patterns", [])
if [x.get("id") for x in items] != pattern_ids:
    fail("pattern provenance IDs/order do not match canonical DS registry")

for item in items:
    pid = item["id"]
    if item["maturity"] == "SOURCE_VERIFIED" and not item["donor_snapshots"]:
        fail(f"{pid} claims SOURCE_VERIFIED without any immutable snapshot lead")
    if not item["donor_snapshots"] and not item["unverified_donors"]:
        fail(f"{pid} lacks all donor information")
    for source in item["donor_snapshots"]:
        path = ROOT / source["snapshot_path"]
        if not path.is_file() or not path.resolve().is_relative_to((ROOT / "tested" / "source_snapshots").resolve()):
            fail(f"{pid} has invalid snapshot path {path}")
        payload = path.read_text(encoding="utf-8")
        expected_fields = {
            "source_path": source["source_path"],
            "source_blob": source["git_blob_sha"],
            "source_repo": source["repo"],
        }
        if len(source["git_blob_sha"]) != 40 or not re.fullmatch(r"[0-9a-f]{40}", source["git_blob_sha"]):
            fail(f"{pid}: invalid immutable source blob")
        for field, value in expected_fields.items():
            if f"{field}: {value}\n" not in payload:
                fail(f"{pid} source provenance not supported by {source['snapshot_path']}")

# Every check intended for branch rulesets must exist on every PR;
# path-filtered pack workflows cannot safely be mandatory branch checks.
workflows = [
    ".github/workflows/validate.yml",
    ".github/workflows/motion-pack-flutter.yml",
    ".github/workflows/semantic-sound-pack.yml",
    ".github/workflows/icon-adapter-pack.yml",
    ".github/workflows/visual-qa-flutter.yml",
]
for rel in workflows:
    body = (ROOT / rel).read_text(encoding="utf-8")
    if "  pull_request:" not in body:
        fail(f"mandatory workflow does not run on every PR: {rel}")
    if re.search(r"  pull_request:\n    paths:", body):
        fail(f"path-filtered required workflow: {rel}")
    for use in re.findall(r"^\s*- uses:\s*([^\s#]+)", body, re.MULTILINE):
        if "@" not in use or not re.fullmatch(r"[0-9a-f]{40}", use.rsplit("@", 1)[-1]):
            fail(f"un-pinned action in {rel}: {use}")

for rel in (
    "docs/GITHUB_BRANCH_PROTECTION.md",
    "docs/LICENSE_POLICY.md",
    "docs/AUDIT_REMEDIATION_v1.md",
    "registry/PATTERN_PROVENANCE.json",
):
    if not (ROOT / rel).is_file():
        fail(f"audit hardening document missing: {rel}")

# Provenance files must not contain contradictory duplicate evidence scalars.
visual_provenance = (ROOT / "packs/visual-qa/PROVENANCE.md").read_text(encoding="utf-8")
if visual_provenance.count("evidence:") != 1:
    fail("visual QA provenance has duplicate or missing evidence metadata")

print(
    f"Design-App validation PASS: {len(pattern_ids)} patterns, "
    f"{len(style_ids)} styles, {len(repos)} OSS sources "
    f"({curated_count}+{new_batch_count} curated, {sound_count} sound), "
    f"{len(snapshot_paths)} snapshots, {len(coverage_rows)} covered products."
)
