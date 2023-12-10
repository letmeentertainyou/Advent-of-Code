#!/bin/python3
"""
NOT SOLVED:

I'm just committing my work so far. This is my first graph problem so I just focused on learning about the data structure today.

Tomorrow I will study path finding, and work on the problem. I suspect I will do well with part 2 because I took the time
to build the graph right. If you are struggling with day 10 maybe this graph outline will help you.

I haven't written a function to solve which direction S goes yet. I'm just using a hardcoded value for S. I will add that function
after solving the path finding.

I know using y, x instead of x, y is confusing but that is how I read the file as rows and then columns.
"""


def hash(y: int, x: int):
    return f"Y{y}X{x}"


def get_coords(char, y, x):
    """I made this into a function so that I could use it with different y, x values. This function will
    also help with solving for what S is supposed to be by checking the characters next to S to see if they connect
    with S."""
    directions = {
        "-": ((y, x - 1), (y, x + 1)),
        "|": ((y - 1, x), (y + 1, x)),
        "L": ((y - 1, x), (y, x + 1)),
        "J": ((y - 1, x), (y, x - 1)),
        "7": ((y + 1, x), (y, x - 1)),
        "F": ((y + 1, x), (y, x + 1)),
    }
    return directions.get(char, ())


# These single letter names are confusing but this feels right
# Some nodes can be dead ends but I think that still matters for getting the count.
def add_node(y, x, char, len_file, len_line, file):
    """We check if char is a valid node character and then if it is we check if
    it has any neighbor nodes that connect with it according to the text of the rules.
    The neighbor nodes are what we return because that's what our graph dict needs for a value.
    get_coords() is the real hero here!
    """

    def validate(Y, X):
        """
        Do a bounds check to see if any of the new coords are legal, and then check if there
        are any connecting nodes on the other side of the edge.
        """
        # These are bounds checks
        if not -1 < Y < len_file:
            return False
        if not -1 < X < len_line:
            return False

        # This is to cross reference that the next node connects with the old one.
        next_char = file[Y][X]
        next_chords = get_coords(next_char, Y, X)
        # print(any(c == (y, x) for c in next_chords))
        return any(c == (y, x) for c in next_chords)

    coords = get_coords(char, y, x)
    node = []
    for coord in coords:
        if validate(*coord):
            node.append(hash(*coord))
    return node


# My S is a | node but I should probably come up with a way to calculate what S will be
# So that anyone else can use this code too.
def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    graph = {}
    len_file = len(file)

    for y, line in enumerate(file):
        len_line = len(line)
        for x, char in enumerate(line):
            if char == "S":
                # S is hardcoded, an additional challenge is to write a function that solves for S.
                # If you know what char your start is then hardcode it below.
                node = add_node(y, x, "|", len_file, len_line, file)
                start = node

            node = add_node(y, x, char, len_file, len_line, file)
            graph[hash(y, x)] = node

    # Start by looping through the keys in start
    # And then apply a path finding algorithm,
    # Maybe only one start key is required because it's a cycle.
    for key in start:
        ...  # find the path here.


part_1("input.txt")

# Answer: NOT SOLVED YET
