#!/usr/bin/python3
"""Fx to return True/False if obj is of class inherited from specific class"""


def inherits_from(obj, a_class):
    """Method to check if obj is a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
