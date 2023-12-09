from solutions.utils import readFile, extractAllNumbers

if __name__ == '__main__':
    lines = readFile('inputs/input09.txt')

    part1 = 0

    for line in lines:
        layers = [extractAllNumbers(line)]

        while not all([x == 0 for x in layers[-1]]):
            last_layer = layers[-1]
            new_layer = [b-a for a,b in zip(last_layer, last_layer[1:])]
            layers.append(new_layer)

        # calculate the next number
        for i in reversed(range(len(layers)-1)):
            cur_layer = layers[i]
            prev_layer = layers[i+1]

            diff = prev_layer[-1]
            cur_layer.append(cur_layer[-1] + diff)

        part1 += layers[0][-1]

    print(f'{part1=}')

    part2 = 0

    for line in lines:
        layers = [extractAllNumbers(line)]

        while not all([x == 0 for x in layers[-1]]):
            last_layer = layers[-1]
            new_layer = [b-a for a,b in zip(last_layer, last_layer[1:])]
            layers.append(new_layer)

        # calculate the next number
        for i in reversed(range(len(layers)-1)):
            cur_layer = layers[i]
            prev_layer = layers[i+1]

            diff = prev_layer[0]
            cur_layer.insert(0, cur_layer[0] - diff)

        part2 += layers[0][0]

    print(f'{part2=}')