from solutions.utils import readFile
from collections import defaultdict


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

    boxes = defaultdict(lambda: [])

    for cmd in cmds:

        if '=' in cmd:
            box_name, focal = cmd.split('=')
            hash_val = hash_string(box_name)

            relevant_box = boxes[hash_val]

            if box_name not in [name for name, _ in relevant_box]:
                boxes[hash_val].append([box_name, int(focal)])
            else:
                ind = next(i for i,v in enumerate(relevant_box) if v[0] == box_name)
                relevant_box[ind][1] = int(focal)

        if '-' in cmd:
            box_name = cmd.rstrip('-')
            hash_val = hash_string(box_name)

            relevant_box = boxes[hash_val]
            if box_name in [name for name, _ in relevant_box]:
                ind = next(i for i,v in enumerate(relevant_box) if v[0] == box_name)
                relevant_box.pop(ind)

    part2 = 0

    for box_ind, slots in boxes.items():
        for slot_ind, contents in enumerate(slots):
            focal = contents[1]

            part2 += (box_ind+1) * (slot_ind+1) * focal

    print(part2)