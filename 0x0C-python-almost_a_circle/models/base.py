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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to use Json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to write the string rep in a file
        Args: list_objs, cls.
        Note: json.dumps() converts a Python obj to JSON string and writes
        """
        name = cls.__name__ + '.json'
        emptylist = []
        for elem in list_objs:
            aux = cls.to_dictionary(elem)
            emptylist.append(aux)
        with open(name, mode='w', encoding="utf-8") as xfile:
            xfile.write(cls.to_json_string(emptylist))
