#!/bin/python3.10
"""
Given a list of arrays determine how many are safe using the following rules:
    The arrays must ascend or descend and cannot change direction.
    The difference between each number must be between 1 and 3.
"""
from sys import argv


def find_safe(line: list[int]) -> bool:
    # determine if the line ascends or descends
    s = sorted(line)
    if not ((line == s) or (line[::-1] == s)):
        return False

    for i, current in enumerate(line):
        # This avoids an index error.
        if i + 1 < len(line):
            diff = abs(current - line[i + 1])
            if not (1 <= diff <= 3):
                return False
    return True


def solve(lines) -> None:
    answer = 0
    for line in lines:
        if find_safe(line):
            answer += 1

    print(answer)


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    lines = []
    for x, line in enumerate(file):
        split_line = [*map(int, line.split(" "))]
        lines.append(split_line)

    solve(lines)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:         2
# Answer:       549
# Rank:         7197
