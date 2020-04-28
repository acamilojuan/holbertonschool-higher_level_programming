#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positive_num = number * -1
    modul = (positive_num % 10) * -1
else:
    modul = number % 10
if modul > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, modul))
elif modul == 0:
    print("Last digit of {} is {} and is 0".format(number, modul))
else:
    print("Last digit of", number, "is", modul, "and is less than 6 and not 0")
