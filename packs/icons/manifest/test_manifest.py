import json
import unittest
from pathlib import Path

PATH = Path(__file__).with_name("icons.json")


class IconManifestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(PATH.read_text(encoding="utf-8"))

    def test_shape_and_order(self):
        entries = self.data["icons"]
        ids = [e["id"] for e in entries]
        self.assertEqual(len(ids), 24)
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(set(ids)), 24)
        for entry in entries:
            self.assertTrue(entry["flutter"])
            self.assertTrue(entry["compose"])
            self.assertTrue(entry["description"])

    def test_no_vendor_assets_or_extended_icons(self):
        policy = self.data["policy"]
        self.assertEqual(policy["external_asset_files"], 0)
        self.assertEqual(policy["external_runtime_packages_flutter"], 0)
        self.assertFalse(policy["extended_icon_dependency_android"])
        self.assertGreaterEqual(policy["min_interactive_target_dp"], 48)
        self.assertTrue(policy["localize_content_descriptions"])
        self.assertTrue(policy["explicit_decorative_icons"])

    def test_source_pin_license_and_rtl(self):
        self.assertEqual(self.data["source"]["license"], "Apache-2.0")
        self.assertRegex(self.data["source"]["observed_commit"], r"^[a-f0-9]{40}$")
        directional = [e["id"] for e in self.data["icons"] if e["auto_mirror_rtl"]]
        self.assertEqual(directional, ["back"])

if __name__ == "__main__":
    unittest.main()
