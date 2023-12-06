#!/bin/python3
"""
Implement the time/distance/speed equation.
Then parse the doc.
Count all scores higher than the high score
Product all the counts.

*** Got this ine one, I hope part two is kind.
"""

import re


def time_to_score(time: int, high_score: int):
    # Get all possible scores for a given input time.
    # Then return that.
    # You only need to do half the work because it mirrors.
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


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    times = re.split("\s+", file[0].strip().split(":")[1].lstrip())
    high_scores = re.split("\s+", file[1].strip().split(":")[1].lstrip())

    answer = 1
    for t, s in zip(times, high_scores):
        answer *= time_to_score(int(t), int(s))

    print(answer)


part_1("input.txt")

# Answer: 138915
