#!/usr/bin/python3
import sys

if (__name__ == "__main__"):
    argc = len(sys.argv)
    count = 1
    add = 0

    for i in range(count, argc, 1):
        add += int(sys.argv[i])
        count += 1

    print("{}".format(add))
