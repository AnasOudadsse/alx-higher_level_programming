#!/usr/bin/python3
"""defines a json to string function"""
import json


def from_json_string(my_str):
    """convert a json to string(python) """
    return json.loads(my_str)
