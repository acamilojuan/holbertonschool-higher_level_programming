#!/usr/bin/python3
"""Creation of class Student that defines a student"""


class Student:
    """Class def"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that rerieves a dict representation of a Student instance"""
        return(self.__dict__)
