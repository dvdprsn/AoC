import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(2).splitlines()

score = 0
for line in data:
    line.split(" ")
    if "A" in line[0]:
        if "X" in line[2]:
            score += 0 + 3
        elif "Y" in line[2]:
            score += 3 + 1
        elif "Z" in line[2]:
            score += 6 + 2
    elif "B" in line[0]:
        if "X" in line[2]:
            score += 0 + 1
        elif "Y" in line[2]:
            score += 3 + 2
        elif "Z" in line[2]:
            score += 6 + 3
    elif "C" in line[0]:
        if "X" in line[2]:
            score += 0 + 2 
        elif "Y" in line[2]:
            score += 3 + 3
        elif "Z" in line[2]:
            score += 6 + 1
    

print(score)