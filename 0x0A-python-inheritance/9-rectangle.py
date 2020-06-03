#!/usr/bin/python3
"""Script to create class Rectangle that inherits from class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class creation"""

    def __init__(self, width, height):
        """Method to validate if args are int"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """Method to print the string"""
        return "[Rectangle] {}/{}".format(self._width, self._height)
