import pytest


@pytest.fixture
def g1_row_major_inputs():
    """G1 격자 row-major 원시 문자열 (로직 없음, 데이터만)."""
    return (
        "meter:2.5",  # row 0 — T-D-LOC-01-01
        "meter2.5",   # row 1 — T-D-LOC-01-02
        "feet:8:2",   # row 2 — T-D-LOC-01-03
    )


@pytest.fixture
def parsed_input_cases():
    """(raw, expected_unit, expected_value | error_marker) 튜플 리스트 (데이터만)."""
    return (
        ("meter:2.5", "meter", 2.5),
        ("meter2.5", None, "InvalidFormatError"),
        ("feet:8:2", "feet", 8.2),
    )
