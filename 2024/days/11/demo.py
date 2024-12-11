#!/bin/python3.10
"""

"""
from sys import argv


def match_rules(stone: str):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        i = len(stone) // 2
        left = stone[:i]
        right = str(int(stone[i:]))

        return [left, right]
    return [str(int(stone) * 2024)]


def solve(stones: list[str]) -> None:

    num_of_blinks: int = 25
    print(stones)
    old = stones
    for n in range(num_of_blinks):
        res = []
        for stone in old:
            res.extend(match_rules(stone))
        old = res
        # print(res)
    print(len(res))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split(" ")
        # file = tmpfile.read()

    solve(file)
    # solve(file)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     55312
# Answer:   187738
# Rank:     .
