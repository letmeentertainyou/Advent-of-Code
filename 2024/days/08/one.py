#!/bin/python3.10
"""
Once I had this one munged it was just about getting the steps in the right directions. 
Overall it was an easy problem but I wish I was faster.
"""
from collections import defaultdict
from sys import argv


def solve(data: dict, freq_indexes: dict) -> None:
    nodes = set()
    for indexes in freq_indexes:
        for x in indexes:
            for y in indexes:
                if y != x:
                    nodes.add(x - (x + y))
                    nodes.add(y + (y - x))

    res = set([n for n in nodes if n in data])
    print(len(res))


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    freq: dict = defaultdict(list)
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


# Test:     14
# Answer:   320
# Rank:     5654
