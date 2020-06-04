#!/usr/bin/python3
"""Fx to write a str to UTF8 txt file n returns the number of chars written"""


def write_file(filename="", text=""):
    """Method to read and write the file
    Args: filename, xfile, text
    """
    with open(filename, mode='w', encoding="UTF8") as xfile:
        return xfile.write(text)
