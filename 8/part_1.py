#!/bin/python3
"""
This was fun, I really enjoyed itertools.cycle. Anytime I think of a way to process data, it's already
a built in!
"""

# This is so cool!
from itertools import cycle


def build_map(file):
    MAP = {}
    for line in file:
        ls = line[:-2].split(" = (")
        key = ls[0]
        values = ls[1].split(", ")
        MAP[key] = values
    return MAP


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    LR: str = file[0].strip()
    MAP: dict = build_map(file[2::])
    count = 0
    pos = MAP["AAA"]
    for step in cycle(LR):
        count += 1
        if step == "L":
            key = pos[0]
        if step == "R":
            key = pos[1]

        if key == "ZZZ":
            print(count)
            break
        else:
            pos = MAP[key]


part_1("input.txt")

# Answer: 20221
