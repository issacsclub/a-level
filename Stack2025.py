# -*- coding: utf-8 -*-
"""
Created on Tue May 27 09:41:55 2025

@author: Support
"""

stack = [None for i in range(10)]
basePointer = 0
topPointer = -1
StackFull = 10
item = None

def Push(item):
    global basePointer, topPointer, stack, StackFull
    
    if topPointer < StackFull-1:
        topPointer = topPointer + 1
        stack[topPointer] = item
        
    else:
        print("The stack is full ")
        
#examples of Pushing Items 

Push(27)
Push(34)
Push(82)
Push(79)

Push(17)
Push(14)
Push(12)
Push(19)
Push(10)
Push(9)

Push(15)


def Pop():
    global topPointer, basePointer, item
    if topPointer == basePointer - 1:
        print("Stack is empty, cannot pop")
    else:
        stack[topPointer] = item
        topPointer = topPointer - 1
        
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()