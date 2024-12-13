#!/bin/python3.10
"""

"""
import itertools as it
import re

from collections import Counter, defaultdict
from copy import deepcopy
from dataclasses import dataclass
from sys import argv


class D:
    """
    This is just a collapsable namespace for capturing all of the 2D
    directions for traversing a graph.
    """

    TOP: complex = -1 + 0j
    RIGHT: complex = 0 + 1j
    BOTTOM: complex = 1 + 0j
    LEFT: complex = 0 + -1j
    TOP_LEFT: complex = -1 + -1j
    TOP_RIGHT: complex = -1 + 1j
    BOTTOM_LEFT: complex = 1 + -1j
    BOTTOM_RIGHT: complex = 1 + 1j

    SIDES: tuple[complex] = (TOP, RIGHT, BOTTOM, LEFT)
    CORNERS: tuple[complex] = (TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM_LEFT)
    EDGES: tuple[complex] = CORNERS + SIDES

    CONSECUTIVE_EDGES: tuple[complex] = (
        TOP_LEFT,
        TOP,
        TOP_RIGHT,
        RIGHT,
        BOTTOM_RIGHT,
        BOTTOM,
        BOTTOM_LEFT,
        LEFT,
    )
    ORTHOGONAL_CORNERS: list[tuple[complex]] = [
        (TOP, RIGHT, TOP_RIGHT),
        (RIGHT, BOTTOM, BOTTOM_RIGHT),
        (BOTTOM, LEFT, BOTTOM_LEFT),
        (LEFT, TOP, TOP_LEFT),
    ]


@dataclass
class Range:
    start: int
    end: int
    length: int
    value: int | str = "."

    def __str__(self):
        return f"{self.start}, {self.end}, {self.length}, {self.value}"


def cabs(n: complex) -> complex:
    """Complex abs for getting abs(slope) when slope is a complex number.."""
    return complex(abs(n.real), abs(n.imag))


def match_all(line: str, pattern: str) -> list[str]:
    return re.findall(pattern, line)


def clone_swap(a: list, x: int, y: int) -> list:
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


# this is flood fill
def traverse(graph: dict, start: complex, target: str = "9"):
    """
    This version of traverse is looking for paths that increment from 0 to 9 and then returns
    the number of paths that reach 9. But it could be modified to have any graph traversal goal state
    you need.
    """

    def get_sides(s: complex):
        sides = []
        for SIDE in D.SIDES:
            new_side = s + SIDE
            if new_side in graph:
                sides.append(new_side)
        return sides

    def r(s):
        next = []
        sides: list[complex] = get_sides(s)

        for side in sides:
            if int(graph[side]) == int(graph[s]) + 1:
                if graph[side] == target:
                    target_sides.append(side)
                next.append(side)

        for n in next:
            r(n)

    target_sides: list = []
    r(start)
    return len(target_sides)


# this looks for linear paths
def step_forward(
    graph: dict, pos: complex, dir: complex, wall: str = "#", rot_dir: int = 1
) -> tuple:
    """
    This finds the next available square that isn't a "#" and it rotates 90° when
    the square is a "#" allowing for easy graph traversal.

    For rot_dir:
     1 = 90°R,  2 = 180°R,  3 = 270°R,  4 = 360°R
    -1 = 90°L, -2 = 180°L, -3 = 270°L, -4 = 360°L
    """

    def rotate() -> complex:
        index = (D.SIDES.index(dir) + rot_dir) % len(D.SIDES)
        return D.SIDES[index]

    new_pos: complex = pos + dir
    if new_pos in graph:
        if graph[new_pos] == wall:
            return step_forward(graph, pos, rotate())

        return new_pos, dir
    # When this happens the position isn't in the graph and can be handled by the calling code.
    return "", None


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
