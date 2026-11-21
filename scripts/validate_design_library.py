#!/usr/bin/env python3
from pathlib import Path
import json
import re
import hashlib

ROOT = Path(__file__).resolve().parents[1]

def fail(message: str):
    print(f"ERROR: {message}")
    raise SystemExit(1)

registry = (ROOT / "registry" / "DESIGN_REGISTRY.yaml").read_text(encoding="utf-8")
oss = (ROOT / "registry" / "OSS_DESIGN_SOURCES.yaml").read_text(encoding="utf-8")
tested = (ROOT / "tested" / "TESTED_REGISTRY.yaml").read_text(encoding="utf-8")
coverage = (ROOT / "sources" / "COVERAGE.md").read_text(encoding="utf-8")

pattern_ids = re.findall(r"^\s+- id:\s+(DS-\d+)\s*$", registry, re.MULTILINE)
style_ids = re.findall(r"^\s+- id:\s+(STYLE-[A-Z]+)\s*$", registry, re.MULTILINE)
all_ids = pattern_ids + style_ids

if len(all_ids) != len(set(all_ids)):
    fail("duplicate design/style IDs")

expected_patterns = [f"DS-{i:03d}" for i in range(1, 38)]
if pattern_ids != expected_patterns:
    fail(f"pattern IDs are not the canonical DS-001..DS-037 sequence: {pattern_ids}")

expected_styles = [f"STYLE-{chr(ord('A') + i)}" for i in range(16)]
if style_ids != expected_styles:
    fail(f"style IDs are not the canonical STYLE-A..STYLE-P sequence: {style_ids}")

repos = re.findall(r'repo:\s*"([^"]+)"', oss)
# Preserve the 95-source historical baseline, and audit explicit new intake batches.
ruixen_intake = len(re.findall(r"^\s+batch:\s+RUIXEN_UI_2026_11_13\s*$", oss, re.MULTILINE))
if ruixen_intake != 1:
    fail(f"expected exactly one Ruixen external intake, found {ruixen_intake}")
dock_intake = len(re.findall(r"^  - batch_id: DOCK_WIDGET_2026_11_16$", oss, re.MULTILINE))
if dock_intake != 1:
    fail(f"expected one 2026-11-16 dock intake, found {dock_intake}")
visual_intake = len(re.findall(r"^  - batch_id: STAR_VISUAL_2026_11_16$", oss, re.MULTILINE))
if visual_intake != 1:
    fail(f"expected exactly one 2026-11-16 visual stars intake, found {visual_intake}")
skills_intake = len(re.findall(r"^  - batch_id: ANTI_SLOP_DESIGN_SKILLS_2026_11_17$", oss, re.MULTILINE))
if skills_intake != 1:
    fail(f"expected one 2026-11-17 design skill intake, found {skills_intake}")
voice_intake = len(re.findall(r"^  - batch_id: BEUI_VOICE_ORB_2026_11_17$", oss, re.MULTILINE))
if voice_intake != 1:
    fail(f"expected one beUI Voice Orb intake, found {voice_intake}")
motion_intake = len(re.findall(r"^  - batch_id: EASEUI_AMICRO_DESIGN_2026_11_17$", oss, re.MULTILINE))
if motion_intake != 1:
    fail(f"Expected exactly one EaseUI/Amicro intake, got {motion_intake}")
watermelon_intake = len(re.findall(r"^  - batch_id: WATERMELON_NINE_2026_11_17$", oss, re.MULTILINE))
if watermelon_intake != 1:
    fail(f"Watermelon intake must be present exactly once: {watermelon_intake}")
uiverse_intake = len(re.findall(r"^    batch: UIVERSE_9_2026_11_18$", oss, re.MULTILINE))
if uiverse_intake != 1:
    fail(f"Uiverse intake must be present exactly once: {uiverse_intake}")
motion_video_intake = len(re.findall(r"^  - batch_id: MOTION_VIDEO_18_2026_11_20$", oss, re.MULTILINE))
if motion_video_intake != 1:
    fail(f"Expected one 2026-11-20 motion/video 18-source intake, found {motion_video_intake}")
motionary_26_intake = len(re.findall(r"^  - batch_id: MOTIONARY_26_LINKS_2026_11_20$", oss, re.MULTILINE))
if motionary_26_intake != 1:
    fail(f"Expected exactly one Motionary/26-link intake, found {motionary_26_intake}")
appllama_motion_intake = len(re.findall(r"^  - batch_id: APPLLAMA_MOTION_ART_STACK_2026_11_21$", oss, re.MULTILINE))
if appllama_motion_intake != 1:
    fail(f"Expected one Appllama/Motion/Art batch, got {appllama_motion_intake}")
expected_source_count = 95 + ruixen_intake + 2 * dock_intake + 7 * visual_intake + 10 * skills_intake + 2 * voice_intake + 2 * motion_intake + watermelon_intake + uiverse_intake + 18 * motion_video_intake + 15 * motionary_26_intake + 6 * appllama_motion_intake
if len(repos) != expected_source_count or len(set(repos)) != expected_source_count:
    fail(f"expected {expected_source_count} unique OSS design sources, found {len(repos)} / {len(set(repos))} unique")
# New curated Motionary/26-link intake: link registry, canonical dedup, and per-app evidence.
motionary_path = ROOT / "sources" / "MOTIONARY_26_REGISTRY_2026-11-20.json"
motionary_app_path = ROOT / "UI-UX" / "MOTIONARY_26_APP_MAP_2026-11-20.json"
if not all(p.is_file() for p in (
    motionary_path,
    motionary_app_path,
    ROOT / "sources" / "MOTIONARY_26_AUDIT_2026-11-20.md",
    ROOT / "UI-UX" / "MOTIONARY_26_APP_MAP_2026-11-20.md",
)):
    fail("Motionary intake audit/registry/app map absent")
motionary = json.loads(motionary_path.read_text(encoding="utf-8"))
motionary_items = motionary.get("source_items", [])
motionary_new = [x for x in motionary_items if str(x.get("state", "")).startswith("NEW")]
motionary_old = [x for x in motionary_items if str(x.get("state", "")).startswith("EXISTING")]
if (len(motionary_items) != 26
        or len(motionary_new) != 15
        or len(motionary_old) != 11
        or motionary.get("links_submitted") != 26
        or motionary.get("unique_new_sources") != 15
        or motionary.get("existing_links_deduplicated") != 11
        or len({x.get("id") for x in motionary_items}) != 26
        or any(x.get("code_archived") is not False or x.get("consumer_implemented") is not False for x in motionary_items)):
    fail("Motionary 26-source intake count, identity or no-code boundary drift")
for item in motionary_new:
    ref = item.get("source_ref")
    if (repos.count(item.get("repository")) != 1
            or (ref is not None and not re.fullmatch(r"[a-f0-9]{40}", str(ref)))):
        fail(f"Motionary new OSS source missing, duplicated or malformed: {item.get('id')}")
motionary_map = json.loads(motionary_app_path.read_text(encoding="utf-8"))
motionary_edges = motionary_map.get("proposals", [])
motionary_apps = {x.get("app") for x in motionary_edges}
if (len(motionary_edges) != 20 or len(motionary_apps) != 10
        or len({(x.get("app"), x.get("source_id")) for x in motionary_edges}) != 20
        or any(x.get("status") != "PROPOSED_ONLY"
               or x.get("source_id") not in {y.get("id") for y in motionary_items}
               for x in motionary_edges)):
    fail("Motionary per-app relation count or source identity drift")
motionary_profiles = {
    x.get("id"): x for x in json.loads((ROOT / "PER_APP" / "REGISTRO_APP_DESIGN.json").read_text(encoding="utf-8")).get("profiles", [])
}
for app_id in motionary_apps:
    profile = motionary_profiles.get(app_id, {})
    doc = ROOT / "PER_APP" / (app_id + ".md")
    expected = {x.get("source_id") for x in motionary_edges if x.get("app") == app_id}
    records = [x for x in profile.get("changelog", []) if x.get("type") == "MOTIONARY_26_2026_11_20"]
    if (not profile or len(records) != 1 or set(records[0].get("source_ids", [])) != expected
            or not doc.is_file() or "MOTIONARY_26_APP_MAP_2026-11-20" not in doc.read_text(encoding="utf-8")):
        fail(f"Motionary per-app provenance/dossier drift: {app_id}")

motion_manifest_path = ROOT / "sources" / "MOTION_VIDEO_18_REGISTRY_2026-11-20.json"
motion_app_map_path = ROOT / "UI-UX" / "MOTION_VIDEO_18_APP_MAP_2026-11-20.json"
if not all(p.is_file() for p in (
    motion_manifest_path,
    motion_app_map_path,
    ROOT / "sources" / "MOTION_VIDEO_18_AUDIT_2026-11-20.md",
    ROOT / "sources" / "MOTION_VIDEO_18_PIPELINE_2026-11-20.md",
    ROOT / "UI-UX" / "MOTION_VIDEO_18_APP_MAP_2026-11-20.md",
)):
    fail("Motion 18-source intake audit, manifest, pipeline or mapping files missing")
motion_manifest = json.loads(motion_manifest_path.read_text(encoding="utf-8"))
motion_sources = motion_manifest.get("records", [])
if (len(motion_sources) != 18
        or len({x.get("id") for x in motion_sources}) != 18
        or len({x.get("repository") for x in motion_sources}) != 18
        or sum(bool(x.get("license_blob_sha")) for x in motion_sources) != 17):
    fail("Motion 18-source manifest count, uniqueness or license provenance inconsistent")
for item in motion_sources:
    if (repos.count(item.get("repository")) != 1
            or not re.fullmatch(r"[0-9a-f]{40}", str(item.get("source_commit", "")))
            or not re.fullmatch(r"[0-9a-f]{40}", str(item.get("readme_blob_sha", "")))
            or item.get("maturity") != "REFERENCE"
            or item.get("code_imported") is not False):
        fail(f"Motion source missing OSS ref/provenance or misclassified: {item.get('id')}")
motion_app_map = json.loads(motion_app_map_path.read_text(encoding="utf-8"))
motion_edges = motion_app_map.get("relations", [])
motion_app_ids = {x.get("app_id") for x in motion_edges}
if (len(motion_edges) != 68 or len(motion_app_ids) != 13
        or len({(x.get("app_id"), x.get("source_id")) for x in motion_edges}) != 68
        or any(x.get("source_id") not in {z["id"] for z in motion_sources} or x.get("state") != "PROPOSED_ONLY" for x in motion_edges)):
    fail("Motion 18-source cross-app relation count/provenance inconsistent")
motion_profiles_path = ROOT / "PER_APP" / "REGISTRO_APP_DESIGN.json"
motion_profiles = {
    x["id"]: x
    for x in json.loads(motion_profiles_path.read_text(encoding="utf-8")).get("profiles", [])
}
for app_id in motion_app_ids:
    expected = {x["source_id"] for x in motion_edges if x["app_id"] == app_id}
    profile = motion_profiles.get(app_id, {})
    observed = {x.get("source_id") for x in profile.get("motion_video_18_2026_11_20", [])}
    dossier = ROOT / "PER_APP" / (app_id + ".md")
    if (not profile or observed != expected or not dossier.is_file()
            or "MOTION_VIDEO_18_APP_MAP_2026-11-20" not in dossier.read_text(encoding="utf-8")):
        fail(f"Motion 18-source per-app dossier/relations mismatch: {app_id}")
if repos.count("uiverse-io/galaxy") != 1:
    fail("Uiverse Galaxy source must be present once")
uiverse_dir = ROOT / "UI-UX" / "UIVERSE"
uiverse_reg_path = uiverse_dir / "REGISTRO_COMPONENTI.json"
uiverse_map_path = uiverse_dir / "MATRICE_APP_COMPONENTI.json"
if not all(p.is_file() for p in (uiverse_reg_path, uiverse_map_path, uiverse_dir / "MATRICE_APP_COMPONENTI.md")):
    fail("Uiverse registry and bidirectional matrix files missing")
uiverse_reg = json.loads(uiverse_reg_path.read_text(encoding="utf-8"))
uiverse_map = json.loads(uiverse_map_path.read_text(encoding="utf-8"))
uiverse_items = uiverse_reg.get("components", [])
uiverse_links = uiverse_reg.get("relations", [])
uiverse_app_ids = {e.get("app_id") for e in uiverse_links}
# 2026-11-18 Uiverse Favorites: enforce exact provenance, archive integrity,
# deduplication and synchronized many-to-many views. Accept future growing
# batches without hardcoding the historic 9/64 snapshot as final forever.
uiverse_count = uiverse_reg.get("counts", {})
item_ids = {x.get("id") for x in uiverse_items}
if len(uiverse_items) < 111 or len(item_ids) != len(uiverse_items) or uiverse_count.get("links") != len(uiverse_items):
    fail("Uiverse 100-item catalog regression or duplicate component IDs")
