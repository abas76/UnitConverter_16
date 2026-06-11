import pytest

from src.entity.constants import METER_TO_FEET, METER_TO_YARD
from src.entity.converter import convert_to_all_units, to_meter_base


def test_d_acc_01_br1_one_meter_equals_feet_ratio():
    result = convert_to_all_units("meter", 1.0)
    assert result["feet"] == pytest.approx(METER_TO_FEET)


def test_d_acc_01_br2_one_meter_equals_yard_ratio():
    result = convert_to_all_units("meter", 1.0)
    assert result["yard"] == pytest.approx(METER_TO_YARD)


def test_d_acc_01_br3_feet_yard_conversion_via_meter():
    meters = to_meter_base("feet", 3.28084)
    assert meters == pytest.approx(1.0)
    all_units = convert_to_all_units("feet", 3.28084)
    assert all_units["yard"] == pytest.approx(METER_TO_YARD, rel=0.001)


def test_d_acc_01_prd_2_5_meter_to_feet_and_yard():
    result = convert_to_all_units("meter", 2.5)
    assert result["feet"] == pytest.approx(2.5 * METER_TO_FEET)
    assert result["yard"] == pytest.approx(2.5 * METER_TO_YARD)
