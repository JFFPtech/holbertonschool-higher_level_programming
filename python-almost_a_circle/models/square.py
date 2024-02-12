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

    def update(self, *args, **kwargs):
        """Updates the class"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """Returns the dictionary representation of the class"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Returns the string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
