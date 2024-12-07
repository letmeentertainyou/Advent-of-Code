#!/bin/python3.10
"""
I loved this problem, nice and easy, I was terrified part two would include PEMDAS but thankfully no.

real    0m0.506s
user    0m0.495s
sys     0m0.008s
"""
import itertools as it

from sys import argv


def solve(test, nums: list[str]) -> None:
    ops = ["*", "+"]
    perms = it.product(ops, repeat=len(nums) - 1)
    for x, perm in enumerate(perms):
        tot = nums[0]
        for i, op in enumerate(perm):
            y = nums[i + 1]
            if op == "*":
                tot *= y
            if op == "+":
                tot += y

            if tot == test:
                return True

    return False


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = (line.strip("\n") for line in tmpfile.readlines())

    answer = 0
    for x, line in enumerate(file):
        split = line.split(":")
        test = int(split[0])
        nums = [int(n) for n in split[1].split()]
        if solve(test, nums):
            answer += test

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     3749
# Answer:   14711933466277
# Rank:     4619
