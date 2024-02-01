#!/usr/bin/python3
"""Square class.

This is a empty class that defines a square.

"""


class Square:
    """Defines a square."""
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
