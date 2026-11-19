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

    # Additional MIT original sources: Amicro, Watermelon, EaseUI.
    extra_file = ROOT / "BIBLIOTECA_COMPONENTI" / "sorgenti" / "PROVENIENZA_OSS_EXTRA_2026-11-19.json"
    extra = json.loads(extra_file.read_text(encoding="utf-8"))
    sources = extra.get("source_repositories", {})
    approved = {"amicro": 30, "watermelon": 7, "easeui": 1}
    if set(sources) != set(approved):
        errors.append("unexpected MIT source provider set")
    for provider, info in sources.items():
        licpath = ROOT / str(info.get("license_path", ""))
        if not licpath.is_file():
            errors.append(f"{provider}: LICENSE notice missing")
            continue
        data = licpath.read_bytes()
        if b"MIT License" not in data:
            errors.append(f"{provider}: expected MIT notice not present")
        if git_blob_sha(data) != info.get("license_sha"):
            errors.append(f"{provider}: LICENSE differs from pinned source")
        if not SHA40.fullmatch(str(info.get("commit", ""))):
            errors.append(f"{provider}: source commit is not immutable SHA40")
    external = extra.get("entries", [])
    if len(external) != sum(approved.values()):
        errors.append("external source entry count must be 38")
    ids_extra = set()
    paths_extra = set()
    count_by_provider = {k: 0 for k in approved}
    for row in external:
        cid = row.get("id", "")
        provider = row.get("provider")
        if cid in ids_extra:
            errors.append(f"duplicate MIT source entry {cid}")
        ids_extra.add(cid)
        if provider not in approved:
            errors.append(f"{cid}: unknown source provider {provider}")
            continue
        count_by_provider[provider] += 1
        record = by_id.get(cid)
        if record is None:
            errors.append(f"{cid}: missing catalog component")
            continue
        local = row.get("archive_path")
        if record.get("archive_path") != local or record.get("archive_state") != "ARCHIVED_SOURCE":
            errors.append(f"{cid}: archive-state/path mismatch with manifest")
            continue
        if record.get("source_repo") != row.get("source_repository"):
            errors.append(f"{cid}: original repository mismatch")
        if record.get("source_commit") != row.get("source_commit"):
            errors.append(f"{cid}: original commit mismatch")
        if record.get("source_path") != row.get("source_path"):
            errors.append(f"{cid}: original file path mismatch")
        if record.get("source_blob_sha") != row.get("source_blob_sha"):
            errors.append(f"{cid}: pinned source blob mismatch")
        expected = sources[provider]
        if row.get("source_repository") != expected.get("repository") or row.get("source_commit") != expected.get("commit"):
            errors.append(f"{cid}: provider origin mismatch")
        if row.get("license_path") != expected.get("license_path"):
            errors.append(f"{cid}: license path mismatch")
        physical = ROOT / str(local or "")
        try:
            physical_resolved = physical.resolve()
            physical_resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{cid}: unsafe archive path")
            continue
        if not physical_resolved.is_file():
            errors.append(f"{cid}: source file missing")
            continue
        checksum = git_blob_sha(physical_resolved.read_bytes())
        if checksum != row.get("source_blob_sha"):
            errors.append(f"{cid}: source bytes drift from original {checksum}")
        paths_extra.add(str(physical_resolved))
    if count_by_provider != approved:
        errors.append(f"provider source totals mismatch: {count_by_provider}")
    actual_extra = set()
    for provider in approved:
        actual_extra.update(
            str(path.resolve()) for path in
            (ROOT / "BIBLIOTECA_COMPONENTI" / "sorgenti" / provider).glob("*.tsx")
        )
    if paths_extra != actual_extra:
        errors.append("external source files differ from provenance manifest")
    # Pin original Forui sources and license without upgrading them to a Flutter Golden.
    native_path = ROOT / "BIBLIOTECA_COMPONENTI/sorgenti/forui/PROVENIENZA.json"
    if not native_path.is_file():
        errors.append("Forui upstream provenance missing")
    else:
        native = json.loads(native_path.read_text(encoding="utf-8"))
        if native.get("source_repo") != "duobaseio/forui" or native.get("source_commit") != "5dbf97c926a53fcfe3436db1be6262ac40961db5":
            errors.append("Forui immutable source SHA/repository drift")
        entries = native.get("entries", [])
        expected = {"button.dart", "text_form_field.dart", "demo_button.dart", "demo_login_form.dart", "LICENSE"}
        if len(entries) != 5 or {Path(e.get("local_path", "")).name for e in entries} != expected:
            errors.append("Forui five-file original source inventory mismatch")
        for e in entries:
            path = ROOT / e.get("local_path", "")
            if not path.is_file() or git_blob_sha(path.read_bytes()) != e.get("source_blob_sha"):
                errors.append("Forui archived original SHA mismatch: " + e.get("local_path", ""))
        license_path = ROOT / "BIBLIOTECA_COMPONENTI/sorgenti/forui/LICENSE"
        if license_path.is_file() and b"MIT License" not in license_path.read_bytes():
            errors.append("Forui MIT notice missing")
    if counter.get("FLUTTER_FORUI") != 2:
        errors.append("expected exactly two Forui native Flutter references")
    for cid in ("FUI-001", "FUI-002"):
        c = by_id.get(cid)
        if not c or c.get("source_site") != "FLUTTER_FORUI" or c.get("archive_state") != "ARCHIVED_SOURCE":
            errors.append(cid + ": source state mismatch")
    if catalog.get("counts", {}).get("archived_originals") != 427:
        errors.append("expected 427 archived originals including Forui")
    if catalog.get("counts", {}).get("referenced_only") != 53:
        errors.append("expected 53 remaining references after MIT batch")

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
