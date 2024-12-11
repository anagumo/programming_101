import common_functions

"""
to_romans(arabics: list[int])
Sample input/output: 1939 -> MCMXXXIX

Instructions:
1. Convert the number into a list where each element is a valid key
from romans dictionary: to_romans_keys(number)
2. Compress the number list into a string where each element is a Roman numeral
"""

"""
Dictionary structured in base 10 that includes the significant roman symbols
"""
romans = {
    1000:'M',
    900:'CM', 500:'D', 400:'CD', 100:'C',
    90:'XC', 50:'L', 40:'XL', 10:'X', 
    9:'IX', 5:'V', 4:'IV', 1:'I'
}

def to_romans_from(arabic_number) -> list[int]:
    """
    A pure conversor function that takes a number as input and returns
    a string. 
    Corner cases:
    - If the input is zero, the function should return and empty list
    """
    roman_values = ""
    arabic_reminder = arabic_number

    while arabic_reminder > 0:
        for key, value in romans.items():
            if arabic_reminder >= key: 
                arabic_reminder = arabic_reminder - key
                roman_values = roman_values + value
                break
        
    return roman_values

def to_romans_from(roman_keys: list[int]) -> str:
    """
    A pure compressor function that takes a number as input and returns 
    a string. Every remider of the number is converted to a roman numeral 
    and its concatenated into the string.
    Corner cases:
    - If the input is an empty list, the function should return an empty string
    """
    roman_values = ""

    for roman_key in roman_keys:
        roman_values = roman_values + romans[roman_key]
        
    return roman_values