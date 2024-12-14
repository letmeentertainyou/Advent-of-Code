#!/bin/python3.10
"""
This one was very vague and without a picture I pretty much have no clue what the 
author wants. I can assume that the picture of the tree looks like
          X
         X X
        X   X
       X     X
      X       X
     x         x
    x           x

This one seemed like it would be really hard to calculate but the naive approach 
of assuming every robot would occupy a different tile works. So all I did was move 
each robot one step forward then make a set of all of the robots positions and 
compare the len of that set to the len of the robots list.

If you have all the robots in unique tiles then you have found the answer.

real    0m3.185s
user    0m3.174s
sys     0m0.010s
"""
from _utils import *


def step_forward(pos, vel, grid_x, grid_y):
    """
    Any time a robots index would move past one of the boundaries negative or positive, move it to the other side like pacman and then update it.
    """
    tmp = pos + vel
    tmp_real = tmp.real % grid_x
    tmp_imag = tmp.imag % grid_y
    return complex(tmp_real, tmp_imag)


def solve(robots: list[tuple], grid_x=101, grid_y=103) -> None:
    answer = 0
    while answer < grid_x * grid_y:
        answer += 1

        for i, r in enumerate(robots):
            robots[i][0] = step_forward(r[0], r[1], grid_x, grid_y)

        s = set([r[0] for r in robots])
        if len(s) == len(robots):
            break

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")

    robots: list = []

    for x, line in enumerate(file):
        ints = find_ints(line)
        pos = complex(ints[0], ints[1])
        vel = complex(ints[2], ints[3])
        robots.append([pos, vel])

    solve(robots)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     ???
# Answer:   8050
# Rank:     3161
