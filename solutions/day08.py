from solutions.utils import readFile
import re

# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)

def buildTree(lines):
    tree = {}
    for line in lines[2:]:
        node, left, right = re.findall(r"(\w+)", line)
        tree[node] = (left, right)
    return tree

def allNodesEndWithZ(nodes):
    return all([x[-1] == 'Z' for x in nodes])

def lcm_of_list(numbers):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to find the LCM.")

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])

    return result

if __name__ == '__main__':
    lines = readFile('inputs/input08.txt')
    tree = buildTree(lines)
    instructions = lines[0]

    part1 = 0
    current = 'AAA'

    while current != 'ZZZ':
        for dir in list(instructions):
            if current == 'ZZZ':
                break

            match dir:
                case 'L':
                    current = tree[current][0]
                case 'R':
                    current = tree[current][1]
            
            part1 += 1
    
    print(f'{part1=}')

    ## part 2 

    current2 = list(filter(lambda x: x[-1] == 'A',tree.keys()))

    lengths = []

    # Find lengths of all cycles
    for i in range(len(current2)):
        length = 0

        while current2[i][-1] != 'Z':
            for dir in list(instructions):
                if current2[i][-1] == 'Z':
                    break

                match dir:
                    case 'L':
                        current2[i] = tree[current2[i]][0]
                    case 'R':
                        current2[i] = tree[current2[i]][1]
            
                length += 1

        lengths.append(length)

    lcm = lcm_of_list(lengths)    
    print(f'part2={lcm}')