#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary representation of a Student"""
        return self.__dict__
