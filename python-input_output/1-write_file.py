#!/usr/bin/python3
"""Writes a string to a text file using 'with'"""


def write_file(filename="", text=""):
    """Writes a string to a text file using 'with'"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
