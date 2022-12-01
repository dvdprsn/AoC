import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(2).splitlines()

hpos = 0
depth = 0
aim = 0

for line in data:
    instruct = line.split(" ")
    if (instruct[0] == "forward"):
        hpos += int(instruct[1])
        depth += aim * int(instruct[1])
    elif (instruct[0] == "down"):
        # depth += int(instruct[1])
        aim += int(instruct[1])
    elif (instruct[0] == "up"):
        # depth -= int(instruct[1])
        aim -= int(instruct[1])

final = hpos * depth
print(final)
