#!/usr/bin/python3
"""Base module with class constructor
"""


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
        """Writes the JSON string representation of list_objs to a file"""
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))
    
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new
    
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                
                list_instances = []

                for d in list_dicts:
                    list_instances.append(cls.create(**d))
                return list_instances
        except FileNotFoundError:
            return []


if __name__ == "__main__":

    pass