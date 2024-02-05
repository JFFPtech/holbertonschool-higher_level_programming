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
    
    def width(self):
        """width: get width"""
        return self.__width
    @property
    def width(self):
        """width: set width"""
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
