#!/bin/usr/python3
"""Square class.

Contains class that defines a square, with initialization of size.
Checks if the values are right. Included area method to return the area of the square.

"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes the size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
    @property
    def size(self):
        """Returns the current square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
