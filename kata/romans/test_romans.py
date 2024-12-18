from pytest import raises
from romans import to_romans, to_arabic, is_valid_repetition, RomanNumberError

"""
Convert from arabic to roman test
"""
def test_value_raises_type_error():
    with raises(RomanNumberError) as context:
        to_romans("")
    assert str(context.value).endswith("is not a valid number")

    with raises(RomanNumberError):
        to_romans("0")
    assert str(context.value).endswith("is not a valid number")

    with raises(RomanNumberError):
        to_romans("zsh")
    assert str(context.value).endswith("is not a valid number")

def test_units():
    assert to_romans(3) == "III"
    assert to_romans(6) == "VI"
    assert to_romans(9) == "IX"

def test_tens():
    assert to_romans(12) == "XII"
    assert to_romans(74) == "LXXIV"
    assert to_romans(99) == "XCIX"

def test_hundreds():
    assert to_romans(123) == "CXXIII"
    assert to_romans(483) == "CDLXXXIII"
    assert to_romans(900) == "CM"

def test_thousands_less_than_3999():
    assert to_romans(1001) == "MI"
    assert to_romans(1323) == "MCCCXXIII"
    assert to_romans(1939) == "MCMXXXIX"

def _test_arabic_raises_value_error_when_greater_than_3999():
    with not raises(ValueError):
        to_romans(4000)
    with not raises(ValueError):
        to_romans(10550)
    with not raises(ValueError):
        to_romans(980345)

def test_numbers_greater_than_3999_and_less_than_1000000():
    assert to_romans(4825) == "IV*DCCCXXV"
    assert to_romans(6001) == "VI*I"
    assert to_romans(9001) == "IX*I"

    assert to_romans(40825) == "XL*DCCCXXV"
    assert to_romans(11001) == "XI*I"
    assert to_romans(90001) == "XC*I"

    assert to_romans(400825) == "CD*DCCCXXV"
    assert to_romans(600001) == "DC*I"
    assert to_romans(900001) == "CM*I"

"""
Convert from roman to arabic tests
"""
def test_to_arabic_less_than_3999():
    assert to_arabic("VI") == 6
    assert to_arabic("XCIX") == 99
    assert to_arabic("MMMCMXCIX") == 3999

def test_to_arabic_greater_than_3999_less_than_100000():
    assert to_arabic("IV*CMXXI") == 4921
    assert to_arabic("XV*CCXXIII") == 15223
    assert to_arabic("XC*CMXCIX") == 90999

def test_to_arabic_greater_than_999999():
    assert to_arabic("VI**DCCCXXV") == 6000825
    assert to_arabic("IV**I") == 4000001
    assert to_arabic("IX**I") == 9000001

def test_invalid_roman_symbols():
    with raises(RomanNumberError) as context:
        to_arabic("ASDF")
    assert str(context.value).endswith("is not a valid roman symbol")

def test_more_than_3_repeat():
    assert not is_valid_repetition("IIII")
    assert not is_valid_repetition("DD")
    assert not is_valid_repetition("CMCCCCVV")

    """with raises(RomanNumberError) as context:
        is_valid_repetition("I","I")
    assert str(context.value).endswith("can be repeated more than 3 times")

    with raises(RomanNumberError) as context:
        is_valid_repetition("VV")
    assert str(context.value).endswith("can be repeated more than 1 time")

    with raises(RomanNumberError) as context:
        is_valid_repetition("DDCCCC")
    assert str(context.value).endswith("can be repeated more than specified times")"""