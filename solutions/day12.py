from solutions.utils import readFile


if __name__ == '__main__':
    lines = readFile('inputs/dummy12.txt')

    lines = [(map, hints.split(',')) for map, hints in [line.split(' ') for line in lines]]
    
    for map, hints in lines:
        unknown_locations = [i for i, ch in enumerate(map) if ch == '?']
        map_size = len(map)
        # Figure out all locations where the damaged springs could be
        # Groups of damadged springs have a start coordinate and a size.
        # Find all possible combinations of start coordinate and size, then figure out if they agree with the hints.

        possible_solutions = {}

        for i, hint in enumerate(hints):
            hint = int(hint)

            # the hint can be anywhere, but tak into account all preceding and succeeding hints
            preceding = hints[:i]
            succeeding = hints[i:]

            empty_space_start = sum(preceding) + len(preceding) # all preceding sizes and 1 gap for each element
            empty_space_end = sum(succeeding) + len(succeeding) + hint # all succeeding sizes and 1 gap for each element
