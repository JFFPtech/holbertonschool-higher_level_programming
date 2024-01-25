#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # ord(0 is used to tget the unicode of the character)
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
