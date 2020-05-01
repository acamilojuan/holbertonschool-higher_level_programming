#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    for a in range(0, len(dir(hidden_4))):
            if (((dir(hidden_4))[a])[0]) != "_":
                print((dir(hidden_4))[a])
