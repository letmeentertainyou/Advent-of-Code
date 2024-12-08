#!/bin/python3.10
"""

"""
import itertools as it
import re

from collections import Counter, defaultdict
from copy import deepcopy
from sys import argv


TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)

TOP_LEFT: complex = -1 + -1j
TOP_RIGHT: complex = -1 + 1j
BOTTOM_LEFT: complex = 1 + -1j
BOTTOM_RIGHT: complex = 1 + 1j
CORNERS: tuple[complex] = (TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT)

EDGES: tuple[complex] = CORNERS + SIDES

# If the edges need to be consecutive
CON_EDGES: tuple[complex] = (
    TOP_LEFT,
    TOP,
    TOP_RIGHT,
    RIGHT,
    BOTTOM_RIGHT,
    BOTTOM,
    BOTTOM_LEFT,
    LEFT,
)


def cabs(n: complex):
    """Complex abs for getting a slope without negative numbers. idk."""
    return complex(abs(n.real), abs(n.imag))


def clone_swap(a: list, x: int, y: int):
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


def solve(lines: list[str]) -> None:

    answer = 0

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())
        # file = tmpfile.read()
        # file = tmpfile.readlines()

    lines: list = []
    for x, line in enumerate(file):

        for y, char in enumerate(line):
            hash = complex(x, y)
            ...

    solve(lines)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     .
# Answer:   .
# Rank:     .
