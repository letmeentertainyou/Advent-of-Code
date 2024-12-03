#!/bin/python3.10
"""

"""
import re

from sys import argv
from collections import Counter
from itertools import *


# This is for 2d arrays.
def is_valid_index_pair(array, x, y) -> bool:
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def hash(x: int, y: int) -> str:
    return f"{x}:{y}"


def solve(lines) -> None:

    answer = 0

    return answer


def parse_input(filename: str) -> tuple:
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
# Ranks:    .
