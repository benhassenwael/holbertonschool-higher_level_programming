#!/usr/bin/python3
""" Module implementing a single function from_json_string """
import json


def from_json_string(my_str):
    """ Return an object represented by a JSON string

    Args:
        my_str: JSON string to decode into an object

    Returns:
        Object
    """
    return json.loads(my_str)
