import re

def readFile(file_path):
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]
    
def extractNumber(input):
    return int(re.search(r"(\d+)", input).group(1))

def extractAllNumbers(input: str) -> list[int]:
    return [int(x) for x in re.findall(r"(-?\d+)", input)]

def padInput(input: list[str], padSymbol=' '):
    width = len(input[0])

    input.insert(0, padSymbol * width)
    input.append(padSymbol * width)

    for i, line in enumerate(input):
        input[i] = f'{padSymbol}{line}{padSymbol}'
