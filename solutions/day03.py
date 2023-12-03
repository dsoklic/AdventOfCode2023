from solutions.utils import readFile
from dataclasses import dataclass
from itertools import product
import numpy
import re

@dataclass
class Number:
    value: int
    start_x: int
    end_x: int
    y: int


def getAllNumbers(input) -> list[Number]:
    found_numbers: list[Number] = []

    for y in range(len(input)):
        for match in re.finditer(r'\d+', input[y]):
            found_numbers.append(Number(int(match.group()), match.start(), match.end(), y))

    return found_numbers

def getAllGears(input) -> tuple[tuple[int, int]]:
    found_gears = []

    for y in range(len(input)):
        for match in re.finditer(r'\*', input[y]):
            found_gears.append((match.start(), y))

    return found_gears


def getPartNumbers(input):
    found_numbers = getAllNumbers(input)

    # Remove those without symbols adjacent
    part_numbers = []
    for number in found_numbers:
        # Make sure we don't go out of bounds
        x_range = range(
            max(number.start_x - 1, 0),
            min(number.end_x+1, len(input[number.y]))
        )

        y_range = range(
            max(number.y - 1, 0),
            min(number.y + 2, len(input))
        )

        symbols = [input[y][x] for x, y in product(x_range, y_range)]

        if any([not sym.isdigit() and sym != '.' for sym in symbols]):
            part_numbers.append(number.value)

    return part_numbers

def rangesOverlap(range1, range2):
    start1, end1 = range1
    start2, end2 = range2

    return end1 >= start2 and end2 >= start1

def getPairsNextToGears(numbers: list[Number], gears):
    pairs = []
    
    for gear_x, gear_y in gears:
        gear_range_x = (
            gear_x - 1,
            gear_x + 1
        )
        gear_range_y = range(
            gear_y - 1,
            gear_y + 2
        )

        adjacent = []

        for number in numbers:
            number_range_x = (number.start_x, number.end_x-1)
            if rangesOverlap(gear_range_x, number_range_x) and number.y in gear_range_y:
                adjacent.append(number.value)
        
        if len(adjacent) == 2:
            pairs.append(adjacent)

    return pairs


if __name__ == "__main__":
    lines = readFile('inputs/input03.txt')
    parts = getPartNumbers(lines)

    part1 = sum([int(x) for x in parts])
    print(f'part1: {part1}')

    part2 = 0
    gears = getAllGears(lines)
    numbers  = getAllNumbers(lines)
    for pair in getPairsNextToGears(numbers, gears):
        part2 += numpy.prod(pair)
    print(f'part2: {part2}')
