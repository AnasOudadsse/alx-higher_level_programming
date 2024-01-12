def search_replace(my_list, search, replace):
    newList = []

    for number in my_list:
        if (number != search):
            newList.append(number)
        else:
            newList.append(replace)
    return newList
