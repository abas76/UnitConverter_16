import json
from pathlib import Path

import pytest

from src.app.application import create_registry, register_unit_definition
from src.entity.config_loader import load_registry_from_json
from src.entity.converter import convert_to_all_units


def test_fr6_load_units_from_json(tmp_path: Path):
    config = tmp_path / "units.json"
    config.write_text(
        json.dumps({"units": {"meter": 1.0, "feet": 0.3048, "yard": 0.9144}}),
        encoding="utf-8",
    )
    registry = load_registry_from_json(config)
    results = convert_to_all_units("meter", 1.0, registry)
    assert results["feet"] == pytest.approx(3.28084, rel=0.001)


def test_fr6_default_config_file_exists():
    config_path = Path("config/units.json")
    assert config_path.is_file()
    registry = create_registry(str(config_path))
    results = convert_to_all_units("meter", 2.5, registry)
    assert set(results.keys()) == {"meter", "feet", "yard"}


def test_fr7_register_cubit_dynamically():
    registry = create_registry(unit_definitions=["1 cubit = 0.4572 meter"])
    results = convert_to_all_units("cubit", 1.0, registry)
    assert results["meter"] == pytest.approx(0.4572)
    assert "cubit" in results


def test_fr7_register_via_helper():
    from src.entity.units.registry import create_default_registry

    registry = create_default_registry()
    register_unit_definition(registry, "1 cubit = 0.4572 meter")
    assert "cubit" in registry.supported_names
