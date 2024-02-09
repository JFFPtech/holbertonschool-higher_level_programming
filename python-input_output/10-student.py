#!/usr/bin/python3
"""Defines a student"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
            
    def to_json(self, attrs=None):
        """Gets the dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict
