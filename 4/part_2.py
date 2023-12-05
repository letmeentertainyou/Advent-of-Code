#!/bin/python3
"""
Make an answer dict with each line number as a key and the default value as 1. 
Then as each line happens, our function will increase the values of each key
in the dict.

And at the end we sum all the values in the dict.

---

TIMES:
real    0m2.613s
user    0m2.597s
sys     0m0.016s
O(N * ((A * B) + C * D))

In terms of big O I see several different factors. 

First is the length of the file called N.
Then you have the two arrays found in each line, and they are different lengths.
So array1 is called A, and array2 is called B.

The original algorithm did the next work in a time of count * line_multiplier (the values stored
in the answer dict.) And those variables are C and D respectively.

---

I removed the C above for my fast solution. But then D got renamed to C for ease of reading. Now
instead of adding one count times, I just add that count one time.

TIMES
real    0m0.049s
user    0m0.042s
sys     0m0.008s
O(N * ((A * B) + C))
"""

import re


# Tomorrow work out this algorithm in Big O and see if it can be reduced.
def recursive_match_arrays(array1, array2, answer, index) -> dict:
    """
    This function isn't actually recursive but it does have a double nested
    for loop so it still takes a few seconds. Basically we just get our winning number
    (count) and then we modify the answer dictionary x times for the amount of work our
    current line has to do (1 iteration for line 0).
    """
    count: int = 0
    for item in array1:
        # Can I get time by using a hash table to store array2, how much time does the python
        # membership test cost? Is it O(log N)? It seems like set() is already much faster than
        # list. I wonder if it improves my speed at all.

        # Nah, sets aren't really faster here. The bulk of the computation is below.
        if item in array2:
            count += 1

    if count > 0:
        # This optimization was stolen from /u/anskak on Reddit.
        # I read their comment and it changed my life.
        for i in range(1, count + 1):
            answer[index + i] += answer[index]

    return answer


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    answer = {k: 1 for k in range(len(file))}
    for index, line in enumerate(file):
        line_split = line.strip().split(" | ")

        # This is a little messy, it's just making the two arrays of ints.
        # re.split handles some of the extra spaces that occur.
        array1 = re.split("\s+", line_split[0].split(": ")[1])
        array2 = re.split("\s+", line_split[1].lstrip())
        answer = recursive_match_arrays(array1, array2, answer, index)

    print(sum(answer.values()))


part_2("input.txt")

# First Guess
# Answer: 13114317
