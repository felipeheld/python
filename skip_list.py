#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.below = None
        self.above = None

class SkipList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def search(self, data):
        current = self.head
        while current.below is not None:
            current = current.below
            while current.next.data < data:
                current = current.next
        return current.data if current.data == data else False
