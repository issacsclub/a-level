# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:09:06 2023

@author: Administrator
"""

# Bubble Sort  


myList =  [0,5,10,45,15,19,8,11,13,2] # 
upperBound = 9
lowerBound = 0
top =  upperBound
swap = False

while swap or top > 0:
    swap = False
    for index in range(top):
        if myList[index] > myList[index + 1]:
            temp = myList[index]
            myList[index] = myList[index+1]
            myList[index + 1] = temp
            swap = True
            
    top = top - 1
print(myList)

