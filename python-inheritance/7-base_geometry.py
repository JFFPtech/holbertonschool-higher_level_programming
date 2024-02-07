#!/usr/bin/python3
"""Module for BaseGeometry class.
Added define area method, returns error.
"""


class BaseGeometry:
    """A class with a define area method."""
    def area(self):
        """Method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
