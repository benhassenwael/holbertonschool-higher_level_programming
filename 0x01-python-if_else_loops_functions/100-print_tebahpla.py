#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        x = 122
    else:
        x = 90
    print(chr(x - i), end='')
