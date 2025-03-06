# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:09:08 2025

@author: Support
"""

myList = [70, 46, 43, 27, 57, 41, 45, 21, 14]
lowerBound = 0
upperBound = 8

for index in range(1,9):
    key = myList[index]
    place = index - 1
    if myList[place] > key:
        while place>=lowerBound and myList[place]>key:
            temp = myList[place+1]
            myList[place+1] = myList[place]
            myList[place] = temp
            place=place - 1
            
        myList[place+1]=key