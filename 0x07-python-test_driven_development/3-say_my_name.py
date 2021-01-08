#!/usr/bin/python3
""" This module contains a single function
    for the purpose of practecing doctests """


def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>"

    Args:
        first_name: string
        last_name: string (default empty string)

    Raises:
        TypeError: if any of the args is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
