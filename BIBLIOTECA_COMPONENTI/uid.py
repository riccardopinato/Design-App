#!/usr/bin/env python3
"""UID resolver and safe adoption manifest for Design-App.

Use from repository root:
  python BIBLIOTECA_COMPONENTI/uid.py lookup UID-0127
  python BIBLIOTECA_COMPONENTI/uid.py plan UID-0350 --app annas-diary --stack flutter --role login
  python BIBLIOTECA_COMPONENTI/uid.py search --text button --limit 12
  python BIBLIOTECA_COMPONENTI/uid.py validate

A source file is NOT a Flutter/Compose drop-in just because it is archived.
This tool never changes consumer apps or promotes experimental code.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UIDFILE = HERE / "UID_REGISTRY.json"
CATFILE = HERE / "CATALOGO.json"
PREVIEWFILE = HERE / "ANTEPRIME.json"
ORIGINSFILE = HERE / "ANTEPRIME_ORIGINI.json"
APP_ALIASES = {"anna-s-diary": "annas-diary"}


def canonical_app(value: str) -> str:
    return APP_ALIASES.get(value.lower().replace("'", "").replace(" ", "-"), value.lower())


def read() -> tuple[dict, dict, dict, dict]:
    uid = json.loads(UIDFILE.read_text(encoding="utf-8"))
    cat = json.loads(CATFILE.read_text(encoding="utf-8"))
    pv = json.loads(PREVIEWFILE.read_text(encoding="utf-8"))["previews"]
    origins = json.loads(ORIGINSFILE.read_text(encoding="utf-8")).get("previews", {}) if ORIGINSFILE.exists() else {}
    return uid, cat, pv, origins


def index(uid: dict, cat: dict) -> tuple[dict, dict]:
    rows = {x["id"]: x for x in cat["components"]}
    uid2id = {}
    id2uid = {}
    for item in uid["entries"]:
        key, cid = item["uid"], item["canonical_id"]
        if not re.fullmatch(r"UID-[0-9]{4,}", key):
            raise ValueError("UID format invalid: " + key)
        if cid not in rows or key in uid2id or cid in id2uid:
            raise ValueError("UID alias collision or missing catalog component: " + key)
        uid2id[key] = cid
        id2uid[cid] = key
    if len(uid2id) != len(rows) or uid["canonical_component_count"] != len(rows):
        raise ValueError("UID registry drift from canonical catalog")
    return uid2id, id2uid


def resolve(ref: str, uid: dict, cat: dict) -> tuple[dict, str]:
    byuid, bycanonical = index(uid, cat)
    key = ref.upper().strip()
    if re.fullmatch(r"[0-9]{1,4}", key):
        key = "UID-" + key.zfill(4)
    canonical = byuid.get(key)
    if canonical is None:
        canonical = key if key in bycanonical else cat.get("aliases", {}).get(key, {}).get("canonical_id")
    if canonical is None:
        raise LookupError("Unknown UID/canonical/legacy alias: " + ref)
    record = next(x for x in cat["components"] if x["id"] == canonical)
    return record, bycanonical[canonical]


def inspect(ref: str) -> dict:
    uid, cat, previews, origins = read()
    c, stable = resolve(ref, uid, cat)
    image = previews.get(c["id"], {})
    origin = origins.get(c["id"])
    return {
        "uid": stable,
        "canonical_id": c["id"],
        "legacy_aliases": [k for k, v in cat.get("aliases", {}).items() if v["canonical_id"] == c["id"]],
        "name": c["name"],
        "source_provider": c["source_site"],
        "category": c["category"],
        "tags": c.get("tags", []),
        "source_language": c["language"],
        "source_url": c.get("source_url"),
        "source_repo": c.get("source_repo"),
        "source_commit": c.get("source_commit"),
        "source_path": c.get("source_path"),
        "source_blob_sha": c.get("source_blob_sha"),
        "archive_path": c.get("archive_path"),
        "archive_state": c.get("archive_state"),
        "license_status": c.get("license_status"),
        "current_maturity": c.get("maturity", "REFERENCE"),
        "consumer_runtime": c.get("consumer_runtime", "NOT_VERIFIED"),
        "suggested_app_ids": sorted(set(canonical_app(a) for a in c.get("apps", []))),
        "preview_path": image.get("image_path"),
        "preview_state": image.get("status", "NOT_VERIFIED"),
        "preview_origin": origin,
    }


def plan(ref: str, app: str, stack: str, role: str) -> dict:
    info = inspect(ref)
    lang = info["source_language"].lower()
    stack = stack.lower()
    if stack not in {"flutter", "compose", "web-react", "web-html"}:
        raise ValueError("stack must be flutter|compose|web-react|web-html")
    same_stack = ((stack == "flutter" and "dart" in lang) or
                  (stack == "compose" and ("kotlin" in lang or "compose" in lang)) or
                  (stack == "web-react" and ("react" in lang or "tsx" in lang)) or
                  (stack == "web-html" and "html" in lang))
    if info["archive_state"] != "ARCHIVED_SOURCE":
        mode = "SOURCE_UNAVAILABLE"
    elif not same_stack:
        mode = "ADAPTER_REQUIRED"
    else:
        mode = "SOURCE_REVIEW_REQUIRED"
    # This flag can only be true for a consumer-validated native adapter.
    native_drop_in = (mode == "SOURCE_REVIEW_REQUIRED" and
                      info["current_maturity"] in {"COPY_READY", "LIBRARY_VERIFIED"} and
                      info["consumer_runtime"] == "VERIFIED")
    return {
        "command": "Usa " + info["uid"] + " per " + (role or "il componente") + " nell'app " + app,
        "app": canonical_app(app), "stack": stack, "role": role,
        "component": info, "adoption_mode": mode,
        "copy_paste_ready": bool(native_drop_in),
        "required_checks": [
            "Inspect target app's Product Bible, approved design and AGENTS.md",
            "Check actual original source, license/attribution and asset rights",
            "Check target platform API/SDK, dependencies, security and APK footprint",
            "Adapt implementation when source language is different",
            "Implement correct functionality: accessibility, states, feedback and data, not just visual shape",
            "Build and test exact source SHA, visual states/light-dark/large type, then physical QA",
            "Do not claim adopted/verified, or merge, until exact-head evidence is recorded",
        ],
        "status": "PLAN_ONLY_NOT_IMPLEMENTED",
    }


def validate() -> dict:
    uid, cat, previews, origins = read()
    ui, ids = index(uid, cat)
    if set(previews) != set(ids):
        raise ValueError("preview manifest coverage mismatch")
    for cid, origin in origins.items():
        if cid not in ids or not origin.get("preview_sha256"):
            raise ValueError("unrecognized/uncertified image provenance: " + cid)
    return {"uids": len(ui), "catalog": len(cat["components"]), "preview_count": sum(bool(x.get("image_path")) for x in previews.values()),
            "source_archived": sum(x.get("archive_state") == "ARCHIVED_SOURCE" for x in cat["components"])}


def main() -> None:
    p = argparse.ArgumentParser(description="Usa UID per componenti Design-App")
    sub = p.add_subparsers(dest="mode", required=True)
    l = sub.add_parser("lookup");l.add_argument("id")
    a = sub.add_parser("plan");a.add_argument("id");a.add_argument("--app", required=True)
    a.add_argument("--stack", required=True, choices=["flutter", "compose", "web-react", "web-html"])
    a.add_argument("--role", default="")
    s = sub.add_parser("search");s.add_argument("--text", default="");s.add_argument("--app", default="")
    s.add_argument("--source", default="");s.add_argument("--limit", type=int, default=20)
    sub.add_parser("validate")
    args = p.parse_args()
    try:
        if args.mode == "lookup": output = inspect(args.id)
        elif args.mode == "plan": output = plan(args.id, args.app, args.stack, args.role)
        elif args.mode == "validate": output = validate()
        else:
            uid, cat, previews, origins = read()
            byuid, bycanonical = index(uid, cat)
            matches = []
            for row in cat["components"]:
                haystack = " ".join([row["id"], row["name"], row["category"], " ".join(row.get("tags", []))]).lower()
                if args.text.lower() not in haystack: continue
                if args.source and row["source_site"].lower() != args.source.lower(): continue
                if args.app and canonical_app(args.app) not in {canonical_app(x) for x in row["apps"]}:continue
                matches.append({"uid": bycanonical[row["id"]], "id": row["id"], "name": row["name"],
                                "preview": previews[row["id"]].get("image_path"),
                                "language": row["language"], "archive_state": row["archive_state"]})
            output = {"total": len(matches), "results": matches[:max(args.limit, 0)]}
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (LookupError, ValueError) as exc:
        print("UID ERROR:", exc, file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
