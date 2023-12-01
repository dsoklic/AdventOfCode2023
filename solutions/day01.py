from utils import readFile

lines = readFile('inputs/input01.txt')

part1 = 0

for line in lines:
    for i in range(len(line)):
        if line[i].isdigit():
            first = line[i]
            break;

    for i in reversed(range(len(line))):
        if line[i].isdigit():
            last = line[i]
            break;

    part1 += int(first + last)

print(part1)

mappings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

min_len = min([len(k) for k in mappings])
max_len = max([len(k) for k in mappings])

def getFirstDigit(line):
    global mappings

    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        for j in range(min_len, max_len+1):
            if i+j > len(line):
                continue

            substr = line[i:i+j]
            if substr in mappings:
                return mappings[substr]

def getLastDigit(line):
    global mappings

    for i in reversed(range(len(line))):
        if line[i].isdigit():
            return line[i]

        for j in range(min_len, max_len+1):
            if i+j > len(line):
                continue

            substr = line[i:i+j]
            if substr in mappings:
                return mappings[substr]

part2 = 0
for line in lines:
    part2 += int(getFirstDigit(line) + getLastDigit(line))

print(part2)
