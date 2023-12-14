#!/bin/python3
"""
I'm still working on the last couple days. I was taking a mini break but this one seemed easy enough so I tried it.

It took me a few minutes to find some logic errors but overall I'm really happy with how this one went. It
was really nice to use the test data. I'm going to do that a lot more often.
"""


# I asked Chat GPT for help with this function because I manually write this code every time.
# I let GPT write it's own doc strings.
def is_valid_index_pair(array, x, y):
    """This function returns True if both x and y are within the valid range of indexes for the given 2D array, and False otherwise.
    It first checks if x is a valid row index (i.e., it’s between 0 and the number of rows), and then checks if y is a valid column index
    (i.e., it’s between 0 and the number of columns)."""
    num_rows = len(array)
    num_cols = len(array[0]) if num_rows > 0 else 0
    return 0 <= x < num_rows and 0 <= y < num_cols


def shift(file, x, y):
    """This code should be robust enough to work with any of the other four directions. I hope that's relevant for part 2."""

    # This is a little ugly with the double breaks but I didn't feel like making a recursive function.
    while True:
        X, Y = (x - 1, y)
        if is_valid_index_pair(file, X, Y):
            if file[X][Y] == ".":
                file[X][Y], file[x][y] = file[x][y], file[X][Y]
                x = X
                y = Y
            else:
                break
        else:
            break
    return file


def score(shifted_file):
    """I learned about str.count() for this one. Just get the count of the "O"s and then do some index math."""
    score = 0
    for index, line in enumerate(shifted_file):
        score += line.count("O") * (len(shifted_file) - index)

    return score


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = [list(l.strip()) for l in tmpfile.readlines()]

    for x, line in enumerate(tuple(file)):
        for y, char in enumerate(line):
            if char == "O":
                file = shift(file, x, y)

    answer = score(file)
    print(answer)


part_1("input.txt")

# Answer: 107142
# Test: 136
