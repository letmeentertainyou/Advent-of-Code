#!/bin/python3
"""
Now I only care about asterisk that touch two numbers. So I check every char if it's is an asterisk.

Then I make a smaller dict of every number that asterisk touches, and if
that asterisk touches two numbers, I multiple them together and add them to a running sum.

This should just require a few modifications. The main change is that instead of a global
PART_IDS dict, I now have a local part_ids dict and I have to manually pass that around
everywhere and update it.

Now that I have multiple functions passing four args it seems line OO could help out a bit.
But I'm not refactoring this because I have to do day 4.
"""

from math import prod


# This function isn't typed hinted because Black Formatter refactors long lines
def find_integer(char, line, line_index, char_index, part_ids) -> dict:
    """
    We check if there is an integer at line[char_index], and if there is we need to know if there are
    any numbers to the left or right.

    We reduce start_index any time we find numbers on the left.
    And we increase end_index anytime we find numbers on the right.

    Then we take those two indexes, add the number with it's indexes as a hash to part_ids
    and we return part_ids.
    """
    if ord(char) in range(48, 58):
        # complete_number(line, line_index, char_index)

        start_index = char_index
        end_index = char_index  # + 1
        int_range = list(range(48, 58))
        while start_index - 1 >= 0:  # LEft
            if ord(line[start_index - 1]) in int_range:
                start_index -= 1
            else:
                break

        while end_index + 1 < len(line):  # RIGHT
            if ord(line[end_index + 1]) in int_range:
                end_index += 1
            else:
                break

        part_ids[f"line:{line_index}char:{start_index}"] = line[
            start_index : end_index + 1
        ]
    return part_ids


# This function isn't typed hinted because Black Formatter refactors long lines
def check_positions(line, line_index, char_index, part_ids) -> dict:
    """
    This function checks the left, center, and right indexes that an asterisk touches.
    """
    if char_index - 1 >= 0:
        part_ids = find_integer(
            line[char_index - 1], line, line_index, char_index - 1, part_ids
        )

    part_ids = find_integer(line[char_index], line, line_index, char_index, part_ids)

    if char_index + 1 < len(line):
        part_ids = find_integer(
            line[char_index + 1], line, line_index, char_index + 1, part_ids
        )

    return part_ids


# This makes sure we only check line indexes that are in the file.
def symbol_scan(line_index: int, char_index: int, file) -> int:
    """
    This function checks the previous, current, and next line that a symbol touches.
    And stores any numbers found by those checks in a dict called part_ids, then
    if there are two unique keys in part_ids, their product is returned, otherwise
    zero is returned.
    """
    part_ids: dict = {}

    # Check three positions of line_index -1
    if line_index - 1 >= 0:
        part_ids = check_positions(
            file[line_index - 1], line_index - 1, char_index, part_ids
        )

    # Check left and right positions on file index
    part_ids = check_positions(file[line_index], line_index, char_index, part_ids)

    # Check three positions of line_index +1
    if line_index + 1 < len(file):
        part_ids = check_positions(
            file[line_index + 1], line_index + 1, char_index, part_ids
        )

    if len(part_ids) > 1:
        return prod([int(v) for v in part_ids.values()])
    else:
        return 0


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer: int = 0
    for line_index, line in enumerate(file):
        for char_index, char in enumerate(line.strip()):
            if char == "*":
                answer += symbol_scan(line_index, char_index, file)
    print(answer)


part_2("input.txt")

# Answer: 86841457
