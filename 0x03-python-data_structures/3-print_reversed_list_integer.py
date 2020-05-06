#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    else:
        for a in range(0, len(my_list)):
            my_list = my_list[::-1]
            print("{:d}".format(my_list[a]))
