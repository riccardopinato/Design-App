#!/usr/bin/env python3
"""Fail closed on every original/Flutter side-by-side reference in Design-App."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "BIBLIOTECA_COMPONENTI"
CAT = json.loads((HERE / "CATALOGO.json").read_text(encoding="utf-8"))
UID = json.loads((HERE / "UID_REGISTRY.json").read_text(encoding="utf-8"))
DATA = json.loads((HERE / "FLUTTER_VARIANTS.json").read_text(encoding="utf-8"))
BY_ID = {c["id"]: c for c in CAT["components"]}
BY_UID = {row["canonical_id"]: row["uid"] for row in UID["entries"]}
PORTS = {
    "RXN-animated-gradient-text": "rxn_animated_gradient_text.dart",
    "RXN-animated-circular-progress-bar": "rxn_animated_circular_progress_bar.dart",
    "UIV-002": "uiv_002_gradient_pill_button.dart",
    "RXN-animated-link": "rxn_animated_link.dart",
    "RXN-accordion-editorial": "rxn_accordion_editorial.dart",
    "UIV-009": "uiv_009_book_card.dart",
    "RXN-animated-shiny-text": "rxn_animated_shiny_text.dart",
}
assert DATA["component_total"] == len(BY_ID) == len(BY_UID) == 480
assert set(DATA["components"]) == set(BY_ID)
assert [x["uid"] for x in DATA["components"].values()] == [
    BY_UID[c["id"]] for c in CAT["components"]
], "UID mapping must stay stable and append-only"
counts = {}
for cid, row in DATA["components"].items():
    source = BY_ID[cid]
    assert row["uid"] == BY_UID[cid], cid
    assert row["original_source_path"] == source.get("archive_path"), cid
    assert row["original_language"] == source["language"], cid
    assert row["original_license"] == source.get("license_status"), cid
    assert row["consumer_runtime"] == "NOT_VERIFIED", cid
    state = row["flutter_status"]
    assert state in {"PENDING_FLUTTER_REWRITE", "NATIVE_DART_DEPENDENCY_GATE",
                     "NATIVE_DART_SOURCE_ARCHIVED_UNVERIFIED_CONSUMER",
                     "SOURCE_NOT_ARCHIVED", "ADAPTER_DRAFT_UNVERIFIED_CONSUMER"}, cid
    counts[state] = counts.get(state, 0) + 1
    fpath = row.get("flutter_code_path")
    if state == "NATIVE_DART_SOURCE_ARCHIVED_UNVERIFIED_CONSUMER":
        assert source["source_site"] == "GENTLEFACE", cid
        assert fpath and fpath.startswith("BIBLIOTECA_COMPONENTI/flutter_adapters/lib/src/gentleface/"), cid
        assert source["archive_state"] == "ARCHIVED_SOURCE", cid
    elif state == "ADAPTER_DRAFT_UNVERIFIED_CONSUMER":
        assert cid in PORTS and fpath and Path(fpath).name == PORTS[cid], cid
    elif state == "NATIVE_DART_DEPENDENCY_GATE":
        assert source["source_site"] == "FLUTTER_FORUI" and fpath == source["archive_path"], cid
    else:
        assert fpath is None, cid
        if state == "SOURCE_NOT_ARCHIVED":
            assert source["archive_state"] == "REFERENCE_ONLY", cid
    if fpath:
        p = (ROOT / fpath).resolve()
        p.relative_to(ROOT.resolve())
        assert p.is_file() and p.suffix == ".dart", cid
    if source["archive_state"] == "ARCHIVED_SOURCE":
        p = (ROOT / source["archive_path"]).resolve()
        p.relative_to(ROOT.resolve())
        assert p.is_file(), cid
assert counts["ADAPTER_DRAFT_UNVERIFIED_CONSUMER"] == 7
assert counts["NATIVE_DART_DEPENDENCY_GATE"] == 2
assert counts["NATIVE_DART_SOURCE_ARCHIVED_UNVERIFIED_CONSUMER"] == 28
print("PASS 480 originals/Flutter column records:", counts)
