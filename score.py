#!/bin/python3
"""I bought the Awk book, and when I get further in it, I'm going to use Awk for this
score!"""

# Expand this script to give me a top three days
# And a top part 1
# and a top part 2.
# I will need a data structure that keeps count of the Days and the parts.


def line_sum(line: str):
    return sum(int(i) for i in line.split(" "))


with open("RANKS.txt", "r", encoding="UTF-8") as tmpfile:
    file = tmpfile.readlines()

score = 0
for line in file[1:-1]:
    score += line_sum(line.strip().split(": ")[1])

print(score)

# Six day score, lower is better,
# 501150
