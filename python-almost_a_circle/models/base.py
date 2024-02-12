#!/usr/bin/python3
"""Base module with class constructor
"""


__nb_objects = 0

def __init__(self, id=None):
    """Initializes an instance"""
    if id is not None:
        self.id = id
    else:
        global __nb_objects
        __nb_objects += 1
        self.id = __nb_objects
