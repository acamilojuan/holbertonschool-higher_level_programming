#!/usr/bin/python3
"Function to define a Rectangle and change its values"


class Rectangle:
    """
    Class Rectangle

    Attributes:
    width: Width of the rectangle
    height: height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        if self.width == 0 or self.height == 0:
            return string
        for a in range(self.height - 1):
            string += (self.print_symbol * self.width) + "\n"
        string += (self.print_symbol * self.width)
        return string

    def __repr__(self):
        """Method to print values of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method to delete the instances and print a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
