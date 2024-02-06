#!/usr/bin/python3
"""
Module for Rectangle class.
Added a private instance attribute: width and height.
Added area and perimeter methods.
Added __str__ method, returning a string representation of the rectangle.
Added __repr__ method, returning a different representation of the rectangle.
Added __del__ method, printing a message for every deletion of a rectangle.
Added a public class attribute: number_of_instances, initialized to 0.
Added public class attribute: print_symbol, initialized to #
Added staticmethod bigger_or_equal, returns biggest rectangle based on area.
"""


class Rectangle:
    """A class representing a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, area=0, perimeter=0):

        """Adds 1 to the number of instances"""
        type(self).number_of_instances += 1
        """The class constructor"""
        self.width = width
        self.height = height

    def __del__(self):
        """Decrements number of instances.
        Print a message for every deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

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

    def _draw_rectangle(self):
        """Draws the rectangle"""
        for i in range(self.height):
            print("{}".format(self.print_symbol) * self.width)

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    @classmethod
    def __del__(cls):
        """Decrements number of instances.
        Print a message for every deletion of a rectangle"""
        cls.number_of_instances -= 1
        print("Bye rectangle...")
