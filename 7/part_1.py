#!/bin/python3
"""
After I got my logic implemented I had an issue with the two pairs because I was using set.subset and of
course the set of [2, 2] is just [2] which gave me the wrong answer. I wracked my brain trying to find the
flaw in my logic and finally figured that out. At that point I asked Chat GPT how to correctly get perfect
subsets and not the sloppy nonsense I was getting. I want to be clear that while Chat GPT did help me write
the is_subset() function, it had no idea what problem I was working on or why.
"""
from collections import Counter, defaultdict


# Chat GPT wrote this function that respects the individual count of each item
# Which mattered because in my old code [2, 2] was occurring as a subset of [2, 1, 1, 1]
# I don't understand why that would be a subset when it isn't a perfect match but at
# least Chat GPT understands.
def is_subset(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    for item, count in counter1.items():
        if counter2[item] < count:
            return False
    return True


def rank_hands(hands):
    def rank_hand(hand_counter):
        ranks = [[5], [4], [3, 2], [3], [2, 2], [2]]
        score = len(ranks)
        for rank in ranks:
            if is_subset(rank, (hand_counter.values())):
                break
            score -= 1
        return score

    ranked_hands = defaultdict(list)

    for hand in hands:
        rank: int = rank_hand(hand[-1])
        ranked_hands[rank].append(hand)
    return ranked_hands


def sort_hands_by_score(ranked_hands):
    values = "23456789TJQKA"
    for key in ranked_hands:
        hands = ranked_hands[key]
        hands = sorted(hands, key=lambda hand: [values.index(i) for i in hand[0]])
        ranked_hands[key] = hands
    return ranked_hands


def part_1(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    hands = []
    for line in file:
        tmp = line.strip().split(" ")
        count = Counter(tmp[0])
        tmp.append(count)
        hands.append(tmp)

    ranked_hands = rank_hands(hands)
    sorted_hands = sort_hands_by_score(ranked_hands)

    count = 0
    answer = 0
    for k in sorted(sorted_hands.keys()):
        for v in sorted_hands[k]:
            # print(v)
            count += 1
            answer += int(v[1]) * count

    print(answer)


part_1("input.txt")

# Answer: 249638405
