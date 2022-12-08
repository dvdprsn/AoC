import sys

sys.path.append("../../")
from aoc import get_input

data = get_input(8).splitlines()
num_lines = sum(1 for l in data)
num_elems = len(data[0])
res = ((2 * num_lines) + (2 * num_elems)) - 4
arr = []


def find_right(elem, cur_row, cur_col):
    steps = 0
    for i in range(cur_col + 1, num_elems):
        steps += 1
        if int(arr[cur_row][i]) >= elem:
            return steps
    return steps


def find_up(elem, cur_row, cur_col):
    steps = 0
    for i in range(cur_row - 1, -1, -1):
        steps += 1
        if int(arr[i][cur_col]) >= elem:
            return steps
    return steps


def find_down(elem, cur_row, cur_col):
    steps = 0
    for i in range(cur_row + 1, num_lines):
        steps += 1
        if int(arr[i][cur_col]) >= elem:
            return steps
    return steps


def find_left(elem, cur_row, cur_col):
    steps = 0
    for i in range(cur_col - 1, -1, -1):
        steps += 1
        if int(arr[cur_row][i]) >= elem:
            return steps
    return steps


# Populate 2d array
for i, line in enumerate(data):
    arr.append(list(line))

max_score = 0
for i in range(1, num_lines - 1):
    for j in range(1, num_elems - 1):
        elem = int(arr[i][j])
        r = find_right(elem, i, j)
        l = find_left(elem, i, j)
        u = find_up(elem, i, j)
        d = find_down(elem, i, j)
        tot = r * l * u * d
        if tot > max_score:
            max_score = tot
print(max_score)
