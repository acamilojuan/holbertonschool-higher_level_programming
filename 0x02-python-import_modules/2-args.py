#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        numberzero = len(sys.argv) - 1
        print("{} arguments.".format(numberzero))
    elif len(sys.argv) == 2:
        numberone = len(sys.argv) - 1
        print("{} argument:".format(numberone))
        print("1: {}".format(sys.argv[1]))
    else:
        others = len(sys.argv) - 1
        print("{} arguments:".format(others))
        for n in range(1, len(sys.argv)):
            print("{}: {}".format(n, sys.argv[n]))
