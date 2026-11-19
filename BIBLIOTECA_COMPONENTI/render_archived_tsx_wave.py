#!/usr/bin/env python3
"""Batch render every unresolved, MIT-archived React TSX, per UID and SHA.

The isolated Vite resolver pins upstream hooks and disables cross-UID error
broadcasting; missing genuine dependencies still fail closed per UID.

Source provenance is exact. A generic fixture is not a fidelity claim: visual
QA remains UNREVIEWED, and imports/visuals that fail are logged rather than
filled with fabricated images. Existing previews and originals are immutable.
"""
from __future__ import annotations
import asyncio,hashlib,json,re,subprocess
from collections import Counter
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from PIL import Image,ImageStat
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"BIBLIOTECA_COMPONENTI"
RUNTIME=HERE/"ruixen_renderer"
OUT=ROOT/"docs/assets/componenti"
CAT=json.loads((HERE/"CATALOGO.json").read_text(encoding="utf-8"))["components"]
PV=json.loads((HERE/"ANTEPRIME.json").read_text(encoding="utf-8"))["previews"]
RU=HERE/"ANTEPRIME_ORIGINI.json"
SEC=HERE/"ANTEPRIME_ORIGINI_SECONDARIE.json"
REPORT=HERE/"RENDER_ARCHIVED_TSX_BATCH_REPORT.json"
PIN="f6b20860623fa39122ac2b5f0e5bd29a9eb10941"
sha=lambda x:hashlib.sha256(x).hexdigest()
gitsha=lambda b:hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

