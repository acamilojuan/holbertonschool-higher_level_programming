#!/usr/bin/python3
"""Script to check area"""


class BaseGeometry:
    """Using the class"""
    def area(self):
        """Method to raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to check values
        Args: Value and Name
        Return: Raises errors
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
