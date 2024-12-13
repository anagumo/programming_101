from pytest import raises
import romans

def test_invalid_input():
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
rootdir: /keepcoding/programming_101
collected 5 items                                                                                                                                                            

kata/romans/test_romans.py .....

============================================================================= 5 passed in 0.01s ==============================================================================
"""

# TODO: Support arabic numbers greater than 3999
def _test_thousands_greater_than_3999():
    assert romans.to_romans(4001) == "IV*I"
    assert romans.to_romans(8231) == "VIII*CCXXXI"
    assert romans.to_romans(10330) == "X*CCCXXX"
    
"""
================================================================================== FAILURES ==================================================================================
______________________________________________________________________ test_thousands_greater_than_3999 ______________________________________________________________________

    def test_thousands_greater_than_3999():
>       assert romans.to_romans(4001) == "IV*I"
E       AssertionError: assert 'MMMMI' == 'IV*I'
E         
E         - IV*I
E         + MMMMI

kata/romans/test_romans.py:47: AssertionError
========================================================================== short test summary info ===========================================================================
FAILED kata/romans/test_romans.py::test_thousands_greater_than_3999 - AssertionError: assert 'MMMMI' == 'IV*I'
======================================================================== 1 failed, 5 passed in 0.05s =========================================================================
"""

# TODO: Implement romans to arabic numbers conversion, ej.: to_arabic(MCMXXXIX) -> 1939
def _to_arabic():
    assert romans.to_romans("VI") == 6
    assert romans.to_romans("XCIX") == 99
    assert romans.to_arabic("MCMXXXIX") == 1939

# TODO: Implement math expresions, ej.: simplify_romans(["CD", "IX"], operation) -> CDIX
def _calculate_romans():
    assert romans.simplify_romans("CD + IX") == "CDIX"
    assert romans.simplify_romans("CD - IX") == "CCCXCI"
    assert romans.simplify_romans("CD * IX") == "MMMDC"