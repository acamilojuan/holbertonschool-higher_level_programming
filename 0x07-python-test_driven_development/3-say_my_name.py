#!/usr/bin/python3
"Function to print to strings"


def say_my_name(first_name, last_name=""):
    """Arguments
    first_name: Str1 Name
    last_name: Str2 Last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
