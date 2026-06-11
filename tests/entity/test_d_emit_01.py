import pytest

from src.entity.constants import METER_TO_FEET, METER_TO_YARD
from src.entity.converter import convert_to_all_units


def test_d_emit_01_from_meter_returns_all_three_units():
    result = convert_to_all_units("meter", 2.5)
    assert set(result.keys()) == {"meter", "feet", "yard"}


def test_d_emit_01_from_meter_values_match_prd_example():
    result = convert_to_all_units("meter", 2.5)
    assert result["meter"] == pytest.approx(2.5)
    assert result["feet"] == pytest.approx(2.5 * METER_TO_FEET)
    assert result["yard"] == pytest.approx(2.5 * METER_TO_YARD)


def test_d_emit_01_same_input_produces_consistent_output():
    first = convert_to_all_units("meter", 2.5)
    second = convert_to_all_units("meter", 2.5)
    assert first == second
