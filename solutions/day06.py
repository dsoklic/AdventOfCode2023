from solutions.utils import readFile, extractAllNumbers



if __name__ == '__main__':
    lines = readFile('inputs/input06.txt')

    times = extractAllNumbers(lines[0])
    distances = extractAllNumbers(lines[1])

    part1 = 1
    for time, distance in zip(times, distances):
        ways = 0
        for i in range(1, time):
            dist = (time-i)*i

            if dist > distance:
                ways += 1

        part1 *= ways

    print(part1)

    big_time = int(''.join([str(x) for x in times]))
    big_distance = int(''.join([str(x) for x in distances]))

    ways = 0
    for i in range(1, big_time):
        dist = (big_time-i)*i

        if dist > big_distance:
            ways += 1

    print(ways)


