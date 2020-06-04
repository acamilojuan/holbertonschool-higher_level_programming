#!/usr/bin/python3
"""Fx to return the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Method to use Json rep
    Arg: my_obj
    """
    return json.dumps(my_obj)
