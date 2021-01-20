#!/usr/bin/python3
""" Module implementing a single function read_file """


def read_file(filename=""):
    """ Reads a utf-8 text file and prints it to stdout

    Args:
        filename: a string representing the file name
    """
    if filename:
        with open(filename, "r", encoding="utf8") as f:
            print(f.read(), end="")
