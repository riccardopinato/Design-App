#!/usr/bin/env python3
"""Non-destructive inventory: rank all 480 source-aware Flutter conversion jobs.

Neither a source entry nor a generated plan is a valid Flutter conversion.
All source files remain unchanged and independent of new Dart counterparts.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"BIBLIOTECA_COMPONENTI"
catalog=json.loads((HERE/"CATALOGO.json").read_text(encoding="utf-8"))
uid_map={x["canonical_id"]:x["uid"] for x in json.loads((HERE/"UID_REGISTRY.json").read_text(encoding="utf-8"))["entries"]}
variants=json.loads((HERE/"FLUTTER_VARIANTS.json").read_text(encoding="utf-8"))["components"]
previews=json.loads((HERE/"ANTEPRIME.json").read_text(encoding="utf-8"))["previews"]
assert len(catalog["components"])==len(uid_map)==len(variants)==len(previews)==480
def classify(item):
    cid=item["id"]
    ref=variants[cid]
    path=item.get("archive_path")
    src=""
    if path and (ROOT/path).is_file():
        src=(ROOT/path).read_text(encoding="utf-8",errors="replace")
    imports=re.findall(r'(?:from\s+|import\s*\()["\x27]([^"\x27]+)["\x27]',src)
    hooks=len(re.findall(r'\b(?:useState|useEffect|useRef|useMemo|useReducer|useCallback)\b',src))
    material=set()
    if any("motion" in s or "framer-motion" in s for s in imports): material.add("ANIMATION_LIBRARY")
    if "three" in src.lower() or "webgl" in src.lower(): material.add("WEBGL_OR_3D")
    if any(s.startswith("@/components/ui") or s.startswith("@radix-ui") for s in imports): material.add("SHADCN_OR_RADIX")
    if any(s.startswith("next/") for s in imports): material.add("NEXTJS_RUNTIME")
    if any("@" in s and not s.startswith("@/lib/utils") for s in imports): material.add("SHARED_PROJECT_IMPORT")
    if any("../../../" in s or s.startswith("../") for s in imports): material.add("RELATIVE_DEPENDENCY")
    if any(a in src for a in ("canvas","ResizeObserver","IntersectionObserver")): material.add("DOM_API")
    if any(a in src for a in ("animation:","@keyframes","animate-")): material.add("CSS_MOTION")
    if any(a in src for a in ("perspective","rotateY","rotatey","transform-style")): material.add("3D_TRANSFORM")
    if "src=" in src or "Image" in src: material.add("ASSET_REVIEW")
    size=len(src.encode("utf-8"))
    status=ref["flutter_status"]
    if status=="PENDING_FLUTTER_REWRITE":
        if not src.strip() or "REFERENCE_ONLY"==item["archive_state"]: priority_group="SOURCE_VERIFICATION"
        elif item["source_site"]=="UIVERSE": priority_group="HTML_CSS_NATIVE_PORT"
        elif len(material)<=1 and hooks==0 and size<7500:priority_group="REACT_LOW_DEPENDENCY"
        elif any("WEBGL" in m for m in material):priority_group="ADVANCED_VISUAL"
        else:priority_group="REACT_INTEGRATION_NEEDED"
    else:priority_group="ALREADY_HAS_DART" if ref.get("flutter_code_path") else "SOURCE_VERIFICATION"
    consumers=len(set(item.get("apps",[])))
    difficulty=min(5,1+len(material)+(1 if hooks>=3 or size>15000 else 0))
    rank=consumers*20 + (15 if item["source_site"]=="UIVERSE" else 0) + (10 if priority_group=="REACT_LOW_DEPENDENCY" else 0) - difficulty*5
    return {
        "uid":uid_map[cid],"canonical_id":cid,"name":item["name"],"source":item["source_site"],
        "source_path":path,"original_archive_state":item["archive_state"],
        "flutter_code_path":ref.get("flutter_code_path"),"flutter_status":status,
        "apps":sorted(set(item.get("apps",[]))),
        "preview_verified_file":bool(previews[cid].get("image_path")),
        "source_length_bytes":size if path else None,
        "native_port_group":priority_group,
        "dependency_markers":sorted(material),
        "import_paths":imports[:30],"react_hook_count":hooks,
        "estimated_difficulty":difficulty,"priority_score":rank,
        "note":"Source-only triage. No consumer compatibility, screenshot fidelity or runtime test asserted."
    }
with ThreadPoolExecutor(max_workers=12) as pool:
    rows=list(pool.map(classify,catalog["components"]))
assert len(rows)==480 and {r["canonical_id"] for r in rows}==set(variants)
rows.sort(key=lambda r:(-r["priority_score"],r["uid"]))
info={"schema_version":1,"as_of":"2026-11-19","canonical_count":480,"status_counts":dict(Counter(r["flutter_status"] for r in rows)),"group_counts":dict(Counter(r["native_port_group"] for r in rows)),"entries":rows}
(HERE/"PORTING_BACKLOG.json").write_text(json.dumps(info,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ru=[r for r in rows if r["source"]=="RUIXEN" and not r["preview_verified_file"]]
assert len(ru)==66, f"unexpected Ruixen missing count {len(ru)}"
(HERE/"RU_SOURCE_RENDER_QUEUE.json").write_text(json.dumps({
    "schema_version":1,
    "missing_ruixen_previews":66,
    "source_commit":"f6b20860623fa39122ac2b5f0e5bd29a9eb10941",
    "image_source":"ORIGINAL_ARCHIVED_REACT_TSX",
    "entries":ru,
    "status":"TRIAGE_ONLY_NOT_CAPTURED",
    "policy":"No fake screenshot or implicit asset permission; source-faithful isolated React rendering, component-specific visual QA required."
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
summary=(
    "# Conversione Flutter e preview — backlog esatto dei 480 UID\n\n"
    "Le conversioni e le anteprime sono due pipeline separate. "
    "Questa classificazione non produce file Dart né immagini, non verifica l'aspetto e non sostituisce gli originali.\n\n"
    f"**Flutter:** {info['status_counts']}.\n\n"
    f"**Gruppi di lavoro:** {info['group_counts']}.\n\n"
    "**Ruixen senza PNG:** 66 (TSX MIT conservati, riproduzione locale richiede runtime React + dipendenze verificate).\n\n"
    "## Prime 50 conversioni da sviluppare\n\n"
    "| UID | Componente | Fonte | Gruppo | Impedimenti | App | Priorità |\n"
    "|---|---|---|---|---|---:|---:|\n"
)
queue=[r for r in rows if r["flutter_status"]=="PENDING_FLUTTER_REWRITE"]
for r in queue[:50]:
    summary+=f"| {r['uid']} | {r['canonical_id']} | {r['source']} | {r['native_port_group']} | {', '.join(r['dependency_markers']) or '—'} | {len(r['apps'])} | {r['priority_score']} |\n"
summary+="\nDettaglio completo, sorgenti originali e stato Flutter: [PORTING_BACKLOG.json](./PORTING_BACKLOG.json). Per il recupero delle immagini Ruixen: [RU_SOURCE_RENDER_QUEUE.json](./RU_SOURCE_RENDER_QUEUE.json).\n"
(HERE/"PORTING_BACKLOG.md").write_text(summary,encoding="utf-8")
print("AUDIT_480",info["status_counts"],info["group_counts"],"RU_66",len(ru))
