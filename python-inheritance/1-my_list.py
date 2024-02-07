#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A class that inherits from a list""
    def print_sorted(self):
        """Prints the list, but sorted."""
        print_list = self[:]
        print_list.sort()
        print(print_list)
