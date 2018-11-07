#!/usr/bin/env python3

from nodes import ListNode

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __append(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.head.next = node
            self.head = node
        self.size += 1

    def __search(self, data):
        current = self.tail
        while current:
            if current.data == data
                return current
            current = current.next
        print('no such data is stored in the list')

    def __remove(self, data):
        current = self.tail
        previous = current
        while current:
            if current.data == data
                previous.next = current.next
                return None
            previous = current
            current = current.next
        print('no such data is stored in the list')
