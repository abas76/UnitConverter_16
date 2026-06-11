from src.entity.constants import METER_TO_FEET
from src.entity.units.base import LengthUnit


class FeetUnit(LengthUnit):
    @property
    def name(self) -> str:
        return "feet"

    def to_meter(self, value: float) -> float:
        return value / METER_TO_FEET

    def from_meter(self, meters: float) -> float:
        return meters * METER_TO_FEET
