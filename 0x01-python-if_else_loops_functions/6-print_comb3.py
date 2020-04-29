#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range((number + 1), 10):
        if number != number2:
            print("{}".format(number), end="")
            print("{}, ".format(number2), end="")
            if number == 8 and number2 == 9:
                print("{}{}".format(number, number2))
