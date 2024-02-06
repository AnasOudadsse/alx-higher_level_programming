#!/usr/bin/python3
"""defines a func that creates a obj froma json file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, mode='r') as f:
        data = json.load(f)
        return data
