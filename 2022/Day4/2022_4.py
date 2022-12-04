import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(4).splitlines()

# P1
sums1 = 0
for line in data:
    line = line.split(',')
    for idx, b in enumerate(line):
        b = b.split("-")
        if idx == 1:
            if int(b[1]) <= max and int(b[0]) >= min or int(b[1]) >= max and int(b[0]) <= min:
                sums1+=1
        else:
            max = int(b[1])
            min = int(b[0])

print(sums1)

# P2
sums2 = 0
for line in data:
    line = sorted(line.split(','))
    for idx, b in enumerate(line):
        b = b.split("-")
        if idx == 1:
            if min <= int(b[1]) and max >= int(b[0]):
                sums2+=1
        else:
            max = int(b[1])
            min = int(b[0])

print(sums2)