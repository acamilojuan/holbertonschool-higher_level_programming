#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        numberzero = len(sys.argv) - 1
        print("{}".format(numberzero))
    elif len(sys.argv) > 1:
        number = 0
        for n in range(1, len(sys.argv)):
            number += int(sys.argv[n])
        print("{}".format(number))
