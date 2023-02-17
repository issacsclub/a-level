# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:34:29 2023

@author: Administrator
"""

# Question 1 (a)
TheData =  [20,3,4,8,12,99,4,26,4]

# 1 (b)
def InsertionSort(TheData):
    for count in range(0,len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count -1 
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue+ 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] =  DataToInsert
            else:
                Inserted = 1 
                
# 1 (c)
def PrintArray(TheData):
    for count in range(0, len(TheData)):
        print(TheData[count])
        
# 1 (d)
print("The data before sorting ")
PrintArray(TheData)
InsertionSort(TheData)
print("The data after sorting ")
PrintArray(TheData)

#1 (e)

def Search(number):
    for i in range(len(TheData)):
        
        if number == TheData[i]:
            print("Found")
            return True
    else:
        print("Not found")
        return False