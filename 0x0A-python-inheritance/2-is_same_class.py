#!/usr/bin/python3
""" Module implementing a single function is_same_class """


def is_same_class(obj, a_class):
    """ Return if obj is axactly an instance of a_class or not """
    return type(obj) is a_class
