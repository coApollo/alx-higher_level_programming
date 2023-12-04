#!/usr/bin/python3

def multiple_returns(sentence):
    length = 0
    char_1 = None

    length = len(sentence)
    if (length > 0):
        char_1 = sentence[0]

    return (length, char_1)
