#!/usr/bin/python3
import sys


def sum(numbers):
    sum_total = 0
    for n in numbers:
        sum_total += int(n)
    return sum_total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(0)
    else:
        numbers = sys.argv[1:]
        result = sum(numbers)
        print(result)
