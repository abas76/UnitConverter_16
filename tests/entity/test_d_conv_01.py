import pytest

from src.entity.converter import to_meter_base


def test_d_conv_01_meter_stays_in_meter_base():
    assert to_meter_base("meter", 2.5) == pytest.approx(2.5)


def test_d_conv_01_feet_converts_to_meter_base():
    # BR-1: 8.2 feet ≈ 2.5 meter
    assert to_meter_base("feet", 8.2) == pytest.approx(2.5, rel=0.01)


def test_d_conv_01_yard_converts_to_meter_base():
    # BR-2: 2.73 yard ≈ 2.5 meter
    assert to_meter_base("yard", 2.734025) == pytest.approx(2.5, rel=0.01)
