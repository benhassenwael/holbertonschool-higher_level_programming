#!/usr/bin/python3
"""
    A script that adds all arguments to a Python list,
    and then save them to a file
"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except:
    with open(filename, "a") as f:
        items = []

for arg in argv[1:]:
    items.append(arg)
save_to_json_file(items, filename)
