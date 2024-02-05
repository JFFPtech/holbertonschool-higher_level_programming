#!/usr/bin/python3
"""
Module for Rectangle class.
Added a private instance attribute: width and height.
"""

class Rectangle:
    """A class representing a rectangle."""
    def __init__(self, width=0, height=0):
        """The class constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value