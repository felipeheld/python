#!/usr/bin/env python3

from nodes import Leaf

class Tree:

    def __init__(self):
        self.root = None

    def __append(self, data):
        leaf = Leaf(data)
        branch = self.root
        if self.root == None:
            self.root = leaf
        else:
            while branch:
                if leaf.data > branch.data:
                    branch = branch.right
                else:
                    branch = branch.left
            branch = leaf

    def __search(self, data):
        branch = self.root
        while branch:
            if branch.data == data:
                return branch
            if data > branch.data:
                branch = branch.right
            else:
                branch = branch.left
