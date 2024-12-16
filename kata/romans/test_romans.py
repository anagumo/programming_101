from pytest import raises
import romans

def test_value_raises_type_error():
    with raises(TypeError):
        romans.to_romans("")
    
    with raises(TypeError):
        romans.to_romans("0")

    with raises(TypeError):
        romans.to_romans("zsh")

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

"""
============================================================================ test session starts =============================================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: keepcoding/programming_101
collected 5 items                                                                                                                                                            

kata/romans/test_romans.py .....

============================================================================= 5 passed in 0.01s ==============================================================================
"""

def _test_arabic_raises_value_error_when_greater_than_3999():
    with not raises(ValueError):
        romans.to_romans(4000)
    with not raises(ValueError):
        romans.to_romans(10550)
    with not raises(ValueError):
        romans.to_romans(980345)

def test_numbers_greater_than_3999_and_less_than_10000():
    assert romans.to_romans(4825) == "IV*DCCCXXV"
    assert romans.to_romans(6001) == "VI*I"
    assert romans.to_romans(9001) == "IX*I"

def test_numbers_greater_than_9999_and_less_than_100000():
    assert romans.to_romans(40825) == "XL**DCCCXXV"
    assert romans.to_romans(11001) == "XI**I"
    assert romans.to_romans(90001) == "XC**I"

def test_numbers_greater_than_99999_and_less_than_1000000():
    assert romans.to_romans(400825) == "CD***DCCCXXV"
    assert romans.to_romans(600001) == "DC***I"
    assert romans.to_romans(900001) == "CM***I"

"""
Convert a roman number into an arabic numbers list
"""
def test_convert_to_arabics_less_than_3999():
    assert romans.convert_to_arabics("VI") == [5,1]
    assert romans.convert_to_arabics("XCIX") == [10,100,1,10]
    assert romans.convert_to_arabics("MCMXXXIX") == [1000,100,1000,10,10,10,1,10]

def test_convert_to_arabics_greater_than_3999():
    assert romans.convert_to_arabics("IV*DCCCXXV") == [1,5,1000,500,100,100,100,10,10,5]
    assert romans.convert_to_arabics("VI*I") == [5,1,1000,1]
    assert romans.convert_to_arabics("IX*I") == [1,10,1000,1]

# TODO: Implement math expresions, ej.: simplify_romans("CD + IX") -> CDIX
def _test_simplify_romans():
    assert romans.simplify_romans("CD + IX") == "CDIX"
    assert romans.simplify_romans("CD - IX") == "CCCXCI"
    assert romans.simplify_romans("CD * IX") == "MMMDC"

"""
============================================================================ test session starts =============================================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0
rootdir: keepcoding/programming_101
collected 8 items                                                                                                                                                            

kata/romans/test_romans.py .....FFF

================================================================================== FAILURES ==================================================================================
______________________________________________________________________ test_thousands_greater_than_3999 ______________________________________________________________________

    def test_thousands_greater_than_3999():
>       assert romans.to_romans(4001) == "IV*I"
E       AssertionError: assert 'MMMMI' == 'IV*I'
E         
E         - IV*I
E         + MMMMI

kata/romans/test_romans.py:47: AssertionError
_______________________________________________________________________________ test_to_arabic _______________________________________________________________________________

    def test_to_arabic():
>       assert romans.to_romans("VI") == 6

kata/romans/test_romans.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

arabic_number = 'VI'

    def to_romans(arabic_number) -> list[int]:
        roman_values = ""
        arabic_reminder = arabic_number
    
        if predicate_functions.is_integer(arabic_number) or arabic_number != 0:
            for key, value in romans.items():
>               while arabic_reminder >= key:
E               TypeError: '>=' not supported between instances of 'str' and 'int'

kata/romans/romans.py:35: TypeError
____________________________________________________________________________ test_simplify_romans ____________________________________________________________________________

    def test_simplify_romans():
>       assert romans.simplify_romans("CD + IX") == "CDIX"
E       AttributeError: module 'romans' has no attribute 'simplify_romans'

kata/romans/test_romans.py:59: AttributeError
========================================================================== short test summary info ===========================================================================
FAILED kata/romans/test_romans.py::test_thousands_greater_than_3999 - AssertionError: assert 'MMMMI' == 'IV*I'
FAILED kata/romans/test_romans.py::test_to_arabic - TypeError: '>=' not supported between instances of 'str' and 'int'
FAILED kata/romans/test_romans.py::test_simplify_romans - AttributeError: module 'romans' has no attribute 'simplify_romans'
======================================================================== 3 failed, 5 passed in 0.04s =========================================================================
"""