#!/usr/bin/env python3
"""Read-only source-code probe for public Uiverse posts.

No browser login, cookies, secrets, headless browser, or user credentials.
Each request is restricted to the public uiverse.io host. Never label
unretrieved snippets as acquired.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.parse import urlparse

from curl_cffi import requests

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "UI-UX/UIVERSE/REGISTRO_COMPONENTI.json"
ROUTE_DATA_KEY = "routes/$username.$friendlyId"
CODE_DATA_KEY = "routes/resource.post.code.$id"
URL_RE = re.compile(r"^https://uiverse[.]io/([A-Za-z0-9_.-]+)/([A-Za-z0-9_-]+-\d+)$")
POST_ID_RE = re.compile(r"^[0-9a-f-]{30,40}$", re.I)


def fetch_json(url: str, *, timeout: int = 22):
    if urlparse(url).hostname != "uiverse.io":
        raise ValueError("Refusing non-Uiverse host")
    try:
        response = requests.get(
            url,
            impersonate="chrome",
            timeout=timeout,
            headers={"Accept": "application/json", "Referer": "https://uiverse.io/"},
        )
    except Exception as exc:
        return None, {"status": "NETWORK_ERROR", "error": str(exc)[:180]}
    if response.status_code != 200:
        return None, {"status": "HTTP_ERROR", "http_status": response.status_code,
                      "content_type": response.headers.get("content-type", "")[:80]}
    try:
        body = response.json()
    except (ValueError, json.JSONDecodeError):
        return None, {"status": "NON_JSON", "content_type": response.headers.get("content-type", "")[:80]}
    if not isinstance(body, dict):
        return None, {"status": "INVALID_SHAPE"}
    return body, {"status": "OK"}


def get_code(item):
    match = URL_RE.fullmatch(item["uiverse_url"])
    if not match:
        return None, {"status": "INVALID_SOURCE_URL"}
    author, slug = match.groups()
    url = "https://uiverse.io/" + author + "/" + slug
    meta_url = url + "?_data=" + ROUTE_DATA_KEY
    meta, metadata_status = fetch_json(meta_url)
    if meta is None:
        return None, {"status": "DETAIL_UNAVAILABLE", "detail": metadata_status}
    post = meta.get("post")
    if not isinstance(post, dict) or not post.get("id"):
        return None, {"status": "POST_NOT_FOUND", "detail_keys": sorted(meta.keys())[:12]}
    post_id = str(post["id"])
    if not POST_ID_RE.fullmatch(post_id):
        return None, {"status": "POST_ID_INVALID"}
    html, css = post.get("html"), post.get("css")
    source_endpoint = "DETAIL_LOADER"
    if not isinstance(html, str) or not isinstance(css, str) or not (html or css):
        code_url = ("https://uiverse.io/resource/post/code/" + post_id
                    + "?v=1&_data=" + CODE_DATA_KEY)
        payload, code_status = fetch_json(code_url)
        if payload is None:
            return None, {"status": "CODE_UNAVAILABLE", "detail": code_status,
                          "post_id": post_id}
        html, css = payload.get("html"), payload.get("css")
        source_endpoint = "CODE_DATA_ENDPOINT"
    if not isinstance(html, str) or not isinstance(css, str) or not (html or css):
        return None, {"status": "NO_HTML_CSS", "post_id": post_id}
    if len(html.encode("utf-8")) + len(css.encode("utf-8")) > 750000:
        return None, {"status": "OVERSIZED_CONTENT", "post_id": post_id}
    tags = [
        x.get("tag", {}).get("value")
        for x in (post.get("post_tag") or [])
        if isinstance(x, dict) and isinstance(x.get("tag"), dict)
        and isinstance(x["tag"].get("value"), str)
    ]
    return {
        "id": item["id"], "url": url, "author": author, "slug": slug,
        "post_id": post_id, "type": post.get("type"),
        "is_tailwind": bool(post.get("isTailwind")),
        "title": post.get("title"), "description": post.get("description"),
        "tags": tags, "html": html, "css": css,
        "html_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest(),
        "css_sha256": hashlib.sha256(css.encode("utf-8")).hexdigest(),
        "retrieval": source_endpoint, "status": "ORIGINAL_WEB_CODE_READ",
    }, {"status": "OK"}


def emit_record(data):
    content = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    encoded = base64.b64encode(content).decode("ascii")
    width = 5500
    chunks = [encoded[i:i+width] for i in range(0, len(encoded), width)]
    for i, chunk in enumerate(chunks, 1):
        print(f"UIVERSE_RECOVERY_DATA|{data['id']}|{i}|{len(chunks)}|{chunk}", flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--limit", type=int, default=2)
    p.add_argument("--delay", type=float, default=1.2)
    p.add_argument("--output-dir", default="out/uiverse")
    args = p.parse_args()
    if not (1 <= args.limit <= 100 and 0 <= args.delay <= 5):
        raise SystemExit("Invalid limit or delay")
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    missing = [x for x in catalog["components"]
               if x.get("user_favorite") and not x.get("source_snapshot")]
    if len(missing) > 100:
        raise SystemExit("Unexpectedly large recovery request")
    dest = Path(args.output_dir)
    dest.mkdir(parents=True, exist_ok=True)
    successes, attempts = [], []
    for item in missing[:args.limit]:
        code, outcome = get_code(item)
        result = {"id": item["id"], "url": item["uiverse_url"], **outcome}
        attempts.append(result)
        if code is not None:
            successes.append(code["id"])
            (dest / (code["id"] + ".json")).write_text(
                json.dumps(code, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8")
            emit_record(code)
        print("UIVERSE_RECOVERY_STATUS|" + json.dumps(result, separators=(",", ":")),
              flush=True)
        time.sleep(args.delay)
    (dest / "manifest.json").write_text(
        json.dumps({"total_attempted": len(attempts), "successes": successes,
                    "attempts": attempts}, indent=2) + "\n", encoding="utf-8")
    print(f"UIVERSE_RECOVERY_SUMMARY|attempted={len(attempts)}|succeeded={len(successes)}",
          flush=True)


if __name__ == "__main__":
    main()
