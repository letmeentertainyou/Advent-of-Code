#!/bin/python3
"""
The hardest part of this was figuring out how to access the first element of
a sublist to match it with the labels. It also took reading the instructions like five
times to understand all the crazy stuff happening here.

Overall it was a really fun day!

Again the test data was helpful, as well as the step by step walk through. I referred
to the question page many times while debugging this!
"""


# I modified this to split off the labels.
def hash(string: str) -> str:
    """Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256."""

    if "-" in string:
        string = string.split("-")[0]

    elif "=" in string:
        string = string.split("=")[0]

    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def solve(k, v):
    """Returns the score for the given k, v pair!"""
    if len(v) == 0:
        return 0

    score = 0
    for index, item in enumerate(v):
        score += (1 + k) * (index + 1) * int(item[1])
    return score


# This is my most complcaiated undocumented function yet.
def find_and_replace(values, label, focus):
    """This is a bit like string.replace but it works with finding a match
    to the first value in a list of tuples/lists. It's a bit weird."""

    for i, pair in enumerate(tuple(values)):
        if pair[0] == label:
            values[i] = [label, focus]
            return values
    values.append([label, focus])
    return values


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read()

    strings = file.strip().split(",")
    boxes = {key: [] for key in range(256)}
    for s in strings:
        h = hash(s)
        val = boxes[h]

        if "-" in s:
            dash_lab = s.split("-")[0]
            for item in val:
                if item[0] == dash_lab:
                    boxes[h] = [v for v in val if v[0] != dash_lab]

        if "=" in s:
            s_split = s.split("=")
            boxes[h] = find_and_replace(val, *s_split)

    answer = 0
    for k, v in boxes.items():
        answer += solve(k, v)

    print(answer)


part_2("input.txt")

# Answer: 265894
# Test: 145
