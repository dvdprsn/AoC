import sys

sys.path.append("../../")

from aoc import get_input

data = get_input(7).splitlines()

# P1 Vars
res = 0

# P2 Vars
res2 = 10**10
most = 70000000
unused = 30000000


class Node:
    def __init__(self, name, kind, parent):
        self.children = []
        self.files = []
        self.parent = parent
        self.name = name
        self.kind = kind
        self.size = 0

    # Insert Node
    def insert(self, node):
        self.children.append(node)

    def print_tree(self):
        print(f"{self.name} ({self.kind}) size={self.size}")
        print(f" -> {self.files} and children {len(self.children)}")
        for node in self.children:
            node.print_tree()

    def set_sums(self):
        self.size = sum(self.files)
        for node in self.children:
            node.set_sums()
        if self.parent != None:
            self.parent.size += self.size

    def get_res(self):
        global res
        if self.size < 100000:
            res += self.size
        for node in self.children:
            node.get_res()

    def find_smallest(self, space):
        global res2
        if self.size < res2 and self.size > space:
            res2 = self.size
        for node in self.children:
            node.find_smallest(space)


root = Node("/", "dir", None)
curNode = root

# Populate the tree
for line in data:
    line = line.split()
    if "dir" in line:
        curNode.insert(Node(line[1], "dir", curNode))
    elif line[0].isdigit():
        curNode.files.append(int(line[0]))
    elif line[1] == "cd" and line[2] != "..":
        for n in curNode.children:
            if n.name in line[2]:
                curNode = n
                break
    elif line[1] == "cd" and line[2] == "..":
        curNode = curNode.parent

curNode = root
root.set_sums()
root.get_res()

free_amount = unused - (most - root.size)
root.find_smallest(free_amount)
print(res)
print(res2)
