#!/usr/bin/python3
"""Class base creation"""
import json


class Base:
    """Class Base
    Attributes: self, id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Method to use Json"""
        if list_dictionaries is None or not bool(list_dictionaries):
            return("[]")
        else:
            return json.dumps(list_dictionaries)
