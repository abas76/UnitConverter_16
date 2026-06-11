from src.entity.exceptions import InvalidFormatError, InvalidNumberError


def parse_unit_value(raw: str) -> tuple[str, float]:
    if ":" not in raw:
        raise InvalidFormatError(
            "Invalid format. Use unit:value (ex: meter:2.5)"
        )

    unit, value_str = raw.split(":", 1)
    try:
        value = float(value_str.replace(":", "."))
    except ValueError:
        raise InvalidNumberError(f"Invalid number: {value_str}") from None
    return unit, value
