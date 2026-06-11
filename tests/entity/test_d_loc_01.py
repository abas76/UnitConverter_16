import pytest

from src.entity.exceptions import InvalidFormatError
from src.entity.input_parser import parse_unit_value


def test_d_loc_01_valid_meter_colon_splits_unit_and_value(g1_row_major_inputs):
    unit, value = parse_unit_value(g1_row_major_inputs[0])
    assert unit == "meter"
    assert value == pytest.approx(2.5)


def test_d_loc_01_missing_colon_raises_invalid_format_error(g1_row_major_inputs):
    with pytest.raises(InvalidFormatError):
        parse_unit_value(g1_row_major_inputs[1])


def test_d_loc_01_first_colon_only_splits_value_with_inner_colon(g1_row_major_inputs):
    unit, value = parse_unit_value(g1_row_major_inputs[2])
    assert unit == "feet"
    assert value == pytest.approx(8.2)
