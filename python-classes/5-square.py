#!/usr/bin/python3
"""Square class.

Contains class that defines a square, with initialization of size.

Checks if the values are right, with setter and getter methods.
Included area method to return the area of the square and print.

"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes the size."""
        self.size = size

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

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
