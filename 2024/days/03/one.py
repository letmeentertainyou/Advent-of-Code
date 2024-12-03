#!/bin/python3.10
"""
This was a pretty straight forward regex for the pattern mul(x, y) and then we just multiply x and y together.
"""
import re

from sys import argv


def solve(file: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)"
    answer = 0
    match = re.findall(pattern, file)

    if match:
        for pair in match:
            x = int(pair[0])
            y = int(pair[1])
            answer += x * y

    return answer


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read()

    print(solve(file))


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     161
# Answer:   170068701
# Rank:     4012
