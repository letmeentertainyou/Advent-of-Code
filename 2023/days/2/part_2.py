#!/bin/python3
"""
The goal here is to find the highest number for each color in a line. Then multiple the values 
for red, green, blue and add that product to a running sum of all the lines. That sum is the answer.
"""

from math import prod


def update_minimums(reveal_dict: dict, mins) -> None:
    """
    This function updates the given mins dict to keep track of the smallest
    possible numbers for each color.
    """
    for key in mins.keys():
        if key in reveal_dict:
            # You can't compare numbers as strings because so these int casts are required.
            if int(reveal_dict[key]) > int(mins[key]):
                mins[key] = reveal_dict[key]


# There are a lot of spaces in the input data so I used split(char + space) several times below.
def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        reveals = line.strip().split(": ")[1].split("; ")
        minimums = dict.fromkeys(["red", "green", "blue"], "0")

        for reveal in reveals:
            reveal_dict: dict = {}
            for pair in reveal.split(", "):
                pair_split = pair.split(" ")
                reveal_dict[pair_split[1]] = pair_split[0]

            update_minimums(reveal_dict, minimums)

        value = prod([int(v) for v in minimums.values()])
        answer += value

    print(answer)


part_2("input.txt")

# Answer: 66909
