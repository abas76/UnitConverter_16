from src.entity.units.registry import DEFAULT_REGISTRY, UnitRegistry


def to_meter_base(unit: str, value: float, registry: UnitRegistry = DEFAULT_REGISTRY) -> float:
    return registry.get(unit).to_meter(value)


def from_meter_base(meters: float, registry: UnitRegistry = DEFAULT_REGISTRY) -> dict[str, float]:
    return {u.name: u.from_meter(meters) for u in registry.all_units()}


def convert_to_all_units(
    unit: str, value: float, registry: UnitRegistry = DEFAULT_REGISTRY
) -> dict[str, float]:
    meters = to_meter_base(unit, value, registry)
    return from_meter_base(meters, registry)
