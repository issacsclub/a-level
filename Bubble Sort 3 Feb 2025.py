# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:32:06 2025

@author: Support
"""

myList = [70,46,43,27,57,41,45,21,14]

lowerBound = 0
upperBound = 8

top = upperBound

swap = True
while swap == True or top > 0:  
    swap = False
    for index in range(0,top):
        if myList[index]>myList[index+1]:
            temp = myList[index]
            myList[index] = myList[index+1]
            myList[index+1] = temp           
            swap= True
    top = top - 1
    