#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str = "{:d}"
    for i in my_list:
        print(str.format(i))
