#!/usr/bin/python3
""""Appends a string to a text file using 'with'"""


def append_write(filename="", text=""):
    """Appends a string to a text file using 'with'"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
