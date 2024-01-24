#!/usr/bin/python3
word = "Holberton"  # [startting point : ending point]
word_first_3 = word[:3]  # positive = start from beginning
word_last_2 = word[-2:]  # negative = start from end
middle_word = word[1:-1]  # eliminate first an lats letters
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
