#!/usr/bin/env python3
"""Source-grounded UID registry and adoption-safety tests."""
import unittest
import uid


class UIDContractTests(unittest.TestCase):
    def test_all_unique_stable_uids_and_no_canonical_loss(self):
        result = uid.validate()
        self.assertEqual(478, result["uids"])
        self.assertEqual(478, result["catalog"])

    def test_examples_resolve_to_exact_canonical(self):
        cases = {
            "UID-0127": "RXN-button-copy",
            "UID-0350": "RXN-verification-input",
            "UID-0361": "UIV-002",
            "UID-0041": "FCL-002",
        }
        for alias, expected in cases.items():
            with self.subTest(alias=alias):
                self.assertEqual(expected, uid.inspect(alias)["canonical_id"])

    def test_legacy_alias_deduplicates(self):
        self.assertEqual(uid.inspect("UIV-107")["canonical_id"], "UIV-055")

    def test_react_source_never_claimed_flutter_drop_in(self):
        p = uid.plan("UID-0127", "annas-diary", "flutter", "pulsante copia")
        self.assertEqual("ADAPTER_REQUIRED", p["adoption_mode"])
        self.assertFalse(p["copy_paste_ready"])
        self.assertEqual("PLAN_ONLY_NOT_IMPLEMENTED", p["status"])

    def test_reference_only_never_claims_a_code_file(self):
        p = uid.plan("UID-0041", "notes-ecosistema", "flutter", "pulsante")
        self.assertEqual("SOURCE_UNAVAILABLE", p["adoption_mode"])
        self.assertIsNone(p["component"]["archive_path"])
        self.assertFalse(p["copy_paste_ready"])

    def test_no_missing_uid_silent_fallback(self):
        with self.assertRaises(LookupError):
            uid.inspect("UID-9999")


if __name__ == "__main__":
    unittest.main()
