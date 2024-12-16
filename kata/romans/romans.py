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
    9:'IX', 5:'V', 4:'IV', 1:'I'
}

def get_points_when_greater_than_3999(arabic):
    points = ""
    if arabic < 10:
        points = '*'
    elif arabic < 100:
        points = '**'
    elif arabic < 1000:
        points = '***'
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


def convert_to_arabics(roman_str: str) -> list [int]:
    """
    A pure conversor function that takes a string as input and returns a list
    of numbers where each element is the conversion from roman symbol to arabic number.
    Corner cases:
    - If the input is an empty string, the function should return an empty list.
    - If the input is an invalid str, the function should handle the error.
    """
    arabic_list = []
    
    for roman_symbol in roman_str:
        for roman_key, roman_value in romans.items():
            if roman_symbol == roman_value:
                arabic_list.append(roman_key)
            elif roman_symbol == "*":
                arabic_list.append(1000)
                break
    return arabic_list