if len(uiverse_links) < 736 or len({(e.get("component_id"), e.get("app_id")) for e in uiverse_links}) != len(uiverse_links):
    fail("Uiverse multi-app relations regression/duplication")
if uiverse_count.get("app_component_relations") != len(uiverse_links) or uiverse_count.get("apps") != len(uiverse_app_ids):
    fail("Uiverse counts do not match many-to-many links")
if any(e.get("component_id") not in item_ids or e.get("status") != "PROPOSED_ONLY" for e in uiverse_links):
    fail("Uiverse relation refers to unknown component or is not a proposal")
if {(e["component_id"], e["app_id"]) for e in uiverse_map.get("relations", [])} != {(e["component_id"], e["app_id"]) for e in uiverse_links}:
    fail("Uiverse canonical relations vs matrix disagree")
if set(uiverse_map.get("by_app", {})) != uiverse_app_ids or set(uiverse_map.get("by_component", {})) != item_ids:
    fail("Uiverse reverse-mapping keys missing")
for a in uiverse_app_ids:
    expected = {(e["component_id"], e["app_id"]) for e in uiverse_links if e["app_id"] == a}
    actual = {(e["component_id"], e["app_id"]) for e in uiverse_map["by_app"].get(a, [])}
    if expected != actual:
        fail(f"Uiverse by-app links do not match: {a}")
for component_id in item_ids:
    expected = {(e["component_id"], e["app_id"]) for e in uiverse_links if e["component_id"] == component_id}
    actual = {(e["component_id"], e["app_id"]) for e in uiverse_map["by_component"].get(component_id, [])}
    if expected != actual:
        fail(f"Uiverse by-component links do not match: {component_id}")

code_count = 0
for item in uiverse_items:
    snap = item.get("source_snapshot")
    if snap:
        code_count += 1
        codepath = ROOT / snap
        sha = item.get("source_blob_sha")
        if not codepath.is_file() or not re.fullmatch(r"[0-9a-f]{40}", str(sha)):
            fail(f"Uiverse source missing or unpinned: {item.get('id')}")
        data = codepath.read_bytes()
        actual_sha = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        if sha != actual_sha:
            fail(f"Uiverse source blob mismatch: {item.get('id')}")
        # Newer Uiverse items are captured as exact HTML + CSS pairs, not
        # repackaged Galaxy HTML. Both files, blob SHAs and source SHA-256
        # must match the archived original HTTP response.
        css_rel = item.get("source_css_snapshot")
        if css_rel:
            css_file = (ROOT / css_rel).resolve()
            allowed_dir = (uiverse_dir / "CODICE_SORGENTE").resolve()
            if not css_file.is_relative_to(allowed_dir) or not css_file.is_file():
                fail(f"Uiverse CSS source missing or unsafe: {item.get('id')}")
            css_bytes = css_file.read_bytes()
            css_sha = hashlib.sha1(b"blob " + str(len(css_bytes)).encode("ascii") + b"\0" + css_bytes).hexdigest()
            if item.get("source_css_blob_sha") != css_sha:
                fail(f"Uiverse CSS blob mismatch: {item.get('id')}")
            if item.get("source_html_sha256") != hashlib.sha256(data).hexdigest():
                fail(f"Uiverse original HTML SHA-256 mismatch: {item.get('id')}")
            if item.get("source_css_sha256") != hashlib.sha256(css_bytes).hexdigest():
                fail(f"Uiverse original CSS SHA-256 mismatch: {item.get('id')}")
            if not re.fullmatch(r"[a-f0-9-]{30,40}", str(item.get("source_post_id", "")), re.I):
                fail(f"Uiverse public post provenance missing: {item.get('id')}")

    elif item.get("source_blob_sha") or not str(item.get("evidence", "")).endswith(
        ("SOURCE_CODE_NOT_LOCATED", "SOURCE_CODE_MISSING", "CATEGORY_NOT_VERIFIED")
    ):
        fail(f"Uiverse unavailable source misreported: {item.get('id')}")
    if item.get("consumer_implemented") is not False:
        fail(f"Uiverse reference incorrectly claims consumer implementation: {item.get('id')}")
if code_count < 111 or uiverse_count.get("original_source_files") != code_count:
    fail("Uiverse original-code source inventory inconsistent")
if not (uiverse_dir / "CODICE_SORGENTE" / "LICENSE-Uiverse-Galaxy-MIT.txt").is_file():
    fail("Uiverse MIT notice missing")

favorites_path = uiverse_dir / "FAVORITES" / "REGISTRO_PREFERITI_2026-11-18.json"
if not favorites_path.is_file():
    fail("Uiverse Favorites export register missing")
favorites = json.loads(favorites_path.read_text(encoding="utf-8"))
favorited = favorites.get("items", [])
fav_urls = {x.get("url") for x in favorited}
if len(favorited) < 97 or len(fav_urls) != len(favorited) or favorites.get("unique_count") != len(favorited):
    fail("Uiverse Favorites declared/unique count mismatch")
if favorites.get("completeness") != "REQUIRES_USER_COUNT_VERIFICATION":
    fail("Uiverse Favorites incorrectly claim independent account completeness")
by_id = {c["id"]: c for c in uiverse_items}
for fav in favorited:
    item = by_id.get(fav.get("id"))
    if not item or item.get("uiverse_url") != fav.get("url") or item.get("user_favorite") is not True:
        fail(f"Uiverse favorite lost from master registry: {fav.get('id')}")
    if bool(item.get("source_snapshot")) != bool(fav.get("code_snapshot")):
        fail(f"Uiverse favorite original-code evidence mismatch: {fav.get('id')}")
if uiverse_count.get("favorite_links") != len(favorited):
    fail("Uiverse favorite count not reflected in master registry")
favorite_originals = sum(bool(by_id.get(f["id"], {}).get("source_snapshot")) for f in favorited)
if (uiverse_count.get("favorite_source_available") != favorite_originals
    or uiverse_count.get("favorite_source_unlocated") != len(favorited) - favorite_originals):
    fail("Uiverse favorite original-code counts inconsistent")
if favorite_originals < 108:
    fail("Uiverse original source inventory regressed below 97 verified Favorites")
per_app_uiverse = json.loads((ROOT / "PER_APP" / "REGISTRO_APP_DESIGN.json").read_text(encoding="utf-8"))
for app_id in uiverse_app_ids:
    profile = next((p for p in per_app_uiverse.get("profiles", []) if p.get("id") == app_id), None)
    if profile is None:
        fail(f"Uiverse app profile missing: {app_id}")
    actual = {(e.get("component_id"), e.get("surface")) for e in profile.get("uiverse_candidates", [])}
    expected = {(e["component_id"], e["surface"]) for e in uiverse_links if e["app_id"] == app_id}
    dossier = ROOT / "PER_APP" / f"{app_id}.md"
    if actual != expected or not dossier.is_file() or "## Uiverse Favorites — archivio incrociato 18/11/2026" not in dossier.read_text(encoding="utf-8"):
        fail(f"Uiverse per-app dossier/relations inconsistent: {app_id}")
if per_app_uiverse.get("counts", {}).get("uiverse_app_links") != len(uiverse_links):
    fail("Uiverse per-app counts mismatch")
# Refresh 108 Favorites: compare source export, delta, original-code coverage,
# and cumulative public endpoint provenance. The older 97 export is preserved.
refresh_diff_path = uiverse_dir / "FAVORITES" / "CONFRONTO_108_VS_97_2026-11-18.json"
refresh_export_path = uiverse_dir / "FAVORITES" / "EXPORT_2026-11-18T16-40-39Z.json"
public_recovery_path = uiverse_dir / "FAVORITES" / "RECUPERO_API_2026_11_18.json"
for required in (refresh_diff_path, refresh_export_path, public_recovery_path):
    if not required.is_file():
        fail("Uiverse latest export/recovery evidence missing")
refresh_diff = json.loads(refresh_diff_path.read_text(encoding="utf-8"))
refresh_export = json.loads(refresh_export_path.read_text(encoding="utf-8"))
public_recovery = json.loads(public_recovery_path.read_text(encoding="utf-8"))
new_urls = refresh_export.get("favorites", [])
if (len(new_urls) < 108 or len(set(new_urls)) != len(new_urls)
    or set(new_urls) != fav_urls
    or refresh_export.get("count") != len(new_urls)):
    fail("Uiverse refreshed source export and favorites registry do not match")
if (refresh_diff.get("added_count") != 11 or refresh_diff.get("removed_count") != 0
    or refresh_diff.get("unchanged_count") != 97
    or len(refresh_diff.get("added", [])) != 11):
    fail("Uiverse 97 to 108 favorite diff evidence inconsistent")
recovered_records = public_recovery.get("recovered", [])
recovered_ids = {x.get("id") for x in recovered_records}
if (len(recovered_records) != 54 or len(recovered_ids) != 54
    or public_recovery.get("total_public_recovered") != 54):
    fail("Uiverse cumulative 43+11 public retrieval ledger regressed")
if len([x for x in uiverse_items if x.get("source_css_snapshot")]) < 54:
    fail("Uiverse original HTML/CSS pairs lost")
if any(c.get("category") == "UNKNOWN" for c in uiverse_items):
    fail("Uiverse newly captured public source category not normalized")
new_ids = {"UIV-" + str(i) for i in range(101, 112)}
if {x.get("id") for x in refresh_diff.get("added", [])} != new_ids:
    fail("Uiverse new 11 IDs changed or missing from export diff")
if any(not by_id.get(i, {}).get("source_css_snapshot") for i in new_ids):
    fail("Uiverse new Favorites not archived with independent original CSS")
if uiverse_count.get("favorite_source_unlocated") != 0 or uiverse_count.get("code_unavailable") != 0:
    fail("Uiverse 108 Favorite code inventory not complete")

for required in ("ruixenui/ruixen.com", "alztrk/opentaskbar", "Acadbek/lumabar"):
    if repos.count(required) != 1:
        fail(f"external source missing or duplicated: {required}")
if not (ROOT / "sources" / "GITHUB_DOCK_WIDGET_REFERENCE_2026-11-16.md").is_file():
    fail("dock reference audit document is missing")
for required in ("tldraw/tldraw", "excalidraw/excalidraw", "xyflow/xyflow", "markmap/markmap",
                 "alztrk/OpenWidget", "AppFlowy-IO/appflowy-editor", "sorenwacker/nodus"):
    if repos.count(required) != 1:
        fail(f"new visual source missing or duplicated: {required}")
if not (ROOT / "sources" / "STARS_750_VISUAL_INTAKE_2026-11-16.md").is_file():
    fail("2026-11-16 visual stars audit documentation missing")
# 2026-11-17 agent design skills must be registered source-pinned with a bidirectional proposed-only app map.
for required in ("uizze/uizze", "pbakaus/impeccable", "Leonxlnx/taste-skill",
                 "emilkowalski/skills", "vercel-labs/agent-skills", "anthropics/skills",
                 "Nutlope/hallmark", "jakubkrehel/skills",
                 "nextlevelbuilder/ui-ux-pro-max-skill", "benjitaylor/skills"):
    if repos.count(required) != 1:
        fail(f"design skills intake missing or duplicated: {required}")
skills_audit = ROOT / "sources" / "ANTI_SLOP_DESIGN_SKILLS_AUDIT_2026-11-17.md"
skills_map_path = ROOT / "UI-UX" / "MATRICE_REPO_DESIGN_APP_2026-11-17.json"
skills_view = ROOT / "UI-UX" / "MATRICE_REPO_DESIGN_APP_2026-11-17.md"
if not all(p.is_file() for p in (skills_audit, skills_map_path, skills_view)):
    fail("design skill intake audit/map/view missing")
skills_map = json.loads(skills_map_path.read_text(encoding="utf-8"))
skills_sources = skills_map.get("sources", [])
skills_links = skills_map.get("associations", [])
skills_counts = skills_map.get("counts", {})
if skills_map.get("batch_id") != "ANTI_SLOP_DESIGN_SKILLS_2026_11_17":
    fail("design skills map wrong batch id")
if len(skills_sources) != 10 or len({x.get("id") for x in skills_sources}) != 10:
    fail("design skills must have ten unique source IDs")
