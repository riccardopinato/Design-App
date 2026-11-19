#!/usr/bin/env python3
"""Read-only reconnaissance: locate real Ruixen component demos for unresolved UID.
Reports DOM structure and status only; does not claim or save any screenshots.
"""
import asyncio
import json
from playwright.async_api import async_playwright

CANDIDATES=[
    "animated-beam","animated-gradient-text","animated-grid-pattern",
    "animated-shiny-text","animated-subscribe-button","blur-fade","box-reveal",
    "arc-timeline","code-comparison","behavioral-history-select",
    "animated-link","floating-cards-hero"
]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(headless=True,args=["--no-sandbox"])
        ctx=await b.new_context(viewport={"width":1100,"height":760},reduced_motion="reduce")
        sem=asyncio.Semaphore(5)
        async def inspect(slug):
            async with sem:
                pg=await ctx.new_page()
                try:
                    for route in (f"/docs/components/{slug}",f"/docs/sections/{slug}",f"/preview/{slug}"):
                        url="https://ruixen.com"+route
                        try:
                            response=await pg.goto(url,wait_until="domcontentloaded",timeout=13000)
                            await pg.wait_for_timeout(800)
                            details=await pg.evaluate("""() => ({
                                title: document.title,
                                headings: Array.from(document.querySelectorAll('main h1,main h2')).map(x=>x.textContent.trim()).slice(0,6),
                                iframeCount: document.querySelectorAll('main iframe').length,
                                mainText: (document.querySelector('main')?.innerText||'').slice(0,300),
                                mainChildren: Array.from(document.querySelector('main')?.children||[]).slice(0,8).map(x=>({tag:x.tagName,class:x.className,tagPreview:x.outerHTML.slice(0,180)})),
                                liveButtons: Array.from(document.querySelectorAll('main button')).map(x=>x.innerText.trim()).filter(Boolean).slice(0,16),
                                components: Array.from(document.querySelectorAll('[data-slot], [data-testid]')).slice(0,10).map(x=>({tag:x.tagName,slot:x.getAttribute('data-slot'),testid:x.getAttribute('data-testid')}))
                            })""")
                            print("RU_PROBE",json.dumps({"slug":slug,"route":route,"status":response.status if response else None,**details},ensure_ascii=False))
                        except Exception as exc:
                            print("RU_PROBE_ERR",json.dumps({"slug":slug,"route":route,"error":str(exc)[:170]}))
                finally:
                    await pg.close()
        await asyncio.gather(*(inspect(s) for s in CANDIDATES))
        await ctx.close();await b.close()
if __name__=="__main__":
    asyncio.run(main())
