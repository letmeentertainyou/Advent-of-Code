#!/bin/python3
"""
Postmortem:
I had originally tried to used string.replace() but I found an issue with this string:
"oneight" when I replaced "one" then it became "1ight" and the "eight" also disappeared.

My next bet was to simply insert an int at the beginning of each number. That would make 
"6fourfour" into "64four4four" but this can also break things because "eighthree" becomes
"eigh3three" and the "eight" is again killed.

My working solution uses the complex dictionary WORDS defined below. With the first letter of 
each digit word as a key.

On every single char I have to check if it's in the dict, and if it is I call left_find to get any
possible string results back. This is heavy computationally but this problem turned out to be 
rather tricky.

This would only ever work in a dynamic language because our function is returning None when no values
are found and I can use that optional to do an "if lFind" check on our value. 

In any strictly typed (non Optional/Union) language you cannot return None. So you would have to
return -1 which works for positive integers but would break in a signed world. Given the scope of
the problem is only positive integers that feels fine but I can see it's flaws from here.

What I like about this solution is that it doesn't modify any of the lines of the file, and it
works left to right which allows the rest of the solution from part 1 to work. A faster solution
is surely available but this solution fit well within the context of part 1.
"""

WORDS = {
    "e": [("eight", "8")],
    "f": [("five", "5"), ("four", "4")],
    "n": [("nine", "9")],
    "o": [("one", "1")],
    "s": [("seven", "7"), ("six", "6")],
    "t": [("three", "3"), ("two", "2")],
    "z": [("zero", "0")],
}


def left_find(line: str, key: str) -> int:
    """
    Takes a string of text, and a key, and finds the first occurrence of any of the words
    stored in WORDS[key]. Returns None if no results found.
    """

    for num in WORDS[key]:
        # When find fails it returns -1 which is bad design because -1 is a
        # valid index in Python, I guess returning None would be tricky too.
        tmp = line[: len(num[0])].find(num[0])

        # Makes sure we only get a value at the first possible index.
        if tmp == 0:
            return num[1]


def part_2(filepath: str) -> None:
    with open(filepath, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    results = []
    int_range = list(range(48, 58))
    for line in file:
        tmp_chars: str = ""
        for idx, char in enumerate(line):
            if ord(char) in int_range:
                tmp_chars += char

            elif char in WORDS.keys():
                lFind = left_find(line[idx:], char)
                if lFind:
                    tmp_chars += lFind

        tmp_string = tmp_chars[0] + tmp_chars[-1]
        results.append(int(tmp_string))

    print(sum(results))


part_2("input.txt")

# Answer: 55902
