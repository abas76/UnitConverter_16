import argparse
import sys
from collections.abc import Callable

from src.app.application import create_registry
from src.boundary.cli_input import CliInputReader
from src.boundary.output_formatter import format_output
from src.entity.exceptions import (
    InvalidFormatError,
    InvalidNumberError,
    NegativeValueError,
    UnknownUnitError,
)
from src.usecase.converter_service import format_error_message, process_conversion


def run(
    raw_input: str | None = None,
    *,
    config_path: str | None = None,
    unit_definitions: list[str] | None = None,
    output_format: str = "table",
    stdin_reader: Callable[[str], str] | None = None,
) -> int:
    registry = create_registry(config_path, unit_definitions)

    if raw_input is None:
        reader = CliInputReader(stdin_reader=stdin_reader or input)
        try:
            raw_input = reader.read_from_stdin()
        except Exception as exc:
            print(format_error_message(exc))
            return 1

    try:
        unit, value, results = process_conversion(raw_input, registry)
        print(format_output(unit, value, results, output_format))
        return 0
    except (InvalidFormatError, InvalidNumberError, UnknownUnitError, NegativeValueError) as exc:
        print(format_error_message(exc))
        return 1


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unit Converter CLI")
    parser.add_argument(
        "--config",
        help="Path to JSON unit configuration (FR-6)",
    )
    parser.add_argument(
        "--register",
        action="append",
        dest="registrations",
        metavar="DEF",
        help='Dynamic unit registration, e.g. "1 cubit = 0.4572 meter" (FR-7)',
    )
    parser.add_argument(
        "--format",
        choices=("table", "json", "csv"),
        default="table",
        help="Output format (FR-8)",
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Optional unit:value input (non-interactive)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    return run(
        raw_input=args.input,
        config_path=args.config,
        unit_definitions=args.registrations,
        output_format=args.format,
    )


if __name__ == "__main__":
    sys.exit(main())
