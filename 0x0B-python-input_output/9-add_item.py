#!/usr/bin/python3
"""Fx to add all arguments to a Python list, and save them to a file"""

import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """Method to add the arguments and print"""
    filename = "add_item.json"

    if os.path.isfile(filename):
        list1 = load_from_json_file(filename)
        list1 += sys.argv[1:]
        save_to_json_file(list(list1), filename)
    else:
        save_to_json_file(list(sys.argv[1:]), filename)
