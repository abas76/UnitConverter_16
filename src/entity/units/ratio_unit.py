from src.entity.units.base import LengthUnit


class MetersPerUnitLengthUnit(LengthUnit):
    """Generic unit defined by how many meters equal one unit (FR-6/FR-7)."""

    def __init__(self, name: str, meters_per_unit: float) -> None:
        self._name = name
        self._meters_per_unit = meters_per_unit

    @property
    def name(self) -> str:
        return self._name

    def to_meter(self, value: float) -> float:
        return value * self._meters_per_unit

    def from_meter(self, meters: float) -> float:
        return meters / self._meters_per_unit
