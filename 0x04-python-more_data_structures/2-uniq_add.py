#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = []
    result = 0

    newList.append(my_list[0])
    for number in range(1, len(my_list)):
        if (my_list[number] not in newList):
            newList.append(my_list[number])
    for i in newList:
        result += i
    return result
