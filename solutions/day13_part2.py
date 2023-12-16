from solutions.utils import readFile
import numpy

def splitMaps(lines):
    maps = [[]]

    for line in lines:
        if line != '':
            maps[-1].append(line)
        else:
            maps.append([])

    return maps

def countLineDifferences(line1, line2):
    return len([a for a,b in zip(line1, line2) if a != b])

def getMirrorLine(map) -> tuple[bool, int]:
    # First try horizontal mirror lines
    for y in range(1, len(map)):
        above = reversed(map[:y])
        below = map[y:]

        if sum([countLineDifferences(a, b) for a,b in zip(below, above)]) == 1:
            return (True, y)
        
    # Try vertical
    individual_elements = [list(line) for line in map]
    rotated = numpy.rot90(individual_elements, k=3)
    for x in range(1, len(rotated)):
        left = [''.join(line) for line in reversed(rotated[:x])]
        right = [''.join(line) for line in rotated[x:]]

        if sum([countLineDifferences(a, b) for a,b in zip(left, right)]) == 1:
            return (False, x)



if __name__ == '__main__':
    lines = readFile('inputs/input13.txt')

    maps = splitMaps(lines)

    # Split into individual maps
    part2 = 0
    for map in maps:
        is_horizontal, line = getMirrorLine(map)
        if is_horizontal:
            part2 += 100 * line
        else:
            part2 += line

    print(part2)

