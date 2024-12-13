#!/bin/python3.10
"""
This is my original brute force attempt before I learned that this problem was a system of equations. Overall I'm glad that I thought of a solution but this is awfully slow.
"""
import re

from sys import argv
from math import inf
from functools import cache


def find_min_tokens(line: list[tuple]):
    @cache
    def r(
        button: list[tuple],
        num_tokens: int,
        cur_x: int = 0,
        cur_y: int = 0,
        AP: int = 0,
        BP: int = 0,
    ):
        nonlocal min_num_tokens
        if num_tokens >= min_num_tokens:
            return
        if AP > 100 or BP > 100:
            return
        cur_x += button[0]
        cur_y += button[1]
        if (cur_x > PRIZE[0]) or (cur_y > PRIZE[1]):
            return

        if (cur_x == PRIZE[0]) and (cur_y == PRIZE[1]):
            if num_tokens < min_num_tokens:
                min_num_tokens = num_tokens

        r(A, num_tokens + 3, cur_x=cur_x, cur_y=cur_y, AP=AP + 1, BP=BP)
        r(B, num_tokens + 1, cur_x=cur_x, cur_y=cur_y, AP=AP, BP=BP + 1)

    A = line[0]
    B = line[1]
    PRIZE = line[2]
    min_num_tokens = inf
    r(A, 3, AP=1)
    r(B, 1, BP=1)
    return min_num_tokens


def solve(lines: list[tuple]) -> None:
    answer = 0
    for line in lines:
        res = find_min_tokens(line)
        if res < inf:
            answer += res
    print(answer)


def find_ints(line: str) -> tuple[int]:
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


# Test:     480
# Answer:   40369
# Rank:     .
