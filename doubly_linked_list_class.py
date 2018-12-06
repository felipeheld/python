#!/usr/bin/env python3

from nodes import DLLNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """appends node keeping track of indexes"""
        node = DLLNode(data)
        if self.head is None:
            self.head = self.tail = node
            self.head.index = 0
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.index = node.prev.index + 1
        self.size += 1

    def remove(self, data):
        """removes every matching node, updating indexes during traversal"""
        # clears both ends of the list in case their data needs removing
        while self.head.data == data:
            if self.size > 1:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = self.tail = None
            self.size -= 1
        while self.tail.data == data:
            if self.size > 1:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.tail = self.head = None
            self.size -= 1
        # traversal begins, updating indexes from 0
        # traversal starts at second node, since the 'head' end has already been cleared
        self.head.index = 0
        current = self.head.next
        while current:
            current.index = current.prev.index + 1
            if current.data == data:
                current.prev.next, current.next.prev = current.next, current.prev
                self.size -= 1
            current = current.next

    def pop(self):
        """returns and removes last element of the list"""
        popped = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1
        return popped.data

    def search_value_by_index(self, index):
        """returns the matching index data"""
        current = self.head
        while current:
            if current.index == index:
                return current.data
            current = current.next
        return False

    def search_index_by_value(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.index
            current = current.next

# auxiliary functions - start
    def print_list(self, with_indexes = False):
        """set with_indexes to True to print list with accompanying indexes"""
        current = some_list.head
        if with_indexes:
            while current:
                print("{} - {}".format(current.data, current.index))
                current = current.next
        else:
            while current:
                print(current.data)
                current = current.next
# auxiliary functions - end


# test #
some_list = DoublyLinkedList()
print("----- filling -----\n")
for i in range(10):
    some_list.append(i**2)
#some_list._remove(5)
#some_list._remove(2)
some_list.print_list(True)
print(some_list.search_by_index(8))
print("----- removal -----\n")
some_list.remove(16)
print("----- search -----\n")
print(some_list.search_by_index(8))
some_list.print_list(True)
# test #
