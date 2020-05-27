#!/usr/bin/python3
"""Slots usage"""


class LockedClass(object):
    """Class"""
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """Init"""
        self.first_name = first_name
