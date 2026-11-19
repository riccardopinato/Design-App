#!/usr/bin/env python3
"""Capture exact live component previews for FCL reference-only catalog entries.

Only an actual official demo iframe/Flutter runtime is a preview. Never crop a
documentation heading, generate stock art or treat a public demo as licensed Dart.
"""
from __future__ import annotations
import asyncio
from collections import Counter
import hashlib
from io import BytesIO
import json
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageStat
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"BIBLIOTECA_COMPONENTI"
IMG=ROOT/"docs/assets/componenti"
SRC=HERE/"CATALOGO.json"
PREVIEW=HERE/"ANTEPRIME.json"
PROVENANCE=HERE/"ANTEPRIME_ORIGINI_SECONDARIE.json"
REPORT=HERE/"FCL_CAPTURE_REPORT.json"
sha=lambda b:hashlib.sha256(b).hexdigest()

def valid_render(raw:bytes):
    if not raw.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Browser did not generate PNG screenshot")
    with Image.open(BytesIO(raw)) as im:
        picture=im.convert("RGB")
        if min(picture.size)<140: raise ValueError("Rendered demo too small")
        std=sum(ImageStat.Stat(picture).stddev)
        if std < 10: raise ValueError("Near-blank/flat demo viewport")
        picture.thumbnail((640,500),Image.Resampling.LANCZOS)
        buff=BytesIO();picture.save(buff,format="PNG",optimize=True)
    return buff.getvalue(),round(std,2)

async def main():
    cat=json.loads(SRC.read_text(encoding="utf-8"))["components"]
    pv=json.loads(PREVIEW.read_text(encoding="utf-8"))["previews"]
    originals=[x for x in cat if x["source_site"]=="FLUTTER_COMPONENT_LIBRARY" and not pv[x["id"]].get("image_path")]
    assert len(originals)<=15
    entries=(json.loads(PROVENANCE.read_text(encoding="utf-8")).get("previews",{})
        if PROVENANCE.exists() else {})
    captured=[]
    blocked={}
    diagnostics={}
    sem=asyncio.Semaphore(3)
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
        context=await browser.new_context(viewport={"width":1170,"height":900}, color_scheme="light",
            reduced_motion="reduce",service_workers="block")
        async def work(c):
            async with sem:
                cid,url=c["id"],c.get("source_url")
                if not url or urlparse(url).netloc!="fluttercomponentlibrary.com":
                    blocked[cid]="NO_VERIFIED_OFFICIAL_SOURCE_PAGE"
                    return
                page=await context.new_page()
                try:
                    resp=await page.goto(url,wait_until="domcontentloaded",timeout=23000)
                    if not resp or resp.status>=400:
                        raise ValueError(f"OFFICIAL_PAGE_HTTP_{resp.status if resp else 'NONE'}")
                    await page.wait_for_timeout(1000)
                    title=await page.title()
                    frames=page.locator("iframe")
                    count=await frames.count()
                    anchors=await page.locator('a[href]').evaluate_all("""els=>els
                        .filter(a=>/open in new tab|live demo/i.test(a.textContent||''))
                        .map(a=>a.href).slice(0,6)""")
                    diagnostics[cid]={
                        "requested_url":url,"final_url":page.url,
                        "http_status":resp.status,"title":title,
                        "iframe_count":count,"demo_links":anchors,
                        "source_code_archived":False,
                        "source_license_verified":False,
                    }
                    if count == 0:
                        raise ValueError("NO_OFFICIAL_DEMO_IFRAME: "+str(anchors[:2])+
                                         "; final_url="+page.url+"; page_title="+title)
                    best=None
                    for k in range(min(5,count)):
                        frame=frames.nth(k)
                        rect=await frame.bounding_box()
                        if rect and rect["width"] >= 210 and rect["height"] >= 180:
                            best=(frame,rect)
                            break
                    if best is None:
                        raise ValueError("NO_VISIBLE_COMPONENT_SPECIFIC_FRAME")
                    frame,rect=best
                    iframe_src=await frame.get_attribute("src") or ""
                    if not iframe_src or iframe_src.startswith("javascript:"):
                        raise ValueError("NO_TRUSTED_DEMO_FRAME_SOURCE")
                    await frame.scroll_into_view_if_needed(timeout=13000)
                    await page.wait_for_timeout(3300)
                    frame_el=await frame.element_handle()
                    if frame_el:
                        inside=await frame_el.content_frame()
                        if inside is not None:
                            for delay in (1100,1700,2500):
                                if await inside.locator("flt-glass-pane,flt-scene-host,canvas").count()>0:
                                    break
                                await page.wait_for_timeout(delay)
                    # This known route displays the library homepage despite a visible
                    # iframe. Keep its false-positive rejection until the exact
                    # widget can be demonstrated, not merely a generic shell.
                    if cid == "FCL-006":
                        raise ValueError("VISUAL_QA_REJECTED_WRONG_COMPONENT: the Book Shelf demo route resolves to catalog homepage")
                    raw=await frame.screenshot(animations="disabled",timeout=20000)
                    png,std=valid_render(raw)
                    if "404" in title.lower():
                        raise ValueError("404 page is not component")
                    dest=IMG/(cid+".png")
                    if dest.exists():raise ValueError("ALREADY_EXISTS_REVIEW_BEFORE_OVERWRITE")
                    dest.write_bytes(png)
                    entries[cid]={
                        "component_id":cid,
                        "source_provider":"FLUTTER_COMPONENT_LIBRARY",
                        "source_reference_url":url,
                        "origin_demo_url":iframe_src,
                        "preview_path":"docs/assets/componenti/"+cid+".png",
                        "preview_sha256":sha(png),
                        "capture_mode":"OFFICIAL_LIVE_DEMO_IFRAME",
                        "original_archive_path":None,
                        "license_status":"NOT_VERIFIED",
                        "reuse_scope":"DOCUMENTARY_REFERENCE_ONLY",
                        "visual_qa":"UNREVIEWED",
                        "image_variance":std,
                        "note":"Screenshot of isolated public live demo; no source/Dart or asset redistribution rights asserted",
                    }
                    captured.append(cid)
                    print("FCL_CAPTURE_OK",cid,"bytes",len(png),"std",std,"demo",iframe_src)
                except Exception as exc:
                    blocked[cid]=str(exc)[:450]
                    print("FCL_CAPTURE_BLOCKED",cid,str(exc)[:220])
                finally:
                    await page.close()
        await asyncio.gather(*(work(c) for c in originals))
        await context.close()
        await browser.close()
    PROVENANCE.write_text(json.dumps({"schema_version":1,"previews":dict(sorted(entries.items()))},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({
        "scope":"Original official FCL component demo preview; reference-only",
        "requested":len(originals),"captured":sorted(captured),"blocked":blocked,
        "diagnostics":diagnostics,
        "rule":"A missing image remains missing; no fake or general page screenshots",
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("FCL_CAPTURE_TOTAL",len(captured),"BLOCKED",len(blocked))
    return 0

if __name__=="__main__":
    raise SystemExit(asyncio.run(main()))
