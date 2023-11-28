#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
lDigit = abs(i) % 10
if i < 0:
    lDigit = -lDigit
if lDigit > 5:
    print(f"Last digit of {i} is {lDigit} and is greater than 5")
elif lDigit == 0:
    print(f"Last digit of {i} is {lDigit} and is 0")
else:
    print(f"Last digit of {i} is {lDigit} and is less than 6 and not 0")
