#!/bin/python3
"""
This one seems really hard, I'm going to focus on identifying the symbols first, and then I will
build an engine to find each adjacent number.

The issue I see here is that if a single number touches two symbols then that number will be 
added into the sum twice. I read over my input and didn't see any such instances but I'm not
ruling it out after I got burned by the input so bad on day 1.

I need a custom hash table. Basically every number that is triggered by a symbol needs to go into a dict
with the key of str(line_index+char_index+number). Then if that number gets triggered for that once it overwrites
itself in the hash table. Next we just need to sum the values in the dict. (And implement symbol_scan.)

This was by far the hardest problem, and I had to use someone else's solution to see what my number should be. I did not
read their code. I got stuck with a best guess of 557167 and at that point I was no longer getting lower/higher clues.

My error was a single minus sign in the place of a plus sign. I realize this solution is convoluted as hell. But the problem
was really really difficult. If I had a simpler solution I would not have fallen prone to that simple syntax error.

In the end I was failing to sum the last line of the file not because my logic was flawed but because I typed my logic
incorrectly.

I was so burned by day one that I kind of over-engineered my solution here but it worked in my favor because numbers could
have been counted twice in several different ways.
"""

# This dict will have unique hashes for every valid part number
# When a number is found in two places it should get the same hash
# And therefore only one entry in the dict.
PART_IDS: dict = {}


def find_integer(char: str, line: str, line_index: int, char_index: int):
    """
    We check if there is an integer at line[char_index], and if there is we need to know if there are
    any numbers to the left or right.

    We reduce start_index any time we find numbers on the left.

    And we increase end_index anytime we find numbers on the right.

    Then we take those two indexes, add the number with it's indexes as a hash to PART_IDS.
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

        PART_IDS[f"line:{line_index}char:{start_index}"] = line[
            start_index : end_index + 1
        ]


# This makes sure we only check char indexes that are in the line
def check_positions(line: str, line_index: int, char_index: int):
    """
    This function checks the left, center, and right indexes that a symbol touches.
    """
    if char_index - 1 >= 0:
        find_integer(line[char_index - 1], line, line_index, char_index - 1)

    find_integer(line[char_index], line, line_index, char_index)

    if char_index + 1 < len(line):
        find_integer(line[char_index + 1], line, line_index, char_index + 1)


# This makes sure we only check line indexes that are in the file.
def symbol_scan(line_index: int, char_index: int, file: str):
    """
    This function checks the previous, current, and next line that a symbol touches.
    """

    # Check three positions of line_index -1
    if line_index - 1 >= 0:
        check_positions(file[line_index - 1], line_index - 1, char_index)

    # Check left and right positions on file index
    check_positions(file[line_index], line_index, char_index)

    # Check three positions of line_index +1
    if line_index + 1 < len(file):
        check_positions(file[line_index + 1], line_index + 1, char_index)


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()
    chars = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for line_index, line in enumerate(file):
        for char_index, char in enumerate(line.strip()):
            if char not in chars:
                symbol_scan(line_index, char_index, file)

    print(sum([int(v) for v in PART_IDS.values()]))


part_1("input.txt")

# Answer: 559667
