#!/usr/bin/python3
""" This module contains a single function
    for the purpose of practecing doctests """


def print_square(size):
    """ prints a square with the character '#'

    Args:
        size: positive integer, the size of the square to print

    Raises:
        TypeError: if 'size' is not an integer
        ValueError: if 'size' is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
