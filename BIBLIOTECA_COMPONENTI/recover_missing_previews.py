#!/usr/bin/env python3
"""Source-accurate recovery of missing Ruixen and MIT Gentleface previews.

No generic stock artwork, webpage chrome, title-generated graphics or fake screenshots.
Success is recorded only after actual source fetch, content check and SHA256.
"""
from __future__ import annotations

import asyncio
from collections import Counter
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "BIBLIOTECA_COMPONENTI"
IMAGES = ROOT / "docs/assets/componenti"
CAT = json.loads((HERE / "CATALOGO.json").read_text(encoding="utf-8"))
CURRENT = json.loads((HERE / "ANTEPRIME.json").read_text(encoding="utf-8"))["previews"]
RU = HERE / "ANTEPRIME_ORIGINI.json"
GF = HERE / "ANTEPRIME_ORIGINI_GENTLEFACE.json"
REPORT = HERE / "RECUPERO_ANTEPRIME_2026-11-19.json"
PINNED = "f6b20860623fa39122ac2b5f0e5bd29a9eb10941"
RUREPO = "ruixenui/ruixen.com"


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read(url: str, timeout: int = 20) -> bytes:
    request = Request(url, headers={"User-Agent": "Design-App-original-reference-only/1.0"})
    with urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise ValueError("HTTP status " + str(response.status))
        return response.read()


def original_png(raw: bytes) -> Image.Image:
    with Image.open(BytesIO(raw)) as source:
        source.load()
        if source.format != "PNG" or min(source.size) < 16:
            raise ValueError("not an official PNG icon")
        return source.convert("RGBA")


