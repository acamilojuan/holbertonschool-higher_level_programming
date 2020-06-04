#!/usr/bin/python3
"""Fx to return the number of lines of a text file"""


def number_of_lines(filename=""):
    """Method to return the number of lines
    Args: filename, xfile
    """
    number = 0
    with open(filename, encoding="UTF8") as xfile:
        for a in xfile:
            number += 1
    return(number)
