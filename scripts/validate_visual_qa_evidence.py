#!/usr/bin/env python3
"""Fail-closed proposed design pilot / visual evidence metadata validator.

Does not run AppLab, inspect screenshots or certify user interfaces.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "UI-UX" / "DESIGN_QA_PILOTS_2026-11-17.json"
EXPECTED_GATES = [f"IWC-{x:02d}" for x in range(1, 9)]
EXPECTED_REPOS = {"riccardopinato/Agenda-per-Anna", "riccardopinato/Android-Omni-Cleaner"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
VALID_STATES = {"PLANNED", "CAPTURED", "REVIEWED", "PASS", "FAIL",
                "BLOCKED", "NOT_VERIFIED", "NOT_APPLICABLE"}


def validate(document: dict) -> list[str]:
    errors: list[str] = []
    if document.get("schema_version") != 1:
        errors.append("unsupported schema_version")
    if document.get("gates") != EXPECTED_GATES:
        errors.append("Impeccable IWC-01..IWC-08 required once and in order")
    if document.get("design_source_id") != "DSK-002":
        errors.append("must preserve canonical Impeccable DSK-002 identity")
    if not SHA40.fullmatch(str(document.get("factory_baseline", ""))):
        errors.append("missing pinned factory baseline")
    if not SHA40.fullmatch(str(document.get("design_source_merge", ""))):
        errors.append("missing immutable source merge")
    if document.get("candidate_only") is not True:
        errors.append("this design intake must stay candidate_only until adoption")
    pilots = document.get("pilots")
    if not isinstance(pilots, list) or {p.get("repository") for p in pilots} != EXPECTED_REPOS:
        errors.append("exactly Anna and Omni pilot repositories are required")
        return errors
    if len(pilots) != len(EXPECTED_REPOS):
        errors.append("duplicate pilot repository")
    for pilot in pilots:
        label = pilot.get("app", "unnamed")
        if not SHA40.fullmatch(str(pilot.get("source_sha", ""))):
            errors.append(f"{label}: source_sha must be immutable 40-char SHA")
        screens = pilot.get("screens", [])
        if not isinstance(screens, list) or not screens or len(screens) != len(set(screens)):
            errors.append(f"{label}: target screens missing or duplicated")
        if not pilot.get("product_authority"):
            errors.append(f"{label}: product authority missing")
        if pilot.get("overall_status") not in VALID_STATES:
            errors.append(f"{label}: invalid overall status")
        captures = pilot.get("screenshots", [])
        runtime = pilot.get("runtime_evidence", [])
        physical = pilot.get("physical_evidence", [])
        if not all(isinstance(x, list) for x in (captures, runtime, physical)):
            errors.append(f"{label}: evidence collections must be arrays")
            continue
        if pilot.get("overall_status") == "CAPTURED" and not captures:
            errors.append(f"{label}: CAPTURED requires screenshots")
        for j, item in enumerate(captures):
            if not isinstance(item, dict):
                errors.append(f"{label}: screenshot[{j}] must be object")
                continue
            required = ("screen_id", "source_sha", "platform", "fixture_id",
                        "viewport", "locale", "theme", "font_scale", "state", "status")
            if any(not item.get(k) for k in required):
                errors.append(f"{label}: screenshot[{j}] incomplete context")
            if item.get("screen_id") not in screens:
                errors.append(f"{label}: screenshot[{j}] unknown screen")
            if item.get("status") not in VALID_STATES:
                errors.append(f"{label}: screenshot[{j}] invalid status")
            if item.get("status") in {"REVIEWED", "PASS"}:
                if not all(item.get(k) for k in (
                    "before_image", "after_image", "reviewer", "reviewed_at", "test_run_url",
                )):
                    errors.append(f"{label}: screenshot[{j}] lacks reviewed before/after evidence")
                if not SHA40.fullmatch(str(item.get("source_sha", ""))) or (
                    item.get("source_sha") != pilot.get("source_sha")
                ):
                    errors.append(f"{label}: screenshot[{j}] source SHA mismatches pilot")
                before_sha = item.get("before_source_sha")
                if before_sha is not None and not SHA40.fullmatch(str(before_sha)):
                    errors.append(f"{label}: screenshot[{j}] invalid before_source_sha")
        if pilot.get("overall_status") in {"PASS", "REVIEWED"}:
            complete = {
                item.get("screen_id") for item in captures if isinstance(item, dict)
                and item.get("status") in {"REVIEWED", "PASS"}
                and item.get("source_sha") == pilot.get("source_sha")
                and all(item.get(k) for k in (
                    "before_image", "after_image", "reviewer", "reviewed_at", "test_run_url",
                ))
            }
            if not pilot.get("reviewer_approval") or complete != set(screens):
                errors.append(f"{label}: cannot mark visually approved without reviewed captures for every screen and reviewer")
        if (runtime or physical) and not captures:
            errors.append(f"{label}: runtime/physical reference with no visual capture")
    reuse = document.get("reuse_candidates", [])
    if not isinstance(reuse, list) or len({p.get("id") for p in reuse}) != len(reuse):
        errors.append("reuse candidates missing or duplicate IDs")
    for entry in reuse:
        if entry.get("maturity") in {"SOURCE_VERIFIED", "LIBRARY_VERIFIED", "COPY_READY"} and not entry.get("consumer_evidence"):
            errors.append(f"{entry.get('id')}: promotion without consumer evidence")
        if entry.get("mode") not in {"REFERENCE_ONLY", "ADAPT", "COPY"}:
            errors.append(f"{entry.get('id')}: unsupported reuse mode")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    doc = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = validate(doc)
    if args.self_test:
        import copy
        promoted = copy.deepcopy(doc)
        promoted["pilots"][0]["overall_status"] = "PASS"
        promoted["pilots"][0]["screenshots"] = []
        promoted["pilots"][0]["reviewer_approval"] = None
        assert any("cannot mark visually approved" in x for x in validate(promoted))
        reused = copy.deepcopy(doc)
        reused["reuse_candidates"][0]["maturity"] = "COPY_READY"
        reused["reuse_candidates"][0]["consumer_evidence"] = []
        assert any("promotion without consumer evidence" in x for x in validate(reused))
        mismatch = copy.deepcopy(doc)
        mismatch["pilots"][0]["screenshots"] = [{
            "screen_id": mismatch["pilots"][0]["screens"][0],
            "source_sha": "f" * 40,
            "platform": "Flutter",
            "fixture_id": "synthetic",
            "viewport": "390x844",
            "locale": "it",
            "theme": "light",
            "font_scale": "1.0",
            "state": "populated",
            "status": "PASS",
            "before_image": "before.png",
            "after_image": "after.png",
            "reviewer": "test",
            "reviewed_at": "2026-11-17",
            "test_run_url": "https://github.com/example/test/actions/runs/1",
        }]
        assert any("source SHA mismatches pilot" in x for x in validate(mismatch))
        missing = copy.deepcopy(doc)
        missing["gates"] = missing["gates"][:-1]
        assert any("IWC-01" in x for x in validate(missing))
        print("Visual QA negative-case self-tests: PASS")
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    print("Visual QA manifest metadata: PASS (candidate planning only, NO visual runtime certification)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
