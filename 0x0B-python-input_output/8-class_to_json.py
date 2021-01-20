#!/usr/bin/python3
""" Module implementing a single function class_to_json """


def class_to_json(obj):
    """ Returns the dictionary description with simple data
        structure for JSON serialization of an object

    Args:
        obj: an instance of a class

    Returns:
        dictionary description of given class instance
    """
    return dict(obj.__dict__)
