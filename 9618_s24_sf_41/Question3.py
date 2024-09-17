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
Enqueue(12)
Enqueue(45)