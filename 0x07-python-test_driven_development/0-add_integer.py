#!/usr/bin/python3
"""
task 0 integer addition
a and b must be integers or floats,
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """ A function that adds 2 integers
    a and b must be casted to integers if they are float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
