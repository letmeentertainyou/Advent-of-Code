#!/bin/python3.10
"""
If a line is determined to be unsafe then try again with one number missing
recursively cover all of the slices with one number removed, if any of those
iterations are safe, then the line is safe.
"""
from sys import argv


def find_safe(line: list[int]) -> bool:
    # determine if the line ascends or descends
    s = sorted(line)
    if not ((line == s) or (line[::-1] == s)):
        return False

    for i, current in enumerate(line):
        # This avoids an index error.
        if i + 1 < len(line):
            diff = abs(current - line[i + 1])
            # if not (1 <= diff <= 3):
            #    return False
    return True


def solve(lines) -> None:
    answer = 0
    for line in lines:
        if find_safe(line):
            answer += 1
            continue

        # This recursively checks each other version of the array slicing away the current index.
        for i in range(len(line)):
            if find_safe(line[:i] + line[i + 1 :]):
                answer += 1
                break

    print(answer)


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    lines = []
    for x, line in enumerate(file):
        split_line = [*map(int, line.split(" "))]
        lines.append(split_line)

    solve(lines)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:      4
# Answer:    589
# Rank:      5157
