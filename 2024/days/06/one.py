#!/bin/python3.10
"""
I was really happy with my ideas for part one but I got absoluter ruined by part 2 so nevermind.
"""
from sys import argv

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
SIDES: list[tuple] = [UP, RIGHT, DOWN, LEFT]


def hash(x: int, y: int) -> str:
    return f"{x}:{y}"


def rotate(dir: tuple):
    index = (SIDES.index(dir) + 1) % len(SIDES)
    return SIDES[index]


def step_forward(data: dict, pos: str, dir: tuple):
    x, y = [int(i) for i in dir]
    X, Y = [int(i) for i in pos.split(":")]
    X += x
    Y += y
    new_pos = hash(str(X), str(Y))
    if new_pos in data:
        if data[new_pos] == "#":
            return step_forward(data, pos, rotate(dir))

        return new_pos, dir
    return "", None


def solve(data: dict, pos: str) -> None:
    visited = set()
    dir = UP
    while True:
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            break
        visited.add(pos)

    print(len(visited))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    data = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            h = hash(x, y)
            if char == "^":
                pos = h
            data[h] = char

    solve(data, pos)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# my code is off by one.
# Test:     41
# Answer:   4656
# Rank:     11564
