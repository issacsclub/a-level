# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:09:51 2024

@author: Form 6.1
"""

class node:
    def __init__(self, item):
        self.item = item
        self.leftPointer = -1
        self.rightPointer = -1
        self.oldPointer = 0
        self.leftBranch = True

nullPointer = -1
myTree = [node(None) for i in range(12)]
rootPointer = nullPointer
nextFreePointer = 0

def nodeAdd(itemAdd):
    global rootPointer, nextFreePointer, myTree
    
    if nextFreePointer == nullPointer:
        print("No nodes free")
    else:
        itemAddPointer = nextFreePointer
        nextFreePointer += 1  # Move to the next free pointer
        itemPointer = rootPointer
        oldPointer = nullPointer  # Initialize oldPointer
        leftBranch = True  # Initialize leftBranch
        
        if itemPointer == nullPointer:
            rootPointer = itemAddPointer
        else:
            while itemPointer != nullPointer:
                oldPointer = itemPointer
                if myTree[itemPointer].item > itemAdd:
                    leftBranch = True
                    itemPointer = myTree[itemPointer].leftPointer
                else:
                    leftBranch = False
                    itemPointer = myTree[itemPointer].rightPointer
            
            if leftBranch:
                myTree[oldPointer].leftPointer = itemAddPointer
            else:
                myTree[oldPointer].rightPointer = itemAddPointer
    
        myTree[itemAddPointer].leftPointer = nullPointer
        myTree[itemAddPointer].rightPointer = nullPointer
        myTree[itemAddPointer].item = itemAdd
