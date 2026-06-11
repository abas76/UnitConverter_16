class InvalidFormatError(ValueError):
    """Raised when input is not in unit:value format."""


class InvalidNumberError(ValueError):
    """Raised when the value part is not a valid number."""


class UnknownUnitError(ValueError):
    """Raised when the unit is not supported."""


class NegativeValueError(ValueError):
    """Raised when the value is negative."""
