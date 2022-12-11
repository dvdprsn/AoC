import sys
import math
from operator import add, mul, pow
sys.path.append("../../")
from aoc import get_input
data = get_input(11).splitlines()

class Monkey:
    def __init__(self, item_list, op, op_value, div, true_m, false_m):
        self.items = item_list
        self.op = op
        self.number_inspections = 0
        self.div_by = div
        self.true_m = true_m
        self.false_m = false_m
        self.op_value = op_value

    def magic(self, old):
        return self.op(old, self.op_value)

    def test(self, value):
        if value % self.div_by == 0:
            return self.true_m
        else:
            return self.false_m

monkeys = []
monkeys.append(Monkey([93, 54, 69, 66, 71], mul, 3, 7, 7, 1))
monkeys.append(Monkey([89, 51, 80, 66], mul, 17, 19, 5, 7))
monkeys.append(Monkey([90, 92, 63, 91, 96, 63, 64], add, 1, 13, 4, 3))
monkeys.append(Monkey([65, 77], add, 2, 3, 4, 6))
monkeys.append(Monkey([76, 68, 94], pow, 2, 2, 0, 6))
monkeys.append(Monkey([86, 65, 66, 97, 73, 83], add, 8, 11, 2, 3))
monkeys.append(Monkey([78], add, 6, 17, 0, 1))
monkeys.append(Monkey([89, 57, 59, 61, 87, 55, 55, 88], add, 7, 5, 2, 5))

# Need to find a common divisor to reduce
lcm = math.lcm(*[7, 19, 13, 3, 2, 11, 17, 5])
# Part 2
round_number = 1
while round_number <= 10000:
    for i in range(0, 8):
        # monkey selects item to inspect
        monkey = monkeys[i]
        for item in monkey.items.copy():
            monkey.number_inspections += 1
            # monkey inspects item
            altered_item = monkey.magic(item)
            # Monkey throws item after testing
            monkeys[monkey.test(altered_item)].items.append(altered_item % lcm)
            monkey.items.remove(item)
    round_number += 1

res = []
for i in range(0, 8):
    res.append(monkeys[i].number_inspections)
res.sort(reverse=True)
print(f"Part 2: {res[0] * res[1]}")
