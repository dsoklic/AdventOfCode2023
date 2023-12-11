from solutions.utils import readFile
from itertools import combinations

def expandUniverse(lines):
    width = len(lines[0])

    y = 0
    while y < len(lines):
        if all([ch == '.' for ch in lines[y]]):
            lines.insert(y, '.' * width)
            y += 1
        y += 1

    x = 0
    while x < len(lines[0]):
        if all([line[x] == '.' for line in lines]):
            # insert space
            for j, data in enumerate(lines):
                lines[j] = data[:x] + '.' + data[x:]
            x += 1
        x += 1
            


if __name__ == '__main__':
    lines = readFile('inputs/input11.txt')
    expandUniverse(lines)
    
    galaxies = []
    number = 1
    for y,line in enumerate(lines):
        hits = [x for x, ch in enumerate(line) if ch == "#"]
        for x in hits:
            galaxies.append((x,y, number))
            number += 1
    
    part1 = 0
    for g1, g2 in combinations(galaxies, 2):
        x1, y1, number1 = g1
        x2, y2, number2 = g2

        dist = abs(x1-x2) + abs(y1-y2)

        # print(f'{number1} and {number2} is {dist}')

        part1 += dist

    print(part1)
