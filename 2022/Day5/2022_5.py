import sys
sys.path.append('../../')
from aoc import get_input

data = get_input(5).splitlines()

arr = []
for line in data:
    if "move" not in line and "1" in line:
        for l in line.strip().split():
            arr.append([])
        break

pop = 0
for line in data:
    line = line.split(" ")
    for idx, l in enumerate(line):
        if l == "" and idx%2 != 0:
            pop+=0.5
        elif "[" in l:
            arr[int(pop)].append(l.replace("[", "").replace("]", ""))
            pop+=1

    pop = 0
for line in data:
    if "move" in line:
        line = line.split()
        for i in range(int(line[1])):
            tmp = arr[int(line[3])-1].pop(0)
            arr[int(line[5])-1].insert(0,tmp)

res = ""
for x in arr:
    res += x[0]
print(res)

arr = []
for line in data:
    if "move" not in line and "1" in line:
        for l in line.strip().split():
            arr.append([])
        break

pop = 0
for line in data:
    line = line.split(" ")
    for idx, l in enumerate(line):
        if l == "" and idx%2 != 0:
            pop+=0.5
        elif "[" in l:
            arr[int(pop)].append(l.replace("[", "").replace("]", ""))
            pop+=1

    pop = 0
for line in data:
    if "move" in line:
        line = line.split()
        for i in range(int(line[1])):
            tmp = arr[int(line[3])-1].pop(0)
            arr[int(line[5])-1].insert(i,tmp)
        

res = ""
for x in arr:
    res += x[0]
print(res)
            

