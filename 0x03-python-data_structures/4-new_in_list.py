#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = []

    for i in range(length):
        new_list.append(my_list[i])

    if (idx < 0 or idx > length):
        return (new_list)

    else:
        new_list[idx] = element
        return (new_list)
