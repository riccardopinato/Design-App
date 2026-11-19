#!/usr/bin/env python3
"""Validate component identity, archive integrity, aliases and source registry.

Source snapshots are not runtime Flutter/UI certifications.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "BIBLIOTECA_COMPONENTI" / "CATALOGO.json"
PROVENANCE = ROOT / "BIBLIOTECA_COMPONENTI" / "sorgenti" / "ruixen" / "PROVENIENZA.json"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def git_blob_sha(contents: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(contents)).encode("ascii") +
                        b"\0" + contents).hexdigest()


def validate() -> list[str]:
    errors = []
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    rows = catalog.get("components", [])
    aliases = catalog.get("aliases", {})
    if catalog.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(rows, list) or not rows:
        return ["catalog must contain components"]
    by_id = {}
    physical_ruixen = {}
    counter = {}
    archive_count = 0
    for entry in rows:
        id = entry.get("id")
        if not isinstance(id, str) or not id:
            errors.append("empty component ID")
            continue
        if id in by_id:
            errors.append(f"duplicate canonical ID: {id}")
        by_id[id] = entry
        src = entry.get("source_site")
        counter[src] = counter.get(src, 0) + 1
        state = entry.get("archive_state")
        local = entry.get("archive_path")
        if state not in {"ARCHIVED_SOURCE", "REFERENCE_ONLY"}:
            errors.append(f"{id}: invalid archive state")
        if (state == "ARCHIVED_SOURCE") != bool(local):
            errors.append(f"{id}: archived status/path mismatch")
        if not local:
            continue
        archive_count += 1
        path = ROOT / local
        try:
            resolved = path.resolve()
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{id}: unsafe local path")
            continue
        if not resolved.is_file():
            errors.append(f"{id}: archive file missing {local}")
            continue
        if src == "RUIXEN":
            if not SHA40.fullmatch(str(entry.get("source_blob_sha") or "")):
                errors.append(f"{id}: missing pinned source SHA")
                continue
            checksum = git_blob_sha(resolved.read_bytes())
            if checksum != entry["source_blob_sha"]:
                errors.append(f"{id}: changed original SHA: {checksum}")
            physical_ruixen[id] = str(resolved)
    if len(rows) != catalog.get("counts", {}).get("unique_components"):
        errors.append("unique component count is inconsistent")
    if archive_count != catalog.get("counts", {}).get("archived_originals"):
        errors.append("archived count is inconsistent")
    if len(rows) - archive_count != catalog.get("counts", {}).get("referenced_only"):
        errors.append("reference-only count is inconsistent")
    if counter != catalog.get("counts", {}).get("by_source"):
        errors.append("source counts inconsistent")
    for alias, info in aliases.items():
        if alias in by_id:
            errors.append(f"alias duplicates canonical ID: {alias}")
        target = info.get("canonical_id")
        if target not in by_id:
            errors.append(f"alias points to absent canonical ID: {alias} -> {target}")
    if len(aliases) != catalog.get("counts", {}).get("aliases"):
        errors.append("alias count inconsistent")

    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    entries = provenance.get("entries", [])
    if provenance.get("source_repository") != "ruixenui/ruixen.com":
        errors.append("unexpected Ruixen upstream")
    if provenance.get("license") != "MIT":
        errors.append("Ruixen license not recorded as MIT")
    lic = ROOT / provenance.get("license_path", "")
    if not lic.is_file() or "MIT" not in lic.read_text(encoding="utf-8"):
        errors.append("MIT license notice missing")
    if len(entries) != 277 or counter.get("RUIXEN") != 277 or len(physical_ruixen) != 277:
        errors.append("all 277 Ruixen originals must exist")
    for x in entries:
        item = by_id.get(x.get("id"))
        if not item or item["archive_path"] != x.get("local_path"):
            errors.append(f"mismatched Ruixen provenance for {x.get('id')}")
        elif item["source_blob_sha"] != x.get("source_blob_sha"):
            errors.append(f"source pin changed for {x.get('id')}")
    registered_paths = set(physical_ruixen.values())
    real_paths = {str(x.resolve()) for x in
                  (ROOT / "BIBLIOTECA_COMPONENTI" / "sorgenti" / "ruixen").glob("*.tsx")}
    if registered_paths != real_paths:
        errors.append(f"Ruixen file inventory mismatch, extra={len(real_paths-registered_paths)}")

    return errors


def main() -> int:
    errs = validate()
    if errs:
        for msg in errs[:35]:
            print("ERROR:", msg, file=sys.stderr)
        return 1
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    counts = catalog["counts"]
    print(f"PASS catalogo: {counts['unique_components']} canonici, "
          f"{counts['aliases']} alias, {counts['archived_originals']} sorgenti, "
          f"{counts['referenced_only']} reference-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
