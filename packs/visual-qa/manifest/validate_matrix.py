#!/usr/bin/env python3
"""Check visual QA matrix policy and 4 committed PNG baselines."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[3]
folder = Path(__file__).resolve().parent
data = json.loads((folder / "visual_matrix.json").read_text(encoding="utf-8"))
assert data["schema_version"] == 1
cases = data["scenarios"]
assert len(cases) == 9
ids = [c["id"] for c in cases]
assert len(ids) == len(set(ids))
assert len(data["states"]) == 5
assert len(ids) * len(data["states"]) == 45
assert any(c.get("theme") == "dark" for c in cases)
assert any(c.get("text_scale", 1) >= 2 for c in cases)
assert any(c.get("ime_bottom", 0) > 0 for c in cases)
assert any(c.get("ad_slot", False) for c in cases)
assert any(c.get("width", 0) > 600 for c in cases)
dart_matrix = (root / data["targets"]["flutter"]["harness"]).read_text(encoding="utf-8")
for id_ in ids:
    assert "id: '" + id_ + "'" in dart_matrix, id_
expected_png = data["baselines"]
assert len(expected_png) == 4 and len(set(expected_png)) == 4
assert data["snapshot_policy"]["committed_images_required"] is True
baseline_dir = root / "packs/visual-qa/flutter/test/goldens"
for stem in expected_png:
    path = baseline_dir / (stem + ".png")
    assert path.is_file(), "Missing immutable baseline: " + str(path)
    raw = path.read_bytes()
    assert raw[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG signature: " + str(path)
    assert len(raw) > 500, "Suspiciously tiny golden baseline: " + str(path)
    assert not re.search(r"[^a-z0-9-]", stem)
extras = sorted(p.name for p in baseline_dir.glob("*.png")
               if p.stem not in expected_png)
assert not extras, "Unexpected baselines: " + str(extras)
print("Visual QA manifest PASS: 9 screen scenarios x 5 states; 4 pinned golden PNGs")