if {x.get("repo") for x in skills_sources} - set(repos):
    fail("design skill map contains sources absent in OSS registry")
if any(not re.fullmatch(r"[0-9a-f]{40}", str(x.get("ref", ""))) for x in skills_sources):
    fail("design skill source HEAD not pinned to 40-char SHA")
if any(x.get("maturity") != "REFERENCE" for x in skills_sources):
    fail("unverified design skill was prematurely promoted")
if len(skills_links) != skills_counts.get("associations"):
    fail("design skill association count mismatch")
if any(e.get("status") != "PROPOSED_ONLY" or e.get("fit") not in ("HIGH", "MEDIUM")
       for e in skills_links):
    fail("design skill app association promoted without consumer evidence")
if len({(e.get("source_id"), e.get("app")) for e in skills_links}) != len(skills_links):
    fail("duplicate design skill app association")
if {e.get("source_id") for e in skills_links} - {s.get("id") for s in skills_sources}:
    fail("design skill association links to unknown source")
if len(skills_map.get("by_app", {})) != skills_counts.get("apps"):
    fail("design skill by-app view count mismatch")
for app, linked in skills_map.get("by_app", {}).items():
    if {(x.get("source_id"), x.get("fit")) for x in linked} != {
         (e.get("source_id"), e.get("fit")) for e in skills_links if e.get("app") == app}:
        fail(f"design skill by-app links out of sync: {app}")
for source_id, linked in skills_map.get("by_source", {}).items():
    if {(x.get("app"), x.get("fit")) for x in linked} != {
         (e.get("app"), e.get("fit")) for e in skills_links if e.get("source_id") == source_id}:
        fail(f"design skill by-source links out of sync: {source_id}")

# The November 17 skills matrix is an immutable ten-source snapshot.
# A dated, separately validated delta supplies new DSK-011 links without
# silently rewriting its original 96 historical proposals.
unslop_path = ROOT / "UI-UX" / "UNSLOP_UI_APP_MAP_2026-11-19.json"
unslop_map = json.loads(unslop_path.read_text(encoding="utf-8"))
unslop_entries = unslop_map.get("apps", [])
if unslop_map.get("source", {}).get("id") != "DSK-011" or unslop_map.get("status") != "PROPOSED_ONLY":
    fail("Unslop mapping must retain DSK-011 proposed-only status")
if unslop_map.get("source", {}).get("sha") != "cd891160453f26aaacc569bad96a8d10d595076d":
    fail("Unslop upstream source pin mismatch")
if len(unslop_entries) != 5 or len({row.get("app_id") for row in unslop_entries}) != 5:
    fail("Unslop must declare exactly five distinct proposed app relations")
if unslop_map.get("counts", {}).get("relations") != len(unslop_entries):
    fail("Unslop relation count drift")
if any(row.get("source_id") != "DSK-011" or row.get("status") != "PROPOSED_ONLY"
       or row.get("fit") not in ("HIGH", "MEDIUM") or row.get("runtime_state") != "NOT_VERIFIED"
       for row in unslop_entries):
    fail("Unslop association status, identity or maturity drift")
unslop_by_app = {row["app_name"]: (row["source_id"], row["fit"], row["scope"])
                 for row in unslop_entries}

ruixen_index = json.loads((ROOT / "sources" / "RUIXEN_UI_REGISTRY_INVENTORY_2026-11-13.json").read_text(encoding="utf-8"))
ruixen_curated = json.loads((ROOT / "sources" / "RUIXEN_UI_CURATED_APP_MAP_2026-11-13.json").read_text(encoding="utf-8"))
files = ruixen_index.get("files", [])
candidates = ruixen_curated.get("items", [])
if len(files) != 277 or len({f.get("slug") for f in files}) != 277:
    fail("Ruixen inventory must contain exactly 277 distinct TSX references")
if len(candidates) != 41 or len({c.get("id") for c in candidates}) != 41:
    fail("Ruixen curated map must contain exactly 41 distinct references")
if len({app for c in candidates for app in c.get("apps", [])}) != 18:
    fail("Ruixen app crosswalk must cover 18 apps")
file_by_slug = {f["slug"]: f for f in files}
for candidate in candidates:
    source = file_by_slug.get(candidate.get("slug"))
    if not source or source.get("blob_sha") != candidate.get("pinned_code_sha"):
        fail(f"Ruixen source mismatch for {candidate.get('id')}")
    if candidate.get("code_imported") or candidate.get("status") != "REFERENCE_NOT_ADOPTED":
        fail(f"Ruixen {candidate.get('id')} prematurely marked as adopted")
if ruixen_index.get("immutable_commit") != ruixen_curated.get("immutable_commit"):
    fail("Ruixen source commit mismatch across catalogues")
if not (ROOT / "sources" / "RUIXEN_UI_DESIGN_MOTION_AUDIT_2026-11-13.md").is_file():
    fail("Ruixen design motion audit missing")

curated_count = len(re.findall(r"^\s+batch:\s+CURATED_2026_10_27\s*$", oss, re.MULTILINE))
if curated_count != 37:
    fail(f"expected 37 sources in CURATED_2026_10_27, found {curated_count}")

source_ref_count = len(re.findall(r'^\s+source_ref:\s+"[0-9a-f]{40}"\s*$', oss, re.MULTILINE))
if source_ref_count < 59:
    fail(f"expected at least 59 pinned curated source refs, found {source_ref_count}")

sound_count = len(re.findall(r"^\s+domain:\s+sound\s*$", oss, re.MULTILINE))
new_batch_count = len(re.findall(r"^\s+batch:\s+CURATED_2026_10_30\s*$", oss, re.MULTILINE))
if new_batch_count != 22:
    fail(f"expected 22 sources in CURATED_2026_10_30, found {new_batch_count}")

if sound_count != 6:
    fail(f"expected 6 curated sound sources, found {sound_count}")

snapshot_paths = re.findall(r"path:\s*([^,}\n]+)", tested)
snapshot_paths = [p.strip() for p in snapshot_paths if p.strip().startswith("tested/source_snapshots/")]
if len(snapshot_paths) != 18:
    fail(f"expected 18 registered source snapshots, found {len(snapshot_paths)}")

for rel in snapshot_paths:
    if not (ROOT / rel).is_file():
        fail(f"registered snapshot missing: {rel}")

coverage_rows = [
    line for line in coverage.splitlines()
    if line.startswith("| ") and not line.startswith("|---") and "App / product" not in line
]
if len(coverage_rows) < 19:
    fail(f"coverage matrix unexpectedly small: {len(coverage_rows)}")

required = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "sources" / "PROJECT_PATTERN_HARVEST.md",
    ROOT / "sources" / "PROJECT_FILE_FRAMEWORKS.md",
    ROOT / "sources" / "GITHUB_DESIGN_RESEARCH_2026-10-27.md",
    ROOT / "sources" / "SOUND_DESIGN_GUIDE.md",
    ROOT / "sources" / "GITHUB_DESIGN_RESEARCH_2026-10-30.md",
    ROOT / "packs" / "ROADMAP_COPY_READY.md",
    ROOT / "packs" / "PACK_REGISTRY.yaml",
    ROOT / "packs" / "motion" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "factory_motion.dart",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "src" / "motion_policy.dart",
    ROOT / "packs" / "motion" / "flutter" / "lib" / "src" / "motion_widgets.dart",
    ROOT / "packs" / "motion" / "flutter" / "test" / "factory_motion_test.dart",
    ROOT / "packs" / "motion" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "motion" / "flutter" / "PROVENANCE.md",
    ROOT / ".github" / "workflows" / "motion-pack-flutter.yml",
    ROOT / "packs" / "sound" / "semantic" / "manifest.json",
    ROOT / "packs" / "sound" / "semantic" / "LICENSE-CC0.txt",
    ROOT / "packs" / "sound" / "semantic" / "validate_assets.py",
    ROOT / "packs" / "sound" / "semantic" / "README.md",
    ROOT / "packs" / "sound" / "semantic" / "PROVENANCE.md",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "factory_sound_flutter.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "semantic_sound.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "audio_backend.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "lib" / "src" / "sound_controller.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "test" / "semantic_sound_test.dart",
    ROOT / "packs" / "sound" / "adapters" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / ".github" / "workflows" / "semantic-sound-pack.yml",
    ROOT / "packs" / "icons" / "manifest" / "icons.json",
    ROOT / "packs" / "icons" / "manifest" / "generate.py",
    ROOT / "packs" / "icons" / "manifest" / "test_manifest.py",
    ROOT / "packs" / "icons" / "README.md",
    ROOT / "packs" / "icons" / "PROVENANCE.md",
    ROOT / "packs" / "icons" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "factory_icons.dart",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "src" / "factory_icon_widgets.dart",
    ROOT / "packs" / "icons" / "flutter" / "lib" / "src" / "generated_factory_icon_keys.dart",
    ROOT / "packs" / "icons" / "flutter" / "test" / "factory_icons_test.dart",
    ROOT / "packs" / "icons" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "icons" / "compose" / "build.gradle.kts",
    ROOT / "packs" / "icons" / "compose" / "settings.gradle.kts",
    ROOT / "packs" / "icons" / "compose" / "src" / "main" / "kotlin" / "factory" / "icons" / "GeneratedFactoryIconKeys.kt",
    ROOT / "packs" / "icons" / "compose" / "src" / "main" / "kotlin" / "factory" / "icons" / "FactoryIconWidgets.kt",
    ROOT / "packs" / "icons" / "compose" / "src" / "test" / "kotlin" / "factory" / "icons" / "FactoryIconMappingTest.kt",
    ROOT / ".github" / "workflows" / "icon-adapter-pack.yml",
    ROOT / "packs" / "visual-qa" / "manifest" / "visual_matrix.json",
    ROOT / "packs" / "visual-qa" / "manifest" / "validate_matrix.py",
    ROOT / "packs" / "visual-qa" / "PROVENANCE.md",
    ROOT / "packs" / "visual-qa" / "flutter" / "pubspec.yaml",
    ROOT / "packs" / "visual-qa" / "flutter" / "README.md",
    ROOT / "packs" / "visual-qa" / "flutter" / "lib" / "factory_visual_qa.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "lib" / "src" / "qa_fixture.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "support" / "visual_matrix.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "visual_matrix_test.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "test" / "visual_golden_test.dart",
    ROOT / "packs" / "visual-qa" / "flutter" / "example" / "lib" / "main.dart",
    ROOT / "packs" / "visual-qa" / "compose" / "README.md",
    ROOT / "packs" / "visual-qa" / "swiftui" / "README.md",
    ROOT / ".github" / "workflows" / "visual-qa-flutter.yml",
]
for path in required:
    if not path.is_file():
        fail(f"required file missing: {path.relative_to(ROOT)}")


# Audit hardening: fail closed on stale Factory baselines, identity collisions
# and provenance locators that silently lose their source file or blob hash.
if not re.search(r"commit: e9507056601c4a6751510da4c5d1f61601a5dc25", registry):
    fail("design registry Factory baseline does not match pinned v27")
if not re.search(r'master: "27"', registry):
    fail("design registry Master must be v27")

harvest = (ROOT / "sources" / "PROJECT_PATTERN_HARVEST.md").read_text(encoding="utf-8")
for conflicting in ("### DS-009 — Consumer-first", "### DS-010 — Ethical premium"):
    if conflicting in harvest:
        fail(f"harvest stable ID conflicts with canonical registry: {conflicting}")

ledger = json.loads((ROOT / "registry" / "PATTERN_PROVENANCE.json").read_text(encoding="utf-8"))
if ledger.get("schema_version") != 1:
    fail("unsupported pattern provenance schema")
items = ledger.get("patterns", [])
if [x.get("id") for x in items] != pattern_ids:
    fail("pattern provenance IDs/order do not match canonical DS registry")

for item in items:
    pid = item["id"]
    if item["maturity"] == "SOURCE_VERIFIED" and not item["donor_snapshots"]:
        fail(f"{pid} claims SOURCE_VERIFIED without any immutable snapshot lead")
    if not item["donor_snapshots"] and not item["unverified_donors"]:
        fail(f"{pid} lacks all donor information")
    for source in item["donor_snapshots"]:
        path = ROOT / source["snapshot_path"]
        if not path.is_file() or not path.resolve().is_relative_to((ROOT / "tested" / "source_snapshots").resolve()):
            fail(f"{pid} has invalid snapshot path {path}")
        payload = path.read_text(encoding="utf-8")
        expected_fields = {
            "source_path": source["source_path"],
            "source_blob": source["git_blob_sha"],
            "source_repo": source["repo"],
        }
        if len(source["git_blob_sha"]) != 40 or not re.fullmatch(r"[0-9a-f]{40}", source["git_blob_sha"]):
            fail(f"{pid}: invalid immutable source blob")
        for field, value in expected_fields.items():
            if f"{field}: {value}\n" not in payload:
                fail(f"{pid} source provenance not supported by {source['snapshot_path']}")

