#!/bin/python3
"""
This was a pretty straight forward problem. You can never go wrong with
a little HASHMAP!
"""


def hash(string: str) -> str:
    """Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256."""
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.read()

    answer = 0
    strings = file.strip().split(",")
    for s in strings:
        answer += hash(s)

    print(answer)


part_1("input.txt")

# Answer: 515974
# Test: 1320
