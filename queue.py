#!/usr/bin/env python3

from nodes import SLLNode

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = SLLNode(data)
        if self.head is not None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is not None:
            data = head.data
            head = head.next
            self.size -= 1
            return data
        else:
            raise Exception('Queue is empty')

    def peek(self):
        if self.head is not None:
            return head.data
        else:
            raise Exception('Queue is empty')

    def isempty(self):
        return self.size == 0
