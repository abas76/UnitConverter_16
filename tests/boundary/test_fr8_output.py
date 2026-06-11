import json

from UnitConverter import run


def test_fr8_table_format_default(capsys):
    exit_code = run("meter:2.5", output_format="table")
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.count("2.5 meter =") == 3


def test_fr8_json_format(capsys):
    exit_code = run("meter:2.5", output_format="json")
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = json.loads(captured.out)
    assert payload["input"] == {"unit": "meter", "value": 2.5}
    assert set(payload["results"].keys()) == {"meter", "feet", "yard"}


def test_fr8_csv_format(capsys):
    exit_code = run("meter:2.5", output_format="csv")
    captured = capsys.readouterr()

    assert exit_code == 0
    lines = captured.out.strip().splitlines()
    assert lines[0] == "source_unit,source_value,unit,value"
    assert len(lines) == 4
