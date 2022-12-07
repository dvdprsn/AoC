import sys

sys.path.append("../../")

from aoc import get_input


data = get_input(7).splitlines()
root_size = 0
res = 0


class Node:
    """Node"""
    def __init__(self, name, kind, parent):
        self.parent = parent
        self.children = []
        self.size = 0
        self.name = name
        self.kind = kind
        self.files = []

    # Insert Node
    def insert(self, node):
        """Insert"""
        self.children.append(node)

    def print_tree(self):
        """Printing"""
        print(f"{self.name} ({self.kind}) size={self.size}")
        print(f" -> {self.files} and children {len(self.children)}")

        for node in self.children:
            node.print_tree()
    def set_sums(self):
        '''Sums of dirs'''
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

# Set dir sizes
curNode = root
root.set_sums()
root.get_res()
print(res)