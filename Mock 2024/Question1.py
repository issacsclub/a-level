# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:10:37 2024

@author: Administrator
"""

#1 (a)
arrayData = [10, 5, 6, 7 , 1,12,13,15,21,8]
#(b) 

def linearSearch(searchValue):
    global arrayData
    for i in range(len(arrayData)):
        if arrayData[i] == searchValue:
            return True
    return False
#(ii)

search =  int(input("Enter a value to search for "))
result = linearSearch(search)
if result == True:
    print("The number was found ")
else:
    print("Not found ")
    
    
#(c)

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

print("The data before sorting ", arrayData)
bubbleSort()
print("Array after sorting ", arrayData)        
            



    