#!/usr/bin/env python3

from nodes import SLLNode

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = SLLNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.next = node
            self.head = node
        self.size += 1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data
                return current
            current = current.next
        raise Exception('no such data is stored in the list')

    def remove(self, data):
        current = self.head
        previous = current
        while self.head == data:
            self.head = self.head.next
        while current:
            if current.data == data
                previous.next = current.next
            previous = current
            current = current.next
        print('no such data is stored in the list')