# Every check intended for branch rulesets must exist on every PR;
# path-filtered pack workflows cannot safely be mandatory branch checks.
workflows = [
    ".github/workflows/validate.yml",
    ".github/workflows/motion-pack-flutter.yml",
    ".github/workflows/semantic-sound-pack.yml",
    ".github/workflows/icon-adapter-pack.yml",
    ".github/workflows/visual-qa-flutter.yml",
]
for rel in workflows:
    body = (ROOT / rel).read_text(encoding="utf-8")
    if "  pull_request:" not in body:
        fail(f"mandatory workflow does not run on every PR: {rel}")
    if re.search(r"  pull_request:\n    paths:", body):
        fail(f"path-filtered required workflow: {rel}")
    for use in re.findall(r"^\s*- uses:\s*([^\s#]+)", body, re.MULTILINE):
        if "@" not in use or not re.fullmatch(r"[0-9a-f]{40}", use.rsplit("@", 1)[-1]):
            fail(f"un-pinned action in {rel}: {use}")

for rel in (
    "docs/GITHUB_BRANCH_PROTECTION.md",
    "docs/LICENSE_POLICY.md",
    "docs/AUDIT_REMEDIATION_v1.md",
    "registry/PATTERN_PROVENANCE.json",
):
    if not (ROOT / rel).is_file():
        fail(f"audit hardening document missing: {rel}")

# Provenance files must not contain contradictory duplicate evidence scalars.
visual_provenance = (ROOT / "packs/visual-qa/PROVENANCE.md").read_text(encoding="utf-8")
if visual_provenance.count("evidence:") != 1:
    fail("visual QA provenance has duplicate or missing evidence metadata")

# External iconography intake remains independent from the tested Icon Adapter Pack.
icons_dir = ROOT / "ICONE"
required_icon_docs = (
    "README.md", "REGISTRO_ICONE.json", "MATRICE_APP_ICONE.md",
    "ANTEPRIME.md", "GENTLEFACE_AUDIT_2026-11-17.md", "GUIDA_INTEGRAZIONE.md",
)
if not all((icons_dir / filename).is_file() for filename in required_icon_docs):
    fail("ICONE required catalog/documentation missing")
icon_data = json.loads((icons_dir / "REGISTRO_ICONE.json").read_text(encoding="utf-8"))
icon_items = icon_data.get("icons", [])
icon_links = icon_data.get("associations", [])
icon_counts = icon_data.get("counts", {})
if icon_data.get("batch") != "GENTLEFACE_2026_11_17" or icon_data.get("maturity") != "REFERENCE":
    fail("ICONE batch/level invalid")
if icon_data.get("runtime_implementation") != "NOT_IMPLEMENTED" or icon_data.get("asset_imports") != 0:
    fail("ICONE claims unsupported implementation or asset import")
if len(icon_items) != 28 or len({i.get("id") for i in icon_items}) != len(icon_items):
    fail("ICONE expected 28 unique candidates")
if len({i.get("slug") for i in icon_items}) != len(icon_items):
    fail("ICONE duplicate icon slug")
if len(icon_items) != icon_counts.get("icon_candidates"):
    fail("ICONE candidate count out of sync")
if any(i.get("maturity") != "REFERENCE" or i.get("adoption") != "PROPOSED_ONLY"
       for i in icon_items):
    fail("ICONE proposed source prematurely promoted")
if any(i.get("asset_bytes_verified") is not False for i in icon_items):
    fail("ICONE claims unverifiable downloaded icon asset")
if any(i.get("animation_evidence") not in
       ("VERIFIED_SITE", "VERIFIED_DETAIL", "ANIMATION_UNVERIFIED") for i in icon_items):
    fail("ICONE unexpected animation evidence state")
if sum(i["animation_evidence"] == "ANIMATION_UNVERIFIED" for i in icon_items) != icon_counts.get("animation_not_verified"):
    fail("ICONE animation status count mismatch")
semantic_manifest = json.loads((ROOT / "packs/icons/manifest/icons.json").read_text(encoding="utf-8"))
semantic_ids = {i["id"] for i in semantic_manifest.get("icons", [])}
if any(i.get("existing_factory_semantic_id") not in semantic_ids | {None} for i in icon_items):
    fail("ICONE references unknown existing semantic key")
icon_ids = {i["id"] for i in icon_items}
icon_pairs = {(e.get("icon_id"), e.get("app")) for e in icon_links}
if len(icon_pairs) != len(icon_links) or len(icon_links) != icon_counts.get("associations"):
    fail("ICONE associations count or unique pair invariant failed")
if any(e.get("icon_id") not in icon_ids or e.get("status") != "PROPOSED_ONLY"
       or e.get("fit") not in ("HIGH", "MEDIUM") for e in icon_links):
    fail("ICONE invalid proposal foreign key/state")
if sum(e["fit"] == "HIGH" for e in icon_links) != icon_counts.get("high"):
    fail("ICONE HIGH count mismatch")
if sum(e["fit"] == "MEDIUM" for e in icon_links) != icon_counts.get("medium"):
    fail("ICONE MEDIUM count mismatch")
apps_in_icons = {e["app"] for e in icon_links}
if len(apps_in_icons) != icon_counts.get("apps"):
    fail("ICONE app coverage count mismatch")
for app, assoc in icon_data.get("by_app", {}).items():
    expected = {(e["icon_id"], e["fit"], e["surface"]) for e in icon_links if e["app"] == app}
    observed = {(e["icon_id"], e["fit"], e["surface"]) for e in assoc}
    if observed != expected:
        fail(f"ICONE by_app mismatch: {app}")
if set(icon_data.get("by_app", {})) != apps_in_icons:
    fail("ICONE by_app key coverage mismatch")
for icon_id, assoc in icon_data.get("by_icon", {}).items():
    expected = {(e["app"], e["fit"], e["surface"]) for e in icon_links if e["icon_id"] == icon_id}
    observed = {(e["app"], e["fit"], e["surface"]) for e in assoc}
    if observed != expected:
        fail(f"ICONE by_icon mismatch: {icon_id}")
if set(icon_data.get("by_icon", {})) != icon_ids:
    fail("ICONE by_icon key coverage mismatch")

# Per-app design dossiers are a persistent read model for icon and skill discovery.
per_app_dir = ROOT / "PER_APP"
profiles_path = per_app_dir / "REGISTRO_APP_DESIGN.json"
profiles_index = per_app_dir / "README.md"
if not profiles_path.is_file() or not profiles_index.is_file():
    fail("PER_APP dossier registry or index missing")
per_app = json.loads(profiles_path.read_text(encoding="utf-8"))
profiles = per_app.get("profiles", [])
profile_counts = per_app.get("counts", {})
if per_app.get("schema_version") != 1 or per_app.get("status") != "CANDIDATE_DESIGN_GUIDANCE_ONLY":
    fail("PER_APP schema/status invalid")
if len(profiles) < 25 or len(profiles) != profile_counts.get("app_profiles"):
    fail("PER_APP profile baseline/count inconsistent")
if len({p.get("name") for p in profiles}) != len(profiles):
    fail("PER_APP duplicate app name")
if len({p.get("id") for p in profiles}) != len(profiles):
    fail("PER_APP duplicate dossier path slug")
if any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(p.get("id", ""))) for p in profiles):
    fail("PER_APP invalid slug")
if per_app.get("source_of_truth") != "PER_APP/REGISTRO_APP_DESIGN.json":
    fail("PER_APP canonical path mismatch")
if any(p.get("decision_state") != "PROPOSAL_ONLY" or p.get("implementation_state") != "NOT_VERIFIED"
       or p.get("product_bible_checked") is not False or p.get("app_code_checked") is not False
       for p in profiles):
    fail("PER_APP falsely asserts approval or consumer evidence")
if any(not p.get("changelog") or not p.get("direction") or not p.get("priority_surfaces")
       or not p.get("avoid") or not p.get("motion_recommendations") for p in profiles):
    fail("PER_APP dossier missing direction, use, anti-patterns, motion or history")
dossier_names = {p["name"] for p in profiles}
if set(icon_data.get("by_app", {})) - dossier_names:
    fail("PER_APP missing app in icon catalog")
if set(skills_map.get("by_app", {})) - dossier_names:
    fail("PER_APP missing app in design skill catalog")
for profile in profiles:
    name = profile["name"]
    actual_icons = {(x["id"], x["fit"], x["surface"]) for x in profile.get("source_icons", [])}
    expected_icons = {(x["icon_id"], x["fit"], x["surface"])
                      for x in icon_data.get("by_app", {}).get(name, [])}
    if actual_icons != expected_icons or len(actual_icons) != len(profile.get("source_icons", [])):
        fail(f"PER_APP icon mapping drift: {name}")
    actual_skills = {(x["id"], x["fit"], x["surface"]) for x in profile.get("source_design_skills", [])}
    expected_skills = {(x["source_id"], x["fit"], x["surface"])
                       for x in skills_map.get("by_app", {}).get(name, [])}
    if name in unslop_by_app:
        expected_skills.add(unslop_by_app[name])
    if actual_skills != expected_skills or len(actual_skills) != len(profile.get("source_design_skills", [])):
        fail(f"PER_APP skill mapping drift: {name}")
    doc_path = per_app_dir / (profile["id"] + ".md")
    if not doc_path.is_file():
        fail(f"PER_APP missing dossier: {name}")
    doc_text = doc_path.read_text(encoding="utf-8")
    if not doc_text.startswith("# " + name + " — Dossier Design-App") or profile["direction"] not in doc_text:
        fail(f"PER_APP dossier title/direction mismatch: {name}")
    if "PROPOSAL_ONLY" not in doc_text:
        fail(f"PER_APP dossier lacks unverified-state disclaimer: {name}")
    for mapping in profile.get("source_icons", []):
        if mapping["id"] not in doc_text or mapping["slug"] not in doc_text:
            fail(f"PER_APP icon not visible in dossier: {name}/{mapping['id']}")
    for mapping in profile.get("source_design_skills", []):
        if mapping["id"] not in doc_text:
            fail(f"PER_APP skill not visible in dossier: {name}/{mapping['id']}")
    for change in profile.get("changelog", []):
        if not change.get("date") or not change.get("origin") or not change.get("status"):
            fail(f"PER_APP changelog entry missing provenance: {name}")
if sum(len(p.get("source_icons", [])) for p in profiles) != profile_counts.get("icon_links"):
    fail("PER_APP icon link count mismatch")
if sum(len(p.get("source_design_skills", [])) for p in profiles) != profile_counts.get("skill_links"):
    fail("PER_APP skills link count mismatch")
cooking = next((p for p in profiles if p.get("name") == "Cooking Anime"), None)
if not cooking:
    fail("PER_APP missing Cooking Anime")
concepts = cooking.get("thematic_icons", [])
if len(concepts) < 30 or len(concepts) != profile_counts.get("cooking_icon_concepts"):
    fail("PER_APP Cooking Anime concept count incomplete")
if len({x.get("id") for x in concepts}) != len(concepts):
    fail("PER_APP duplicate Cooking Anime concept IDs")
if not {"kawaii-gattini", "food-japan", "food-china", "anime-seasonal", "ui-standard"}.issubset(
       {x.get("category") for x in concepts}):
    fail("PER_APP Cooking Anime thematic categories incomplete")
if any(x.get("provider") != "NOT_SELECTED" or x.get("asset_exist_verified") is not False
       or x.get("status") != "DESIGN_IDEA" for x in concepts):
    fail("PER_APP Cooking Anime concept was misrepresented as licensed asset")
cooking_doc = (per_app_dir / "cooking-anime.md").read_text(encoding="utf-8")
if any(x["id"] not in cooking_doc for x in concepts):
    fail("PER_APP Cooking Anime concept not in human-readable dossier")
profiles_index_content = profiles_index.read_text(encoding="utf-8")
if any(("./" + p["id"] + ".md") not in profiles_index_content for p in profiles):
    fail("PER_APP missing dossier index link")

# Six exact X links preserved as DISCOVERY: no unverifiable content promoted to reuse.
x_six_manifest_path = ROOT / "sources" / "X_SIX_DESIGN_DISCOVERY_2026-11-21.json"
x_six_audit_path = ROOT / "sources" / "X_SIX_DESIGN_DISCOVERY_2026-11-21.md"
if not x_six_manifest_path.is_file() or not x_six_audit_path.is_file():
    fail("six-post X discovery manifest/audit missing")
