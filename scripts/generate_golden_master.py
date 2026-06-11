"""Generate Golden Master snapshot files from the current CLI behavior."""

from __future__ import annotations

import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from UnitConverter import run

GOLDEN_DIR = ROOT / "tests" / "golden"

CASES: list[dict] = [
    {
        "id": "meter_2_5_table",
        "description": "PRD normal output — meter:2.5 table",
        "kwargs": {"raw_input": "meter:2.5", "output_format": "table"},
        "expected_exit_code": 0,
    },
    {
        "id": "feet_8_2_table",
        "description": "PRD input — feet:8.2 table",
        "kwargs": {"raw_input": "feet:8.2", "output_format": "table"},
        "expected_exit_code": 0,
    },
    {
        "id": "yard_3_table",
        "description": "PRD input — yard:3 table",
        "kwargs": {"raw_input": "yard:3", "output_format": "table"},
        "expected_exit_code": 0,
    },
    {
        "id": "meter_2_5_json",
        "description": "FR-8 JSON output",
        "kwargs": {"raw_input": "meter:2.5", "output_format": "json"},
        "expected_exit_code": 0,
    },
    {
        "id": "meter_2_5_csv",
        "description": "FR-8 CSV output",
        "kwargs": {"raw_input": "meter:2.5", "output_format": "csv"},
        "expected_exit_code": 0,
    },
    {
        "id": "error_invalid_format",
        "description": "PRD error — missing colon",
        "kwargs": {"raw_input": "meter2.5", "output_format": "table"},
        "expected_exit_code": 1,
    },
    {
        "id": "error_invalid_number",
        "description": "PRD error — invalid number",
        "kwargs": {"raw_input": "meter:abc", "output_format": "table"},
        "expected_exit_code": 1,
    },
    {
        "id": "error_unknown_unit",
        "description": "PRD error — unknown unit",
        "kwargs": {"raw_input": "inch:5", "output_format": "table"},
        "expected_exit_code": 1,
    },
    {
        "id": "error_negative_value",
        "description": "PRD error — negative value",
        "kwargs": {"raw_input": "meter:-1", "output_format": "table"},
        "expected_exit_code": 1,
    },
    {
        "id": "cubit_2_table",
        "description": "FR-7 dynamic unit — cubit:2 table",
        "kwargs": {
            "raw_input": "cubit:2",
            "output_format": "table",
            "unit_definitions": ["1 cubit = 0.4572 meter"],
        },
        "expected_exit_code": 0,
    },
]


def capture_case(case: dict) -> tuple[int, str]:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        exit_code = run(**case["kwargs"])
    return exit_code, buffer.getvalue()


def generate() -> None:
    GOLDEN_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []

    for case in CASES:
        exit_code, output = capture_case(case)
        if exit_code != case["expected_exit_code"]:
            raise RuntimeError(
                f"{case['id']}: expected exit {case['expected_exit_code']}, got {exit_code}"
            )

        output_path = GOLDEN_DIR / f"{case['id']}.txt"
        output_path.write_text(output, encoding="utf-8", newline="")

        manifest.append(
            {
                "id": case["id"],
                "description": case["description"],
                "file": output_path.name,
                "exit_code": exit_code,
                "kwargs": case["kwargs"],
            }
        )
        print(f"Wrote {output_path.name} (exit={exit_code})")

    manifest_path = GOLDEN_DIR / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {manifest_path.name} ({len(manifest)} cases)")


if __name__ == "__main__":
    generate()
