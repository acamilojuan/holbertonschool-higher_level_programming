#!/usr/bin/python3
"""Fx to append a str at the end of a text file"""


def append_write(filename="", text=""):
    """Method to open and append a str
    Args: filename, text, xfile
    """
    with open(filename, mode='a', encoding="UTF8") as xfile:
        return xfile.write(text)
