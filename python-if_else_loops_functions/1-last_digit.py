#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
sign = "negative" if number < 0 else "positive"

if last_digit > 5:
    comparison = "greater than 5"
elif last_digit == 0:
    comparison = "0"
else:
    comparison = "less than 6 and not 0"

print(f"Last digit of {sign} number {number} is {last_digit} and is {comparison}")
