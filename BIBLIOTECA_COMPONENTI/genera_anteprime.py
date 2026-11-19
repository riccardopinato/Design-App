#!/usr/bin/env python3
"""Generate canonical image evidence and GitHub-readable preview tables.

No source component is executed by this script. Images are recorded only when
a PNG actually exists under docs/assets/componenti/. It never invents a
screenshot based on the title, source URL, or programming language.
"""
from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
import html
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "BIBLIOTECA_COMPONENTI"
CATALOG = HERE / "CATALOGO.json"
MANIFEST = HERE / "ANTEPRIME.json"
IMAGE_DIR = ROOT / "docs" / "assets" / "componenti"
APPS_DIR = HERE / "PER_APP"
OVERVIEW = HERE / "TABELLA_478.md"
PNG_SIGNATURE = bytes.fromhex("89504e470d0a1a0a")
ORIGINS = HERE / "ANTEPRIME_ORIGINI.json"
FORUI_PROVENANCE = HERE / "ANTEPRIME_ORIGINI_FORUI.json"
UIDS_FILE = HERE / "UID_REGISTRY.json"
VARIANTS_FILE = HERE / "FLUTTER_VARIANTS.json"
FLUTTER_BY_ID = json.loads(VARIANTS_FILE.read_text(encoding="utf-8"))["components"]
UID_BY_ID = {x["canonical_id"]: x["uid"] for x in json.loads(UIDS_FILE.read_text(encoding="utf-8"))["entries"]}
ALL_SOURCE_TYPES = {"RUIXEN", "UIVERSE", "FLUTTER_FORUI", "DEVLIBRARIES_AMICRO",
                    "DEVLIBRARIES_BOOKMARKS", "DEVLIBRARIES_EASEUI",
                    "DEVLIBRARIES_WATERMELON", "FLUTTER_COMPONENT_LIBRARY",
                    "GENTLEFACE", "USER_IMAGE"}


def load() -> dict:
    obj = json.loads(CATALOG.read_text(encoding="utf-8"))
    ids = [c["id"] for c in obj["components"]]
    if obj["counts"]["unique_components"] != len(ids):
        raise ValueError("canonical component count inconsistent")
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate component ID")
    if set(c["source_site"] for c in obj["components"]) != ALL_SOURCE_TYPES:
        raise ValueError("source categories drift")
    return obj


def is_valid_png(path: Path) -> bool:
    return path.is_file() and path.stat().st_size >= 512 and path.open("rb").read(8) == PNG_SIGNATURE


def build_manifest(rows: list[dict]) -> dict:
    out = {}
    for c in rows:
        cid = c["id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]+", cid):
            raise ValueError("unsafe component ID: " + cid)
        path = IMAGE_DIR / (cid + ".png")
        valid = is_valid_png(path)
        if valid and c["source_site"] == "RUIXEN":
            record = json.loads(ORIGINS.read_text(encoding="utf-8")).get("previews", {}).get(cid) if ORIGINS.exists() else None
            if not record:
                raise ValueError(cid + ": Ruixen image without origin manifest")
            if record.get("preview_path") != "docs/assets/componenti/" + cid + ".png":
                raise ValueError(cid + ": incorrect preview path in provenance")
            if record.get("origin_source_commit") != c.get("source_commit"):
                raise ValueError(cid + ": image/source commit mismatch")
            if record.get("origin_repo") != "ruixenui/ruixen.com":
                raise ValueError(cid + ": incorrect image source repository")
            if record.get("capture_mode") not in {"PINNED_OFFICIAL_PREVIEW_IMAGE", "LIVE_COMPONENT_ONLY_SCREENSHOT", "OFFICIAL_SITE_STATIC_IMAGE", "LIVE_DOCS_COMPONENT_IFRAME"}:
                raise ValueError(cid + ": unsupported acquisition method")
            if hashlib.sha256(path.read_bytes()).hexdigest() != record.get("preview_sha256"):
                raise ValueError(cid + ": screenshot bytes differ from registered SHA256")
        if valid and c["source_site"] == "FLUTTER_FORUI":
            records = json.loads(FORUI_PROVENANCE.read_text(encoding="utf-8")).get("previews", {}) if FORUI_PROVENANCE.exists() else {}
            rec = records.get(cid)
            if (not rec or rec.get("origin_source_commit") != c.get("source_commit")
                    or rec.get("origin_repo") != "duobaseio/forui"
                    or rec.get("preview_path") != "docs/assets/componenti/" + cid + ".png"
                    or rec.get("capture_mode") != "OFFICIAL_FLUTTER_WEB_DEMO_IFRAME"
                    or rec.get("visual_qa") != "UNREVIEWED"
                    or rec.get("preview_sha256") != hashlib.sha256(path.read_bytes()).hexdigest()):
                raise ValueError(cid + ": invalid Forui screenshot provenance")
        if valid and c["source_site"] not in {"RUIXEN", "UIVERSE", "FLUTTER_FORUI"}:
            raise ValueError("unregistered image provider: " + cid)
        if valid:
            out[cid] = {
                "image_path": "docs/assets/componenti/" + cid + ".png",
                "status": ("CAPTURED_UPSTREAM_OR_LIVE_UNREVIEWED" if c["source_site"] == "RUIXEN" else "CAPTURED_ORIGINAL_DEMO_UNREVIEWED" if c["source_site"] == "FLUTTER_FORUI" else "CAPTURED_LOCAL_HTML_UNREVIEWED"),
                "origin_type": ("PINNED_RUIXEN_IMAGE_OR_OFFICIAL_DEMO" if c["source_site"] == "RUIXEN" else "LIVE_ORIGINAL_FLUTTER_DEMO" if c["source_site"] == "FLUTTER_FORUI" else "ARCHIVED_HTML_CSS"),
                "image_evidence": ("Exact origin is recorded in ANTEPRIME_ORIGINI.json; visual QA pending"
                                   if c["source_site"] == "RUIXEN" else
                                   "Authentic Forui demo, provenance in ANTEPRIME_ORIGINI_FORUI.json; QA pending"
                                   if c["source_site"] == "FLUTTER_FORUI" else
                                   "rendered from pinned original Uiverse HTML/CSS; screenshot visual QA pending"),
            }
        else:
            src = c["source_site"] == "UIVERSE"
            out[cid] = {
                "image_path": None,
                "status": "RENDERABLE_HTML_PENDING_CAPTURE" if src else "NO_VERIFIED_IMAGE",
                "origin_type": "ARCHIVED_HTML_CSS" if src else "SOURCE_REFERENCE",
                "image_evidence": None,
            }
    if any(p.stem not in out for p in IMAGE_DIR.glob("*.png")):
        raise ValueError("orphan preview PNG not registered in the canonical catalog")
    return {
        "schema_version": 1,
        "catalog_component_count": len(rows),
        "coverage": "Captures require screenshot generation and visual QA; no source page or source code is itself an image.",
        "created_at": "2026-11-19",
        "previews": out,
    }