x_six_manifest = json.loads(x_six_manifest_path.read_text(encoding="utf-8"))
x_six_entries = x_six_manifest.get("items", [])
x_six_expected = {
    "0xaditin": "2123469621449850890",
    "ianneo_ai": "2123243488645206322",
    "Jakubantalik": "2122738787667349562",
    "elbeyoglu": "2123328186901836077",
    "amananimates": "2123291753264656823",
    "BenjaminUIX": "2123340929633550834",
}
if (x_six_manifest.get("source_urls_submitted") != 6
        or len(x_six_entries) != 6
        or len({x.get("post_id") for x in x_six_entries}) != 6
        or len({x.get("intake_id") for x in x_six_entries}) != 6
        or x_six_manifest.get("verified_tweet_contents") != 0
        or x_six_manifest.get("approved_visual_styles") != 0
        or x_six_manifest.get("repo_sites_added") != 0
        or x_six_manifest.get("consumer_app_modifications") != 0):
    fail("six-post X discovery intake counts or no-promotion guard drift")
for item in x_six_entries:
    handle = item.get("url_handle")
    postid = item.get("post_id")
    if (x_six_expected.get(handle) != postid
            or item.get("original_link") != f"https://x.com/{handle}/status/{postid}"
            or item.get("maturity") != "DISCOVERY"
            or item.get("reuse_mode") != "REFERENCE_ONLY"
            or item.get("post_text_verified") is not False
            or item.get("post_media_verified") is not False
            or item.get("post_links_verified") is not False
            or item.get("content_description") is not None
            or item.get("design_classification") is not None
            or item.get("license") != "UNKNOWN_UNVERIFIED"
            or item.get("app_mappings") != []
            or item.get("code_imported") is not False
            or item.get("consumer_implemented") is not False):
        fail(f"X discovery link content was improperly inferred/promoted: {handle}")

# Dynamic design directory sources are not GitHub repositories and must not be counted as OSS repo records.
sites_path = ROOT / "sources" / "DESIGN_RESEARCH_SITES.json"
sites_data = json.loads(sites_path.read_text(encoding="utf-8"))
site_items = sites_data.get("sites", [])
if len({s.get("id") for s in site_items}) != len(site_items):
    fail("duplicate design discovery site ID")
if len({s.get("url") for s in site_items}) != len(site_items):
    fail("duplicate design discovery URL")
# Florent 5-link reference-only intake: two canonical providers, two reused, two provider subpages.
florient_manifest_path = ROOT / "sources" / "FLORIENT_STACK_5_REGISTRY_2026-11-20.json"
florient_map_path = ROOT / "UI-UX" / "FLORIENT_STACK_5_APP_MAP_2026-11-20.json"
if not all(p.is_file() for p in (
    florient_manifest_path,
    florient_map_path,
    ROOT / "sources" / "FLORIENT_STACK_5_AUDIT_2026-11-20.md",
    ROOT / "UI-UX" / "FLORIENT_STACK_5_APP_MAP_2026-11-20.md",
)):
    fail("Florent design stack intake missing documents")
florient_manifest = json.loads(florient_manifest_path.read_text(encoding="utf-8"))
florient_links = florient_manifest.get("reference_links", [])
if (florient_manifest.get("submitted_urls") != 5
        or florient_manifest.get("unique_providers") != 4
        or florient_manifest.get("new_providers") != 2
        or len(florient_links) != 5
        or len({x.get("id") for x in florient_links}) != 5
        or len({x.get("url") for x in florient_links}) != 5
        or sum(x.get("state") == "ALREADY_CATALOGUED" for x in florient_links) != 2
        or florient_manifest.get("no_uid_added") is not True
        or florient_manifest.get("no_source_copied") is not True
        or florient_manifest.get("no_consumer_changes") is not True):
    fail("Florent source count, canonical dedup or no-source boundary drift")
site_index = {x.get("id"): x for x in site_items}
for site_id, expected_url in (
    ("DESIGN-SITE-022", "https://fontshare.com/"),
    ("DESIGN-SITE-033", "https://mobbin.com/"),
    ("DESIGN-SITE-047", "https://getshipframe.com/"),
    ("DESIGN-SITE-048", "https://supply.madebyoversight.com/"),
):
    if site_index.get(site_id, {}).get("url") != expected_url:
        fail(f"Florent canonical site ID or URL drift: {site_id}")
oversight_subs = {x.get("id"): x for x in site_index["DESIGN-SITE-048"].get("subpages", [])}
for subid, url in (
    ("DESIGN-SUBL-004", "https://supply.madebyoversight.com/sections"),
    ("DESIGN-SUBL-005", "https://supply.madebyoversight.com/videos"),
):
    if oversight_subs.get(subid, {}).get("url") != url or oversight_subs[subid].get("no_new_site_id") is not True:
        fail(f"Florent Oversight subpage drift: {subid}")
florient_map = json.loads(florient_map_path.read_text(encoding="utf-8"))
florient_edges = florient_map.get("proposals", [])
florient_apps = {x.get("app") for x in florient_edges}
if (len(florient_edges) != 26 or len(florient_apps) != 12
        or len({(x.get("app"), x.get("source_id")) for x in florient_edges}) != 26
        or florient_map.get("proposed_relations") != 26
        or florient_map.get("app_profiles") != 12
        or any(x.get("source_id") not in {item.get("id") for item in florient_links}
               or x.get("status") != "PROPOSED_ONLY"
               or x.get("consumer_implemented") is not False for x in florient_edges)):
    fail("Florent app crosswalk counts, status or identities drift")
florient_profiles = {
    x.get("id"): x
    for x in json.loads((ROOT / "PER_APP" / "REGISTRO_APP_DESIGN.json").read_text(encoding="utf-8")).get("profiles", [])
}
for app_id in florient_apps:
    profile = florient_profiles.get(app_id, {})
    expected = {x["source_id"] for x in florient_edges if x.get("app") == app_id}
    records = [x for x in profile.get("changelog", []) if x.get("type") == "FLORIENT_STACK_5_2026_11_20"]
    dossier = ROOT / "PER_APP" / (app_id + ".md")
    if (not profile or len(records) != 1 or set(records[0].get("source_ids", [])) != expected
            or not dossier.is_file()
            or "FLORIENT_STACK_5_APP_MAP_2026-11-20" not in dossier.read_text(encoding="utf-8")):
        fail(f"Florent per-app dossier or provenance drift: {app_id}")

# Keep AppLlama MCP workflow as a documented Flutter-first original-product prompt.
appllama_prompt_path = ROOT / "sources" / "APPLLAMA_MCP_FLUTTER_PROMPT_2026-11-21.md"
if not appllama_prompt_path.is_file():
    fail("AppLlama Flutter-first prompt not archived")
appllama_prompt = appllama_prompt_path.read_text(encoding="utf-8")
for required in (
    "mcp.appllama.io/mcp", "appllama.io/terms", "Flutter",
    "App Factory", "non incollare TSX", "NON ESEGUITA",
):
    if required not in appllama_prompt:
        fail(f"AppLlama guarded Flutter workflow missing clause: {required}")

# Appllama, Waves, 10 UI libraries, 3 uploaded motion videos and art-app ideation.
art_manifest_path = ROOT / "sources" / "APPLLAMA_MOTION_ART_STACK_REGISTRY_2026-11-21.json"
art_map_path = ROOT / "UI-UX" / "APPLLAMA_MOTION_ART_APP_MAP_2026-11-21.json"
if not all(p.is_file() for p in (
    art_manifest_path, art_map_path,
    ROOT / "sources" / "APPLLAMA_MOTION_ART_STACK_AUDIT_2026-11-21.md",
    ROOT / "UI-UX" / "APPLLAMA_MOTION_ART_APP_MAP_2026-11-21.md",
)):
    fail("Appllama/Motion/Art intake files missing")
art_manifest = json.loads(art_manifest_path.read_text(encoding="utf-8"))
art_records = art_manifest.get("records", [])
art_videos = art_manifest.get("uploaded_video_inspection", [])
if (art_manifest.get("submitted_external_url_occurrences") != 18
        or len(art_records) != 18
        or len({x.get("id") for x in art_records}) != 18
        or len({x.get("url") for x in art_records}) != 18
        or art_manifest.get("unique_new_design_sites") != 11
        or art_manifest.get("new_oss_count") != 6
        or art_manifest.get("unknown_shortlink_count") != 1
        or len(art_videos) != 3
        or art_manifest.get("submitted_video_files") != 3
        or art_manifest.get("created_uids") != 0
        or art_manifest.get("consumer_implementations") != 0
        or art_manifest.get("video_sources_imported") != 0):
    fail("Appllama/Motion/Art manifest counts, dedup or boundaries drift")
if (len({x.get("sha256") for x in art_videos}) != 3
        or any(not re.fullmatch("[0-9a-f]{64}", str(x.get("sha256", "")))
               or x.get("media_uploaded_to_repository") is not False
               or x.get("component_source_imported") is not False
               or x.get("status") != "VIDEO_INSPECTED_REFERENCE_ONLY" for x in art_videos)):
    fail("Appllama/Motion/Art video hashes, source/rights or media import boundary drift")
art_expected_sites = [
    ("DESIGN-SITE-049", "https://appllama.io/mcp"),
    ("DESIGN-SITE-050", "https://dissolve.rselmi.com/"),
    ("DESIGN-SITE-051", "https://anotherboring.day/"),
    ("DESIGN-SITE-052", "https://libraries.dev/"),
    ("DESIGN-SITE-053", "https://magicui.design/"),
    ("DESIGN-SITE-054", "https://21st.dev/"),
    ("DESIGN-SITE-055", "https://ui.shadcn.com/"),
    ("DESIGN-SITE-056", "https://motion-primitives.com/"),
    ("DESIGN-SITE-057", "https://cult-ui.com/"),
    ("DESIGN-SITE-058", "https://animate-ui.com/"),
    ("DESIGN-SITE-059", "https://kibo-ui.com/"),
]
for site_id, url in art_expected_sites:
    if len([s for s in site_items if s.get("id") == site_id and s.get("url") == url]) != 1:
        fail(f"Appllama/Motion/Art canonical site absent: {site_id}")
for existing_site_id in ("DESIGN-SITE-034", "DESIGN-SITE-035", "DESIGN-SITE-040"):
    if len([s for s in site_items if s.get("id") == existing_site_id]) != 1:
        fail(f"Appllama/Motion/Art existing site duplicated: {existing_site_id}")
art_oss = {
    "Appllama/appllama-skills", "seo-skills/seo-audit-skill",
    "ibelick/motion-primitives", "nolly-studio/cult-ui",
    "imskyleen/animate-ui", "shadcnblocks/kibo",
}
if any(repos.count(name) != 1 for name in art_oss):
    fail("Appllama/Motion/Art OSS source missing or duplicated")
art_unresolved = [x for x in art_records if x.get("state") == "UNRESOLVED"]
if (len(art_unresolved) != 1
        or art_unresolved[0].get("url") != "https://t.co/fRjCLeHI5m"
        or art_unresolved[0].get("site_id") is not None
        or art_unresolved[0].get("status") != "DISCOVERY"):
    fail("Unresolved X shortlink was improperly promoted")
art_map = json.loads(art_map_path.read_text(encoding="utf-8"))
art_edges = art_map.get("proposals", [])
art_apps = {x.get("app") for x in art_edges}
if (len(art_edges) != 20 or len(art_apps) != 9
        or art_map.get("proposal_count") != 20
        or art_map.get("existing_app_profiles") != 9
        or art_map.get("new_app_ideas") != 1
        or art_map.get("new_app_idea_id") != "ART-2026-001"
        or len({(x.get("app"), x.get("source_id")) for x in art_edges}) != 20
        or any(x.get("status") != "PROPOSED_ONLY"
               or x.get("consumer_implemented") is not False for x in art_edges)):
    fail("Appllama/Motion/Art proposed relations or app statuses drift")
