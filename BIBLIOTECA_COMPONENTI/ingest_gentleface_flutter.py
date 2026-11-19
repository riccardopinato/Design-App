#!/usr/bin/env python3
"""Archive ORIGINAL official MIT SVG + NATIVE Flutter source for 28 Gentleface UIDs.

Sources are fetched by canonical URL, inspected, hashed, stored separately and
never invented. Existing React/CSS/HTML archives are untouched. This is not a
consumer integration or a Flutter Golden certification.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "BIBLIOTECA_COMPONENTI"
CATFILE = BASE / "CATALOGO.json"
VARFILE = BASE / "FLUTTER_VARIANTS.json"
ORIGINALS = BASE / "sorgenti" / "gentleface"
DARTS = BASE / "flutter_adapters" / "lib" / "src" / "gentleface"
BARREL = BASE / "flutter_adapters" / "lib" / "design_app_flutter_adapters.dart"
PROVENANCE = ORIGINALS / "PROVENIENZA.json"
UIDFILE = BASE / "UID_REGISTRY.json"


def fetch(url: str) -> bytes:
    with urlopen(Request(url, headers={"User-Agent": "AppFactory-SourceAudit/1.0"}), timeout=24) as res:
        if res.status != 200:
            raise ValueError(f"Unexpected HTTP {res.status}: {url}")
        data = res.read()
    if not data or len(data) > 500000:
        raise ValueError(f"Source missing/unexpectedly large: {url}")
    return data


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def run():
    catalog = json.loads(CATFILE.read_text(encoding="utf-8"))
    variants = json.loads(VARFILE.read_text(encoding="utf-8"))
    original = [x for x in catalog["components"] if x["source_site"] == "GENTLEFACE"]
    assert len(original) == 28, "Cannot change Gentleface baseline silently"
    assert all(x["archive_state"] == "REFERENCE_ONLY" for x in original)
    uids = {x["canonical_id"]: x["uid"] for x in json.loads(UIDFILE.read_text(encoding="utf-8"))["entries"]}
    rows = {}
    payloads = {}
    dart_names = set()
    for icon in original:
        cid = icon["id"]
        slug_match = re.fullmatch("https://gentleface[.]com/icons/([a-z0-9-]+)", icon["source_url"])
        if not slug_match:
            raise ValueError(cid + ": canonical official icon link absent")
        slug = slug_match.group(1)
        markdown_url = icon["source_url"] + ".md"
        svg_url = f"https://gentleface.com/svg/line-round/16/{slug}.svg"
        markdown = fetch(markdown_url)
        source = markdown.decode("utf-8")
        matches = re.findall(r"\x60{3}(?:dart|flutter)[^\n]*\n([\s\S]*?)\x60{3}", source, re.IGNORECASE)
        if len(matches) != 1:
            raise ValueError(f"{cid}: expected exactly one official native Dart block, got {len(matches)}")
        dart = matches[0].strip() + "\n"
        if (f'Gentleface "{slug}"' not in dart or "MIT" not in dart
                or "import 'package:flutter/widgets.dart';" not in dart
                or "extends StatelessWidget" not in dart or "CustomPainter" not in dart):
            raise ValueError(cid + ": invalid or unlicensed official Flutter source")
        if re.search(r"import ['\"](?!package:flutter/)", dart):
            raise ValueError(cid + ": unexpected external package dependency")
        classes = re.findall(r"class\s+(\w+)\s+extends\s+StatelessWidget", dart)
        if len(classes) != 1 or classes[0] in dart_names:
            raise ValueError(cid + ": missing/duplicate Flutter exported class")
        dart_names.add(classes[0])
        svg = fetch(svg_url)
        if (b"<svg" not in svg or b"</svg>" not in svg or
                not any(tag in svg for tag in (b"<path", b"<rect", b"<line", b"<circle", b"<polyline", b"<polygon"))):
            raise ValueError(cid + ": cannot verify source SVG semantics")
        original_path = f"BIBLIOTECA_COMPONENTI/sorgenti/gentleface/{cid}.svg"
        flutter_path = f"BIBLIOTECA_COMPONENTI/flutter_adapters/lib/src/gentleface/{cid.lower().replace('-', '_')}.dart"
        rows[cid] = {
            "uid": uids[cid], "slug": slug, "source_page": icon["source_url"],
            "original_markdown_url": markdown_url, "original_svg_url": svg_url,
            "original_svg_path": original_path, "native_flutter_path": flutter_path,
            "official_exported_class": classes[0],
            "markdown_sha256": sha256(markdown),
            "original_svg_sha256": sha256(svg),
            "original_svg_git_blob_sha": git_sha(svg),
            "native_flutter_sha256": sha256(dart.encode("utf-8")),
            "license": "MIT (official Gentleface source)",
            "pinning": "LIVE_SOURCE_HASHED_NOT_GIT_COMMIT_PINNED",
            "consumer_runtime": "NOT_VERIFIED",
        }
        payloads[cid] = (svg, dart)
        print("STAGED", cid, classes[0], len(svg), len(dart))
    assert len(rows) == len(payloads) == 28, "partial intake refused"
    # Commit only AFTER ALL 28 originals + native code were acquired.
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    DARTS.mkdir(parents=True, exist_ok=True)
    for cid, (svg, dart) in payloads.items():
        (ROOT / rows[cid]["original_svg_path"]).write_bytes(svg)
        (ROOT / rows[cid]["native_flutter_path"]).write_text(dart, encoding="utf-8")
    PROVENANCE.write_text(json.dumps({
        "schema_version": 1, "provider": "gentleface.com", "license": "MIT",
        "source_commit": None, "source_version": "LIVE_SOURCE_HASHED_NOT_GIT_COMMIT_PINNED",
        "entries": rows,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for icon in original:
        cid = icon["id"]
        icon["archive_path"] = rows[cid]["original_svg_path"]
        icon["archive_state"] = "ARCHIVED_SOURCE"
        icon["source_repo"] = "gentleface.com"
        icon["source_path"] = "/svg/line-round/16/" + rows[cid]["slug"] + ".svg"
        icon["source_blob_sha"] = rows[cid]["original_svg_git_blob_sha"]
        icon["license_status"] = "MIT_OFFICIAL_SVG_SOURCE_ARCHIVED"
        icon["language"] = "SVG (original, archived)"
        icon["notes"] = icon.get("notes", "") + " Original MIT SVG source archived with SHA256; official Dart variant stored independently (LIVE hash, not commit-pinned)."
        variant = variants["components"][cid]
        assert variant["flutter_status"] == "SOURCE_NOT_ARCHIVED" and variant["flutter_code_path"] is None
        variant["original_source_path"] = rows[cid]["original_svg_path"]
        variant["original_language"] = icon["language"]
        variant["original_license"] = icon["license_status"]
        variant["flutter_code_path"] = rows[cid]["native_flutter_path"]
        variant["flutter_status"] = "NATIVE_DART_SOURCE_ARCHIVED_UNVERIFIED_CONSUMER"
    counts = catalog["counts"]
    assert counts["archived_originals"] == 427 and counts["referenced_only"] == 53
    assert counts["by_language"]["SVG / motion asset (not imported)"] == 28
    counts["archived_originals"] = 455
    counts["referenced_only"] = 25
    del counts["by_language"]["SVG / motion asset (not imported)"]
    counts["by_language"]["SVG (original, archived)"] = 28
    CATFILE.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    VARFILE.write_text(json.dumps(variants, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    barrel = BARREL.read_text(encoding="utf-8")
    for cid in sorted(rows):
        export = f"export 'src/gentleface/{cid.lower().replace('-', '_')}.dart';"
        if export not in barrel:
            barrel += export + "\n"
    BARREL.write_text(barrel, encoding="utf-8")
    print("GENTLEFACE_NATIVE_INTAKE", len(rows), "MIT SVG originals + 28 distinct Dart widgets")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
