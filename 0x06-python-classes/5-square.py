#!/usr/bin/python3
"Empty class Square that defines a square"


class Square:
    """
    Class Square

    Attributes:
    size: Size of the square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Method to get a value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set a change in the value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Method to print the square with # character"""
        if self.__size == 0:
            print()
        for a in range(0, self.__size):
            print("#" * self.__size)
