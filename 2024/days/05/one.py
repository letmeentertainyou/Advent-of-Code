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
        self.lefts = []
        self.rights = []

    def al(self, n):
        self.lefts.append(n)

    def ar(self, n):
        self.rights.append(n)


def solve(page_nums: list[str], page_map: dict[Order]) -> bool:
    for l_idx, num in enumerate(page_nums):
        lefts = page_map[num].lefts
        for right in page_nums[l_idx + 1 :]:
            if right in lefts:
                return False
    return True


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    answer = 0
    page_map: dict[Order] = defaultdict(Order)
    for line in file:
        if "|" in line:
            left, right = line.split("|")
            # page_map[left].ar(right)
            page_map[right].al(left)

        elif "," in line:
            page_nums = line.split(",")
            if solve(page_nums, page_map):
                mid_idx = len(page_nums) // 2
                answer += int(page_nums[mid_idx])

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
