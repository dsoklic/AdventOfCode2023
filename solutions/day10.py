from solutions.utils import readFile, padInput
from collections import deque
from dataclasses import dataclass

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
    
    visited_locations = set() # dict from (x,y) to distance int
    visited_locations.add((start_x, start_y))

    if lines[start_y-1][start_x] in ('|', '7', 'F'):
        location_queue.append(Location((start_x,start_y-1), 1))
    if lines[start_y+1][start_x] in ('|', 'L', 'J'):
        location_queue.append(Location((start_x,start_y+1), 1))
    if lines[start_y][start_x-1] in ('-', 'L', 'F'):
        location_queue.append(Location((start_x-1,start_y), 1))
    if lines[start_y][start_x+1] in ('-', 'J', '7'):
        location_queue.append(Location((start_x+1,start_y), 1))

    part1 = 0

    debug_info = {}

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
        
    print(part1)

    # Print debug data
    # for y, line in enumerate(lines):
    #     for x, char in enumerate(line):
    #         if (x,y) in debug_info:
    #             print(debug_info[(x,y)]%10, end='')
    #         else:
    #             print(char, end='')
    #     print()
            