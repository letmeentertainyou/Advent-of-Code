#!/bin/python3.10
"""
# every other digit of the file is free space or file length
# file free file free
# 0     2    0     2
# 0202
# if free space == 0 then the files are connected.
# File files also have an ID number which is their order of appearance in the memory
# 12345 becomes
# 0..111....22222
# put the i times the value or . times the free space
More rightmost data into each leftmost period
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
You can just keep the indexes of the periods instead of looking up the leftmost one every time because you are only overwriting them once and then moving on.
We'll be finished when there are only periods or only numbers and no cross matches.

We can start at the index of the last period we filled, then scan right for the next period, once we find one, we scan right again for an int. If we find any ints we aren't done. This is a little ineffeint thouigh because we want our numbers from the right so we have to know what's happening on that side too..

Scan the file backwards it's done if there are no periods after the leftmost number.
If there is a periord after the leftmost number then we must move one more number.
Repeat ad naus.

Then iterate through the final piece of memory multipling the files positions by it's original value (need to track this). If a file is memory skip it, if it's position is 0 then it multiplies to 0.

Then sum those at the end,.
"""
from sys import argv


def mem_map(line: str):
    """
    00...111...2...333.44.5555.6666.777.888899
    """
    index = 0
    mode = True
    res = []
    for char in line:
        res.extend([index if mode else "." for _ in range(int(char))])
        if mode:
            index += 1
        mode = not mode
    return res


def mem_shift(line: str):
    """
    00...111...2...333.44.5555.6666.777.888899
    0099811188827773336446555566..............
    """

    def next_index():
        i = n_indexes.pop(-1)
        if len(n_indexes) > 0:
            if line[i] == ".":
                return next_index(line, n_indexes)
            return i
        return False

    n_indexes = [i for i, c in enumerate(line) if c != "."]
    for i, c in enumerate(line):
        if c == ".":
            r = next_index()
            if (not r) or (r < i):
                break
            line[i], line[r] = line[r], line[i]

    return line


def check_sum(line):
    check = 0
    for i, c in enumerate(line):
        if c != ".":
            check += i * int(c)
    return check


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = [c for c in tmpfile.read()]

    solve(file)


def solve(file: list[str]) -> None:

    answer = 0
    # print(file)
    file = mem_map(file)
    file = mem_shift(file)
    answer += check_sum(file)

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     1928
# Answer:   6279058075753
# Rank:     .
