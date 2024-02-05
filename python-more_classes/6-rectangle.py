#!/usr/bin/python3
"""
Module for Rectangle class.
Added a private instance attribute: width and height.
Added area and perimeter methods.
Added __str__ method, returning a string representation of the rectangle.
Added __repr__ method, returning a different representation of the rectangle.
Added __del__ method, printing a message for every deletion of a rectangle.
Added a public class attribute: number_of_instances, initialized to 0.
"""

class Rectangle:
    """A class representing a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0, area=0, perimeter=0):
        
        """Adds 1 to the number of instances"""
        type(self).number_of_instances += 1 
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
    
    def area(self):
        """area: returns the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """perimeter: returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @classmethod
    def __del__(cls):
        """Decrements number of instances.
        Print a message for every deletion of a rectangle"""
        cls.number_of_instances -= 1
        print("Bye rectangle...")
