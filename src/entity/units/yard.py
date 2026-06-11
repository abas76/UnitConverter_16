from src.entity.constants import METER_TO_YARD
from src.entity.units.base import LengthUnit


class YardUnit(LengthUnit):
    @property
    def name(self) -> str:
        return "yard"

    def to_meter(self, value: float) -> float:
        return value / METER_TO_YARD

    def from_meter(self, meters: float) -> float:
        return meters * METER_TO_YARD
