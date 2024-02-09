#!/usr/bin/python3
"""Converts a class to a JSON object"""


def class_to_json(obj):
    """Converts a class to a JSON object"""
    return obj.__dict__
