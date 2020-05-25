#!/usr/bin/python3
"Function to define a Rectangle and change its values"


class Rectangle:
    """
    Class Rectangle

    Attributes:
    width: Width of the rectangle
    height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializing attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Decorator that works as a getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set a new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to set a new value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return the value of the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to return the value of the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to return a string with character #"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for a in range(self.height - 1):
            string += ("#" * self.width) + "\n"
        string += ("#" * self.width)
        return string
