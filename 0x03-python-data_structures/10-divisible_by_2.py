#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = my_list.copy()
    for numb in range(0, len(my_list)):
        if my_list[numb] % 2 > 0:
            new_list[numb] = False
        else:
            new_list[numb] = True
    return new_list
