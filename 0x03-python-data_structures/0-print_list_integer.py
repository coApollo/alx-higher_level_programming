#!/usr/bin/python3
def print_list_integer(my_list=[]):
    lists = len(my_list)
    for (i in range(lists)):
        print("{:d}".format(my_list[i]))
