# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:34:21 2024

@author: Support
"""

stack = [None for i in range(10)]

basePointer = 1
topPointer = 0

stackFull = 10

def Push(item):
    global topPointer, stackFull,stack
    if topPointer < stackFull:
        stack[topPointer] = item
        topPointer = topPointer + 1
    else:
        print("The stack is full, cannot push ")
        
Push(2)
Push(45)

for i in range(8):
    Push(56)
    
Push(78)

def Pop():
    global topPointer, basePointer, stack
    if topPointer == basePointer - 1:
        print("The stack is empty, cannot pop")
    else:
        topPointer = topPointer -1 
        stack[topPointer] = None
        
        
Pop()
for i in range(9):
    Pop()
Pop()
