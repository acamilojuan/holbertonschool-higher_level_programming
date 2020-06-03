#!/usr/bin/python3
"""Fx to inherite from other class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Use of class Rectangle"""

    def __init__(self, width, height):
        """Method to validate if args are int"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
