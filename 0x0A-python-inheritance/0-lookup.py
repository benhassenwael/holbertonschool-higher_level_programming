#!/usr/bin/python3
""" Module implementing a single function lookup """


def lookup(obj):
    """ Return the list of available attributes and methods of obj """
    return dir(obj)
