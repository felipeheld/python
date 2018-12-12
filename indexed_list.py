#!/usr/bin/env python3

class Node:

    def __init__(self, index):
        self.index = index
        self.jump_100 = None
        self.jump_50 = None
        self.jump_10 = None
        self.nextNode = None
        self.prevNode = None


class IndexedList:
    # this list does not contain duplicate elements (every index is unique)

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.indexed = False

    def insert(self, index):
        """inserts a node in the list in order"""
        self.indexed = False
        node = Node(index)
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
        elif self.tail.index < index:
            node.prevNode = self.tail
            self.tail.nextNode = node
            self.tail = node
            self.size += 1
        elif self.head.index > index:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.jump_100 and current.jump_100.index <= index:
                current = current.jump_100
            while current.jump_50 and current.jump_50.index <= index:
                current = current.jump_50
            while current.jump_10 and current.jump_10.index <= index:
                current = current.jump_10
            while current.nextNode and current.nextNode.index <= index:
                current = current.nextNode
            if current.index == index:
                raise Exception('a node with same index as argument already exists in the list')
            #if current == self.head:
            if current.index > index:
                current.prevNode = node
                node.nextNode = current
                self.head = node
            elif current == self.tail:
                current.nextNode = node
                node.prevNode = current
                self.tail = node
            else:
                node.nextNode = current.nextNode
                node.nextNode.prevNode = node
                node.prevNode = current
                current.nextNode = node
        self.size += 1

    def search(self, index):
        """searches for a node with the specified index within the list and returns it if found"""
        if not self.empty():
            if not self.indexed:
                self.re_index()
            current = self.head
            while current.jump_100 and current.jump_100.index <= index:
                current = current.jump_100
            while current.jump_50 and current.jump_50.index <= index:
                current = current.jump_50
            while current.jump_10 and current.jump_10.index <= index:
                current = current.jump_10
            while current.nextNode and current.nextNode.index <= index:
                current = current.nextNode
            if current.index == index:
                return current.index
            else:
                raise Exception('List does not contain any node with argument index')
        else:
            raise Exception('Cannot perform search on empty list')

    def remove(self, index):
        # fix the jumping problem when indexes are jump indexes
        """removes from the list the node with specified index"""
        if not self.empty():
            self.indexed = False
            current = self.head
            last_jump_100 = None
            last_jump_50 = None
            last_jump_10 = None
            if current is not self.head and current is not self.tail:
                if current.jump_100:
                    last_jump_100 = current
                    while current.jump_100 and current.jump_100.index < index:
                        current = current.jump_100
                        last_jump_100 = current
                if current.jump_50:
                    last_jump_50 = current
                    while current.jump_50 and current.jump_50.index < index:
                        current = current.jump_50
                        last_jump_50 = current
                if current.jump_10:
                    last_jump_10 = current
                    while current.jump_10 and current.jump_10.index < index:
                        current = current.jump_10
                        last_jump_10 = current
            while current.nextNode and current.nextNode.index <= index:
                current = current.nextNode
            if current.index == index:
                if current == self.head == self.tail:
                    self.head = self.tail = None
                elif current == self.head:
                    current.nextNode.jump_100 = current.jump_100 if not current.nextNode.jump_100 else current.nextNode.jump_100
                    current.nextNode.jump_50 = current.jump_50 if not current.nextNode.jump_50 else current.nextNode.jump_50
                    current.nextNode.jump_10 = current.jump_10 if not current.nextNode.jump_10 else current.nextNode.jump_10
                    self.head = current.nextNode
                    self.head.prevNode = None
                elif current == self.tail:
                    if last_jump_100:
                        if last_jump_100 is current.prevNode:
                            last_jump_100.jump_100 = None
                        last_jump_100.jump_100 = current.prevNode if last_jump_100.jump_100 == current else last_jump_100.jump_100
                    if last_jump_50:
                        if last_jump_50 is current.prevNode:
                            last_jump_50.jump_50 = None
                        last_jump_50.jump_50 = current.prevNode if last_jump_50.jump_50 == current else last_jump_50.jump_50
                    if last_jump_10:
                        if last_jump_10 is current.prevNode:
                            last_jump_10.jump_10 = None
                        last_jump_10.jump_10 = current.prevNode if last_jump_10.jump_10 == current else last_jump_10.jump_10
                    self.tail = current.prevNode
                    self.tail.nextNode = None
                else:
                    if last_jump_100 and last_jump_100.jump_100 == current:
                        last_jump_100.jump_100 = current.nextNode
                        if current.jump_100 and not current.nextNode.jump_100:
                            current.nextNode.jump_100 = current.jump_100
                    if last_jump_50 and last_jump_50.jump_50 == current:
                        last_jump_50.jump_50 = current.nextNode
                        if current.jump_50 and not current.nextNode.jump_50:
                            current.nextNode.jump_50 = current.jump_50
                    if last_jump_10 and last_jump_10.jump_10 == current:
                        last_jump_10.jump_10 = current.nextNode
                        if current.jump_10 and not current.nextNode.jump_10:
                            current.nextNode.jump_10 = current.jump_10
                    current.prevNode.nextNode = current.nextNode
                    current.nextNode.prevNode = current.prevNode
                self.size -= 1
            else:
                raise Exception('List contains no node with argument index')
        else:
            raise Exception('Cannot perform removal on empty list')

    def re_index(self):
        self.indexed = True
        current = self.head
        last_jump_100 = current
        last_jump_50 = current
        last_jump_10 = current
        position = 1
        while current:
            if position % 10 == 0:
                last_jump_10.jump_10 = current
                last_jump_10 = current
            else:
                last_jump_10.jump_10 = None
            if position % 50 == 0:
                last_jump_50.jump_50 = current
                last_jump_50 = current
            else:
                last_jump_50.jump_50 = None
            if position % 100 == 0:
                last_jump_100.jump_100 = current
                last_jump_100 = current
            else:
                last_jump_100.jump_100 = None
            current = current.nextNode
            position += 1

    def empty(self):
        return self.size == 0

    def iterator(self):
        current = self.head
        while current:
            print('index: {}, jump_100: {}, jump_50: {}, jump_10: {}'.format(current.index, current.jump_100.index if current.jump_100 else None, current.jump_50.index if current.jump_50 else None, current.jump_10.index if current.jump_10 else None))
            current = current.nextNode

# tests

lista = IndexedList()
#lista.insert(50)
#lista.insert(49)
#lista.insert(65)
#lista.insert(67)
#lista.insert(66)
#lista.insert(12)
#for i in range(1,121):
#    lista.insert(i)
#lista.search(50)
#for i in range(2,120):
#    lista.remove(i)
#
#lista.remove(1)
#print(lista.head.index)
#print(lista.tail.index)
#lista.remove(120)
#print(lista.empty())
#lista.iterator()
for i in range(1, 10000):
    lista.insert(i)

print(lista.search(992))
lista.iterator()
#print(lista.search(993))
#print(lista.search(667))
#print(lista.search(113))
