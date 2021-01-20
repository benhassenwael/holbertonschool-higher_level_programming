#!/usr/bin/python3
""" Module implementing a single function to_json_string """
import json


def to_json_string(my_obj):
    """ Return the JSON representation of an object

    Args:
        my_obj: object to get its representation as JSON

    Returns:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
