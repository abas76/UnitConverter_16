import pytest

from src.boundary.cli_input import CliInputReader
from src.boundary.exceptions import InputGridNotConfiguredError


def test_u_in_01_grid_none_raises_e003():
    reader = CliInputReader(input_grid=None)
    with pytest.raises(InputGridNotConfiguredError) as exc_info:
        reader.read()
    assert exc_info.value.code == "E003"


def test_u_in_02_feet_input_read_from_grid():
    reader = CliInputReader(input_grid=["feet:8.2"])
    assert reader.read() == "feet:8.2"


def test_u_in_03_yard_input_read_from_grid():
    reader = CliInputReader(input_grid=["yard:3"])
    assert reader.read() == "yard:3"
