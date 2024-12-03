#!/bin/python3
"""
This part is literally just inverting one single step. It might be the easiest part 2.

The only problem I ran into is the order of the terms flr example: x + y is the same as y + x .
But that is not true with subtraction.
"""


def diff(list_of_ints):
    """I have no clue why -1 * (a - b) worked and abs(a - b) didn't. But now my output matches
    numpy's and who am I to argue with numpy?"""
    res = []
    for i, v in enumerate(list_of_ints[:-1]):
        res.append(-1 * (v - list_of_ints[i + 1]))
    return res


def all_zeroes(list_of_ints):
    """
    This is pretty straightforward and it could be inlined but it's a lot
    of chars and I'm using it in a while loop so this is cleaner.

    This might be a little slower than the custom for loop because all()
    doesn't have a break-early option. So it is comparing every item even
    after the first non zero is found. Trying a generator to see if that
    breaks early.
    """
    return all(x == 0 for x in list_of_ints)


def solve(list_of_values):
    """Work out the differences until they are all zero, and then
    work out the next value backwards.
    """
    res = [list_of_values]
    while not all_zeroes(res[-1]):
        res.append(diff(res[-1]))

    backwards = res[::-1]
    for index, arr in enumerate(tuple(backwards[:-1])):
        next_arr = backwards[index + 1]
        next_value = next_arr[0] - arr[0]
        next_arr.insert(0, next_value)

    return backwards[-1][0]


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        answer += solve([int(v) for v in line.strip().split(" ")])

    print(answer)


part_2("input.txt")

# Answer: 803
