import re

def readFile(file_path):
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]
    
def extractNumber(input):
    return re.search(r"(\d+)", input).group(1)