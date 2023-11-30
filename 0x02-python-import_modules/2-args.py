#!/usr/bin/python3
import sys

args = len(sys.argv)

for i in range(0, args):
    if args < 2:
        print("0 arguments")

    elif args == 2:
        print("{} argument: ".format(args), end="\n", "{}: {}".format(i, sys.argv[i])

    else:
        print("{} arguments: ".format(args), end="\n", "{}: {}".format(i, sys.argv[i])
