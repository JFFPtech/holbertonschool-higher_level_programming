#!/usr/bin/python3
"""
Text indentation module.

This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to print.

    Returns:
        None.

    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
