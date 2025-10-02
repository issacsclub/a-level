# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:20:35 2025

@author: Support
"""
# define class Node
class Node:
    def __init__(self, item):
      self.left = None
      self.right = None
      self.item = item     


    def insert(self, item):
        if self.item:
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
      while self.item != item:
        if item < self.item:
          self.item = self.left
        else:
          self.item = self.right
        if self.item is None:
            return None
      return self.item
  
    
root = Node(27)

root.insert(19)
root.insert(36)
root.insert(42)
root.insert(16)

print(root.search(16))