import pytest
from strring_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("startswith, removeprefix", [
    (" skypro", "skypro"),
    (" 1234567", "1234567"),
    (" 04/09 2020", "04/09 2020"),
])
def test_trim_positive(startswith, removeprefix):
    assert string_utils.trim(startswith) == removeprefix


@pytest.mark.negative
@pytest.mark.parametrize("startswith, removeprefix", [
    ("", ""),
    ("   ", ""),
    ("  04/09 2020", "04/09 2020"),
])
def test_trim_negative(startswith, removeprefix):
    assert string_utils.trim(startswith) == removeprefix


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", True),
    ("1234567", "7", True),
    (" 04/09 2020", "9", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "S", False),
    (" ", "7", False),
    ("Skypro", "q", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("I'm", "'m", "I"),
    ("do noteing", "eing", "do not"),
    ("understand(", "(", "understand"),
    ("&???!!", "&???!", "!")
])
def test_delete_symbol_positive(utils, input_string, symbol, expected_output):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("", "", ""),
    (" ", " ", ""),
    ("12345", "", "12345")
])
def test_delete_symbol_negative(utils, input_string, symbol, expected_output):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected_output
