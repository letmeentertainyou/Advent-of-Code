#!/bin/python3
"""
This isn't my prettiest code but I am really happy that I understood all the math concepts and had
them ready to go in my head. Part 1 from yesterday helped a lot.
"""

from itertools import combinations


def hash(y: int, x: int):
    return f"{y}:{x}"


def get_dubs(data, length, index):
    """Get the dubs and return it as a list of ints."""
    vsplit = []
    for val in data.values():
        tmp = [int(i) for i in val.split(":")]
        vsplit.append(tmp[index])

    dubs = []
    for i in range(length):
        if i not in vsplit:
            dubs.append(i)

    return dubs


# Figure out x distance and y distance
# Add extra points for each y_dub/x_dub we intersect.
def solve(data, key1, key2, y_dub, x_dub):
    """Get the two keys from data, find a path between their hashes."""
    coords1 = [int(_) for _ in data[key1].split(":")]
    coords2 = [int(_) for _ in data[key2].split(":")]

    # get x_chords/y_chords and sort them
    y_coords = sorted([coords1[0], coords2[0]])
    x_coords = sorted([coords1[1], coords2[1]])

    score = 0
    score += y_coords[1] - y_coords[0]
    score += x_coords[1] - x_coords[0]

    # Count how many y_dubs are in range(y_coords)
    for y in y_dub:
        if y in range(*y_coords):
            score += 1

    # Count how many x_dubs are in range(x_coords)
    for x in x_dub:
        if x in range(*x_coords):
            score += 1

    return score


# Get all the hash-marks and put them in a dict with index as the key and a count as the value
# Then write a function that finds any indexes in the range(len(file)) or range(len(line)) that are
# Not represented by the hash dict. Those are the lines to double and it really is that easy to calculate them
# Any index in the doubles struct will count for two steps when path finding. That is the whole thing.
def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    count = 0
    data = {}
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == "#":
                data[count] = hash(y, x)
                count += 1

    y_dubs = get_dubs(data, len(file), 0)
    x_dubs = get_dubs(data, len(file[0]), 1)

    dubs = [y_dubs, x_dubs]
    pairs = combinations(data.keys(), 2)

    answer = 0
    for pair in pairs:
        answer += solve(data, *pair, *dubs)

    print(answer)


part_1("input.txt")

# Answer: 10289334
