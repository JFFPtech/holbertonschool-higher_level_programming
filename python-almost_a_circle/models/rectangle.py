#!/usr/bin/python3
"""Rectangle module with inherited Base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value
    
    @property
    def height(self):
        """Getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value