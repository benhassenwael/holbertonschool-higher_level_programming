#!/usr/bin/python3
""" Module implementing a single function add_attribute """


def add_attribute(obj, name, value):
    """ adds a new attribute to an object if it's possible

    Args:
        obj: the object to add the attribute to
        name: name of the attribute to add
        vlaue: the value of the added attribute

    Raises:
        TypeError: if the given object can't have a new attribute
    """
    if ("__dict__" in obj.__dir__()):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
