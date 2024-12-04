#!/bin/python3.10

from math import inf


def line_parse(line: str):
    line_split = line.strip().split(": ")
    key = line_split[0]
    part1, part2 = [int(i) if int(i) > 0 else inf for i in line_split[1].split(" ")]
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


def average(scores: list, idx: int):
    total = sum([s[idx] for s in scores.values()])
    return total // len(scores)


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
    print(f"You average scores p1: {average(scores, 0)}, p2: {average(scores, 1)}")


score_ranks("RANKS.txt")
