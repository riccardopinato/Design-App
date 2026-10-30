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
if len(repos) != 95 or len(set(repos)) != 95:
    fail(f"expected 95 unique OSS design sources, found {len(repos)} / {len(set(repos))} unique")

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
