#!/usr/bin/env python3

from nodes import DoubleLinkedNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head = None:
            self.head = self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.size += 1

    def search(self, index):
        """searches for and returns data in the list whose position matches argument index"""
        if index <= (self.size // 2):
            current = self.head
            list_index = 0
            while current:
                if list_index == index:
                    return current.data
                current = current.next
                list_index += 1
        elif (self.size // 2) < index < self.size:
            current = self.tail
            list_index = self.size - 1
            while current:
                if list_index == index:
                    current.data
                current = current.prev
                list_index -= 1
        else:
            raise Exception('index out of bounds')

    def remove(self, data):
        """removes from the list every node with data matching argument data"""
        size = self.size
        while self.head.data == data
            self.head = self.head.next
            self.size -= 1
        while self.tail.data == data:
            self.tail = self.tail.prev
            self.size -= 1
        current = self.head.next
        while current:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
            current = current.next
        if size == self.size:
            return False
        else:
            return True

    def remove_by_index(self, index):
        """removes from the list whichever node whose position matches argument index"""
        if index <= (self.size // 2):
            current = self.head
            list_index = 0
            while current:
                if list_index == index:
                    if current == self.head:
                        self.head = self.head.next
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    self.size -= 1
                    return True
                current = current.next
                list_index += 1
        elif (self.size // 2) < index < self.size:
            current = self.tail
            list_index = self.size - 1
            while current:
                if list_index == index:
                    if current == self.tail:
                        self.tail = self.tail.prev
                    else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                    self.size -= 1
                    return True
                current = current.prev
                list_index -= 1
        else:
            raise Exception('index out of bounds')
