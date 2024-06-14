# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:33:12 2023

@author: Support
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 08:04:21 2023

@author: Administrator
"""

# Define the list first 
# DECLARE myList: ARRAY[0:9] OF INTEGER
myList = [2,3,4,7,8,9,12,17,21,34]

upperBound = 9
lowerBound = 0

item = int(input("Enter an item to search for "))

found = False
counter = 0

while found==False and counter <= 9:
    index = int((lowerBound + upperBound)/2)
    if item == myList[index]:
        found = True
        
    if item > myList[index]:
        lowerBound = index + 1
        
    if item < myList[index]:
        upperBound = index -1
        
    counter = counter + 1
if found == True:
    print("Found at index ", index)
else:
    print("Not found")
        
        