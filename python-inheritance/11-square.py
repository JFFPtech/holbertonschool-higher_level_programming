#!/usr/bin/python3
"""Module for Square class that inherits rom Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class."""
    def __init__(self, size):
        """Instantiation with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the following square description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
