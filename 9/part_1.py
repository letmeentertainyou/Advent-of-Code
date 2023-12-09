#!/bin/python3
"""
Dang I lost a lot of time on this one because I tried writing the diff algorithm myself and I was failing
somewhere. I finally looked up how to diff a list of ints and used numpy.diff which instantly gave me the
correct answer. With my own version of diff the sample data worked fine but a few of my more complicated
inputs were not reducing to all zeroes.

I think it has to do with negative numbers and even though I was using abs I was still getting a wrong answer.
I really wish they would have shown negative numbers in the sample since they are in the real data.

This can be sped-up a lot by removing the numpy import, I will do that tomorrow.

---

I removed numpy.diff and now it's about 5x faster without the numpy import taking a few hundred milliseconds.

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
    after the first non zero is found.
    """
    return all([x == 0 for x in list_of_ints])


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
        next_value = arr[-1] + next_arr[-1]
        next_arr.append(next_value)

    return backwards[-1][-1]


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        answer += solve([int(v) for v in line.strip().split(" ")])

    print(answer)


part_1("input.txt")

# Answer: 1681758908


"""
# I'm leaving my old diff code here so that I can
# do a post-mortem on why it failed tomorrow.
# My answer seems broken so I'm trying numpy

def get_differences(list_of_ints):
    diff = list(numpy.diff(list_of_ints))
    return diff

    res = []
    for i, v in enumerate(list_of_ints[:-1]):
        res.append(abs(v - list_of_ints[i + 1]))
    return res

"""
