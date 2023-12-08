from solutions.utils import readFile
from collections import defaultdict
from functools import cmp_to_key

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

def parseInput(lines):
    return_val = []

    for line in lines:
        a, b = line.split(' ')
        return_val.append((a, int(b)))

    return return_val

def createHand(hand):
    counted_hand = defaultdict(lambda: 0)

    for card in list(hand):
        counted_hand[card] += 1

    return counted_hand

def hasPair(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        pass
    else:
        return any([count >= 2 for count in counted_hand.values()])

def hasTwoPairs(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        pass
    else:
        return [count >= 2 for count in counted_hand.values()].count(True) >= 2

def hasThreeOfAKind(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        pass
    else:
        return any([count >= 3 for count in counted_hand.values()])

def hasFullHouse(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        pass
    else:
        return 3 in counted_hand.values() and 2 in counted_hand.values()

def hasFourOfAKind(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        # return max(counted_hand.values()) + counted_hand['J'] == 4
        pass
    else:
        return any([count >= 4 for count in counted_hand.values()])

def hasFiveOfAKind(hand):
    counted_hand = createHand(hand)

    if 'J' in hand:
        return len(counted_hand.values()) <= 2 and sum(counted_hand.values()) == 5
    else:
        return any([count >= 5 for count in counted_hand.values()])

def handToNumber(hand):
    if hasFiveOfAKind(hand):
        return 6
    if hasFourOfAKind(hand):
        return 5
    if hasFullHouse(hand):
        return 4
    if hasThreeOfAKind(hand):
        return 3
    if hasTwoPairs(hand):
        return 2
    if hasPair(hand):
        return 1
    
    return 0

card_ranking = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

def compareHands(hand1, hand2) -> int:
    number1 = handToNumber(hand1)
    number2 = handToNumber(hand2)

    if number1 != number2:
        return number1 - number2
    else:
        for a, b in zip(list(hand1), list(hand2)):
            if a != b:
                return card_ranking[a] - card_ranking[b]
        
        return 0

def comparator(line1, line2):
    hand1, _ = line1
    hand2, _ = line2

    return compareHands(hand1, hand2)

def sortLines(lines):
    return sorted(lines, key=cmp_to_key(comparator))

if __name__ == '__main__':
    lines = parseInput(readFile('inputs/input07.txt'))

    lines = sortLines(lines)

    part1 = 0
    for i, line in enumerate(lines):
        _, score = line
        part1 += score * (i+1)

    print(part1)