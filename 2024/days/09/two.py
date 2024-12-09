#!/bin/python3.10
"""
This is by far my sloppiest code yet and I fell into a second foot gun. Basically the test data passed for
me for both parts when my actual data did not. It took forever to figure out what I was doing wrong but
technically the rules did state what I need to do correctly.

Overall, I pretty much hated this one. It started easy enough but it just got so messy while I was trying to solve it.
"""

from sys import argv


class R:
    def __init__(self, start, end, length, value="."):
        self.start = start
        self.end = end
        self.length = length
        self.value = value

    def __str__(self):
        return f"{self.start}, {self.end}, {self.length}, {self.value}"


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


def find_ranges(line):
    nums, periods = [], []
    length = 0
    old = line[0]
    start = 0
    # print(line)
    for i, c in enumerate(line):
        if c == old:
            length += 1
        else:
            end = start + length - 1
            if old == ".":
                periods.append(R(start, end, length))
            else:
                nums.append(R(start, end, length, old))
            length = 1
            old = c
            start = i
    if old == ".":
        periods.append(R(start, start + length - 1, length))
    else:
        nums.append(R(start, start + length - 1, length, old))
    # print(nums)
    # print([str(n) for n in nums])
    nums = sorted(nums, key=lambda x: x.value)[::-1]
    # print([str(n) for n in nums])
    # quit()
    return nums, periods


def old_find_ranges(line):
    n_indexes = [(i, c) for i, c in enumerate(line) if c != "."]
    value = n_indexes[0][1]
    start = n_indexes[0][0]
    length = 0
    res = []

    for x, y in n_indexes:
        if y == value:
            length += 1
        else:
            end = (start + length) - 1
            res.append(R(start, end, length, value))
            value = y
            start = x
            length = 1
    else:
        res.append(R(start, (start + length) - 1, length, value))
    return sorted(res, key=lambda x: x.value)[::-1]


def find_consecutive(line):
    p_indexes = [i for i, c in enumerate(line) if c == "."]
    start = p_indexes[0]
    end = start
    length = 1
    result = []
    for i in range(1, len(p_indexes)):
        if p_indexes[i] == end + 1:
            end = p_indexes[i]
            length += 1
        else:
            result.append(R(start, end, length))
            start = p_indexes[i]
            end = start
            length = 1
    return result


def mem_shift(line: list, nums: list[R], periods: list[R]):
    """
    00...111...2...333.44.5555.6666.777.888899
    00992111777.44.333....5555.6666.....8888..
    """

    # ranges: list[R] = find_ranges(line)
    # con: list[R] = find_consecutive(line)
    # print(line)
    for r in nums:
        l = r.length
        for _i, c in enumerate(periods):
            # This is the second footgun that the example didn't have.
            if r.start < c.start:
                break

            if l <= c.length:
                for buff in range(l):
                    i1 = r.end - buff
                    i2 = c.start + buff
                    line[i1], line[i2] = line[i2], line[i1]
                c.start += l
                c.length -= l
                break
    # print(line)
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

    answer = 0
    file = mem_map(file)
    nums, periods = find_ranges(file)
    file = mem_shift(file, nums, periods)
    answer += check_sum(file)

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     2858
# Answer:   6301361958738
# Rank:     .
