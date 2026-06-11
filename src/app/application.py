import re

from src.entity.units.base import LengthUnit
from src.entity.units.ratio_unit import MetersPerUnitLengthUnit
from src.entity.units.registry import UnitRegistry, create_default_registry


class InvalidUnitDefinitionError(ValueError):
    """Raised when a dynamic unit definition cannot be parsed."""


_UNIT_DEFINITION_PATTERN = re.compile(
    r"^\s*1\s+(\w+)\s*=\s*([\d.]+)\s+meter\s*$",
    re.IGNORECASE,
)


def parse_unit_definition(line: str) -> tuple[str, float]:
    match = _UNIT_DEFINITION_PATTERN.match(line.strip())
    if not match:
        raise InvalidUnitDefinitionError(
            f"Invalid unit definition: {line!r}. Use format: 1 cubit = 0.4572 meter"
        )
    return match.group(1).lower(), float(match.group(2))


def register_unit_definition(registry: UnitRegistry, line: str) -> LengthUnit:
    name, meters_per_unit = parse_unit_definition(line)
    unit = MetersPerUnitLengthUnit(name, meters_per_unit)
    registry.register(unit)
    return unit


def create_registry(
    config_path: str | None = None,
    unit_definitions: list[str] | None = None,
) -> UnitRegistry:
    if config_path:
        from src.entity.config_loader import load_registry_from_json

        registry = load_registry_from_json(config_path)
    else:
        registry = create_default_registry()

    for line in unit_definitions or []:
        register_unit_definition(registry, line)
    return registry
