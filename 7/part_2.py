#!/bin/python3
"""
For part 2 J is the weakest card sorting wise, but it also is a wild card for the Counter. My first idea
would have over counted the number of cards in each hand by a lot.
I need to know what the best possible hand is with x wild cards without creating an impossible hand.

This was a really fun puzzle and I enjoyed working on it. However, I butted heads against the Python language
a lot. It just never did what my intuition said it should. I would have solved this literally hours sooner if
the code did what I intended it to. Which I guess is usually not the computer's fault.
"""
from collections import Counter, defaultdict


# Chat GPT wrote this function that respects the individual count of each item
# Which mattered because in my old code [2, 2] was occurring as a subset of [2, 1, 1,1]
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
    values = "J23456789TQKA"
    for key in ranked_hands:
        hands = ranked_hands[key]
        hands = sorted(hands, key=lambda word: [values.index(i) for i in word[0]])
        ranked_hands[key] = hands
    return ranked_hands


def handle_jacks(count, hand: str):
    if hand != "JJJJJ":
        num_jacks = count["J"]
        del count["J"]
        count[max(count, key=count.get)] += num_jacks
    return count


def part_2(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    hands = []
    for line in file:
        tmp = line.strip().split(" ")
        count = Counter(tmp[0])
        if "J" in tmp[0]:
            count = handle_jacks(count, tmp[0])
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


part_2("input.txt")

# Too high
# Answer: 249776650
