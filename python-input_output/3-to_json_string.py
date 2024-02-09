#!/usr/bin/python3
"""Converts a Python object to a JSON string"""


import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string"""
    return json.dumps(my_obj)