def recover_gentleface(rows):
    old = json.loads(GF.read_text(encoding="utf-8")) if GF.exists() else {}
    entries = old.get("previews", {})
    failures = {}
    for c in rows:
        cid = c["id"]
        dest = IMAGES / (cid + ".png")
        if dest.is_file() and cid in entries and sha256(dest.read_bytes()) == entries[cid]["preview_sha256"]:
            continue
        source = c.get("source_url", "")
        match = re.fullmatch(r"https://gentleface\.com/icons/([a-z0-9-]+)", source)
        if not match:
            failures[cid] = "official icon URL not canonical"
            continue
        slug = match.group(1)
        png_url = f"https://gentleface.com/png/line-round/48/{slug}.png"
        try:
            original_bytes = read(png_url)
            icon = original_png(original_bytes)
            if icon.getbbox() is None:
                raise ValueError("transparent/empty PNG")
            # Some correct minimalist icons (e.g. pause) cover very few pixels.
            # Crop only to actual nontransparent source bounds before enlarging;
            # preserve the glyph pixels, aspect ratio, and official source hash.
            if cid == "ICO-021":
                alpha = icon.getchannel("A")
                bounds = alpha.getbbox()
                if not bounds:
                    raise ValueError("official icon has no visible pixels")
                icon = icon.crop(bounds)
            icon.thumbnail((48, 48), Image.Resampling.NEAREST)
            icon = icon.resize((96, 96), Image.Resampling.NEAREST)
            canvas = Image.new("RGBA", (112, 112), "#f5f6f9")
            canvas.alpha_composite(icon, (8, 8))
            buf = BytesIO()
            canvas.convert("RGB").save(buf, format="PNG", optimize=True)
            thumb = buf.getvalue()
            if len(thumb) < 512 or sum(ImageStat.Stat(canvas.convert("RGB")).stddev) < 5:
                raise ValueError("original icon yielded uninformative image")
            dest.write_bytes(thumb)
            entries[cid] = {
                "component_id": cid, "preview_path": f"docs/assets/componenti/{cid}.png",
                "preview_sha256": sha256(thumb), "origin_url": source,
                "origin_asset_url": png_url, "original_asset_sha256": sha256(original_bytes),
                "origin_provider": "gentleface.com", "source_license": "MIT",
                "capture_mode": "OFFICIAL_MIT_PNG_CONTAINED",
                "pixel_transform": "line-round 48px contained; ICO-021 cropped to alpha bounds for legibility; no synthetic glyph",
                "source_availability": "OFFICIAL_LIVE_NON_COMMIT_PINNED",
                "visual_qa": "UNREVIEWED", "asset_rights": "MIT_REFERENCE_NO_CONSUMER_BUNDLE",
            }
        except (HTTPError, URLError, ValueError, OSError) as exc:
            failures[cid] = str(exc)[:180]
    GF.write_text(json.dumps({
        "schema_version": 1, "origin": "Gentleface Icons MIT — https://gentleface.com/",
        "previews": dict(sorted(entries.items()))
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return entries, failures


async def recover_ruixen(rows):
    """Screenshot actual official component iframes, never a whole docs page."""
    from playwright.async_api import async_playwright
    original = json.loads(RU.read_text(encoding="utf-8"))
    entries = original["previews"]
    failures = {}
    mutex = asyncio.Semaphore(5)
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(
            viewport={"width": 1140, "height": 780}, color_scheme="light",
            reduced_motion="no-preference"
        )
        async def one(c):
            cid, slug = c["id"], c["id"][4:]
            if cid in entries and (IMAGES / (cid + ".png")).is_file():
                return
            async with mutex:
                page = await context.new_page()
                attempts = []
                candidates = [
                    f"https://ruixen.com/docs/components/{slug}",
                    f"https://ruixen.com/docs/sections/{slug}",
                    f"https://ruixen.com/preview/{slug}",
                ]
                try:
                    for url in candidates:
                        try:
                            reply = await page.goto(url, wait_until="domcontentloaded", timeout=13000)
                            if not reply or reply.status >= 400:
                                attempts.append(f"{url}: HTTP or no response")
                                continue
                            # A matching component heading must exist (no global site-page capture).
                            headings = await page.locator("main h1,main h2").all_text_contents()
                            if not any(slug.replace("-", " ").lower() in h.lower().replace("—", " ") for h in headings):
                                attempts.append(f"{url}: no component-specific heading")
                                continue
                            frame = page.locator("main iframe").first
                            if await frame.count() == 0:
                                attempts.append(f"{url}: no isolated component iframe")
                                continue
                            await frame.wait_for(state="visible", timeout=7000)
                            await frame.scroll_into_view_if_needed(timeout=5000)
                            await page.wait_for_timeout(1400)
                            size = await frame.bounding_box()
                            if not size or size["width"] < 100 or size["height"] < 50:
                                attempts.append(f"{url}: invalid demo size")
                                continue
                            raw = await frame.screenshot(animations="disabled", timeout=12000)
                            with Image.open(BytesIO(raw)) as im:
                                shot = im.convert("RGB")
                                if sum(ImageStat.Stat(shot).stddev) < 9:
                                    raise ValueError("blank or near-uniform component")
                                shot.thumbnail((640, 440), Image.Resampling.LANCZOS)
                                buffer = BytesIO()
                                shot.save(buffer, "PNG", optimize=True)
                            png = buffer.getvalue()
                            if len(png) < 700:
                                raise ValueError("too-small demo screenshot")
                            path = IMAGES / (cid + ".png")
                            path.write_bytes(png)
                            entries[cid] = {
                                "component_id": cid, "preview_path": f"docs/assets/componenti/{cid}.png",
                                "preview_sha256": sha256(png), "origin_url": url,
                                "origin_repo": RUREPO, "origin_source_commit": PINNED,
                                "capture_mode": "LIVE_DOCS_COMPONENT_IFRAME",
                                "preview_source_version": "LIVE_UNPINNED_NOT_ASSERTED_MATCHING_CODE_SHA",
                                "visual_qa": "UNREVIEWED",
                                "source_scope": "isolated official component iframe, NOT docs page chrome",
                                "asset_rights": "REFERENCE_ONLY_NOT_ADMITTED_TO_CONSUMER",
                            }
                            break
                        except Exception as error:
                            attempts.append(f"{url}: {str(error)[:100]}")
                    if cid not in entries:
                        failures[cid] = attempts
                finally:
                    await page.close()
        await asyncio.gather(*(one(c) for c in rows))
        await context.close()
        await browser.close()
    RU.write_text(json.dumps({
        **{k: v for k, v in original.items() if k != "previews"},
        "previews": dict(sorted(entries.items())),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return entries, failures


async def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    missing = [c for c in CAT["components"] if not CURRENT[c["id"]].get("image_path")]
    by_source = Counter(c["source_site"] for c in missing)
    ruixen = [c for c in missing if c["source_site"] == "RUIXEN"]
    gentle = [c for c in missing if c["source_site"] == "GENTLEFACE"]
    if len(missing) > 158 or len(ruixen) > 67 or len(gentle) > 28:
        raise ValueError("unexpected increase in missing original previews; investigate")
    icons, gf_fail = recover_gentleface(gentle)
    recovered, ru_fail = await recover_ruixen(ruixen)
    ru_new = [c["id"] for c in ruixen if c["id"] in recovered and (IMAGES / (c["id"] + ".png")).exists()]
    gf_new = [c["id"] for c in gentle if c["id"] in icons and (IMAGES / (c["id"] + ".png")).exists()]
    REPORT.write_text(json.dumps({
        "catalog_sha_immutable": PINNED,
        "baseline_missing": 158,
        "round_start_missing": len(missing),
        "baseline_by_source": by_source,
        "new_ruixen": len(ru_new), "new_gentleface": len(gf_new),
        "new_total": len(ru_new) + len(gf_new),
        "estimated_remaining": len(missing) - len(ru_new) - len(gf_new),
        "cumulative_recovered_from_322_baseline": 158 - (len(missing) - len(ru_new) - len(gf_new)),
        "recovered_ruixen_ids": ru_new, "recovered_gentleface_ids": gf_new,
        "ruixen_unresolved": ru_fail, "gentleface_unresolved": gf_fail,
        "other_source_missing": {
            key: n for key, n in by_source.items() if key not in {"RUIXEN", "GENTLEFACE"}
        },
        "claim": "Only files actually acquired and hashed count; all images are UNREVIEWED until visual inspection."
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("RECOVERY_RESULT", len(ru_new), "Ruixen,", len(gf_new),
          "Gentleface; residual", len(missing) - len(ru_new) - len(gf_new))
    for cid, detail in list(ru_fail.items())[:10]:
        print("RUIXEN_BLOCKED", cid, detail[-1] if detail else "no source")
    for cid, detail in list(gf_fail.items())[:10]:
        print("GENTLEFACE_BLOCKED", cid, detail)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
