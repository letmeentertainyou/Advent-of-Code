#!/bin/python3
"""
Each line of the file represents one game and several reveals. I split the line into each reveal
and then tested to see if those reveals are invalid. If all the reveals for a given game are valid 
then that game's number is added to the answer sum,
"""


def validate_reveal(reveal_dict: dict) -> bool:
    """Compare the input dict with the DATA dict, and return True or False."""
    DATA: dict = {
        "red": "12",
        "green": "13",
        "blue": "14",
    }

    for key in DATA.keys():
        if key in reveal_dict:
            # You can't compare numbers as strings because so these int casts are required.
            if int(reveal_dict[key]) > int(DATA[key]):
                return False
    return True


# There are a lot of spaces in the input data so I used split(char + space) several times below.
def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = 0
    for line in file:
        reveals = line.strip().split(": ")[1].split("; ")

        for reveal in reveals:
            reveal_dict: dict = {}
            for pair in reveal.split(", "):
                pair_split = pair.split(" ")
                reveal_dict[pair_split[1]] = pair_split[0]

            if not validate_reveal(reveal_dict):
                break

        # The rare for-else statement
        else:
            value = int(line.split(":")[0][5:])
            answer += value

    print(answer)


part_1("input.txt")

# Answer: 2156
