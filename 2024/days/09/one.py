#!/bin/python3.10
"""
I spent a good five to ten minutes typing up the requirements for this parsing before I solved
it in earnest. Doing that does help me process the desired outcome but I also wish I had solved
this once faster. The example data worked with simple string manipulations and it took me a long
time to realize that I needed to use a list to get my real answer.

real    0m0.093s
user    0m0.089s
sys     0m0.004s
"""
from sys import argv


def mem_map(line: str) -> list:
    """
    00...111...2...333.44.5555.6666.777.888899

    The first footgun is that this needs to return a list and not a string. In the
    example strings were fine but in the real data there can be values that are more
    than one digit and they change the length of the string.
    """
    index = 0
    mode = True
    res = []
    for char in line:
        res.extend([index if mode else "." for _ in range(int(char))])
        if mode:
            index += 1
        mode = not mode
    return res


def mem_shift(mapped: list) -> list:
    """
    00...111...2...333.44.5555.6666.777.888899
    0099811188827773336446555566..............
    """

    def next_index() -> int | bool:
        i = n_indexes.pop(-1)
        if len(n_indexes) > 0:
            if mapped[i] == ".":
                return next_index(mapped, n_indexes)
            return i
        return False

    n_indexes = [i for i, c in enumerate(mapped) if c != "."]
    for i, c in enumerate(mapped):
        if c == ".":
            r = next_index()
            if (not r) or (r < i):
                break
            mapped[i], mapped[r] = mapped[r], mapped[i]

    return mapped


def check_sum(shifted) -> int:
    check: int = 0
    for i, c in enumerate(shifted):
        if c != ".":
            check += i * int(c)
    return check


def solve(file: list[str]) -> None:
    answer: int = 0
    mapped: list = mem_map(file)
    shifted: list = mem_shift(mapped)
    answer += check_sum(shifted)
    print(answer)


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file: str = tmpfile.read()

    solve(file)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     1928
# Answer:   6279058075753
# Rank:     7015
