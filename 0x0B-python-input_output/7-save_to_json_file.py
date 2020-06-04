#!/usr/bin/python3
"""Fx to write an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Method to write the obj
    Args: my_obj, filename.
    Note: json.dumps() converts a Python obj to JSON string and writes.
    """
    with open(filename, mode='w', encoding="UTF8") as xfile:
        json.dump(my_obj, xfile)
