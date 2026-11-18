#!/usr/bin/env python3
"""Apply PUBLIC Uiverse HTML/CSS to the Design-App catalog; never alter consumer apps."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "UI-UX/UIVERSE"
SOURCES = UI / "CODICE_SORGENTE"
REGISTER = UI / "REGISTRO_COMPONENTI.json"
FAVORITES = UI / "FAVORITES/REGISTRO_PREFERITI_2026-11-18.json"
APP_REG = ROOT / "PER_APP/REGISTRO_APP_DESIGN.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def sha1_blob(s):
    b = s.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\x00" + b).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="out/uiverse")
    args = p.parse_args()
    input_files = sorted(Path(args.source).glob("UIV-*.json"))
    if not input_files:
        print("UIVERSE_APPLY_SUMMARY|new=0|no-op")
        return
    reg, fav, apps = load(REGISTER), load(FAVORITES), load(APP_REG)
    by_id = {c["id"]: c for c in reg["components"]}
    fav_by_id = {f["id"]: f for f in fav["items"]}
    evidence, date = [], datetime.now(timezone.utc).isoformat()
    for path in input_files:
        c = load(path)
        cid = c.get("id")
        if not isinstance(cid, str) or not re.fullmatch(r"UIV-\d{3}", cid):
            raise RuntimeError("Invalid identifier")
        if cid != path.stem or cid not in by_id or cid not in fav_by_id:
            raise RuntimeError("Source ID mismatch")
        item, favorite = by_id[cid], fav_by_id[cid]
        if item.get("source_snapshot") or c.get("url") != item.get("uiverse_url") or c.get("url") != favorite.get("url"):
            raise RuntimeError("Duplicate or wrong source: " + cid)
        if not re.fullmatch(r"https://uiverse\.io/[A-Za-z0-9_.-]+/[A-Za-z0-9_-]+-\d+", c["url"]):
            raise RuntimeError("Unsafe URL")
        if not re.fullmatch(r"[a-fA-F0-9-]{30,40}", str(c.get("post_id", ""))) or c.get("status") != "ORIGINAL_WEB_CODE_READ":
            raise RuntimeError("Unsupported provenance")
        html, css = c.get("html"), c.get("css")
        if not isinstance(html, str) or not isinstance(css, str) or not (html or css):
            raise RuntimeError("Missing raw code")
        if hashlib.sha256(html.encode()).hexdigest() != c.get("html_sha256") or hashlib.sha256(css.encode()).hexdigest() != c.get("css_sha256"):
            raise RuntimeError("Original SHA-256 mismatch")
        if len(html.encode()) + len(css.encode()) > 750000:
            raise RuntimeError("Source too large")
        html_name, css_name = cid + "_original.html", cid + "_original.css"
        if (SOURCES / html_name).exists() or (SOURCES / css_name).exists():
            raise RuntimeError("Existing source must remain immutable")
        (SOURCES / html_name).write_text(html, encoding="utf-8")
        (SOURCES / css_name).write_text(css, encoding="utf-8")
        item.update({
            "source_snapshot": "UI-UX/UIVERSE/CODICE_SORGENTE/" + html_name,
            "source_css_snapshot": "UI-UX/UIVERSE/CODICE_SORGENTE/" + css_name,
            "source_blob_sha": sha1_blob(html), "source_css_blob_sha": sha1_blob(css),
            "source_html_sha256": c["html_sha256"], "source_css_sha256": c["css_sha256"],
            "source_repository": None, "source_commit": None, "source_path": c["url"],
            "source_post_id": c["post_id"], "source_endpoint_type": c["retrieval"],
            "source_captured_at": date, "evidence": "UVERSE_LIVE_PUBLIC_POST_HTML_CSS_CAPTURED",
            "license": "MIT_UIVERSE_POST_WITH_CREATOR_ATTRIBUTION",
            "maturity": "REFERENCE", "consumer_implemented": False, "consumer_tested": False,
            "upstream_category": c.get("type"),
            "upstream_tags": [t for t in c.get("tags", []) if isinstance(t, str)],
            "source_code_analysis": {
                "html_chars": len(html), "css_chars": len(css),
                "css_keyframes": len(re.findall(r"@keyframes", css, re.I)),
                "hover_selectors": css.count(":hover"),
                "contains_svg": "<svg" in html.lower(),
                "gradient": "gradient(" in css,
                "static_review_flags": (["INFINITE_ANIMATION_WITHOUT_REDUCED_MOTION"] if "infinite" in css and "prefers-reduced-motion" not in css else []),
                "source_status": "ORIGINAL_PUBLIC_HTTP_NOT_RUNTIME_TESTED",
            },
        })
        favorite.update({
            "code_availability": "PUBLIC_ENDPOINT_ORIGINAL_HTML_CSS_CAPTURED",
            "code_snapshot": item["source_snapshot"], "css_snapshot": item["source_css_snapshot"],
            "source_post_id": c["post_id"],
            "source_html_sha256": c["html_sha256"], "source_css_sha256": c["css_sha256"],
        })
        evidence.append({
            "id": cid, "url": c["url"], "post_id": c["post_id"],
            "html_path": item["source_snapshot"], "css_path": item["source_css_snapshot"],
            "html_sha256": c["html_sha256"], "css_sha256": c["css_sha256"],
            "html_git_blob": item["source_blob_sha"], "css_git_blob": item["source_css_blob_sha"],
            "type": c.get("type"), "tags": c.get("tags", []),
            "retrieval": c["retrieval"], "captured_at": date,
            "runtime_tested": False,
        })

    recovered_ids = {x["id"] for x in evidence}
    for profile in apps["profiles"]:
        relevant = [e for e in evidence if any(r["component_id"] == e["id"] and r["app_id"] == profile["id"] for r in reg["relations"])]
        if not relevant:
            continue
        for c in profile.get("uiverse_candidates", []):
            if c["component_id"] in recovered_ids:
                c["code_original_available"] = True
        profile["changelog"].append({
            "date": date[:10], "type": "UIVERSE_PUBLIC_SOURCE_RECOVERY",
            "status": "PROPOSED_ONLY", "origin": "https://uiverse.io/",
            "source": "UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json",
            "component_ids": [x["id"] for x in relevant],
            "note": "Original HTML/CSS captured; no consumer implementation or runtime test."
        })
        dossier = ROOT / "PER_APP" / (profile["id"] + ".md")
        lines = dossier.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            for ent in relevant:
                cid = ent["id"]
                if line.startswith("| [" + cid + "](") and "Codice non recuperato" in line:
                    lines[i] = line.replace("Codice non recuperato",
                        f"[HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/{cid}_original.html) · "
                        f"[CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/{cid}_original.css)")
        dossier.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    catalog_count = sum(bool(x.get("source_snapshot")) for x in reg["components"])
    favorites_count = sum(bool(by_id[x["id"]].get("source_snapshot")) for x in fav["items"])
    remaining = len(fav["items"]) - favorites_count
    reg["counts"].update({
        "original_source_files": catalog_count, "code_unavailable": 100-catalog_count,
        "favorite_source_available": favorites_count, "favorite_source_unlocated": remaining
    })
    apps["counts"]["uiverse_original_sources"] = catalog_count
    apps["counts"]["uiverse_pending_sources"] = remaining
    fav["code_available"] = favorites_count
    fav["source_missing"] = remaining
    fav["last_code_recovery_at"] = date
    save(REGISTER, reg)
    save(FAVORITES, fav)
    save(APP_REG, apps)
    save(UI / "FAVORITES/RECUPERO_API_2026_11_18.json", {
        "schema_version": 1, "retrieval_method": "Uiverse public Remix loader",
        "captured_at": date, "newly_recovered": len(evidence),
        "recovered": evidence, "catalog_originals": catalog_count,
        "favorite_originals": favorites_count, "remaining": remaining,
        "license": "MIT declared by Uiverse on post pages",
        "consumer_implemented": False, "runtime_tested": False,
    })
    # Refresh links for retrieval while preserving older source inventory.
    intro = UI / "README.md"
    lines = intro.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        for entry in evidence:
            cid = entry["id"]
            if line.startswith("| " + cid + " |") and "**Da recuperare**" in line:
                lines[i] = line.replace("**Da recuperare**",
                  f"[HTML](./CODICE_SORGENTE/{cid}_original.html) · [CSS](./CODICE_SORGENTE/{cid}_original.css)")
    lines.extend(["", "## Recupero pubblico del " + date[:10], "",
        f"Nuovi originali HTML/CSS: **{len(evidence)}**. Totale catalogo: **{catalog_count}/100**;",
        f"Favorites: **{favorites_count}/97** con codice, **{remaining}** ancora mancanti.",
        "[Evidenze API](./FAVORITES/RECUPERO_API_2026_11_18.json) · [codice](./CODICE_SORGENTE/README.md). "
        "Codice Web non ancora portato/testato nei consumer.", ""])
    intro.write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
    missing = sorted((x for x in reg["components"] if x.get("user_favorite") and not x.get("source_snapshot")),
                     key=lambda x: x.get("favorite_export_position", 999))
    miss = ["# Uiverse Favorites — sorgenti ancora da recuperare", "",
            f"**{len(missing)} mancanti** al {date[:10]}.",
            "", "| ID | Uiverse | Categoria |", "|---|---|---|"]
    miss += [f"| {x['id']} | [{x['author']}/{x['slug']}]({x['uiverse_url']}) | {x['category']} |" for x in missing]
    (UI / "FAVORITES/CODICE_NON_REPERITO.md").write_text("\n".join(miss)+"\n", encoding="utf-8")
    src_readme = SOURCES / "README.md"
    append = "\n\n## Recupero diretto dal sito Uiverse\n\n"
    append += f"**{len(evidence)} originali aggiuntivi** in coppie HTML/CSS, non presenti nel vecchio archivio Galaxy. "
    append += "[SHA/post ID/provenienza](../FAVORITES/RECUPERO_API_2026_11_18.json). MIT per post Uiverse; originale Web non testato.\n\n"
    for x in evidence:
        cid = x["id"]
        append += f"- {cid}: [HTML](./{cid}_original.html), [CSS](./{cid}_original.css), [pagina]({x['url']}).\n"
    src_readme.write_text(src_readme.read_text(encoding="utf-8").rstrip()+append, encoding="utf-8")
    for docpath in [ROOT/"README.md", ROOT/"UI-UX/README.md", ROOT/"PER_APP/README.md",
                    UI/"FAVORITES/README.md",ROOT/"sources/UIVERSE_FAVORITES_97_AUDIT_2026-11-18.md"]:
        text = docpath.read_text(encoding="utf-8").rstrip()
        text += (f"\n\n## Aggiornamento recupero pubblico ({date[:10]})\n\n"
                 f"Originali HTML/CSS aggiunti: **{len(evidence)}**; catalogo **{catalog_count}/100**; "
                 f"Favorites **{favorites_count}/97**; codice non recuperato **{remaining}**. "
                 "Provenienza e checksum in "
                 "[RECUPERO_API](../UI-UX/UIVERSE/FAVORITES/RECUPERO_API_2026_11_18.json). "
                 "Le cifre precedenti documentano lo stato storico prima di questo recupero. "
                 "Nessuna adozione o test su app consumer.\n")
        docpath.write_text(text, encoding="utf-8")
    print(f"UIVERSE_APPLY_SUMMARY|new={len(evidence)}|catalog={catalog_count}"
          f"|favorites={favorites_count}|missing={remaining}", flush=True)

if __name__ == "__main__":
    main()