def safe(s: object) -> str:
    return html.escape(str(s or ""), quote=True).replace("|", "&#124;").replace("\n", " ")


def href(url: str, label: str) -> str:
    return '<a href="' + html.escape(url, quote=True) + '" target="_blank" rel="noopener noreferrer">' + safe(label) + "</a>"


def row_markdown(c: dict, image: dict, relative: str) -> str:
    cid = c["id"]
    if image.get("image_path"):
        # GitHub renders the small thumbnail and opens the original PNG.
        src = relative + "/docs/assets/componenti/" + cid + ".png"
        cell = '<a href="' + safe(src) + '"><img src="' + safe(src) + '" width="112" alt="Anteprima ' + safe(cid) + '"></a>'
    else:
        source = c.get("source_url") or ""
        if c["source_site"] == "UIVERSE" and c.get("archive_path"):
            cell = '<small>Da acquisire</small> · ' + (href(source, "Demo originale") if source else "—")
        elif source:
            cell = '<small>Non disponibile</small> · ' + href(source, "Fonte")
        else:
            cell = '<small>Non disponibile</small>'
    source_url = c.get("source_url") or (
        "https://github.com/riccardopinato/Design-App/blob/main/" + c["archive_path"]
        if c.get("archive_path") else "")
    source_cell = href(source_url, c["source_site"]) if source_url else safe(c["source_site"])
    apps = ", ".join(safe(x) for x in c["apps"]) or "Non assegnato"
    original = (href(relative + "/" + c["archive_path"], "Apri " + c["language"])
                if c.get("archive_path") else
                (href(c.get("source_url"), "Solo riferimento") if c.get("source_url") else "Non disponibile"))
    native = FLUTTER_BY_ID[cid]
    dart_path = native.get("flutter_code_path")
    flutter_code = (href(relative + "/" + dart_path, "Dart nativo (gate dipendenze)" if native["flutter_status"] == "NATIVE_DART_DEPENDENCY_GATE" else "Apri codice Flutter (bozza)")
                    if dart_path else
                    ("Sorgente non archiviata" if native["flutter_status"] == "SOURCE_NOT_ARCHIVED" else "Da convertire"))
    return "| " + " | ".join([
        cell,
        "<code>" + safe(UID_BY_ID[cid]) + "</code>",
        "<code>" + safe(cid) + "</code>",
        safe(c["name"]),
        source_cell,
        safe(c["category"]),
        apps,
        original,
        flutter_code,
    ]) + " |"


