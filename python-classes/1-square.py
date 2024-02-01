#!/usr/bin/python3
"""Square class.

Contains class that defines a square, with initialization of size.

"""


class Square:
    """Defines a square."""
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
