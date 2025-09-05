# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 15:17:54 2025

@author: Support
"""
#1 (a)
arrayData = [10,5,6,7,1,12,13,15,21,8]

#1 (b) (i)

def linearSearch(SearchValue):
    
    #global arrayData
    
    for i in range(len(arrayData)):
        if arrayData[i] == SearchValue:
            return True
        
    return False


number = int(input("Enter a vale to search for "))
result = linearSearch(number)
if result == True:
    print("The number was found ")
else:
    print("The number was not found")
    
    
#(c)

def bubbleSort():
    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1]= temp
print("Array data before sorting")
print (arrayData)

bubbleSort()
print("Array data after sorting")
print (arrayData)


    
    

    





