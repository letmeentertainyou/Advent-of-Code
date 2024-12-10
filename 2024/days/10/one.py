#!/bin/python3.10
"""

"""
from sys import argv


TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)


def get_sides(graph: dict, start: complex, visited: list[complex]):
    sides = []
    for SIDE in SIDES:
        tmp = start + SIDE
        if (tmp in graph) and (tmp not in visited):
            sides.append(tmp)
    return sides


def traverse(graph: dict, start: complex):
    def r(s):
        next = []
        visited.append(s)
        sides: list[complex] = get_sides(graph, s, visited)
        for side in sides:
            if int(graph[side]) == int(graph[s]) + 1:
                if graph[side] == "9":
                    nine_sides.add(side)
                next.append(side)

        for n in next:
            r(n)

    visited = []
    nine_sides: set = set()

    r(start)
    return len(nine_sides)


def solve(graph: dict, starts: list) -> None:
    answer = 0
    for start in starts:
        answer += traverse(graph, start)

    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read().split("\n")

    graph: dict = {}
    starts = []
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            hash = complex(x, y)
            if char == "0":
                starts.append(hash)
            graph[hash] = char

    solve(graph, starts)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     36
# Answer:   744
# Rank:     4114
