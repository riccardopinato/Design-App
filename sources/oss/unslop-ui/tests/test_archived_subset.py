"""Runnable subset of pinned MIT Unslop UI scanner/loader smoke tests.

The upstream tests/test_skill.py imports unarchived evals, examples and plugin
fixtures. Keep that original file untouched as provenance; this subset tests
only the original scanner/loader that this library actually archived.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCANNER = ROOT / "skills" / "unslop-ui" / "scripts" / "count_tells.py"
LOADER = ROOT / "skills" / "unslop-ui" / "scripts" / "load_unslop.py"


class ArchivedSubsetSmokeTest(unittest.TestCase):
    def test_scanner_reports_actual_decorative_numbering(self):
        with tempfile.TemporaryDirectory() as tmp:
            sample = Path(tmp) / "example.html"
            sample.write_text("<section>01 // Features</section>\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCANNER), str(sample)],
                capture_output=True, text=True, check=True,
            )
            data = json.loads(result.stdout)
            self.assertGreaterEqual(data["total"], 1)
            self.assertGreaterEqual(data["U2 decorative numbering"]["count"], 1)

    def test_minimal_ui_does_not_trigger_regex_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            sample = Path(tmp) / "clean.html"
            sample.write_text("<h1>Settings</h1>\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCANNER), str(sample)],
                capture_output=True, text=True, check=True,
            )
            self.assertEqual(json.loads(result.stdout)["total"], 0)

    def test_fallback_loader_runs_without_external_plugins(self):
        with tempfile.TemporaryDirectory() as tmp:
            environment = dict(os.environ, HOME=tmp)
            result = subprocess.run(
                [sys.executable, str(LOADER)],
                cwd=tmp, env=environment,
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout.strip())
            self.assertTrue("bundled rules" in result.stdout or "Patterns to detect" in result.stdout)


if __name__ == "__main__":
    unittest.main()
