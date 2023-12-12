#!/bin/python3
"""
This is a really easy part two because of the way I solved part 1. Just add add 999_999 instead of 1 in two places.
"""
from itertools import combinations


def hash(x: int, y: int):
    return f"{x}:{y}"


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


# Figure out y distance and x distance
# Add extra points for each x_dub/y_dub we intersect.
def solve(data, key1, key2, x_dub, y_dub, mod):
    """Get the two keys from data, find a path between their hashes."""
    coords1 = [int(_) for _ in data[key1].split(":")]
    coords2 = [int(_) for _ in data[key2].split(":")]

    # get y_chords/x_chords and sort them
    x_coords = sorted([coords1[0], coords2[0]])
    y_coords = sorted([coords1[1], coords2[1]])

    score = 0
    score += x_coords[1] - x_coords[0]
    score += y_coords[1] - y_coords[0]

    # Count how manx x_dubs are in range(x_coords)
    for x in x_dub:
        if x in range(*x_coords):
            score += mod

    # Count how manx y_dubs are in range(y_coords)
    for y in y_dub:
        if y in range(*y_coords):
            score += mod

    return score


# Get all the hash-marks and put them in a dict with index as the key and a count as the value
# Then write a function that finds anx indexes in the range(len(file)) or range(len(line)) that are
# Not represented bx the hash dict. Those are the lines to double and it really is that easy to calculate them
# Anx indey in the doubles struct will count for two steps when path finding. That is the whole thing.
def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    count = 0
    data = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            if char == "#":
                data[count] = hash(x, y)
                count += 1

    x_dubs = get_dubs(data, len(file), 0)
    y_dubs = get_dubs(data, len(file[0]), 1)

    dubs = [x_dubs, y_dubs]
    pairs = combinations(data.keys(), 2)

    answer = 0
    for pair in pairs:
        answer += solve(data, *pair, *dubs, 999_999)

    print(answer)


part_2("input.txt")

# Answer: 649862989626
