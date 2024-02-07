#!/usr/bin/python3
"""Module for BaseGeometry class.
Added define area method, returns error.
"""


class BaseGeometry:
    """A class with a define area method."""
    def area(self):
        """Method that raises an exception."""
        raise Exception("area() is not implemented")
