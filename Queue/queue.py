# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:30:55 2024

@author: Support
"""

queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0


def enqueue(item):
    global queueLength, rearPointer, queueFull
    if queueLength < queueFull:
        if rearPointer < queueFull - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
            
        queueLength = queueLength + 1
        queue[rearPointer] = item
    else:
        print(" Queue is full, cannot enque")
        
enqueue(45)
       
        
def deQueue():
    global queueLength, frontPointer
    if queueLength == 0:
        print(" The queue is empty, cannot pop  ")
        
    else:
        queue[frontPointer] = None
        if frontPointer == len(queue) - 1:
            frontPointer = 0
    queueLength = queueLength - 1
        
deQueue()


