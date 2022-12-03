import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(3).splitlines()
sums = 0
count = 0 
group = []
for line in data:
    group.append(line)
    value = 0 
    count += 1

    # Have grouping
    if count >= 3:
        st = ""
        for char in line:
            if char in st:
                continue
            if char in group[0] and char in group[1]:
                st += char
                if char.isupper():
                    value += ord(char)-38
                else:
                    value += ord(char)-96
        sums += value
        count = 0 
        group = []

print(sums)
