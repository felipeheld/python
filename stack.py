#!/usr/bin/env python3

from nodes import SLLNode

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = SLLNode(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            raise Exception('Stack is empty')

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            raise Exception('Stack is empty')

    def isempty(self):
        return self.size == 0
