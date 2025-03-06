# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:53:03 2025

@author: Support
"""

myList = [5,8,6,4,18,10,15,40,9, 2]

upperBound = 9
lowerBound = 0

item = int(input("Enter the value to be found "))

found = False
index = lowerBound

while index <= upperBound and found==False:
    if item == myList[index]:
        found = True
    index = index + 1
    
if found == True:
    print("Found")
else:
    print("Item not found")