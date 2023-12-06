from solutions.utils import readFile, extractAllNumbers, extractNumber
from collections import deque

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

def getCardInfo(line):
    id_str, numbers = line.split(': ')

    winning_str, actual_str = numbers.split(' | ')

    id = extractNumber(id_str)
    winners = extractAllNumbers(winning_str)
    actual = extractAllNumbers(actual_str)

    return id, winners, actual

def getScore(winners, actual) -> int:
    count = 0
    for num in winners:
        if num in actual:
            count += 1

    return int(2 ** (count-1))

def getWinningNumbers(winners, actual) -> list[int]:
    matching = []

    for num in winners:
        if num in actual:
            matching.append(num)

    return matching

def calculatePart2(lines) -> int:
    pipeline = deque(lines)
    cards = 0

    while pipeline:
        cards += 1
        game = pipeline.popleft()
        id, winners, actual = getCardInfo(game)

        # Get winning numbers
        matching = getWinningNumbers(winners, actual)
        if matching:
            for i in range(id, id+len(matching)):
                pipeline.append(lines[i])

    return cards

if __name__ == '__main__':
    lines = readFile('inputs/input04.txt')

    part1 = 0
    for line in lines:
        _, winners, actual = getCardInfo(line)
        part1 += getScore(winners, actual)
    print(f"part1 {part1}")

    
    part2 = calculatePart2(lines)
    print(f"part2: {part2}")