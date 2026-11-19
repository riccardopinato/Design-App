#!/usr/bin/env python3
"""Screenshot unchanged MIT TSX using a local isolated React/Tailwind renderer.
Never label a reconstruction as an upstream official screenshot.
Fixture only supplies props and visual bounds; actual component code is pinned.
"""
from __future__ import annotations
import asyncio, hashlib, json, subprocess, time, urllib.request
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageStat
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"BIBLIOTECA_COMPONENTI"
RUNTIME=HERE/"ruixen_renderer"
PROV=HERE/"ANTEPRIME_ORIGINI.json"
CAT={x["id"]:x for x in json.loads((HERE/"CATALOGO.json").read_text(encoding="utf-8"))["components"]}
OUT=ROOT/"docs/assets/componenti"
COMMIT="f6b20860623fa39122ac2b5f0e5bd29a9eb10941"
ALLOWED=("grain-gradient-bg","grid-pattern","pulsating-button","shimmer-button")
sha=lambda b:hashlib.sha256(b).hexdigest()
def git_blob(b):
    return hashlib.sha1(b"blob "+str(len(b)).encode("ascii")+b"\0"+b).hexdigest()
async def main():
    existing=json.loads(PROV.read_text(encoding="utf-8"))
    entries=existing["previews"]
    server=subprocess.Popen(["npm","run","dev"],cwd=RUNTIME,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    try:
        for attempt in range(65):
            if server.poll() is not None: raise RuntimeError("Isolated original TSX server exited early")
            try:
                with urllib.request.urlopen("http://127.0.0.1:5181/",timeout=2) as resp:
                    if resp.status==200:break
            except Exception:
                await asyncio.sleep(.4)
        else:raise RuntimeError("Vite local component renderer did not start")
        async with async_playwright() as pw:
            browser=await pw.chromium.launch(headless=True,args=["--no-sandbox"])
            ctx=await browser.new_context(viewport={"width":1024,"height":720},color_scheme="light",reduced_motion="reduce")
            async def local_only(route):
                url=route.request.url
                if url.startswith("http://127.0.0.1:5181/"): await route.continue_()
                else: await route.abort()
            await ctx.route("**/*",local_only)
            made,blocked=[],{}
            for slug in ALLOWED:
                cid="RXN-"+slug
                item=CAT[cid]
                if item["source_site"]!="RUIXEN" or item["source_commit"]!=COMMIT:
                    raise ValueError("Inconsistent pinned React source: "+cid)
                source=(ROOT/item["archive_path"]).read_bytes()
                if git_blob(source)!=item["source_blob_sha"]:
                    raise ValueError("Ruixen original source SHA drift: "+cid)
                if cid in entries: continue
                page=await ctx.new_page()
                errors=[]
                page.on("pageerror",lambda e:errors.append(str(e)))
                try:
                    res=await page.goto(f"http://127.0.0.1:5181/?component={slug}",wait_until="networkidle",timeout=25000)
                    if not res or res.status!=200 or errors:
                        raise ValueError("React runtime failure: "+";".join(errors[:2]))
                    elem=page.locator("#component-root")
                    await elem.wait_for(state="visible",timeout=10000)
                    await page.wait_for_timeout(600)
                    if await elem.get_attribute("data-original-slug")!=slug:
                        raise ValueError("Wrong source fixture")
                    raw=await elem.screenshot(animations="disabled",timeout=14000)
                    with Image.open(BytesIO(raw)) as source_img:
                        im=source_img.convert("RGB")
                        if min(im.size)<150:raise ValueError("Preview bounds too small")
                        if sum(ImageStat.Stat(im).stddev)<10:
                            raise ValueError("Near-flat image; cannot establish faithful distinct component")
                        im.thumbnail((640,440),Image.Resampling.LANCZOS)
                        buf=BytesIO()
                        im.save(buf,"PNG",optimize=True)
                    png=buf.getvalue()
                    if len(png)<700:raise ValueError("Generated screenshot unexpectedly small")
                    path=OUT/(cid+".png")
                    if path.exists():raise ValueError("Do not overwrite existing original preview "+cid)
                    path.write_bytes(png)
                    entries[cid]={
                        "component_id":cid,"preview_path":f"docs/assets/componenti/{cid}.png",
                        "preview_sha256":sha(png),"origin_url":item["source_url"],
                        "origin_repo":"ruixenui/ruixen.com","origin_source_commit":COMMIT,
                        "source_blob_sha":item["source_blob_sha"],
                        "capture_mode":"PINNED_ORIGINAL_TSX_ISOLATED_REACT_RENDER",
                        "local_fixture_path":"BIBLIOTECA_COMPONENTI/ruixen_renderer/src/main.tsx",
                        "local_renderer_package_sha256":sha((RUNTIME/"package.json").read_bytes()),
                        "visual_qa":"UNREVIEWED",
                        "source_scope":"Pinned original TSX executed in isolated React runtime. Example props and layout are local fixtures, NOT official upstream screenshot.",
                        "asset_rights":"REFERENCE_ONLY_NOT_ADMITTED_TO_CONSUMER"
                    }
                    made.append(cid)
                    print("TSX_SCREENSHOT_OK",cid,len(png),sha(png))
                except Exception as exc:
                    blocked[cid]=str(exc)[:320]
                    print("TSX_SCREENSHOT_BLOCKED",cid,blocked[cid])
                finally:await page.close()
            await ctx.close();await browser.close()
        existing["previews"]={k:entries[k] for k in sorted(entries)}
        PROV.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        (HERE/"RU_TSX_RENDER_REPORT.json").write_text(json.dumps({
           "renderer":"React/Vite isolated demo with unchanged pinned original TSX","requested":list(ALLOWED),
           "captured":made,"blocked":blocked,"source_revision":COMMIT,
           "status":"IMAGE_UNREVIEWED_NOT_OFFICIAL_UPSTREAM_CAPTURE",
        },indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        return 0
    finally:
        server.terminate()
        try:server.wait(timeout=8)
        except subprocess.TimeoutExpired:server.kill()
if __name__=="__main__":
    raise SystemExit(asyncio.run(main()))
