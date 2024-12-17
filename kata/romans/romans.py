from kata.common import predicate_functions
import re

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
    9:'IX', 5:'V', 4:'IV', 1:'I',
}
POINT_SYMBOL = "*"
POINT_VALUE = 1000

def get_points_when_greater_than_3999(arabic):
    points = ""
    if arabic < 1000:
        points = POINT_SYMBOL * 1
    else:
        points = POINT_SYMBOL * 2
    return points

def to_romans(arabic_number: int) -> list[int]:
    """
    A pure conversor function that takes a number as input and returns
    a string.
    Corner cases:
    - If the input is zero, the function should return and empty list
    """
    
    roman_values = ""
    arabic_reminder = arabic_number
    symplify_arabic = int(arabic_number / 1000)
    arabic_subreminder = int(arabic_number / 1000)
    grater_than = 3999

    if predicate_functions.is_integer(arabic_number) or arabic_number != 0:
        for key, value in romans.items():
            while arabic_reminder >= key:
                if arabic_reminder > grater_than:
                    for sub_key, sub_value in romans.items():
                        while arabic_subreminder >= sub_key:
                            roman_values = roman_values + sub_value
                            arabic_subreminder = arabic_subreminder - sub_key
                    roman_values = roman_values + get_points_when_greater_than_3999(symplify_arabic)
                    arabic_reminder = arabic_reminder - (symplify_arabic * 1000)
                else:
                    roman_values = roman_values + value
                    arabic_reminder = arabic_reminder - key
    else:
        raise TypeError("The input is not a valid arabic number")

    return roman_values

def to_arabic_digits(roman: str) -> list [int]:
    """
    A pure conversor function that takes a string as input and returns a list
    of numbers where each element is the conversion from roman symbol to arabic number.
    Corner cases:
    - If the input is an empty string, the function should return an empty list.
    - If the input is an invalid str, the function should handle the error.
    """
    arabic_list = []
    
    for symbol in roman:
        for roman_key, roman_value in romans.items():
            if symbol == roman_value:
                arabic_list.append(roman_key)
            elif symbol == POINT_SYMBOL:
                arabic_list.append(0)
                break
    return arabic_list

def to_arabic(roman: str) -> int:
    """
    Pure compress function that takes a str as input and returns an
    int. The string is the representation of a roman number and the function
    should converted to an arabic one, uses: convert_to_arabics()
    Corner cases:
    - If the input is an empty string, the function should return zero
    - If the input is an invalid roman value, the function should handle the error
    """
    arabic_digits = to_arabic_digits(roman)
    prev_value = 0
    compression = 0

    for arabic in arabic_digits:
        if arabic == 0:
            compression = compression * POINT_VALUE
        if prev_value >= arabic:
            compression = compression + arabic
        else:
            compression = compression + (arabic - prev_value * 2)
    
        prev_value = arabic
    
    return compression