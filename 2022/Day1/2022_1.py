import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(1).splitlines()

mostCal = []
cur = 0

for line in data:
    if (line == ""):
        mostCal.append(cur)
        cur = 0
    else:
        cur += int(line)

mostCal.sort(reverse=True)
print(sum(mostCal[:3]))
