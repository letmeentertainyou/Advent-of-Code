#!/bin/python3
"""
***NOTE: This was a truly poorly worded question and I did not enjoy working on it.

Loop through all the seeds, make a dict for each seed.

Send each seed all the way through the maps, and at the end
find out which seed corresponded to the lowest final number.

Step 1 parse all the seeds.
Step 2 get the first map implementation working.
Step 3 walk through all the maps.
Step 4 check the lowest seed number.
"""
from math import inf


def check_against_map(seed, a, b, c):
    """I got this backwards at first. I will document better tomorrow."""
    a, b, c = int(a), int(b), int(c)
    N = seed[-1]

    if N in range(b, b + c):
        diff = N - b
        seed.append(a + diff)

    return seed


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    seeds = {}
    seed_split = file[0].strip().split(" ")[1::]
    seeds = {s: [int(s)] for s in seed_split}

    for key, seed in seeds.items():
        seed_length = 1
        for line in file[2:]:
            if ":" in line:
                seed_length += 1

            elif line == "\n":
                if len(seed) < seed_length:
                    seed.append(seed[-1])

            elif len(seed) < seed_length:
                seed = check_against_map(seed, *line.split(" "))

    current = inf
    for seed in seeds.values():
        if seed[-1] < current:
            current = seed[-1]
    print(current)


part_1("input.txt")

# Answer: 282277027
