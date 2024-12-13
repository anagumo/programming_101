from kata.common import predicate_functions

"""
to_romans(arabics: list[int])
Sample input/output: 1939 -> MCMXXXIX

Instructions:
1. Convert the number into a list where each element is a valid key
from romans dictionary: to_romans(number)
2. Compress the number list into a string where each element is a Roman numeral
"""

"""
Structure data that includes the significant roman symbols
"""
romans = {
    1000:'M',
    900:'CM', 500:'D', 400:'CD', 100:'C',
    90:'XC', 50:'L', 40:'XL', 10:'X', 
    9:'IX', 5:'V', 4:'IV', 1:'I'
}

def to_romans(arabic_number) -> list[int]:
    """
    A pure conversor function that takes a number as input and returns
    a string.
    Corner cases:
    - If the input is zero, the function should return and empty list
    """
    roman_values = ""
    arabic_reminder = arabic_number

    if predicate_functions.is_integer(arabic_number) or arabic_number != 0:
        for key, value in romans.items():
            while arabic_reminder >= key:
                arabic_reminder = arabic_reminder - key
                roman_values = roman_values + value
    else:
        raise TypeError("The input is not a valid arabic number")

    return roman_values