import sys

sys.path.append("../../")
from aoc import get_input

data = get_input(9).splitlines()

def is_negative(i):
    if i == 0:
        return 0
    if i < 0:
        return -1
    else: 
        return 1
    
class Rope_Point:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.unique_spaces = []

    def is_newspace(self):
        pos = f"{self.x_pos},{self.y_pos}"
        if pos not in self.unique_spaces:
            self.unique_spaces.append(pos)

    def move_y(self, delta):
        self.y_pos += delta

    def move_x(self, delta):
        self.x_pos += delta

    def print_point(self, end):
        print(f"{end} -> {self.x_pos}, {self.y_pos}")


def detect_move(point_head, point_tail):
    x_difference = point_head.x_pos - point_tail.x_pos
    y_difference = point_head.y_pos - point_tail.y_pos
    abs_x = abs(x_difference)
    abs_y = abs(y_difference)

    if abs_x == 2 or abs_y == 2:
        tail.move_x(is_negative(x_difference))
        tail.move_y(is_negative(y_difference))
        
    point_tail.is_newspace()


head = Rope_Point()
tail = Rope_Point()
for line in data:
    line = line.split(" ")
    for i in range(0, int(line[1])):
        if "U" in line[0]:
            head.move_x(1)
        if "D" in line[0]:
            head.move_x(-1)
        if "R" in line[0]:
            head.move_y(1)
        if "L" in line[0]:
            head.move_y(-1)

        detect_move(head, tail)

head.print_point("head")
tail.print_point("tail")
print(len(tail.unique_spaces))
