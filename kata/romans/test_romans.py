from pytest import raises
import romans

"""
Convert from arabic to roman
"""
def test_value_raises_type_error():
    with raises(romans.RomanNumberError) as context:
        romans.to_romans("")
    assert str(context.value).endswith("is not a valid number")

    with raises(romans.RomanNumberError):
        romans.to_romans("0")
    assert str(context.value).endswith("is not a valid number")

    with raises(romans.RomanNumberError):
        romans.to_romans("zsh")
    assert str(context.value).endswith("is not a valid number")

def test_units():
    assert romans.to_romans(3) == "III"
    assert romans.to_romans(6) == "VI"
    assert romans.to_romans(9) == "IX"

def test_tens():
    assert romans.to_romans(12) == "XII"
    assert romans.to_romans(74) == "LXXIV"
    assert romans.to_romans(99) == "XCIX"

def test_hundreds():
    assert romans.to_romans(123) == "CXXIII"
    assert romans.to_romans(483) == "CDLXXXIII"
    assert romans.to_romans(900) == "CM"

def test_thousands_less_than_3999():
    assert romans.to_romans(1001) == "MI"
    assert romans.to_romans(1323) == "MCCCXXIII"
    assert romans.to_romans(1939) == "MCMXXXIX"

def _test_arabic_raises_value_error_when_greater_than_3999():
    with not raises(ValueError):
        romans.to_romans(4000)
    with not raises(ValueError):
        romans.to_romans(10550)
    with not raises(ValueError):
        romans.to_romans(980345)

def test_numbers_greater_than_3999_and_less_than_1000000():
    assert romans.to_romans(4825) == "IV*DCCCXXV"
    assert romans.to_romans(6001) == "VI*I"
    assert romans.to_romans(9001) == "IX*I"

    assert romans.to_romans(40825) == "XL*DCCCXXV"
    assert romans.to_romans(11001) == "XI*I"
    assert romans.to_romans(90001) == "XC*I"

    assert romans.to_romans(400825) == "CD*DCCCXXV"
    assert romans.to_romans(600001) == "DC*I"
    assert romans.to_romans(900001) == "CM*I"

"""
Convert from roman to arabic
"""
def test_convert_to_arabic_digits_less_than_3999():
    assert romans.to_arabic_list("VI") == [5,1]
    assert romans.to_arabic_list("XCIX") == [10,100,1,10]
    assert romans.to_arabic_list("MMMCMXCIX") == [1000,1000,1000,100,1000,10,100,1,10]

def test_convert_to_arabic_digits_greater_than_3999():
    assert romans.to_arabic_list("IV*DCCCXXV") == [1,5,0,500,100,100,100,10,10,5]
    assert romans.to_arabic_list("VI*I") == [5,1,0,1]
    assert romans.to_arabic_list("IX*I") == [1,10,0,1]

def test_to_arabic_less_than_3999():
    assert romans.to_arabic("VI") == 6
    assert romans.to_arabic("XCIX") == 99
    assert romans.to_arabic("MMMCMXCIX") == 3999

def test_to_arabic_greater_than_3999_less_than_100000():
    assert romans.to_arabic("IV*CMXXI") == 4921
    assert romans.to_arabic("XV*CCXXIII") == 15223
    assert romans.to_arabic("XC*CMXCIX") == 90999

def test_to_arabic_greater_than_999999():
    assert romans.to_arabic("VI**DCCCXXV") == 6000825
    assert romans.to_arabic("IV**I") == 4000001
    assert romans.to_arabic("IX**I") == 9000001

"""
Sum of romans
"""
def test_sum_romans():
    assert romans.sum_romans("CD", "IX") == "CDIX"
    assert romans.sum_romans("CM", "MCCXXIX") == "MMCXXIX"
    assert romans.sum_romans("IV*XXXIX", "MCXXIX") == "V*CLXVIII"