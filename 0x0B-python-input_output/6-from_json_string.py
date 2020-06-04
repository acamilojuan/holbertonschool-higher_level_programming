#!/usr/bin/python3
"""Fx to return an object (Python data struct) represented by a JSON string"""

import json


def from_json_string(my_str):
    """Method to use the JSON rep
    Arg: my_str
    """
    return json.loads(my_str)
