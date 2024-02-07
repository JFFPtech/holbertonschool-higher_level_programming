#!/usr/bin/python3
"""Module for is_same_class method."""
def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a class."""
    return type(obj) is a_class
