#!/bin/python3
"""I bought the Awk book, and when I get further in it, I'm going to use Awk for this
score!"""


def line_parse(line: str):
    line_split = line.strip().split(": ")
    key = line_split[0]
    part1, part2 = [int(i) for i in line_split[1].split(" ")]
    return key, part1, part2


def sum_dict(scores) -> int:
    score = 0
    for v in scores.values():
        score += sum(v)
    return score


def best_three_days(scores):
    res = []
    for k, v in scores.items():
        res.append([sum(v), k])

    res = sorted(res)
    for day in res[:3]:
        print(f"{day[1]}: {day[0]}")
    return res


def score_ranks(filename):
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    scores = {}
    for line in file[1:]:
        key, part1, part2 = line_parse(line)
        scores[key] = [part1, part2]

    print(f"Your high score is: {sum_dict(scores)}")
    print(f"Your best part 1 is: {min(scores.values(), key=lambda v: v[0])[0]}")
    print(f"Your best part 2 is: {min(scores.values(), key=lambda v: v[1])[1]}")
    print(f"Your best three days are:")
    best_three_days(scores)


score_ranks("RANKS.txt")

# Day 8 score: 592322
