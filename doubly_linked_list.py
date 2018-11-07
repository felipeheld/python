#!/usr/bin/env python3

from nodes import DoubleLinkedNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __append(self, data):
        node = DoubleLinkNode(data)
        if self.head = None:
            self.head = self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.size += 1

    def __search(self, data):
        current = self.tail
        while current:
            if current.data == data:
                return current
            current = current.next

    def __remove(self, data):
        current = self.tail
        while current:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return None
            print('no such data is stored in the list')
