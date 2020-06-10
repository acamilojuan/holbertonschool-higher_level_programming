#!/usr/bin/python3
"""Class Square creation"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square creation that inherits from Class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
