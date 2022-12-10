import sys

sys.path.append("../../")
from aoc import get_input

data = get_input(10).splitlines()

queue = []
for line in data:
    queue.append(line.split(" "))

current_ins = []
current_cycle = 0
cycle_pause = 0
reg_value = 1
sig_sum = 0

image_string = ""

while len(queue) != 0:
    current_cycle += 1
    # Insturction is completed
    if cycle_pause == 0:
        if "addx" in current_ins:
            reg_value += int(current_ins[1])
    # Next char to write is within range of sprite pos
    if len(image_string) in range(reg_value-1, reg_value+2):
        image_string += "#"
    else:
        image_string += "."
    # For P1
    if current_cycle%40 == 20:
        sig_sum += reg_value * current_cycle
    # For P2
    if current_cycle%40 == 0:
        print(image_string)
        image_string = ""
    # Dont read next instruction until current is done
    if cycle_pause != 0:
        cycle_pause -= 1
        continue
    # Read next instruction
    current_ins = queue.pop(0)
    
    if "addx" in current_ins:
        cycle_pause += 1

print(f"Part 1: {sig_sum}")