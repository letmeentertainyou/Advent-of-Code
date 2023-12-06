#!/bin/python3
"""
The only difference here is that instead of four races we have one single race
with larger numbers. I thought this might be too big to brute force but nope.

TIMES:
real    0m6.445s
user    0m5.897s
sys     0m0.547s

I would optimize this but it's fast enough. I believe I can solve it instantly in the way
I described above time_to_score. I will probably post that solution tomorrow.
"""

import re


# Probably can't brute force this with such large numbers so
# I will need an equation to calculate all the high scores.
# All I need to know is how many total scores are possible
# And how many are below high_score
# Plus the odd/even thing.
def time_to_score(time: int, high_score: int):
    """This function gets all possible scores higher than high_score
    for a given input time, and returns the sum of that list."""
    res = []
    for x in range(1, time):
        diff = time - x
        score = x * diff
        if score > high_score:
            res.append(score)

    if len(res) > 0:
        return len(res)

    # Since this is a prod and not a sum.
    else:
        return 1


def parse_weird_input(line: str):
    """This combines all the ints on a given line as a string,
    and then returns that string as an int."""
    split = re.split("\s+", line.strip().split(":")[1].lstrip())
    str_number = "".join(split)
    return int(str_number)


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    time = parse_weird_input(file[0])
    high_score = parse_weird_input(file[1])
    answer = time_to_score(time, high_score)
    print(answer)


part_2("input.txt")

# Answer: 27340847
