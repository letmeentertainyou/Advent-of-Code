#!/bin/python3
"""
For part 2 all we have to is change how we calculate the initial seeds dict.
Although all that extra data might make my solution too slow.

I don't know range math, and I didn't use it. I hope to speed up my solution tomorrow
but I really wasn't expecting this much difficulty until day 10+ and I'm not super inspired
to keep working on it if every day is this hard.

I tried to brute force this forwards and it would have taken weeks to calculate. Then I went with
brute forcing it backwards and it took three minutes.

TIMES:
real    3m23.646s
user    3m23.245s
sys     0m0.252s

Wow. It literally took me 23 hours to write a good brute force solution to this problem.
Advent of Code was fun last year. I really hope day 6 is a nice break from the tedium..
"""


def assemble_seeds(line):
    seed_split = line.strip().split(" ")[1::]
    starts = []
    lengths = []

    for i, v in enumerate(seed_split):
        if i % 2 == 0:
            starts.append(int(v))
        else:
            lengths.append(int(v))
    seeds = dict(zip(starts, lengths))

    return seeds


def assemble_maps(file):
    maps = {}
    index = 0
    for line in file:
        if line == "\n":
            index += 1
        elif ":" not in line:
            entry = [int(i) for i in line.strip().split(" ")]
            if index not in maps:
                maps[index] = [entry]
            else:
                maps[index].append(entry)
    for key in maps.keys():
        maps[key] = sorted(maps[key])

    return maps


def apply_maps(guess, maps):
    for map in reversed(maps.values()):
        old = guess

        for entry in map:
            if guess != old:
                break
            a, b, c = entry
            if a <= guess < a + c:
                diff = guess - a
                guess = b + diff

    return guess


def is_seed(guess, seeds):
    for start, length in seeds.items():
        if start <= guess <= start + length:
            return True
    return False


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    seeds = assemble_seeds(file[0])
    maps = assemble_maps(file[2:])

    for map in list(maps.values())[-1]:
        print(map)
        for guess in range(map[0], map[0] + map[2] + 1):
            # print(guess)
            seed = apply_maps(guess, maps)
            if is_seed(seed, seeds):
                print(guess)
                return


part_2("input.txt")

# Answer: 11554135
