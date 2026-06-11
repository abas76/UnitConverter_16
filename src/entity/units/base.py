from abc import ABC, abstractmethod


class LengthUnit(ABC):
    """Single responsibility: one length unit's meter-base conversion."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def to_meter(self, value: float) -> float:
        ...

    @abstractmethod
    def from_meter(self, meters: float) -> float:
        ...
