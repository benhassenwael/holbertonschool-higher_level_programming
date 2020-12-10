#!/usr/bin/python3
import sys

if __name__ == "__main__":
    res = 0
    for elem in sys.argv[1:]:
        res += int(elem)
    print(res)
