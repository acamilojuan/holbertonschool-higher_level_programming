#!/usr/bin/python3
"""Fx to read n lines of a UTF8 text file and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """Method to open the file and read it
    Args: filename, nb_lines
    """
    with open(filename, encoding="UTF8") as xfile:
        if nb_lines > 0:
            for a in range(nb_lines):
                print(xfile.readline(), end='')
        else:
            print(xfile.read(), end='')
