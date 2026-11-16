"""Compare a sourced physical pin map with kicad-tool lib-symbol query JSON.

Reads JSON only, never KiCad design files. Exit 0: maps agree; 1: mismatch;
2: invalid input. Agreement does not validate the reference map or circuit.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import sys


def pin_records(document, label):
    if not isinstance(document, dict):
        raise ValueError(f"{label}: expected a JSON object")
    pins = document.get("pins")
    if not isinstance(pins, list) or not pins:
        raise ValueError(f"{label}: pins must be a nonempty array")
    for pin in pins:
        if not isinstance(pin, dict):
            raise ValueError(f"{label}: each pin must be an object")
        for field in ("number", "name"):
            value = pin.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label}: pin {field} must be a nonempty string")
        aliases = pin.get("aliases", [])
        if not isinstance(aliases, list) or any(
            not isinstance(alias, str) or not alias.strip() for alias in aliases
        ):
            raise ValueError(f"{label}: aliases must be an array of nonempty strings")
    return pins


def compare(expected, actual):
    wanted = pin_records(expected, "expected")
    for field in ("part", "package", "source"):
        if not isinstance(expected.get(field), str) or not expected[field].strip():
            raise ValueError(f"expected: {field} is required")
    observed = pin_records(actual, "actual")
    if actual.get("found") is not True:
        raise ValueError("actual: requires a successful full library-symbol query")

    want_counts = Counter(p["number"] for p in wanted)
    have_counts = Counter(p["number"] for p in observed)
    expected_duplicates = sorted(n for n, count in want_counts.items() if count > 1)
    actual_duplicates = sorted(n for n, count in have_counts.items() if count > 1)
    wanted_by_number = {p["number"]: p for p in wanted}
    missing = sorted(want_counts.keys() - have_counts.keys())
    unexpected = sorted(have_counts.keys() - want_counts.keys())
    name_mismatches = []
    aliases_used = []
    for pin in observed:
        reference = wanted_by_number.get(pin["number"])
        if reference is None:
            continue
        accepted = [reference["name"], *reference.get("aliases", [])]
        if pin["name"] not in accepted:
            name_mismatches.append({"number": pin["number"],
                                    "expected_names": accepted,
                                    "actual_name": pin["name"]})
        elif pin["name"] != reference["name"]:
            aliases_used.append({"number": pin["number"],
                                 "expected_name": reference["name"],
                                 "actual_name": pin["name"]})
    failures = (missing, unexpected, name_mismatches,
                expected_duplicates, actual_duplicates)
    return {
        "status": "fail" if any(failures) else "pass",
        "part": expected["part"],
        "package": expected["package"],
        "declared_source": expected["source"],
        "actual_lib_id": actual.get("lib_id"),
        "expected_distinct_identifiers": len(want_counts),
        "actual_records": len(observed),
        "actual_distinct_identifiers": len(have_counts),
        "matching_identifiers": len(want_counts.keys() & have_counts.keys()),
        "missing": missing,
        "unexpected": unexpected,
        "name_mismatches": name_mismatches,
        "expected_duplicate_identifiers": expected_duplicates,
        "actual_duplicate_identifiers": actual_duplicates,
        "aliases_used": aliases_used,
        "scope": "Symbol agreement with supplied map only. Source extraction, pin "
                 "types, placed units, nets, footprints and electrical behavior "
                 "are not validated by this helper.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        expected = json.loads(args.expected.read_text(encoding="utf-8-sig"))
        actual = json.loads(args.actual.read_text(encoding="utf-8-sig"))
        report = compare(expected, actual)
        exit_code = 0 if report["status"] == "pass" else 1
    except (OSError, ValueError) as error:
        report = {"status": "invalid_input", "error": str(error)}
        exit_code = 2
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
