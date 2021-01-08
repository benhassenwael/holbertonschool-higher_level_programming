#!/usr/bin/python3
""" This module contains a single function
    for the purpose of practecing doctests """


def add_integer(a, b=98):
    """ Addition of two integers

    Args:
        a: first integer
        b: second integer (default: 98)

    Returns:
        the sum of 'a' and 'b' as integers

    Raises:
        TypeError: if any of the args is not an int or a float
    """
    if (
            type(a) is not int and
            type(a) is not float
            ):
        raise TypeError("a must be an integer")
    if (
            type(b) is not int and
            type(b) is not float
            ):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
