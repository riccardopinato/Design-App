#!/usr/bin/env python3
"""Capture actual Ruixen previews, not generic mockups. Origin pinned to MIT repo."""
import argparse
import asyncio
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "BIBLIOTECA_COMPONENTI"
OUT = ROOT / "docs/assets/componenti"
ORIGINS = HERE / "ANTEPRIME_ORIGINI.json"
COMMIT = "f6b20860623fa39122ac2b5f0e5bd29a9eb10941"
UPSTREAM = "ruixenui/ruixen.com"
RAW = f"https://raw.githubusercontent.com/{UPSTREAM}/{COMMIT}/"
PNG = bytes.fromhex("89504e470d0a1a0a")


def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": "Design-App-Preview/1.0"}), timeout=25) as response:
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}")
        return response.read()


def load_map():
    source = fetch(RAW + "lib/component-preview-data.ts")
    mapping = {}
    for match in re.finditer(r'"([a-z0-9-]+)":\s*\{([\s\S]*?)\n\s*\},', source.decode()):
        img = re.search(r'light:\s*[\x60"](/preview_images/[^\x60"]+)[\x60"]', match.group(2))
        if img:
            mapping[match.group(1)] = img.group(1)
    return mapping, hashlib.sha256(source).hexdigest()


def save(raw, cid):
    im = Image.open(BytesIO(raw))
    im.load()
    if min(im.size) < 10:
        raise ValueError("preview too small")
    im = im.convert("RGB")
    im.thumbnail((640, 440), Image.Resampling.LANCZOS)
    buf = BytesIO()
    im.save(buf, "PNG", optimize=True)
    blob = buf.getvalue()
    if not blob.startswith(PNG) or len(blob) < 500:
        raise ValueError("invalid screenshot")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / (cid + ".png")).write_bytes(blob)
    return hashlib.sha256(blob).hexdigest(), len(blob)


def evidence(cid, sha, url, mode, **kw):
    return {"component_id": cid, "preview_path": f"docs/assets/componenti/{cid}.png",
            "preview_sha256": sha, "origin_url": url,
            "origin_repo": UPSTREAM, "origin_source_commit": COMMIT,
            "capture_mode": mode, "visual_qa": "UNREVIEWED",
            "asset_rights": "REFERENCE_ONLY_NOT_ADMITTED_TO_CONSUMER", **kw}


async def demos(missing):
    from playwright.async_api import async_playwright
    findings, failures = {}, []
    sem = asyncio.Semaphore(4)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1100, "height": 720},
                                        color_scheme="light", reduced_motion="reduce")
        async def one(item):
            async with sem:
                cid = item["id"]
                slug = cid.removeprefix("RXN-")
                url = f"https://ruixen.com/preview/{slug}"
                page = await ctx.new_page()
                try:
                    resp = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    if not resp or resp.status >= 400:
                        raise ValueError("page HTTP failure")
                    area = page.locator("main > div").first
                    await area.wait_for(state="visible", timeout=12000)
                    await page.wait_for_timeout(1500)
                    text = (await area.inner_text()).lower()
                    if "component not found" in text or "could not be found" in text or (text.strip() == "loading..."):
                        raise ValueError("no rendered component")
                    box = await area.bounding_box()
                    if not box or box["width"] < 100 or box["height"] < 30:
                        raise ValueError("invalid preview bounds")
                    data = await page.screenshot(
                        clip={"x": max(0, box["x"]), "y": max(0, box["y"]),
                              "width": min(1020, box["width"]), "height": min(480, box["height"])},
                        animations="disabled", timeout=20000)
                    sha, size = save(data, cid)
                    findings[cid] = evidence(
                        cid, sha, url, "LIVE_COMPONENT_ONLY_SCREENSHOT",
                        captured_on="2026-11-19", bytes=size)
                except Exception as exc:
                    # The /preview route does not exist for every upstream
                    # item. The official MDX docs may still mount an actual
                    # interactive component in a dedicated React iframe.
                    captured = False
                    for docs_section in ("components", "sections"):
                        docs_url = f"https://ruixen.com/docs/{docs_section}/{slug}"
                        try:
                            resp = await page.goto(docs_url, wait_until="domcontentloaded", timeout=28000)
                            if not resp or resp.status >= 400:
                                continue
                            frame = page.locator("main iframe").first
                            await frame.wait_for(state="visible", timeout=8500)
                            await frame.scroll_into_view_if_needed()
                            await page.wait_for_timeout(1100)
                            box = await frame.bounding_box()
                            if not box or box["width"] < 120 or box["height"] < 80:
                                continue
                            data = await frame.screenshot(animations="disabled", timeout=14000)
                            # An empty frame or a blank docs shell is not an
                            # authentic preview of this original component.
                            from PIL import ImageStat
                            im = Image.open(BytesIO(data)).convert("RGB")
                            if sum(ImageStat.Stat(im).stddev) < 8:
                                continue
                            sha, size = save(data, cid)
                            findings[cid] = evidence(
                                cid, sha, docs_url, "LIVE_DOCS_COMPONENT_IFRAME",
                                captured_on="2026-11-19", bytes=size,
                                source_scope="component_iframe_not_site_header")
                            captured = True
                            break
                        except Exception:
                            continue
                    if not captured:
                        failures.append(f"{cid}: preview and docs iframe unavailable ({exc})")
                finally:
                    await page.close()
        await asyncio.gather(*(one(x) for x in missing))
        await ctx.close()
        await browser.close()
    return findings, failures


