#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    my_list.copy()
    if idx < 0 or (idx > (len(my_list) - 1)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
