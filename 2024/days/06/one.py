#!/bin/python3.10
"""
I was really happy with my ideas for part one but I got absoluter ruined by part two so nevermind.
"""
from sys import argv

TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: list[complex] = [TOP, RIGHT, BOTTOM, LEFT]


def rotate(dir: complex) -> complex:
    index = (SIDES.index(dir) + 1) % len(SIDES)
    return SIDES[index]


def step_forward(data: dict, pos: complex, dir: complex) -> tuple:
    new_pos: complex = pos + dir

    if new_pos in data:
        if data[new_pos] == "#":
            return step_forward(data, pos, rotate(dir))

        return new_pos, dir
    return "", None


def solve(data: dict, start: complex) -> None:
    visited: set = set()
    dir: complex = TOP
    pos: complex = start

    while True:
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            break
        visited.add(pos)

    print(len(visited))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    data: dict = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash: complex = complex(x, y)
            if char == "^":
                pos = hash
            data[hash] = char

    solve(data, pos)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     41
# Answer:   4656
# Rank:     11564
