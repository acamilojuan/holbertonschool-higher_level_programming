#!/usr/bin/python3
"""Fx to return True/False depends if obj is an instance of the class or not"""


def is_same_class(obj, a_class):
    """Method to compare
    Args: obj and a_class
    Returns: True if obj is of the class, False if not.
    """
    return type(obj) is a_class
