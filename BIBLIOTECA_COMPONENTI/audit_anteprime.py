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
        "catalog_total": 478,
        "preview_images": len(records),
        "missing_preview_images": 478 - len(records),
        "near_flat_candidates": [x["id"] for x in records if x["near_flat_candidate"]],
        "report": records,
        "duplicate_screenshot_byte_counts": dict(Counter(x["bytes"] for x in records)),
        "claim": "Candidate screenshots from local HTML/CSS; manual review still required.",
    }
    (OUT / "REPORT_110.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("Visual QA 110 images; near-flat candidates:", summary["near_flat_candidates"])


if __name__ == "__main__":
    main()
