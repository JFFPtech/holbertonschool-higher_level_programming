#!/usr/bin/python3
"""
This is the add_integer module.

This module has one function, add_integer().
"""


def add_integer(a, b=98):
    """Return the sum of two integers.

    a and b must be integers or floats, otherwise a TypeError
    exception is raised.

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)