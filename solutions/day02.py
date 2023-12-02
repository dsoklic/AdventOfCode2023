from utils import readFile, extractNumber

lines = readFile('inputs/input02.txt')


### Part 1 ###
possible_game_ids = []

for line in lines:
    game_id_part, moves_part = line.split(': ')

    game_id = int(extractNumber(game_id_part))

    all_possible = True
    for move in moves_part.split('; '):
        red = 0
        green = 0
        blue = 0

        for cube in move.split(', '):
            count, color = cube.split(' ')

            match color:
                case 'red':
                    red = int(count)
                case 'green':
                    green = int(count)
                case 'blue':
                    blue = int(count)

        maximums = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        if red > maximums['red'] or green > maximums['green'] or blue > maximums['blue']:
            all_possible = False
            break
    
    if all_possible:
        possible_game_ids.append(game_id)

print('part1: ' + str(sum(possible_game_ids)))


### Part 2 ###

power_sum = 0

for line in lines:
    game_id_part, moves_part = line.split(': ')

    game_id = int(extractNumber(game_id_part))

    max_red = 0
    max_green = 0
    max_blue = 0

    for move in moves_part.split('; '):
        red = 0
        green = 0
        blue = 0

        for cube in move.split(', '):
            count, color = cube.split(' ')

            match color:
                case 'red':
                    red = int(count)
                case 'green':
                    green = int(count)
                case 'blue':
                    blue = int(count)

        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)

    power_sum += max_red * max_blue * max_green

print('part2: ' + str(power_sum))