art_profiles = {
    x.get("id"): x for x in json.loads((ROOT / "PER_APP" / "REGISTRO_APP_DESIGN.json").read_text(encoding="utf-8")).get("profiles", [])
}
for app in art_apps:
    prof = art_profiles.get(app, {})
    expected = {x.get("source_id") for x in art_edges if x.get("app") == app}
    logs = [x for x in prof.get("changelog", []) if x.get("type") == "APPLLAMA_MOTION_ART_STACK_2026_11_21"]
    doc = ROOT / "PER_APP" / (app + ".md")
    if (not prof or len(logs) != 1 or set(logs[0].get("source_ids", [])) != expected
            or not doc.is_file()
            or "APPLLAMA_MOTION_ART_APP_MAP_2026-11-21" not in doc.read_text(encoding="utf-8")):
        fail(f"Appllama/Motion/Art dossier drift: {app}")

devlibraries = next((s for s in site_items if s.get("id") == "DESIGN-SITE-001"), None)
if not devlibraries or devlibraries.get("url") != "https://devlibraries.com/":
    fail("DevLibraries not registered as design discovery directory")
if devlibraries.get("kind") != "MULTI_LIBRARY_UI_AGGREGATOR" or devlibraries.get("status") != "REFERENCE":
    fail("DevLibraries was promoted or misclassified")
for required in ("starc007/ui-components", "starc007/beui-native"):
    if repos.count(required) != 1:
        fail(f"official beUI source missing/duplicated: {required}")
for relative in ("sources/DEVLIBRARIES_DISCOVERY_2026-11-17.md",
                 "sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md",
                 "UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md"):
    if not (ROOT / relative).is_file():
        fail(f"voice/design source document missing: {relative}")
voice_map = json.loads((ROOT / "UI-UX/VOICE_ORB_APP_MAP_2026-11-17.json").read_text(encoding="utf-8"))
if voice_map.get("source_id") != "VOICE-UI-001" or voice_map.get("status") != "REFERENCE":
    fail("Voice Orb source promotion or mismatched source ID")
if voice_map.get("app_implementation") != "NONE":
    fail("Voice Orb claims implementation without evidence")
voice_links = voice_map.get("associations", [])
if len(voice_links) != voice_map.get("counts", {}).get("apps") or len(voice_links) != 10:
    fail("Voice Orb map baseline must have ten proposed applications")
if len({(e.get("source_id"), e.get("app")) for e in voice_links}) != len(voice_links):
    fail("Voice Orb duplicated app relation")
if any(e.get("status") != "PROPOSED_ONLY" or e.get("feature_state") != "NOT_IMPLEMENTED"
       or e.get("fit") not in ("HIGH", "MEDIUM") for e in voice_links):
    fail("Voice Orb incorrectly claims approved/implemented voice")
if any(e.get("app") not in dossier_names for e in voice_links):
    fail("Voice Orb app not cataloged in PER_APP")
if sum(e.get("fit") == "HIGH" for e in voice_links) != voice_map["counts"].get("high"):
    fail("Voice Orb high-fit count mismatch")
if sum(e.get("fit") == "MEDIUM" for e in voice_links) != voice_map["counts"].get("medium"):
    fail("Voice Orb medium-fit count mismatch")
if set(voice_map.get("by_app", {})) != {e.get("app") for e in voice_links}:
    fail("Voice Orb inverse map out of sync")
if profile_counts.get("voice_orb_candidate_apps") != len(voice_links):
    fail("PER_APP voice proposal count out of sync")
for e in voice_links:
    p = next((p for p in profiles if p.get("name") == e["app"]), None)
    if p is None or len(p.get("voice_ui_candidates", [])) != 1:
        fail(f"PER_APP missing voice proposal for {e['app']}")
    proposal = p["voice_ui_candidates"][0]
    for key in ("association_id", "source_id", "fit", "purpose", "surface", "status", "feature_state"):
        if proposal.get(key) != e.get(key):
            fail(f"PER_APP voice proposal drift: {e['app']}/{key}")
    doc = (per_app_dir / (p["id"] + ".md")).read_text(encoding="utf-8")
    if "Voice Orb — proposta futura" not in doc or e["purpose"] not in doc:
        fail(f"PER_APP human-readable voice proposal missing: {e['app']}")
if any(p.get("voice_ui_candidates") for p in profiles if p.get("name") not in voice_map["by_app"]):
    fail("PER_APP voice proposal exists outside the canonical voice map")

# EaseUI/Amicro pattern references and the user-provided loader visual are design-only.
for required_repo in ("rjcuff/easeui", "Subhan-code/Amicro--Micro-transitions-"):
    if repos.count(required_repo) != 1:
        fail(f"missing/duplicated motion source: {required_repo}")
for site_id, expected_url in (
        ("DESIGN-SITE-005", "https://easeui.dev/"),
        ("DESIGN-SITE-006", "https://amicro.vercel.app/")):
    match = [s for s in site_items if s.get("id") == site_id]
    if len(match) != 1 or match[0].get("url") != expected_url or match[0].get("status") != "REFERENCE":
        fail(f"invalid design research site: {site_id}")
pattern_paths = (
    ROOT / "UI-UX" / "EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.json",
    ROOT / "UI-UX" / "EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md",
    ROOT / "sources" / "EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md",
)
if not all(path.is_file() for path in pattern_paths):
    fail("EaseUI/Amicro motion audit or map absent")
pattern_map = json.loads(pattern_paths[0].read_text(encoding="utf-8"))
pattern_list = pattern_map.get("patterns", [])
pattern_links = pattern_map.get("associations", [])
pattern_counts = pattern_map.get("counts", {})
if pattern_map.get("batch") != "EASEUI_AMICRO_LOADER_REFERENCES_2026_11_17":
    fail("EaseUI/Amicro batch identity incorrect")
if pattern_map.get("status") != "REFERENCE_ONLY" or pattern_map.get("consumer_implementation") != "NONE":
    fail("motion references incorrectly promoted or claimed implemented")
if len(pattern_list) != 6 or len({x.get("code") for x in pattern_list}) != 6:
    fail("six unique theme/motion/loading patterns expected")
if len(pattern_links) != pattern_counts.get("links"):
    fail("motion crosswalk count mismatch")
if len({(e.get("pattern_id"),e.get("app")) for e in pattern_links}) != len(pattern_links):
    fail("duplicate motion app pattern pairing")
if any(e.get("fit") not in ("HIGH","MEDIUM") or e.get("status") != "PROPOSED_ONLY" for e in pattern_links):
    fail("motion association has invalid state/fit")
if any(p.get("status") != "REFERENCE" or p.get("app_implementation") != "NONE" for p in pattern_list):
    fail("motion source prematurely promoted")
if sum(p.get("evidence") == "SOURCE_FILE_READ" for p in pattern_list) != 5:
    fail("five source files have now been read across EaseUI/Amicro initial intake")
if sum(p.get("evidence") == "DESCRIPTIVE_CATALOG_ONLY" for p in pattern_list) != 0:
    fail("initial four Amicro descriptions have verified source files and must not be left stale")
user_screenshot = [p for p in pattern_list if p.get("evidence") == "USER_IMAGE_NOT_ARCHIVED_AS_BINARY"]
if len(user_screenshot) != 1 or user_screenshot[0].get("source") != "USER_IMAGE":
    fail("user screenshot was misrepresented as executable or persisted file")
if pattern_counts.get("apps") != len({e.get("app") for e in pattern_links}):
    fail("motion mapped app count incorrect")
if any(e.get("app") not in dossier_names for e in pattern_links):
    fail("motion mapping names an app without a dossier")
if set(pattern_map.get("by_app", {})) != {e["app"] for e in pattern_links}:
    fail("motion by-app inverse mapping incomplete")
if set(pattern_map.get("by_pattern", {})) != {p["code"] for p in pattern_list}:
    fail("motion by-pattern inverse mapping incomplete")
for pattern in pattern_list:
    expected = {(e["app"],e["fit"],e["application"]) for e in pattern_links if e["pattern_id"]==pattern["code"]}
    actual = {(e["app"],e["fit"],e["application"]) for e in pattern_map["by_pattern"][pattern["code"]]}
    if expected != actual:
        fail(f"motion by-pattern mapping drift for {pattern['code']}")
if profile_counts.get("motion_design_candidate_apps") != pattern_counts.get("apps"):
    fail("motion per-app profile count mismatch")
if profile_counts.get("motion_design_candidate_relations") != len(pattern_links):
    fail("motion per-app relation count mismatch")
for p in profiles:
    links = p.get("motion_design_candidates", [])
    expected = {(e["pattern_id"],e["fit"],e["application"]) for e in pattern_links if e["app"] == p["name"]}
    actual = {(e["pattern_id"],e["fit"],e["application"]) for e in links}
    if expected != actual or len(actual) != len(links):
        fail(f"motion per-app mapping drift for {p['name']}")
    if links:
        doc = (per_app_dir / (p["id"] + ".md")).read_text(encoding="utf-8")
        if "Tema, transizioni, tendine e loader" not in doc:
            fail(f"motion ideas not documented in {p['name']} dossier")
        for link in links:
            if link["pattern_id"] not in doc:
                fail(f"pattern {link['pattern_id']} missing in {p['name']} dossier")

# Six additional Amicro components: provenance and 19-app bidirectional catalogue.
if len(re.findall(r"^  - batch_id: AMICRO_SIX_COMPONENTS_2026_11_17$", oss, re.MULTILINE)) != 1:
    fail("Amicro six-component intake not registered exactly once")
amicro_path = ROOT / "UI-UX" / "AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.json"
amicro_docs = (
    amicro_path,
    ROOT / "UI-UX" / "AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md",
    ROOT / "sources" / "AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md",
)
if not all(p.is_file() for p in amicro_docs):
    fail("Amicro six-component catalogue/docs missing")
amicro = json.loads(amicro_path.read_text(encoding="utf-8"))
new_patterns = amicro.get("patterns", [])
new_links = amicro.get("associations", [])
new_counts = amicro.get("counts", {})
if amicro.get("batch") != "AMICRO_SIX_COMPONENTS_2026_11_17":
    fail("Amicro six-component batch mismatch")
if amicro.get("status") != "REFERENCE" or amicro.get("consumer_implementation") != "NONE":
    fail("Amicro six-component intake incorrectly promoted or marked implemented")
if amicro.get("origin_repository") != "Subhan-code/Amicro--Micro-transitions-":
    fail("Amicro six-component origin mismatch")
if not re.fullmatch(r"[0-9a-f]{40}", str(amicro.get("origin_ref", ""))):
    fail("Amicro six-component source not commit-pinned")
if len(new_patterns) != 6 or len({p.get("id") for p in new_patterns}) != 6:
    fail("Amicro six-component unique ID invariant failed")
if len({p.get("url") for p in new_patterns}) != 6:
    fail("Amicro six-component duplicate source link")
if len(new_links) != new_counts.get("associations"):
    fail("Amicro six-component edge count drift")
if len(new_links) != 60:
    fail("Amicro six-component expected 60 proposed associations")
if len({(e.get("pattern_id"), e.get("app")) for e in new_links}) != len(new_links):
    fail("Amicro six-component duplicate app association")
if any(e.get("status") != "PROPOSED_ONLY" or e.get("implementation") != "NONE"
       or e.get("fit") not in ("HIGH", "MEDIUM") for e in new_links):
    fail("Amicro six-component app relation incorrectly promoted")
if any(e.get("app") not in dossier_names for e in new_links):
    fail("Amicro six-component orphan destination")
if len({e["app"] for e in new_links}) != new_counts.get("apps"):
    fail("Amicro six-component app count drift")
if sum(e["fit"] == "HIGH" for e in new_links) != new_counts.get("high"):
    fail("Amicro six-component HIGH count mismatch")
if sum(e["fit"] == "MEDIUM" for e in new_links) != new_counts.get("medium"):
    fail("Amicro six-component MEDIUM count mismatch")
source_read = [p for p in new_patterns if p.get("source_status") == "SOURCE_FILE_READ"]
not_located = [p for p in new_patterns if p.get("source_status") == "EXACT_SOURCE_NOT_LOCATED"]
if len(source_read) != 4 or len(not_located) != 2:
    fail("Amicro six-component verified/unverified source boundary drift")
for p in source_read:
    if not p.get("file") or not re.fullmatch(r"[0-9a-f]{40}", str(p.get("blob", ""))) or not p.get("export"):
        fail(f"Amicro source file/sha/export missing: {p.get('id')}")
for p in not_located:
    if p.get("file") is not None or p.get("blob") is not None or p.get("export") is not None:
        fail(f"Amicro unidentified component given invented executable source: {p.get('id')}")
if any(p.get("consumer_status") != "NOT_IMPLEMENTED" or p.get("design_maturity") != "REFERENCE"
       for p in new_patterns):
    fail("Amicro pattern consumer implementation or maturity overclaimed")
