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

def getMirrorLine(map) -> tuple[bool, int]:
    # First try horizontal mirror lines
    for y in range(1, len(map)):
        above = reversed(map[:y])
        below = map[y:]

        if all([a == b for a,b in zip(below, above)]):
            return (True, y)
        
    # Try vertical
    individual_elements = [list(line) for line in map]
    rotated = numpy.rot90(individual_elements, k=3)
    for x in range(1, len(rotated)):
        left = [''.join(line) for line in reversed(rotated[:x])]
        right = [''.join(line) for line in rotated[x:]]

        if all([a == b for a,b in zip(left, right)]):
            return (False, x)




if __name__ == '__main__':
    lines = readFile('inputs/input13.txt')

    maps = splitMaps(lines)

    # Split into individual maps
    part1 = 0
    for map in maps:
        is_horizontal, line = getMirrorLine(map)
        if is_horizontal:
            part1 += 100 * line
        else:
            part1 += line

    print(part1)

