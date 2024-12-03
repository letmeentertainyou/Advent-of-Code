#!/bin/python3
"""

"""


# This is for 2d arrays.
def is_valid_index_pair(array, x, y):
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def hash(x: int, y: int) -> str:
    """Modifying this method correctly can solve a lot of problems."""
    return f"{x}:{y}"


def solve():
    """"""
    score = 0
    return score


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    for x, line in enumerate(file):
        for y, char in enumerate(line):
            ...

    answer = 0
    print(answer)


part_1("input.txt")

# Answer:
# Test:
