from solutions.utils import readFile, padInput
from collections import deque
from dataclasses import dataclass
from colorama import Fore, Back, Style

@dataclass
class Location:
    location: tuple[int, int]
    distance: int

def findStart(lines: list[str]) -> tuple[int, int]:
    for y, line in enumerate(lines):
        x = line.find('S')

        if x != -1:
            return (x, y)
            

if __name__ == '__main__':
    lines = readFile('inputs/input10.txt')
    padInput(lines, padSymbol='.') # avoid any unwanted out of bounds errors

    location_queue: deque[Location] = deque()

    start_x, start_y = findStart(lines)

    flipping_char = {'|', '7', 'F'}
    
    visited_locations = set() # dict from (x,y) to distance int
    visited_locations.add((start_x, start_y))

    if lines[start_y-1][start_x] in ('|', '7', 'F'):
        location_queue.append(Location((start_x,start_y-1), 1))
    if lines[start_y+1][start_x] in ('|', 'L', 'J'):
        location_queue.append(Location((start_x,start_y+1), 1))
        flipping_char.add('S')
    if lines[start_y][start_x-1] in ('-', 'L', 'F'):
        location_queue.append(Location((start_x-1,start_y), 1))
    if lines[start_y][start_x+1] in ('-', 'J', '7'):
        location_queue.append(Location((start_x+1,start_y), 1))

    part1 = 0

    debug_info = {}
    debug_info[(start_x, start_y)] = 0

    while location_queue:
        next_loc = location_queue.popleft()


        next_x, next_y = next_loc.location
        symbol = lines[next_y][next_x]

        if next_loc.location in visited_locations or symbol in ('.', 'S'):
            continue

        debug_info[next_loc.location] = next_loc.distance
        part1 = max(part1, next_loc.distance)
        visited_locations.add(next_loc.location)

        new_dist = next_loc.distance + 1
        # What are the neighbors?
        match symbol:
            case '|':
                location_queue.append(Location((next_x, next_y-1), new_dist))
                location_queue.append(Location((next_x, next_y+1), new_dist))
            case '-':
                location_queue.append(Location((next_x-1, next_y), new_dist))
                location_queue.append(Location((next_x+1, next_y), new_dist))
            case 'L':
                location_queue.append(Location((next_x, next_y-1), new_dist))
                location_queue.append(Location((next_x+1, next_y), new_dist))
            case 'J':
                location_queue.append(Location((next_x, next_y-1), new_dist))
                location_queue.append(Location((next_x-1, next_y), new_dist))
            case '7':
                location_queue.append(Location((next_x-1, next_y), new_dist))
                location_queue.append(Location((next_x, next_y+1), new_dist))
            case 'F':
                location_queue.append(Location((next_x, next_y+1), new_dist))
                location_queue.append(Location((next_x+1, next_y), new_dist))
        
    print(f'{part1=}')

    ## Part 2
    part2 = 0
    for y, line in enumerate(lines):
        inside_loop = False

        for x, char in enumerate(line):
            if (x,y) in visited_locations and char in flipping_char:
                inside_loop = not inside_loop # flip flag
            
            if inside_loop and (x,y) not in visited_locations:
                part2 += 1
                print('I', end='')
            elif (x,y) in visited_locations:
                print(Fore.RED +char+Style.RESET_ALL, end='')
            else:
                print(char, end='')
        
        print()
    
    print(f'{part2=}')
