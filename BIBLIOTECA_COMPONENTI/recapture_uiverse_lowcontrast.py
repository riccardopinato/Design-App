#!/usr/bin/env python3
"""Targeted second-pass Uiverse CSS preview captures: no source alterations.

The initial static screenshot used animations=disabled, forcing some infinite
CSS loaders into an invisible keyframe; pale-on-pale items also disappear.
This pass samples actual running CSS animations on an isolated contrasting
fixture and replaces an archived PNG ONLY for measurable visual improvement.
All replacements remain UNREVIEWED. Never draw substitute component graphics.
"""
from __future__ import annotations
import asyncio, hashlib, io, json
from pathlib import Path
from PIL import Image, ImageStat
from playwright.async_api import async_playwright
from render_uiverse_previews import source_html

ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/"BIBLIOTECA_COMPONENTI/CATALOGO.json").read_text())["components"]
DEST=ROOT/"docs/assets/componenti"
REPORT=ROOT/"BIBLIOTECA_COMPONENTI/UIVERSE_LOWCONTRAST_RECOVERY.json"
# Candidate IDs are from objective near-flat QA at the 459 PNG checkpoint.
IDS=["UIV-005","UIV-011","UIV-033","UIV-041","UIV-042","UIV-044",
     "UIV-050","UIV-061","UIV-062","UIV-065","UIV-066",
     "UIV-088","UIV-089","UIV-094","UIV-098"]
# The archived source uses white text, borders or glows. Contrast belongs to
# the DEMO BACKDROP, not to the archived component styles.
DARK={"UIV-033","UIV-041","UIV-042","UIV-061","UIV-066","UIV-089","UIV-094"}
FULL={"UIV-050","UIV-061","UIV-098"}
def stats(raw):
    with Image.open(io.BytesIO(raw)) as im:
        rgb=im.convert("RGB")
        if rgb.size!=(420,280): raise ValueError("SCREENSHOT_DIMENSIONS_CHANGED")
        avg=round(sum(ImageStat.Stat(rgb).stddev)/3,3)
        return avg,im.copy()
def digest(b):return hashlib.sha256(b).hexdigest()

async def main():
    catalog={c["id"]:c for c in CAT}
    cases={}
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
        context=await browser.new_context(viewport={"width":420,"height":280},
            device_scale_factor=1,color_scheme="light",
            reduced_motion="no-preference",java_script_enabled=False)
        await context.route("**/*",lambda route: route.abort())
        page=await context.new_page()
        try:
            for cid in IDS:
                c=catalog[cid]
                assert c["source_site"]=="UIVERSE" and c["archive_state"]=="ARCHIVED_SOURCE"
                html=source_html(c)
                if cid in DARK:
                    html=html.replace("</head>","<style>html,body{background:#182334!important;color:#f5f5f5!important}</style></head>")
                if cid in FULL:
                    html=html.replace("</head>","<style>#preview{width:380px;height:240px;min-height:240px;overflow:visible}</style></head>")
                await page.set_content(html,wait_until="domcontentloaded",timeout=15000)
                path=DEST/(cid+".png")
                previous=path.read_bytes()
                oldstd,_=stats(previous)
                best=None
                beststd=-1.
                samples=[]
                # Take real frames at reproducible cumulative offsets. Never
                # switch off infinite animations (that hid loaders at opacity 0).
                for delay in (420,500,450):
                    await page.wait_for_timeout(delay)
                    raw=await page.screenshot(full_page=False,animations="allow",timeout=12000)
                    std,_=stats(raw)
                    samples.append(std)
                    if std>beststd:
                        beststd=std;best=raw
                accepted=beststd>=4.5 and beststd>oldstd+1.5
                if accepted:
                    assert best and best.startswith(bytes([137,80,78,71])),"INVALID_RENDERED_IMAGE"
                    path.write_bytes(best)
                cases[cid]={
                    "source_url":c["source_url"],
                    "archived_source_path":c["archive_path"],
                    "archived_source_blob_sha":c["source_blob_sha"],
                    "old_sha256":digest(previous),
                    "current_sha256":digest(best) if accepted else digest(previous),
                    "old_stddev":oldstd,"candidate_frame_stddev":samples,
                    "best_stddev":beststd,"replaced":accepted,
                    "fixture_backdrop":"DARK" if cid in DARK else "NEUTRAL",
                    "fixture_size":"380x240" if cid in FULL else "CONTENT_BASED",
                    "capture_mode":"ORIGINAL_HTML_CSS_RUNNING_ANIMATION",
                    "visual_qa":"UNREVIEWED",
                    "claim":"Real archived source rendered in browser; no original code or external asset changed"
                }
                print("UVERSE_QA",cid,"old",oldstd,"new",beststd,"accepted",accepted)
        finally:
            await page.close()
            await context.close()
            await browser.close()
    REPORT.write_text(json.dumps({
        "as_of":"2026-11-19",
        "original_count":110,
        "candidates":len(IDS),
        "replaced":sum(v["replaced"] for v in cases.values()),
        "still_needs_source_visual_acceptance":110,
        "fixture_rule":"Only output real archived HTML/CSS. The wrapper can change contrast/size; never source styles.",
        "cases":cases
    },ensure_ascii=False,indent=2)+chr(10),encoding="utf-8")
    print("UVERSE_TARGETED_PREVIEW_RECOVERY",sum(v["replaced"] for v in cases.values()),"/",len(IDS))
if __name__=="__main__":
    asyncio.run(main())
