#!/usr/bin/python3
"Empty class Square that defines a square"


class Square:
    """
    Class Square

    Attributes:
    size: Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value in the position"""
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
            
    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Method to print the square with # character"""
        if self.__size == 0:
            print()
        else:
            for a in range(0, self.__position[1]):
                print()
            for a in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
