#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    counter = 0

    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                counter += 1
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
    print("")
    return counter
