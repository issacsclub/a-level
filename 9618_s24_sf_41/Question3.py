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




def DeQueue():
    global QueueHead, QueueTail, QueueData
    if QueueHead < 0 or QueueHead > QueueTail:
        return False
    else:
        QueueHead = QueueHead + 1
        return QueueData[QueueHead - 1]
    
# (d) (i)

def StoreItems():
    
    global QueueData, QueueHead, QueueTail
    InvalidCount = 0
    for i in range(10):
        string = input("Enter the string ")
        total =  int(string[0])*1 + int(string[1])*3 +int(string[2])*1+int(string[3])*3+int(string[4])*1+int(string[5])*3
        total = int(total /10)
        if (total == 10 and string[6] == "X") or (total == int(string[6])):
            result = Enqueue(string[:5])
            if result == True:
                print("The string was succesfully inserted! ")
            else:
                print("The Queue is full")
        else:
            InvalidCount += 1
            
    print("There were ", InvalidCount, " invalid items")
            

            
            
                
        