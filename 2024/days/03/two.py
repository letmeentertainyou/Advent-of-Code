#!/bin/python3.10
"""
I wasted over an hour trying to do such a complex regex solution and after I got my answer
I found out there is a much more elegant solution. 

I'm sharing the split() solution because it's my preference, it's fast, it's easy to read, 
and usually str.split() is my go to on AoC but I got my brain on regex and completely missed 
the neat solution. I hope I can use my new messy regex skills on a later day.

The other reason I went with this style of presentation is that I like the symmetry of a having
the solve() function be identical across part 1 and part 2.
"""
import re

from sys import argv


def solve(file: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)"
    answer = 0
    match = re.findall(pattern, file)

    if match:
        for pair in match:
            x = int(pair[0])
            y = int(pair[1])
            answer += x * y

        return answer
    return 0


def parse_input(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read()

    answer = 0
    dos = file.split("do()")
    for do in dos:
        donts = do.split("don't()")
        answer += solve(donts[0])

    print(answer)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     48
# Answer:   78683433
# Rank:     12004
