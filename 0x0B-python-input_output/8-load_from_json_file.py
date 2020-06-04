#!/usr/bin/python3
"""Fx to create an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """Method to open
    Arg: filename, xfile.
    """
    with open(filename, encoding="utf-8") as xfile:
        return json.load(xfile)
