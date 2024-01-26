#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{} {}{}".format(num_args, "argument" if num_args == 1 else "arguments", ":" if num_args > 0 else "."))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))

