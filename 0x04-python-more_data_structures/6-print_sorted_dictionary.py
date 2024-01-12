#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newDict = {}

    newDict = dict(sorted(a_dictionary.items()))

    for key, value in newDict.items():
        print(f"{key}: {value}")
