from src.entity.converter import convert_to_all_units
from src.entity.exceptions import (
    InvalidFormatError,
    InvalidNumberError,
    NegativeValueError,
    UnknownUnitError,
)
from src.entity.input_parser import parse_unit_value
from src.entity.input_validator import validate_unit_value
from src.entity.units.registry import UnitRegistry


def process_conversion(raw: str, registry: UnitRegistry) -> tuple[str, float, dict[str, float]]:
    unit, value = parse_unit_value(raw)
    validate_unit_value(unit, value, registry)
    results = convert_to_all_units(unit, value, registry)
    return unit, value, results


def format_error_message(error: Exception) -> str:
    if isinstance(error, InvalidFormatError):
        return str(error)
    if isinstance(error, InvalidNumberError):
        return str(error)
    if isinstance(error, UnknownUnitError):
        return str(error)
    if isinstance(error, NegativeValueError):
        return str(error)
    return str(error)
