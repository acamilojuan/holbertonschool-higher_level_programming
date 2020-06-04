#!/usr/bin/python3
"""Fx to read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Method to read a UTF8 text file and print it"""
    with open(filename, encoding="UTF8") as xfile:
        for line in xfile:
            print(line, end="")
