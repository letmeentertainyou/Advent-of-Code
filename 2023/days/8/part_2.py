#!/bin/python3.10
"""
I normally use python3.8 for these but math.lcm didn't get included ultil python 3.9
so this script just hard links to python 3.10.

Make a dict of all keys that ends in an A,
then walk through the steps modify each key in the dict, per step, and
also keep a running count. This will need a custom update function.

Get all nodes that end with A.
Follow the L or R direction for each node in the dict.
Break when every node ends in Z.
Return the count.

I wrote a really neat elegant brute force for this but it would have taken the age of the universe to run.
So math hacks instead.
"""

# This is so cool!
from itertools import cycle
from math import lcm


def build_map(file):
    MAP = {}
    for line in file:
        ls = line[:-2].split(" = (")
        key = ls[0]
        values = ls[1].split(", ")
        MAP[key] = values
    return MAP


def get_all_a_keys(MAP):
    positions = []
    for key in MAP:
        if key[2] == "Z":
            positions.append(MAP[key])
    return positions


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    LR: str = file[0].strip()
    MAP: dict = build_map(file[2::])
    a_keys = get_all_a_keys(MAP)
    counts = []
    for pos in a_keys:
        count = 0
        for step in cycle(LR):
            count += 1
            if step == "L":
                key = pos[0]
            if step == "R":
                key = pos[1]
            if key[2] == "Z":
                counts.append(count)
                break
            else:
                pos = MAP[key]
    answer = lcm(*counts)
    print(answer)


part_2("input.txt")

# Answer: 14616363770447
