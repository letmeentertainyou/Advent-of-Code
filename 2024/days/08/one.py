#!/bin/python3.10
"""
Once I had this one munged it was just about getting the steps in the right directions. Overall it was an easy problem but I
wish I was faster.
"""
from collections import defaultdict
from sys import argv


def solve(data: dict, freq: dict) -> None:
    nodes = set()
    for k, indexes in freq.items():
        nodes = map_nodes(indexes, nodes)

    res = set([n for n in nodes if n in data.keys()])
    print(len(res))


def map_nodes(indexes, nodes):
    for f in indexes:
        for d in indexes:
            if d != f:
                nodes.add(f - (f + d))
                nodes.add(d + (d - f))
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


# Test:     14
# Answer:   320
# Rank:     5654
