#!/bin/python3.10
"""
This one straight up doesn't count. I loved the problem but I hated the cycle detection process. I can't even phrase how unsettling this brute force was for my spirit. Suffice it to say I learned a lot of neat cycle detection tricks that will hopefully help be rank higher next time.

TIMES:
real    0m9.217s
user    0m9.208s
sys     0m0.008s

The final optimization is a little awkward because the solve function works for part one and part two. The main reason I did 
that is because 90% of the two different functions overlapped and I didn't want to repeat the code. Overall I'm pretty happy 
with 9s on my mobile 7700k, I'm guessing it's quite a bit faster on a modern CPU.
"""
from sys import argv

TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)


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


def solve(data: dict, start: str, mode: bool = True) -> set | bool:
    """
    This returns the visited keys when a loop isn't detected. I did this so that I wouldn't have two
    nearly identical functions in my code.
    """
    visited: set = set()
    dir: complex = TOP
    pos: complex = start
    while True:
        old_dir = dir
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            return set([v[0] for v in visited])

        # this is a neat trick I got from /u/rkechols that checks if both the position and direction are repeats.
        if (pos, dir) in visited:
            return True

        # when mode is on we count every square visited
        if mode:
            visited.add((pos, dir))

        # when mode is off we only count the squares with rotations
        elif old_dir != dir:
            visited.add((pos, dir))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    data: dict = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash: complex = complex(x, y)
            if char == "^":
                start = hash
            data[hash] = char

    visited = solve(data, start)
    answer = 0
    for key in visited:
        old = data[key]
        if old != "#":
            data[key] = "#"
            if solve(data, start, mode=False) == True:
                answer += 1
            data[key] = old

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     6
# Answer:   1575
# Rank:     11830
