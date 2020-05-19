#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    aux = 0
    for a in range(0, list_length):
        try:
            aux = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            aux = 0
        except ZeroDivisionError:
            print("division by 0")
            aux = 0
        except IndexError:
            print("out of range")
            aux = 0
        finally:
            new_list.append(aux)
    return new_list
