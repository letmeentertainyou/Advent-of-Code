#!/bin/python3.10
"""
This one was pretty fun other than some python pains with nested functions accessing what should be local variables.
But part two took me absolutely forever to bug check and probably ruined my average.
"""
from sys import argv


TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)


def check_tile(graph: dict, tile: complex, visited: set):
    def r(t: complex):
        nonlocal perm
        area.add(t)
        visited.add(t)
        for side in SIDES:
            tmp = t + side
            if (tmp in graph) and (tmp not in visited) and (graph[tmp] == value):
                r(tmp)

            if (tmp not in graph) or (graph[tmp] != value):
                perm += 1

    area = set()
    perm = 0
    value = graph[tile]
    r(tile)
    return len(area) * perm


def solve(graph: dict) -> None:
    visited = set()
    answer = 0

    for k in graph:
        if k not in visited:
            answer += check_tile(graph, k, visited)

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")

    graph: dict = {}
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash = complex(x, y)
            graph[hash] = char

    solve(graph)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     1930
# Answer:   1371306
# Rank:     5897
