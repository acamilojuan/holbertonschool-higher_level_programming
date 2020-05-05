#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for a in range(0, len(my_list)):
        b = len(my_list) - (len(my_list) + 1 + a)
        print("{:d}".format(my_list[b]))
