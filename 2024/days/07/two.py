#!/bin/python3.10
"""
My brute force is 40 seconds and I'm pretty happy with that after yesterdays problem. I do have some ideas about how to reduce the time. My basic theory is that the join operator makes fantastically large numbers and I don't need to bother with that unless all of the other combinations of characters total to less than the target number. And I can shortcut that even further by checking if the product of nums is less than the target number. Basically if the product is greater I can use join and if the product is less than I can do the normal approach.


real    0m39.925s
user    0m39.265s
sys     0m0.656s
"""
import itertools as it

from sys import argv


def solve(test, nums: list[str]) -> None:
    ops = ["*", "+", "|"]
    perms = []
    perms.extend(it.product(ops, repeat=len(nums) - 1))
    for x, perm in enumerate(perms):
        tot = nums[0]
        for i, op in enumerate(perm):
            y = nums[i + 1]
            if op == "*":
                tot *= y
            if op == "+":
                tot += y
            if op == "|":
                tot = int(str(tot) + str(y))

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


# Test:     11387
# Answer:   286580387663654
# Rank:     3660
