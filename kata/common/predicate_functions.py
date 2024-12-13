
def is_integer(input_text:str) -> bool:
    """
    Predicate function that takes a string as input and checks if it is a
    postive integer.
    Corner cases:
    - If the input is not a number, the function should handle the error.
    """
    is_integer: False

    try:
        int(input_text)
        is_integer = True
    except:
        is_integer = False
    return is_integer