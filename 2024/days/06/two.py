#!/bin/python3.10
"""
This one straight up doesn't count. I loved the problem but I hated the cycle detection process. I can't even phrase how unsettling this brute force was for my spirit. I did learn a really neat cycle detection algorithm called Turtle and the Hare that did not more on my data because it's possible for the guard to perform a 180 and then the Hare an the Turtle overlap. 

The other easier type of cycle detection where anytime you enter the same square more than once also didn't work because you might cross a square several times going different directions before you hit exit.

Overall, I can't even imagine what the real solution is.

TIMES:
real    0m40.998s
user    0m40.984s
sys     0m0.013s'

40 seconds isn't bad for such a crazy brute force but I still feel bad about it. I noticed that everyone else who finished part 1 with me, also took 3 hours on part 2.
"""
from sys import argv

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
SIDES: list[tuple] = [UP, RIGHT, DOWN, LEFT]


def hash(x: int, y: int) -> str:
    return f"{x}:{y}"


def rotate(dir: tuple):
    index = (SIDES.index(dir) + 1) % len(SIDES)
    return SIDES[index]


def step_forward(data: dict, pos: str, dir: tuple):
    x, y = [int(i) for i in dir]
    X, Y = [int(i) for i in pos.split(":")]
    X += x
    Y += y
    new_pos = hash(str(X), str(Y))
    if new_pos in data:
        if data[new_pos] == "#":
            return step_forward(data, pos, rotate(dir))

        return new_pos, dir
    return "", None


def check_for_loop(data: dict, start: str) -> None:
    pos = start
    dir = UP
    step_count = 0
    while True:
        step_count += 1
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            return False
        # this just sucks but it's the only way I could check, and it has to be a very high number because
        #  you will routinely do more than 8000 steps on this problem, my solution doesn't work for you
        # try tep_count > 300000

        if step_count > 10000:
            return True


def solve(data: dict, start: str) -> None:
    pos = start
    visited = set()
    dir = UP
    while True:
        pos, dir = step_forward(data, pos, dir)
        if pos not in data:
            break
        visited.add(pos)

    # this was my first ugly brute force, I can't believe it wasn't enough
    answer = 0
    for key in visited:
        old = data[key]
        if old != "#":
            data[key] = "#"
            if check_for_loop(data, start):
                answer += 1
            data[key] = old

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    data = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            h = hash(x, y)
            if char == "^":
                pos = h
            data[h] = char

    solve(data, pos)


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
