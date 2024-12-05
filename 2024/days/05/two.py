#!/bin/python3.10
"""
This one was pretty straight forward. Once you identify where the mistake is you swap the current page number with the one
that should be on it's left and recursively call solve() again. This effectively sorts them into the correct order. I lost
a fair few precious seconds because Python insists upon editing my array inside of a function. I would really prefer a language
that deep copies by default. That behaviors is one of the biggest foot guns in Python and I cannot stand it. It's just bad design
and it feels bad every time my array gets nuked inside a function.

But at least I will be prepared to use deepcopy on the days ahead. 
"""
from sys import argv
from collections import defaultdict
from copy import deepcopy


class Order:
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
                r_idx = page.index(j)
                p = deepcopy(page)
                p[i], p[r_idx] = p[r_idx], p[i]
                return solve(p, filled_map)
    return page


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
        p = solve(page, filled_map)
        if page != p:
            mid_index = len(p) // 2
            answer += int(p[mid_index])

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     123
# Answer:   4145
# Rank:     8401
