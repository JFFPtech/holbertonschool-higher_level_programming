#!/usr/bin/python3
number = 0
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))
    number += 1
