from collections.abc import Callable

from src.boundary.exceptions import InputGridNotConfiguredError


class CliInputReader:
    """Reads raw unit:value input from a configured grid or stdin."""

    def __init__(
        self,
        input_grid: list[str] | None = None,
        stdin_reader: Callable[[str], str] | None = None,
    ) -> None:
        self._input_grid = input_grid
        self._stdin_reader = stdin_reader

    def read(self) -> str:
        if self._input_grid is None:
            raise InputGridNotConfiguredError("Input grid not configured")
        return self._input_grid[0]

    def read_from_stdin(self, prompt: str = "Insert value for converting (ex: meter:2.5): ") -> str:
        if self._stdin_reader is None:
            raise InputGridNotConfiguredError("Stdin reader not configured")
        return self._stdin_reader(prompt).strip()
