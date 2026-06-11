from src.entity.units.base import LengthUnit


class MeterUnit(LengthUnit):
    @property
    def name(self) -> str:
        return "meter"

    def to_meter(self, value: float) -> float:
        return value

    def from_meter(self, meters: float) -> float:
        return meters
