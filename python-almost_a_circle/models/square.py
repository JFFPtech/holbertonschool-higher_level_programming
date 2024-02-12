#!/usr/bin/python3
"""Square module with inherited Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
