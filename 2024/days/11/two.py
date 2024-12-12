#!/bin/python3.10
"""
I wish I could claim I solved this one alone but I didn't recognize the problem as a cache problem. I know how to recognize problems that need modulus for big numbers but I was baffled here.
"""
from functools import cache
from sys import argv


# @cache
def match_rules(stone: int, count: int = 0) -> int:
    if count == 75:
        return 1

    count += 1
    if stone == 0:
        return match_rules(1, count)
    s = str(stone)

    if len(s) % 2 == 0:
        i = len(s) // 2
        left = int(s[:i])
        right = int(s[i:])
        return match_rules(left, count) + match_rules(right, count)

    return match_rules(stone * 2024, count)


def solve(stones: list[str]) -> None:
    answer = 0

    for stone in stones:
        answer += match_rules(int(stone))

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split(" ")

    solve(file)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     65601038650482  TEST ANSWER NOT PROVIDED
# Answer:   223767210249237
# Rank:     5997
