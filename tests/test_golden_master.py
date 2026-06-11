"""Golden Master regression tests — compare CLI output to approved snapshots."""

from __future__ import annotations

import io
import json
from contextlib import redirect_stdout
from pathlib import Path

import pytest

from UnitConverter import run

GOLDEN_DIR = Path(__file__).resolve().parent / "golden"
MANIFEST_PATH = GOLDEN_DIR / "manifest.json"


def _load_manifest() -> list[dict]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def _capture(kwargs: dict) -> tuple[int, str]:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        exit_code = run(**kwargs)
    return exit_code, buffer.getvalue()


@pytest.fixture(scope="module")
def manifest() -> list[dict]:
    assert MANIFEST_PATH.is_file(), "Golden Master manifest missing — run scripts/generate_golden_master.py"
    return _load_manifest()


@pytest.mark.parametrize("case_id", [c["id"] for c in _load_manifest()])
def test_golden_master_output_matches(case_id: str, manifest: list[dict]) -> None:
    case = next(item for item in manifest if item["id"] == case_id)
    golden_path = GOLDEN_DIR / case["file"]
    expected = golden_path.read_text(encoding="utf-8")

    exit_code, actual = _capture(case["kwargs"])

    assert exit_code == case["exit_code"], (
        f"{case_id}: exit code mismatch — expected {case['exit_code']}, got {exit_code}"
    )
    assert actual == expected, (
        f"{case_id}: output mismatch\n"
        f"--- expected ({golden_path.name}) ---\n{expected!r}\n"
        f"--- actual ---\n{actual!r}"
    )


def test_golden_master_manifest_case_count() -> None:
    manifest = _load_manifest()
    golden_files = sorted(GOLDEN_DIR.glob("*.txt"))
    assert len(manifest) == len(golden_files)
    assert len(manifest) >= 10
