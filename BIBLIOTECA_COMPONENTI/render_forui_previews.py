#!/usr/bin/env python3
"""Capture documented *real* Forui Flutter demo iframes (not site chrome).

The package's pinned MIT Dart sources are in BIBLIOTECA_COMPONENTI/sorgenti/forui.
Live docs preview is unpinned and remains UNREVIEWED until human QA.
"""
import asyncio
import hashlib
from io import BytesIO
import json
from pathlib import Path
from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "docs/assets/componenti"
PROVENANCE = ROOT / "BIBLIOTECA_COMPONENTI/ANTEPRIME_ORIGINI_FORUI.json"
SHA = "5dbf97c926a53fcfe3436db1be6262ac40961db5"
PAGES = {
    "FUI-001": "https://forui.dev/docs/widgets/form/button",
    "FUI-002": "https://forui.dev/docs/widgets/form/text-form-field",
}


async def main():
    from playwright.async_api import async_playwright
    entries, failed = {}, []
    DIR.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1240, "height": 850},
                                        reduced_motion="reduce", color_scheme="light")
        for cid, url in PAGES.items():
            page = await ctx.new_page()
            try:
                res = await page.goto(url, wait_until="domcontentloaded", timeout=38000)
                if not res or res.status >= 400:
                    raise ValueError("source docs page unavailable")
                iframe = page.locator("main iframe").first
                await iframe.wait_for(state="visible", timeout=25000)
                await iframe.scroll_into_view_if_needed()
                await page.wait_for_timeout(2400)
                box = await iframe.bounding_box()
                if not box or box["width"] < 150 or box["height"] < 120:
                    raise ValueError("invalid native demo iframe dimensions")
                raw = await iframe.screenshot(animations="disabled", timeout=20000)
                img = Image.open(BytesIO(raw)).convert("RGB")
                if sum(ImageStat.Stat(img).stddev) < 7:
                    raise ValueError("near-blank Forui demo: do not archive a placeholder")
                img.thumbnail((640, 440), Image.Resampling.LANCZOS)
                buf = BytesIO()
                img.save(buf, format="PNG", optimize=True)
                data = buf.getvalue()
                image_path = DIR / (cid + ".png")
                image_path.write_bytes(data)
                entries[cid] = {
                    "component_id": cid,
                    "preview_path": "docs/assets/componenti/" + cid + ".png",
                    "preview_sha256": hashlib.sha256(data).hexdigest(),
                    "origin_url": url,
                    "origin_repo": "duobaseio/forui",
                    "origin_source_commit": SHA,
                    "capture_mode": "OFFICIAL_FLUTTER_WEB_DEMO_IFRAME",
                    "visual_qa": "UNREVIEWED",
                    "asset_rights": "REFERENCE_ONLY_NO_CONSUMER_IMPORT",
                }
                print("CAPTURED", cid, image_path.stat().st_size, "bytes")
            except Exception as error:
                failed.append(f"{cid}: {error}")
            finally:
                await page.close()
        await ctx.close()
        await browser.close()
    PROVENANCE.write_text(json.dumps({"schema_version": 1, "source_commit": SHA,
                                      "previews": entries}, indent=2) + "\n", encoding="utf-8")
    print(f"FORUI: captured {len(entries)}/{len(PAGES)}")
    for error in failed:
        print("UNRESOLVED", error)
    return 0 if len(entries) == len(PAGES) else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
