from solutions.utils import readFile
from itertools import combinations, takewhile


def getCoordinateConsideringSpaces(coordinate, spaces: list[int]):
    important_spaces = len([i for i in spaces if i < coordinate])
    return coordinate + (999999 * important_spaces)


if __name__ == '__main__':
    lines = readFile('inputs/input11.txt')
    vertical_spaces = [y for y, line in enumerate(lines) if all([ch == '.' for ch in line])]            
    horizontal_spaces = [x for x in range(len(lines[0])) if all([line[x] == '.' for line in lines])]
    
    galaxies = []
    number = 1
    for y,line in enumerate(lines):
        hits = [x for x, ch in enumerate(line) if ch == "#"]
        for x in hits:
            galaxies.append((x,y, number))
            number += 1
    
    part2 = 0
    for g1, g2 in combinations(galaxies, 2):
        x1, y1, number1 = g1
        x2, y2, number2 = g2

        x1 = getCoordinateConsideringSpaces(x1, horizontal_spaces)
        x2 = getCoordinateConsideringSpaces(x2, horizontal_spaces)
        y1 = getCoordinateConsideringSpaces(y1, vertical_spaces)
        y2 = getCoordinateConsideringSpaces(y2, vertical_spaces)

        dist = abs(x1-x2) + abs(y1-y2)

        # print(f'{number1} and {number2} is {dist}')

        part2 += dist

    print(part2)
