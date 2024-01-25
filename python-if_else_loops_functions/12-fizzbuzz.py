#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:  # ? check for multiples of 15 first
            print("FizzBuzz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        else:  # ? if not a multiple of 3 or 5, print the number
            print(f"{i} ", end="")
