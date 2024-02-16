#!/usr/bin/python3
"""Base module with class constructor"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A function that Writes JSON serialization of objects to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A function that returns a class instantied from a dictionary"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)

            else:
                new = cls(1)

            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """A function that returns a list of classes instantiated from JSON"""

        filename = str(cls.__name__) + ".json"
        try:

            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in list_dicts])

        except IOError:
            return ([])
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """A function that draws rectangles and squares"""

        import turtle
        import random

        turtle.title("Rectangles and Squares")
        turtle.bgcolor("black")
        turtle.hideturtle()

        for r in list_rectangles:
            turtle.penup()
            turtle.color("white")
            turtle.goto(r.x, r.y)
            turtle.pendown()
            turtle.forward(r.width)
            turtle.left(90)
            turtle.forward(r.height)
            turtle.left(90)
            turtle.forward(r.width)
            turtle.left(90)
            turtle.forward(r.height)
            turtle.left(90)

        for s in list_squares:
            turtle.penup()
            turtle.color("white")
            turtle.goto(s.x, s.y)
            turtle.pendown


if __name__ == "__main__":

    pass