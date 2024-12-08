#!/bin/python3.10
"""
This was mostly a munging problem which I did in part one but it took a few tries to get my steps going correctly and then after solving it I cleaned up my while loop to be a sub function called step().
"""

from collections import defaultdict
from sys import argv


def solve(data: dict, freq: dict) -> None:
    nodes = set()
    for k, indexes in freq.items():
        nodes = map_nodes(indexes, nodes, data)

    res = set([n for n in nodes if n in data.keys()])
    print(len(res))


def map_nodes(indexes, nodes, data):
    def step(start, diff):
        while diff:
            nodes.add(start)
            start -= diff
            if start not in data:
                break

    for f in indexes:
        for d in indexes:
            step(f, f + d)
            step(d, d - f)

    return nodes


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    freq = defaultdict(list)
    data: list = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash = complex(x, y)
            data[hash] = char
            if char.isalnum():
                freq[char].append(hash)

    solve(data, freq)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     34
# Answer:   1157
# Rank:     4940
