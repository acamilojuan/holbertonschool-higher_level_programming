#!/usr/bin/python3
"""Class base creation"""


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
