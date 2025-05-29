# -*- coding: utf-8 -*-
"""
Created on Wed May 28 11:44:37 2025

@author: Support
"""

queue = [None for i in range(10)]

frontPointer = 0
rearPointer = -1
queueFull = 10
queLength = 0
item= None

def Enqueue(item):
    global queLength, rearPointer, queue
    
    if queLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queLength = queLength + 1
        queue[rearPointer] = item
    else:
        
        print("Queue is full, cannot enqueue")
        
Enqueue(27)
Enqueue(34)
Enqueue(25)
Enqueue(17)
Enqueue(44)
Enqueue(15)
Enqueue(57)
Enqueue(54)
Enqueue(55)

Enqueue(2)
Enqueue(7)

def DeQueue():
    global queue, frontPointer, queLength, queueFull, item
    if queLength == 0:
        print("The queue is empty, cannot dequeue")
    else:
        queue[frontPointer] = item
        if frontPointer == len(queue)-1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queLength = queLength - 1

DeQueue()