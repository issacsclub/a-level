# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 08:17:58 2024

@author: Support
"""

class Node:
    def __init__(self, item=None, left_pointer=None, right_pointer=None):
        self.item = item
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer
        
# Constants
null_pointer = -1

# Initialize tree and pointers
my_tree = [Node(None) for i in range(12)]
root_pointer = null_pointer
next_free_pointer = 0


def node_add(item_add):
    global root_pointer, next_free_pointer
    if next_free_pointer == null_pointer:
        print("No nodes free")
        
    item_add_pointer = next_free_pointer
    next_free_pointer = my_tree[next_free_pointer].left_pointer
    item_pointer = root_pointer
    if item_pointer == null_pointer:
        root_pointer = item_add_pointer
    else:
        while item_pointer != null_pointer:
            old_pointer = item_pointer
            if my_tree[item_pointer].item > item_add:
                left_branch = True
                item_pointer = my_tree[item_pointer].left_pointer
            else:
                left_branch = False
                item_pointer = my_tree[item_pointer].right_pointer
        if left_branch:
            my_tree[old_pointer].left_pointer = item_add_pointer
        else:
            my_tree[old_pointer].right_pointer = item_add_pointer
    my_tree[item_add_pointer].left_pointer = null_pointer
    my_tree[item_add_pointer].right_pointer = null_pointer
    my_tree[item_add_pointer].item = item_add


# Example usage

