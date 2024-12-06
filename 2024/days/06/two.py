#!/bin/python3.10
"""
This one straight up doesn't count. I loved the problem but I hated the cycle detection process. I can't even phrase how unsettling this brute force was for my spirit. I did learn a really neat cycle detection algorithm called Turtle and the Hare that did not more on my data because it's possible for the guard to perform a 180 and then the Hare an the Turtle overlap. 

The other easier type of cycle detection where anytime you enter the same square more than once also didn't work because you might cross a square several times going different directions before you hit exit.

Overall, I can't even imagine what the real solution is.

TIMES:
real    0m12.708s
user    0m12.705s
sys     0m0.002s

40 seconds isn't bad for such a crazy brute force but I still feel bad about it. I noticed that everyone else who finished part 1 with me, also took 3 hours on part 2.
"""
from sys import argv

TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: list[complex] = [TOP, RIGHT, BOTTOM, LEFT]


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


def solve(data: dict, start: str) -> set | bool:
    """
    This returns the visited keys when a loop isn't detected. I did this so that I wouldn't have two
    nrealy identical functions in my code.
    """
    visited: set = set()
    dir: complex = TOP
    pos: complex = start

    while True:
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            return set([v[0] for v in visited])

        # this is a neat trick I got from /u/rkechols that checks if both the position and direction are repeats.
        if (pos, dir) in visited:
            return True

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
            if solve(data, start) == True:
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
