#!/usr/bin/python3
"Function to return the add of teo integers"


def add_integer(a, b=98):
    """Arguments:
    a = Type integer
    b = Type integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('NaN') or type(b) is float('NaN'):
        raise ValueError("cannot convert float infinity to integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
