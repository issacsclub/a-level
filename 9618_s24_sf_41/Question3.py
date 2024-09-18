# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:29:32 2024

@author: Support
"""

global QueueData
global QueueHead
global QueueTail
QueueData = ["" for i in range(20)]
QueueHead = -1
QueueTail = -1


    
def Enqueue(DataToInsert):
    global QueueData
    global QueueHead
    global QueueTail
    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0
    QueueTail = QueueTail + 1
    QueueData[QueueTail] = DataToInsert
    return True


def Dequeue():
    global QueueHead
    global QueueTail
    global QueueData
    
    if QueueHead < 0:
        return False
    else:
        QueueHead = QueueHead +1
    
        return QueueData[QueueHead-1]


def StoreItems():
    
    global QueueHead,QueueTail, QueueData
    invalidCount = 0
    for i in range(10):
        string = input("Enter the first string ")
        total = int(string[0])*1 + int(string[1])*3 + int(string[2])*1+int(string[3])*3 + int(string[4])*1 + int(string[5])*3
        total = int(total / 10) 
        if total==int(string[6]) or tota
    
    
    
    
    
    
    
    
    
Enqueue(45)
Enqueue(5)
Enqueue(4)

nextValue = Dequeue()
print("The next value ", nextValue)


