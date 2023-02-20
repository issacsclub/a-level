# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 07:44:07 2023

@author: Administrator
"""

# Initialize Stacks

stack =  [None for i in range(10)]

topPointer = -1
basePointer = 0
stackFull = 10

item = None


#  Push

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
    else:
        print("Stack is full, cannot push")
        
# Test the code

push(4)
push(5)
push(8)


# pop 

def pop():
    global topPointer, basePointer
    if topPointer == basePointer -1:
        print("Stack is empty,cannot pop")
    else:        
        stack[topPointer] = None 
        topPointer = topPointer -1
    return stack
pop()    
pop()
pop()
pop()



