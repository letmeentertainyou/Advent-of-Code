#!/bin/python3.8
"""
This one is going to be way too hard for me to do tonight. The basic concept is to find an X of MAS

M S
 A
M S

Find the four corner coords, then check every single A. Once an A is found check if the diagonal corner 
combos contain one M and one S. If all that is met then we have a Point.
"""
from sys import argv


def is_valid_index_pair(array, x, y) -> bool:
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def solve(grid, X, Y):
    chars = ["M", "S"]
    dirs = [(X - 1, Y - 1), (X - 1, Y + 1), (X + 1, Y - 1), (X + 1, Y + 1)]

    # validate that all the corners are on the grid
    for d in dirs:
        if not is_valid_index_pair(grid, *d):
            return False

    # check the top left and bottom right corners.
    tl, br = grid[dirs[0][0]][dirs[0][1]], grid[dirs[3][0]][dirs[3][1]]
    if not ((tl in chars) and (br in chars) and (tl != br)):
        return False

    # check the bottom left and top right corners.
    bl, tr = grid[dirs[2][0]][dirs[2][1]], grid[dirs[1][0]][dirs[1][1]]
    if not ((bl in chars) and (tr in chars) and (bl != tr)):
        return False

    # dirs2 = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    return True


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    # we need access to the entire grid when we check each A so we have to generate it before we loop.
    grid: list[list] = []
    for line in file:
        grid.append([c for c in line.strip()])

    answer = 0
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            if char == "A":
                if solve(grid, x, y):
                    answer += 1

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     9
# Answer:   1952
# Rank:     8818
