import re

def readFile(file_path):
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]
    
def extractNumber(input):
    return int(re.search(r"(\d+)", input).group(1))

def extractAllNumbers(input: str) -> list[int]:
    return [int(x) for x in re.findall(r"(-?\d+)", input)]
