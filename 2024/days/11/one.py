#!/bin/python3.10
"""
I should have known that such an easy part one was a trap. I could technically just
publish the part two solution for part one but I've left my original brute force for
context.
"""

from sys import argv


def match_rules(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    s = str(stone)
    if len(s) % 2 == 0:
        i = len(s) // 2
        left = int(s[:i])
        right = int(s[i:])
        return [left, right]

    return [stone * 2024]


def solve(stones: list[str]) -> None:
    num_of_blinks: int = 25
    old = stones

    for _ in range(num_of_blinks):
        res = []
        for stone in old:
            res.extend(match_rules(int(stone)))
        old = res

    print(len(res))


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


# Test:     55312
# Answer:   187738
# Rank:     3608
