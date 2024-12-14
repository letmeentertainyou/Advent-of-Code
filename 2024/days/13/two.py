#!/bin/python3.10
"""
Well this one was pretty hard because I didn't recognize it as a system of equations and I
also didn't know how to solve a system of equations in Python. Hopefully I will recognize this
type of question in the future.

I absolutely hate how these past few days haven't had an example answer for part two, it makes
it very hard to know where I am wrong when I am blindly guessing in the wind.
"""
import re

from sys import argv


def find_min_tokens(line: list[tuple]):
    x = line[0]
    y = line[1]
    z = [n + 10000000000000 for n in line[2]]
    b: float = (z[1] * x[0] - z[0] * x[1]) / (y[1] * x[0] - y[0] * x[1])
    a: float = (z[0] - b * y[0]) / x[0]

    if a.is_integer() and b.is_integer():
        return int(a * 3 + b)

    return 0


def solve(lines: list[tuple]) -> None:
    answer = 0
    for line in lines:
        answer += find_min_tokens(line)

    print(answer)


def find_ints(line: str) -> list[int]:
    return tuple(int(n) for n in re.findall(r"\d+", line))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")

    lines: list = []
    for i in range(0, len(file), 4):
        lines.append(
            (
                find_ints(file[i]),
                find_ints(file[i + 1]),
                find_ints(file[i + 2]),
            )
        )
    solve(lines)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     875318608908
# Answer:   72587986598368
# Rank:     6824
