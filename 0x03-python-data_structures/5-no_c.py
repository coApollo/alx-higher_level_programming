#!/usr/bin/python3

def no_c(my_string):
    new_s = ''.join([char for char in my_string if char not in ['C', 'c']])
    return (new_s)
