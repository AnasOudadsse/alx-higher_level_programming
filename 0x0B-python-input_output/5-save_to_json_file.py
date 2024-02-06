#!/usr/bin/python3
"""defines a func that writes an obj to a file using json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text file, using a JSON"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
