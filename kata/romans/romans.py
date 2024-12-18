from kata.common import predicate_functions

class RomanNumberError(Exception):
    pass

"""
Structure data that includes the significant roman symbols
"""
romans_for_symbol = {
    '*':0,
    'I':1, 'IV':4, 'V':5, 'IX':9,
    'X':10, 'XL':40, 'L':50, 'XC':90,
    'C':100, 'CD':400, 'D':500, 'CM':900,
    'M':1000
}
romans_for_arabic = {
    1000:'M',
    900:'CM', 500:'D', 400:'CD', 100:'C',
    90:'XC', 50:'L', 40:'XL', 10:'X',
    9:'IX', 5:'V', 4:'IV', 1:'I'
}

"""
to_romans(number: int)
Sample input/output: 1939 -> "MCMXXXIX"

Instructions:
1. Convert the number into a list where each element is a valid key
from romans dictionary: to_romans(number)
2. Compress the number list into a string where each element is a Roman numeral
"""

def get_roman_values(arabic: int) -> str:
    """
    A pure compressor function that takes a number as input and returns a string.
    The output is the result to convert and concatenate each reminder of the input 
    to a roman key.
    """
    symbols = ""

    for key, value in romans_for_arabic.items():
        while arabic >= key:
            symbols = symbols + value
            arabic = arabic - key

    return symbols

def to_romans(input: int) -> str:
    """
    A pure conversor function that takes a number as input and returns
    a string. The output is the result to conver each significative value of
    the input to a roman key.
    Corner cases:
    - If the input is zero, the function should handle the error
    - If the input is an invalid string, the function should handle the error
    """
    roman_symbols = ""
    GREATER_THAN = 3999
    M_VALUE = romans_for_symbol.get('M')
    num_points = lambda num: '*' if num < M_VALUE else '*' * 2
    
    if predicate_functions.is_integer(input):
        arabic = int(input)
        if arabic > 0:
            arabic_thousand = int(arabic / M_VALUE)
            if arabic > GREATER_THAN:
                symbols = get_roman_values(arabic_thousand)
                roman_symbols = roman_symbols + symbols + num_points(arabic_thousand)
                arabic = arabic - arabic_thousand * M_VALUE
            symbols = get_roman_values(arabic)
            roman_symbols = roman_symbols + symbols
        else:
            raise RomanNumberError(f"{input} is not a valid number")
    else:
        raise RomanNumberError(f"{input} is not a valid number")

    return roman_symbols

"""
to_arabic(roman: str)
Sample input/output: "MCMXXXIX" -> 1939

Instructions:
1. Convert the number into a list where each element is a valid key
from romans dictionary: to_romans(number)
2. Compress the number list into a string where each element is a Roman numeral
"""

def is_valid_repetition(roman: str):
    invalid_repetitions = {
        4: ['I','X','C','M'],
        2: ['V','L','D']
    }
    prev_char = ""
    char_counter = 0
    is_valid_repetition = True

    for char in roman:
        if prev_char == char:
            char_counter = char_counter + 1
            repeated_symbols = invalid_repetitions.get(char_counter)
            if repeated_symbols != None and char in repeated_symbols:
                is_valid_repetition = False
                break
        else:
            char_counter = 1
        
        prev_char = char
    
    return is_valid_repetition, char_counter - 1

def to_arabic(roman: str) -> int:
    """
    Pure compress function that takes a str as input and returns an
    int. The string is the representation of a roman number and the function
    should converted to an arabic one, uses: convert_to_arabics()
    Corner cases:
    - If the input is an empty string, the function should return zero
    - If the input is an invalid roman value, the function should handle the error
    """
    prev_value = 0
    compression = 0

    is_valid, symbol_limit = is_valid_repetition(roman)
    if not is_valid:
        raise RomanNumberError(f"{roman} can be repeated more than {symbol_limit} times")

    for char in roman:
        roman_value = romans_for_symbol.get(char)

        if roman_value == None:
            raise RomanNumberError(f"{roman_value} is not a valid roman symbol")
        elif roman_value == romans_for_symbol.get('*'):
            compression = compression * romans_for_symbol.get('M')
        elif prev_value >= roman_value:
            compression = compression + roman_value
        else:
            compression = compression + (roman_value - prev_value * 2)

        prev_value = roman_value
    
    return compression