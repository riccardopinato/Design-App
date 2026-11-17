#!/usr/bin/env python3
from pathlib import Path
import json
import re

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
expected_source_count = 95 + ruixen_intake + 2 * dock_intake + 7 * visual_intake + 10 * skills_intake + 2 * voice_intake + 2 * motion_intake + watermelon_intake
if len(repos) != expected_source_count or len(set(repos)) != expected_source_count:
    fail(f"expected {expected_source_count} unique OSS design sources, found {len(repos)} / {len(set(repos))} unique")
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

# Dynamic design directory sources are not GitHub repositories and must not be counted as OSS repo records.
sites_path = ROOT / "sources" / "DESIGN_RESEARCH_SITES.json"
sites_data = json.loads(sites_path.read_text(encoding="utf-8"))
site_items = sites_data.get("sites", [])
if len({s.get("id") for s in site_items}) != len(site_items):
    fail("duplicate design discovery site ID")
if len({s.get("url") for s in site_items}) != len(site_items):
    fail("duplicate design discovery URL")
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


print(
    f"Design-App validation PASS: {len(pattern_ids)} patterns, "
    f"{len(style_ids)} styles, {len(repos)} OSS sources "
    f"({curated_count}+{new_batch_count} curated, {sound_count} sound), "
    f"{len(snapshot_paths)} snapshots, {len(coverage_rows)} covered products."
)
