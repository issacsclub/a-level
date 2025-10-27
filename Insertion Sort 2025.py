# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:09:08 2025

@author: Support
"""

myList = [70, 46, 43, 27, 57, 41, 45, 21, 14]
print("My list", myList)
lowerBound = 0
print("LowerBound", lowerBound)
upperBound = 8
print("UpperBound", upperBound)
for index in range(1,9):
    print("Index", index)
    key = myList[index]
    print("Key", key)
    place = index - 1
    print("Place", place)
    if myList[place] > key:
        while place>=lowerBound and myList[place]>key:
            temp = myList[place+1]
            myList[place+1] = myList[place]
            myList[place] = temp
            place=place - 1
            
        myList[place+1]=key
    print("My List ", myList)