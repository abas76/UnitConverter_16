import pytest

from UnitConverter import run


def test_u_flow_02_meter_e2e_success(capsys):
    exit_code = run("meter:2.5")
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.count("2.5 meter =") == 3
    assert captured.err == ""


def test_u_in_04_invalid_format_message(capsys):
    exit_code = run("meter2.5")
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Invalid format. Use unit:value (ex: meter:2.5)" in captured.out


def test_u_in_05_invalid_number_message(capsys):
    exit_code = run("meter:abc")
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Invalid number: abc" in captured.out


def test_u_in_unknown_unit_message(capsys):
    exit_code = run("inch:5")
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Unknown unit: inch" in captured.out


def test_u_in_negative_value_message(capsys):
    exit_code = run("meter:-1")
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Negative value" in captured.out
