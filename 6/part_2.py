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

TIMES:
real    0m1.455s
user    0m1.446s
sys     0m0.008s

I implemented a halfway step between the fully algebraic and the brute force.
I still loop through to find half of all the numbers that are lower than the high
score. That loop does still effect our time quite a bit.

If I could derive how many possible numbers below the high score exist, then I don't
need any for loops.
"""

import re


# RELEGATED
def time_to_score(time: int, high_score: int):
    """This function gets all possible scores higher than high_score
    for a given input time, and returns the sum of that list."""
    res = []
    for x in range(1, time):
        diff = time - x
        score = x * diff
        if score > high_score:
            res.append(score)

    return len(res)


def time_to_score_quad(time: int, high_score: int):
    """This function gets all possible scores higher than high_score
    for a given input time, and returns the sum of that list.

    This version of the algorithm is a bit faster. All I need to know is how many total
    scores are possible, and how many are below high_score.
    """

    # This is the easiest fix for my off by 1 error.
    time += 1
    low_scores = 0
    # If I do binary search here with an enumerate,
    # Then I can figure out low_scores quicker.
    for x in range(0, time):
        diff = time - x
        score = x * diff
        if score < high_score:
            low_scores += 1
        else:
            break

    return time - (low_scores * 2)


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
    # answer = time_to_score(time, high_score)
    answer = time_to_score_quad(time, high_score)
    print(answer)


part_2("input.txt")

# Answer: 27340847
