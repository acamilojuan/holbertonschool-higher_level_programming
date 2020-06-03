#!/usr/bin/python3
"""Script to check area"""


class BaseGeometry:

    def area(self):
        """Method to raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to check values"""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
