#!/usr/bin/env python3
from pathlib import Path
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
]
for path in required:
    if not path.is_file():
        fail(f"required file missing: {path.relative_to(ROOT)}")

print(
    f"Design-App validation PASS: {len(pattern_ids)} patterns, "
    f"{len(style_ids)} styles, {len(repos)} OSS sources "
    f"({curated_count}+{new_batch_count} curated, {sound_count} sound), "
    f"{len(snapshot_paths)} snapshots, {len(coverage_rows)} covered products."
)
