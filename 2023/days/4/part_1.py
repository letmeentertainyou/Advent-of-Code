#!/bin/python3
"""
Some values are separated by two spaces. And that sucks but we can just check the len
and only add non empty strings. (Actually re.split is what I wanted to do.)

So take each line, split it into two lists,

Then count which of the items in list 1, are in list 2.
If count > 0 then return 2 ** (count -1) 

1 * 2    |  2 ** x
1        |  0
2        |  1
4        |  3
8        |  4
16       |  5 


if count == 0:
    return 0
if count > 0:
    return 2 ** (n -1)

That is the whole problem.

I'm not sure if there are any duplicates in array2, but I might run it through a set just in case.
In fact if I loop through array1, then I will only get 1 count per match and it doesn't matter if 
the input is janky. (I'm never gonna recover from how weird day 1 was.)
"""

import re


def match_arrays(array1, array2) -> int:
    """
    This function takes two arrays, and loops through the first array,
    checking if each entry is in array2 and adding one to the count for every
    match.

    Then it returns 0 for no matches, and otherwise 2 ** (count -1) as per the rules.
    """
    count: int = 0
    for item in array1:
        if item in array2:
            count += 1

    if count == 0:
        return 0

    elif count > 0:
        return 2 ** (count - 1)


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        line_split = line.strip().split(" | ")

        # This is a little messy, it's just making the two arrays of ints.
        # re.split handles some of the extra spaces that occur.
        array1 = re.split("\s+", line_split[0].split(": ")[1])
        array2 = re.split("\s+", line_split[1].lstrip())
        answer += match_arrays(array1, array2)

    print(answer)


part_1("input.txt")

# Answer: 24706
