#!/usr/bin/env python3
from pathlib import Path
import re
import sys

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

expected_patterns = [f"DS-{i:03d}" for i in range(1, 26)]
if pattern_ids != expected_patterns:
    fail(f"pattern IDs are not the canonical DS-001..DS-025 sequence: {pattern_ids}")

expected_styles = [f"STYLE-{chr(ord('A') + i)}" for i in range(16)]
if style_ids != expected_styles:
    fail(f"style IDs are not the canonical STYLE-A..STYLE-P sequence: {style_ids}")

repos = re.findall(r'\{repo:\s*"([^"]+)"', oss)
if len(repos) != 36 or len(set(repos)) != 36:
    fail(f"expected 36 unique OSS design sources, found {len(repos)} / {len(set(repos))} unique")

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
]
for path in required:
    if not path.is_file():
        fail(f"required file missing: {path.relative_to(ROOT)}")

print(
    f"Design-App validation PASS: {len(pattern_ids)} patterns, "
    f"{len(style_ids)} styles, {len(repos)} OSS sources, "
    f"{len(snapshot_paths)} snapshots, {len(coverage_rows)} covered products."
)
