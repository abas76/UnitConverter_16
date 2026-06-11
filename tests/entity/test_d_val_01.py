import pytest

from src.entity.exceptions import (
    InvalidFormatError,
    InvalidNumberError,
    NegativeValueError,
    UnknownUnitError,
)
from src.entity.input_parser import parse_unit_value
from src.entity.input_validator import validate_unit_value


def test_d_val_01_invalid_format_raises():
    with pytest.raises(InvalidFormatError, match="unit:value"):
        parse_unit_value("meter2.5")


def test_d_val_01_invalid_number_raises():
    with pytest.raises(InvalidNumberError, match="Invalid number: abc"):
        parse_unit_value("meter:abc")


def test_d_val_01_unknown_unit_raises():
    with pytest.raises(UnknownUnitError, match="Unknown unit: inch"):
        validate_unit_value("inch", 5.0)


def test_d_val_01_negative_value_raises():
    with pytest.raises(NegativeValueError, match="Negative value"):
        validate_unit_value("meter", -1.0)
