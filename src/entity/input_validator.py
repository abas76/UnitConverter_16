from src.entity.exceptions import NegativeValueError
from src.entity.units.registry import DEFAULT_REGISTRY, UnitRegistry


def validate_unit_value(
    unit: str, value: float, registry: UnitRegistry = DEFAULT_REGISTRY
) -> None:
    if value < 0:
        raise NegativeValueError(f"Negative value not allowed: {value}")
    registry.get(unit)
