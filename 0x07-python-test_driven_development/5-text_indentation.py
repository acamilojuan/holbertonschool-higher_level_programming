#!/usr/bin/python3
"""Fx to print a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Method to indent
    Args: text, str, tmp, chars, char
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = [".", "?", ":"]
    tmp = "."
    for char in text:
        if char is " " and tmp in chars:
            continue
        print(char, end="")
        if char in chars:
            print("\n")
        tmp = char
