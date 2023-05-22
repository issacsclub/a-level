# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:33:21 2023

@author: Administrator
"""

queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0

item = None


# inserting items in a queue
def enQueue(item):
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        queue[rearPointer] = item
    else:
        print("Queue is full, cannot enqueue")

        
# Test enqueue procedure      
enQueue(8)
enQueue(5)
enQueue(3)
enQueue(7)
enQueue(6)
enQueue(4)
enQueue(10)
enQueue(12)
enQueue(15)
enQueue(80)

# deleting items
def deQueue():
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("Queue is empty,cannot dequeue")
    else:
        queue[frontPointer] = item
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queueLength = queueLength -1


