#!/usr/bin/env python3
"""Validate every vendored semantic SFX against pinned source bytes."""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = Path(__file__).with_name("manifest.json")
EXPECTED = {
    "selection", "success", "warning", "error",
    "completion", "notification_soft",
}
ASSET_ROOT = (ROOT / "packs/sound/adapters/flutter/assets").resolve()


def validate() -> None:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert data["source_repo"] == "wyzowl/sfx-kit"
    assert data["license"] == "CC0-1.0"
    assert (ROOT / data["license_path"]).is_file()
    assert len(data["assets"]) == 6
    assert {item["id"] for item in data["assets"]} == EXPECTED

    total = 0
    for item in data["assets"]:
        path = (ROOT / item["asset_path"]).resolve()
        assert path.parent == ASSET_ROOT, f"unexpected asset location: {path}"
        assert path.name == item["id"] + ".wav", item["id"]
        raw = path.read_bytes()
        assert len(raw) == item["size_bytes"], f"size mismatch: {path}"
        assert len(raw) < 128_000, f"oversized UI sound: {path}"
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == item["sha256"], f"SHA256 mismatch: {path}"
        git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + bytes((0,)) + raw).hexdigest()
        assert git_blob == item["source_blob_sha"], f"source byte mismatch: {path}"

        assert raw[:4] == b"RIFF" and raw[8:12] == b"WAVE", path
        # These six upstream clips have the same simple 44-byte PCM WAV header.
        assert raw[12:16] == b"fmt " and raw[36:40] == b"data", path
        assert struct.unpack_from("<I", raw, 16)[0] == 16, path
        encoding, channels, sample_rate = struct.unpack_from("<HHI", raw, 20)
        bits = struct.unpack_from("<H", raw, 34)[0]
        assert (encoding, channels, sample_rate, bits) == (1, 1, 48_000, 24), path
        data_size = struct.unpack_from("<I", raw, 40)[0]
        assert struct.unpack_from("<I", raw, 4)[0] == len(raw) - 8, f"RIFF size mismatch: {path}"
        # Upstream WAVs may include trailing metadata chunks after the audio payload.
        assert 44 + data_size <= len(raw), f"WAV data exceeds file: {path}"
        duration = data_size / (sample_rate * channels * (bits // 8))
        assert abs(duration - item["duration_seconds"]) < 0.001, path
        total += len(raw)

    assert total == data["distribution"]["total_bytes"], "total size mismatch"
    assert total < 500_000, "semantic sound pack exceeded size budget"
    assert data["distribution"]["default_enabled"] is False
    assert data["distribution"]["critical_alarm"] is False
    print(f"Semantic sound pack PASS: {len(EXPECTED)} CC0 WAVs, {total} bytes, SHA256/Git SHA1 verified")


if __name__ == "__main__":
    try:
        validate()
    except (AssertionError, OSError, ValueError, KeyError) as exc:
        print(f"Semantic sound pack FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
