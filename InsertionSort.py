# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:54:12 2023

@author: Administrator
"""

myList = [5,8,7,2,4,3,9,10]
lowerBound = 0
upperBound = 7
for i in range(1, len(myList)):
    key = myList[i]
    place = i - 1
    if myList[place] > key:
        while place >= lowerBound and myList[place] > key:
            temp = myList[place+1]
            myList[place + 1] = myList[place]
            myList[place] = temp
            place = place - 1
        myList[place+1] = key
print(myList)