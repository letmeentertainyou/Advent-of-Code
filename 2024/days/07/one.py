#!/bin/python3.10
"""
I loved this problem, nice and easy, I was terrified part two would include PEMDAS but thankfully no.

real    0m0.506s
user    0m0.495s
sys     0m0.008s

Optimized times:

real    0m0.147s
user    0m0.142s
sys     0m0.005s
"""
from sys import argv


def solve(test, nums: list[str]) -> None:
    def r(tot: int, i: int):
        if tot == test:
            return True

        i += 1
        if (tot > test) or (i == len(nums)):
            return False

        if r(tot + nums[i], i):
            return True

        return r(tot * nums[i], i)

    return r(nums[0], 0)


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
