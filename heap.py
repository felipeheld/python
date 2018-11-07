#!/usr/bin/env pyhon3


class Heap:

    def __init__(self):
        self.root = None
        self.size = 0

    def _append(self, data):
        node = Node(data)
        current = self.root
        while current:
            
