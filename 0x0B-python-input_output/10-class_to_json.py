#!/usr/bin/python3
"""Fx that returns the dict for JSON serialization of an object"""


def class_to_json(obj):
    """Definition of the class"""
    return(obj.__dict__)
