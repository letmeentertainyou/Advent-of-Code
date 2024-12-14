#!/bin/python3.10
"""
Update the robot positions 100 times (100 seconds) then count the number of robots 
per quadrant. Don't count any robots in the middle row or middle column. Multiply 
the number of robots in each quadrant together and that's the answer.
"""
from _utils import *
from math import prod


def step_forward(pos, vel, grid_x, grid_y):
    """
    Any time a robots index would move past one of the boundaries negative or positive, move it to the other side like pacman and then update it. This should step forwards 100 times at once and then find the boundaries.
    """
    tmp = pos + (vel * 100)
    tmp_real = tmp.real % grid_x
    tmp_imag = tmp.imag % grid_y
    return complex(tmp_real, tmp_imag)


def find_quadrants(rows, cols):
    mid_row = rows // 2
    mid_col = cols // 2

    quadrants = {"Q1": [], "Q2": [], "Q3": [], "Q4": []}

    for i in range(rows):
        for j in range(cols):
            if i == mid_row or j == mid_col:
                continue
            if i < mid_row and j > mid_col:
                quadrants["Q1"].append(complex(i, j))
            elif i < mid_row and j < mid_col:
                quadrants["Q2"].append(complex(i, j))
            elif i > mid_row and j < mid_col:
                quadrants["Q3"].append(complex(i, j))
            elif i > mid_row and j > mid_col:
                quadrants["Q4"].append(complex(i, j))

    return quadrants


# The grids have different sizes which is stupid and makes it pretty hard
# to switch from the test case to real case.
def solve(robots: list[tuple], grid_x=101, grid_y=103) -> None:
    # grid_x = 7
    # grid_y = 11
    for i, r in enumerate(robots):
        robots[i] = step_forward(r[0], r[1], grid_x, grid_y)

    quads = find_quadrants(grid_x, grid_y)
    quad_count = Counter()
    for robot in robots:
        for Q in quads.keys():
            if robot in quads[Q]:
                quad_count.update(Q.split())

    print(prod(quad_count.values()))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")

    robots: list = []

    for x, line in enumerate(file):
        ints = find_ints(line)
        pos = complex(ints[0], ints[1])
        vel = complex(ints[2], ints[3])
        robots.append((pos, vel))

    solve(robots)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     12
# Answer:   215987200
# Rank:     4830
