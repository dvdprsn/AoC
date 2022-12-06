import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(6).splitlines()

# P1
# 4 chars all different at start
# Scan in block of 4 and all must be different
res = []
for line in data:
    line = list(line)
    for idx, i in enumerate(line):
        for x in range(4):
            res.append(line[idx+x])
        if len(res) == len(set(res)):
            print(idx+4)
            break
        else:
            res = []

# P2
res = []
for line in data:
    line = list(line)
    for idx, i in enumerate(line):
        for x in range(14):
            res.append(line[x+idx])
        if len(res) == len(set(res)):
            print(idx+14)
            break
        else:
            res = []