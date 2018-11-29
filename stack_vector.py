#!/usr/bin/env python3

class StackUnderFlow(Exception):
    pass

class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = 0

    def push(self, data):
        if self.top == self.size - 1:
            self.stack[top] = data
            self.top += 1

    def pop(self):
        if not self.is_empty():
            top = self.stack[self.top]
            self.top -= 1
            return top

    def peek:
        pass

    def is_empty(self):
        return self.top == 0
