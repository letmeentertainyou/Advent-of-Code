#!/bin/python3.10
"""
This one was pretty straight forward. Once you identify where the mistake is you swap the current page number
with the one that should be on it's left and recursively call solve() again. This effectively sorts them into
the correct order. I lost a fair few precious seconds because Python insists upon editing my array inside of
a function. I would really prefer a language that deep copies by default. That behaviors is one of the biggest
foot guns in Python and I cannot stand it. It's just bad design and it feels bad every time my array gets nuked 
inside a function. But at least I will be prepared to use deepcopy on the days ahead. 
"""
from collections import defaultdict
from copy import deepcopy
from sys import argv


class Order:
    def __init__(self):
        self.l = []
        self.r = []

    def al(self, l):
        self.l.append(l)

    def ar(self, r):
        self.r.append(r)


def clone_swap(a: list, x: int, y: int):
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


def solve(page_nums: list[str], page_map: dict[Order]) -> list[str]:
    for l_idx, num in enumerate(page_nums):
        lefts = page_map[num].l
        for j in page_nums[l_idx + 1 :]:
            if j in lefts:
                r_idx = page_nums.index(j)
                return solve(clone_swap(page_nums, l_idx, r_idx), page_map)
    return page_nums


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    page_map: dict[Order] = defaultdict(Order)
    for x, line in enumerate(file):
        if "|" in line:
            l, r = line.strip("\n").split("|")
            # page_map[l].ar(r)
            page_map[r].al(l)

        elif "," in line:
            page = line.strip("\n").split(",")
            p = solve(page, page_map)
            if page != p:
                answer += int(p[len(page) // 2])

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
