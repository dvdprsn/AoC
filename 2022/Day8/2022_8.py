import sys

sys.path.append("../../")
from aoc import get_input

data = get_input(8).splitlines()
num_lines = sum(1 for l in data)
num_elems = len(data[0])
res = ((2 * num_lines) + (2 * num_elems))-4
arr = []

def find_right(elem, cur_row, cur_col):
    for i in range(cur_col+1, num_elems):
        if int(arr[cur_row][i]) >= elem:
            return False
    return True

def find_up(elem, cur_row, cur_col):
    for i in range(cur_row-1, -1, -1):
        if int(arr[i][cur_col]) >= elem:
            return False
    return True

def find_down(elem, cur_row, cur_col):
    for i in range(cur_row+1, num_lines):
        if int(arr[i][cur_col]) >= elem:
            return False
    return True

def find_left(elem, cur_row, cur_col):
    for i in range(cur_col-1, -1, -1):
        if int(arr[cur_row][i]) >= elem:
            return False
    return True

for i, line in enumerate(data):
    arr.append(list(line))
# For each horizontal
for i in range(1, num_lines - 1):
    # For each vertical
    for j in range(1, num_elems - 1):
        elem = int(arr[i][j])
        if find_right(elem,i,j):
            res+=1
            continue
        if find_up(elem,i,j):
            res+=1
            continue
        if find_down(elem,i,j):
            res+=1
            continue
        if find_left(elem,i,j):
            res+=1
            continue
print(res)