if set(amicro.get("by_pattern", {})) != {p["id"] for p in new_patterns}:
    fail("Amicro inverse pattern-key coverage mismatch")
if set(amicro.get("by_app", {})) != {e["app"] for e in new_links}:
    fail("Amicro inverse app-key coverage mismatch")
for p in new_patterns:
    expected = {(e["app"],e["fit"],e["usage"]) for e in new_links if e["pattern_id"]==p["id"]}
    actual = {(e["app"],e["fit"],e["usage"]) for e in amicro["by_pattern"][p["id"]]}
    if expected != actual:
        fail(f"Amicro by-pattern relation drift: {p['id']}")
for app, relations in amicro["by_app"].items():
    expected = {(e["pattern_id"],e["fit"],e["usage"]) for e in new_links if e["app"]==app}
    actual = {(e["pattern_id"],e["fit"],e["usage"]) for e in relations}
    if expected != actual:
        fail(f"Amicro by-app relation drift: {app}")
if profile_counts.get("amicro_six_candidate_apps") != new_counts.get("apps"):
    fail("Amicro per-app coverage count drift")
if profile_counts.get("amicro_six_candidate_links") != len(new_links):
    fail("Amicro per-app association count drift")
for profile in profiles:
    relations = profile.get("amicro_six_candidates", [])
    expected = {(e["pattern_id"],e["fit"],e["usage"]) for e in new_links
                if e["app"]==profile["name"]}
    actual = {(e["pattern_id"],e["fit"],e["usage"]) for e in relations}
    if actual != expected or len(relations) != len(actual):
        fail(f"Amicro per-app profile relation drift: {profile['name']}")
    if relations:
        text_doc = (per_app_dir / (profile["id"] + ".md")).read_text(encoding="utf-8")
        if "Nuove microinterazioni Amicro — 6 references" not in text_doc:
            fail(f"Amicro missing human dossier: {profile['name']}")
        if any(link["pattern_id"] not in text_doc for link in relations):
            fail(f"Amicro missing pattern in dossier: {profile['name']}")
# Initial intake source correction is still REFERENCE, not COPY_READY.
for prior in pattern_list:
    if prior.get("code") in ("DSP-002","DSP-003","DSP-004","DSP-005"):
        if prior.get("evidence") != "SOURCE_FILE_READ" or not prior.get("source_path"):
            fail(f"stale Amicro original intake source: {prior.get('code')}")

# Watermelon UI: exact source confidence, source repo dedupe, and per-app dossier consistency.
if repos.count("WatermelonCorp/watermelon-platform") != 1:
    fail("Watermelon source repository must be registered once")
wm_sites = [s for s in site_items if s.get("id") == "DESIGN-SITE-007"]
if len(wm_sites) != 1 or wm_sites[0].get("url") != "https://ui.watermelon.sh/" or wm_sites[0].get("status") != "REFERENCE":
    fail("Watermelon UI source site registration missing or promoted")
wm_files = (
    ROOT / "UI-UX" / "WATERMELON_NINE_APP_MAP_2026-11-17.json",
    ROOT / "UI-UX" / "WATERMELON_NINE_APP_MAP_2026-11-17.md",
    ROOT / "sources" / "WATERMELON_UI_NINE_AUDIT_2026-11-17.md",
)
if not all(p.is_file() for p in wm_files):
    fail("Watermelon required registry/audit documents missing")
wm = json.loads(wm_files[0].read_text(encoding="utf-8"))
wm_components = wm.get("components", [])
wm_edges = wm.get("associations", [])
wm_counts = wm.get("counts", {})
if wm.get("batch") != "WATERMELON_NINE_2026_11_17":
    fail("Watermelon intake batch identity mismatch")
if wm.get("status") != "REFERENCE_ONLY" or wm.get("consumer_implementation") != "NONE":
    fail("Watermelon proposals prematurely promoted or claimed implemented")
if wm.get("source_repository") != "WatermelonCorp/watermelon-platform":
    fail("Watermelon repo identity mismatch")
if not re.fullmatch(r"[0-9a-f]{40}", str(wm.get("source_commit", ""))):
    fail("Watermelon origin SHA must be immutable")
if len(wm_components) != 9 or len({c.get("id") for c in wm_components}) != 9:
    fail("Watermelon requires nine unique component IDs")
if len({c.get("source_user_url") for c in wm_components}) != 9:
    fail("Watermelon duplicate source URL")
if len(wm_edges) != wm_counts.get("associations") or len(wm_edges) != 73:
    fail("Watermelon mapping expected 73 unique associations")
if len({(e.get("component_id"),e.get("app")) for e in wm_edges}) != len(wm_edges):
    fail("Watermelon duplicated component-app edge")
if any(e.get("status") != "PROPOSED_ONLY" or e.get("consumer_implementation") != "NONE"
       or e.get("fit") not in ("HIGH","MEDIUM") for e in wm_edges):
    fail("Watermelon association wrongly claims app implementation")
if any(e.get("app") not in dossier_names for e in wm_edges):
    fail("Watermelon candidate app has no dossier")
if len({e["app"] for e in wm_edges}) != wm_counts.get("apps"):
    fail("Watermelon mapped app count differs")
if sum(e["fit"] == "HIGH" for e in wm_edges) != wm_counts.get("high"):
    fail("Watermelon HIGH count differs")
if sum(e["fit"] == "MEDIUM" for e in wm_edges) != wm_counts.get("medium"):
    fail("Watermelon MEDIUM count differs")
verified = [comp for comp in wm_components if comp.get("evidence") == "SOURCE_FILE_READ"]
unlocated = [comp for comp in wm_components if comp.get("evidence") == "EXACT_SOURCE_NOT_LOCATED"]
if len(verified) != 6 or len(unlocated) != 3:
    fail("Watermelon source-confidence invariant changed")
if {x["slug"] for x in unlocated} != {"text-gradient","notification-list","flip-clock"}:
    fail("Watermelon three unlocated exact names mislabeled")
for comp in verified:
    if not comp.get("source_path") or not re.fullmatch(r"[0-9a-f]{40}", str(comp.get("source_blob_sha", ""))):
        fail(f"Watermelon named source evidence missing: {comp.get('id')}")
    if not comp.get("metadata_path") or not re.fullmatch(r"[0-9a-f]{40}", str(comp.get("metadata_blob_sha", ""))):
        fail(f"Watermelon component metadata missing: {comp.get('id')}")
for comp in unlocated:
    if any(comp.get(key) is not None for key in ("source_path","source_blob_sha","metadata_path","metadata_blob_sha")):
        fail(f"Unlocated Watermelon component given invented source: {comp.get('id')}")
if any(comp.get("adoption") != "REFERENCE" or comp.get("consumer_implementation") != "NONE" for comp in wm_components):
    fail("Watermelon source maturity overclaimed")
if set(wm.get("by_component", {})) != {c["id"] for c in wm_components}:
    fail("Watermelon inverse component map incomplete")
if set(wm.get("by_app", {})) != {e["app"] for e in wm_edges}:
    fail("Watermelon inverse per-app map incomplete")
for comp in wm_components:
    expected = {(e["app"],e["fit"],e["use_case"]) for e in wm_edges if e["component_id"] == comp["id"]}
    actual = {(e["app"],e["fit"],e["use_case"]) for e in wm["by_component"][comp["id"]]}
    if expected != actual:
        fail(f"Watermelon component associations mismatch: {comp['id']}")
for app, incoming in wm["by_app"].items():
    expected = {(e["component_id"],e["fit"],e["use_case"]) for e in wm_edges if e["app"] == app}
    actual = {(e["component_id"],e["fit"],e["use_case"]) for e in incoming}
    if expected != actual:
        fail(f"Watermelon per-app inverse mapping differs: {app}")
if profile_counts.get("watermelon_ui_candidate_apps") != wm_counts.get("apps"):
    fail("Watermelon profile app coverage count mismatch")
if profile_counts.get("watermelon_ui_candidate_links") != len(wm_edges):
    fail("Watermelon profile edge count mismatch")
for prof in profiles:
    relations = prof.get("watermelon_ui_candidates", [])
    expected = {(e["component_id"],e["fit"],e["use_case"]) for e in wm_edges if e["app"] == prof["name"]}
    actual = {(e["component_id"],e["fit"],e["use_case"]) for e in relations}
    if actual != expected or len(relations) != len(actual):
        fail(f"Watermelon per-app dossier relation drift: {prof['name']}")
    if relations:
        human = (per_app_dir / (prof["id"] + ".md")).read_text(encoding="utf-8")
        if "Watermelon UI — 9 riferimenti" not in human:
            fail(f"Watermelon dossier not updated: {prof['name']}")
        for link in relations:
            if link["component_id"] not in human:
                fail(f"Watermelon idea missing from dossier: {prof['name']}")
anna_p = next((p for p in profiles if p.get("name") == "Anna's Diary"), None)
if not anna_p:
    fail("Watermelon lacks Anna's Diary baseline")
anna_today = anna_p.get("anna_today_daily_agenda_proposal", {})
if anna_today.get("status") != "PROPOSED_ONLY" or anna_today.get("implementation_scope") != "NOT_APPROVED_OR_IMPLEMENTED":
    fail("Anna daily brief was treated as approved/implemented")
if set(anna_today.get("user_requested_trigger_modes", [])) != {"first_app_open_each_local_day","user_configured_time"}:
    fail("Anna daily brief must preserve both user timing requirements")
if anna_today.get("source_component_id") != "WML-008" or anna_today.get("source_evidence") != "EXACT_SOURCE_NOT_LOCATED":
    fail("Anna daily brief must not assert unsupported Notification List source")
anna_carousel = anna_p.get("anna_memories_carousel_proposal", {})
if anna_carousel.get("component_id") != "WML-001" or anna_carousel.get("status") != "PROPOSED_ONLY":
    fail("Anna Memories Carousel recommendation missing")
anna_human = (per_app_dir / (anna_p["id"] + ".md")).read_text(encoding="utf-8")
for phrase in ("prima apertura", "orario", "Ricordi", "notifica di sistema", "Carousel Slider"):
    if phrase not in anna_human:
        fail(f"Anna's Diary missing user's daily brief requirement: {phrase}")


# User-supplied DevLibraries screenshot intake: 30 references, no claim of logged-in account access.
bookmarks_file = ROOT / "sources" / "DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.json"
bookmarks_md = ROOT / "sources" / "DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md"
bookmarks_matrix = ROOT / "UI-UX" / "DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md"
bookmarks_workflow = ROOT / "sources" / "DEVLIBRARIES_BOOKMARKS_INTAKE.md"
if not all(f.is_file() for f in (bookmarks_file,bookmarks_md,bookmarks_matrix,bookmarks_workflow)):
    fail("DevLibraries screenshot bookmarks registry/docs missing")
bm = json.loads(bookmarks_file.read_text(encoding="utf-8"))
bm_items = bm.get("items", [])
bm_edges = bm.get("associations", [])
bm_counts = bm.get("counts", {})
screens = bm.get("screenshot_files", [])
if bm.get("batch") != "DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026_11_17":
    fail("DevLibraries screenshot batch mismatch")
if bm.get("status") != "VISUAL_INTAKE_REGISTERED" or bm.get("repo_impact") != "DOCUMENTATION_ONLY":
    fail("DevLibraries screenshot batch has incorrect completion status")
if bm.get("user_account_read") is not False or bm.get("source_repo_new") != 0:
    fail("DevLibraries screenshots cannot claim account access or new source repos")
if len(screens) != 3 or sum(s.get("items", 0) for s in screens) != 30:
    fail("DevLibraries screenshot provenance/observed rows mismatch")
if [s.get("items") for s in screens] != [18, 8, 4]:
    fail("DevLibraries source screenshot batch row counts changed")
if any(not re.fullmatch(r"[0-9a-f]{64}", str(s.get("sha256",""))) or
       s.get("asset_in_repo") is not False for s in screens):
    fail("DevLibraries screenshot SHA-256 format or binary asset boundary invalid")
if len(bm_items) != 30 or len({i.get("id") for i in bm_items}) != 30:
    fail("DevLibraries screenshot expected 30 unique item IDs")
if len({(i.get("screenshot_number"),i.get("screenshot_order")) for i in bm_items}) != 30:
    fail("DevLibraries screenshot item positions not unique")
if any(i.get("id") != f"DBM-{n:03d}" for n,i in enumerate(bm_items, 1)):
    fail("DevLibraries screenshot items out of canonical ID order")
if any(i.get("screenshot_number") not in (1,2,3) or
       i.get("screenshot_sha256") != screens[i["screenshot_number"]-1]["sha256"]
       for i in bm_items):
    fail("DevLibraries item screenshot hash provenance mismatch")
