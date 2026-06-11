from src.entity.exceptions import UnknownUnitError
from src.entity.units.base import LengthUnit
from src.entity.units.feet import FeetUnit
from src.entity.units.meter import MeterUnit
from src.entity.units.yard import YardUnit


class UnitRegistry:
    """Open for extension: register new units without modifying converter logic."""

    def __init__(self, units: list[LengthUnit] | None = None) -> None:
        self._units: dict[str, LengthUnit] = {}
        for unit in units or []:
            self.register(unit)

    def register(self, unit: LengthUnit) -> None:
        self._units[unit.name] = unit

    def get(self, name: str) -> LengthUnit:
        try:
            return self._units[name]
        except KeyError:
            raise UnknownUnitError(f"Unknown unit: {name}") from None

    def all_units(self) -> tuple[LengthUnit, ...]:
        return tuple(self._units.values())

    @property
    def supported_names(self) -> frozenset[str]:
        return frozenset(self._units)


def create_default_registry() -> UnitRegistry:
    return UnitRegistry([MeterUnit(), FeetUnit(), YardUnit()])


DEFAULT_REGISTRY = create_default_registry()
