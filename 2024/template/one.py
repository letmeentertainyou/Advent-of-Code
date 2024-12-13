#!/bin/python3.10
"""

"""
from _utils import *


def solve(graph: dict, lines: list[str]) -> None:

    answer = 0
    for line in lines:
        ...

    for k, v in graph.items():
        ...

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")
        # file = tmpfile.read()

    lines: list = []
    graph: dict = {}
    # data: dict = defaultdict(list)

    for x, line in enumerate(file):
        lines.append(line)
        for y, char in enumerate(line):
            hash = complex(x, y)
            graph[hash] = char
            # data[char].append(hash)
            ...

    solve(graph, lines)
    # solve(file)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     .
# Answer:   .
# Rank:     .
