import json
from pathlib import Path

from src.entity.units.ratio_unit import MetersPerUnitLengthUnit
from src.entity.units.registry import UnitRegistry


def load_registry_from_json(config_path: str | Path) -> UnitRegistry:
    path = Path(config_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    units = data.get("units", data)
    registry = UnitRegistry()
    for name, meters_per_unit in units.items():
        registry.register(MetersPerUnitLengthUnit(name, float(meters_per_unit)))
    return registry
