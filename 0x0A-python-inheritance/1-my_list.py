#!/usr/bin/python3
""" define an inherit class that inherits from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints the list sorted in a ascending order"""
        print(sorted(self))
