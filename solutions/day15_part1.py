from solutions.utils import readFile


def hash_string(input: str) -> int:
    current = 0

    for ch in input:
        current += ord(ch)
        current *= 17
        current %= 256

    return current

if __name__ == '__main__':
    line = readFile('inputs/input15.txt')[0]
    cmds = line.split(',')

    part1 = 0

    for cmd in cmds:
        part1 += hash_string(cmd)

    print(part1)