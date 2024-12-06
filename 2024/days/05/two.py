#!/bin/python3.10
"""
This one was pretty straight forward. Once you identify where the mistake is you swap the current page number
with the one that should be on it's left and recursively call solve() again. This effectively sorts them into
the correct order. I lost a fair few precious seconds because Python insists upon editing my array inside of
a function. I would really prefer a language that deep copies by default. That behavior is one of the biggest
foot guns in Python and I cannot stand it. It's just bad design and it feels bad every time my array gets nuked 
inside a function. But at least I will be prepared to use deepcopy on the days ahead. 
"""
from collections import defaultdict
from copy import deepcopy
from sys import argv


class Order:
    def __init__(self):
        self.lefts = []
        self.rights = []

    def al(self, n):
        self.lefts.append(n)

    def ar(self, n):
        self.rights.append(n)


def clone_swap(a: list, x: int, y: int):
    A = deepcopy(a)
    A[x], A[y] = A[y], A[x]
    return A


def solve(page_nums: list[str], page_map: dict[Order]) -> list[str]:
    for l_idx, num in enumerate(page_nums):
        lefts = page_map[num].lefts
        for right in page_nums[l_idx + 1 :]:
            if right in lefts:
                r_idx = page_nums.index(right)
                swap_nums = clone_swap(page_nums, l_idx, r_idx)
                return solve(swap_nums, page_map)
    return page_nums


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
            swap_nums = solve(page_nums, page_map)
            if page_nums != swap_nums:
                mid_idx = len(swap_nums) // 2
                answer += int(swap_nums[mid_idx])

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
