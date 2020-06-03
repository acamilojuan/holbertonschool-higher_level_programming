#!/usr/bin/python3
"""Script to create a class that inherits from a list"""


class MyList(list):
    """Creation class Mylist"""
    def print_sorted(self):
        """Method to print the info of the class sorted"""
        print(sorted(self))