def table_head() -> str:
    return "| Anteprima | UID | ID canonico | Componente | Fonte | Categoria | App associate | Codice originale | Codice Flutter |\n" + \
           "|---|---|---|---|---|---|---|---|---|\n"


def outputs(catalog: dict, manifest: dict) -> dict[Path, str]:
    rows = catalog["components"]
    images = manifest["previews"]
    if set(FLUTTER_BY_ID) != {c["id"] for c in rows}:
        raise ValueError("Flutter dual-source registry does not cover every component")
    assigned = defaultdict(list)
    for row in rows:
        for app in row["apps"]:
            # The catalog contains two historical IDs for the same Anna's
            # Diary product. Keep the source IDs untouched but present one
            # unified app view with both sets of component relations.
            public_app = "annas-diary" if app == "anna-s-diary" else app
            assigned[public_app].append(row)
    result = {}
    count_images = sum(bool(x["image_path"]) for x in images.values())
    common = ("Le immagini qui mostrate sono catture documentali, **non** una verifica "
              "di riuso Flutter, compatibilità nativa o licenze degli asset di terzi. "
              "In assenza di una PNG realmente acquisita la cella dichiara "
              "«Non disponibile» e punta alla fonte originale. " 
              "Le colonne Codice originale e Codice Flutter sono INDIPENDENTI; " 
              "una variante Dart non implica test su app consumer.\n\n")
    summary = [
        f"# Componenti Design-App — tutte le {len(rows)} anteprime\n\n",
        f"**{len(rows)} componenti canonici · {len(catalog['aliases'])} alias · {count_images} immagini archiviate.**\n\n",
        "[Tabelle filtrate per app](./PER_APP/README.md) · "
        "[Visualizzatore con lightbox](../docs/componenti.html) "
        "(richiede GitHub Pages o un server locale).\n\n",
        common, table_head(),
    ]
    summary.extend(row_markdown(c, images[c["id"]], "..") + "\n" for c in rows)
    result[OVERVIEW] = "".join(summary)
    index = [
        "# Anteprime componenti per app\n\n",
        "Tabelle **generate** esclusivamente dalle associazioni nel catalogo "
        "canonico. Ogni riga ha una colonna Anteprima e un collegamento alla fonte.\n\n",
        f"**{len(assigned)} identificativi app · "
        f"{sum(map(len, assigned.values()))} relazioni · "
        f"{len([c for c in rows if not c['apps']])} componenti senza app.**\n\n",
        f"[Tutti i {len(rows)}](../TABELLA_478.md) · "
        "[Vista interattiva](../../docs/componenti.html)\n\n",
        "| App (identificativo del catalogo) | Componenti distinti | Tabella |\n|---|---:|---|\n",
    ]
    for app, subset in sorted(assigned.items()):
        if not re.fullmatch(r"[a-z0-9-]+", app):
            raise ValueError("unsafe app slug: " + app)
        index.append("| " + safe(app) + " | " + str(len(subset)) + " | "
                     + "[Apri anteprime](" + app + ".md) |\n")
        page = [
            "# Anteprime dei componenti — " + safe(app) + "\n\n",
            f"**{len(subset)} componenti associati**, dal solo catalogo Design-App; "
            "l'associazione non prova che il componente sia integrato nell'app.\n\n",
            "[Tutte le app](./README.md) · [Catalogo completo](../TABELLA_478.md) · "
            "[Vista con filtro app](../../docs/componenti.html?app=" + app + ")\n\n",
            common, table_head(),
        ]
        page.extend(row_markdown(c, images[c["id"]], "../..") + "\n" for c in subset)
        result[APPS_DIR / (app + ".md")] = "".join(page)
    result[APPS_DIR / "README.md"] = "".join(index)
    # Preserve old deep links for the historical alias.
    result[APPS_DIR / "anna-s-diary.md"] = (
        "# Anna's Diary — alias storico\n\n"
        "Le associazioni \`anna-s-diary\` e \`annas-diary\` sono "
        "riunite nella [tabella unica di Anna's Diary](./annas-diary.md).\n"
    )
    return result


def run(write: bool) -> int:
    catalog = load()
    manifest = build_manifest(catalog["components"])
    result = {MANIFEST: json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"}
    result.update(outputs(catalog, manifest))
    changed = []
    for path, content in result.items():
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        changed.append(path.relative_to(ROOT).as_posix())
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    count = sum(bool(v["image_path"]) for v in manifest["previews"].values())
    print(f"Catalog: {len(catalog['components'])} canonical, {count} original preview PNG, "
          f"{len(result)-2} app tables; changed={len(changed)}")
    if changed:
        print("\n".join(changed[:35]))
    return 0 if write or not changed else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="regenerate image manifest and Markdown tables")
    mode.add_argument("--check", action="store_true", help="fail when preview tables drift from source")
    args = parser.parse_args()
    sys.exit(run(write=args.write))
