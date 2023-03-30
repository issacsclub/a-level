# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:00:41 2023

@author: Administrator
"""

StackArray = [None for i in range(8)]
TopPointer = -1
basePointer = 0
StackFull = 8

item= None



def push(item):
    global TopPointer, StackFull
    if TopPointer< StackFull:
        TopPointer = TopPointer + 1
        StackArray[TopPointer] = item
        return True
    else:
        print("Stack is full ")
        return None
    
push(20)
push(35)
push(43)
push(55)

print(StackArray)

def pop():
    global TopPointer, basePointer
    if TopPointer == basePointer -1:
        print("Stack is empty,cannot pop")
    else:        
        StackArray[TopPointer] = None 
        TopPointer = TopPointer -1
    return StackArray

pop()
    
print(StackArray)   
    
    