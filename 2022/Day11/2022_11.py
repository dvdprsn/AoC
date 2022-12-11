import sys
import math
sys.path.append("../../")
from aoc import get_input

data = get_input(11).splitlines()
# What a terrible way to hardcode a solution....
# But, it works!
class M0:
    def __init__(self):
        self.items = [93, 54, 69, 66, 71]
        self.number_inspections = 0

    def operation(self, old_worry):
        return old_worry * 3

    def test(self, worry):
        if worry % 7 == 0:
            return 7
        else:
            return 1


class M1:
    def __init__(self):
        self.items = [89, 51, 80, 66]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry * 17

    def test(self, worry):
        if worry % 19 == 0:
            return 5
        else:
            return 7


class M2:
    def __init__(self):
        self.items = [90, 92, 63, 91, 96, 63, 64]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry + 1

    def test(self, worry):
        if worry % 13 == 0:
            return 4
        else:
            return 3


class M3:
    def __init__(self):
        self.items = [65, 77]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry + 2

    def test(self, worry):
        if worry % 3 == 0:
            return 4
        else:
            return 6


class M4:
    def __init__(self):
        self.items = [76, 68, 94]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry * old_worry

    def test(self, worry):
        if worry % 2 == 0:
            return 0
        else:
            return 6


class M5:
    def __init__(self):
        self.items = [86, 65, 66, 97, 73, 83]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry + 8

    def test(self, worry):
        if worry % 11 == 0:
            return 2
        else:
            return 3


class M6:
    def __init__(self):
        self.items = [78]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry + 6

    def test(self, worry):
        if worry % 17 == 0:
            return 0
        else:
            return 1


class M7:
    def __init__(self):
        self.items = [89, 57, 59, 61, 87, 55, 55, 88]
        self.number_inspections = 0
    def operation(self, old_worry):
        return old_worry + 7

    def test(self, worry):
        if worry % 5 == 0:
            return 2
        else:
            return 5
        
round_number = 1
 
monkeys = []
monkeys.append(M0())
monkeys.append(M1())
monkeys.append(M2())
monkeys.append(M3())
monkeys.append(M4())
monkeys.append(M5())
monkeys.append(M6())
monkeys.append(M7())
# Need to find a common divisor to reduce
# Luckly these are all primes
divs = [7, 19, 13, 3, 2, 11, 17, 5]
lcm = math.lcm(*divs)

while round_number <= 10000:
    for i in range(0, 8):
        # monkey selects item to inspect
        monkey = monkeys[i]
        for y in monkey.items.copy():
            # print(y)
            original = y
            monkey.number_inspections += 1
            # monkey inspects item
            y = monkey.operation(y)
            # worry level decreases
            # y = y/3
            # Test where to throw
            throw = monkey.test(y)
            # throw to next monkey
            monkeys[throw].items.append(y % lcm)
            monkey.items.remove(original)
    round_number += 1

largest = []
for i in range(0,8):
    largest.append(monkeys[i].number_inspections)
    print(f"Monkey {i} inspected {monkeys[i].number_inspections} times")

max1 = max(largest)
largest.remove(max1)
max2 = max(largest)
print(max1*max2)