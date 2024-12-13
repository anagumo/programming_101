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