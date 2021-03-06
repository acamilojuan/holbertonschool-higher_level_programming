#!/usr/bin/python3
"""Class Rectangle creation"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Class Base
    Attributes: self, width, height, x, y and id.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Method to return the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Method to display char # in stdout"""
        for a in range(self.__y):
            print()
        for a in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Method to update the values of the instances"""
        list1 = ["id", "width", "height", "x", "y"]
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, list1[arg], args[arg])

    def to_dictionary(self):
        """Method to return the dictionary representation of a Rectangle"""
        return dict(x=self.__x, y=self.__y, id=self.id,
                    height=self.__height, width=self.__width)
