import csv
import io
import json


def _display_value(value: float) -> str:
    rounded = round(value, 1)
    if rounded == int(rounded):
        return str(int(rounded))
    return str(rounded)


def format_table(source_unit: str, source_value: float, results: dict[str, float]) -> str:
    unit_order = ("meter", "feet", "yard")
    ordered = [u for u in unit_order if u in results]
    ordered.extend(u for u in results if u not in unit_order)
    lines = [
        f"{_display_value(source_value)} {source_unit} = {_display_value(results[u])} {u}"
        for u in ordered
    ]
    return "\n".join(lines)


def format_json(source_unit: str, source_value: float, results: dict[str, float]) -> str:
    payload = {
        "input": {"unit": source_unit, "value": source_value},
        "results": results,
    }
    return json.dumps(payload, indent=2)


def format_csv(source_unit: str, source_value: float, results: dict[str, float]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["source_unit", "source_value", "unit", "value"])
    for unit, value in results.items():
        writer.writerow([source_unit, source_value, unit, value])
    return buffer.getvalue().strip()


def format_output(
    source_unit: str,
    source_value: float,
    results: dict[str, float],
    output_format: str = "table",
) -> str:
    if output_format == "json":
        return format_json(source_unit, source_value, results)
    if output_format == "csv":
        return format_csv(source_unit, source_value, results)
    return format_table(source_unit, source_value, results)
