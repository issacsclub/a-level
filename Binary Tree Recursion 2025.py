# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 16:02:44 2025

@author: Support
"""

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item     

    def insert(self, item):
        if self.item is not None:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item
              
    def search(self, item):
        current = self
        while current is not None:
            if current.item == item:
                return current.item
            elif item < current.item:
                current = current.left
            else:
                current = current.right
        return None

# Create root node and populate with values
root = Node(27)
root.insert(19)
root.insert(36)
root.insert(42)
root.insert(16)




print(root.left.item)

