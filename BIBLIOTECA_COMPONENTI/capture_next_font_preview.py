#!/usr/bin/env python3
"""Capture the one original Ruixen TSX requiring Next.js next/font/google.

Fail closed. A screenshot counts only if it runs the source byte-for-byte in a
real Next runtime, renders Poppins via the Next font loader, and is nonblank.
Do not overwrite other previews or claim native Flutter support.
"""
from __future__ import annotations
import asyncio, hashlib, json, subprocess, time
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from PIL import Image, ImageStat
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "BIBLIOTECA_COMPONENTI"
RUNTIME = HERE / "next_source_renderer"
ORIGINAL = HERE / "sorgenti/ruixen/glowing-send-input.tsx"
OUT = ROOT / "docs/assets/componenti/RXN-glowing-send-input.png"
PROVENANCE = HERE / "ANTEPRIME_ORIGINI.json"
SOURCE_BLOB = "a7a0d3dd2785d9a708a5d8a654637547af2fa235"
SOURCE_COMMIT = "f6b20860623fa39122ac2b5f0e5bd29a9eb10941"

def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

async def main() -> None:
    assert git_blob(ORIGINAL.read_bytes()) == SOURCE_BLOB, "ORIGINAL_TSX_CHANGED"
    assert not OUT.exists(), "EXISTING_PREVIEW_REFUSE_OVERWRITE"
    log_path = Path("/tmp/next_original_source_capture.log")
    with log_path.open("w", encoding="utf-8") as log:
        server = subprocess.Popen(["npm", "run", "dev"], cwd=RUNTIME, stdout=log, stderr=subprocess.STDOUT)
        try:
            ready = False
            for _ in range(100):
                if server.poll() is not None:
                    raise RuntimeError("NEXT_SERVER_EXITED")
                try:
                    with urlopen("http://127.0.0.1:5182", timeout=3) as response:
                        if response.status == 200:
                            ready = True
                            break
                except Exception:
                    pass
                await asyncio.sleep(1)
            if not ready:
                raise RuntimeError("NEXT_SERVER_UNAVAILABLE")
            async with async_playwright() as play:
                browser = await play.chromium.launch(headless=True, args=["--no-sandbox"])
                page = await browser.new_page(viewport={"width": 1000, "height": 650}, device_scale_factor=1, color_scheme="light")
                errors: list[str] = []
                page.on("pageerror", lambda exc: errors.append(str(exc)))
                try:
                    resp = await page.goto("http://127.0.0.1:5182", wait_until="networkidle", timeout=60000)
                    if not resp or resp.status != 200:
                        raise ValueError("ORIGINAL_NEXT_PAGE_NOT_HTTP_200")
                    root = page.locator('#component-root[data-source="RXN-glowing-send-input"]')
                    await root.wait_for(state="visible", timeout=30000)
                    input_el = root.locator("input")
                    await input_el.wait_for(state="visible")
                    await input_el.fill("Design App")
                    await page.evaluate("document.fonts.ready")
                    css = await input_el.evaluate("(el) => getComputedStyle(el)")
                    family = await input_el.evaluate("(el) => getComputedStyle(el).fontFamily")
                    loaded = await input_el.evaluate("""el => {
                       const f = getComputedStyle(el).fontFamily.split(',')[0].replace(/[\\\"']/g, '').trim();
                       return document.fonts.check('500 16px "' + f + '"');
                    }""")
                    if "poppins" not in family.lower() or not loaded:
                        raise ValueError("ORIGINAL_POPPINS_FONT_NOT_LOADED: " + family)
                    button_count = await root.locator("button").count()
                    if button_count != 1:
                        raise ValueError("ORIGINAL_SOURCE_BUTTON_MISSING")
                    if errors:
                        raise ValueError("BROWSER_RUNTIME_ERRORS: " + "; ".join(errors)[:400])
                    await page.wait_for_timeout(1300)
                    raw = await root.screenshot(animations="disabled", timeout=20000)
                    with Image.open(BytesIO(raw)) as img:
                        rgb = img.convert("RGB")
                        std = sum(ImageStat.Stat(rgb).stddev)
                        if rgb.size != (720, 340) or std < 9 or len(raw) < 1000:
                            raise ValueError("BLANK_OR_WRONG_SOURCE_PREVIEW")
                        image_copy = rgb.copy()
                    buf = BytesIO()
                    image_copy.save(buf, format="PNG", optimize=True)
                    png = buf.getvalue()
                    digest = hashlib.sha256(png).hexdigest()
                    package_sha = hashlib.sha256((RUNTIME / "package.json").read_bytes()).hexdigest()
                    origins = json.loads(PROVENANCE.read_text(encoding="utf-8"))
                    assert "RXN-glowing-send-input" not in origins.get("previews", {}), "ORIGIN_ALREADY_EXISTS"
                    OUT.write_bytes(png)
                    origins["previews"]["RXN-glowing-send-input"] = {
                        "component_id": "RXN-glowing-send-input",
                        "preview_path": "docs/assets/componenti/RXN-glowing-send-input.png",
                        "preview_sha256": digest,
                        "origin_url": "https://github.com/ruixenui/ruixen.com/blob/" + SOURCE_COMMIT + "/registry/ruixenui/glowing-send-input.tsx",
                        "source_blob_sha": SOURCE_BLOB,
                        "capture_mode": "PINNED_ORIGINAL_TSX_NEXTJS_RENDER",
                        "local_fixture_path": "BIBLIOTECA_COMPONENTI/next_source_renderer/app/page.tsx",
                        "local_renderer_package_sha256": package_sha,
                        "runtime": "Next.js webpack, real next/font/google loader",
                        "font_evidence": {"family": family, "loaded": loaded, "weight": "500", "source": "next/font/google Poppins"},
                        "visual_qa": "UNREVIEWED",
                        "source_scope": "Unchanged original TSX in isolated real Next runtime; fixture input Design App",
                        "asset_rights": "REFERENCE_ONLY_NOT_ADMITTED_TO_CONSUMER",
                        "origin_repo": "ruixenui/ruixen.com",
                        "origin_source_commit": SOURCE_COMMIT,
                    }
                    PROVENANCE.write_text(json.dumps(origins, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
                    print("ORIGINAL_NEXT_PNG_OK", digest, "bytes", len(png), "font", family)
                finally:
                    await page.close()
                    await browser.close()
        finally:
            server.terminate()
            try:
                server.wait(timeout=8)
            except subprocess.TimeoutExpired:
                server.kill()
            if not OUT.exists():
                print("NEXT_SOURCE_RENDER_DIAGNOSTIC_START")
                print(log_path.read_text(encoding="utf-8")[-9000:])
                print("NEXT_SOURCE_RENDER_DIAGNOSTIC_END")

if __name__ == "__main__":
    asyncio.run(main())
