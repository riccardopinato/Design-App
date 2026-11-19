#!/usr/bin/env python3
"""Create an inspectable visual QA contact sheet for archived component screenshots.

This report does not certify component source/runtime correctness. It helps
reviewers identify apparently blank, near-duplicate or cropped captures.
"""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path
import statistics

from PIL import Image, ImageDraw, ImageStat

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "docs/assets/componenti"
OUT = ROOT / "preview-qa-output"
CAT = json.loads((ROOT / "BIBLIOTECA_COMPONENTI/CATALOGO.json").read_text(encoding="utf-8"))
MAN = json.loads((ROOT / "BIBLIOTECA_COMPONENTI/ANTEPRIME.json").read_text(encoding="utf-8"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    thumbs = []
    for item in CAT["components"]:
        # Preserve the exact 110 Uiverse-only baseline contact sheet.
        if item["source_site"] != "UIVERSE":
            continue
        cid = item["id"]
        rec = MAN["previews"][cid]
        if not rec["image_path"]:
            continue
        path = ROOT / rec["image_path"]
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            values = ImageStat.Stat(rgb).stddev
            color_std = round(statistics.fmean(values), 2)
            result = {
                "id": cid,
                "size": list(rgb.size),
                "bytes": path.stat().st_size,
                "color_stddev": color_std,
                "near_flat_candidate": color_std < 4,
            }
            records.append(result)
            copy = rgb.copy()
            copy.thumbnail((165, 110))
            thumbs.append((cid, copy))
    if len(records) != 110 or set(r["id"] for r in records) != {
        c["id"] for c in CAT["components"] if c["source_site"] == "UIVERSE"
    }:
        raise ValueError("Uiverse screenshots must map to exactly 110 canonical IDs")
    columns, width, height = 8, 190, 145
    rows = (len(thumbs) + columns - 1) // columns
    board = Image.new("RGB", (columns * width, rows * height), "#e8edf5")
    d = ImageDraw.Draw(board)
    for index, (cid, mini) in enumerate(thumbs):
        x, y = index % columns * width, index // columns * height
        board.paste(mini, (x + (width - mini.width) // 2, y + 7))
        d.text((x + 10, y + 119), cid, fill="#182838")
    board.save(OUT / "CONTACT_SHEET_110.png", optimize=True)
    summary = {
        "catalog_total": len(CAT["components"]),
        "preview_images": len(records),
        "missing_preview_images": 110 - len(records),
        "near_flat_candidates": [x["id"] for x in records if x["near_flat_candidate"]],
        "report": records,
        "duplicate_screenshot_byte_counts": dict(Counter(x["bytes"] for x in records)),
        "claim": "Candidate screenshots from local HTML/CSS; manual review still required.",
    }
    (OUT / "REPORT_110.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("Visual QA 110 images; near-flat candidates:", summary["near_flat_candidates"])

    # Separately review all newly captured Ruixen screenshots, never silently
    # mix them into the Uiverse 110 baseline or claim visual approval.
    ruixen_records = []
    ruixen_thumbs = []
    for item in CAT["components"]:
        if item["source_site"] != "RUIXEN":
            continue
        cid = item["id"]
        rec = MAN["previews"][cid]
        if not rec["image_path"]:
            continue
        path = ROOT / rec["image_path"]
        with Image.open(path) as img:
            rgb = img.convert("RGB")
            std = round(statistics.fmean(ImageStat.Stat(rgb).stddev), 2)
            ruixen_records.append({
                "id": cid, "bytes": path.stat().st_size,
                "color_stddev": std, "near_flat_candidate": std < 4
            })
            copy = rgb.copy()
            copy.thumbnail((165, 110))
            ruixen_thumbs.append((cid, copy))
    if ruixen_thumbs:
        rows2 = (len(ruixen_thumbs) + columns - 1) // columns
        sheet2 = Image.new("RGB", (columns * width, rows2 * height), "#e8edf5")
        draw2 = ImageDraw.Draw(sheet2)
        for index, (cid, thumb) in enumerate(ruixen_thumbs):
            x, y = index % columns * width, index // columns * height
            sheet2.paste(thumb, (x + (width-thumb.width)//2, y+7))
            draw2.text((x+10, y+119), cid, fill="#182838")
        sheet2.save(OUT / "CONTACT_SHEET_RUIXEN.png", optimize=True)
    ruixen_summary = {
        "canonical_ruixen": 277,
        "captured": len(ruixen_records),
        "missing": 277 - len(ruixen_records),
        "near_flat_candidates": [x["id"] for x in ruixen_records if x["near_flat_candidate"]],
        "report": ruixen_records,
        "claim": "Visual QA evidence only, not human-reviewed or native UI verified."
    }
    (OUT / "REPORT_RUIXEN.json").write_text(
        json.dumps(ruixen_summary, indent=2) + "\n", encoding="utf-8")
    print("Ruixen visual evidence", len(ruixen_records), "/277;",
          "near-flat candidates:", len(ruixen_summary["near_flat_candidates"]))


    # Keep Forui evidence separate: screenshots are references, not app QA.
    forui = []
    for cid in ("FUI-001", "FUI-002"):
        record = MAN["previews"].get(cid)
        if not record or not record.get("image_path"):
            raise ValueError("Forui original preview missing: " + cid)
        with Image.open(ROOT / record["image_path"]) as img:
            rgb = img.convert("RGB")
            std = round(statistics.fmean(ImageStat.Stat(rgb).stddev), 2)
            thumb = rgb.copy()
            thumb.thumbnail((500, 260))
            forui.append((cid, thumb, {
                "id": cid, "size": list(rgb.size), "color_stddev": std,
                "near_flat_candidate": std < 4,
                "visual_qa": "UNREVIEWED",
            }))
    board3 = Image.new("RGB", (1050, 340), "#e8edf5")
    labeler = ImageDraw.Draw(board3)
    for index, (cid, img, metrics) in enumerate(forui):
        x = 25 + index * 525
        board3.paste(img, (x + (500-img.width)//2, 15))
        labeler.text((x+8, 300), cid + " · Flutter original demo (unreviewed)", fill="#182838")
    board3.save(OUT / "CONTACT_SHEET_FORUI.png", optimize=True)
    (OUT / "REPORT_FORUI.json").write_text(json.dumps({
        "catalog_total": len(CAT["components"]), "forui_original_previews": len(forui),
        "report": [item[2] for item in forui],
        "claim": "Source-pinned official Flutter demo screenshots, manual appearance and consumer acceptance not certified.",
    }, indent=2) + "\n", encoding="utf-8")
    print("Forui visual references", len(forui), "/2; visual QA UNREVIEWED")


if __name__ == "__main__":
    main()
