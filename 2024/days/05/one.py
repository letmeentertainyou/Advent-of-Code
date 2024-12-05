#!/bin/python3.10
"""
This was the first data where splitting up the data into a manageable workflow was the majority of the work and it took me
a while to understand the shape of my containers here. Ultimately it was a fairly simple problem of mapping out the lefts and
rights associated with each number and the iterating through every number and every line. If ever a number that should be to
the left of N is on it's right then we have an error. 

Overall I liked this problem but I definitely panicked a bit while I was working it out and it took over an hour to do both parts.
"""
from sys import argv
from collections import defaultdict


class Order:
    """
    You don't need the list of rights at all to solve the problem but I like that this parse can be extended easily to care
    about both directions of parsing.
    """

    def __init__(self):
        self.l = []
        self.r = []

    def al(self, l):
        self.l.append(l)

    def ar(self, r):
        self.r.append(r)


def mapper(orders: list[tuple]):
    filled_map = defaultdict(Order)
    for x, y in orders:
        filled_map[x].ar(y)
        filled_map[y].al(x)

    return filled_map


def solve(page: list, filled_map) -> None:
    for i, k in enumerate(page):
        lefts = filled_map[k].l
        for j in page[i + 1 :]:
            if j in lefts:
                return False
    return True


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    orders: list[tuple] = []
    pages: list = []
    for x, line in enumerate(file):
        if "|" in line:
            orders.append(line.strip("\n").split("|"))
        elif "," in line:
            pages.append(line.strip("\n").split(","))

    filled_map = mapper(orders)
    answer = 0
    for page in pages:
        if solve(page, filled_map):
            mid_index = len(page) // 2
            answer += int(page[mid_index])

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     143
# Answer:   6949
# Rank:     10864
