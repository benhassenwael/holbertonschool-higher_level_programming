#!/usr/bin/python3
""" Module implementing a single function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Return if obj is axactly an instance of a_class or not """
    return isinstance(obj, a_class)
