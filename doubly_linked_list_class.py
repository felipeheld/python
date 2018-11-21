#!/usr/bin/env python3

from nodes import DoubleLinkNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.sorted = False

    #def _append(self, data):
    #    node = DoubleLinkNode(data)
    #    node.index = self.size
    #    if self.head is None:
    #        self.head = self.tail = node
    #    else:
    #        node.prev = self.tail
    #        self.tail.next = node
    #        self.tail = node
    #    self.size += 1

    def append_indexing(self, data):
        """appends node keeping track of indexes"""
        node = DoubleLinkNode(data)
        if self.head is None:
            self.head = self.tail = node
            node.index = 0
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.index = node.prev.index + 1
        self.size += 1

    #def _remove(self, data):
    #    new_index = 0
    #    if self.head.data == data:
    #        self.head.next.prev = None
    #        self.head = self.head.next
    #        self.size -= 1
    #        print('Item found and removed from list')
    #        return True
    #    elif self.tail.data == data:
    #        self.tail.prev.next = None
    #        self.tail = self.tail.prev
    #        self.size -= 1
    #        print('Item found and removed from list')
    #        return True
    #    else:
    #        current = self.head
    #        while current:
    #            if current.data == data:
    #                current.prev.next = current.next
    #                current.next.prev = current.prev
    #                self.size -= 1
    #                print('Item found and removed from list')
    #                return True
    #            current = current.next
    #    print('Item not found in list')
    #    return True

    def remove_indexing(self, data):
        """removes node updating indexes during traversal"""
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
            current = current.next

    def _pop(self):
        popped = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return popped.data


# test #
#some_list = DoublyLinkedList()
#for i in range(10):
#    some_list._append(i)
#current = some_list.head
#some_list._remove(5)
#some_list._remove(2)
#while current:
#    print(current.data)
#    current = current.next
# test #
