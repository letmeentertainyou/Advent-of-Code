#!/bin/python3.10
"""

"""
import re
import itertools as it

from collections import Counter, defaultdict
from copy import deepcopy
from sys import argv

SIDES: list[tuple] = [(-1, 0), (0, 1), (0, -1), (1, 0)]
CORNERS: list[tuple] = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
EDGES: list[tuple] = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def clone_swap(a: list, x: int, y: int):
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


def is_valid_index_pair(array, x, y) -> bool:
    """
    Note: I should try the default dict method that automatically handles bounds checking.
    """
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def hash(x: int, y: int) -> str:
    return f"{x}:{y}"


def solve(lines) -> None:

    answer = 0

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

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
