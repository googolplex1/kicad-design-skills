"""Regressions for incomplete or misleading physical pin inventories."""
import copy
import importlib.util
from pathlib import Path
import unittest


script = Path(__file__).resolve().parents[1] / "kicad-schematic/scripts/check_pinmap.py"
spec = importlib.util.spec_from_file_location("pinmap_check", script)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PinmapTests(unittest.TestCase):
    def setUp(self):
        self.expected = {
            "part": "Test-3", "package": "Three balls", "source": "Test fixture",
            "pins": [{"number": "A1", "name": "VIN"},
                     {"number": "A2", "name": "GND"},
                     {"number": "B1", "name": "OUT", "aliases": ["VOUT"]}],
        }
        self.actual = {"found": True, "pins": copy.deepcopy(self.expected["pins"])}

    def test_valid_map_and_reviewed_alias(self):
        self.actual["pins"][2]["name"] = "VOUT"
        result = checker.compare(self.expected, self.actual)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(len(result["aliases_used"]), 1)

    def test_same_count_wrong_number_fails(self):
        self.actual["pins"][1]["number"] = "B2"
        result = checker.compare(self.expected, self.actual)
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["missing"], ["A2"])
        self.assertEqual(result["unexpected"], ["B2"])

    def test_group_text_does_not_replace_physical_pins(self):
        self.actual["pins"] = [{"number": "A1/A2", "name": "VIN"},
                               {"number": "GND balls", "name": "GND"},
                               {"number": "B1", "name": "OUT"}]
        result = checker.compare(self.expected, self.actual)
        self.assertEqual(result["matching_identifiers"], 1)
        self.assertEqual(result["missing"], ["A1", "A2"])

    def test_swapped_functions_fail_with_complete_number_set(self):
        self.actual["pins"][0]["name"] = "GND"
        self.actual["pins"][1]["name"] = "VIN"
        result = checker.compare(self.expected, self.actual)
        self.assertEqual(result["status"], "fail")
        self.assertEqual(len(result["name_mismatches"]), 2)

    def test_duplicate_cannot_mask_omission(self):
        self.actual["pins"][1] = copy.deepcopy(self.actual["pins"][0])
        result = checker.compare(self.expected, self.actual)
        self.assertEqual(result["actual_duplicate_identifiers"], ["A1"])
        self.assertEqual(result["missing"], ["A2"])

    def test_bad_reference_is_not_accepted(self):
        del self.expected["source"]
        with self.assertRaises(ValueError):
            checker.compare(self.expected, self.actual)

    def test_missing_symbol_or_empty_maps_cannot_pass(self):
        self.actual["found"] = False
        with self.assertRaises(ValueError):
            checker.compare(self.expected, self.actual)
        self.actual["found"] = True
        self.actual["pins"] = []
        self.expected["pins"] = []
        with self.assertRaises(ValueError):
            checker.compare(self.expected, self.actual)


if __name__ == "__main__":
    unittest.main()
