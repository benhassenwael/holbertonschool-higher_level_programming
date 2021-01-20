#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys


def print_status(file_size, status):
    """ Print file size and status code """
    print("File size: {:d}".format(file_size))
    for code in sorted(status.keys()):
        if status[code]:
            print("{:d}: {:d}".format(code, status[code]))

file_size = 0
status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
         }
try:
    for i, line in enumerate(sys.stdin, 1):
        line = line.split()
        file_size += int(line[-1])
        status[line[-2]] += 1
        if i % 10 == 0:
            print_status(file_size, status)
except KeyboardInterrupt:
    print_status(file_size, status)
    raise
