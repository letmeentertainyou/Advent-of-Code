#!/bin/python3
"""
NOT SOLVED:
I'm taking these later days a bit slower so that I can get to the heart of the problem. 
I'm pretty sure there is a simple math application to finish this one and I will try to
find it tomorrow. So this code just represents how far I got tonight.

I got all the ranges in a given line that can be a faulty spring. Now I just need to find
a clean implementation of permutations that keeps track of the rules of this game.

One step to simplify this is that the order of the groupings matter
3 2 1 does not match 1 2 3 etc so you can use that as a sort of map.
"""


def get_ranges(springs):
    "These are all the ranges that can contain a spring."

    # Save time when we there is only one range.
    if "." not in springs:
        return [range(len(springs))]

    # This feels sloppy with all the extra variables, I'm guessing regex is the way to go here.
    ranges = []
    active = False
    for index, char in enumerate(springs):
        if char != "." and not active:
            start = index
            active = True

        if char == "." and active:
            ranges.append(range(start, index))
            active = False

    return ranges


# For a permutation to be valid there needs to be x characters to the right
# Where x is sum(remaining group members) + len(remaining group members)
# So the permutations function backtracks when that rule is broken

# You need to know what the contiguous ranges are and which of them can be subdivided.
# The max number of ranges including sub division needs to match len(groups)


def solve(springs, groups):
    """Figure out the possible ranges in springs (can be sub function)
    apply the map of groups to those ranges, count permutations (or whatever)
    and return sum."""

    # This should be a simple range permutation problem but I don't know the elegant answer yet.
    # Do I loop through ranges or groups?
    # how many ways can our groups fit into the springs map accounting for the ?s ?
    def r(ranges, groups):
        """This is the inner recursive function for counting the permutations."""
        return 0

    ranges = get_ranges(springs)
    score = r(ranges, groups)
    return score


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        lsplit = line.split()
        springs = lsplit[0]
        groups = lsplit[1].split(",")
        answer += solve(springs, groups)

    print(answer)


part_1("_test.txt")

# Answer:
# Test: 21
