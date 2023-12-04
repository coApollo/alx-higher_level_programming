#!/usr/bin/python3

def max_integer(my_list=[]):
    max_1 = -1

    if (my_list):
        for item in my_list:
            if (item > max_1):
                max_1 = item
        return (max_1)
    return (None)
