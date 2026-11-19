#!/usr/bin/env python3
"""Capture static, honest previews from archived Uiverse HTML/CSS with Playwright.

- Never executes third-party JavaScript (JS disabled and scripts stripped).
- Blocks external requests, so no unlicensed remote images/fonts are pulled in.
- Captures a fixed, isolated neutral viewport per original component.
- Never labels images as QA-certified. A PNG is visual reference evidence only.
"""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "BIBLIOTECA_COMPONENTI" / "CATALOGO.json"
DEST = ROOT / "docs" / "assets" / "componenti"

WRAPPER_START = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy"
content="default-src 'none'; style-src 'unsafe-inline'; img-src data: blob:; font-src data:;">
<style>
html,body{width:100%;height:100%;margin:0;padding:0;background:#f4f6fa;color:#1d283a;}
body{display:grid;place-items:center;font-family:system-ui,sans-serif;overflow:hidden;}
#preview{min-width:0;max-width:100%;max-height:100%;overflow:hidden;display:grid;place-items:center;}
*{box-sizing:border-box}
</style></head><body><div id="preview">"""
WRAPPER_END = "</div></body></html>"


def source_html(record: dict) -> str:
    path = ROOT / record["archive_path"]
    if not path.is_file():
        raise FileNotFoundError(f'{record["id"]}: archived HTML absent: {path}')
    original = path.read_text(encoding="utf-8")
    # CSS from the same archived ID, not a fetched third-party library.
    cssfile = path.with_suffix(".css")
    css = cssfile.read_text(encoding="utf-8") if cssfile.is_file() else ""
    # Strip scripts before constructing src markup; Chromium JS stays disabled.
    original = re.sub(r"<script\b[^>]*>[\s\S]*?</script\s*>", "", original,
                      flags=re.IGNORECASE)
    original = re.sub(r"<base\b[^>]*>", "", original, flags=re.IGNORECASE)
    original = re.sub(r"<iframe\b[^>]*>[\s\S]*?</iframe\s*>", "", original,
                      flags=re.IGNORECASE)
    original = re.sub(r"<meta\s+http-equiv\s*=\s*['\"]?refresh[^>]*>", "",
                      original, flags=re.IGNORECASE)
    return WRAPPER_START + original + ("<style>" + css + "</style>" if css else "") + WRAPPER_END


async def capture(count: int = 0) -> int:
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Playwright not installed. Install with pip install playwright "
              "then python -m playwright install chromium.", file=sys.stderr)
        return 2
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    rows = [c for c in catalog["components"] if c["source_site"] == "UIVERSE"]
    if len(rows) != 110:
        raise ValueError(f"expected 110 canonical Uiverse, got {len(rows)}")
    if count:
        rows = rows[:count]
    DEST.mkdir(parents=True, exist_ok=True)
    ok, failed = 0, []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 420, "height": 280},
                                            device_scale_factor=1,
                                            color_scheme="light",
                                            reduced_motion="reduce",
                                            java_script_enabled=False)
        async def deny_external(route):
            await route.abort()
        await context.route("**/*", deny_external)
        page = await context.new_page()
        page.set_default_timeout(12000)
        for row in rows:
            cid = row["id"]
            out = DEST / (cid + ".png")
            try:
                source = source_html(row)
                await page.set_content(source, wait_until="domcontentloaded", timeout=12000)
                await page.screenshot(path=str(out), full_page=False,
                                      animations="disabled", timeout=12000)
                # Avoid registering blank or invalid images.
                if out.stat().st_size < 900:
                    raise ValueError("empty/near-empty rendered screenshot")
                ok += 1
            except Exception as e:
                if out.exists():
                    out.unlink()
                failed.append(cid + ": " + str(e))
        await context.close()
        await browser.close()
    print(f"Uiverse preview capture: {ok}/{len(rows)} PNG generated")
    for issue in failed[:25]:
        print("PREVIEW FAILED:", issue, file=sys.stderr)
    # A partial harvest remains usable but must be reported.
    return 0 if ok else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0,
                        help="maximum entries to capture (0 = all 110)")
    args = parser.parse_args()
    raise SystemExit(asyncio.run(capture(args.limit)))
