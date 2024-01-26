#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args_text = "argument" if num_args == 1 else "arguments"
    punctuation = ":" if num_args > 0 else "."

    print("{} {}{}".format(num_args, args_text, punctuation))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