if any(i.get("status") != "REFERENCE" or i.get("implementation_status") != "NOT_IMPLEMENTED"
       or i.get("asset_status") != "SCREENSHOT_NOT_COMMITTED" for i in bm_items):
    fail("DevLibraries screenshots falsely marked implemented or screenshot archived")
if bm_counts.get("screenshot_cards") != len(bm_items) or bm_counts.get("screenshots") != len(screens):
    fail("DevLibraries total counts inconsistent")
provider_count = {x:sum(i.get("provider")==x for i in bm_items)
                  for x in ("Amicro","Watermelon UI","UNVERIFIED_PROVIDER")}
if (provider_count["Amicro"],provider_count["Watermelon UI"],provider_count["UNVERIFIED_PROVIDER"]) != (23,3,4):
    fail("DevLibraries screenshot provider classification drift")
if bm_counts.get("amicro") != 23 or bm_counts.get("watermelon") != 3 or bm_counts.get("unverified_provider") != 4:
    fail("DevLibraries reported provider counts drift")
paths = [i for i in bm_items if i.get("source_path")]
unresolved = [i for i in bm_items if not i.get("source_path")]
if len(paths) != 25 or len(unresolved) != 5:
    fail("DevLibraries source-path confidence boundary must be 25/5")
if bm_counts.get("source_path_pinned") != len(paths) or bm_counts.get("unverified_source") != len(unresolved):
    fail("DevLibraries source evidence stats invalid")
for i in paths:
    if (not re.fullmatch(r"[0-9a-f]{40}", str(i.get("source_blob_sha",""))) or
        not re.fullmatch(r"[0-9a-f]{40}", str(i.get("source_commit","")))):
        fail(f"DevLibraries missing source SHA or commit: {i.get('id')}")
    if i.get("source_evidence") not in ("SOURCE_FILE_READ","SOURCE_FILE_PREVIOUSLY_READ","SOURCE_PATH_PINNED"):
        fail(f"DevLibraries unsupported source evidence: {i.get('id')}")
for i in unresolved:
    if i.get("source_evidence") not in ("USER_SCREENSHOT_ONLY","EXACT_SOURCE_NOT_LOCATED"):
        fail(f"DevLibraries unresolved item misclassified: {i.get('id')}")
if any(i.get("provider") == "UNVERIFIED_PROVIDER" and
       any(i.get(key) is not None for key in ("source_path","source_repo","source_commit","source_blob_sha"))
       for i in bm_items):
    fail("DevLibraries unidentified visual attributed to guessed provider")
if any(i.get("provider") == "Amicro" and
       (i.get("source_repo") != "Subhan-code/Amicro--Micro-transitions-" or
        i.get("source_path") != "registry/ui/loading/" + i.get("slug","") + ".tsx")
       for i in bm_items):
    fail("DevLibraries Amicro pinned source path/provider mismatch")
if any(i.get("provider") == "Watermelon UI" and
       i.get("source_repo") != "WatermelonCorp/watermelon-platform" for i in bm_items):
    fail("DevLibraries Watermelon source attribution mismatch")
duplicate_refs = {i.get("title"):i.get("existing_design_ref") for i in bm_items
                  if i.get("existing_design_ref")}
if duplicate_refs != {"Accordion Loader":"AMX-006",
                      "Range Selection Slider":"WML-004",
                      "Notification List":"WML-008"}:
    fail("DevLibraries previously cataloged component dedupe links drift")
if bm_counts.get("existing_deduped") != 3 or bm_counts.get("new_curation_items") != 27:
    fail("DevLibraries deduplicated source count drift")
notification = next((i for i in bm_items if i.get("title") == "Notification List"),None)
if not notification or notification.get("source_evidence") != "EXACT_SOURCE_NOT_LOCATED" or notification.get("source_path"):
    fail("DevLibraries Notification List source may not be inferred from user screenshot")
by_name = {i["title"]:i for i in bm_items}
if by_name["Infinite Spiral"]["category"] != "UNVERIFIED_MEDIA_VISUAL":
    fail("DevLibraries Infinite Spiral must not be reported as loader")
if by_name["Face Id Scan"]["category"] != "BIOMETRIC_STATUS_VISUAL_ONLY":
    fail("DevLibraries Face ID UI may not be misrepresented as security engine")
if len(bm_edges) != 120 or len(bm_edges) != bm_counts.get("associations"):
    fail("DevLibraries screenshot edge count not 120")
if len({(e.get("bookmark_id"),e.get("app")) for e in bm_edges}) != len(bm_edges):
    fail("DevLibraries duplicate screenshot app association")
if any(e.get("bookmark_id") not in {i["id"] for i in bm_items}
       or e.get("app") not in dossier_names
       or e.get("fit") not in ("HIGH","MEDIUM")
       or e.get("status") != "PROPOSED_ONLY" for e in bm_edges):
    fail("DevLibraries screenshot edge foreign key/status invalid")
bm_apps = {e.get("app") for e in bm_edges}
if len(bm_apps) != bm_counts.get("apps") or len(bm_apps) != 20:
    fail("DevLibraries screenshot app count drift")
if set(bm.get("by_app",{})) != bm_apps:
    fail("DevLibraries screenshot inverse app keys mismatch")
if set(bm.get("by_item",{})) != {i["id"] for i in bm_items}:
    fail("DevLibraries screenshot inverse item keys mismatch")
for app, refs in bm.get("by_app",{}).items():
    expected={(e["bookmark_id"],e["fit"],e["use_case"]) for e in bm_edges if e["app"]==app}
    actual={(e["bookmark_id"],e["fit"],e["use_case"]) for e in refs}
    if actual != expected:
        fail(f"DevLibraries screenshot by_app mismatch: {app}")
for identifier, refs in bm.get("by_item",{}).items():
    expected={(e["app"],e["fit"],e["use_case"]) for e in bm_edges if e["bookmark_id"]==identifier}
    actual={(e["app"],e["fit"],e["use_case"]) for e in refs}
    if actual != expected:
        fail(f"DevLibraries screenshot by_item mismatch: {identifier}")
if (profile_counts.get("bookmarks_screenshot_profiles") != 20 or
    profile_counts.get("bookmarks_screenshot_edges") != 120 or
    profile_counts.get("bookmarks_screenshot_cards") != 30):
    fail("DevLibraries screenshot aggregate profile stats mismatch")
for profile in profiles:
    refs=profile.get("bookmarked_visual_references",[])
    expected={(e["bookmark_id"],e["fit"],e["use_case"]) for e in bm_edges if e["app"]==profile["name"]}
    observed={(e["bookmark_id"],e["fit"],e["use_case"]) for e in refs}
    if observed != expected or len(refs) != len(observed):
        fail(f"DevLibraries screenshot per-app profile drift: {profile['name']}")
    if refs:
        doc=(per_app_dir / (profile["id"] + ".md")).read_text(encoding="utf-8")
        if "DevLibraries Bookmarks — screenshot 17/11/2026" not in doc:
            fail(f"DevLibraries screenshot dossier missing: {profile['name']}")
        if any(e["bookmark_id"] not in doc for e in refs):
            fail(f"DevLibraries screenshot mapping not visible in dossier: {profile['name']}")
        if any(e.get("status") != "PROPOSED_ONLY" or e.get("implementation") != "NOT_IMPLEMENTED"
               or e.get("image_binary_in_repo") is not False for e in refs):
            fail(f"DevLibraries screenshot dossier promoted without consumer evidence: {profile['name']}")
anna_bm = next(p for p in profiles if p["name"] == "Anna's Diary")
brief = anna_bm.get("anna_today_daily_agenda_proposal",{})
if (brief.get("visual_preview_seen_in_user_screenshot") is not True or
    brief.get("source_code_evidence") != "EXACT_SOURCE_NOT_LOCATED" or
    brief.get("approval_unchanged") != "PROPOSED_ONLY"):
    fail("DevLibraries screenshot cannot promote Anna Notification List implementation")
if set(brief.get("user_requested_trigger_modes",[])) != {"first_app_open_each_local_day","user_configured_time"}:
    fail("DevLibraries screenshot must preserve Anna Home Oggi trigger choices")


# Impeccable Designing design-quality extension validation (reference only).
impeccable_doc = ROOT / "sources" / "IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md"
impeccable_map_path = ROOT / "UI-UX" / "IMPECCABLE_DESIGNING_APP_MATRIX_2026-11-17.json"
if not impeccable_doc.is_file() or not impeccable_map_path.is_file():
    fail("Impeccable Designing documentation or app matrix missing")
impeccable_map = json.loads(impeccable_map_path.read_text(encoding="utf-8"))
impeccable_apps = impeccable_map.get("by_app", {})
impeccable_workflow = impeccable_map.get("workflow", [])
if impeccable_map.get("batch_id") != "IMPECCABLE_DESIGNING_EXPANSION_2026_11_17":
    fail("Impeccable Designing batch ID changed")
if impeccable_map.get("canonical_source_id") != "DSK-002" or impeccable_map.get("canonical_repo") != "pbakaus/impeccable":
    fail("Impeccable Designing must use existing source reference")
if impeccable_map.get("counts", {}).get("new_source_repos") != 0:
    fail("Impeccable Designing may not duplicate source repositories")
if len(impeccable_apps) != 10 or len(impeccable_workflow) != 8:
    fail("Impeccable Designing acceptance baseline requires 10 apps and 8 gates")
if len({w.get("id") for w in impeccable_workflow}) != len(impeccable_workflow):
    fail("Impeccable Designing duplicate quality gate")
if impeccable_map.get("platform_facts", {}).get("detector") != "Web source/rendered HTML/CSS only":
    fail("Impeccable detector must be explicitly Web only")
if impeccable_map.get("platform_facts", {}).get("native", "").startswith("Use native") is False:
    fail("Impeccable native QA boundary missing")
if oss.count('repo: "pbakaus/impeccable"') != 1:
    fail("Impeccable existing OSS skill missing/duplicated")
if not impeccable_apps.keys() <= dossier_names:
    fail("Impeccable Designing mapped app missing from official dossiers")
original_skills = json.loads((ROOT / "UI-UX" / "MATRICE_REPO_DESIGN_APP_2026-11-17.json").read_text(encoding="utf-8"))
old_impeccable = {e["app"] for e in original_skills.get("associations", []) if e.get("source_id") == "DSK-002"}
if set(impeccable_apps) != old_impeccable:
    fail("Impeccable Designing must not invent new per-app relations")
if profile_counts.get("impeccable_designing_quality_candidate_apps") != len(impeccable_apps):
    fail("Impeccable Designing per-app quality count drift")
if profile_counts.get("impeccable_designing_workflow_gates") != len(impeccable_workflow):
    fail("Impeccable Designing quality gate count drift")
for profile in profiles:
    mapped = impeccable_apps.get(profile["name"])
    local = profile.get("impeccable_designing_quality")
    if mapped is None and local is not None:
        fail(f"Impeccable non-candidate profile unexpectedly modified: {profile['name']}")
    if mapped is None:
        continue
    if not local or local.get("canonical_skill_id") != "DSK-002" or local.get("reference_status") != "REFERENCE_ONLY":
        fail(f"Impeccable profile provenance missing: {profile['name']}")
    if local.get("consumer_qa_state") != "NOT_EXECUTED" or local.get("dependency_added") is not False:
        fail(f"Impeccable profile prematurely claims QA execution or dependencies: {profile['name']}")
    for k in ("source_id","fit","priority","mode","surface","objective","acceptance_checks","status","implementation"):
        if local.get(k) != mapped.get(k):
            fail(f"Impeccable per-app quality drift: {profile['name']} / {k}")
    if len(local.get("acceptance_checks", [])) < 3:
        fail(f"Impeccable acceptance list under-specified: {profile['name']}")
    dossier = (per_app_dir / (profile["id"] + ".md")).read_text(encoding="utf-8")
    if "Impeccable — metodologia Designing" not in dossier:
        fail(f"Impeccable quality checklist missing in app dossier: {profile['name']}")
    for check in local["acceptance_checks"]:
        if check not in dossier:
            fail(f"Impeccable app dossier missing specific acceptance check: {profile['name']}")

print(
    f"Design-App validation PASS: {len(pattern_ids)} patterns, "
    f"{len(style_ids)} styles, {len(repos)} OSS sources "
    f"({curated_count}+{new_batch_count} curated, {sound_count} sound), "
    f"{len(snapshot_paths)} snapshots, {len(coverage_rows)} covered products."
)