async def main():
    candidates=[c for c in CAT if not PV[c["id"]].get("image_path") and (
        c["source_site"]=="RUIXEN" or c["source_site"].startswith("DEVLIBRARIES_")
    )]
    assert len(candidates)<=103, "unexpected pending archived sources explosion"
    ru_data=json.loads(RU.read_text(encoding="utf-8"))
    sec_data=json.loads(SEC.read_text(encoding="utf-8")) if SEC.exists() else {"schema_version":1,"previews":{}}
    ru=ru_data["previews"];sec=sec_data["previews"]
    failed={};made=[];skipped={};cross_uid_overlays={}
    active=[]
    for c in candidates:
        cid=c["id"]
        source=c.get("archive_path")
        if c.get("archive_state")!="ARCHIVED_SOURCE" or not source:
            skipped[cid]="BLOCKED_NO_ARCHIVED_SOURCE"
            continue
        file=ROOT/source
        if not file.is_file() or file.suffix!=".tsx":
            skipped[cid]="BLOCKED_MISSING_ARCHIVED_TSX"
            continue
        if gitsha(file.read_bytes()) != c.get("source_blob_sha"):
            skipped[cid]="BLOCKED_ARCHIVED_SOURCE_BLOB_MISMATCH"
            continue
        if c["source_site"]=="RUIXEN" and c.get("source_commit")!=PIN:
            skipped[cid]="BLOCKED_RUIXEN_SOURCE_PIN_MISMATCH"
            continue
        if not c["license_status"].startswith(("MIT_","MIT_SOURCE")):
            skipped[cid]="BLOCKED_NO_ARCHIVED_SOURCE_LICENSE"
            continue
        active.append(c)
    # Additional upstream MIT hook is archived byte-for-byte. Do not silently
    # satisfy an original dependency with a fabricated stub.
    amicro_hook = RUNTIME/"vendor/amicro/useLoopFlg.ts"
    if not amicro_hook.is_file() or gitsha(amicro_hook.read_bytes()) != "8738725f506363ed5cb088a70a5ba93f4be87c38":
        raise ValueError("PINNED_AMICRO_HOOK_MISSING_OR_MUTATED")
    log=open("/tmp/design_app_full_source_render.log","w",encoding="utf-8")
    server=subprocess.Popen(["npm","run","dev"],cwd=RUNTIME,stdout=log,stderr=subprocess.STDOUT)
    try:
        for _ in range(100):
            if server.poll() is not None: raise RuntimeError("Vite source renderer stopped unexpectedly")
            try:
                with urlopen("http://127.0.0.1:5181/batch.html",timeout=2) as check:
                    if check.status==200:break
            except Exception:
                await asyncio.sleep(.4)
        else: raise RuntimeError("Vite source renderer unavailable")
        async with async_playwright() as p:
            browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
            ctx=await browser.new_context(viewport={"width":1024,"height":650},reduced_motion="reduce",color_scheme="light")
            async def local_only(route):
                url=route.request.url
                if url.startswith("http://127.0.0.1:5181/"): await route.continue_()
                else:await route.abort()
            await ctx.route("**/*",local_only)
            semaphore=asyncio.Semaphore(5)
            def assert_server_alive(stage):
                if server.poll() is not None:
                    try:
                        with open("/tmp/design_app_full_source_render.log",encoding="utf-8",errors="replace") as lf:
                            tail=lf.read()[-4800:]
                    except OSError:
                        tail="LOG_UNAVAILABLE"
                    raise RuntimeError("VITE_RUNTIME_TERMINATED stage="+stage+
                                       " code="+str(server.returncode)+"\n"+tail)
            async def work(c):
                cid=c["id"]
                async with semaphore:
                    page=await ctx.new_page()
                    await page.add_init_script("""window.__sourceErrorStacks=[];
                    window.addEventListener('error', e => {
                      window.__sourceErrorStacks.push(String(e.error?.stack || e.message));
                    });
                    window.addEventListener('unhandledrejection', e => {
                      window.__sourceErrorStacks.push(String(e.reason?.stack || e.reason));
                    });""")
                    errors=[]; console_errors=[]; http_errors=[]; request_errors=[]
                    page.on("pageerror",lambda e:errors.append(str(e)[:2200]))
                    page.on("console",lambda m:console_errors.append(m.text[:230]) if m.type=="error" else None)
                    page.on("response",lambda res:http_errors.append(str(res.status)+" "+res.url[-150:]) if res.status>=400 else None)
                    page.on("requestfailed",lambda req:request_errors.append(req.url[-170:]))
                    try:
                        assert_server_alive("before_navigation_"+cid)
                        await page.goto("http://127.0.0.1:5181/batch.html?cid="+cid,
                            wait_until="domcontentloaded",timeout=19000)
                        target=page.locator("#component-root")
                        await page.wait_for_function(
                            "()=>['ready','failed'].includes(document.getElementById('component-root')?.dataset.captureStatus||'')",
                            timeout=23000)
                        state=await target.get_attribute("data-capture-status")
                        if state!="ready":
                            why=await target.get_attribute("data-source-error")
                            details={"console":console_errors[:3],"http":http_errors[:3],"requests":request_errors[:3]}
                            raise ValueError("ORIGINAL_TSX_IMPORT_OR_RENDER_FAILED "+str(why)+" "+json.dumps(details,ensure_ascii=False))
                        if cid=="RXN-video-text":
                            # Procedural ORIGINAL demo video frames, not an
                            # external media asset. Feed HTMLVideoElement's real
                            # srcObject, retaining the unmodified VideoText mask.
                            await page.evaluate("""async () => {
                              const v = document.querySelector('#component-root video');
                              if (!v) throw Error('ORIGINAL_VIDEO_ELEMENT_MISSING');
                              const canvas = document.createElement('canvas');
                              canvas.width=640; canvas.height=360;
                              const g=canvas.getContext('2d');
                              if (!g || !canvas.captureStream)
                                throw Error('LOCAL_CANVAS_MEDIA_STREAM_UNSUPPORTED');
                              let frame=0;
                              const paint=()=>{
                                const w=640,h=360,t=frame++/12;
                                const grad=g.createLinearGradient(0,0,w,h);
                                grad.addColorStop(0,'#1d4ed8');
                                grad.addColorStop(.45,'#f97316');
                                grad.addColorStop(1,'#8b5cf6');
                                g.fillStyle=grad;g.fillRect(0,0,w,h);
                                for(let i=0;i<8;i++){
                                  const x=((i*92+t*70)%750)-55;
                                  g.fillStyle=i%2?'#fef08a':'#22d3ee';
                                  g.beginPath();g.arc(x,90+i*24,24+i*2,0,Math.PI*2);g.fill();
                                }
                                requestAnimationFrame(paint);
                              };
                              paint();
                              v.srcObject=canvas.captureStream(12);
                              v.muted=true;
                              await v.play();
                            }""")
                            await page.wait_for_function("""() => {
                              const v=document.querySelector('#component-root video');
                              return v && v.readyState>=2 && v.videoWidth>0;
                            }""",timeout=10000)
                        # Cursor-only originals have no visible output until
                        # a real pointer event. Exercise the original runtime.
                        if cid in {"AMX-002","RXN-smooth-cursor"}:
                            await page.mouse.move(440,270)
                            await page.wait_for_timeout(420)
                            await page.mouse.move(505,295)
                        await page.wait_for_timeout(950)
                        if errors:
                            stacks=await page.evaluate("() => (window.__sourceErrorStacks||[]).slice(0,2)")
                            raise ValueError("SOURCE_JS_EXCEPTION "+str(errors[:2])+
                                             " BROWSER_STACK "+json.dumps(stacks,ensure_ascii=False))
                        # Vite can broadcast an error from an unrelated UID into
                        # the same browser context. Reject errors in THIS source
                        # or renderer; explicitly log and remove unrelated overlays
                        # before capture. Never screenshot a Vite error UI.
                        async def clear_cross_uid_overlays():
                            count=await page.locator("vite-error-overlay").count()
                            for _ in range(count):
                                overlay=page.locator("vite-error-overlay").first
                                detail=await overlay.evaluate(
                                    "(el)=>el.shadowRoot?.textContent?.slice(0,550) || el.textContent?.slice(0,550) || 'vite error'")
                                basename=Path(c["archive_path"]).name
                                if basename in detail or "batch_main.tsx" in detail or "vite.config.ts" in detail:
                                    raise ValueError("VITE_SOURCE_OR_RENDERER_COMPILATION_OVERLAY "+str(detail)[:380])
                                cross_uid_overlays.setdefault(cid,[]).append(str(detail)[:260])
                                await overlay.evaluate("(el)=>el.remove()")
                        await clear_cross_uid_overlays()
                        actual_source=await target.get_attribute("data-source-path")
                        if not actual_source or not actual_source.endswith("/"+Path(c["archive_path"]).name):
                            raise ValueError("COMPONENT_SOURCE_PATH_DID_NOT_MATCH_ARCHIVE actual="+repr(actual_source)+" expected="+repr(c["archive_path"]))
                        n=await target.locator("*").count()
                        # Check the original implementation, not merely the
                        # surrounding fixture, before accepting visual examples.
                        if cid=="RXN-video-text":
                            proof=await target.locator("video").first.evaluate("""(v)=>{
                                const mask=getComputedStyle(v.parentElement).maskImage;
                                return v.readyState>=2 && v.videoWidth>0 &&
                                    v.srcObject instanceof MediaStream &&
                                    !!mask && mask!=='none';
                            }""")
                            if not proof:
                                raise ValueError("VIDEO_TEXT_LIVE_SOURCE_OR_MASK_NOT_RENDERED")
                        if cid=="RXN-pixel-image":
                            count=await target.locator('img[alt^="Pixel image piece"]').count()
                            valid=await target.locator('img[alt^="Pixel image piece"]').first.evaluate(
                                "(img)=>img.complete && img.naturalWidth>0") if count else False
                            if count!=24 or not valid:
                                raise ValueError("PIXEL_SOURCE_IMAGE_GRID_NOT_REAL_OR_UNLOADED")
                        if cid=="RXN-progressive-blur":
                            layers=await target.locator(".gradient-blur > div").count()
                            if layers!=8:
                                raise ValueError("PROGRESSIVE_BLUR_ORIGINAL_LAYERS_NOT_RENDERED")
                        # A valid source may render ONE span/canvas/input directly.
                        # This is a DOM presence check, not an arbitrary child count.
                        if n<1:raise ValueError("NO_RENDERED_COMPONENT_ELEMENT")
                        if "SOURCE_MODULE_FAILED" in (await target.inner_text()):
                            raise ValueError("SOURCE_MODULE_FAILED_MESSAGE")
                        # Date/time scrub controls occupy only a few short text
                        # lines. Capture their actual interactive UI at a
                        # tighter frame; do not lower the anti-blank QA threshold.
                        if cid=="RXN-scrub-datetime":
                            await target.evaluate("""el => {
                                el.style.width='410px';
                                el.style.height='220px';
                                el.style.background='#111827';
                            }""")
                        if cid=="RXN-scrub-datetime":
                            # Focus on the two actual interactive rows, not
                            # the empty space around the text control.
                            rows=target.locator("div.flex.items-baseline")
                            if await rows.count()!=2:
                                raise ValueError("SCRUB_DATETIME_SOURCE_ROWS_NOT_FOUND")
                            boxes=[await rows.nth(i).bounding_box() for i in range(2)]
                            if any(not b for b in boxes):
                                raise ValueError("SCRUB_DATETIME_ROW_GEOMETRY_UNAVAILABLE")
                            x1=min(b["x"] for b in boxes)-16
                            y1=min(b["y"] for b in boxes)-16
                            x2=max(b["x"]+b["width"] for b in boxes)+16
                            y2=max(b["y"]+b["height"] for b in boxes)+16
                            raw=await page.screenshot(clip={"x":max(0,x1),"y":max(0,y1),
                                "width":x2-max(0,x1),"height":y2-max(0,y1)},
                                animations="disabled",timeout=14000)
                        else:
                            raw=await target.screenshot(animations="disabled",timeout=14000)
                        # A late unrelated overlay cannot invalidate the tested UID;
                        # late errors for the requested source still fail closed.
                        await clear_cross_uid_overlays()
                        with Image.open(BytesIO(raw)) as image:
                            canvas=image.convert("RGB")
                            variance=sum(ImageStat.Stat(canvas).stddev)
                            if variance < 9:
                                raise ValueError("NEAR_BLANK_UNVERIFIED_COMPONENT")
                            canvas.thumbnail((640,430),Image.Resampling.LANCZOS)
                            buf=BytesIO();canvas.save(buf,"PNG",optimize=True)
                        png=buf.getvalue()
                        if len(png)<800:raise ValueError("PNG_TOO_SMALL")
                        dest=OUT/(cid+".png")
                        if dest.exists():raise ValueError("IMAGE_ALREADY_EXISTS")
                        dest.write_bytes(png)
                        base={
                            "component_id":cid,
                            "preview_path":"docs/assets/componenti/"+cid+".png",
                            "preview_sha256":sha(png),
                            "origin_url":c.get("source_url"),
                            "source_blob_sha":c.get("source_blob_sha"),
                            "capture_mode":"PINNED_ORIGINAL_TSX_ISOLATED_REACT_RENDER",
                            "local_fixture_path":"BIBLIOTECA_COMPONENTI/ruixen_renderer/src/batch_main.tsx",
                            "local_renderer_package_sha256":sha((RUNTIME/"package.json").read_bytes()),
                            "visual_qa":"UNREVIEWED",
                            "source_scope":("Original immutable VideoText TSX with generated local canvas MediaStream; NOT an upstream example or licensed footage"
                                            if cid=="RXN-video-text" else
                                            "Original immutable archived TSX executed in isolated React with demo props, not official upstream screenshot"),
                            "asset_rights":"REFERENCE_ONLY_NOT_ADMITTED_TO_CONSUMER",
                        }
                        if c["source_site"]=="RUIXEN":
                            ru[cid]={**base,"origin_repo":"ruixenui/ruixen.com","origin_source_commit":PIN}
                        else:
                            sec[cid]={
                                **base,
                                "source_provider":c["source_site"],
                                "source_reference_url":c.get("source_url"),
                                "original_archive_path":c.get("archive_path"),
                                "capture_mode":"ARCHIVED_ORIGINAL_TSX_ISOLATED_RENDER",
                                "reuse_scope":"DOCUMENTARY_REFERENCE_ONLY",
                                "note":"Source-git-blob-matched TSX executed; client runtime visual fidelity not certified"
                            }
                        made.append(cid)
                        print("TSX_WAVE_OK",cid,"bytes",len(png),"variance",round(variance,1))
                    except Exception as exc:
                        if "ERR_CONNECTION_REFUSED" in str(exc):
                            assert_server_alive("connection_refused_"+cid)
                            raise RuntimeError("VITE_INFRASTRUCTURE_CONNECTION_REFUSED "+cid) from exc
                        failed[cid]=str(exc)[:2500]
                        print("TSX_WAVE_BLOCKED",cid,failed[cid][:180])
                    finally:
                        await page.close()
            await asyncio.gather(*(work(c) for c in active))
            await ctx.close();await browser.close()
    finally:
        server.terminate()
        try:server.wait(timeout=8)
        except subprocess.TimeoutExpired:server.kill()
        log.close()
    ru_data["previews"]=dict(sorted(ru.items()))
    sec_data["previews"]=dict(sorted(sec.items()))
    RU.write_text(json.dumps(ru_data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    SEC.write_text(json.dumps(sec_data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    totals=Counter(c["source_site"] for c in active)
    REPORT.write_text(json.dumps({
        "original_pending_count":len(candidates),"source_eligible":len(active),
        "captured":sorted(made),"failed":failed,"blocked_before_run":skipped,
        "unrelated_vite_overlays":cross_uid_overlays,
        "eligible_by_source":totals,"source_integrity":"Exact source blob SHA checked before execution",
        "status":"SOURCE_PREVIEW_UNREVIEWED",
        "statement":"A preview is considered captured ONLY with a physical nonblank PNG and exact source provenance. No source code altered."
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("TSX_TOTAL",len(made),"OF",len(candidates),"NEW_BY_SOURCE",dict(Counter(c["source_site"] for c in active if c["id"] in made)))
    return 0

if __name__=="__main__":
    raise SystemExit(asyncio.run(main()))
