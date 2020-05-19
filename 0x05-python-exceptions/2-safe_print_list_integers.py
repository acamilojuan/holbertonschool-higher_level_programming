#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            b += 1
        except (TypeError, ValueError):
            pass
    print()
    return b
