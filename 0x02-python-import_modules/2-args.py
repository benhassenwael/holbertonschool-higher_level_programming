#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    i = 1
    for elem in sys.argv[1:]:
        print("{}: {}".format(i, elem))
        i += 1
