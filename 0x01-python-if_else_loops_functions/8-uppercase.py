#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        if i < 123 and i > 96:
            c = chr(i - 32)
        print("{}".format(c), end='')
    print('\n', end='')
