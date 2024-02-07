#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """Custom list type intended to only contain integers."""


    def print_sorted(self):
        """Prints MyList lists in ascending order by value. """


        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
