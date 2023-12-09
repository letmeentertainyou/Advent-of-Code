#!/bin/python3
"""
Dang I lost a lot of time on this one because I tried writing the diff algorithm myself and I was failing
somewhere. I finally looked up how to diff a list of ints and used numpy.diff which instantly gave me the
correct answer. With my own version of diff the sample data worked fine but a few of my more complicated
inputs were not reducing to all zeroes.

I think it has to do with negative numbers and even though I was using abs I was still getting a wrong answer.
I really wish they have show negative numbers in the sample since they are in the real data.

I have found the AoC rules to be directly misleading on several days now. Oh well on to part 2.

This can be sped-up a lot by removing the numpy import, I will do that tomorrow.
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
        next_value = arr[-1] + next_arr[-1]
        next_arr.append(next_value)

    # This works but I didn't add zero to the last list. Idk if that will
    # effect part 2.

    return backwards[-1][-1]


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        answer += solve([int(v) for v in line.strip().split(" ")])

    print(answer)


part_1("input.txt")

# Answer: 1681758908


"""
# I'm leaving my old diff code here so that I can
# do a post-mortem on why it failed tomorrow.
# My answer seems broken so I'm trying numpy

def get_differences(list_of_ints):
    diff = list(numpy.diff(list_of_ints))
    return diff

    res = []
    for i, v in enumerate(list_of_ints[:-1]):
        res.append(abs(v - list_of_ints[i + 1]))
    return res

"""
