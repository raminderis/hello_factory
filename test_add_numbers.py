import builtins
from io import StringIO
import sys
import pytest

from main import add_numbers, get_positive_integer, main


# -----------------------------
# Tests for add_numbers()
# -----------------------------

def test_add_numbers_valid():
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 20) == 30


def test_add_numbers_invalid_type():
    with pytest.raises(ValueError):
        add_numbers("a", 5)

    with pytest.raises(ValueError):
        add_numbers(5, None)


def test_add_numbers_invalid_value():
    with pytest.raises(ValueError):
        add_numbers(-1, 5)

    with pytest.raises(ValueError):
        add_numbers(5, 0)


# -----------------------------
# Tests for get_positive_integer()
# -----------------------------

def test_get_positive_integer_valid(monkeypatch):
    # Simulate user entering "5"
    monkeypatch.setattr(builtins, "input", lambda _: "5")
    assert get_positive_integer("Enter: ") == 5


def test_get_positive_integer_retry(monkeypatch, capsys):
    # Simulate invalid input then valid input
    inputs = iter(["-1", "abc", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    result = get_positive_integer("Enter: ")
    assert result == 3

    captured = capsys.readouterr()
    assert "positive integer" in captured.out.lower()
    assert "invalid input" in captured.out.lower()


# -----------------------------
# Integration test for main()
# -----------------------------

def test_main_integration(monkeypatch, capsys):
    # Simulate two valid inputs: 4 and 6
    inputs = iter(["4", "6"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Capture stdout
    main()

    output = capsys.readouterr().out.lower()

    # Check key phrases
    assert "positive integer addition" in output
    assert "4 + 6 = 10" in output