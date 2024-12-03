#!/bin/python3
"""
The goal here was to find any characters in a given string that represent an integer. So I used
ord() with the range of 48-57 inclusive, which covers the 0-9 in ASCII. 

All I did was append every integer in the give line of the file to a variable called tmp_chars
and then I made a string with the first and last characters of tmp_chars.

I convert that two character string into an int. This should never fail if got the ord() math right.
I add all of those digit numbers into a list called results and the last thing we do is sum(results).

This problem was fairly simple but part two really got my thinking.
"""


def part_1(filename: str):
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    results = []
    int_range = list(range(48, 58))
    for line in file:
        tmp_chars = ""
        for char in line:
            if ord(char) in int_range:
                tmp_chars += char

        tmp_string = tmp_chars[0] + tmp_chars[-1]
        results.append(int(tmp_string))
    print(sum(results))


part_1("input.txt")

# Answer: 56465
