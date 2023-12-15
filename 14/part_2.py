#!/bin/python3
"""
I'm still working on the last couple days. I was taking a mini break but this one seemed easy enough so I tried it.

It took me a few minutes to find some logic errors but overall I'm really happy with how this one went. It
was really nice to use the test data. I'm going to do that a lot more often.

This one took me awhile to wrap my head around how to do the cycles. I thought I needed some really complicated algorithm
but I just needed to hash a 2d array. I was trying to store the scores for each position but it's possible to reach the same
score with different board states. Hashing a board state is a really neat idea!
"""


# I asked Chat GPT for help with this function because I manually write this code every time.
# I let GPT write it's own doc strings.
def is_valid_index_pair(array, x, y):
    """This function returns True if both x and y are within the valid range of indexes for the given 2D array, and False otherwise.
    It first checks if x is a valid row index (i.e., it’s between 0 and the number of rows), and then checks if y is a valid column index
    (i.e., it’s between 0 and the number of columns)."""
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def shift(file, x, y):
    while True:
        X, Y = (x - 1, y)
        if is_valid_index_pair(file, X, Y) and file[X][Y] == ".":
            file[X][Y], file[x][y] = file[x][y], file[X][Y]
            x, y = X, Y
        else:
            break

    return file


def shift_file(file):
    for x, line in enumerate(tuple(file)):
        for y, char in enumerate(line):
            if char == "O":
                file = shift(file, x, y)
    return file


def rotate_file(file):
    return [list(reversed(x)) for x in zip(*file)]


def score(shifted_file):
    """I learned about str.count() for this one. Just get the count of the "O"s and then do some index math."""
    score = 0
    for index, line in enumerate(shifted_file):
        score += line.count("O") * (len(shifted_file) - index)

    return score


def quadrate(file):
    "Shifts and rotates the file four times."
    for _ in range(4):
        file = shift_file(file)
        file = rotate_file(file)
    return file


def hash(file):
    """If I can hash my grid then I will know when it repeats."""
    h = [y for x in file for y in x]
    return str(h)


# Find the index at which is becomes a cycle them do
# dist = (1_000_000_000 - (start + 1)) % length
def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = [list(l.strip()) for l in tmpfile.readlines()]

    cycles = []
    for i in range(1000):
        file = quadrate(file)
        h = hash(file)
        if h in cycles:
            start = cycles.index(h)
            length = i - start
            break
        cycles.append(h)

    dist = (1_000_000_000 - (start + 1)) % length
    for _ in range(dist):
        file = quadrate(file)

    answer = score(file)
    print(answer)


part_2("input.txt")

# Answer: 104815
# Test: 64
