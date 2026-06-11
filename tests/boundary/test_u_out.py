from src.boundary.output_formatter import format_output
from src.entity.converter import convert_to_all_units


def test_u_out_01_meter_input_produces_three_table_lines(capsys):
    from UnitConverter import run

    exit_code = run("meter:2.5")
    captured = capsys.readouterr()

    assert exit_code == 0
    lines = [line for line in captured.out.strip().splitlines() if line]
    assert len(lines) == 3
    assert all("2.5 meter =" in line for line in lines)
    assert any("feet" in line for line in lines)
    assert any("yard" in line for line in lines)


def test_u_out_01_formatter_matches_prd_shape():
    results = convert_to_all_units("meter", 2.5)
    output = format_output("meter", 2.5, results, "table")
    lines = output.splitlines()
    assert len(lines) == 3
    assert lines[0].startswith("2.5 meter =")
    assert "feet" in lines[1]
    assert "yard" in lines[2]
