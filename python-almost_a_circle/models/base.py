#!/usr/bin/python3
"""Base module with class constructor
"""


__nb_objects = 0

class Base:
  """Base class
  """

def __init__(self, id=None):
    """Initializes the class
    """
    if id is not None:
        self.id = id
    else:
        global __nb_objects
        __nb_objects += 1
        self.id = __nb_objects
