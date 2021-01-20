#!/usr/bin/python3
""" Module implementing a single function load_from_json_file """
import json


def load_from_json_file(filename):
    """ Creates an Object from a JSON file

    Args:
        filename: file to read JSON from
    """
    with open(filename, "r", encoding="utf8") as f:
        return json.loads(f.read())
