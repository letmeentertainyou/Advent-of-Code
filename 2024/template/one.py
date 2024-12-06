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
SIDES: list[complex] = [TOP, RIGHT, BOTTOM, LEFT]

TOP_LEFT = -1 + -1j
TOP_RIGHT = -1 + 1j
BOTTOM_LEFT = 1 + -1j
BOTTOM_RIGHT = 1 + 1j
CORNERS: list[tuple] = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]

EDGES: list[tuple] = CORNERS + SIDES

# If the edges need to be consecutive
CON_EDGES = [TOP_LEFT, TOP, TOP_RIGHT, RIGHT, BOTTOM_RIGHT, BOTTOM, BOTTOM_LEFT, LEFT]


def clone_swap(a: list, x: int, y: int):
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


# This is relegated because you can just check if the key is in the dict.
def is_valid_index_pair(array, x, y) -> bool:
    """
    Note: I should try the default dict method that automatically handles bounds checking.
    """
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def hash(x: int, y: int) -> complex:
    return complex(x, y)


def solve(lines) -> None:

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
