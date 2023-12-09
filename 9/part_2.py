#!/bin/python3
"""
This part is literally just inverting one single step. It might be the easiest part 2.

The only problem I ran into is the order of the terms x + y is the same as y + x
But that is not true with subtraction. The example data was useful for debugging that
even though it was totally worthless for part 1. I found the text of part 2 to be 
unhelpful though.
"""
import numpy


def not_all_zeroes(list_of_ints):
    """I'm positive there is elegant way to do this in Python."""
    for value in list_of_ints:
        if value != 0:
            return True
    return False


def solve(list_of_values):
    """Work out the differences until they are all zero, and then
    work out the next value backwards.
    """
    res = [list_of_values]
    while not_all_zeroes(res[-1]):
        diff = list(numpy.diff(res[-1]))
        res.append(diff)

    backwards = res[::-1]
    for index, arr in enumerate(tuple(backwards[:-1])):
        next_arr = backwards[index + 1]
        next_value = next_arr[0] - arr[0]
        next_arr.insert(0, next_value)

    return backwards[-1][0]


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        answer += solve([int(v) for v in line.strip().split(" ")])

    print(answer)


part_2("input.txt")

# Answer: 803
