#!/usr/bin/python3
""" Module implementing a single function inherits_from """


def inherits_from(obj, a_class):
    """ Return if obj is axactly an instance of a_class or not """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
