#!/usr/bin/env python3

from node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.sorted = False

    def _append(self, data):
        node = Node(data)
        node.index = self.size
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def _remove(self, data):
        new_index = 0
        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next
            self.size -= 1
            print('Item found and removed from list')
            return True
        elif self.tail.data == data:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
            print('Item found and removed from list')
            return True
        else:
            current = self.head
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    print('Item found and removed from list')
                    return True
                current = current.next
        print('Item not found in list')
        return True

    def _pop(self):
        popped = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return popped.data


# test #
some_list = DoublyLinkedList()
for i in range(10):
    some_list._append(i)
current = some_list.head
some_list._remove(5)
some_list._remove(2)
while current:
    print(current.data)
    current = current.next
# test #
