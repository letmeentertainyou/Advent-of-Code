#!/bin/python3.10
"""
Sort the lists and sum the differences from left to right.
"""
from sys import argv


def solve(lefts, rights):
    lefts.sort()
    rights.sort()

    answer = 0
    for i in range(len(lefts)):
        answer += abs(lefts[i] - rights[i])

    print(answer)


def parse_input(filename: str) -> tuple:
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


# Test:      11
# Answer:    2086478
# Rank:      14499
