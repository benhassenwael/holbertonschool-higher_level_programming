#!/usr/bin/python3
""" Module implementing a single function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file using JSON representation

    Args:
        my_obj: Object to wirite as a JSON in a file
        filename: file to write into
    """
    with open(filename, "w", encoding="utf8") as f:
        f.write(json.dumps(my_obj))
