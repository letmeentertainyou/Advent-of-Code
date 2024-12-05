#!/bin/python3.10
"""
This was the first data where splitting up the data into a manageable workflow was the majority of the work
and it took me a while to understand the shape of my containers here. Ultimately it was a fairly simple problem
of mapping out the lefts and rights associated with each number and the iterating through every number and every
line. If ever a number that should be to the left of N is on it's right then we have an error. 
"""
from collections import defaultdict
from sys import argv


class Order:
    def __init__(self):
        self.l = []
        self.r = []

    def al(self, l):
        self.l.append(l)

    def ar(self, r):
        self.r.append(r)


def solve(page_nums: list[str], page_map: dict[Order]) -> bool:
    for l_idx, num in enumerate(page_nums):
        lefts = page_map[num].l
        for j in page_nums[l_idx + 1 :]:
            if j in lefts:
                return False
    return True


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
            if solve(page, page_map):
                answer += int(page[len(page) // 2])

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
