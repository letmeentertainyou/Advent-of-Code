#!/bin/python3
"""
This is my first graph problem so I just focused on learning about the data structure today.

I haven't written a function to solve which direction S goes yet. I'm just using a hardcoded value for S. 
I will add that function after solving the path finding.

I know using y, x instead of x, y is confusing but that is how I read the file as rows and then columns.

This was fun to solve my first graph problem without external resources!
"""


def hash(y: int, x: int):
    return f"Y{y}X{x}"


def get_coords(char, y, x):
    """I made this into a function so that I could use it with different y, x values. This function will
    also help with solving for what S is supposed to be by checking the characters next to S to see if they connect
    with S."""

    # This function needs a hardcoded case for S because it might be called with S from other nodes.
    # This should call a function that solves for S so it isn't hard coded.
    if char == "S":
        char = "|"

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
        return any(c == (y, x) for c in next_chords)

    coords = get_coords(char, y, x)
    node = []
    for coord in coords:
        if validate(*coord):
            node.append(hash(*coord))
    return node


def calculate_distance(start, graph):
    """This function took me a while to debug but we got there in the end!

    # Pick one of the nodes in start and then walk through keep track of he node
    # You came from until we get back to start.
    # Count the distance.
    """
    prev = start
    next = graph[start][1]
    count = 1
    while next != start:
        val = graph[next]
        for v in val:
            if v != prev:
                new = v
                break
        prev = next
        next = new
        count += 1
    return count // 2


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    graph = {}
    len_file = len(file)

    for y, line in enumerate(file):
        len_line = len(line)
        for x, char in enumerate(line):
            if char == "S":
                start = hash(y, x)
            node = add_node(y, x, char, len_file, len_line, file)
            if node:
                graph[hash(y, x)] = node

    answer = calculate_distance(start, graph)
    print(answer)


part_1("input.txt")

# Answer: 6820
