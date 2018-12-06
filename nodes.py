#!/usr/bin/env python3

class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class DLLNode:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.index = None

class Leaf:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
