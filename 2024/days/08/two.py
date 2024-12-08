#!/bin/python3.10
"""
This was mostly a munging problem which I did in part one but it took a few tries to get my steps going correctly and then after solving it I cleaned up my while loop to be a sub function called step().
"""

from collections import defaultdict
from sys import argv


def solve(data: dict, freq_indexes: dict) -> None:
    def r_step(start, diff) -> None:
        while start in data:
            nodes.add(start)
            start -= diff

    nodes = set()
    for indexes in freq_indexes:
        for x in indexes:
            for y in indexes:
                if x != y:
                    r_step(x, x + y)
                    r_step(y, y - x)

    res = set([n for n in nodes if n in data.keys()])
    print(len(res))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    freq = defaultdict(list)
    data: dict = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash = complex(x, y)
            data[hash] = char
            if char.isalnum():
                freq[char].append(hash)

    solve(data, freq.values())


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
