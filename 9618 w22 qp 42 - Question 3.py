# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:13:56 2023

@author: Administrator
"""
#3 (a)
queue = [None for i in range(0,100)]
headPointer = -1
tailPointer = 0


#3 (b)
def enQueue(Data):
    global headPointer, tailPointer
    if(tailPointer < 100):
        if headPointer == -1:
            headPointer = 0
        queue[tailPointer] = Data
        tailPointer = tailPointer + 1
        return True
    return False
# 3c         
for i in range(1,21):
    success = enQueue(i)
    if success == True:
        print(i, "successfully added ")
        
    else:
        print("Unsuccessful")