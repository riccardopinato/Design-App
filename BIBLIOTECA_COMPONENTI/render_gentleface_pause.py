#!/usr/bin/env python3
"""Render the actual MIT source SVG of ICO-021, without synthetic art."""
from __future__ import annotations
import hashlib
from io import BytesIO
import json
from pathlib import Path
import cairosvg
from PIL import Image, ImageStat

ROOT=Path(__file__).resolve().parents[1]
ROOTDIR=ROOT/"BIBLIOTECA_COMPONENTI"
provenance=json.loads((ROOTDIR/"sorgenti/gentleface/PROVENIENZA.json").read_text(encoding="utf-8"))
c=provenance["entries"]["ICO-021"]
svg_path=ROOT/c["original_svg_path"]
raw=svg_path.read_bytes()
sha=lambda x:hashlib.sha256(x).hexdigest()
if sha(raw)!=c["original_svg_sha256"]:
    raise ValueError("Official MIT pause SVG sha differs from archived record")
data=cairosvg.svg2png(bytestring=raw,output_width=192,output_height=192)
with Image.open(BytesIO(data)) as im:
    glyph=im.convert("RGBA")
bbox=glyph.getchannel("A").getbbox()
if bbox is None or bbox[2]-bbox[0] < 8:
    raise ValueError("Actual pause icon has no visible shape")
canvas=Image.new("RGBA",(224,224),(245,246,249,255))
canvas.alpha_composite(glyph,(16,16))
out=BytesIO()
canvas.convert("RGB").save(out,format="PNG",optimize=True)
b=out.getvalue()
if len(b)<512 or sum(ImageStat.Stat(canvas.convert("RGB")).stddev)<1:
    raise ValueError("Original asset rendering insufficiently visible")
path=ROOT/"docs/assets/componenti/ICO-021.png"
if path.exists(): raise ValueError("Do not overwrite any existing preview")
path.write_bytes(b)
origins=ROOTDIR/"ANTEPRIME_ORIGINI_GENTLEFACE.json"
records=json.loads(origins.read_text(encoding="utf-8"))
if "ICO-021" in records["previews"]: raise ValueError("Origin entry already exists")
records["previews"]["ICO-021"]={
  "component_id":"ICO-021",
  "preview_path":"docs/assets/componenti/ICO-021.png",
  "preview_sha256":sha(b),
  "origin_url":c["source_page"],
  "origin_asset_url":c["original_svg_url"],
  "original_asset_sha256":sha(raw),
  "origin_provider":"gentleface.com",
  "source_license":"MIT",
  "capture_mode":"OFFICIAL_MIT_SVG_RENDERED",
  "pixel_transform":"Original official SVG rendered at 192 pixels, alpha composited on neutral 224px canvas",
  "source_availability":"ARCHIVED_MIT_SVG_HASHED",
  "visual_qa":"UNREVIEWED",
  "asset_rights":"MIT_REFERENCE_NO_CONSUMER_BUNDLE",
}
records["previews"]={k:records["previews"][k] for k in sorted(records["previews"])}
origins.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
report=ROOTDIR/"RECUPERO_ANTEPRIME_2026-11-19.json"
if report.exists():
    meta=json.loads(report.read_text(encoding="utf-8"))
    meta["new_gentleface"]=1
    meta["new_total"]=1
    meta["round_start_missing"]=130
    meta["estimated_remaining"]=129
    meta["cumulative_recovered_from_322_baseline"]=29
    meta["recovered_gentleface_ids"]=["ICO-021"]
    meta["gentleface_unresolved"]={}
    report.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("OFFICIAL_SVG_RENDERED ICO-021",sha(b),"bytes",len(b))