async def main(live, limit):
    original = json.loads((HERE / "CATALOGO.json").read_text(encoding="utf-8"))
    rows = [x for x in original["components"] if x["source_site"] == "RUIXEN"]
    if len(rows) != 277 or any(x["source_commit"] != COMMIT for x in rows):
        raise ValueError("Ruixen catalog baseline mismatch")
    mapping, index_sha = load_map()
    previous = json.loads(ORIGINS.read_text(encoding="utf-8")) if ORIGINS.exists() else {}
    entries = previous.get("previews", {})
    missing = []
    for c in rows:
        cid, slug = c["id"], c["id"][4:]
        dest = OUT / (cid + ".png")
        if dest.exists() and cid in entries and hashlib.sha256(dest.read_bytes()).hexdigest() == entries[cid]["preview_sha256"]:
            continue
        upstream_image = mapping.get(slug)
        if not upstream_image:
            missing.append(c)
            continue
        remote = RAW + "public" + upstream_image
        try:
            raw = fetch(remote)
            sha, length = save(raw, cid)
            entries[cid] = evidence(cid, sha, remote, "PINNED_OFFICIAL_PREVIEW_IMAGE",
                original_sha256=hashlib.sha256(raw).hexdigest(),
                origin_path="public" + upstream_image,
                upstream_preview_index_sha256=index_sha, bytes=length)
        except Exception as exc:
            # Some original preview paths are not committed as public Git
            # blobs, but the upstream docs serve the same static image.
            live_static = "https://ruixen.com" + upstream_image
            try:
                raw = fetch(live_static)
                sha, length = save(raw, cid)
                entries[cid] = evidence(
                    cid, sha, live_static, "OFFICIAL_SITE_STATIC_IMAGE",
                    original_sha256=hashlib.sha256(raw).hexdigest(),
                    origin_path=None, upstream_preview_index_sha256=index_sha,
                    bytes=length, source_availability="LIVE_UNPINNED_IMAGE_BYTES")
            except Exception as second:
                print("STATIC_MISSING", cid, str(exc), "| website:", str(second))
                missing.append(c)
    failures = []
    if live:
        more, failures = await demos(missing[:limit] if limit else missing)
        entries.update(more)
    ORIGINS.write_text(json.dumps({
        "schema_version": 1, "source_commit": COMMIT,
        "preview_index_sha256": index_sha,
        "previews": dict(sorted(entries.items()))}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"RUIXEN: {len(entries)} previews, {277-len(entries)} unresolved; "
          f"{len(mapping)} official index entries, {len(failures)} live errors")
    for failure in failures[:20]:
        print("LIVE_MISSING", failure)
    return 0 if entries else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    raise SystemExit(asyncio.run(main(args.live, args.limit)))
