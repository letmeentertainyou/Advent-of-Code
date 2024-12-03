#!/bin/python3.10
"""
Iterate through left list and for each number multiply it by the number of times it appears in the right list.
Then sum that result. This involves taking a counter of the right list.
"""

from collections import Counter
from sys import argv


def solve(lefts, rights):
    right_count = Counter(rights)

    answer = 0
    for i in lefts:
        answer += i * right_count[i]

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()
    lefts, rights = [], []

    for x, line in enumerate(file):
        left, right = line.split()
        lefts.append(int(left))
        rights.append(int(right))

    solve(lefts, rights)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:      31
# Answer:    24941624
# Rank:      13590
