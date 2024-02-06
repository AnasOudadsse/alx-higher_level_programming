#!/usr/bin/python3
"""defines a string object to json"""
import json


def to_json_string(my_obj):
    """convert a string obj to json"""
    return json.dumps(my_obj)
