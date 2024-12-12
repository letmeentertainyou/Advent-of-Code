#!/bin/python3.10
"""
Wow this one took me forever to figure out. It's because a single tile can be multiple corners so once I 
switched my find_corners function to return a count things worked out fine.

Python has some very weird behavior with integers being accessed by nested functions that quite frankly I
think is bad design and defeats the purpose of a nested function.
"""
from sys import argv

TOP: complex = -1 + 0j
RIGHT: complex = 0 + 1j
BOTTOM: complex = 1 + 0j
LEFT: complex = 0 + -1j
SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)

TOP_LEFT: complex = -1 + -1j
TOP_RIGHT: complex = -1 + 1j
BOTTOM_LEFT: complex = 1 + -1j
BOTTOM_RIGHT: complex = 1 + 1j

CORNERS = [
    (TOP, RIGHT, TOP_RIGHT),
    (RIGHT, BOTTOM, BOTTOM_RIGHT),
    (BOTTOM, LEFT, BOTTOM_LEFT),
    (LEFT, TOP, TOP_LEFT),
]


def count_corners(graph, tile, value):
    corners = 0
    for A, B, C in CORNERS:
        next_a = (graph[tile + A] == value) if tile + A in graph else False
        next_b = (graph[tile + B] == value) if tile + B in graph else False
        next_c = (graph[tile + C] == value) if tile + C in graph else False

        if (not next_a) and (not next_b):
            corners += 1

        if (next_a) and (next_b) and (not next_c):
            corners += 1

    return corners


def check_tile(graph: dict, tile: complex, visited: set):

    area = set()
    corners = 0
    value = graph[tile]

    def r(t: complex):
        nonlocal corners
        area.add(t)
        visited.add(t)
        corners += count_corners(graph, t, value)

        for side in SIDES:
            tmp = t + side
            if (tmp in graph) and (tmp not in visited) and (graph[tmp] == value):
                r(tmp)

    r(tile)
    return len(area) * corners


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


# Test:     1206
# Answer:   805880
# Rank:     7563
