#!/bin/python3.8
"""
I wasted about 10 minutes today fiddling with pip and pyenv in an attempt to install scipy and use a convolution that
I'd learned for solving connect four. But I don't think that solution would have lead me anywhere because I'm still a
bit confused about how to implement those. Then I worked on a more general brute force. 

It seems like we're getting ready to build a proper parse which I am excited for but it's frustrating attempting to
get a decent rank because I feel like I'm under the gun to finish the code quickly and that leads me to want to avoid
overly verbose structures.

I would love to find out that some of my previous code structures will work for future days, it doesn't usually seem
that way but I'm hopeful anyways.
"""
from sys import argv


def is_valid_index_pair(array, x, y) -> bool:
    len_rows = len(array)
    len_cols = len(array[0]) if len_rows else 0
    return 0 <= x < len_rows and 0 <= y < len_cols


def solve(grid):
    def search_dir(r, c, x, y):
        for i in range(len(word)):
            nr, nc = r + i * x, c + i * y
            if (not is_valid_index_pair(grid, nr, nc)) or (grid[nr][nc] != word[i]):
                return False
        return True

    word = "XMAS"
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    answer = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for x, y in dirs:
                if search_dir(row, col, x, y):
                    answer += 1

    print(answer)


def parse_input(filename: str) -> tuple:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    grid: list[list] = []
    for x, line in enumerate(file):
        grid.append([c for c in line.strip()])

    solve(grid)


if __name__ == "__main__":
    if len(argv) > 1:
        filename = "test.txt"
    else:
        filename = "input.txt"
    print(f"Parsing {filename}.")
    parse_input(filename)


# Test:     18
# Answer:   2644
# Rank:     7805
