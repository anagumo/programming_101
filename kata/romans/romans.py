from kata.common import predicate_functions
from typing import Tuple

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

def get_roman_values(arabic: int) -> str:
    """
    A pure compressor function that takes a number as input and returns a string.
    The output is the result to convert and concatenate each reminder of the input 
    to a roman key.
    """
    symbols = ""

    for key, value in romans.items():
        while arabic >= key:
            symbols = symbols + value
            arabic = arabic - key

    return symbols

def get_asterisk(arabic) -> str :
    """
    A pure convertor function that takes a number as input and returns a
    a string.
    """
    points = ""

    if arabic < 1000:
        points = POINT_SYMBOL
    else:
        points = POINT_SYMBOL * 2
    
    return points

def to_romans(arabic: int) -> str:
    """
    A pure conversor function that takes a number as input and returns
    a string. The output is the result to conver each significative value of
    the input to a roman key.
    Corner cases:
    - If the input is zero, the function should handle the error
    - If the input is an invalid string, the function should handle the error
    """
    romans = ""
    ARABIC_GREATER_THAN = int(arabic / POINT_VALUE)
    GREATER_THAN = 3999

    if predicate_functions.is_integer(arabic) or arabic != 0:
        if arabic > GREATER_THAN:
            symbols = get_roman_values(ARABIC_GREATER_THAN)
            romans = romans + symbols + get_asterisk(ARABIC_GREATER_THAN)
            arabic = arabic - ARABIC_GREATER_THAN * POINT_VALUE

        symbols = get_roman_values(arabic)
        romans = romans + symbols
    else:
        raise TypeError("The input is not a valid arabic number")

    return romans

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

def sum_romans(a:str, b: str) -> int:
    """
    A pure compressor function that takes two strings as input and
    returns the sum of them.
    """
    result = to_arabic(a) + to_arabic(b)
    return to_romans(result)
